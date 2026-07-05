# Session handoff (session s_0705-080628-17af)

**Stop reason**: Logical milestone — all 6 initial open questions (Q1–Q6) resolved.

**Current focus**: Rankin integral reformulation. The conjecture follows from:
  **Sub-claim**: For any primitive A ⊂ [x,∞) and all u > 1, F_A(u) := ∑_{a∈A} a^{-u} ≤ ∑_p p^{-u} =: F_P(u).
This is the KEY OPEN STEP and corresponds to Lemma `primes_are_extremal`.

**Status of lemmas**:
- `stratum_bound`: trivial (any subset ≤ full stratum), status: open (estimate needs F3 clarification)
- `cross_stratum_constraint`: proved (primitivity prevents divisibility across strata)
- `primes_are_extremal`: OPEN (the main gap — sub-claim F_A(u) ≤ F_P(u))
- `rankin_integral`: proved (identity 1/(a log a) = ∫_1^∞ a^{-u} du)

**qids in flight**: All 6 (Q1–Q6) are now resolved. No open qids.

**Key findings this session**:
1. F3 formula (1 - ck²/2^k) is an asymptotic as k→∞, NOT the full infinite-set sum.
   For k=1, the primes-from-2 sum is ~1.636 >> 0.967 (the F3 leading term).
2. No witness exists for x_floor=100, 1000, 10000 (primes give ~1/log(x) << 1).
   Trivial witness {2,3} exists at x_floor=2 but is not a meaningful counterexample.
3. Naive stratum decomposition diverges (sum of per-stratum bounds = sum over all n ≥ x = ∞).
4. Rankin integral: ∑_A 1/(a log a) = ∫_1^∞ F_A(u) du; conjecture ↔ F_A(u) ≤ F_P(u) ∀u>1.

**Files modified this session**:
- proof_strategy.md (Sections 1–5, Rankin approach)
- proof_lemmas/lemma_stratum_bound.md (created)
- proof_lemmas/lemma_cross_stratum_constraint.md (created, status: proved)
- proof_lemmas/lemma_primes_are_extremal.md (created, status: open)
- proof_lemmas/lemma_rankin_integral.md (created, status: proved)

**Suggested next move** (for next session):
1. Read Lichtman–Pomerance 2021 ("Primitive sets with large counting functions").
2. Transcribe their proof of the Rankin sub-claim into Lemma `primes_are_extremal`.
3. Once `primes_are_extremal` is proved (status: proved), the conjecture follows.
4. Consider running proof_prepare.py with AUTOERDOS_PROOF_CRITICS=1 for full critic
   screening before claiming convergence.
