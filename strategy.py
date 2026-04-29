"""
strategy.py — multi-restart randomized DFS for max-Sidon in [1,N].

Try several short DFS attempts at target=13 with different anchors and
random branch orderings. If none find size 13, fall back to seed (size 12).
Distinct AST from prior single-anchor / SAT / SA attempts.
"""
from __future__ import annotations

import itertools
import random

from library import capset, sidon
from prepare import (
    TimeBudget,
    load_best_so_far,
    load_hypothesis_log,  # noqa: F401
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
        return _seed_sidon(spec, tb)
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


def _seed_sidon(spec, tb=None):
    """Multi-restart randomized DFS targeting size-13, plus seed fallback."""
    N = int(spec["N"])
    target = 13

    # Try several short randomized DFS attempts with different anchors.
    rng = random.Random(20260429)
    anchor_set = [1, 2, 3, 4, 5]
    for anchor in anchor_set:
        if tb is not None and tb.expired:
            break
        result = _randomized_dfs_sidon(N, target, anchor, rng, max_nodes=200_000)
        if result is not None and len(result) >= target:
            return result

    # Fall back to standard seed pipeline for size-12.
    candidates: list[list] = []
    prior = load_best_so_far()
    if prior is not None and prior.get("family") == "sidon":
        prior_set = [int(x) for x in prior.get("candidate", [])]
        if prior_set and all(1 <= x <= N for x in prior_set):
            candidates.append(prior_set)
    singer = sidon.singer_for_n(N)
    if singer:
        candidates.append(singer)
    candidates.append(_randomized_greedy_sidon(N))
    return max(candidates, key=len)


def _randomized_dfs_sidon(N: int, target: int, anchor: int, rng: random.Random, max_nodes: int):
    """Randomized branch-ordering DFS for a Sidon set of size `target`.

    State: chosen list (sorted ascending), sums-set, min-next.
    Branch order: candidate ints sampled in random permutation per-node.
    """
    chosen = [anchor]
    sums = {2 * anchor}
    nodes = [0]

    def feasible_remaining(min_next: int) -> int:
        # Trivial UB: at most N - min_next + 1 + len(chosen) (loose).
        return (N - min_next + 1) + len(chosen)

    def recurse(min_next: int) -> list[int] | None:
        if len(chosen) >= target:
            return list(chosen)
        if nodes[0] >= max_nodes:
            return None
        if feasible_remaining(min_next) < target:
            return None
        # Build feasible candidates [min_next, N] preserving Sidon.
        feasible: list[int] = []
        for x in range(min_next, N + 1):
            two_x = 2 * x
            if two_x in sums:
                continue
            ok = True
            for c in chosen:
                if (x + c) in sums:
                    ok = False
                    break
            if ok:
                feasible.append(x)
        # Randomize branch order per call.
        rng.shuffle(feasible)
        for x in feasible:
            nodes[0] += 1
            new_sums: list[int] = [2 * x]
            for c in chosen:
                new_sums.append(x + c)
            chosen.append(x)
            sums.update(new_sums)
            res = recurse(x + 1)
            if res is not None:
                return res
            chosen.pop()
            for s in new_sums:
                sums.discard(s)
        return None

    return recurse(anchor + 1)


def _randomized_greedy_capset(n):
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
