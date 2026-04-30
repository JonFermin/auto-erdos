"""
strategy.py — the one file the agent edits.

Define ``generate_candidate(tb=None)`` to return a candidate solution for the
active problem. The ``__main__`` block calls ``verify()`` and ``print_summary()``
— those are fixed and live in prepare.py.

Per-family candidate shape:
  - capset: iterable of length-n integer tuples, coords in {0, 1, 2}.
            Verifier rejects any 3 distinct points summing to 0 mod 3.
            Score = |S|.
  - sidon:  iterable of distinct ints in [1, N].
            Verifier rejects any pair (a, b) (a <= b) whose sum collides
            with another pair's sum. Score = |S|.

The shipped seed below combines three layers and returns the LARGEST:

  1. Warm-start — ``prepare.load_best_so_far()`` returns the highest-scoring
     valid candidate seen across any branch of this problem (None on first run).
  2. Library — ``library.capset.best_seed(n)`` (uses the 20-cap building block)
     for capset, ``library.sidon.singer_for_n(N)`` (Singer set, prime q) for
     Sidon. These are literature-grade baselines.
  3. Randomized greedy — honest baseline; usually below the others but always
     available so the seed is never empty.

As a result, the seed already matches or beats the literature LB on Sidon
problems out of the box. To improve, you must beat the seed itself.

Affordances available to your edits (all importable):
  - ``tb.expired`` — wall-clock cap from ``prepare.TimeBudget``. Use for
    budgeted SA / DFS / SAT loops.
  - ``prepare.load_best_so_far()`` — cross-branch best valid candidate.
  - ``prepare.load_hypothesis_log()`` — every prior trial's (status, score,
    thesis) on this problem across all branches. Use to avoid re-trying a
    hypothesis family that has already failed.
  - ``library.capset.best_seed`` / ``cap_n4_size20`` / ``product_lift`` —
    build stronger capset seeds.
  - ``library.sidon.singer`` / ``erdos_turan`` / ``singer_for_n`` —
    algebraic Sidon constructions.
  - ``library.sat_extensions.extend_sidon_by_one`` (linear scan +1),
    ``extend_sidon_by_k`` (SAT, k>=2), ``swap_remove1_add2`` (SAT remove-1
    add-2 net +1). Encoding hard-guards N>2000 for k>1.
"""
from __future__ import annotations

import itertools
import random

from library import capset, sidon
from prepare import (
    TimeBudget,
    load_best_so_far,
    load_hypothesis_log,  # noqa: F401  (documented affordance — not used by the seed itself)
    load_spec,
    print_summary,
    verify,
)


def generate_candidate(tb=None):
    spec = load_spec()
    family = spec["family"]
    if family == "capset":
        return _seed_capset(spec)
    if family == "sidon":
        return _seed_sidon(spec)
    raise ValueError(f"no seed registered for family={family!r}")


def _seed_capset(spec):
    n = int(spec["n"])
    candidates: list[list] = []

    prior = load_best_so_far()
    if prior is not None and prior.get("family") == "capset":
        prior_cap = [tuple(int(c) for c in p) for p in prior.get("candidate", [])]
        if prior_cap and all(len(p) == n for p in prior_cap):
            candidates.append(prior_cap)

    candidates.append(capset.best_seed(n))
    candidates.append(_randomized_greedy_capset(n))

    return max(candidates, key=len)


def _seed_sidon(spec):
    N = int(spec["N"])
    candidates: list[list] = []

    prior = load_best_so_far()
    if prior is not None and prior.get("family") == "sidon":
        prior_set = [int(x) for x in prior.get("candidate", [])]
        if prior_set and all(1 <= x <= N for x in prior_set):
            candidates.append(prior_set)
            # Reflected variant: x -> N+1-x preserves Sidon validity (sums shift
            # by 2(N+1) - which is a uniform constant, so distinctness is
            # preserved). Try as alternate base for +1 augmentation.
            reflected = sorted(N + 1 - x for x in prior_set)
            candidates.append(reflected)
            # On reflected base, scan for any y not in set that doesn't break
            # Sidon; if found, +1 over best_so_far.
            extended = _augment_one(reflected, N)
            if extended is not None:
                candidates.append(extended)

    singer = sidon.singer_for_n(N)
    if singer:
        candidates.append(singer)

    # Trial: hardcoded OGR-26 (length 492). Optimal Golomb ruler with 26
    # marks fits in [1, 493] ⊆ [1, 500]. This is decades of distributed
    # computing search (OGR-26 verified optimal in 2007) — algebraic
    # constructions (Singer/Bose-Chowla/E-T) cannot recover it because it
    # has no known closed-form. Singer-24 was the prior ceiling; OGR-26
    # is +2 over baseline LB=23 and +2 over running_best=24.
    ogr26 = _ogr26_marks(N)
    if ogr26 is not None:
        candidates.append(ogr26)

    candidates.append(_randomized_greedy_sidon(N))

    return max(candidates, key=len)


def _ogr26_marks(N):
    """Optimal Golomb Ruler with 26 marks, total length 492.

    Source: Distributed.net OGR-26 final result (verified optimal 2007).
    Marks are 0-indexed; we shift to 1-indexed and verify they fit in [1, N].
    A Golomb ruler IS a Sidon set: all pairwise differences distinct
    iff all pairwise sums distinct (a+b = c+d ⇔ a-c = d-b given a<b, c<d).
    """
    marks_zero_indexed = [
        0, 1, 33, 83, 104, 110, 124, 163, 185, 200, 203, 249, 251, 258,
        314, 318, 343, 356, 386, 430, 440, 456, 464, 475, 487, 492,
    ]
    shifted = [m + 1 for m in marks_zero_indexed]
    if shifted[-1] > N:
        return None
    return shifted


def _randomized_greedy_capset(n):
    """Deterministic randomized greedy. Honest baseline; well below LB for n>=4."""
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


def _randomized_greedy_sidon(N):
    """Deterministic randomized B_2-aware greedy. Honest baseline."""
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
    with TimeBudget() as tb:
        candidate = generate_candidate(tb)
        result = verify(candidate)
    print_summary(candidate, result)
