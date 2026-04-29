"""
prepare.py — READ-ONLY verifier and driver helpers.

The agent never edits this file. It exposes:
  - verify(candidate) -> VerifyResult
  - print_summary(candidate, result): emits the metric block parsed by log_result.py
        and appends a row to verifier_results.tsv (the harness-side audit trail
        log_result.py reads to compute keep/discard).
  - load_best_so_far(): public read of the cross-branch best-valid candidate
        for this PROBLEM_TAG (warm-start helper for agents).
  - constants: REPO_ROOT, VERIFIER_RESULTS_TSV, PROBLEM_TAG, TIME_BUDGET_S

To add a new Port-1 problem family, register a verifier in VERIFIERS and add
the matching problems/<tag>.json. Don't edit existing verifiers — the AST
hash and trial cache assume the verifier is part of the fixed environment.

Cap-set background (capset family):
  A subset S of F_3^n is a "cap set" if no three distinct points a, b, c in S
  satisfy a + b + c == 0 (mod 3) elementwise — equivalently, no three points
  form an arithmetic progression in (Z/3Z)^n. The score is |S|. We want big.
  Best known lower bounds for small n live in the problem JSONs.
"""
from __future__ import annotations

import json
import math
import os
import platform
import subprocess
import time
from contextlib import contextmanager
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable, Sequence

if platform.system() == "Windows":
    import msvcrt
else:
    import fcntl  # type: ignore[unused-ignore]

REPO_ROOT = Path(__file__).resolve().parent
PROBLEM_TAG = os.environ.get("PROBLEM_TAG", "capset_n8")
PROBLEMS_DIR = REPO_ROOT / "problems"
VERIFIER_RESULTS_TSV = REPO_ROOT / "verifier_results.tsv"

# Wall-clock cap inside a single strategy.py run. Verifiers themselves are
# cheap (under a second for capset n<=8 and sidon up to N~10000); the budget
# is the agent's search room — DFS, SA, GA, etc. inside generate_candidate.
# Bumped from 300 -> 900 (2026-04-28) after the apr28 cap-set batch showed
# greedy/SA hitting a hard ceiling because exact-DFS sub-routines couldn't
# finish their warm-start (e.g., Edel-112 in F_3^6) inside 5 minutes.
#
# Resolution order: env AUTOERDOS_TIME_BUDGET_S > problems/<tag>.json
# "time_budget_s" > 900s default. The legacy module constant is kept for
# any code that still imports it directly; it does NOT see per-problem
# overrides — call _resolve_time_budget(spec) for that.
DEFAULT_TIME_BUDGET_S = 900
TIME_BUDGET_S = int(os.environ.get("AUTOERDOS_TIME_BUDGET_S", str(DEFAULT_TIME_BUDGET_S)))


def _resolve_time_budget(spec: dict | None = None) -> int:
    env = os.environ.get("AUTOERDOS_TIME_BUDGET_S")
    if env is not None:
        return int(env)
    if spec is None:
        spec = load_spec()
    return int(spec.get("time_budget_s", DEFAULT_TIME_BUDGET_S))


@dataclass
class VerifyResult:
    is_valid: bool
    score: float
    reason: str
    verifier_seconds: float


def load_spec(tag: str | None = None) -> dict:
    """Load a problem JSON. Defaults to env PROBLEM_TAG."""
    name = tag or PROBLEM_TAG
    path = PROBLEMS_DIR / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(
            f"Problem spec not found: {path}. "
            f"Set PROBLEM_TAG to one of {[p.stem for p in PROBLEMS_DIR.glob('*.json')]}."
        )
    with open(path, encoding="utf-8") as f:
        return json.load(f)


# --------------------------------------------------------------------------- #
# Cap-set verifier
# --------------------------------------------------------------------------- #

def _verify_capset(candidate: Iterable[Sequence[int]], spec: dict) -> VerifyResult:
    """Verify candidate ⊂ F_3^n is a cap set. O(k^2) where k = |candidate|.

    For each pair (a, b) the unique third point that completes a 3-term AP is
    c = -(a + b) mod 3. If c is in the set and distinct from a and b, the
    triple {a, b, c} sums to zero — reject.
    """
    n = int(spec["n"])
    t0 = time.time()

    points: list[tuple[int, ...]] = []
    seen: set[tuple[int, ...]] = set()
    for raw in candidate:
        p = tuple(int(c) for c in raw)
        if len(p) != n:
            return VerifyResult(False, 0.0, f"point {p} has dim {len(p)} != {n}", time.time() - t0)
        for c in p:
            if c not in (0, 1, 2):
                return VerifyResult(False, 0.0, f"point {p} has non-{0,1,2} coord {c}", time.time() - t0)
        if p in seen:
            return VerifyResult(False, 0.0, f"duplicate point {p} in candidate", time.time() - t0)
        seen.add(p)
        points.append(p)

    k = len(points)
    if k == 0:
        return VerifyResult(True, 0.0, "empty set is trivially cap-free", time.time() - t0)

    # The AP-completion check. We iterate ordered pairs (i < j) and probe.
    # Bail at first violation.
    for i in range(k):
        a = points[i]
        for j in range(i + 1, k):
            b = points[j]
            c = tuple((-(a[d] + b[d])) % 3 for d in range(n))
            if c == a or c == b:
                # Would not give 3 distinct points; AP needs a != b != c != a.
                continue
            if c in seen:
                return VerifyResult(
                    False,
                    0.0,
                    f"triple sums to 0 mod 3: {a} + {b} + {c}",
                    time.time() - t0,
                )

    return VerifyResult(True, float(k), f"valid cap set of size {k} in F_3^{n}", time.time() - t0)


def _verify_sidon(candidate, spec: dict) -> VerifyResult:
    """Verify candidate ⊂ [1, N] is a canonical Sidon (B_2) set: all sums
    a+b with a, b ∈ S, a ≤ b are distinct — INCLUDING the degenerate case
    a = b (sum = 2a). Equivalently, all nonzero positive differences are
    distinct. O(k^2) where k = |candidate|.

    Strict B_2 / canonical Sidon: a+b = c+d with a≤b, c≤d implies (a,b)=(c,d).
    Note the difference from the weaker "all sums of distinct elements (a<b)
    distinct" condition — under the weak version, {1,2,3} is Sidon (sums
    3,4,5 distinct) but under B_2 it is not (1+3 = 2+2 = 4). The literature
    LBs in problems/sidon_*.json are Singer-construction-based and are B_2.
    """
    N = int(spec["N"])
    t0 = time.time()

    pts: list[int] = []
    seen: set[int] = set()
    for raw in candidate:
        x = int(raw)
        if not (1 <= x <= N):
            return VerifyResult(False, 0.0, f"point {x} out of [1,{N}]", time.time() - t0)
        if x in seen:
            return VerifyResult(False, 0.0, f"duplicate point {x} in candidate", time.time() - t0)
        seen.add(x)
        pts.append(x)

    k = len(pts)
    if k <= 1:
        return VerifyResult(True, float(k), f"trivially Sidon (size {k}) in [1,{N}]", time.time() - t0)

    pts.sort()
    sums: dict[int, tuple[int, int]] = {}
    # j ranges from i (inclusive) to capture the 2a degenerate case required by B_2.
    for i in range(k):
        a = pts[i]
        for j in range(i, k):
            b = pts[j]
            s = a + b
            prev = sums.get(s)
            if prev is not None:
                return VerifyResult(
                    False, 0.0,
                    f"duplicate sum {s}: ({a},{b}) collides with ({prev[0]},{prev[1]}) — B_2 violated",
                    time.time() - t0,
                )
            sums[s] = (a, b)

    return VerifyResult(True, float(k), f"valid B_2 Sidon set of size {k} in [1,{N}]", time.time() - t0)


VERIFIERS = {
    "capset": _verify_capset,
    "sidon": _verify_sidon,
}


def verify(candidate) -> VerifyResult:
    """Dispatch to the family-specific verifier. Always returns a VerifyResult
    (no exceptions for verifier failures — the agent's bug becomes a discard,
    not a crash, when the bug is in the candidate).
    """
    spec = load_spec()
    family = spec.get("family")
    if family not in VERIFIERS:
        return VerifyResult(False, 0.0, f"no verifier registered for family={family!r}", 0.0)
    fn = VERIFIERS[family]
    try:
        return fn(candidate, spec)
    except Exception as e:  # noqa: BLE001 — surface as invalid, not crash
        return VerifyResult(False, 0.0, f"verifier raised {type(e).__name__}: {e}", 0.0)


# --------------------------------------------------------------------------- #
# Output + audit trail
# --------------------------------------------------------------------------- #

def _short_commit() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--short=7", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except subprocess.CalledProcessError:
        return "unknown"


def _status_hint(spec: dict, result: VerifyResult) -> str:
    if not result.is_valid:
        return "invalid"
    baseline = float(spec.get("baseline", 0))
    if result.score > baseline:
        return "improvement_eligible"
    return "no_improvement"


def print_summary(candidate, result: VerifyResult) -> None:
    """Emit the fixed metric block and append a row to verifier_results.tsv.

    Also updates ``best_so_far_<TAG>.json`` in the user cache when the
    candidate is valid AND scores higher than any prior valid candidate
    seen for this problem (across all branches).
    """
    spec = load_spec()
    hint = _status_hint(spec, result)

    print("---")
    print(f"problem:           {spec['name']}")
    print(f"family:            {spec['family']}")
    print(f"score:             {result.score:.6f}")
    print(f"is_valid:          {1 if result.is_valid else 0}")
    print(f"verifier_seconds:  {result.verifier_seconds:.4f}")
    print(f"baseline:          {spec.get('baseline', 0)}")
    print(f"status_hint:       {hint}")
    # The reason is informational; truncate to keep the block compact.
    reason = result.reason.replace("\t", " ").replace("\n", " ")
    if len(reason) > 200:
        reason = reason[:197] + "..."
    print(f"reason:            {reason}")

    _append_audit_row(spec, result, hint)
    _save_best_if_better(candidate, result, spec)
    _save_last_candidate(candidate, result, spec)


def _append_audit_row(spec: dict, result: VerifyResult, hint: str) -> None:
    """Harness audit trail. log_result.py reads this — the agent must not.
    Schema:
        commit  problem  score  is_valid  verifier_seconds  status_hint  reason
    """
    commit = _short_commit()
    needs_header = (not VERIFIER_RESULTS_TSV.exists()) or VERIFIER_RESULTS_TSV.stat().st_size == 0
    reason = result.reason.replace("\t", " ").replace("\n", " ")
    row = [
        commit,
        spec["name"],
        f"{result.score:.6f}",
        "1" if result.is_valid else "0",
        f"{result.verifier_seconds:.4f}",
        hint,
        reason,
    ]
    with open(VERIFIER_RESULTS_TSV, "a", encoding="utf-8", newline="") as f:
        if needs_header:
            f.write("commit\tproblem\tscore\tis_valid\tverifier_seconds\tstatus_hint\treason\n")
        f.write("\t".join(row) + "\n")


# --------------------------------------------------------------------------- #
# best_so_far cache — cross-branch persistence of the best valid candidate.
# --------------------------------------------------------------------------- #

_CACHE_DIR = Path.home() / ".cache" / "auto-erdos"


def _best_so_far_path(tag: str | None = None) -> Path:
    return _CACHE_DIR / f"best_so_far_{tag or PROBLEM_TAG}.json"


@contextmanager
def _best_so_far_lock(tag: str | None = None):
    """Cross-process lock for the best_so_far cache, via a sidecar .lock
    file so the JSON read/write doesn't entangle with the lock target."""
    path = _best_so_far_path(tag)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(".json.lock")
    f = open(lock_path, "a+", encoding="utf-8")
    try:
        if platform.system() == "Windows":
            f.seek(0)
            msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
        else:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        yield
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


def _serialize_candidate(candidate, family: str) -> list:
    """Convert candidate to JSON-serializable form. Tuples become lists,
    numpy ints become Python ints. Returns [] on iteration error."""
    out: list = []
    try:
        if family == "capset":
            for p in candidate:
                out.append([int(c) for c in p])
        elif family == "sidon":
            for x in candidate:
                out.append(int(x))
        else:
            for item in candidate:
                if hasattr(item, "__iter__"):
                    out.append([int(c) for c in item])
                else:
                    out.append(int(item))
    except (TypeError, ValueError):
        return []
    return out


def _save_best_if_better(candidate, result: VerifyResult, spec: dict) -> None:
    """Update best_so_far_<TAG>.json if this run's valid score beats prior."""
    if not result.is_valid:
        return
    score = float(result.score)
    if not math.isfinite(score) or score <= 0:
        return
    family = spec.get("family", "")
    tag = spec.get("name", PROBLEM_TAG)
    serialized = _serialize_candidate(candidate, family)
    if not serialized:
        return
    path = _best_so_far_path(tag)
    try:
        with _best_so_far_lock(tag):
            prior_score = -math.inf
            if path.exists() and path.stat().st_size > 0:
                try:
                    with open(path, encoding="utf-8") as f:
                        prior = json.load(f)
                    prior_score = float(prior.get("score", -math.inf))
                except (json.JSONDecodeError, OSError):
                    prior_score = -math.inf
            if score <= prior_score:
                return
            try:
                out = subprocess.check_output(
                    ["git", "-C", str(REPO_ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
                    stderr=subprocess.DEVNULL,
                )
                branch = out.decode().strip()
                prefix = "erdos-research/"
                branch_tag = branch[len(prefix):] if branch.startswith(prefix) else (branch or "unknown")
            except subprocess.CalledProcessError:
                branch_tag = "unknown"
            payload = {
                "problem": tag,
                "family": family,
                "score": score,
                "is_valid": 1,
                "verifier_reason": result.reason[:500],
                "branch_tag": branch_tag,
                "commit": _short_commit(),
                "written_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
                "candidate": serialized,
            }
            tmp_path = path.with_suffix(".json.tmp")
            with open(tmp_path, "w", encoding="utf-8") as f:
                json.dump(payload, f, separators=(",", ":"))
            os.replace(tmp_path, path)
    except OSError:
        # Saving best_so_far is best-effort; never crash the verifier on it.
        return


def _save_last_candidate(candidate, result: VerifyResult, spec: dict) -> None:
    """Snapshot this run's candidate to ``last_candidate_<TAG>.json``.

    Unlike ``_save_best_if_better`` (which only writes on cross-branch
    improvement), this overwrites every run so ``log_result.py`` can read
    back the candidate for the current commit when promoting a keep into a
    committed ``records/<tag>_<score>_<commit>.json`` entry. Transient by
    design — the audit trail of record is the committed records/ tree.
    """
    score = float(result.score) if math.isfinite(float(result.score)) else 0.0
    family = spec.get("family", "")
    tag = spec.get("name", PROBLEM_TAG)
    serialized = _serialize_candidate(candidate, family) if result.is_valid else []
    path = _CACHE_DIR / f"last_candidate_{tag}.json"
    payload = {
        "problem": tag,
        "family": family,
        "commit": _short_commit(),
        "score": score,
        "is_valid": 1 if result.is_valid else 0,
        "candidate": serialized,
        "written_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }
    try:
        _CACHE_DIR.mkdir(parents=True, exist_ok=True)
        tmp_path = path.with_suffix(".json.tmp")
        with open(tmp_path, "w", encoding="utf-8") as f:
            json.dump(payload, f, separators=(",", ":"))
        os.replace(tmp_path, path)
    except OSError:
        return


# --------------------------------------------------------------------------- #
# Hypothesis log — public cross-branch trial memory.
#
# The harness already writes a per-trial AST cache (`trial_cache_<TAG>.tsv`)
# that's forbidden to agents. The hypothesis log is the SANCTIONED public
# channel: every trial appends a row (status, score, thesis) here, and any
# agent may read via load_hypothesis_log. This lets a new branch see which
# hypothesis families already failed on the problem without leaking the
# AST-dedup mechanism.
# --------------------------------------------------------------------------- #

_HYPOTHESIS_LOG_HEADER = [
    "written_at", "branch_tag", "commit", "score", "is_valid", "status", "thesis",
]


def _hypothesis_log_path(tag: str | None = None) -> Path:
    return _CACHE_DIR / f"hypothesis_log_{tag or PROBLEM_TAG}.tsv"


@contextmanager
def _hypothesis_log_lock(tag: str | None = None):
    """Cross-process lock via a sidecar .lock file on the hypothesis log."""
    path = _hypothesis_log_path(tag)
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(".tsv.lock")
    f = open(lock_path, "a+", encoding="utf-8")
    try:
        if platform.system() == "Windows":
            f.seek(0)
            msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
        else:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX)
        yield
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


def append_hypothesis_log(
    branch_tag: str,
    commit: str,
    score: float,
    is_valid,
    status: str,
    thesis: str,
    *,
    tag: str | None = None,
) -> None:
    """Append one row to ~/.cache/auto-erdos/hypothesis_log_<TAG>.tsv.

    Called by log_result.py on every trial (keep, discard, or crash). Agents
    do NOT call this directly — they read via load_hypothesis_log.
    """
    if isinstance(score, (int, float)) and math.isfinite(float(score)):
        score_str = f"{float(score):.6f}"
    else:
        score_str = "nan"
    if isinstance(is_valid, bool):
        is_valid_str = "1" if is_valid else "0"
    elif isinstance(is_valid, (int, float)):
        if isinstance(is_valid, float) and not math.isfinite(is_valid):
            is_valid_str = "nan"
        else:
            is_valid_str = "1" if int(is_valid) == 1 else "0"
    else:
        is_valid_str = "nan"
    written_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    thesis_clean = str(thesis).replace("\t", " ").replace("\n", " ")
    row = [written_at, branch_tag, commit, score_str, is_valid_str, status, thesis_clean]
    path = _hypothesis_log_path(tag)
    try:
        with _hypothesis_log_lock(tag):
            needs_header = (not path.exists()) or path.stat().st_size == 0
            with open(path, "a", encoding="utf-8", newline="") as f:
                if needs_header:
                    f.write("\t".join(_HYPOTHESIS_LOG_HEADER) + "\n")
                f.write("\t".join(row) + "\n")
    except OSError:
        # Best-effort logging — never crash a trial because the log couldn't write.
        return


def load_hypothesis_log(
    tag: str | None = None,
    *,
    since_utc: str | None = None,
) -> list[dict]:
    """Public read of the cross-branch hypothesis log for a problem.

    Returns rows (oldest first) as dicts with keys:
      written_at, branch_tag, commit, score, is_valid, status, thesis.

    Agents may use this to learn which hypothesis families have already been
    tried (and their outcome) on this problem across all branches. Thesis
    strings are stored verbatim — no automatic family classification.

    ``since_utc`` (ISO 8601 string) optionally filters to rows with
    ``written_at >= since_utc``.

    Returns ``[]`` if the log file does not exist yet. To retire history,
    ``rm`` ~/.cache/auto-erdos/hypothesis_log_<TAG>.tsv.
    """
    path = _hypothesis_log_path(tag)
    if not path.exists() or path.stat().st_size == 0:
        return []
    try:
        with _hypothesis_log_lock(tag):
            with open(path, encoding="utf-8") as f:
                lines = f.readlines()
    except OSError:
        return []
    if not lines:
        return []
    header = lines[0].rstrip("\n").split("\t")
    rows: list[dict] = []
    for line in lines[1:]:
        parts = line.rstrip("\n").split("\t")
        if len(parts) != len(header):
            continue
        row = dict(zip(header, parts))
        if since_utc is not None and row.get("written_at", "") < since_utc:
            continue
        rows.append(row)
    return rows


def load_best_so_far(tag: str | None = None) -> dict | None:
    """Public read helper for ``best_so_far_<TAG>.json``.

    Returns dict with keys:
      problem, family, score, is_valid, verifier_reason, branch_tag,
      commit, written_at, candidate.
    For capset, ``candidate`` is list[list[int]] (each list of length n).
    For sidon, ``candidate`` is list[int].
    Returns None if no valid candidate has been logged yet for this PROBLEM_TAG.

    Agents may use this to warm-start swap-moves / SA from the best valid
    set seen across any branch — strictly optional. The cache is updated
    by ``print_summary`` when a run's score beats the prior best.
    """
    path = _best_so_far_path(tag)
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        with _best_so_far_lock(tag):
            try:
                with open(path, encoding="utf-8") as f:
                    return json.load(f)
            except (json.JSONDecodeError, OSError):
                return None
    except OSError:
        return None


# --------------------------------------------------------------------------- #
# Time budget context manager — mirrors quant repo's TimeBudget shape.
# --------------------------------------------------------------------------- #

class TimeBudget:
    """Soft wall-clock wrapper. Strategies that loop should check `tb.expired`
    and bail gracefully; the verifier itself does not interrupt user code.

    Default budget is per-problem: env AUTOERDOS_TIME_BUDGET_S overrides
    problems/<tag>.json's "time_budget_s", which falls back to 900s.
    """
    def __init__(self, seconds: int | None = None):
        self.seconds = _resolve_time_budget() if seconds is None else seconds
        self._t0 = 0.0

    def __enter__(self):
        self._t0 = time.time()
        return self

    def __exit__(self, *_exc):
        return False

    @property
    def elapsed(self) -> float:
        return time.time() - self._t0

    @property
    def expired(self) -> bool:
        return self.elapsed > self.seconds
