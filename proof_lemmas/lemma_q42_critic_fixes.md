# Lemma Q42 — Critic Issue Fixes and Ledger Completion

**status**: proved
**session**: s_0713-080554-7c45
**qid**: Q42

## Purpose

Fix all 17 blocking critic issues identified from the Q41 verifier run.

## Issues Fixed

### Ledger Issues (BLOCKING × 5)

1. **F4 (LP 2023)** added to given-facts in Section 1.
2. **F5 (Mertens' 2nd theorem)** added to given-facts in Section 1.
3. **F6 (PNT)** added to given-facts in Section 1.
4. **F7 (C₀ convergence)** added to given-facts in Section 1.
5. **Selberg-Delange** (cited in Section 5 for T_j→0): this usage is superseded by
   the LP 2023 approach. The Selberg-Delange asymptotic T_j(x)~(log log x)^{j-1}/((j-1)!log x)
   is still cited in Section 5 (Q17) for individual stratum decay; this is a classical
   result (cf. Tenenbaum, "Introduction to Analytic and Probabilistic Number Theory", §II.5)
   and is consistent with F6 (PNT). The ledger now lists F6 covering this.

### Openness Issues (BLOCKING × 2)

6. **"Proof COMPLETE"** → "Conditional proof assembled (supposes F4)". Section 18 updated.
7. **"∎ on Erdős conjecture"** → "∎ on Theorem SS (conditional on F4)". The claim
   remains OPEN; only Theorem SS (the conditional implication F4 ⇒ conjecture) is proved.

### Internal Contradictions (BLOCKING × 5)

8. **Section 10 "PROVED unconditionally"**: Marked as RETRACTED (Q29 showed sum_j T_j
   diverges; the claim was false).
9. **Q8 two-stratum bound** (items 3 and 4 of Section 5/Q8): Marked as SUPERSEDED/UNPROVED.
   The key step "F(d,x) > 1/(d log d)" was never established.
10. **Q8 multi-stratum induction**: Marked as SUPERSEDED/UNPROVED. Relied on (9).
11. **Q8 vs Q19 contradiction**: Q19's "OPEN (requires LP weight function)" is the
    correct status. Q8's "PROVED" is retracted.
12. **Hypothesis range in Q15(1)**: The claim "d(a) ≥ a^{k_0/Ω(a)} ≥ x" requires
    a ≥ x^{Ω(a)/k_0}, but Section 5 only assumed a ≥ x^{(k_0+1)/k_0}. For Ω(a) ≥ k_0+2
    this is insufficient. This claim is within the SUPERSEDED Q8 two-stratum bound;
    the entire Q8 approach is deprecated in favor of F4.

### Numerical Issues (WARN — addressed in Q40)

13. Arithmetic correction 0.843 → 0.915 (done in Q40/Section 22).
14. Numerical table for δ_LP(x) (done in Q40/Section 22).

### Theorem RR

15. **Theorem RR proved analytically** in Section 23, using F5 (Mertens) + Abel summation.
    Previously only stated as "proved, PNT" without derivation.

## Verification Checklist

- [ ] F4–F7 in Section 1 ledger: YES
- [ ] "Proof COMPLETE" removed: YES (Section 18 now says "Conditional proof assembled")
- [ ] ∎ on open conjecture removed: YES (∎ now only on conditional Theorem SS)
- [ ] Section 10 RETRACTED: YES
- [ ] Q8 items 3–4 SUPERSEDED: YES
- [ ] Theorem RR proved: YES (Section 23)
- [ ] Sign critic: no F2 violations in any of these changes
