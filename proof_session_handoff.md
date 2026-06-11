# Session handoff — s_0611-080505-e1cc

**Stop reason**: 4 productive rounds complete; context approaching limit.

**Current focus**: Proof is in "partial result" state with 4 newly proved sub-results and two hard gaps precisely identified.

**qid in flight**: None. Q7 and Q8 resolved as partial.

**Proved this session:**
1. `stratum_bound` (status: proved): each stratum contributes < 1 (F3 + monotonicity).
2. `single_interval` (status: proved, round 5): for A ⊆ [x, 2x), sum < log2/logx from calculus. This is the single-block case of f1_gap.
3. Cross-stratum sum < 1.399 (F1 directly, documented in Q7).
4. Low-k strata contribute o(1) as x → ∞ (F3 convergence, tail argument, documented in Q7).

**Still open (the two hard gaps):**
- **Gap 1 (high-k coupling)**: lemma_cross_stratum_sum: the primitive antichain constraint must suppress total contributions across all high-k strata. Approaches tried: cascade (blocked by Mertens/non-overlap not in ledger), F1 bound (gives 1.399, not 1).
- **Gap 2 (multi-block f1_gap)**: extending Lemma single_interval from one dyadic block to A spanning multiple blocks. The naive dyadic sum diverges (sum of 1/logx + 1/log(2x) + ... diverges) — cross-block primitive constraints are needed.

**Critical lesson from this session**: The cascade argument using Mertens (not in given-facts ledger) triggers BLOCKING from critic_ledger even when labeled "informal". Any mathematical inequality in the proof body (even in a section explicitly labeled heuristic) gets checked if it's load-bearing. The fix is to either add Mertens to the given-facts ledger, or avoid using it entirely.

The k=2..5 partial sum table triggered a complex Omega-lambda from the numerical critic that errors in sandboxed eval → BLOCKING. The fix was to replace it with an analytic F3 reference.

**Numerical findings:**
- Fat antichain [101,201): sum ≈ 0.1396; [1001,2001): sum ≈ 0.0956 (both verified via witness API)
- No witness found for x_floor ≥ 100 across primes, fat antichains, 3-almost-primes

**Files modified this session:**
- proof_strategy.md (Section 2 Q2 rewritten analytically, Section 3 two proved lemmas added, Section 4 cumulative proved results + precise gaps)
- proof_lemmas/lemma_cross_stratum_sum.md (partial proofs from F1 and tail argument added)
- proof_lemmas/lemma_f1_gap.md (Zhang-sieve structural claim removed, empirical evidence added, smooth-rough decomposition outlined)
- proof_lemmas/lemma_stratum_bound.md (status: proved)
- proof_lemmas/lemma_single_interval.md (NEW, status: proved)

**Suggested next move:**
1. Read this handoff and proof_strategy.md Section 4.
2. Open new Q9: attempt to prove the multi-block case of f1_gap via cross-block primitive constraints. Key question: if A ∩ [x, 2x) is large (contributes ε to the sum), does the primitive constraint force A ∩ [2x, 4x) to be small? Try: for each a ∈ A ∩ [x, 2x), the element 2a ∈ [2x, 4x) is excluded. How many elements of [2x, 4x) does this exclude? If |A ∩ [x,2x)| = m, then m elements of [2x, 4x) are excluded (exactly one per element: 2a). This gives |A ∩ [2x, 4x)| ≤ 2x - m... but bounding m vs. contribution is the key.
3. Alternatively, open Q10: try to prove a Sidon-type or inclusion-exclusion bound for the two-block primitive case.
4. If both are blocked by the ledger, add Mertens' theorem or the prime count estimate to the given_facts.json — but this is a repo decision (modifying proofs/primitive_set_erdos.json) that should be made deliberately.
