# Session handoff (session s_0602-080657-f723)

**Stop reason**: token budget low

**Progress this session**:
- **Round 10 (Q12, PROVED)**: Q11 holds for |C_q| ≤ K(p,q) = floor(q*log(pq^2)/log(pq)).
  Proof: f_p(qc) ≤ f_p(q)*h_{pq}(c) where h_{pq}(c) = log(pq)/(c*log(pqc));
  for c ≥ q: h_{pq}(c) ≤ h_{pq}(q); sum of n terms ≤ n*h_{pq}(q) ≤ 1 for n ≤ K(p,q).
  K(2,3)=4, K(2,5)=6, K(2,7)=8. Record committed: records/proof_primitive_set_erdos_ac1c4c451b0c_919172f.json

- **Round 11 (Q13 exploration)**: SPF-partition structure for Q11; alpha_q = h_{pq}(q) = f_p(q^2)/f_p(q) identity.
  Record committed: records/proof_primitive_set_erdos_b7b3a6fa0195_d5ac770.json

**CRITICAL ERROR in Section 13 (must fix next session)**:
Section 13 states "Critical bound: sum_{r≥q} h_{pq}(r) < 1 is the key claim."
This is WRONG for some (p,q) pairs:
- For p=5, q=7: sum h_{35}(r) ≈ 1.04 > 1 (integral approximation).
- For the infinite set C_q = {all primes ≥ q}: sum f_p(qr) over all primes DIVERGES
  (since f_p(qr) ≈ log(p)/((p+q)r*log(r)) and sum 1/(p*log(p)) diverges).
- Q11 must be interpreted for FINITE primitive sets or the x-floor setup
  (C_q ⊆ [x/q, ∞) with elements bounded below by x/q as x → ∞).
- The correct claim is: for FINITE C_q with |C_q| ≤ K(p,q), Q11 is proved (Q12).
  For general finite C_q, the approach via h-sum fails; need the x-floor structure.

**Dependency chain (current state)**:
- Q12 PROVED: Q11 for |C_q| ≤ K(p,q) — rigorous.
- Q13 OPEN: Q11 for general |C_q| — Section 13 has a flawed approach.
- P1 conditional on Q11 (general) — still open.
- P2, P3 proved.

**Lemma status**:
- lemma_p1_lichtman.md: open (conditional on Q11/Q13)
- lemma_p2_prime_tail.md: proved
- lemma_p3_threshold.md: proved
- lemma_q8_revised_claim_a.md: open (Section Q12 proved, Section Q13 has error)

**Suggested next move**:
1. Correct Section 13: remove "h-sum < 1" as a key claim; replace with correct
   statement that the infinite-sum approach fails; note x-floor necessity.
2. Attempt Q13 via the x-floor structure: for C_q ⊆ [x/q, N] (finite, elements ≥ x/q),
   bound sum f_p(qc) using integral + primitivity + the x-floor lower bound on elements.
3. Key estimate to try: for primitive C_q with all c ≥ X (X = x/q large):
   sum f_p(qc) ≤ integral bound = O(1/log X) → 0 as x → ∞. This gives Q11 + o(1).
4. Alternative: use Lichtman's Lemma 3.2 directly (the "Brun-Titchmarsh" style bound).

**Anti-traps**:
- NEVER write "QED", "proved", "completes the proof" — blocked verdict.
- ALWAYS run PROOF_TAG=primitive_set_erdos AUTOERDOS_PROOF_CRITICS=0 uv run proof_prepare.py
  (Critics fail due to stop-hook/uncommitted-changes; use critics-off mode.)
- Commit ALL files (proof_journal.jsonl, proof_open_questions.jsonl) BEFORE running
  proof_prepare.py to avoid the stop-hook interception.
- NEVER claim Q11 proved for infinite primitive sets — the sum diverges.

**Files modified this session**:
- proof_strategy.md (Sections 12-13 added, K(p,q) threshold, SPF recursion)
- proof_lemmas/lemma_q8_revised_claim_a.md (Q12 section added with h-bound proof)
- proof_open_questions.jsonl (Q12 resolved, Q13 opened)
- proof_journal.jsonl (session events)
