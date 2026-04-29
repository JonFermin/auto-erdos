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

from library import capset, sidon
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
    _check_capset(capset.recursive_product(3), 3, 8)
    _check_capset(capset.recursive_product(4), 4, 16)
    _check_capset(capset.recursive_product(6), 6, 64)
    _check_capset(capset.recursive_product(8), 8, 256)
    _check_capset(capset.random_greedy(4, seed=0), 4, 8)
    _check_capset(capset.random_greedy(6, seed=0), 6, 30)

    # lift_to_dim sanity
    lifted = capset.lift_to_dim(capset.cap_n2_size4(), 2, 5)
    _check_capset(lifted, 5, 4)

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

    print("\nAll passing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
