"""sum_product_witness — rigorous verifier for Erdős–Szemerédi sum-product witnesses.

The Track 2 proof loop on `erdos_szemeredi_sum_product` allows an agent to
commit a candidate witness as a `<!-- WITNESS -->` block in
`proof_strategy.md`. A witness is a finite set $A$ of distinct positive
integers together with a parameter $\\varepsilon$. The agent claims
$|A + A| + |A \\cdot A| < |A|^{2 - \\varepsilon}$ — a "violation" of a
specific quantitative form of the Erdős–Szemerédi sum-product conjecture.

Verifier contract — `verify_witness(payload, spec) -> VerifyResult`:
    - is_valid=True iff
        (a) `payload["elements"]` is a non-empty list of distinct positive integers;
        (b) `payload["eps"]` parses as a float in (0, 1);
        (c) $|A+A| + |A \\cdot A| < |A|^{2 - \\varepsilon}$ (strict).
    - score = $|A+A| + |A \\cdot A|$ (the witness's combined sumset+productset cardinality)
    - reason = string explaining the cardinalities and the threshold
    - is_valid=False with a clear reason otherwise.

Implementation:
    - Sumset and productset constructed by Python `set` comprehensions.
      O(|A|^2) in time, O(|A|^2) in memory. For |A| up to a few thousand
      this fits comfortably under the per-witness budget.
    - The `eps` parameter is read from the payload, not the spec — the
      spec's `witness_threshold` is fixed by configuration, but the agent
      may target different ε values across rounds; we honour both.
    - Threshold computed as $|A|^{2 - \\varepsilon}$ in float, then
      ceiled. Any integer strictly less than $\\lceil |A|^{2-\\varepsilon} \\rceil$
      is also strictly less than the real-valued threshold.

Match `library.primitive_set_witness.VerifyResult` shape so callers can
swap. (proof_prepare imports `verify_witness` by name from the configured
module and reads `.is_valid`, `.score`, `.reason`, `.verifier_seconds`.)
"""
from __future__ import annotations

import math
import time
from dataclasses import dataclass


@dataclass
class VerifyResult:
    is_valid: bool
    score: float
    reason: str
    verifier_seconds: float


_DEFAULT_EPS = 2.0 / 3.0  # the Solymosi (2009) regime: threshold ~ |A|^{4/3}


def _sumset_cardinality(elements: list[int]) -> int:
    """|A + A| via Python set."""
    return len({a + b for a in elements for b in elements})


def _productset_cardinality(elements: list[int]) -> int:
    """|A · A| via Python set."""
    return len({a * b for a in elements for b in elements})


def verify_witness(payload: dict, spec: dict) -> VerifyResult:
    """Deterministically check a sum-product witness."""
    t0 = time.time()

    if not isinstance(payload, dict):
        return VerifyResult(False, 0.0, f"payload must be dict, got {type(payload).__name__}", time.time() - t0)
    if "elements" not in payload:
        return VerifyResult(False, 0.0, "payload missing 'elements'", time.time() - t0)

    raw_elements = payload["elements"]
    if not isinstance(raw_elements, list):
        return VerifyResult(False, 0.0, f"'elements' must be list, got {type(raw_elements).__name__}", time.time() - t0)

    try:
        elements = [int(x) for x in raw_elements]
    except (TypeError, ValueError) as e:
        return VerifyResult(False, 0.0, f"'elements' contains non-integer: {e}", time.time() - t0)

    n = len(elements)
    if n < 2:
        return VerifyResult(False, 0.0, f"|A|={n} too small (need >= 2 for non-trivial sum-product)", time.time() - t0)

    if any(a <= 0 for a in elements):
        return VerifyResult(False, 0.0, "elements must be positive integers", time.time() - t0)

    distinct = set(elements)
    if len(distinct) != n:
        return VerifyResult(False, 0.0, f"elements not distinct (|set|={len(distinct)} vs |list|={n})", time.time() - t0)

    # Soft cap to keep the verifier's O(|A|^2) work inside the budget.
    if n > 5000:
        return VerifyResult(
            False, 0.0,
            f"|A|={n} exceeds 5000 verifier soft-cap (|A+A|+|A*A| would exceed memory/time budget)",
            time.time() - t0,
        )

    # eps: prefer payload, fall back to spec, fall back to default.
    eps = payload.get("eps")
    if eps is None:
        eps = spec.get("default_eps", _DEFAULT_EPS)
    try:
        eps = float(eps)
    except (TypeError, ValueError) as e:
        return VerifyResult(False, 0.0, f"'eps' is not a float: {e}", time.time() - t0)
    if not (0.0 < eps < 1.0):
        return VerifyResult(False, 0.0, f"eps={eps} must lie strictly in (0, 1)", time.time() - t0)

    # Compute |A+A|, |A·A|, and the combined.
    sumset_card = _sumset_cardinality(elements)
    productset_card = _productset_cardinality(elements)
    combined = sumset_card + productset_card

    # Threshold: ceil(|A|^{2 - eps}). A combined value strictly less than
    # this ceiling is strictly less than the real-valued threshold.
    threshold_real = float(n) ** (2.0 - eps)
    threshold_ceil = math.ceil(threshold_real)

    is_witness = combined < threshold_ceil

    summary = (
        f"|A|={n}, eps={eps:.6f}; |A+A|={sumset_card}, |A*A|={productset_card}, "
        f"combined={combined}; threshold |A|^(2-eps) = {threshold_real:.6f} (ceil {threshold_ceil})"
    )

    if is_witness:
        reason = f"COUNTEREXAMPLE candidate: {summary}; combined < threshold strictly"
        return VerifyResult(True, float(combined), reason, time.time() - t0)
    reason = f"{summary}; combined >= threshold, so NOT a witness"
    return VerifyResult(False, float(combined), reason, time.time() - t0)
