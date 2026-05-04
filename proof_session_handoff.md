# Session handoff (session s_0503-183514-b863)

**Stop reason**: One round logged. Returning to /loop driver.

**This session's contribution (Round 22, Section 21)**

Audited the §13/§20 distributional model. Key findings:

1. §13 used "log p uniform on [log 2, log u]" — NOT classical
   Erdős-Kac (which is loglog p uniform).
2. Both §13 and a corrected Erdős-Kac model OVERESTIMATE
   empirical E[log delta_2] by factors of 2-3 across (k_2 = 3, 4, 5, 6).
3. Reason: discreteness of small primes (P(smallest prime = 2) = 1/2)
   makes empirical delta_2 much smaller than continuous models predict.

CONSEQUENCE: §20's saddle-point heuristic gives a Gaussian-tail
bound on rho_k that is COMPUTED RELATIVE TO THE WRONG MEAN. Since
the true mean is smaller, more of A_{k_2} satisfies the constraint,
so rho_k is LARGER than §20 predicts. The §20 conclusion
"sum rho_k = O(L) = o(log x)" was therefore overconfident.

Whether the corrected model still gives o(log x) is not yet known.

**For next session**

Two productive paths:

(a) **Recompute the saddle-point with correct discrete model.**
    Reference: Tenenbaum III.3-III.6 or Ford 2008 (smallest prime
    factor). Even without literature access, an empirical sieve
    can give the right mean and variance for E[log delta_{k_1}]
    at multiple (k_1, k_2, u) and back-out a model.

(b) **Re-examine the §18 numerical decay.** §18 showed
    sup_two-stratum S decays 0.337 -> 0.133 across x = 10^2..10^4.
    If the §20 heuristic predicts SMALLER decay than observed,
    that's evidence the cross-stratum framework is fundamentally
    incomplete and multi-stratum interactions matter.

Recommendation: (a) first via empirical sieve. Compute the empirical
distribution of log delta_{k_1} for several (k_1, k_2) pairs at
varying u, and fit it to a parametric model. The "right" mean
should then plug back into §20's framework cleanly.

**Files modified this session**

- proof_strategy.md — added Section 21 (~100 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 22 update.
- proof_open_questions.jsonl — Q21 claimed and resolved.
- proof_journal.jsonl — round 22 entry.
- 1 new record in records/.

**qid in flight**: none. Next is Q22.

**Status update**

22 rounds across 13 sessions. 22 keeps. 0 disproofs. The §20
heuristic has been invalidated; the proof is back to "Lemma 3
remains open with clear directions but no rigorous closing
argument". The §13+§20 sequence is no longer a proof sketch — it's
a heuristic that has been audited and corrected.

This is honest: the loop is identifying its own errors. Better
than a confident wrong answer.
