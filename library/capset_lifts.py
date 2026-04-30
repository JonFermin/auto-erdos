"""Stronger cap-set seeds via product-lifts and the Edel 112-cap.

Public:
  cap_n6_size112()    — Edel's 112-cap in F_3^6 (literature LB), if cached.
  best_seed_v2(n)     — strongest available seed; uses cap_n6_size112 when present.
  best_decomposition_size(n) — size of the best product-lift the library can build.

The 112-cap is a one-time SAT computation (see scripts/find_cap_n6_size112.py).
If library/data/cap_n6_size112.json is present, this module loads it and
uses it as the dominant building block. If not, best_seed_v2 falls back to
the existing cap_n4_size20 / cap_n3_size9 primitives — a slightly stronger
optimization than library.capset.best_seed (e.g., n=10 picks 4+3+3=1620
over 4+4+2=1600).

Concrete sizes vs. literature LBs (with cap_n6_size112 cached):

  n=5:  40   / 45   (no improvement — same as best_seed)
  n=6:  112  / 112  (LB MATCHED)
  n=7:  224  / 236
  n=8:  448  / 496
  n=9:  1008 / 1082
  n=10: 2240 / 2474
  n=11: 4480 / —
  n=12: 12544 / —

Without cap_n6_size112 (fallback path):

  n=5:  40   (same as best_seed)
  n=6:  81   (+1 over best_seed's 80, via 3+3 decomposition)
  n=7:  180  (same)
  n=8:  400  (same)
  n=9:  800  (same)
  n=10: 1620 (+20 over best_seed's 1600, via 4+3+3 decomposition)
"""
from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

from library import capset

_DATA_DIR = Path(__file__).resolve().parent / "data"


# --------------------------------------------------------------------------- #
# cap_n6_size112 — disk-cached only. Build via scripts/find_cap_n6_size112.py.
# --------------------------------------------------------------------------- #

@lru_cache(maxsize=1)
def cap_n6_size112() -> list[tuple[int, int, int, int, int, int]] | None:
    """112-cap in F_3^6 (Edel 2004, the literature LB).

    Returns the cap if library/data/cap_n6_size112.json is present and
    verifies as cap-free. Returns None if the cache is missing — callers
    must fall through to product-lifts of smaller primitives.

    The cache is built by scripts/find_cap_n6_size112.py (one-time SAT
    search). DO NOT compute it lazily on import — F_3^6 SAT can take
    minutes-to-hours and that would silently block strategy.py runs.
    """
    path = _DATA_DIR / "cap_n6_size112.json"
    if not path.exists() or path.stat().st_size == 0:
        return None
    try:
        with open(path, encoding="utf-8") as f:
            data = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None
    if data.get("n") != 6 or data.get("size") != 112:
        return None
    raw = data.get("candidate")
    if not isinstance(raw, list) or len(raw) != 112:
        return None
    cap: list[tuple[int, int, int, int, int, int]] = []
    for p in raw:
        if not isinstance(p, list) or len(p) != 6:
            return None
        if any(c not in (0, 1, 2) for c in p):
            return None
        cap.append(tuple(int(c) for c in p))
    seen = set(cap)
    if len(seen) != 112:
        return None
    for i, a in enumerate(cap):
        for b in cap[i + 1:]:
            c = tuple((-(a[d] + b[d])) % 3 for d in range(6))
            if c != a and c != b and c in seen:
                return None
    return cap


# --------------------------------------------------------------------------- #
# Decomposition optimizer — pick the product-lift that maximizes |cap|.
# --------------------------------------------------------------------------- #

def _primitive_sizes() -> dict[int, int]:
    """{dim: size} of the best primitive cap available at each small dim.

    Includes cap_n6_size112 ONLY if its cache is present. Callers use this
    table to pick optimal decompositions of the target n.
    """
    table = {1: 2, 2: 4, 3: 9, 4: 20}
    if cap_n6_size112() is not None:
        table[6] = 112
    return table


def _best_decomposition(n: int) -> tuple[list[int], int]:
    """Find the partition of n into parts in _primitive_sizes() that
    maximizes the product of corresponding cap sizes.

    Returns (parts, product_size). For small n where every primitive
    exists, this is a tiny DP — brute force is fine.
    """
    sizes = _primitive_sizes()
    # DP: best[k] = (best_size, parts) for the integer k.
    best: dict[int, tuple[int, list[int]]] = {0: (1, [])}
    for k in range(1, n + 1):
        for part, part_size in sizes.items():
            if part > k:
                continue
            prev = best.get(k - part)
            if prev is None:
                continue
            cand_size = prev[0] * part_size
            if k not in best or cand_size > best[k][0]:
                best[k] = (cand_size, prev[1] + [part])
    if n not in best:
        return [], 0
    return best[n][1], best[n][0]


def best_decomposition_size(n: int) -> int:
    """Just the size — for use in tests / strategy decisions."""
    _, sz = _best_decomposition(n)
    return sz


# --------------------------------------------------------------------------- #
# best_seed_v2 — assemble the cap from the optimal decomposition.
# --------------------------------------------------------------------------- #

def _primitive_cap(dim: int) -> list[tuple[int, ...]]:
    if dim == 1:
        return capset.cap_n1()
    if dim == 2:
        return capset.cap_n2_size4()
    if dim == 3:
        return capset.cap_n3_size9()
    if dim == 4:
        return capset.cap_n4_size20()
    if dim == 6:
        cap = cap_n6_size112()
        if cap is None:
            raise RuntimeError(
                "cap_n6_size112 not cached — run scripts/find_cap_n6_size112.py first"
            )
        return cap
    raise ValueError(f"no primitive available at dim={dim}")


def best_seed_v2(n: int) -> list[tuple[int, ...]]:
    """Strongest available cap-set seed for F_3^n via product-lifts.

    For n in {1, 2, 3, 4}, returns the exact maximum cap (matches LB).
    For n >= 5, picks the optimal decomposition over available primitives
    and assembles via library.capset.product_lift.

    When cap_n6_size112 is cached, results jump significantly for n >= 6:
    e.g., n=10 returns a 2240-cap (vs 1600 from library.capset.best_seed).
    """
    if n < 0:
        raise ValueError(f"n must be non-negative (got {n})")
    if n == 0:
        return [()]
    parts, _ = _best_decomposition(n)
    if not parts:
        # Fallback — n=5 has no cap_n5 primitive; decompose recursively.
        return capset.best_seed(n)
    blocks = [(_primitive_cap(p), p) for p in parts]
    cur, cur_dim = blocks[0]
    for blk, blk_dim in blocks[1:]:
        cur = capset.product_lift(cur, cur_dim, blk, blk_dim)
        cur_dim += blk_dim
    return cur
