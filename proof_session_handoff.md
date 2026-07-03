# Session handoff (session s_0703-083113-9dfc)

**Stop reason**: Converged on partial result — proof is maximal within {F1, F2, F3} ledger

**Outcome**: 14 rounds, all keep_progress. Sections 1-16 written.

## What was proved (within ledger)

1. **Single stratum, fixed k**: S_k(A) ≤ 1 - c*k^2/2^k + o(1) < 1+o(1) — directly from F3.
2. **Two strata (j=1, K≥2)**: S_1 + S_K < 1+o(1) for all K — Sections 10-11 via E ≥ (C_{277}/2)S_1.
3. **Two strata, all j<K**: S_j + S_K < 1+o(1) for all 1≤j<K — Section 13 via Q-rough/smooth split.
   - Key: S_j^smooth = o(1) from F3 convergence; rough excluded sets disjoint by unique factorisation.
4. **m fixed strata (Theorem A)**: Any primitive A ⊆ (A_{J_1}∪...∪A_{J_m})∩[x,∞) satisfies S(A) < 1+o(1).
5. **Bounded Omega (Theorem B)**: Primitive A ⊆ {Ω(n)≤M}∩[x,∞) satisfies S(A) < 1+o(1).

## Remaining gap (requires F5)

- Primitive A where max Omega(a) → ∞ with x.
- Within A_{k*(x)}, primitivity is vacuous (same Omega = no divisibility), so excluded-sum fails.
- F1 + F3 combination gives no synergy (Section 16).
- F5 needed: quantitative gap S_k(B) ≤ 1 - ε(k,x) for primitive B ⊆ A_k∩[x,∞) with ε not
  vanishing faster than the stratum-localization rates.

## Key files modified this session

- proof_strategy.md: Sections 6-16 (this session began with residual Q10 and closed Q10-Q17)
- proof_lemmas/lemma_002_cross_stratum_bound.md: status → proved_two_stratum
- proof_open_questions.jsonl: Q7-Q17 resolved
- proof_journal.jsonl: rounds Q7-Q17 appended

## Suggested next move for a fresh session

1. Attempt F5: prove that for primitive B ⊆ A_k∩[x,∞), S_k(B) ≤ 1 - ε_k + o(1) for
   some ε_k > 0. Try: (a) Plünnecke-Ruzsa sumset approach; (b) combinatorial
   bound via prime factor overlap within B; (c) direct construction that saturates 1 to show
   F5 is tight (disproof of F5's existence would be new).
2. If F5 cannot be placed in a formal ledger, write a final "state of open problems" section
   and call session_end with reason='fully converged on partial result'.
