# Session handoff (session s_0504-003511-fa34)

**Stop reason**: One round logged. Returning to /loop driver.

**This session's contribution (Round 33, §26.3a)**

A background experiment from earlier sessions completed:
single-element-swap local search around M(x, N=10^5) finds NO
primitive subset improving on S(M) at x in {50, 100, 300, 1000,
3000, 10000}. So M is locally maximal under that perturbation.

Combined with §26.2's multi-stratum global gain (+0.055 at
N=10^6): two distinct optimisation regimes. Local search around
M is stable; multi-stratum global constructions exceed M but are
invisible to local moves.

This refines the picture without changing the conclusion:
  sup_A S(A) ~ S(M) + bounded additive overhead.

**Status**

33 rounds, 23 sessions, 33 keeps, 0 disproofs.

**For future sessions**

The proof attempt continues to add fractional refinements with
each round. The natural next-step pivots are:
1. Paper writeup via write_paper.py (unchanged recommendation).
2. Sieve to N=10^8 for x=10^4 to give exact ratio.
3. Investigate whether M's local stability extends to k-element
   swaps (k=2, 3, ...) — would constrain how much multi-stratum
   constructions can beat M.

Each gives diminishing returns relative to the converged state.

**Files modified this session**

- proof_strategy.md — added §26.3a (~25 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 33 update.
- proof_open_questions.jsonl — Q32 claimed and resolved.
- proof_journal.jsonl — round 33 entry.
- 1 new record in records/.

**qid in flight**: none.
