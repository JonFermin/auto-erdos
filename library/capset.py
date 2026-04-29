"""Capset constructions for F_3^n.

Public:
  random_greedy(n, seed=0)        — randomized greedy seed (current strategy.py default).
  cap_n1()                         — 2-cap in F_3^1 (the maximum).
  cap_n2_size4()                   — 4-cap in F_3^2 (the maximum).
  cap_n3_size9()                   — 9-cap in F_3^3 (the maximum, exact DFS).
  cap_n4_size20()                  — 20-cap in F_3^4 (the maximum, exact DFS, disk-cached).
  product_lift(A, n_a, B, n_b)     — direct sum: caps × caps -> cap in F_3^{n_a+n_b}.
  lift_to_dim(cap, src_n, tgt_n)   — zero-pad embedding into higher dim.
  recursive_product(n)             — cap of size 4^(n//2) * 2^(n % 2) in F_3^n.
  best_seed(n)                     — strongest shipped cap for F_3^n via 20-cap × ...

Use ``best_seed(n)`` in strategy.py — it picks the largest combination of shipped
exact caps via product-lift. For n >= 5 it dominates ``recursive_product(n)`` by
factors of 1.25× (n=5: 40 vs 32) up to 1.56× (n=10: 1600 vs 1024).

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
import json
import os
import random
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent / "data"


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


def cap_n3_size9() -> list[tuple[int, int, int]]:
    """9-cap in F_3^3: matches the maximum a_3(F_3) = 9.

    Computed via exact branch-and-bound DFS on 27 points (sub-second).
    """
    return _exact_max_cap(n=3, target=9, lb=8)


def cap_n4_size20() -> list[tuple[int, int, int, int]]:
    """20-cap in F_3^4: matches the maximum a_4(F_3) = 20.

    Computed via exact branch-and-bound DFS on 81 points. The result is
    cached on disk at ``library/data/cap_n4_size20.json`` after the first
    run; subsequent imports are instant. On every load the cached set is
    re-verified for cap-freeness so corrupted caches are detected.
    """
    cached = _load_cached_cap("cap_n4_size20.json", expected_n=4, expected_size=20)
    if cached is not None:
        return cached
    cap = _exact_max_cap(n=4, target=20, lb=16)
    if len(cap) != 20:
        raise RuntimeError(
            f"cap_n4_size20 DFS returned size {len(cap)} != 20 — search bug"
        )
    _save_cached_cap(cap, "cap_n4_size20.json", n=4, size=20)
    return cap


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

    All sizes are below the literature LB for n >= 4. For a strictly
    stronger seed using exact 9-cap and 20-cap building blocks, see
    ``best_seed(n)``.
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


def best_seed(n: int) -> list[tuple[int, ...]]:
    """Strongest shipped cap-set seed for F_3^n.

    Uses ``cap_n4_size20`` as the dominant building block via product-lift,
    matched with smaller exact caps for the remainder dim. Concrete sizes
    vs. literature lower bounds:

      n=0: 1               n=1: 2 / 2     (LB)
      n=2: 4 / 4 (LB)      n=3: 9 / 9 (LB)
      n=4: 20 / 20 (LB)    n=5: 40 / 45
      n=6: 80 / 112        n=7: 180 / 236
      n=8: 400 / 496       n=9: 800 / 1082
      n=10: 1600 / 2474

    Hits the literature LB exactly for n in {1, 2, 3, 4}; for n >= 5 it
    dominates ``recursive_product(n)`` substantially but is still below
    the literature LB (Edel-class constructions are not yet shipped).
    """
    if n < 0:
        raise ValueError(f"n must be non-negative (got {n})")
    if n == 0:
        return [()]
    if n == 1:
        return cap_n1()
    if n == 2:
        return cap_n2_size4()
    if n == 3:
        return cap_n3_size9()
    if n == 4:
        return cap_n4_size20()
    # Decompose n = 4*k + r (k >= 1, 0 <= r < 4). Build with k copies of
    # cap_n4_size20 and one small cap for r.
    k = n // 4
    r = n % 4
    blocks: list[tuple[list[tuple[int, ...]], int]] = []
    for _ in range(k):
        blocks.append((cap_n4_size20(), 4))
    if r > 0:
        blocks.append((best_seed(r), r))
    cur, cur_dim = blocks[0]
    for blk, blk_dim in blocks[1:]:
        cur = product_lift(cur, cur_dim, blk, blk_dim)
        cur_dim += blk_dim
    return cur


# --------------------------------------------------------------------------- #
# Exact DFS for small-n caps — used by cap_n3_size9 and cap_n4_size20.
# --------------------------------------------------------------------------- #

def _exact_max_cap(n: int, target: int, lb: int) -> list[tuple[int, ...]]:
    """Exact branch-and-bound DFS for the largest cap in F_3^n.

    Stops as soon as a cap of size ``target`` is found (since target is
    the proven maximum for the n it's called with). Initialized with a
    lower bound ``lb`` from random_greedy so pruning kicks in immediately.

    Time: sub-second for n=3, a few seconds for n=4. Don't call with n >= 5.
    """
    points = list(itertools.product((0, 1, 2), repeat=n))
    # Warm-start: random_greedy gives a non-trivial LB.
    best: list[tuple[int, ...]] = []
    for seed in range(8):
        candidate = random_greedy(n, seed=seed)
        if len(candidate) > len(best):
            best = candidate
        if len(best) >= lb:
            break

    state = {"best": list(best), "found_target": False}

    def dfs(idx: int, chosen: list, forbidden: set) -> None:
        if state["found_target"]:
            return
        # Bound: if even taking every remaining point can't beat best, prune.
        if len(chosen) + (len(points) - idx) <= len(state["best"]):
            return
        if idx == len(points):
            if len(chosen) > len(state["best"]):
                state["best"] = list(chosen)
                if len(chosen) >= target:
                    state["found_target"] = True
            return
        p = points[idx]

        # Branch 1: include p (only if not forbidden by existing chosen pairs).
        if p not in forbidden:
            new_forbidden = set(forbidden)
            for c in chosen:
                r = tuple((-(c[d] + p[d])) % 3 for d in range(n))
                if r != c and r != p:
                    new_forbidden.add(r)
            chosen.append(p)
            dfs(idx + 1, chosen, new_forbidden)
            chosen.pop()
            if state["found_target"]:
                return

        # Branch 2: exclude p.
        dfs(idx + 1, chosen, forbidden)

    dfs(0, [], set())
    return state["best"]


# --------------------------------------------------------------------------- #
# Disk cache for exact caps (only cap_n4 is cached; cap_n3 is fast enough).
# --------------------------------------------------------------------------- #

def _load_cached_cap(
    filename: str, expected_n: int, expected_size: int
) -> list[tuple[int, ...]] | None:
    path = _DATA_DIR / filename
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None
    if data.get("n") != expected_n or data.get("size") != expected_size:
        return None
    raw = data.get("candidate")
    if not isinstance(raw, list) or len(raw) != expected_size:
        return None
    cap: list[tuple[int, ...]] = []
    for p in raw:
        if not isinstance(p, list) or len(p) != expected_n:
            return None
        if any(c not in (0, 1, 2) for c in p):
            return None
        cap.append(tuple(int(c) for c in p))
    # Re-verify cap-freeness on load — corruption insurance.
    seen = set(cap)
    if len(seen) != expected_size:
        return None
    for i, a in enumerate(cap):
        for b in cap[i + 1:]:
            c = tuple((-(a[d] + b[d])) % 3 for d in range(expected_n))
            if c != a and c != b and c in seen:
                return None
    return cap


def _save_cached_cap(
    cap: list[tuple[int, ...]], filename: str, n: int, size: int
) -> None:
    _DATA_DIR.mkdir(parents=True, exist_ok=True)
    path = _DATA_DIR / filename
    payload = {
        "n": n,
        "size": size,
        "candidate": [list(p) for p in cap],
    }
    tmp_path = path.with_suffix(".json.tmp")
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(payload, f, separators=(",", ":"))
    os.replace(tmp_path, path)
