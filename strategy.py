"""
strategy.py — the one file the agent edits.

Define `generate_candidate()` to return a candidate solution for the active
problem. The __main__ block calls verify() and print_summary() — those are
fixed and live in prepare.py.

For the capset family: return an iterable of length-n integer tuples, each
coordinate in {0, 1, 2}. The verifier checks no 3 distinct points sum to 0
mod 3, and scores by |S|.

Seed: randomized greedy. Shuffle all 3^n points, walk them in order, accept
any point that does not complete a 3-term AP with two existing points.
A naive but honest baseline — non-trivially big, far from the literature
lower bound for n>=8, lots of headroom for the agent to improve.
"""
from __future__ import annotations

import itertools
import random

from prepare import TimeBudget, load_spec, print_summary, verify


def generate_candidate():
    spec = load_spec()
    n = int(spec["n"])

    # Deterministic seed for reproducibility — when the agent changes the
    # algorithm it should also change the seed (or remove the seed) so that
    # the AST-dedup catches genuine no-ops, not "different seed, same code".
    rng = random.Random(0)

    all_points = list(itertools.product((0, 1, 2), repeat=n))
    rng.shuffle(all_points)

    chosen: list[tuple[int, ...]] = []
    chosen_set: set[tuple[int, ...]] = set()
    for p in all_points:
        ok = True
        for a in chosen:
            # b = -(a + p) mod 3 completes the 3-term AP.
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


if __name__ == "__main__":
    with TimeBudget():
        candidate = generate_candidate()
        result = verify(candidate)
    print_summary(candidate, result)
