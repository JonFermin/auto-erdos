# Session handoff (session s_0504-011718-36a5)

**Stop reason**: One round logged. Returning to /loop driver.

**This session's contribution (Round 34, §26.3b)**

Reconciled apparent tension between §26.2 (multi-stratum beats M
at N=10^6) and §26.3a (local search finds nothing at N=10^5):

Recomputed multi-stratum vs M at N=10^5:
  x=50:  multi-stratum gives +0.042 over M
  x=100: +0.031
  x=300: +0.014
  x=1000: -0.001 (multi-stratum LOSES to M)
  x=3000: -0.009
  x=10^4: -0.012

So the multi-stratum gain is N-dependent: positive when N is large
enough relative to x, negative otherwise. At small N relative to
x, the cross-stratum exclusion costs more than the high-k strata
contribute.

For the conjecture's regime (x → infty, N = infty), multi-stratum
does beat M, with bounded saturation gap.

**Status**

34 rounds, 24 sessions, 34 keeps, 0 disproofs.

**Files modified this session**

- proof_strategy.md — added §26.3b (~30 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 34 update.
- proof_open_questions.jsonl — Q33 claimed and resolved.
- proof_journal.jsonl — round 34 entry.
- 1 new record in records/.

**qid in flight**: none.

**Status: deeply converged**

The proof attempt now adds 1-2% incremental information per round.
Recommended pivot: paper writeup. Each successive analytical round
explores nuance without changing the central conclusions.
