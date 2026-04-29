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

    # Hyp [SAT]: search F_3^6 for a cap of size > 121. cap_n3_size9 ⊗ cap_n6
    # gives 9 * size in F_3^9. To beat 1082, need size >= 121 in F_3^6.
    # Lit LB n=6 is 112. Try SAT(112) first as feasibility check, then SA
    # to push higher.
    if n == 9:
        cap6 = _sat_then_sa_v2(n=6, sat_target=100, sa_target=121,
                                time_limit_s=900, restart_seed=0)
        if cap6 is not None and len(cap6) >= 121:
            cap3 = capset.cap_n3_size9()
            lifted = capset.product_lift(cap6, 6, cap3, 3)
            candidates.append(lifted)

    return max(candidates, key=len)


def _sat_then_sa_v2(n, sat_target, sa_target, time_limit_s, restart_seed=0):
    """SAT-warm + SA hill-climb in F_3^n."""
    import math
    import time
    from pysat.card import CardEnc, EncType
    from pysat.formula import IDPool
    from pysat.solvers import Glucose3

    t0 = time.time()
    points = list(itertools.product((0, 1, 2), repeat=n))
    point_to_idx = {p: i for i, p in enumerate(points)}

    pool = IDPool()
    var = [pool.id(("p", i)) for i in range(len(points))]
    solver = Glucose3()
    for i in range(len(points)):
        a = points[i]
        for j in range(i + 1, len(points)):
            b = points[j]
            c = tuple((-(a[d] + b[d])) % 3 for d in range(n))
            if c == a or c == b:
                continue
            k = point_to_idx[c]
            if k <= j:
                continue
            solver.add_clause([-var[i], -var[j], -var[k]])
    cnf = CardEnc.atleast(lits=var, bound=sat_target, encoding=EncType.seqcounter, vpool=pool)
    for cl in cnf.clauses:
        solver.add_clause(cl)
    if restart_seed > 0:
        solver.add_clause([var[restart_seed % len(points)]])
    if not solver.solve():
        solver.delete()
        return None
    model = solver.get_model()
    solver.delete()
    if model is None:
        return None
    ms = set(model)
    cap = [points[i] for i in range(len(points)) if var[i] in ms]
    best = list(cap)
    if len(best) >= sa_target:
        return best

    rng = random.Random(31415 + restart_seed * 7)
    cap_set = set(cap)
    forbid_count: dict[tuple[int, ...], int] = {}
    for i in range(len(cap)):
        a = cap[i]
        for j in range(i + 1, len(cap)):
            b = cap[j]
            r = tuple((-(a[d] + b[d])) % 3 for d in range(n))
            if r != a and r != b:
                forbid_count[r] = forbid_count.get(r, 0) + 1
    iters = 0
    while time.time() - t0 < time_limit_s:
        iters += 1
        frac = (time.time() - t0) / time_limit_s
        T = max(0.05, 2.5 * (1.0 - frac))
        if rng.random() < 0.5 and len(cap) > 0:
            x = cap[rng.randrange(len(cap))]
            if rng.random() < math.exp(-1.0 / T):
                cap.remove(x)
                cap_set.discard(x)
                for c in cap:
                    r = tuple((-(c[d] + x[d])) % 3 for d in range(n))
                    if r != c and r != x:
                        forbid_count[r] -= 1
                        if forbid_count[r] == 0:
                            del forbid_count[r]
        else:
            for _ in range(40):
                q = points[rng.randrange(len(points))]
                if q in cap_set or q in forbid_count:
                    continue
                for c in cap:
                    r = tuple((-(c[d] + q[d])) % 3 for d in range(n))
                    if r != c and r != q:
                        forbid_count[r] = forbid_count.get(r, 0) + 1
                cap.append(q)
                cap_set.add(q)
                break
        if len(cap) > len(best):
            best = list(cap)
            if len(best) >= sa_target:
                return best
    return best


def _seed_sidon(spec):
    N = int(spec["N"])
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
