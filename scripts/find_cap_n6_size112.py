"""One-shot: SAT-find a 112-cap in F_3^6 (Edel's literature LB) and
write it to library/data/cap_n6_size112.json so library/capset_lifts.py
can use it as a building block.

This is a build-time computation, not a runtime path. Run once per repo:

    uv run scripts/find_cap_n6_size112.py

The encoding:
  - 729 Boolean variables (one per point in F_3^6).
  - One 3-clause per 3-AP {a, b, c} with a+b+c == 0 elementwise and
    a, b, c distinct: clause is (~x_a v ~x_b v ~x_c).
  - Cardinality "at least 112" via sequential counter.

Tries target 112 first. If SAT, writes the cap. If UNSAT or interrupted,
falls back to bisecting downward (110, 108, ...) and reports the largest
size found within the budget. Anything <112 is a cache failure — caller
must NOT promote a smaller cap into cap_n6_size112.json.
"""
from __future__ import annotations

import itertools
import json
import os
import sys
import time
from pathlib import Path

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Glucose3

REPO_ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = REPO_ROOT / "library" / "data"
OUTPUT = DATA_DIR / "cap_n6_size112.json"

N = 6
TARGET = 112
CONFLICT_BUDGET = 50_000_000  # ~10-30 minutes on Glucose3


def build_3ap_clauses(n):
    points = list(itertools.product((0, 1, 2), repeat=n))
    npts = len(points)
    idx = {p: i + 1 for i, p in enumerate(points)}
    seen: set[frozenset] = set()
    clauses: list[list[int]] = []
    for i in range(npts):
        a = points[i]
        for j in range(i + 1, npts):
            b = points[j]
            c = tuple((-(a[d] + b[d])) % 3 for d in range(n))
            if c == a or c == b:
                continue
            ap = frozenset((a, b, c))
            if ap in seen:
                continue
            seen.add(ap)
            clauses.append([-idx[a], -idx[b], -idx[c]])
    return points, idx, clauses


def solve_with_target(points, idx, clauses, target, conflict_budget):
    npts = len(points)
    pool = IDPool(start_from=npts + 1)
    solver = Glucose3()
    for cl in clauses:
        solver.add_clause(cl)
    card = CardEnc.atleast(
        lits=list(range(1, npts + 1)),
        bound=target,
        top_id=pool.top,
        encoding=EncType.seqcounter,
    )
    for cl in card.clauses:
        solver.add_clause(cl)
    solver.conf_budget(conflict_budget)
    t0 = time.time()
    result = solver.solve_limited(expect_interrupt=True)
    elapsed = time.time() - t0
    if result is None:
        solver.delete()
        return None, elapsed  # budget exhausted
    if not result:
        solver.delete()
        return False, elapsed  # UNSAT
    model = solver.get_model()
    chosen = [points[i] for i in range(npts) if model[i] > 0]
    solver.delete()
    return chosen, elapsed


def main():
    print(f"Building 3-AP clauses for F_3^{N}...", flush=True)
    points, idx, clauses = build_3ap_clauses(N)
    print(f"  {len(points)} points, {len(clauses)} 3-AP clauses", flush=True)

    sizes_to_try = [TARGET, 110, 108, 106, 104, 100]
    best_cap: list[tuple[int, ...]] | None = None
    for target in sizes_to_try:
        if best_cap is not None and len(best_cap) >= target:
            continue
        print(f"\nSAT target = {target} (conflict budget = {CONFLICT_BUDGET:,})", flush=True)
        result, elapsed = solve_with_target(points, idx, clauses, target, CONFLICT_BUDGET)
        if result is None:
            print(f"  budget exhausted after {elapsed:.1f}s", flush=True)
            continue
        if result is False:
            print(f"  UNSAT in {elapsed:.1f}s — no {target}-cap exists", flush=True)
            continue
        print(f"  SAT in {elapsed:.1f}s — found {len(result)}-cap", flush=True)
        if best_cap is None or len(result) > len(best_cap):
            best_cap = result
        if target == TARGET:
            break  # success at literature LB

    if best_cap is None:
        print("\nFAIL: no cap found at any target — SAT solver budget too tight",
              file=sys.stderr)
        return 1

    # Verify cap-freeness via the same logic the verifier uses.
    seen = set(best_cap)
    for i, a in enumerate(best_cap):
        for b in best_cap[i + 1:]:
            c = tuple((-(a[d] + b[d])) % 3 for d in range(N))
            if c != a and c != b and c in seen:
                print(f"FAIL: result is not cap-free — {a}+{b}+{c}=0", file=sys.stderr)
                return 2

    if len(best_cap) < TARGET:
        print(
            f"\nWARNING: best found is size {len(best_cap)} < target {TARGET}.\n"
            f"  Refusing to write cap_n6_size112.json with a smaller cap — "
            f"that would mislead callers.\n"
            f"  Bump CONFLICT_BUDGET and retry, or accept the gap.",
            file=sys.stderr,
        )
        return 3

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    payload = {
        "n": N,
        "size": len(best_cap),
        "candidate": [list(p) for p in best_cap],
        "source": "SAT (Glucose3 + seqcounter cardinality)",
    }
    tmp = OUTPUT.with_suffix(".json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))
    os.replace(tmp, OUTPUT)
    print(f"\nwrote {OUTPUT.relative_to(REPO_ROOT)} — {len(best_cap)} points", flush=True)
    return 0


if __name__ == "__main__":
    sys.exit(main())
