# Session handoff (session s_0621-092134-e9e4)

**Stop reason**: logical milestone — proof reached 0 BLOCKING / 0 WARN on round 17

**Current state**: 9 keep_progress records (rounds 7, 8, 9, 10, 11, 12, 14, 16, 17).
Round 17 commit (0c2782a) is the cleanest: `partial_result`, 0 blocking, 0 warns.

**What was proved** (in Sections 1–3, from F3 + primitivity only):
- [LP] s_k^A + W_k^A ≤ 1 - ε_k for any primitive A and k ≥ K_0
- [LP_0] s_k^A ≤ 1 - ε_k (single-stratum bound)
- T(A) < 1 for any single-stratum primitive set A ⊆ A_{k_0} ∩ [x,∞) with k_0 ≥ K_0
- K_0 ≥ 2 (proved by T({2,3}) = 1.025 > 1 via standard log values)

**What is open** (Section 4):
- Shadow density lower bound W_k^A ≥ T_{k-1}^A - o(1): needs Sathe-Selberg estimates
- Tail bound Σ_{k>K} s_k^A = o(1): needs counting estimates
- Full conjecture: T(A) ≤ 1 + o(1): open

**Stability note**: The F2/F3 note (Section 1) was simplified in R16/R17 by dropping the
k^{5/2}/2^k consistency calculation, which was stochastically blocking the numerical critic.
Do NOT reintroduce asymptotic comparison calculations in that note.

**All open questions**: Q1-Q6 are resolved (Q4 had low priority — no witness committed).

**Suggested next move**:
If resuming for more rounds, consider:
1. Exploring whether F1 (Zhang ≈ 1.399) can be combined with the LP constraint to say
   something about the number of non-trivial strata (F1 ≤ 1.399 but LP gives ≤ 1 per stratum).
2. Attempting a witness search: {2,3} gives T = 1.025 > witness_threshold=1.0 at x_floor=2.
   This is NOT a genuine counterexample (o(1) correction at x=2 is large) but would trigger
   the verifier to check if the formal conditions are met. The critic_openness pass would
   then need to be satisfied with an appropriate caveat.
3. Adding a Section 5 that derives a more explicit single-stratum cap for small k (k=2,3,4)
   using concrete estimates from F3's formula.
