"""Capset constructions for F_3^n.

Public:
  random_greedy(n, seed=0)        — randomized greedy seed (current strategy.py default).
  cap_n1()                         — 2-cap in F_3^1 (the maximum).
  cap_n2_size4()                   — 4-cap in F_3^2 (the maximum).
  product_lift(A, n_a, B, n_b)     — direct sum: caps × caps -> cap in F_3^{n_a+n_b}.
  lift_to_dim(cap, src_n, tgt_n)   — zero-pad embedding into higher dim.
  recursive_product(n)             — cap of size 4^(n//2) * 2^(n % 2) in F_3^n.

Validity proof for product_lift (referenced by recursive_product):
  Let A subset F_3^a, B subset F_3^b be caps. Suppose three distinct points
  (a_i, b_i) in A x B sum to 0 in F_3^{a+b}. Then sum a_i = 0 in F_3^a and
  sum b_i = 0 in F_3^b. Case-split on equality:
    - a_1, a_2, a_3 distinct: A has a 3-AP — contradiction.
    - exactly two a_i equal (WLOG a_1 = a_2 != a_3): the three points are
      distinct, so b_1 != b_2; b_3 = -(b_1 + b_2) makes b_1, b_2, b_3 a
      3-AP in B (one shows they are distinct using a_1 = a_2 != a_3 and
      a_1 + a_2 + a_3 = 0 implies a_3 = a_1) — contradiction.
    - all three a_i equal: distinctness of points gives distinct b_i, and
      b_1 + b_2 + b_3 = 0 makes them a 3-AP in B — contradiction.
  Therefore A x B is a cap.
"""
from __future__ import annotations
import itertools
import random


def random_greedy(n: int, seed: int = 0) -> list[tuple[int, ...]]:
    """Randomized greedy cap-set construction in F_3^n.

    Shuffle all 3^n points with the given seed, walk in order, accept any
    point that doesn't complete a 3-AP with two already-chosen points.
    Same algorithm as the original ``_seed_capset`` in ``strategy.py``.
    """
    rng = random.Random(seed)
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


def cap_n1() -> list[tuple[int]]:
    """2-cap in F_3^1: the maximum (a_1(F_3) = 2). {(0,), (1,)}."""
    return [(0,), (1,)]


def cap_n2_size4() -> list[tuple[int, int]]:
    """4-cap in F_3^2: the maximum (a_2(F_3) = 4). {(0,0), (1,0), (0,1), (1,1)}.

    Verify: any 3 of the 4 must not sum to (0,0) mod 3.
      (0,0)+(1,0)+(0,1) = (1,1)
      (0,0)+(1,0)+(1,1) = (2,1)
      (0,0)+(0,1)+(1,1) = (1,2)
      (1,0)+(0,1)+(1,1) = (2,2)
    None are zero — valid cap.
    """
    return [(0, 0), (1, 0), (0, 1), (1, 1)]


def product_lift(
    A: list[tuple[int, ...]],
    n_a: int,
    B: list[tuple[int, ...]],
    n_b: int,
) -> list[tuple[int, ...]]:
    """A x B as a cap in F_3^{n_a + n_b}, size |A| * |B|.

    Validity preservation: A and B caps -> A x B cap (proof in module docstring).
    """
    for p in A:
        if len(p) != n_a:
            raise ValueError(f"A has tuple of length {len(p)} but n_a={n_a}")
    for p in B:
        if len(p) != n_b:
            raise ValueError(f"B has tuple of length {len(p)} but n_b={n_b}")
    return [tuple(a) + tuple(b) for a in A for b in B]


def lift_to_dim(
    cap: list[tuple[int, ...]],
    src_n: int,
    tgt_n: int,
) -> list[tuple[int, ...]]:
    """Embed cap from F_3^{src_n} into F_3^{tgt_n} (tgt_n >= src_n) by
    zero-padding. Trivially valid: any 3-AP in the lifted set, restricted
    to the first src_n coords, is a 3-AP in the original cap.
    """
    if tgt_n < src_n:
        raise ValueError(f"tgt_n={tgt_n} < src_n={src_n}")
    if tgt_n == src_n:
        return [tuple(p) for p in cap]
    pad = (0,) * (tgt_n - src_n)
    return [tuple(p) + pad for p in cap]


def recursive_product(n: int) -> list[tuple[int, ...]]:
    """Cap in F_3^n built by repeatedly applying ``product_lift`` to the
    canonical 1-cap and 2-cap. Size 4^(n//2) * 2^(n % 2):

      n=1 -> 2;  n=2 -> 4;  n=3 -> 8;  n=4 -> 16;  n=5 -> 32;
      n=6 -> 64; n=7 -> 128; n=8 -> 256; n=9 -> 512; n=10 -> 1024.

    All sizes are below the literature LB for n >= 4, so this is a
    starting point only — agents are expected to augment it.
    """
    if n < 0:
        raise ValueError(f"n must be non-negative (got {n})")
    if n == 0:
        return [()]
    if n == 1:
        return cap_n1()
    if n == 2:
        return cap_n2_size4()
    half = n // 2
    A = recursive_product(half)
    B = recursive_product(n - half)
    return product_lift(A, half, B, n - half)
