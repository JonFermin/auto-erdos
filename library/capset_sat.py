"""SAT-based cap-set extension helpers — analog of library.sat_extensions
for the Sidon family.

Public:
  extend_capset_by_one(seed, n) -> list[tuple[int,...]] | None
      Linear scan over 3^n - |seed| candidate points. Adds the first
      point that doesn't complete a 3-AP with any pair of seed points.
      No SAT — fast.

  extend_capset_by_k(seed, n, k, *, time_limit_s=60) -> list[tuple[int,...]] | None
      SAT-based: var per candidate point, hard clauses for any 3-AP that
      includes >=1 seed point (the seed points already pin those vars to
      true), plus pure-candidate 3-AP clauses. Cardinality at-least-k.
      CEGAR loop: solve, verify cap-freeness across (seed ∪ chosen), block
      bad assignment if the solver picked a violating triple, retry.

      Hard guard: raises RuntimeError if 3^n > 20000 (i.e., n >= 10) since
      the var count makes the encoding impractical. Use orbit-sweep + +1
      extension at n=10 instead.

  swap_remove_k_add_kplus1(seed, n, k, *, time_limit_s=120) -> ...
      Net +1 swap. Drop k seed points, run extend_capset_by_k(k+1).

Inputs/outputs are sorted lists of length-n integer tuples with coords in
{0, 1, 2}. "Cap-free" means no three distinct points sum to 0 elementwise
mod 3.
"""
from __future__ import annotations

import itertools
import time
from typing import Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Glucose3


_MAX_VARS = 20_000  # 3^9 = 19683 — anything larger is impractical for SAT.


def _all_points(n: int) -> list[tuple[int, ...]]:
    return list(itertools.product((0, 1, 2), repeat=n))


def _third_ap_point(a: tuple[int, ...], b: tuple[int, ...], n: int) -> tuple[int, ...]:
    """For points a, b in F_3^n, the unique c with a+b+c=0 elementwise mod 3."""
    return tuple((-(a[d] + b[d])) % 3 for d in range(n))


# --------------------------------------------------------------------------- #
# +1 extension: linear scan
# --------------------------------------------------------------------------- #

def extend_capset_by_one(
    seed: Iterable[Iterable[int]],
    n: int,
) -> list[tuple[int, ...]] | None:
    """Try to add a single point to seed in F_3^n preserving cap-freeness.

    Linear in 3^n: precomputes the set of points that would complete a
    3-AP with two seed points (forbidden points), then returns the first
    non-forbidden, non-seed point.

    Returns the extended cap (sorted), or None if seed is locally maximal.
    """
    seed_set: set[tuple[int, ...]] = {tuple(int(c) for c in p) for p in seed}
    seed_list = sorted(seed_set)
    forbidden: set[tuple[int, ...]] = set(seed_set)
    for i, a in enumerate(seed_list):
        for b in seed_list[i + 1:]:
            c = _third_ap_point(a, b, n)
            if c == a or c == b:
                continue
            forbidden.add(c)
    for x in itertools.product((0, 1, 2), repeat=n):
        if x in forbidden:
            continue
        return sorted(seed_list + [x])
    return None


# --------------------------------------------------------------------------- #
# +k extension: SAT with CEGAR
# --------------------------------------------------------------------------- #

def extend_capset_by_k(
    seed: Iterable[Iterable[int]],
    n: int,
    k: int,
    *,
    time_limit_s: float = 60.0,
) -> list[tuple[int, ...]] | None:
    """Add k extra points to seed in F_3^n preserving cap-freeness — SAT.

    For k == 1, falls through to extend_capset_by_one (linear scan).

    Encoding:
      - One Boolean per candidate point in F_3^n \\ seed not already
        "burned" (i.e., would complete a 3-AP with two seed points).
      - For each unordered pair (x, y) of candidates whose third AP point
        c lies in seed: post (~x v ~y) — picking both completes a 3-AP
        with the seed point c.
      - For each unordered pair (x, y) of candidates whose third AP point
        c is also a candidate: post (~x v ~y v ~c) — pure-candidate 3-AP.
      - Cardinality "at least k" via seqcounter.
      - CEGAR loop: solve, verify cap-freeness across (seed ∪ chosen),
        block the assignment if any 3-AP is found, retry.

    Hard guard: raises RuntimeError if 3^n > 20000.

    Returns the extended cap (sorted), or None on UNSAT or timeout.
    """
    if k <= 0:
        return sorted({tuple(int(c) for c in p) for p in seed})
    if k == 1:
        return extend_capset_by_one(seed, n)

    npts_total = 3 ** n
    if npts_total > _MAX_VARS:
        raise RuntimeError(
            f"extend_capset_by_k(n={n}, k={k}) — 3^n = {npts_total} > {_MAX_VARS}; "
            f"encoding too large. Use orbit-sweep + extend_capset_by_one at n>=10."
        )

    seed_set: set[tuple[int, ...]] = {tuple(int(c) for c in p) for p in seed}
    seed_list = sorted(seed_set)

    # Pre-burn: candidate must not already form a 3-AP with two seed points.
    burned: set[tuple[int, ...]] = set(seed_set)
    for i, a in enumerate(seed_list):
        for b in seed_list[i + 1:]:
            c = _third_ap_point(a, b, n)
            if c == a or c == b:
                continue
            burned.add(c)

    candidates = [p for p in _all_points(n) if p not in burned]
    if len(candidates) < k:
        return None

    pool = IDPool()
    var = {p: pool.id(p) for p in candidates}
    cand_set = set(candidates)
    seed_lookup = seed_set  # for membership tests in the inner loop

    solver = Glucose3()

    # Pair forbids (3-AP with seed) and triple forbids (pure-candidate 3-AP).
    cand_list = candidates
    for i, x in enumerate(cand_list):
        for j in range(i + 1, len(cand_list)):
            y = cand_list[j]
            c = _third_ap_point(x, y, n)
            if c == x or c == y:
                continue
            if c in seed_lookup:
                # 3-AP {x, y, c} with c in seed: picking x and y completes it.
                solver.add_clause([-var[x], -var[y]])
            elif c in cand_set:
                # Pure-candidate 3-AP {x, y, c}: at most 2 of three.
                # Post (~x v ~y v ~c) once per unordered triple — to avoid
                # triplicate posting, only when (x, y, c) is in canonical
                # order x < y < c (lexicographic on tuple).
                if c > y:
                    solver.add_clause([-var[x], -var[y], -var[c]])

    card = CardEnc.atleast(
        lits=list(var.values()),
        bound=k,
        top_id=pool.top,
        encoding=EncType.seqcounter,
    )
    for cl in card.clauses:
        solver.add_clause(cl)

    deadline = time.time() + time_limit_s
    try:
        while time.time() < deadline:
            if not solver.solve():
                return None
            model = solver.get_model()
            true_set = {abs(lit) for lit in model if lit > 0}
            chosen = sorted(p for p in candidates if var[p] in true_set)
            if len(chosen) > k:
                chosen = chosen[:k]

            # Full CEGAR check across (seed ∪ chosen).
            full = sorted(seed_list + chosen)
            full_set = set(full)
            ok = True
            violated_pair: tuple | None = None
            for i, a in enumerate(full):
                for b in full[i + 1:]:
                    c = _third_ap_point(a, b, n)
                    if c == a or c == b:
                        continue
                    if c in full_set:
                        # 3-AP detected. Pick a candidate-side pair to block.
                        in_chosen = [p for p in (a, b, c) if p in cand_set]
                        if len(in_chosen) >= 2:
                            violated_pair = tuple(in_chosen[:2])
                        else:
                            violated_pair = (a, b)
                        ok = False
                        break
                if not ok:
                    break

            if ok:
                return full

            # Block this assignment via the chosen-set rather than just
            # the violating pair (the violation may depend on the seed too).
            solver.add_clause([-var[p] for p in chosen])
        return None  # timeout
    finally:
        solver.delete()


# --------------------------------------------------------------------------- #
# Net-+1 swap: drop k seed points, add k+1 new ones.
# --------------------------------------------------------------------------- #

def swap_remove_k_add_kplus1(
    seed: Iterable[Iterable[int]],
    n: int,
    k: int,
    *,
    time_limit_s: float = 120.0,
) -> list[tuple[int, ...]] | None:
    """Try to drop k points from seed and add k+1 new ones in F_3^n,
    yielding a cap of size |seed| + 1.

    Iterates over k-subsets of seed (in sorted order) and runs
    extend_capset_by_k(k+1) on each remaining set. Returns the first
    successful swap, or None if budget exhausts.

    Deterministic ordering — the seed is sorted, so the same call returns
    the same result on the same inputs. For randomization, shuffle the
    output of itertools.combinations externally.
    """
    seed_list = sorted({tuple(int(c) for c in p) for p in seed})
    if len(seed_list) <= k:
        return None
    deadline = time.time() + time_limit_s
    for drop in itertools.combinations(range(len(seed_list)), k):
        remaining_s = deadline - time.time()
        if remaining_s <= 0.5:
            return None
        smaller = [seed_list[i] for i in range(len(seed_list)) if i not in set(drop)]
        result = extend_capset_by_k(
            smaller, n, k + 1,
            time_limit_s=remaining_s,
        )
        if result is not None and len(result) == len(seed_list) + 1:
            return result
    return None
