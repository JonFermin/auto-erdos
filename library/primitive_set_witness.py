"""primitive_set_witness — rigorous verifier for primitive-set counterexample witnesses.

The Track 2 proof loop allows the agent to commit a candidate "counterexample"
to Erdős's primitive-set conjecture as an embedded `<!-- WITNESS -->` block
inside `proof_strategy.md`. This module is the *only* sanctioned path to the
``counterexample_proven`` verdict — it must be paranoid about float rounding
because a bug here would let the loop claim a disproof of an open problem.

A witness payload is a JSON object with:

    {
      "x_floor": int,                       # every element must be >= x_floor
      "elements": list[int],                # pairwise non-divisible
      "claimed_sum_lower_bound": float      # agent's claim, recomputed below
    }

``verify_witness(payload, spec)`` returns a ``VerifyResult`` (mirroring
``prepare.VerifyResult``):
    - is_valid=True iff (a) every element is an int >= max(2, x_floor), (b)
      pairwise non-divisible (no element divides another), and (c) a
      provably-lower-bound on sum 1/(a log a) strictly exceeds
      ``spec["witness_threshold"]``.
    - score = the rigorous lower bound on the sum (a Python float; the
      Decimal-based bound is also returned in `result.reason` for audit).

Rigor approach (no new dependencies — stdlib only):

    1. For each integer ``a >= 2``, compute ``log(a)`` with ``math.log``.
       Bump it upward by 4 ULPs via ``math.nextafter`` to obtain a guaranteed
       strict upper bound on the true natural log. (libm ``log`` is accurate
       to ~1 ULP on every IEEE-754 platform we ship to; 4 ULPs is generous.)
    2. Wrap that float with ``Decimal(repr(.))``. Compute ``a * upper_log_a``
       exactly in Decimal. ``1 / (a * upper_log_a)`` is then a strict lower
       bound on the true ``1 / (a * log a)``.
    3. Sum these lower bounds in Decimal at ``getcontext().prec = 80``.
    4. Compare against ``spec["witness_threshold"]`` (also coerced to
       Decimal). The comparison is exact in Decimal.

The factor-4 ULP slack is documented in ``_log_strict_upper_bound`` and
exercised by ``tests/test_witness_rigor.py``. If a future libm regression
ever returned a log that exceeds the true value by more than 4 ULPs we'd
notice via the float-equality regression test that pins the rigorous
bound for the canonical ``A_k`` set sum (which is known to be < 1).

Pairwise non-divisibility check: O(k log max) sieve. We sort once, then for
each element scan its multiples in the sorted set via a hash. Faster than the
O(k^2) naive divisor scan and trivially correct.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from decimal import Decimal, getcontext
from typing import Iterable

# Match prepare.VerifyResult's shape so log_result-style callers can swap.
@dataclass
class VerifyResult:
    is_valid: bool
    score: float
    reason: str
    verifier_seconds: float


# Decimal precision: 80 digits is overkill for any realistic witness size
# (the sum has order-of-magnitude 1, and we never need more than ~20
# significant digits to decide whether it strictly exceeds 1.0). Keeping
# it large means the running sum can accumulate without precision loss.
_DECIMAL_PREC = 80
_LOG_ULP_SLACK = 4  # number of ULPs to bump math.log() upward


def _log_strict_upper_bound(a: int) -> Decimal:
    """Provable strict upper bound on ln(a), as a Decimal.

    We compute log(a) in IEEE-754 double precision and then bump it
    upward by 4 ULPs via math.nextafter. On every platform whose libm
    log is accurate to within 4 ULPs (a generous slack — every modern
    libm is within 1-2 ULPs), the returned value strictly exceeds the
    true natural log. We require a >= 2 so that ln(a) > 0 — calling
    this on a in {0, 1} is a programming error.
    """
    if not isinstance(a, int):
        raise TypeError(f"a must be int, got {type(a).__name__}")
    if a < 2:
        raise ValueError(f"a must be >= 2, got {a}")
    val = math.log(a)
    if not math.isfinite(val) or val <= 0:
        # log(a) for a >= 2 is finite and positive; this is unreachable on
        # any sane libm. Surface as a defensive error rather than a silent
        # zero-divide downstream.
        raise RuntimeError(f"unexpected math.log({a}) = {val!r}")
    bumped = val
    for _ in range(_LOG_ULP_SLACK):
        bumped = math.nextafter(bumped, math.inf)
    # Decimal(repr(float)) preserves the float's exact bit-pattern as a
    # Decimal. Decimal(float) directly does the same but with platform-
    # dependent rounding for repr-shorter floats; using repr() is safer.
    return Decimal(repr(bumped))


def _check_pairwise_non_divisible(elements: list[int]) -> tuple[bool, str]:
    """Return (ok, reason). Sorts in place; we do not need stable order."""
    if not elements:
        return True, "empty primitive set is trivially primitive"
    elements_sorted = sorted(elements)
    seen: set[int] = set()
    for x in elements_sorted:
        if x in seen:
            return False, f"duplicate element {x} in candidate"
        seen.add(x)
    # For each element a, scan multiples a, 2a, 3a, ... up to max(elements).
    # If any multiple > a is in seen, a divides that element — primitive
    # condition violated. O(sum_{a in S} max/a) which is at most O(k * max/min).
    max_el = elements_sorted[-1]
    for a in elements_sorted:
        if a < 2:
            return False, f"element {a} below minimum 2 (primitivity is meaningless for 1 or below)"
        # Start at 2a — `a divides a` is trivially true and not a violation.
        m = 2 * a
        while m <= max_el:
            if m in seen:
                return False, f"{a} divides {m} — both in candidate, primitivity violated"
            m += a
    return True, "pairwise non-divisible"


def _rigorous_sum_lower_bound(elements: Iterable[int]) -> Decimal:
    """Strict lower bound on sum_{a in elements} 1/(a log a), in Decimal.

    For each a we compute an upper bound on log(a) via _log_strict_upper_bound
    (rigorous), so 1/(a * upper_log_a) is a strict lower bound on the true
    1/(a log a). Summing strict lower bounds gives a strict lower bound on
    the total. Decimal arithmetic at prec=80 introduces no measurable error
    on summands of this magnitude.
    """
    getcontext().prec = _DECIMAL_PREC
    total = Decimal(0)
    for a in elements:
        if a < 2:
            raise ValueError(f"element {a} < 2 has undefined log term")
        upper_log = _log_strict_upper_bound(int(a))
        denom = Decimal(int(a)) * upper_log
        if denom <= 0:
            raise RuntimeError(f"non-positive denom for a={a}: {denom}")
        total += Decimal(1) / denom
    return total


def verify_witness(payload: dict, spec: dict) -> VerifyResult:
    """Deterministically check a counterexample witness.

    Returns ``is_valid=True`` iff the payload is a primitive set whose
    rigorous lower bound on sum 1/(a log a) strictly exceeds
    ``spec["witness_threshold"]``. The returned ``score`` is the rigorous
    lower bound (a float — the full-precision Decimal is in ``reason`` for
    audit-trail purposes).
    """
    import time
    t0 = time.time()

    # Schema checks first — fail fast with a clear reason.
    if not isinstance(payload, dict):
        return VerifyResult(False, 0.0, f"payload must be dict, got {type(payload).__name__}", time.time() - t0)
    if "elements" not in payload:
        return VerifyResult(False, 0.0, "payload missing 'elements'", time.time() - t0)
    if "x_floor" not in payload:
        return VerifyResult(False, 0.0, "payload missing 'x_floor'", time.time() - t0)

    raw_elements = payload["elements"]
    if not isinstance(raw_elements, list):
        return VerifyResult(False, 0.0, f"'elements' must be list, got {type(raw_elements).__name__}", time.time() - t0)

    try:
        elements = [int(x) for x in raw_elements]
    except (TypeError, ValueError) as e:
        return VerifyResult(False, 0.0, f"'elements' contains non-integer: {e}", time.time() - t0)

    try:
        x_floor = int(payload["x_floor"])
    except (TypeError, ValueError) as e:
        return VerifyResult(False, 0.0, f"'x_floor' is not an int: {e}", time.time() - t0)

    if x_floor < 2:
        return VerifyResult(False, 0.0, f"x_floor={x_floor} must be >= 2 (log undefined for a in {{0,1}})", time.time() - t0)

    try:
        threshold = Decimal(repr(float(spec["witness_threshold"])))
    except (KeyError, TypeError, ValueError) as e:
        return VerifyResult(False, 0.0, f"spec['witness_threshold'] missing or unparseable: {e}", time.time() - t0)

    # Floor check: every element must be at least x_floor.
    for a in elements:
        if a < x_floor:
            return VerifyResult(False, 0.0, f"element {a} below x_floor={x_floor}", time.time() - t0)

    # Primitivity.
    ok, reason = _check_pairwise_non_divisible(elements)
    if not ok:
        return VerifyResult(False, 0.0, reason, time.time() - t0)

    # Rigorous sum lower bound.
    try:
        lower_bound = _rigorous_sum_lower_bound(elements)
    except (ValueError, RuntimeError) as e:
        return VerifyResult(False, 0.0, f"rigorous sum failed: {e}", time.time() - t0)

    is_counterexample = lower_bound > threshold
    score_float = float(lower_bound)
    if is_counterexample:
        reason = (
            f"rigorous_lower_bound={lower_bound} > threshold={threshold} "
            f"(|S|={len(elements)}, x_floor={x_floor}); strictly verified counterexample"
        )
    else:
        reason = (
            f"rigorous_lower_bound={lower_bound} <= threshold={threshold} "
            f"(|S|={len(elements)}, x_floor={x_floor}); does NOT exceed threshold"
        )
    # Truncate the Decimal repr in the reason if it's huge.
    if len(reason) > 500:
        reason = reason[:497] + "..."

    return VerifyResult(is_counterexample, score_float, reason, time.time() - t0)
