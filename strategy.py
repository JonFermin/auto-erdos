"""strategy.py — sidon_500 ILS depth-K kick + greedy restore.

Hypothesis: SA / swap_remove1_add2 / multi-restart greedy all explored
small (depth-1 or thermal) neighborhoods of Singer-24. Try a deeper
deterministic neighborhood: Iterated Local Search with kick depth K=3..9.

Loop:
  1. Start from best-so-far (Singer-24).
  2. While budget left: pick random K elements to drop, greedy-fill in
     random order, then attempt extend_sidon_by_one to push past 24.
  3. Track best valid set seen. Return max(best, best_so_far).

Differs from prior trials: SA uses Metropolis acceptance, swap_remove1_add2
is depth-1 SAT, multi-restart-greedy used a 6-element Singer pin-core. This
runs with kick depth K randomly in [3, 9] and uses pure hill-climbing
acceptance (only keep if strictly larger).
"""
from __future__ import annotations

import random

from library import sidon
from library.sat_extensions import extend_sidon_by_one
from prepare import (
    TimeBudget,
    load_best_so_far,
    load_spec,
    print_summary,
    verify,
)


def _is_sidon(s):
    sums = set()
    arr = sorted(s)
    for i, a in enumerate(arr):
        for b in arr[i:]:
            v = a + b
            if v in sums:
                return False
            sums.add(v)
    return True


def _greedy_fill(base, N, rng):
    chosen = sorted(set(int(x) for x in base))
    chosen_set = set(chosen)
    sums = set()
    for i, a in enumerate(chosen):
        for b in chosen[i:]:
            sums.add(a + b)
    pool = [x for x in range(1, N + 1) if x not in chosen_set]
    rng.shuffle(pool)
    for x in pool:
        new_sums = {2 * x}
        bad = (2 * x) in sums
        if not bad:
            for c in chosen:
                v = x + c
                if v in sums or v in new_sums:
                    bad = True
                    break
                new_sums.add(v)
        if not bad:
            chosen.append(x)
            chosen_set.add(x)
            sums.update(new_sums)
    return sorted(chosen)


def _ils_round(seed, N, rng, k_min=4, k_max=8):
    K = rng.randint(k_min, k_max)
    if len(seed) <= K:
        return list(seed)
    drop_idx = set(rng.sample(range(len(seed)), K))
    keep = [seed[i] for i in range(len(seed)) if i not in drop_idx]
    return _greedy_fill(keep, N, rng)


def generate_candidate(tb=None):
    spec = load_spec()
    N = int(spec["N"])

    prior = load_best_so_far()
    if prior is not None and prior.get("family") == "sidon":
        anchor = sorted(int(x) for x in prior.get("candidate", []) if 1 <= int(x) <= N)
    else:
        anchor = []
    fresh_singer = sidon.singer_for_n(N)
    if len(fresh_singer) > len(anchor):
        anchor = fresh_singer

    best = list(anchor)
    rng = random.Random(20260429)

    ext = extend_sidon_by_one(anchor, N)
    if ext is not None and len(ext) > len(best):
        best = ext

    rounds = 0
    while True:
        if tb is not None and tb.expired:
            break
        rounds += 1
        if rounds > 30000:
            break
        if rounds < 1000:
            k_min, k_max = 3, 5
        elif rounds < 5000:
            k_min, k_max = 4, 7
        else:
            k_min, k_max = 5, 9
        cand = _ils_round(best, N, rng, k_min=k_min, k_max=k_max)
        ext = extend_sidon_by_one(cand, N)
        if ext is not None:
            cand = ext
        if len(cand) > len(best):
            if _is_sidon(cand):
                best = cand
                if len(best) >= 26:
                    break

    return best


if __name__ == "__main__":
    with TimeBudget() as tb:
        candidate = generate_candidate(tb)
        result = verify(candidate)
    print_summary(candidate, result)
