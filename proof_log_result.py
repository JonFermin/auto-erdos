"""proof_log_result.py — sole gatekeeper for the Track 2 proof loop.

Parallel to ``log_result.py`` for the search loop. The agent runs:

    uv run proof_log_result.py "thesis: stratify by Omega(a) and bound..."

Everything else is computed by the harness from state on disk:

  1. Compute content-hash of ``proof_strategy.md`` (strips HTML comments
     except ``<!-- WITNESS -->``, collapses whitespace, lowercases, sha256).
     Look up against ``~/.cache/auto-erdos/proof_trial_cache_<tag>.tsv``.
     Hash already seen on any branch ⇒ exit 3.
  2. Count rows in ``proof_results.tsv`` against ``round_cap`` (default 50,
     per-problem override ``proofs/<tag>.json:round_cap``). Cap reached ⇒
     exit 4.
  3. Look up the current commit's verdict in ``proof_verifier_results.tsv``.
     No row ⇒ ``proof_prepare.py`` never reached print_summary ⇒ exit 5.
  4. Apply the keep rule:
        witness_valid==1                                        ⇒ keep_disproof
        critic_blocking==0 AND verdict in {partial_result,open} ⇒ keep_progress
        else                                                    ⇒ discard
  5. Write the row to ``proof_results.tsv``; append to shared cache;
     write a record file on keeps; auto-commit the record.
  6. Compute terminal-condition exits:
        keep_disproof    ⇒ exit 7 (counterexample — stop the loop, summarize)
        converged        ⇒ exit 6 (clean critics, content-hash unchanged
                            for 3 checkpoints, no open qids ⇒ done)
        otherwise        ⇒ exit 0 (advance / discard, loop continues)

Exit codes:
  0 — row logged; ``status=keep_progress|discard`` on stdout's last line
  2 — description invalid (missing 'thesis: ' or contains tab/newline)
  3 — proof_hash duplicate of a prior round on this problem (any branch)
  4 — round cap reached on this branch — stop the loop
  5 — verifier crash (no proof_verifier_results.tsv row for this commit)
  6 — converged: clean critics + stable content + no open qids — done
  7 — counterexample proven: keep_disproof — stop the loop and re-verify
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import platform
import re
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

# Track 2 imports — keep separate from prepare.* to leave Track 1 untouched.
from proof_prepare import (
    PROOF_TAG,
    PROOF_VERIFIER_RESULTS_TSV,
    REPO_ROOT,
    _proof_hash,
    load_proof_spec,
)

if platform.system() == "Windows":
    import msvcrt
else:
    import fcntl  # type: ignore[unused-ignore]

PROOF_RESULTS_TSV = REPO_ROOT / "proof_results.tsv"
PROOF_STRATEGY_MD = REPO_ROOT / "proof_strategy.md"
PROOF_OPEN_QUESTIONS = REPO_ROOT / "proof_open_questions.jsonl"
HEADER = [
    "commit", "claim_status", "witness_valid", "witness_score",
    "critic_blocking", "critic_warn", "verdict_hint", "verifier_seconds",
    "proof_hash", "status", "description",
]

_CACHE_DIR = Path.home() / ".cache" / "auto-erdos"
CACHE_HEADER = [
    "proof_hash", "branch_tag", "commit", "verdict_hint",
    "status", "written_at",
]

DEFAULT_ROUND_CAP = 50
ROUND_CAP = int(os.environ.get("AUTOERDOS_ROUND_CAP", str(DEFAULT_ROUND_CAP)))

RECORDS_DIR = REPO_ROOT / "records"

# Convergence parameters: how many consecutive checkpoints with no content
# change before we declare "stable". The plan called for 3.
STABLE_CHECKPOINT_COUNT = 3


# --------------------------------------------------------------------------- #
# Git helpers (duplicated from log_result.py — Track 1 stays untouched)
# --------------------------------------------------------------------------- #

def _short_commit() -> str:
    out = subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "--short=7", "HEAD"],
        stderr=subprocess.DEVNULL,
    )
    return out.decode().strip()


def _current_branch_tag() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return "unknown"
    branch = out.decode().strip()
    prefix = "erdos-proof/"
    return branch[len(prefix):] if branch.startswith(prefix) else (branch or "unknown")


# --------------------------------------------------------------------------- #
# Per-problem proof-hash cache (shared across branches)
# --------------------------------------------------------------------------- #

def _cache_path() -> Path:
    return _CACHE_DIR / f"proof_trial_cache_{PROOF_TAG}.tsv"


def _resolve_round_cap(spec: dict) -> int:
    env = os.environ.get("AUTOERDOS_ROUND_CAP")
    if env is not None:
        return int(env)
    return int(spec.get("round_cap", DEFAULT_ROUND_CAP))


@contextmanager
def _cache_lock(path: Path, *, exclusive: bool):
    path.parent.mkdir(parents=True, exist_ok=True)
    mode = "a+" if exclusive else "r"
    f = open(path, mode, encoding="utf-8", newline="")
    try:
        if platform.system() == "Windows":
            f.seek(0)
            msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
        else:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
        yield f
    finally:
        try:
            if platform.system() == "Windows":
                try:
                    f.seek(0)
                    msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
                except OSError:
                    pass
            else:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        finally:
            f.close()


def _read_cache() -> pd.DataFrame:
    path = _cache_path()
    if not path.exists() or path.stat().st_size == 0:
        return pd.DataFrame(columns=CACHE_HEADER)
    try:
        with _cache_lock(path, exclusive=False) as f:
            f.seek(0)
            df = pd.read_csv(
                f, sep="\t",
                dtype={c: str for c in CACHE_HEADER},
            )
    except (pd.errors.EmptyDataError, OSError):
        return pd.DataFrame(columns=CACHE_HEADER)
    except pd.errors.ParserError as e:
        print(
            f"WARNING: proof-trial cache at {path} malformed ({e}); "
            f"dedup disabled for this run.",
            file=sys.stderr,
        )
        return pd.DataFrame(columns=CACHE_HEADER)
    for col in CACHE_HEADER:
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    return df


def _append_cache(
    proof_hash: str,
    branch_tag: str,
    commit: str,
    verdict_hint: str,
    status: str,
) -> None:
    path = _cache_path()
    written_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    row = [proof_hash, branch_tag, commit, verdict_hint, status, written_at]
    with _cache_lock(path, exclusive=True) as f:
        f.seek(0, os.SEEK_END)
        if f.tell() == 0:
            f.write("\t".join(CACHE_HEADER) + "\n")
        f.write("\t".join(row) + "\n")
        f.flush()
        os.fsync(f.fileno())


def _find_cache_duplicate(
    cache_df: pd.DataFrame, proof_hash: str, current_commit: str
) -> tuple[str, str] | None:
    if cache_df.empty or "proof_hash" not in cache_df.columns:
        return None
    hits = cache_df[cache_df["proof_hash"] == proof_hash]
    if "commit" in hits.columns:
        hits = hits[hits["commit"] != current_commit]
    if hits.empty:
        return None
    row = hits.iloc[0]
    return (str(row.get("branch_tag", "unknown")), str(row.get("commit", "")))


# --------------------------------------------------------------------------- #
# proof_results.tsv I/O
# --------------------------------------------------------------------------- #

def _read_results_tsv() -> pd.DataFrame:
    if not PROOF_RESULTS_TSV.exists() or PROOF_RESULTS_TSV.stat().st_size == 0:
        return pd.DataFrame(columns=HEADER)
    try:
        df = pd.read_csv(
            PROOF_RESULTS_TSV, sep="\t",
            dtype={c: str for c in HEADER},
        )
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=HEADER)
    for col in ("witness_valid", "critic_blocking", "critic_warn", "witness_score", "verifier_seconds"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _append_results_row(row: dict) -> None:
    needs_header = (
        not PROOF_RESULTS_TSV.exists() or PROOF_RESULTS_TSV.stat().st_size == 0
    )
    fields = [str(row.get(c, "")) for c in HEADER]
    with open(PROOF_RESULTS_TSV, "a", encoding="utf-8", newline="") as f:
        if needs_header:
            f.write("\t".join(HEADER) + "\n")
        f.write("\t".join(fields) + "\n")
    print(f"logged: {fields[0]}\t{fields[6]}\t{fields[9]}\t{fields[10]}")
    print(f"status={fields[9]}")


# --------------------------------------------------------------------------- #
# Verifier audit lookup
# --------------------------------------------------------------------------- #

def _read_verifier_log() -> pd.DataFrame:
    if not PROOF_VERIFIER_RESULTS_TSV.exists() or PROOF_VERIFIER_RESULTS_TSV.stat().st_size == 0:
        return pd.DataFrame()
    try:
        df = pd.read_csv(PROOF_VERIFIER_RESULTS_TSV, sep="\t", dtype=str)
    except pd.errors.EmptyDataError:
        return pd.DataFrame()
    for col in ("witness_valid", "critic_blocking", "critic_warn", "witness_score", "verifier_seconds"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _latest_verifier_row(commit: str, problem: str, df: pd.DataFrame) -> pd.Series | None:
    if df.empty or "commit" not in df.columns:
        return None
    matches = df[df["commit"] == commit]
    if "problem" in matches.columns:
        matches = matches[matches["problem"] == problem]
    if matches.empty:
        return None
    return matches.iloc[-1]


# --------------------------------------------------------------------------- #
# Records (parallel to log_result._write_record)
# --------------------------------------------------------------------------- #

def _write_record(
    commit: str,
    *,
    proof_hash: str,
    proof_md: str,
    spec: dict,
    branch_tag: str,
    desc: str,
    verifier_row: pd.Series,
    record_kind: str,
) -> Path | None:
    """Write a kept proof attempt to records/proof_<tag>_<short_hash>.json.

    Auto-commits as a follow-up commit (never undoes a kept record on
    commit failure — bookkeeping never loses real results).
    """
    tag = spec.get("name", PROOF_TAG)
    short_hash = proof_hash[:12]
    filename = f"proof_{tag}_{short_hash}_{commit}.json"
    path = RECORDS_DIR / filename

    # Optional witness payload.
    witness_payload: dict | None = None
    try:
        from proof_prepare import extract_witness_payload
        witness_payload = extract_witness_payload(proof_md)
    except Exception:  # noqa: BLE001
        witness_payload = None

    record = {
        "kind": record_kind,
        "problem": tag,
        "family": spec.get("family", ""),
        "track": "proof",
        "claim_status": spec.get("claim_status", "unknown"),
        "claim_latex": spec.get("claim_latex", ""),
        "witness_valid": int(verifier_row.get("witness_valid", 0) or 0),
        "witness_score": _safe_float(verifier_row.get("witness_score")),
        "witness_payload": witness_payload,
        "critic_blocking_count": int(verifier_row.get("critic_blocking", 0) or 0),
        "critic_warn_count": int(verifier_row.get("critic_warn", 0) or 0),
        "verdict_hint": str(verifier_row.get("verdict_hint", "")),
        "verifier_seconds": _safe_float(verifier_row.get("verifier_seconds")),
        "proof_hash": proof_hash,
        "proof_md": proof_md,
        "commit": commit,
        "branch": f"erdos-proof/{branch_tag}",
        "thesis": desc,
        "written_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    try:
        RECORDS_DIR.mkdir(parents=True, exist_ok=True)
        if path.exists():
            print(
                f"WARNING: record {filename} already exists; refusing to overwrite.",
                file=sys.stderr,
            )
            return None
        with open(path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, sort_keys=True)
            f.write("\n")
    except OSError as e:
        print(f"WARNING: failed to write record {filename}: {e}", file=sys.stderr)
        return None

    rel = path.relative_to(REPO_ROOT).as_posix()
    try:
        subprocess.check_call(
            ["git", "-C", str(REPO_ROOT), "add", rel],
            stderr=subprocess.DEVNULL,
        )
        subprocess.check_call(
            ["git", "-C", str(REPO_ROOT), "commit", "-m",
             f"proof_record: {tag} {record_kind} ({branch_tag})"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"record: committed {rel}", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(
            f"WARNING: record {rel} written but auto-commit failed ({e}). "
            f"It is staged/untracked and can be committed by hand.",
            file=sys.stderr,
        )
    return path


def _safe_float(v) -> float:
    try:
        f = float(v)
        if not math.isfinite(f):
            return 0.0
        return f
    except (TypeError, ValueError):
        return 0.0


# --------------------------------------------------------------------------- #
# Convergence detection
# --------------------------------------------------------------------------- #

def _live_open_question_count() -> int:
    """Count qids whose most-recent row has status in {open, released}."""
    if not PROOF_OPEN_QUESTIONS.exists() or PROOF_OPEN_QUESTIONS.stat().st_size == 0:
        return 0
    latest: dict[str, str] = {}
    try:
        with open(PROOF_OPEN_QUESTIONS, encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                try:
                    obj = json.loads(line)
                except json.JSONDecodeError:
                    continue
                qid = obj.get("qid")
                status = obj.get("status")
                if qid and status:
                    latest[qid] = status
    except OSError:
        return 0
    return sum(1 for s in latest.values() if s in ("open", "released"))


def _is_converged(results: pd.DataFrame, current_proof_hash: str) -> bool:
    """Converged iff:
       - the last STABLE_CHECKPOINT_COUNT rows in proof_results all have
         the same proof_hash equal to current_proof_hash AND
         verdict_hint in {partial_result, open} (no blockings), AND
       - no live open questions remain.
    """
    if _live_open_question_count() > 0:
        return False
    if results.empty or "proof_hash" not in results.columns:
        return False
    tail = results.tail(STABLE_CHECKPOINT_COUNT)
    if len(tail) < STABLE_CHECKPOINT_COUNT:
        return False
    if not all(str(h) == current_proof_hash for h in tail["proof_hash"].tolist()):
        return False
    verdicts = [str(v).lower() for v in tail.get("verdict_hint", [])]
    if not all(v in ("partial_result", "open") for v in verdicts):
        return False
    blockings = pd.to_numeric(tail.get("critic_blocking", 0), errors="coerce").fillna(0)
    if (blockings > 0).any():
        return False
    return True


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "description",
        help="One-line rationale. Must start with 'thesis: '.",
    )
    args = parser.parse_args()
    desc = args.description.strip()
    if "\t" in desc or "\n" in desc:
        print("ERROR: description may not contain tabs or newlines", file=sys.stderr)
        return 2

    spec = load_proof_spec()
    commit = _short_commit()
    branch_tag = _current_branch_tag()
    round_cap = _resolve_round_cap(spec)

    # Round cap (every row counts, including discards/crashes).
    results = _read_results_tsv()
    if len(results) >= round_cap:
        print(
            f"ERROR: round cap {round_cap} reached on this branch "
            f"(set AUTOERDOS_ROUND_CAP to override, or stop the loop).",
            file=sys.stderr,
        )
        return 4

    # Read proof_strategy.md and compute content hash.
    if not PROOF_STRATEGY_MD.exists():
        print(
            f"ERROR: {PROOF_STRATEGY_MD} not found — cannot log a round.",
            file=sys.stderr,
        )
        return 5
    proof_md = PROOF_STRATEGY_MD.read_text(encoding="utf-8")
    proof_hash = _proof_hash(proof_md)

    # Verifier audit lookup — must exist for this commit.
    verifier_log = _read_verifier_log()
    v_row = _latest_verifier_row(commit, spec.get("name", PROOF_TAG), verifier_log)
    if v_row is None:
        # Crash row: proof_prepare never reached print_summary.
        crash_row = {
            "commit": commit,
            "claim_status": spec.get("claim_status", "unknown"),
            "witness_valid": "0",
            "witness_score": "nan",
            "critic_blocking": "0",
            "critic_warn": "0",
            "verdict_hint": "crash",
            "verifier_seconds": "0",
            "proof_hash": proof_hash,
            "status": "crash",
            "description": desc,
        }
        _append_results_row(crash_row)
        return 5

    # Description must start with 'thesis: ' on non-crash rows.
    if not desc.lower().startswith("thesis:"):
        print("ERROR: keep/discard descriptions must start with 'thesis: '", file=sys.stderr)
        return 2

    # AST-equivalent dedup: proof_hash already seen on any branch?
    cache_df = _read_cache()
    dup = _find_cache_duplicate(cache_df, proof_hash, commit)
    if dup is not None:
        dup_branch, dup_commit = dup
        print(
            f"ERROR: proof_strategy.md content-hash matches prior round {dup_commit} "
            f"(branch erdos-proof/{dup_branch}, problem {PROOF_TAG}). "
            f"Make a real change before logging.",
            file=sys.stderr,
        )
        return 3

    witness_valid = int(v_row.get("witness_valid", 0) or 0)
    critic_blocking = int(v_row.get("critic_blocking", 0) or 0)
    critic_warn = int(v_row.get("critic_warn", 0) or 0)
    verdict_hint = str(v_row.get("verdict_hint", "")).strip().lower()
    verifier_seconds = _safe_float(v_row.get("verifier_seconds"))
    witness_score = _safe_float(v_row.get("witness_score"))

    # Keep rule.
    if witness_valid == 1:
        status = "keep_disproof"
    elif critic_blocking == 0 and verdict_hint in ("partial_result", "open"):
        status = "keep_progress"
    else:
        status = "discard"

    row = {
        "commit": commit,
        "claim_status": spec.get("claim_status", "unknown"),
        "witness_valid": str(witness_valid),
        "witness_score": f"{witness_score:.6f}" if not math.isnan(witness_score) else "nan",
        "critic_blocking": str(critic_blocking),
        "critic_warn": str(critic_warn),
        "verdict_hint": verdict_hint,
        "verifier_seconds": f"{verifier_seconds:.4f}",
        "proof_hash": proof_hash,
        "status": status,
        "description": desc,
    }
    _append_results_row(row)
    _append_cache(proof_hash, branch_tag, commit, verdict_hint, status)

    if status in ("keep_disproof", "keep_progress"):
        record_kind = "disproof" if status == "keep_disproof" else "partial"
        _write_record(
            commit,
            proof_hash=proof_hash,
            proof_md=proof_md,
            spec=spec,
            branch_tag=branch_tag,
            desc=desc,
            verifier_row=v_row,
            record_kind=record_kind,
        )

    # Terminal-condition exit codes.
    if status == "keep_disproof":
        # The verifier has ratified a counterexample. The agent should stop
        # the loop and let the human re-verify; exit 7 is the signal.
        print(
            f"COUNTEREXAMPLE: witness verified for {PROOF_TAG}; "
            f"score={witness_score} (rigorous lower bound on sum). "
            f"Stop the loop and have a human re-run library.primitive_set_witness.",
            file=sys.stderr,
        )
        return 7

    # Re-read results to include this row, then check convergence.
    results_after = _read_results_tsv()
    if status == "keep_progress" and _is_converged(results_after, proof_hash):
        print(
            "CONVERGED: critics clean, content stable, no open qids. "
            "Stop the loop — partial result is the kept artifact.",
            file=sys.stderr,
        )
        return 6

    return 0


if __name__ == "__main__":
    sys.exit(main())
