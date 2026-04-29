"""Sanity tests for the constructions library.

Run with::

    uv run python -m library._selftest

Each construction is fed through the prepare verifier and asserted to be
valid + at the expected size. Not part of any agent loop — purely for the
human maintainer to confirm the library hasn't bit-rotted.
"""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from library import capset, sat_extensions, sidon
from prepare import _verify_capset, _verify_sidon


def _check_capset(cap: list, n: int, expect_at_least: int) -> int:
    spec = {"family": "capset", "n": n}
    result = _verify_capset(cap, spec)
    if not result.is_valid:
        raise AssertionError(f"capset(n={n}) INVALID: {result.reason}")
    score = int(result.score)
    if score < expect_at_least:
        raise AssertionError(
            f"capset(n={n}) score {score} < expected {expect_at_least}"
        )
    print(f"  capset(n={n}): size {score} (>= {expect_at_least}) OK")
    return score


def _check_sidon(s: list, N: int, expect_at_least: int) -> int:
    spec = {"family": "sidon", "N": N}
    result = _verify_sidon(s, spec)
    if not result.is_valid:
        raise AssertionError(f"sidon(N={N}) INVALID: {result.reason}")
    score = int(result.score)
    if score < expect_at_least:
        raise AssertionError(
            f"sidon(N={N}) score {score} < expected {expect_at_least}"
        )
    print(f"  sidon(N={N}): size {score} (>= {expect_at_least}) OK")
    return score


def main() -> int:
    print("library/_selftest")
    print("=" * 50)

    print("\ncapset:")
    _check_capset(capset.cap_n1(), 1, 2)
    _check_capset(capset.cap_n2_size4(), 2, 4)
    _check_capset(capset.cap_n3_size9(), 3, 9)
    _check_capset(capset.cap_n4_size20(), 4, 20)
    _check_capset(capset.recursive_product(3), 3, 8)
    _check_capset(capset.recursive_product(4), 4, 16)
    _check_capset(capset.recursive_product(6), 6, 64)
    _check_capset(capset.recursive_product(8), 8, 256)
    _check_capset(capset.random_greedy(4, seed=0), 4, 8)
    _check_capset(capset.random_greedy(6, seed=0), 6, 30)

    # lift_to_dim sanity
    lifted = capset.lift_to_dim(capset.cap_n2_size4(), 2, 5)
    _check_capset(lifted, 5, 4)

    # best_seed: strongest shipped per n. Sizes match the n=4 building block
    # composed with smaller exact caps via product_lift.
    print("\ncapset.best_seed:")
    for n, expected in [
        (1, 2), (2, 4), (3, 9), (4, 20),
        (5, 40), (6, 80), (7, 180), (8, 400),
        (9, 800), (10, 1600),
    ]:
        _check_capset(capset.best_seed(n), n, expected)

    print("\nsidon:")
    # Singer sets — direct (in [0, q^2+q]).
    s23 = sidon.singer(23)
    assert len(s23) == 24, f"singer(23) size {len(s23)} != 24"
    # Lift to [1, q^2+q+1] for verifier.
    s23_lifted = [x + 1 for x in s23]
    _check_sidon(s23_lifted, max(s23_lifted), 24)

    s31 = sidon.singer(31)
    assert len(s31) == 32, f"singer(31) size {len(s31)} != 32"
    s31_lifted = [x + 1 for x in s31]
    _check_sidon(s31_lifted, max(s31_lifted), 32)

    s53 = sidon.singer(53)
    assert len(s53) == 54, f"singer(53) size {len(s53)} != 54"
    s53_lifted = [x + 1 for x in s53]
    _check_sidon(s53_lifted, max(s53_lifted), 54)

    # Erdős–Turán
    et31 = sidon.erdos_turan(31)
    assert len(et31) == 31, f"erdos_turan(31) size {len(et31)} != 31"
    et31_lifted = [x + 1 for x in et31]
    _check_sidon(et31_lifted, max(et31_lifted), 31)

    # singer_for_n: best-fit at each problem N.
    s_500 = sidon.singer_for_n(500)
    _check_sidon(s_500, 500, 22)  # apr28 note: usually 22 or 23
    s_1000 = sidon.singer_for_n(1000)
    _check_sidon(s_1000, 1000, 32)
    s_3000 = sidon.singer_for_n(3000)
    _check_sidon(s_3000, 3000, 53)

    print("\nsat_extensions:")
    # Tiny-seed +1 extension.
    tiny = [1, 2, 5]
    ext1 = sat_extensions.extend_sidon_by_one(tiny, 30)
    assert ext1 is not None and len(ext1) == 4, f"extend_sidon_by_one tiny failed: {ext1}"
    _check_sidon(ext1, 30, 4)

    # +2 extension (SAT path).
    ext2 = sat_extensions.extend_sidon_by_k(tiny, 30, 2)
    assert ext2 is not None and len(ext2) == 5, f"extend_sidon_by_k(2) tiny failed: {ext2}"
    _check_sidon(ext2, 30, 5)

    # Try +1 extension on Singer(31)-derived 32-element seed in [1, 1000].
    # Either we find a 33rd point (research result) or returns None
    # (locally maximal). Both outcomes are acceptable here — the assertion
    # is just "function runs, output is correct shape".
    seed_1000 = sidon.singer_for_n(1000)
    ext_singer = sat_extensions.extend_sidon_by_one(seed_1000, 1000)
    if ext_singer is not None:
        _check_sidon(ext_singer, 1000, len(seed_1000) + 1)
        print(f"  extend_sidon_by_one(singer_for_n(1000), 1000): +1 to size {len(ext_singer)} OK")
    else:
        print(f"  extend_sidon_by_one(singer_for_n(1000), 1000): None (locally maximal at {len(seed_1000)}) OK")

    # swap_remove1_add2 smoke on a small valid seed.
    seed5 = [1, 2, 5, 11, 22]  # 5-element B_2 set
    swp = sat_extensions.swap_remove1_add2(seed5, 50)
    if swp is not None:
        _check_sidon(swp, 50, 6)
        print(f"  swap_remove1_add2(size-5, N=50): +1 to size {len(swp)} OK")
    else:
        print("  swap_remove1_add2(size-5, N=50): None (no swap fits) OK")

    print("\nhypothesis_log roundtrip:")
    from prepare import append_hypothesis_log, load_hypothesis_log
    # Use a unique tag to avoid colliding with real cache files.
    test_tag = "_selftest_hypothesis_log_smoke"
    append_hypothesis_log(
        "selftest", "deadbee", 42.0, 1, "discard",
        "thesis: selftest smoke row", tag=test_tag,
    )
    rows = load_hypothesis_log(tag=test_tag)
    assert len(rows) >= 1, "hypothesis_log roundtrip failed"
    last = rows[-1]
    assert last["thesis"] == "thesis: selftest smoke row"
    assert last["status"] == "discard"
    print(f"  append + load ({len(rows)} row{'s' if len(rows) != 1 else ''}): OK")
    # Cleanup test cache files.
    from pathlib import Path
    cache_dir = Path.home() / ".cache" / "auto-erdos"
    for suffix in (".tsv", ".tsv.lock"):
        p = cache_dir / f"hypothesis_log_{test_tag}{suffix}"
        if p.exists():
            p.unlink()

    print("\nAll passing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
