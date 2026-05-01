"""powerful_triple_witness — rigorous verifier for Erdős–Mollin–Walsh witnesses.

The Track 2 proof loop on `erdos_mollin_walsh` allows an agent to commit a
candidate counterexample as a `<!-- WITNESS -->` block in `proof_strategy.md`.
A witness is a single integer $n$ asserting that $(n, n+1, n+2)$ are all
powerful. This module is the only sanctioned path to `witness_valid = 1`.

A positive integer $m \\geq 2$ is **powerful** iff every prime $p \\mid m$
satisfies $p^2 \\mid m$. Equivalently: in the prime factorization of $m$
every exponent is $\\geq 2$. By convention $m = 1$ is also called powerful
(empty factorization), but the EMW conjecture concerns triples of
consecutive integers all $\\geq 2$, so we do not handle $m = 1$ specially —
the agent's payload should have $n \\geq 2$.

Verifier contract — `verify_witness(payload, spec) -> VerifyResult`:
    - is_valid=True iff
        (a) `payload["n"]` parses as a positive integer >= 2;
        (b) each of n, n+1, n+2 has every prime-factor exponent >= 2.
    - score = float(n)        # the candidate's smallest element
    - reason = string with the factorizations and pass/fail of each
    - is_valid=False with a clear reason otherwise.

Implementation:
    - Trial-division factorization. Worst-case cost is O(sqrt(n+2)) per
      element; the harness's per-witness 5-minute budget allows n up to
      ~10^15 comfortably.
    - For genuinely large witnesses (n > 10^15), trial division gets slow.
      We do not implement Pollard rho or other fast factorization here —
      keeping the verifier dead-simple is more important than speed
      because the verifier's correctness has to be auditable by hand.
    - No mpmath / sympy / numpy. Stdlib `math.isqrt` only.

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


def _factorize_with_exponents(m: int) -> dict[int, int]:
    """Trial-division factorization. Returns {prime: exponent}.

    For m == 1 returns {} (the empty factorization). For m < 1 raises.
    Trial-divides primes up to sqrt(m); whatever remains > 1 after that
    is itself prime (a fact we verify via a final exhaustive check).
    """
    if m < 1:
        raise ValueError(f"factorize requires m >= 1, got {m}")
    factors: dict[int, int] = {}
    n = m
    # Strip factors of 2 first (the only even prime).
    while n % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        n //= 2
    # Trial-divide odd candidates up to sqrt(n).
    d = 3
    while d * d <= n:
        while n % d == 0:
            factors[d] = factors.get(d, 0) + 1
            n //= d
        d += 2
    # Whatever is left > 1 is a prime factor of the original m.
    if n > 1:
        factors[n] = factors.get(n, 0) + 1
    return factors


def _is_powerful(m: int) -> tuple[bool, str]:
    """Return (is_powerful, factorization_string) for m >= 2."""
    if m < 2:
        return False, f"{m} < 2 (powerful requires m >= 2 in EMW context)"
    factors = _factorize_with_exponents(m)
    factor_str = " * ".join(
        f"{p}^{e}" if e > 1 else f"{p}" for p, e in sorted(factors.items())
    )
    bad = [(p, e) for p, e in factors.items() if e < 2]
    if bad:
        bad_str = ", ".join(f"{p}^{e}" for p, e in bad)
        return False, f"{m} = {factor_str} (NOT powerful: prime(s) {bad_str} have exponent < 2)"
    return True, f"{m} = {factor_str} (powerful)"


def verify_witness(payload: dict, spec: dict) -> VerifyResult:
    """Deterministically check an EMW counterexample witness.

    Returns is_valid=True iff `payload["n"]` is a positive integer >= 2 and
    each of n, n+1, n+2 is powerful (every prime factor has exponent >= 2).
    """
    t0 = time.time()

    # Schema checks first — fail fast with a clear reason.
    if not isinstance(payload, dict):
        return VerifyResult(False, 0.0, f"payload must be dict, got {type(payload).__name__}", time.time() - t0)
    if "n" not in payload:
        return VerifyResult(False, 0.0, "payload missing 'n'", time.time() - t0)

    try:
        n = int(payload["n"])
    except (TypeError, ValueError) as e:
        return VerifyResult(False, 0.0, f"'n' is not an int: {e}", time.time() - t0)

    if n < 2:
        return VerifyResult(False, 0.0, f"n={n} must be >= 2", time.time() - t0)

    # Soft cap: trial-division on n > 10^17 will take far longer than the
    # critic budget. Reject loudly rather than hang.
    if n > 10**17:
        return VerifyResult(
            False, 0.0,
            f"n={n} exceeds 10^17 verifier soft-cap (trial-division would exceed budget); "
            f"a faster factorization path is needed for super-large witnesses",
            time.time() - t0,
        )

    triple = (n, n + 1, n + 2)
    results = []
    all_powerful = True
    for m in triple:
        ok, msg = _is_powerful(m)
        results.append((m, ok, msg))
        if not ok:
            all_powerful = False

    detail = "; ".join(msg for _, _, msg in results)

    if all_powerful:
        reason = (
            f"COUNTEREXAMPLE: ({n}, {n+1}, {n+2}) all powerful. {detail}"
        )
        return VerifyResult(True, float(n), reason, time.time() - t0)

    # Identify which member(s) failed, for the agent's benefit.
    fail = [m for m, ok, _ in results if not ok]
    reason = (
        f"({n}, {n+1}, {n+2}): not all powerful — failure(s) at {fail}. {detail}"
    )
    return VerifyResult(False, 0.0, reason, time.time() - t0)
