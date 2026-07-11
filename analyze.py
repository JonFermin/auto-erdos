"""
analyze.py — FREE structural diagnostics of the current best candidate.

Running this costs NO trial budget: it never touches results.tsv, the
trial cache, or verifier_results.tsv. It exists because "understand why
we're stuck" is the input to good hypotheses, and a bare score provides
no gradient. Run it between trials as often as you like:

    PROBLEM_TAG=sidon_3000 uv run analyze.py            # analyze best_so_far
    PROBLEM_TAG=capset_n8  uv run analyze.py --elites   # summarize the elite archive

What it reports (family-specific):

  sidon:  size vs baseline/UB, endpoint slack, consecutive-gap profile,
          sum-density, the exact list of +1 extension points (if any),
          and near-miss points blocked by only one collision.
  capset: size vs baseline/UB, coordinate fiber profile (how the cap
          distributes over each hyperplane direction), weight histogram,
          +1 extension count, and blocked-set coverage.

The agent may paste findings into the notes channel
(`prepare.append_problem_notes`) so the NEXT session starts from them.
"""
from __future__ import annotations

import argparse
import sys
from collections import Counter

from prepare import (
    PROBLEM_TAG,
    load_best_so_far,
    load_elites,
    load_spec,
)


def _analyze_sidon(cand: list[int], spec: dict) -> None:
    N = int(spec["N"])
    pts = sorted(int(x) for x in cand)
    k = len(pts)
    print(f"size:               {k}")
    print(f"baseline / UB:      {spec.get('baseline', '?')} / {spec.get('upper_bound', '?')}")
    print(f"range used:         [{pts[0]}, {pts[-1]}] of [1, {N}]  (slack {pts[0]-1} left, {N-pts[-1]} right)")

    gaps = [b - a for a, b in zip(pts, pts[1:])]
    if gaps:
        print(f"consecutive gaps:   min {min(gaps)}  max {max(gaps)}  mean {sum(gaps)/len(gaps):.1f}")
        small = [g for g in gaps if g <= 3]
        print(f"tight gaps (<=3):   {len(small)}  ({small[:15]}{'...' if len(small) > 15 else ''})")

    sums = {pts[i] + pts[j] for i in range(k) for j in range(i, k)}
    possible = 2 * N - 1
    print(f"sum density:        {len(sums)} distinct sums of {possible} possible ({100*len(sums)/possible:.1f}%)")

    s_set = set(pts)
    addable: list[int] = []
    near_miss: list[tuple[int, int]] = []  # (x, #collisions) with exactly 1 collision
    for x in range(1, N + 1):
        if x in s_set:
            continue
        coll = (1 if (2 * x) in sums else 0) + sum(1 for a in pts if (x + a) in sums)
        if coll == 0:
            addable.append(x)
        elif coll == 1:
            near_miss.append((x, coll))
    if addable:
        print(f"+1 extensions:      {len(addable)} point(s): {addable[:20]}{'...' if len(addable) > 20 else ''}")
    else:
        print("+1 extensions:      NONE — locally maximal; +1 needs a swap (remove-k add-k+1)")
    print(f"1-collision points: {len(near_miss)}  (each blocked by a single sum — prime swap targets)")
    if near_miss:
        print(f"                    e.g. {[x for x, _ in near_miss[:15]]}")


def _analyze_capset(cand: list[list[int]], spec: dict) -> None:
    n = int(spec["n"])
    pts = [tuple(int(c) for c in p) for p in cand]
    k = len(pts)
    print(f"size:               {k}")
    print(f"baseline / UB:      {spec.get('baseline', '?')} / {spec.get('upper_bound', '?')}")
    print(f"ambient:            3^{n} = {3**n} points; cap uses {100*k/3**n:.1f}%")

    # Fiber profile: for each coordinate direction, how the cap splits
    # across the three parallel hyperplanes x_i = 0/1/2. Very uneven fibers
    # suggest room in the thin hyperplane; even fibers suggest a
    # product-like structure.
    print("fiber profile (per coordinate, counts at value 0/1/2):")
    for i in range(n):
        c = Counter(p[i] for p in pts)
        print(f"  x_{i}: {c.get(0, 0):>5} {c.get(1, 0):>5} {c.get(2, 0):>5}")

    wts = Counter(sum(1 for c in p if c != 0) for p in pts)
    print(f"weight histogram:   {dict(sorted(wts.items()))}")

    s_set = set(pts)
    blocked: set[tuple[int, ...]] = set()
    for i in range(k):
        a = pts[i]
        for j in range(i + 1, k):
            b = pts[j]
            blocked.add(tuple((-(a[d] + b[d])) % 3 for d in range(n)))
    covered = len(s_set | blocked)
    addable = 3 ** n - covered
    print(f"blocked coverage:   {covered} of {3**n} points are in-cap or AP-blocked")
    if addable:
        print(f"+1 extensions:      {addable} free point(s) — greedy +1 is still on the table")
    else:
        print("+1 extensions:      NONE — locally maximal; progress needs swap moves or a new construction")


def main() -> int:
    parser = argparse.ArgumentParser(description="Free structural diagnostics — no trial cost.")
    parser.add_argument("--elites", action="store_true",
                        help="summarize the elite archive instead of analyzing best_so_far")
    args = parser.parse_args()

    spec = load_spec()
    print(f"=== analyze: {spec['name']} (status: {spec.get('status', 'open')}) ===")

    if args.elites:
        elites = load_elites()
        if not elites:
            print("elite archive is empty — no valid candidate has been recorded yet")
            return 0
        print(f"{len(elites)} elite(s), best first:")
        for e in elites:
            print(f"  score {e.get('score'):>10}  commit {e.get('commit', '?')}  written {e.get('written_at', '?')}")
        print("load in strategy.py via prepare.load_elites() — recombination beats re-mutation of one best.")
        return 0

    best = load_best_so_far()
    if best is None:
        print("no best_so_far recorded for this problem yet — run the seed first")
        return 1
    cand = best.get("candidate", [])
    print(f"analyzing best_so_far: score {best.get('score')} (branch {best.get('branch_tag', '?')}, commit {best.get('commit', '?')})")
    family = spec.get("family")
    if family == "sidon":
        _analyze_sidon(cand, spec)
    elif family == "capset":
        _analyze_capset(cand, spec)
    else:
        print(f"no analyzer for family={family!r}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
