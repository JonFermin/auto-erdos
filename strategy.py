"""
strategy.py — the one file the agent edits.

Define `generate_candidate()` to return a candidate solution for the active
problem. The __main__ block calls verify() and print_summary() — those are
fixed and live in prepare.py.

Per-family candidate shape:
  - capset: iterable of length-n integer tuples, coords in {0, 1, 2}.
            Verifier rejects any 3 distinct points summing to 0 mod 3.
            Score = |S|.
  - sidon: iterable of distinct ints in [1, N].
            Verifier rejects any pair (a,b) (a<b) whose sum collides with
            another pair's sum. Score = |S|.

Seeds below are randomized greedy — honest baselines, well below the
literature lower bound for nontrivial problem sizes. The agent's job is
to close that gap with constructions, local search, etc.
"""
from __future__ import annotations

import itertools
import random

from prepare import TimeBudget, load_spec, print_summary, verify


def generate_candidate():
    spec = load_spec()
    family = spec["family"]
    if family == "capset":
        return _seed_capset(spec)
    if family == "sidon":
        return _seed_sidon(spec)
    raise ValueError(f"no seed registered for family={family!r}")


def _seed_capset(spec):
    """Randomized greedy: shuffle all 3^n points, walk them in order,
    accept any point that doesn't complete a 3-term AP with two existing
    chosen points. Deterministic via fixed seed.
    """
    n = int(spec["n"])
    rng = random.Random(0)
    all_points = list(itertools.product((0, 1, 2), repeat=n))
    rng.shuffle(all_points)
    chosen: list[tuple[int, ...]] = []
    chosen_set: set[tuple[int, ...]] = set()
    for p in all_points:
        ok = True
        for a in chosen:
            b = tuple((-(a[d] + p[d])) % 3 for d in range(n))
            if b == a or b == p:
                continue
            if b in chosen_set:
                ok = False
                break
        if ok:
            chosen.append(p)
            chosen_set.add(p)
    return chosen


def _seed_sidon(spec):
    """Randomized B_2-aware greedy: shuffle [1, N], walk in order, accept x
    if (a) 2x is not already a pairwise sum AND (b) every x+c for c in
    chosen is also not an existing sum. Tracks the degenerate 2c sums
    that B_2 (canonical Sidon) requires. Deterministic via fixed seed.
    """
    N = int(spec["N"])
    rng = random.Random(0)
    candidates = list(range(1, N + 1))
    rng.shuffle(candidates)
    chosen: list[int] = []
    sums: set[int] = set()
    for x in candidates:
        s_2x = 2 * x
        if s_2x in sums:
            continue
        ok = True
        new_sums: list[int] = [s_2x]
        for c in chosen:
            s = x + c
            if s in sums:
                ok = False
                break
            new_sums.append(s)
        if ok:
            chosen.append(x)
            sums.update(new_sums)
    return sorted(chosen)


if __name__ == "__main__":
    with TimeBudget():
        candidate = generate_candidate()
        result = verify(candidate)
    print_summary(candidate, result)
