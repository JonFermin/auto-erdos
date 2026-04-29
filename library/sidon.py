"""Sidon (B_2) constructions: literature lower-bound-attaining sets.

Public:
  singer(q)             — q+1-element Sidon set in [0, q^2+q] (q prime).
  erdos_turan(p)        — p-element Sidon set in [0, 2p^2-p] (p prime).
  singer_for_n(N, base) — best-fitting Singer set in [base, base+N-1].

All sets are returned as sorted ``list[int]``.

Verifier expects values in [1, N], so use ``base=1`` (default) and filter
to fit the active problem's N. ``singer_for_n`` does both for you.
"""
from __future__ import annotations
import math

from library._ff import (
    _mul_x_in_cubic,
    find_primitive_cubic,
    is_prime,
)


def singer(q: int) -> list[int]:
    """Singer Sidon set: q+1 elements forming a perfect difference set in
    Z/(q^2+q+1), embedded as integers in [0, q^2+q]. Requires q prime.

    Algorithm: pick primitive cubic g(x) over F_q, walk the orbit of 1
    under multiplication by x in F_q[x]/g(x), and record indices i where
    x^i lies in span_{F_q}(1, x) (i.e., the x^2-coefficient is 0).
    Exactly q+1 such indices appear in i in [0, q^2+q].

    A perfect difference set in Z/N is automatically Sidon (B_2) when
    lifted to [0, N-1], because pairwise differences avoid wraparound.
    """
    if not is_prime(q):
        raise ValueError(
            f"singer requires prime q (got q={q}); F_{{q}} prime-power not supported"
        )
    cubic = find_primitive_cubic(q)
    period = q * q + q + 1
    state = (1, 0, 0)
    out: list[int] = []
    for i in range(period):
        if state[2] == 0:
            out.append(i)
        state = _mul_x_in_cubic(state, cubic, q)
    return out


def erdos_turan(p: int) -> list[int]:
    """Erdős–Turán Sidon set: {2pa + (a^2 mod p) : 0 <= a < p} for prime p.
    Size p, lives in [0, 2p^2 - p]. Slightly weaker than Singer (size p
    rather than q+1 over a comparable range) but trivial to compute.
    """
    if not is_prime(p):
        raise ValueError(f"erdos_turan requires prime p (got p={p})")
    return sorted(2 * p * a + (a * a) % p for a in range(p))


def singer_for_n(N: int, base: int = 1) -> list[int]:
    """Largest Singer Sidon set fitting in [base, base + N - 1].

    Tries primes q with q^2 + q + 1 around N. For each q, computes the
    Singer perfect difference set in Z/(q^2+q+1), then sweeps all M=q^2+q+1
    cyclic translates and picks the one fitting the most elements inside
    [0, N-1]. Returns the best (translated, shifted by ``base``).

    Translates remain perfect difference sets — Sidon-ness is preserved —
    so the only thing to optimize over is the contiguous window placement.
    Returns [] if no prime q yields any element in range.
    """
    if N < 2:
        return []
    candidates: list[tuple[int, int, list[int]]] = []
    q_center = max(2, int(math.isqrt(N)))
    for q in range(max(2, q_center - 4), q_center + 7):
        if not is_prime(q):
            continue
        try:
            s = singer(q)
        except (ValueError, RuntimeError):
            continue
        M = q * q + q + 1
        best_size = 0
        best_set: list[int] = []
        for t in range(M):
            translated = sorted((x + t) % M for x in s)
            fit = [y for y in translated if y < N]
            if len(fit) > best_size:
                best_size = len(fit)
                best_set = fit
        if best_set:
            shifted = [y + base for y in best_set]
            candidates.append((len(shifted), q, shifted))
    if not candidates:
        return []
    candidates.sort(key=lambda t: (-t[0], t[1]))
    return candidates[0][2]
