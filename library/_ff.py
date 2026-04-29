"""Tiny finite-field helpers for the constructions library.

Internal module — public API is in ``library.sidon`` / ``library.capset``.

Currently supports:
  - F_p for p prime (Z/p arithmetic).
  - Cubic extensions F_p[x] / g(x) used by the Singer construction.

Prime-power F_{p^k} (k > 1) is NOT implemented; Singer/Bose-Chowla here
require q prime.
"""
from __future__ import annotations
import math


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    for d in range(3, math.isqrt(n) + 1, 2):
        if n % d == 0:
            return False
    return True


def factor(n: int) -> list[int]:
    """Distinct prime factors of n. n >= 2."""
    if n < 2:
        raise ValueError(f"cannot factor {n}")
    out: list[int] = []
    m = n
    if m % 2 == 0:
        out.append(2)
        while m % 2 == 0:
            m //= 2
    d = 3
    while d * d <= m:
        if m % d == 0:
            out.append(d)
            while m % d == 0:
                m //= d
        d += 2
    if m > 1:
        out.append(m)
    return out


def _has_root_mod(cubic: tuple[int, int, int], q: int) -> bool:
    """True iff x^3 + c2 x^2 + c1 x + c0 has a root in F_q."""
    c2, c1, c0 = cubic
    for r in range(q):
        if (r * r * r + c2 * r * r + c1 * r + c0) % q == 0:
            return True
    return False


def _mul_x_in_cubic(state: tuple[int, int, int], cubic: tuple[int, int, int], q: int) -> tuple[int, int, int]:
    """Multiply (e0, e1, e2) by x in F_q[x] / (x^3 + c2 x^2 + c1 x + c0).

    x * (e0 + e1 x + e2 x^2) = e0 x + e1 x^2 + e2 x^3
                              = -e2 c0 + (e0 - e2 c1) x + (e1 - e2 c2) x^2.
    """
    e0, e1, e2 = state
    c2, c1, c0 = cubic
    return (
        (-e2 * c0) % q,
        (e0 - e2 * c1) % q,
        (e1 - e2 * c2) % q,
    )


def _mul_in_cubic(a: tuple[int, int, int], b: tuple[int, int, int], cubic: tuple[int, int, int], q: int) -> tuple[int, int, int]:
    """Multiply two F_q[x] / cubic elements."""
    a0, a1, a2 = a
    b0, b1, b2 = b
    c2, c1, c0 = cubic

    # Polynomial product (degree up to 4).
    p0 = a0 * b0
    p1 = a0 * b1 + a1 * b0
    p2 = a0 * b2 + a1 * b1 + a2 * b0
    p3 = a1 * b2 + a2 * b1
    p4 = a2 * b2

    # Reduction:
    #   x^3 = -c2 x^2 - c1 x - c0
    #   x^4 = (c2^2 - c1) x^2 + (c2 c1 - c0) x + c2 c0
    r0 = p0 - p3 * c0 + p4 * (c2 * c0)
    r1 = p1 - p3 * c1 + p4 * (c2 * c1 - c0)
    r2 = p2 - p3 * c2 + p4 * (c2 * c2 - c1)

    return (r0 % q, r1 % q, r2 % q)


def _pow_x_fast(cubic: tuple[int, int, int], q: int, k: int) -> tuple[int, int, int]:
    """x^k via square-and-multiply in F_q[x] / cubic."""
    if k == 0:
        return (1, 0, 0)
    base = (0, 1, 0)  # x
    result = (1, 0, 0)
    while k > 0:
        if k & 1:
            result = _mul_in_cubic(result, base, cubic, q)
        base = _mul_in_cubic(base, base, cubic, q)
        k >>= 1
    return result


def find_primitive_cubic(q: int) -> tuple[int, int, int]:
    """(c2, c1, c0) such that g(x) = x^3 + c2 x^2 + c1 x + c0 is irreducible
    over F_q AND x is primitive in F_{q^3}*.

    Iterates (c0, c1, c2) in lex order with c0 in F_q*. The first or second
    irreducible cubic is usually primitive.
    """
    if not is_prime(q):
        raise ValueError(f"prime q required for cubic search (got q={q})")
    n = q * q * q - 1
    facs = factor(n)
    for c0 in range(1, q):
        for c1 in range(q):
            for c2 in range(q):
                cubic = (c2, c1, c0)
                if _has_root_mod(cubic, q):
                    continue
                if all(_pow_x_fast(cubic, q, n // p) != (1, 0, 0) for p in facs):
                    return cubic
    raise RuntimeError(f"no primitive cubic over F_{q} found (unexpected)")
