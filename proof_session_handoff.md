# Session handoff (s_0502-191106-4665)

**Stop reason**: Loop wind-down. The autonomous proof loop has
plateaued: 16 rounds across 8 sessions, all critics-off,
all keep_progress. Section 15 consolidates the partial result and
identifies the literature gap (Sathe-Selberg constant) as the
single missing analytical fact that would close the CST conjecture.

**Final state**

- 16 keep_progress rounds, 0 keep_disproof, 0 crashes-causing-loss.
- 15 sections in proof_strategy.md (~1100 lines).
- 3 lemma files in proof_lemmas/.
- 16 records in records/proof_primitive_set_erdos_*.json.
- The conjecture remains OPEN. No false claim of resolution slipped
  through â€” the witness verifier and resolution-string defense-in-
  depth held for all 16 rounds.

**The substantive findings (in priority order)**

1. (Â§9) sum_k k^2/2^k = 6 exactly. F3 total deficit 6c â‰ˆ 0.394 vs.
   F1 gap â‰ˆ 0.399 â€” within 0.005 numerically. If exactly equal,
   the CST conjecture closes the gap structurally.
2. (Â§11) Sigma_{A_k}(t) ~ (loglog t)^k / k!, max attained at k =
   loglog t exactly Behrend's bound. Single-stratum saturates only
   at one t.
3. (Â§12) Incomplete-Gamma representation:
   S(A_k cap [x, infty)) ~ Gamma(k, loglog x)/(k-1)!
   = P(Poisson(loglog x) < k).
4. (Â§13) Cross-stratum threshold k_1 ~ sqrt(2 k_2) (Erdos-Kac
   heuristic + numerical validation).
5. (Â§14) Multi-stratum max-S empirically 0.366 at x=100, N=10^6
   (K = {2,3,4,5}). 27% over single-stratum.

**For a future session resumer**

If you have web access: look up the analytical value of c in F3
(Sathe-Selberg / Selberg 1954). If c = (e^gamma pi/4 - 1)/6
exactly, the CST conjecture's closing direction is structural;
otherwise the Â§9 coincidence is numerical.

If you want to push further with autonomous tools: the SA
experiment of round 16 (this session) had a temperature bug
(T = 0.001 was too large vs. weights ~ 1e-6, every move accepted).
Retry with T ~ 1e-7 to 1e-8 and proper cooling.

If the user wants to ship this as a partial result paper:
write_paper.py against any record/proof_primitive_set_erdos_*.json
will produce an amsart writeup. The proof body is honest about the
gap (Lemma 3 = the conjecture itself).

The loop is wound down. No ScheduleWakeup to follow.
