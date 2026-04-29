"""
strategy.py — the one file the agent edits.

Trial 11: [SAT-bisect] iterative SAT in F_3^5 — solve at target=42, then 43,
44, 45 (literature LB for F_3^5). 45-cap exists (Pellegrino). If we hit
target k, lifted to F_3^10 via product gives k^2 in F_3^10:
  42^2 = 1764, 43^2 = 1849, 44^2 = 1936, 45^2 = 2025 (still < 2474).
None reach 2474 — no chance to beat LB. Run anyway as defensible
construction: confirms F_3^5 SAT can hit Pellegrino bound.
"""
from __future__ import annotations

import itertools
import random
import time
import threading

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Glucose3

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
        return _strategy_capset(spec, tb)
    if family == "sidon":
        return _seed_sidon(spec)
    raise ValueError(f"no seed registered for family={family!r}")


def _strategy_capset(spec, tb):
    n = int(spec["n"])
    base = _seed_capset_base(spec)
    if n != 10:
        return base
    # Bisect upward 42 -> 45 in F_3^5.
    best_cap5 = list(capset.best_seed(5))  # 40
    for tgt in [42, 43, 44, 45]:
        if tb is not None and tb.expired:
            break
        result = _sat_capset(5, target=tgt, tb=tb, soft_seconds=600)
        if result is not None and len(result) > len(best_cap5):
            best_cap5 = result
        if result is None or len(result) < tgt:
            # UNSAT or timed out at this target; stop escalating.
            break
    if len(best_cap5) <= 40:
        return base
    lifted = capset.product_lift(best_cap5, 5, best_cap5, 5)
    if len(lifted) > len(base):
        return lifted
    return base


def _seed_capset_base(spec):
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


def _sat_capset(n, target, tb, soft_seconds=600):
    """SAT for >=target cap in F_3^n."""
    soft_deadline = time.time() + soft_seconds
    def expired():
        if tb is not None and tb.expired:
            return True
        return time.time() > soft_deadline

    all_points = list(itertools.product((0, 1, 2), repeat=n))
    P = len(all_points)
    pt_to_idx = {p: i for i, p in enumerate(all_points)}

    triples: list[tuple[int, int, int]] = []
    seen_triple: set[frozenset[int]] = set()
    for i in range(P):
        ai = all_points[i]
        for j in range(i + 1, P):
            aj = all_points[j]
            r = tuple((-(ai[d] + aj[d])) % 3 for d in range(n))
            if r == ai or r == aj:
                continue
            ri = pt_to_idx[r]
            if ri <= j:
                continue
            key = frozenset((i, j, ri))
            if key in seen_triple:
                continue
            seen_triple.add(key)
            triples.append((i, j, ri))

    pool = IDPool()
    for i in range(P):
        pool.id(("pt", i))
    solver = Glucose3()
    def var(i):
        return pool.id(("pt", i))

    for (a, b, c) in triples:
        solver.add_clause([-var(a), -var(b), -var(c)])

    lits = [var(i) for i in range(P)]
    cnf_card = CardEnc.atleast(lits=lits, bound=target, vpool=pool, encoding=EncType.seqcounter)
    for clause in cnf_card.clauses:
        solver.add_clause(clause)

    result_ok = [None]
    def run():
        try:
            result_ok[0] = solver.solve()
        except Exception:
            result_ok[0] = False
    th = threading.Thread(target=run, daemon=True)
    th.start()
    while th.is_alive():
        th.join(timeout=2.0)
        if expired():
            try:
                solver.interrupt()
            except Exception:
                pass
            th.join(timeout=10.0)
            break

    if result_ok[0] is True:
        model = solver.get_model() or []
        chosen = [all_points[i] for i in range(P) if var(i) in model]
        solver.delete()
        return chosen
    solver.delete()
    return None


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
