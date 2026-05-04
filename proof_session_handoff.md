# Session handoff (session s_0504-070306-564e)

**Stop reason**: One round logged. Returning to /loop driver.

**Round 42 contribution (§29.5g_pre)**

Clarified the regime distinction between two asymptotics:
- §19 incomplete-Gamma form: a_k(x; infty) ~ (1/log x) sum_{j=0..k-1} L^j/j!
  derives from Sigma_{A_k}(t) ~ (loglog t)^k/k! valid only for k <= L = loglog x.
- §11 Sathe-Selberg: S(A_k) = 1 - (c + o(1)) k^2/2^k as k -> infty,
  valid unconditionally as k grows.

For k_x = ceil(log_2 x) >> L: §11 applies, §19 does not.

The §29.5e Corollary D (S(A_{k_x}) -> 1) is rigorous via §11
(Sathe-Selberg), not via §19. Earlier numerics that mixed the two
were incorrect.

**Status**

42 rounds, 32 sessions, 42 keeps, 0 disproofs.

**Files modified this session**

- proof_strategy.md — added §29.5g_pre (~20 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 42 update.
- proof_open_questions.jsonl — Q41 claimed and resolved.
- proof_journal.jsonl — round 42 entry.
- 1 new record in records/.

**qid in flight**: none.
