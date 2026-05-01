"""tests/test_witness_rigor.py — load-bearing rigor tests for primitive_set_witness.

The witness verifier is the *only* path to the ``counterexample_proven``
verdict in Track 2. A bug here would let the loop claim a disproof of an
open problem. These tests pin its behavior on hand-computed cases.
"""
from __future__ import annotations

import json
import math
import sys
from decimal import Decimal
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import pytest

from library.primitive_set_witness import (
    _LOG_ULP_SLACK,
    _check_pairwise_non_divisible,
    _log_strict_upper_bound,
    _rigorous_sum_lower_bound,
    verify_witness,
)


def _spec(threshold: float = 1.0) -> dict:
    return {"witness_threshold": threshold}


# --------------------------------------------------------------------------- #
# log_strict_upper_bound: must dominate the true log
# --------------------------------------------------------------------------- #

def test_log_upper_strictly_above_true_log():
    """For every probe a, the bumped value strictly exceeds the unbumped
    math.log(a). 4 ULPs of nextafter is non-zero on every IEEE-754 platform."""
    for a in [2, 3, 5, 7, 100, 1_000, 1_000_003]:
        ub = _log_strict_upper_bound(a)
        true = Decimal(repr(math.log(a)))
        assert ub > true, f"upper bound {ub} did not exceed math.log({a}) = {true}"


def test_log_upper_rejects_a_below_two():
    for bad in (-1, 0, 1):
        with pytest.raises(ValueError):
            _log_strict_upper_bound(bad)


def test_log_upper_rejects_non_int():
    with pytest.raises(TypeError):
        _log_strict_upper_bound(2.5)  # type: ignore[arg-type]


def test_log_upper_bump_is_at_least_four_ulps():
    """Pin the slack at 4. Regression guard: if someone changes the constant
    silently, this test fails loudly."""
    assert _LOG_ULP_SLACK == 4
    for a in (10, 1000, 1_000_000):
        plain = math.log(a)
        bumped = float(_log_strict_upper_bound(a))
        # bumped must be exactly _LOG_ULP_SLACK ULPs above plain.
        cursor = plain
        for _ in range(_LOG_ULP_SLACK):
            cursor = math.nextafter(cursor, math.inf)
        assert bumped == cursor, f"a={a}: bumped {bumped!r} != cursor {cursor!r}"


# --------------------------------------------------------------------------- #
# Pairwise non-divisibility check
# --------------------------------------------------------------------------- #

def test_primitive_check_passes_on_primes():
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    ok, reason = _check_pairwise_non_divisible(primes)
    assert ok, reason


def test_primitive_check_passes_on_omega_two():
    """{4, 6, 9, 10, 14, 15, 21, 22, 25, ...} — Omega(n)=2 set is primitive."""
    omega2 = [4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46]
    ok, reason = _check_pairwise_non_divisible(omega2)
    assert ok, reason


def test_primitive_check_rejects_divides():
    ok, reason = _check_pairwise_non_divisible([3, 5, 15])
    assert not ok
    assert "divides" in reason.lower()


def test_primitive_check_rejects_duplicate():
    ok, reason = _check_pairwise_non_divisible([3, 5, 5])
    assert not ok
    assert "duplicate" in reason.lower()


def test_primitive_check_empty_is_trivial():
    ok, reason = _check_pairwise_non_divisible([])
    assert ok


# --------------------------------------------------------------------------- #
# Rigorous sum lower bound
# --------------------------------------------------------------------------- #

def test_rigorous_sum_strictly_below_naive_sum():
    """For any non-empty set, the rigorous lower bound is strictly below the
    naive float sum (which uses log without bumping). This is the structural
    invariant: bumping log up shrinks every term, so the sum is a strict
    under-estimate of the true sum."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    rigor = _rigorous_sum_lower_bound(primes)
    naive = sum(1.0 / (a * math.log(a)) for a in primes)
    assert float(rigor) < naive
    # But the gap should be tiny — at most a few ULPs per term times k terms.
    relative_gap = (Decimal(repr(naive)) - rigor) / Decimal(repr(naive))
    assert relative_gap < Decimal("1e-10"), f"rigor gap too large: {relative_gap}"


def test_rigorous_sum_known_omega_two_set_below_one():
    """Omega(n)=2 is the canonical near-extremal primitive set; F3 says the
    sum is below 1 for every k. Pin the rigor: a hand-picked finite slice
    must give a rigorous lower bound well below 1."""
    # First 50 elements of Omega(n)=2: products of two primes (with repetition).
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    omega2 = sorted({p * q for p in primes for q in primes if p <= q})[:50]
    lb = _rigorous_sum_lower_bound(omega2)
    assert lb < Decimal("1"), f"finite Omega(n)=2 slice rigor bound {lb} should be < 1"
    # Sanity: it should be a meaningful contribution, not near zero.
    assert lb > Decimal("0.05"), f"50-element Omega(n)=2 slice should sum more than 0.05, got {lb}"


def test_rigorous_sum_rejects_a_below_two():
    with pytest.raises(ValueError):
        _rigorous_sum_lower_bound([1, 2, 3])


# --------------------------------------------------------------------------- #
# verify_witness end-to-end
# --------------------------------------------------------------------------- #

def test_verify_witness_rejects_below_threshold():
    """An Omega(n)=2 slice has sum < 1 (F3); verifier must reject threshold=1.

    Note: starting at x_floor=2 with primes the sum approaches ~1.64 by F2/F3
    and so a few primes alone exceed 1. Using Omega(n)=2 elements (a primitive
    set whose sum is provably < 1 in the limit) is the right negative case."""
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
    omega2 = sorted({p * q for p in primes for q in primes if p <= q})[:30]
    payload = {"x_floor": min(omega2), "elements": omega2}
    result = verify_witness(payload, _spec(1.0))
    assert result.is_valid is False, (
        f"30-element Omega(n)=2 slice should sum < 1; got score={result.score}, reason={result.reason}"
    )
    assert "does NOT exceed" in result.reason or "<=" in result.reason


def test_verify_witness_accepts_synthetic_above_threshold():
    """Synthetic test of the ABOVE-threshold path — we don't actually have a
    counterexample to Erdős, so we use an artificially low threshold to
    exercise the success branch. This is the hot codepath: getting it right
    matters far more than getting it triggered by real math."""
    # The set {2, 3, 5, 7} has sum 1/(2 ln 2) + 1/(3 ln 3) + 1/(5 ln 5) + 1/(7 ln 7)
    # ≈ 0.7213 + 0.3033 + 0.1242 + 0.0735 ≈ 1.222. Well above 0.5.
    payload = {"x_floor": 2, "elements": [2, 3, 5, 7]}
    result = verify_witness(payload, _spec(0.5))
    assert result.is_valid is True
    assert "strictly verified counterexample" in result.reason
    assert result.score > 0.5


def test_verify_witness_rejects_non_primitive():
    payload = {"x_floor": 2, "elements": [2, 3, 6]}  # 2 | 6
    result = verify_witness(payload, _spec(0.0))
    assert result.is_valid is False
    assert "divides" in result.reason.lower()


def test_verify_witness_rejects_below_x_floor():
    payload = {"x_floor": 100, "elements": [50, 101, 103]}
    result = verify_witness(payload, _spec(0.0))
    assert result.is_valid is False
    assert "below x_floor" in result.reason


def test_verify_witness_rejects_x_floor_below_two():
    payload = {"x_floor": 1, "elements": [3, 5, 7]}
    result = verify_witness(payload, _spec(0.0))
    assert result.is_valid is False
    assert "x_floor" in result.reason


def test_verify_witness_rejects_malformed():
    # Not a dict.
    result = verify_witness("not a dict", _spec(0.5))  # type: ignore[arg-type]
    assert result.is_valid is False
    # Missing keys.
    result = verify_witness({}, _spec(0.5))
    assert result.is_valid is False
    result = verify_witness({"elements": [3]}, _spec(0.5))
    assert result.is_valid is False
    # Non-int element.
    result = verify_witness({"x_floor": 2, "elements": [3, "five", 7]}, _spec(0.5))
    assert result.is_valid is False
    # Non-list elements.
    result = verify_witness({"x_floor": 2, "elements": "not a list"}, _spec(0.5))
    assert result.is_valid is False


def test_verify_witness_threshold_just_above_true_sum_rejects():
    """Boundary case: threshold set just above the true sum must reject.
    The rigor of the lower bound matters most when the answer is close.
    Pick a small primitive set, compute its naive sum, and set threshold
    just above — verifier must reject (lower bound is below naive, hence
    below threshold)."""
    elements = [2, 3, 5, 7]  # naive sum ≈ 1.222
    naive = sum(1.0 / (a * math.log(a)) for a in elements)
    payload = {"x_floor": 2, "elements": elements}
    threshold = naive + 1e-9  # just above naive sum
    result = verify_witness(payload, _spec(threshold))
    # The rigorous lower bound is below the naive sum by some tiny amount;
    # threshold is above naive, so threshold > naive > rigor; must reject.
    assert result.is_valid is False, (
        f"verifier should reject threshold above naive sum; "
        f"naive={naive!r}, threshold={threshold!r}, score={result.score!r}, reason={result.reason!r}"
    )


def test_verify_witness_idempotent():
    """Running twice on the same input gives the same verdict and score."""
    payload = {"x_floor": 2, "elements": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]}
    r1 = verify_witness(payload, _spec(0.5))
    r2 = verify_witness(payload, _spec(0.5))
    assert r1.is_valid == r2.is_valid
    assert r1.score == r2.score


# --------------------------------------------------------------------------- #
# Spec ledger sanity (the JSON file is part of the witness contract)
# --------------------------------------------------------------------------- #

def test_problem_json_loads_and_has_required_fields():
    spec_path = REPO_ROOT / "proofs" / "primitive_set_erdos.json"
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)
    for required in (
        "name", "family", "track", "claim_status", "claim_latex",
        "given_facts", "witness_type", "witness_threshold",
        "witness_verifier_module", "witness_schema", "round_cap",
    ):
        assert required in spec, f"missing required field {required}"
    assert spec["track"] == "proof"
    assert spec["family"] == "primitive_set"
    assert spec["claim_status"] == "open"
    # Witness threshold is the conjectured bound.
    assert float(spec["witness_threshold"]) == 1.0
    # Given facts ledger has the three facts the user prompt named.
    facts = {f["id"] for f in spec["given_facts"]}
    assert "F1_erdos_zhang_upper" in facts
    assert "F2_omega_k_lower_unsigned" in facts
    assert "F3_omega_k_exact_below_one" in facts
    # F2 is the one whose sign is the load-bearing trap; verify the
    # disambiguation note flags "unsigned" so future critic_sign maintenance
    # doesn't accidentally drop the warning.
    f2 = next(f for f in spec["given_facts"] if f["id"] == "F2_omega_k_lower_unsigned")
    assert "UNSIGNED" in f2["sign_disambiguation"]
    assert "SIGN ERROR" in f2["sign_disambiguation"]


def test_problem_json_module_path_resolves():
    """The witness_verifier_module must point at this very module — keep
    the JSON in sync with the import path."""
    spec_path = REPO_ROOT / "proofs" / "primitive_set_erdos.json"
    with open(spec_path, encoding="utf-8") as f:
        spec = json.load(f)
    import importlib
    mod = importlib.import_module(spec["witness_verifier_module"])
    assert hasattr(mod, "verify_witness"), (
        f"{spec['witness_verifier_module']} is missing verify_witness"
    )
