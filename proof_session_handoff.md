# Session handoff (session s_0504-015936-2581)

**Stop reason**: One round logged. Returning to /loop driver.

**Round 35 contribution (§26.3c)**

Tabulated multi-stratum gap (with K={2..6}) vs M across
(x, N) ∈ {(50..10^4) × (10^4, 10^5, 10^6)}.

Found clean crossover scale: multi-stratum > M iff x <~ sqrt(N).
At fixed x: gap grows with N. At fixed N: gap goes from positive
(x small) through zero (x ~ sqrt N) to negative (x > sqrt N).

For conjecture (N = infty): crossover absent, multi-stratum
always beats M but by bounded amount (§26.3 saturation).

**Status**

35 rounds, 25 sessions, 35 keeps, 0 disproofs.

**Files modified this session**

- proof_strategy.md — added §26.3c (~30 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 35 update.
- proof_open_questions.jsonl — Q34 claimed and resolved.
- proof_journal.jsonl — round 35 entry.
- 1 new record in records/.

**qid in flight**: none.

**Continuing assessment**

Loop saturating. Each round adds 1-2% nuance to the converged
picture. Paper writeup remains the natural pivot.
