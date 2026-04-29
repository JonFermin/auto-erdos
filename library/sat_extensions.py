"""Sidon (B_2) extension helpers — scan + SAT.

Public:
  extend_sidon_by_one(seed, N, *, exclude=None) -> list[int] | None
      Try to add a single element x in [1, N] outside `exclude` (default: seed)
      such that the result is still a B_2 Sidon set. Linear scan; no SAT.

  extend_sidon_by_k(seed, N, k, *, exclude=None, time_limit_s=30) -> list[int] | None
      Find k extra elements in [1, N] outside `exclude` (default: seed) that
      preserve B_2. SAT-based with a CEGAR loop on candidate-vs-candidate
      sum collisions. Hard guard: raises if N > 2000 and k > 1.

  swap_remove1_add2(seed, N, *, time_limit_s=60) -> list[int] | None
      Net +1 swap: drop one seed element, add two new ones. Iterates over
      seed elements to drop and runs extend_by_k(2) on each; returns the
      first valid swap.

All inputs/outputs are sorted lists of distinct ints in [1, N]. Sidon means
B_2: a+b = c+d with a<=b, c<=d implies (a,b) = (c,d) — i.e. all multi-set
sums are distinct, including the degenerate 2a case.

The SAT functions use python-sat (already a project dep). Integration:

    from library.sidon import singer_for_n
    from library.sat_extensions import extend_sidon_by_one

    seed = singer_for_n(spec["N"])
    extended = extend_sidon_by_one(seed, spec["N"])
    if extended is not None:
        return extended           # +1 result
    return seed                   # locally maximal, return seed
"""
from __future__ import annotations
import time
from typing import Iterable

from pysat.card import CardEnc, EncType
from pysat.formula import IDPool
from pysat.solvers import Glucose3


# --------------------------------------------------------------------------- #
# +1 extension: linear scan
# --------------------------------------------------------------------------- #

def extend_sidon_by_one(
    seed: Iterable[int],
    N: int,
    *,
    exclude: Iterable[int] | None = None,
) -> list[int] | None:
    """Try to add a single x in [1, N] preserving B_2.

    `exclude` defaults to `seed`; pass a superset (e.g., when called from
    swap_remove1_add2 with the original seed) to forbid a wider range.

    Returns the extended set (sorted), or None if no x fits.

    Linear in N: builds the seed-sum set once, then for each candidate x
    checks all len(seed)+1 new sums against it.
    """
    seed_list = sorted(set(int(s) for s in seed))
    seed_set = set(seed_list)
    excl = set(int(x) for x in exclude) if exclude is not None else seed_set
    seed_sums: set[int] = set()
    for i, a in enumerate(seed_list):
        for b in seed_list[i:]:
            seed_sums.add(a + b)
    for x in range(1, N + 1):
        if x in excl:
            continue
        new_sums: set[int] = {2 * x}
        bad = False
        for s in seed_list:
            v = x + s
            if v in seed_sums or v in new_sums:
                bad = True
                break
            new_sums.add(v)
        if bad:
            continue
        if 2 * x in seed_sums:
            continue
        return sorted(seed_list + [x])
    return None


# --------------------------------------------------------------------------- #
# +k extension: SAT with CEGAR
# --------------------------------------------------------------------------- #

def extend_sidon_by_k(
    seed: Iterable[int],
    N: int,
    k: int,
    *,
    exclude: Iterable[int] | None = None,
    time_limit_s: float = 30.0,
) -> list[int] | None:
    """Find k extra elements in [1, N] preserving B_2 — SAT-based.

    For k == 1, falls through to extend_sidon_by_one (linear scan).

    Encoding:
      - One Boolean per candidate x in [1, N] \\ exclude not already
        forbidden by a candidate-vs-seed sum collision.
      - For each pair of candidates (x, y) where x + y is already a seed
        sum, post a clause ~x v ~y.
      - Cardinality "at least k true" via seqcounter encoding.
      - CEGAR loop: solve, check candidate-vs-candidate sum collisions
        among picked points; if any, post a blocking clause and retry.

    Hard guard: raises RuntimeError if N > 2000 and k > 1 (encoding too
    large to be safe). Use bisection or scan-extend-by-one in that range.

    Returns the extended set (sorted), or None on UNSAT or timeout.
    """
    if k <= 0:
        return sorted(set(int(s) for s in seed))
    if k == 1:
        return extend_sidon_by_one(seed, N, exclude=exclude)
    if N > 2000:
        raise RuntimeError(
            f"extend_sidon_by_k(N={N}, k={k}) encoding too large; "
            f"bisect or use extend_sidon_by_one"
        )

    seed_list = sorted(set(int(s) for s in seed))
    seed_set = set(seed_list)
    excl = set(int(x) for x in exclude) if exclude is not None else seed_set
    seed_sums: set[int] = set()
    for i, a in enumerate(seed_list):
        for b in seed_list[i:]:
            seed_sums.add(a + b)
    seed_diffs: set[int] = {b - a for i, a in enumerate(seed_list)
                            for b in seed_list[i + 1:]}

    # Build candidate list, dropping x's with immediate seed-vs-x collisions.
    candidates: list[int] = []
    for x in range(1, N + 1):
        if x in excl:
            continue
        if (2 * x) in seed_sums:
            continue
        if any((x + s) in seed_sums for s in seed_list):
            continue
        candidates.append(x)

    if len(candidates) < k:
        return None

    pool = IDPool()
    var = {x: pool.id(x) for x in candidates}

    solver = Glucose3()

    # Pair-forbids: rule out obviously-bad pairs (p < q) by binary constraints.
    # The remaining 3-ary / 4-ary collisions are caught by the CEGAR loop.
    #   (a) p + q in seed_sums:
    #         (p, q) and (s1, s2) collide.
    #   (b) (q - p) in seed_diffs (equivalently: q - p = t - s for some
    #       seed pair s < t):
    #         (p, t) and (q, s) collide via p + t = q + s.
    #   (c) (2 p - q) in seed:
    #         (p, p) and (q, s) collide where s = 2p - q.
    #   (d) (2 q - p) in seed:
    #         (q, q) and (p, s) collide where s = 2q - p.
    for i, p in enumerate(candidates):
        for j in range(i + 1, len(candidates)):
            q = candidates[j]
            forbid = False
            if (p + q) in seed_sums:
                forbid = True
            elif (q - p) in seed_diffs:
                forbid = True
            elif (2 * p - q) in seed_set:
                forbid = True
            elif (2 * q - p) in seed_set:
                forbid = True
            if forbid:
                solver.add_clause([-var[p], -var[q]])

    # Cardinality: at least k of the candidate vars true.
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
            chosen = sorted(x for x in candidates if var[x] in true_set)
            # Cardinality is "at least k"; trim to the smallest k.
            if len(chosen) > k:
                chosen = chosen[:k]

            # Full CEGAR check: every B_2 sum across (seed ∪ chosen) must be
            # unique. Cheaper than re-running the full verifier and guaranteed
            # correct.
            full = sorted(seed_list + chosen)
            sums_seen: dict[int, tuple[int, int]] = {}
            violated_pair: tuple[int, int] | None = None
            ok = True
            for i, a in enumerate(full):
                for b in full[i:]:
                    s = a + b
                    if s in sums_seen:
                        # Pick a candidate-side pair to block: prefer the
                        # (a, b) pair with at least one element in chosen.
                        prev = sums_seen[s]
                        if a in chosen or b in chosen:
                            violated_pair = (a, b)
                        else:
                            violated_pair = prev
                        ok = False
                        break
                    sums_seen[s] = (a, b)
                if not ok:
                    break
            if ok:
                return full
            # Block this assignment. We block the specific selection of
            # `chosen` rather than just the violated pair, since the
            # violation may depend on the seed too.
            solver.add_clause([-var[x] for x in chosen])
        return None  # timeout
    finally:
        solver.delete()


# --------------------------------------------------------------------------- #
# Net-+1 swap: remove 1, add 2.
# --------------------------------------------------------------------------- #

def swap_remove1_add2(
    seed: Iterable[int],
    N: int,
    *,
    time_limit_s: float = 60.0,
) -> list[int] | None:
    """Try to drop one element from seed and add two new elements in [1, N],
    yielding a B_2 Sidon set of size |seed| + 1.

    Iterates over seed elements (in order) and runs extend_sidon_by_k(2)
    on (seed - {r}) with the full original seed as `exclude` (so r doesn't
    come back). Returns the first successful swap, or None.

    Note: the per-r SAT search shares the time_limit_s budget proportionally;
    early r's that succeed return immediately.
    """
    seed_list = sorted(set(int(s) for s in seed))
    if not seed_list:
        return None
    if N > 2000:
        raise RuntimeError(
            f"swap_remove1_add2(N={N}) encoding too large for the "
            f"underlying extend_sidon_by_k(2)"
        )
    deadline = time.time() + time_limit_s
    excl = set(seed_list)
    for r in seed_list:
        remaining_s = deadline - time.time()
        if remaining_s <= 0.5:
            return None
        smaller = [x for x in seed_list if x != r]
        result = extend_sidon_by_k(
            smaller, N, 2,
            exclude=excl,
            time_limit_s=remaining_s,
        )
        if result is not None:
            return result
    return None
