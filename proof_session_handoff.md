# Session handoff (session s_0504-024230-9a09)

**Stop reason**: One round logged. Returning to /loop driver.

**Round 36 contribution (§26.3d)**

Heuristic for the §26.3c x ~ sqrt(N) crossover.

Key observation: M(x, N)'s composites satisfy n < x * p_min(n) <=
x * sqrt(n), hence n < x^2. So M(x, N) for N >= x^2 has the same
composites as M(x, x^2) — adding more N doesn't add more
composites to M.

Multi-stratum can include composites in (x^2, N] that pass
cross-stratum exclusion. This window is empty when N < x^2,
non-empty when N > x^2 — yielding the crossover at N ~ x^2,
i.e., x ~ sqrt(N).

This is consistent with §22's alpha_{k_1, k_2} ~ 1/2 for
(k_1, k_2) = (2, 4): typical kept-window scale x^{1/alpha} = x^2.

**Status**

36 rounds, 26 sessions, 36 keeps, 0 disproofs.

**Files modified this session**

- proof_strategy.md — added §26.3d (~30 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 36 update.
- proof_open_questions.jsonl — Q35 claimed and resolved.
- proof_journal.jsonl — round 36 entry.
- 1 new record in records/.

**qid in flight**: none.
