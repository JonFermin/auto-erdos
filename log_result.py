"""
log_result.py — sole gatekeeper that appends rows to results.tsv.

The agent runs:

    uv run log_result.py "thesis: greedy + restart on the n=4 sub-cube"

Everything else is computed by the harness from state on disk:

  1. Hash the stripped-AST of strategy.py at HEAD and look it up in the
     per-problem shared cache at
     ~/.cache/auto-erdos/trial_cache_<PROBLEM_TAG>.tsv. If any prior trial
     on any branch of this problem has the same AST hash, reject (exit 3).
     Comment/whitespace/docstring-only changes hash identically and are
     also rejected.
  2. Count rows in results.tsv against AUTOERDOS_TRIAL_CAP (default 20)
     (exit 4).
  3. Look up the current commit's verifier verdict in verifier_results.tsv.
     No row → strategy.py never reached print_summary → crash (exit 5).
  4. Apply the keep rule (is_valid AND score > running_best, where
     running_best starts at the problem's literature baseline and ratchets
     up with each `keep`); compute status; write the row; append to the
     shared cache; exit 0.

The agent never chooses the status. Mis-grading is structurally impossible
under this CLI — same idea as the parent quant repo, minus the statistics
layer (no IS/OOS, no bootstrap, no Sharpe deflation — none of those have
analogs in deterministic combinatorial verification).

Exit codes:
  0 — row logged (status computed; final stdout line is `status=keep|discard`)
  2 — description invalid (tab/newline, or missing `thesis: ` on a non-crash row)
  3 — AST duplicate of a prior trial on this problem (any branch)
  4 — trial cap reached — stop the loop and review
  5 — crash row logged (the run never reached print_summary)
"""
from __future__ import annotations

import argparse
import ast
import hashlib
import json
import math
import os
import platform
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path

import pandas as pd

from prepare import (
    PROBLEM_TAG,
    REPO_ROOT,
    VERIFIER_RESULTS_TSV,
    append_hypothesis_log,
    load_spec,
)

if platform.system() == "Windows":
    import msvcrt
else:
    import fcntl

RESULTS_TSV = REPO_ROOT / "results.tsv"
HEADER = ["commit", "score", "is_valid", "verifier_seconds", "status", "description"]

_CACHE_DIR = Path.home() / ".cache" / "auto-erdos"
CACHE_HEADER = [
    "ast_sha256",
    "branch_tag",
    "commit",
    "score",
    "status",
    "written_at",
]

DEFAULT_TRIAL_CAP = 20
TRIAL_CAP = int(os.environ.get("AUTOERDOS_TRIAL_CAP", str(DEFAULT_TRIAL_CAP)))


def _resolve_trial_cap(spec: dict) -> int:
    """Per-call resolution: env AUTOERDOS_TRIAL_CAP > spec.trial_cap > 20.

    Default stays at 20 — the cap is a discipline mechanism, not a knob.
    Override individual problems via "trial_cap" in problems/<tag>.json
    only after a 20-trial branch shows real progression but ran out.
    """
    env = os.environ.get("AUTOERDOS_TRIAL_CAP")
    if env is not None:
        return int(env)
    return int(spec.get("trial_cap", DEFAULT_TRIAL_CAP))


# --------------------------------------------------------------------------- #
# Git helpers
# --------------------------------------------------------------------------- #

def _short_commit() -> str:
    out = subprocess.check_output(
        ["git", "-C", str(REPO_ROOT), "rev-parse", "--short=7", "HEAD"],
        stderr=subprocess.DEVNULL,
    )
    return out.decode().strip()


def _git_show(ref: str, relpath: str) -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "show", f"{ref}:{relpath}"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode("utf-8", errors="replace")
    except subprocess.CalledProcessError:
        return None


def _current_branch_tag() -> str:
    """Return the portion of the branch name after `erdos-research/`.

    Falls back to the bare branch name (or 'unknown' on detached HEAD).
    """
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return "unknown"
    branch = out.decode().strip()
    prefix = "erdos-research/"
    return branch[len(prefix):] if branch.startswith(prefix) else (branch or "unknown")


# --------------------------------------------------------------------------- #
# AST dedup
# --------------------------------------------------------------------------- #

def _strip_docstrings(tree: ast.AST) -> ast.AST:
    """In-place strip module/class/function-level docstrings so a pure
    docstring rewrite compares equal. Comments and whitespace are already
    dropped by `ast.parse`.
    """
    for node in ast.walk(tree):
        if isinstance(node, (ast.Module, ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            body = getattr(node, "body", None)
            if not body:
                continue
            first = body[0]
            if (
                isinstance(first, ast.Expr)
                and isinstance(first.value, ast.Constant)
                and isinstance(first.value.value, str)
            ):
                node.body = body[1:] or [ast.Pass()]
    return tree


def _strategy_ast_hash() -> str | None:
    src = _git_show("HEAD", "strategy.py")
    if src is None:
        return None
    try:
        tree = _strip_docstrings(ast.parse(src))
    except SyntaxError:
        return None
    dump = ast.dump(tree, annotate_fields=False, include_attributes=False)
    return hashlib.sha256(dump.encode("utf-8")).hexdigest()


# --------------------------------------------------------------------------- #
# Per-problem trial cache (shared across branches)
# --------------------------------------------------------------------------- #

def _cache_path() -> Path:
    return _CACHE_DIR / f"trial_cache_{PROBLEM_TAG}.tsv"


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
                dtype={
                    "ast_sha256": str, "branch_tag": str,
                    "commit": str, "status": str, "written_at": str,
                },
            )
    except (pd.errors.EmptyDataError, OSError):
        return pd.DataFrame(columns=CACHE_HEADER)
    except pd.errors.ParserError as e:
        print(
            f"WARNING: trial cache at {path} is malformed ({e}); "
            f"dedup disabled for this run. Inspect manually.",
            file=sys.stderr,
        )
        return pd.DataFrame(columns=CACHE_HEADER)
    if "score" in df.columns:
        df["score"] = pd.to_numeric(df["score"], errors="coerce")
    for col in ("ast_sha256", "branch_tag", "commit", "status"):
        if col in df.columns:
            df[col] = df[col].astype(str).str.strip()
    return df


def _append_cache(
    ast_hash: str,
    branch_tag: str,
    commit: str,
    score: float,
    status: str,
) -> None:
    path = _cache_path()
    written_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    score_str = (
        f"{float(score):.6f}"
        if score is not None and math.isfinite(float(score))
        else "nan"
    )
    row = [ast_hash, branch_tag, commit, score_str, status, written_at]
    with _cache_lock(path, exclusive=True) as f:
        f.seek(0, os.SEEK_END)
        if f.tell() == 0:
            f.write("\t".join(CACHE_HEADER) + "\n")
        f.write("\t".join(row) + "\n")
        f.flush()
        os.fsync(f.fileno())


def _find_cache_duplicate(
    cache_df: pd.DataFrame, ast_hash: str, current_commit: str
) -> tuple[str, str] | None:
    if cache_df.empty or "ast_sha256" not in cache_df.columns:
        return None
    hits = cache_df[cache_df["ast_sha256"] == ast_hash]
    if "commit" in hits.columns:
        hits = hits[hits["commit"] != current_commit]
    if hits.empty:
        return None
    row = hits.iloc[0]
    return (str(row.get("branch_tag", "unknown")), str(row.get("commit", "")))


# --------------------------------------------------------------------------- #
# results.tsv I/O
# --------------------------------------------------------------------------- #

def _read_results_tsv() -> pd.DataFrame:
    if not RESULTS_TSV.exists() or RESULTS_TSV.stat().st_size == 0:
        return pd.DataFrame(columns=HEADER)
    try:
        df = pd.read_csv(
            RESULTS_TSV, sep="\t",
            dtype={"commit": str, "status": str, "description": str},
        )
    except pd.errors.EmptyDataError:
        return pd.DataFrame(columns=HEADER)
    if "status" in df.columns:
        df["status"] = df["status"].astype(str).str.strip().str.lower()
    if "commit" in df.columns:
        df["commit"] = df["commit"].astype(str).str.strip()
    for col in ("score", "is_valid", "verifier_seconds"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    return df


def _append_results_row(
    commit: str,
    score: float,
    is_valid: float,
    verifier_seconds: float,
    status: str,
    desc: str,
) -> None:
    def fmt(x: float, spec: str, fallback: str) -> str:
        if x is None or not math.isfinite(float(x)):
            return fallback
        return format(float(x), spec)

    needs_header = (not RESULTS_TSV.exists()) or RESULTS_TSV.stat().st_size == 0
    row = [
        commit,
        fmt(score, ".6f", "0.000000"),
        fmt(is_valid, ".0f", "0"),
        fmt(verifier_seconds, ".4f", "0.0000"),
        status,
        desc,
    ]
    with open(RESULTS_TSV, "a", encoding="utf-8", newline="") as f:
        if needs_header:
            f.write("\t".join(HEADER) + "\n")
        f.write("\t".join(row) + "\n")
    print(f"logged: {commit}\t{row[1]}\t{row[2]}\t{row[3]}\t{status}\t{desc}")
    print(f"status={status}")


# --------------------------------------------------------------------------- #
# Verifier audit lookup
# --------------------------------------------------------------------------- #

def _read_verifier_log() -> pd.DataFrame:
    if not VERIFIER_RESULTS_TSV.exists() or VERIFIER_RESULTS_TSV.stat().st_size == 0:
        return pd.DataFrame()
    try:
        df = pd.read_csv(
            VERIFIER_RESULTS_TSV, sep="\t",
            dtype={
                "commit": str, "problem": str,
                "status_hint": str, "reason": str,
            },
        )
    except pd.errors.EmptyDataError:
        return pd.DataFrame()
    for col in ("score", "is_valid", "verifier_seconds"):
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce")
    if "commit" in df.columns:
        df["commit"] = df["commit"].astype(str).str.strip()
    if "status_hint" in df.columns:
        df["status_hint"] = df["status_hint"].astype(str).str.strip().str.lower()
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
# Running best
# --------------------------------------------------------------------------- #

def _running_best(results: pd.DataFrame, baseline: float) -> float:
    """Highest score among kept rows; baseline if none."""
    if results.empty or "status" not in results.columns:
        return float(baseline)
    kept = results[results["status"] == "keep"]
    if kept.empty or "score" not in kept.columns:
        return float(baseline)
    scores = pd.to_numeric(kept["score"], errors="coerce").dropna()
    if scores.empty:
        return float(baseline)
    return max(float(baseline), float(scores.max()))


# --------------------------------------------------------------------------- #
# Records — committed snapshot of every keep that beats the literature LB.
# --------------------------------------------------------------------------- #

RECORDS_DIR = REPO_ROOT / "records"


def _read_last_candidate(tag: str, commit: str) -> list | None:
    """Read this run's candidate from prepare.py's per-run cache. Returns
    None if the cache is missing, malformed, or written for a different
    commit (defensive — the cache is overwritten every strategy.py run).
    """
    path = _CACHE_DIR / f"last_candidate_{tag}.json"
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        with open(path, encoding="utf-8") as f:
            payload = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None
    if str(payload.get("commit", "")).strip() != commit:
        return None
    cand = payload.get("candidate")
    return cand if isinstance(cand, list) else None


def _write_record(
    commit: str,
    score: float,
    is_valid: int,
    verifier_seconds: float,
    desc: str,
    spec: dict,
    branch_tag: str,
) -> None:
    """Write a committed record snapshot for a kept trial.

    Filename: records/<tag>_<score>_<commit>.json. The commit suffix
    guarantees uniqueness — two distinct strategies that hit the same
    score get separate records.

    Best-effort auto-commit: if `git add && git commit` succeeds, the
    record lands as a follow-up commit (the kept strategy commit is its
    parent). If the commit step fails, the file remains as untracked and
    the agent can pick it up on its next commit. The keep itself is
    unaffected — bookkeeping failures must not undo a real result.
    """
    tag = spec.get("name", "unknown")
    baseline = float(spec.get("baseline", 0))
    candidate = _read_last_candidate(tag, commit)

    record = {
        "problem": tag,
        "family": spec.get("family", ""),
        "score": score,
        "baseline": baseline,
        "improvement_over_baseline": score - baseline,
        "is_valid": is_valid,
        "verifier_seconds": verifier_seconds,
        "commit": commit,
        "branch": f"erdos-research/{branch_tag}",
        "thesis": desc,
        "candidate": candidate,
        "candidate_available": candidate is not None,
        "written_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }

    score_int = int(score) if math.isfinite(score) else 0
    filename = f"{tag}_{score_int}_{commit}.json"
    path = RECORDS_DIR / filename
    try:
        RECORDS_DIR.mkdir(parents=True, exist_ok=True)
        if path.exists():
            print(
                f"WARNING: record {filename} already exists; refusing to overwrite. "
                f"Keep is logged but record was not refreshed.",
                file=sys.stderr,
            )
            return
        with open(path, "w", encoding="utf-8") as f:
            json.dump(record, f, indent=2, sort_keys=True)
            f.write("\n")
    except OSError as e:
        print(f"WARNING: failed to write record {filename}: {e}", file=sys.stderr)
        return

    rel = path.relative_to(REPO_ROOT).as_posix()
    try:
        subprocess.check_call(
            ["git", "-C", str(REPO_ROOT), "add", rel],
            stderr=subprocess.DEVNULL,
        )
        subprocess.check_call(
            ["git", "-C", str(REPO_ROOT), "commit", "-m",
             f"record: {tag} score={score_int} ({branch_tag})"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        print(f"record: committed {rel}", file=sys.stderr)
    except subprocess.CalledProcessError as e:
        print(
            f"WARNING: record {rel} written but auto-commit failed ({e}); "
            f"file is staged/untracked and can be committed by hand.",
            file=sys.stderr,
        )

    _maybe_write_papers(path)


def _maybe_write_papers(record_path: Path) -> None:
    """Optionally invoke write_paper.py for one or more model presets.

    Triggered by env AUTOERDOS_WRITEUP. Default is unset/'0'/'off' — no
    paper generation, no extra wall-clock cost on the autoresearch loop.

    Accepted values:
      unset / '' / '0' / 'off' / 'false' → skip
      '1' / 'on' / 'true' / 'all'        → both opus and codex
      comma-list (e.g. 'opus' or 'opus,codex') → that subset

    Failures are logged to stderr and swallowed — paper generation must
    NEVER undo a kept record. Output goes to papers/ alongside records/
    and gets auto-committed as a follow-up by write_paper.py? No — it
    does not auto-commit. Whoever invokes the keep can `git add papers/`
    on their next commit, or run write_paper.py later from any record.
    """
    raw = os.environ.get("AUTOERDOS_WRITEUP", "").strip().lower()
    if not raw or raw in ("0", "off", "false", "no"):
        return
    if raw in ("1", "on", "true", "yes", "all"):
        models = ["opus", "codex"]
    else:
        models = [m.strip() for m in raw.split(",") if m.strip()]
        valid = {"opus", "codex"}
        bad = [m for m in models if m not in valid]
        if bad:
            print(
                f"WARNING: AUTOERDOS_WRITEUP={raw!r} contains unknown model(s) {bad}; "
                f"skipping paper generation. Valid: {sorted(valid)}.",
                file=sys.stderr,
            )
            return
        if not models:
            return

    mode = os.environ.get("AUTOERDOS_WRITEUP_MODE", "paper").strip().lower() or "paper"
    if mode not in ("paper", "proof"):
        print(
            f"WARNING: AUTOERDOS_WRITEUP_MODE={mode!r} is not 'paper' or 'proof'; "
            f"defaulting to 'paper'.",
            file=sys.stderr,
        )
        mode = "paper"

    cmd = [
        sys.executable, str(REPO_ROOT / "write_paper.py"),
        str(record_path),
        "--mode", mode,
        "--models", ",".join(models),
    ]
    print(f"writeup: invoking {' '.join(cmd)}", file=sys.stderr)
    try:
        rc = subprocess.call(cmd, cwd=str(REPO_ROOT))
        if rc != 0:
            print(
                f"WARNING: write_paper.py exited {rc}; record is still kept. "
                f"Inspect papers/ for partial output.",
                file=sys.stderr,
            )
    except OSError as e:
        print(
            f"WARNING: could not launch write_paper.py ({e}); record is still kept.",
            file=sys.stderr,
        )


# --------------------------------------------------------------------------- #
# Main
# --------------------------------------------------------------------------- #

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Log this run to results.tsv. Status is computed — the agent does not choose it."
    )
    parser.add_argument(
        "description",
        help="One-line rationale. Non-crash rows must start with 'thesis: '.",
    )
    args = parser.parse_args()
    desc = args.description.strip()
    if "\t" in desc or "\n" in desc:
        print("ERROR: description may not contain tabs or newlines", file=sys.stderr)
        return 2

    commit = _short_commit()
    spec = load_spec()
    baseline = float(spec.get("baseline", 0))
    trial_cap = _resolve_trial_cap(spec)

    # Trial cap (crashes count: cognitive budget).
    results = _read_results_tsv()
    if len(results) >= trial_cap:
        print(
            f"ERROR: trial cap {trial_cap} reached on this branch "
            f"(set AUTOERDOS_TRIAL_CAP to override, or start a new branch).",
            file=sys.stderr,
        )
        return 4

    # AST dedup against this problem's shared cache (any branch).
    ast_hash = _strategy_ast_hash()
    cache_df = _read_cache()
    if ast_hash is not None:
        dup = _find_cache_duplicate(cache_df, ast_hash, commit)
        if dup is not None:
            dup_branch, dup_commit = dup
            print(
                f"ERROR: strategy.py AST matches prior trial {dup_commit} "
                f"(branch erdos-research/{dup_branch}, problem {PROBLEM_TAG}). "
                f"Pick a genuinely different hypothesis.",
                file=sys.stderr,
            )
            return 3

    # Verifier audit lookup.
    verifier_log = _read_verifier_log()
    v_row = _latest_verifier_row(commit, spec["name"], verifier_log)

    if v_row is None:
        # The run never reached print_summary — crash row, free-form description.
        _append_results_row(commit, float("nan"), float("nan"), float("nan"), "crash", desc)
        branch_tag = _current_branch_tag()
        if ast_hash is not None:
            _append_cache(ast_hash, branch_tag, commit, float("nan"), "crash")
        append_hypothesis_log(
            branch_tag, commit, float("nan"), float("nan"), "crash", desc,
        )
        return 5

    if not desc.lower().startswith("thesis:"):
        print("ERROR: keep/discard descriptions must start with 'thesis: '", file=sys.stderr)
        return 2

    score = float(v_row.get("score", float("nan")))
    is_valid = int(v_row.get("is_valid", 0) or 0)
    verifier_seconds = float(v_row.get("verifier_seconds", float("nan")))
    hint = str(v_row.get("status_hint", "")).strip().lower()
    reason_tail = str(v_row.get("reason", ""))

    running_best = _running_best(results, baseline)

    checks = {
        f"is_valid {is_valid} == 1": is_valid == 1,
        f"score {score:.4f} > running_best {running_best:.4f}":
            math.isfinite(score) and score > running_best,
    }
    keep = all(checks.values())
    status = "keep" if keep else "discard"
    if keep:
        reason = (
            f"cleared all gates (score {score:.4f} > running_best {running_best:.4f}; "
            f"hint={hint}; verifier_seconds={verifier_seconds:.4f})"
        )
    else:
        failed = [k for k, v in checks.items() if not v]
        reason = (
            f"failed: {'; '.join(failed)}"
            f" (hint={hint}; running_best={running_best:.4f}; "
            f"verifier reason: {reason_tail[:120]})"
        )

    print(f"grader: {status} ({reason})", file=sys.stderr)
    _append_results_row(commit, score, is_valid, verifier_seconds, status, desc)
    branch_tag = _current_branch_tag()
    if ast_hash is not None:
        _append_cache(ast_hash, branch_tag, commit, score, status)
    append_hypothesis_log(branch_tag, commit, score, is_valid, status, desc)
    if keep:
        _write_record(
            commit, score, is_valid, verifier_seconds, desc,
            spec, branch_tag,
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
