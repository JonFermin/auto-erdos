# Session handoff (session s_0622-080320-1ed5)

**Stop reason**: logical milestone — all open questions resolved; Section 5 added and verified clean (0B 0W round 21)

**Current state**: 10 keep_progress records (rounds 7–12, 14, 16, 17 from prior session; R21 from this session).
Commit d88e3b7 is the cleanest: `partial_result`, 0 blocking, 0 warns.

**What was proved** (Sections 1–3, from F3 + primitivity only):
- [LP] s_k^A + W_k^A <= 1 - eps_k for primitive A, k >= K_0
- [LP_0] s_k^A <= 1 - eps_k (single-stratum bound)
- T(A) < 1 for single-stratum A in A_{k_0} ∩ [x,∞) with k_0 >= K_0
- K_0 >= 2 (proved by T({2,3}) > 1 via standard log values)

**What was added this session** (Section 5):
- Two-stratum bound [2S]: for A ⊆ A_k ∪ A_{k+1}: T(A) <= 2 - eps_k - eps_{k+1}
- Showed [2S] is too weak for the conjecture (approaches 2 as k → ∞)
- Identified [Shadow-LB] as the explicit sufficient condition for the two-stratum conjecture:
  W_{k+1}^A >= s_k^A - eps_k + o(1) would give T(A) <= 1 + o(1)
- Showed [Shadow-LB] requires Mertens-type estimates not in {F1, F2, F3}

**All open questions**: Q1-Q6 all resolved.

**Status table**:
| Statement | Status |
|---|---|
| s_k^A + W_k^A <= 1-eps_k (LP, F3 range) | Proved |
| s_k^A <= 1-eps_k (single-stratum) | Proved |
| T(A) < 1 for single-stratum A | Proved |
| T(A) <= 2-eps_k-eps_{k+1} (two-stratum) | Proved |
| [Shadow-LB]: W_{k+1}^A >= s_k^A - eps_k + o(1) | Open (sufficient but unproved) |
| Full conjecture: T(A) <= 1 + o(1) | Open |

**Suggested next move** (if continuing in a new session):
1. Attempt to prove [Shadow-LB] using F2 more carefully (even though F2's big-O is unsigned,
   a lower bound on W_{k+1}^A might still follow from counting prime multiples).
2. Or: explore the N-stratum generalization: for A ⊆ ∪_{j=k}^{k+N} A_j, one expects
   T(A) <= 1 + o(1) via iterated shadow coupling.
3. Or: accept the partial result as the final deliverable.

**Stability note**: The F2/F3 note (Section 1) remains stable. Do NOT reintroduce
numerical comparison calculations in that note (critic_numerical sensitivity).
