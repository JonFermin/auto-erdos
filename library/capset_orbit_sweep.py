"""GL(n, 3) orbit + affine translate sweeps for cap-sets in F_3^n.

The Sidon harness's `_singer37_multiplier_window` finds bigger windows by
sweeping every multiplier coset of a Singer perfect difference set. The
direct cap-set analog: sweep GL(n, 3) orbits and affine translates of a
seed cap. Different orbit reps give caps that are *isomorphic* but laid
out differently in F_3^n, which matters for any downstream routine that
treats some points as preferred (e.g., greedy extensions starting from a
fixed lex-first seed, or SAT encodings that benefit from low Hamming
distance to the all-zero point).

Public:
  random_invertible(n, rng) -> tuple[tuple[int,...], ...]
      Sample a uniformly-random invertible n×n matrix over F_3.

  apply_linear(A, cap)
      Apply A (n×n F_3 matrix) to every point of cap.

  apply_translate(t, cap)
      Add t to every point of cap (mod 3).

  iter_orbit_samples(seed, n, rng, max_samples)
      Yield up to max_samples (random A, A·seed) pairs. Caps are returned
      sorted. Useful for "try N random orbit reps, keep the best by some
      criterion" loops in strategy.py.

  best_orbit_extension(seed, n, *, max_samples, rng, extender, tb)
      For each random orbit rep + every affine translate, call extender
      on the transformed cap and track the largest valid result.
      `extender` is a callable (transformed_cap, n) -> list | None — pass
      capset_sat.extend_capset_by_one or a custom +1 routine.

All operations preserve cap-freeness. A: cap -> A·cap is a bijection of
F_3^n that preserves 3-APs (since linear maps commute with the AP
relation a+b+c=0). Affine translates trivially preserve cap-freeness.
"""
from __future__ import annotations

import itertools
import random
from typing import Callable, Iterator


def random_invertible(n: int, rng: random.Random) -> tuple[tuple[int, ...], ...]:
    """Sample a uniformly-random invertible n×n matrix over F_3.

    Algorithm: rejection sampling on uniform F_3-matrices, checking
    invertibility via Gaussian elimination. F_3 invertibility density is
    high (~|GL(n,3)| / 3^{n^2} ≈ 0.56 for small n), so 1-2 attempts
    typically suffice.
    """
    while True:
        rows = tuple(
            tuple(rng.randint(0, 2) for _ in range(n))
            for _ in range(n)
        )
        if _is_invertible_f3(rows, n):
            return rows


def _is_invertible_f3(rows: tuple[tuple[int, ...], ...], n: int) -> bool:
    """Gaussian elimination over F_3. Returns True iff full rank."""
    M = [list(r) for r in rows]
    for col in range(n):
        pivot = None
        for r in range(col, n):
            if M[r][col] != 0:
                pivot = r
                break
        if pivot is None:
            return False
        if pivot != col:
            M[col], M[pivot] = M[pivot], M[col]
        # Normalize pivot row to 1 (multiply by inverse of M[col][col]).
        inv = _f3_inv(M[col][col])
        M[col] = [(x * inv) % 3 for x in M[col]]
        # Eliminate column col in all other rows.
        for r in range(n):
            if r == col or M[r][col] == 0:
                continue
            factor = M[r][col]
            M[r] = [(M[r][j] - factor * M[col][j]) % 3 for j in range(n)]
    return True


def _f3_inv(x: int) -> int:
    """Multiplicative inverse in F_3. 1 -> 1, 2 -> 2 (since 2*2=4=1 mod 3)."""
    if x == 1:
        return 1
    if x == 2:
        return 2
    raise ZeroDivisionError("0 has no inverse in F_3")


def apply_linear(
    A: tuple[tuple[int, ...], ...],
    cap: list[tuple[int, ...]],
) -> list[tuple[int, ...]]:
    """Apply A to every point of cap. A is n×n; each point is length-n."""
    n = len(A)
    out: list[tuple[int, ...]] = []
    for p in cap:
        new = tuple(
            sum(A[i][j] * p[j] for j in range(n)) % 3
            for i in range(n)
        )
        out.append(new)
    return sorted(out)


def apply_translate(
    t: tuple[int, ...],
    cap: list[tuple[int, ...]],
) -> list[tuple[int, ...]]:
    """Translate every point of cap by t (componentwise mod 3)."""
    n = len(t)
    return sorted(
        tuple((p[d] + t[d]) % 3 for d in range(n))
        for p in cap
    )


def iter_orbit_samples(
    seed: list[tuple[int, ...]],
    n: int,
    rng: random.Random,
    max_samples: int,
) -> Iterator[tuple[tuple[tuple[int, ...], ...], list[tuple[int, ...]]]]:
    """Yield (A, A·seed) for max_samples random invertible A in GL(n, 3).

    The transformed cap remains cap-free (linear maps preserve 3-APs in
    F_3^n). Useful for strategies that want to try many "rotations" of
    the same underlying cap before running a positional algorithm.
    """
    for _ in range(max_samples):
        A = random_invertible(n, rng)
        yield A, apply_linear(A, seed)


def best_orbit_extension(
    seed: list[tuple[int, ...]],
    n: int,
    extender: Callable[[list[tuple[int, ...]], int], list[tuple[int, ...]] | None],
    *,
    max_orbit_samples: int = 50,
    sweep_translates: bool = True,
    rng: random.Random | None = None,
    tb=None,
) -> list[tuple[int, ...]]:
    """Best cap found over (random orbit reps × affine translates), each
    extended by `extender`.

    For each of `max_orbit_samples` random A in GL(n, 3):
      transformed = A · seed
      if sweep_translates:
        for every t in F_3^n: try extender(transformed + t)
      else:
        try extender(transformed)
    Track the largest result. tb.expired aborts the loop.

    `extender` defaults can be capset_sat.extend_capset_by_one for fast
    +1 attempts, or a longer SAT routine for a deeper search.

    Returns the best cap seen, or `seed` itself if no orbit yields an
    improvement (so the result is never worse than the input).
    """
    if rng is None:
        rng = random.Random(0)

    best: list[tuple[int, ...]] = sorted(tuple(int(c) for c in p) for p in seed)

    samples_done = 0
    for A in (random_invertible(n, rng) for _ in range(max_orbit_samples)):
        if tb is not None and tb.expired:
            break
        transformed = apply_linear(A, best)
        if not sweep_translates:
            result = extender(transformed, n)
            if result is not None and len(result) > len(best):
                best = result
        else:
            for t in itertools.product((0, 1, 2), repeat=n):
                if tb is not None and tb.expired:
                    return best
                shifted = apply_translate(t, transformed)
                result = extender(shifted, n)
                if result is not None and len(result) > len(best):
                    best = result
        samples_done += 1
    return best
