"""tests/test_capset_records.py — the shipped record caps are load-bearing.

If a data file were corrupted or mis-transcribed, capset seeds would either
start below the literature LB (silently wasting every trial's budget) or —
far worse — feed an invalid "cap" into warm-starts. This performs the full
O(k²) cap-freeness verification that record_cap() deliberately skips at
load time, and pins the sizes best_seed_v2 must reach.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import pytest

from library import capset_lifts, capset_records

EXPECTED = {7: 236, 8: 512, 9: 1082, 10: 2432}


def test_record_sizes_match_expected():
    sizes = capset_records.record_sizes()
    for n, size in EXPECTED.items():
        assert sizes.get(n) == size, f"n={n}: expected {size}, got {sizes.get(n)}"


@pytest.mark.parametrize("n", sorted(EXPECTED))
def test_record_cap_is_cap_free(n):
    cap = capset_records.record_cap(n)
    assert cap is not None
    assert len(cap) == EXPECTED[n]
    assert all(len(p) == n and all(c in (0, 1, 2) for c in p) for p in cap)
    seen = set(cap)
    assert len(seen) == len(cap)
    for i, a in enumerate(cap):
        for b in cap[i + 1:]:
            c = tuple((-(a[d] + b[d])) % 3 for d in range(n))
            assert c == a or c == b or c not in seen, f"AP triple at n={n}: {a},{b},{c}"


def test_best_seed_v2_reaches_literature_lb():
    for n, size in EXPECTED.items():
        seed = capset_lifts.best_seed_v2(n)
        assert len(seed) == size, f"best_seed_v2({n}) = {len(seed)}, want {size}"


def test_best_seed_v2_composes_records_above_n10():
    # 10+1 product: 2432 * 2 = 4864
    assert capset_lifts.best_decomposition_size(11) == 4864


def test_baselines_match_shipped_records():
    """The problem specs' baselines must equal what the library seed delivers —
    the 'library reproduces the LB' invariant from README."""
    import json

    for n, size in EXPECTED.items():
        spec = json.loads((REPO_ROOT / "problems" / f"capset_n{n}.json").read_text())
        assert float(spec["baseline"]) == size, f"capset_n{n} baseline {spec['baseline']} != shipped {size}"
