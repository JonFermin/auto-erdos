"""
prepare.py — READ-ONLY verifier and driver helpers.

The agent never edits this file. It exposes:
  - verify(candidate) -> VerifyResult
  - print_summary(candidate, result): emits the metric block parsed by log_result.py
        and appends a row to verifier_results.tsv (the harness-side audit trail
        log_result.py reads to compute keep/discard).
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
import os
import subprocess
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Sequence

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
TIME_BUDGET_S = int(os.environ.get("AUTOERDOS_TIME_BUDGET_S", "900"))


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
    """Verify candidate ⊂ [1, N] is a Sidon (B_2) set: all pairwise sums
    a+b with a < b are distinct. Equivalently, all positive differences
    are distinct. O(k^2) where k = |candidate|.
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
    for i in range(k):
        a = pts[i]
        for j in range(i + 1, k):
            b = pts[j]
            s = a + b
            prev = sums.get(s)
            if prev is not None:
                return VerifyResult(
                    False, 0.0,
                    f"duplicate sum {s}: ({a},{b}) collides with ({prev[0]},{prev[1]})",
                    time.time() - t0,
                )
            sums[s] = (a, b)

    return VerifyResult(True, float(k), f"valid Sidon set of size {k} in [1,{N}]", time.time() - t0)


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
    """Emit the fixed metric block and append a row to verifier_results.tsv."""
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
# Time budget context manager — mirrors quant repo's TimeBudget shape.
# --------------------------------------------------------------------------- #

class TimeBudget:
    """Soft wall-clock wrapper. Strategies that loop should check `tb.expired`
    and bail gracefully; the verifier itself does not interrupt user code.
    """
    def __init__(self, seconds: int = TIME_BUDGET_S):
        self.seconds = seconds
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
