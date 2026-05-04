# Session handoff (session s_0503-190516-c36f)

**Stop reason**: One round logged. Returning to /loop driver.

**This session's contribution (Round 23, Section 22)**

Empirical fit at N=2*10^6: for each (k_1, k_2),
  E[log delta_{k_1}(b) | b in A_{k_2}, b ~ u] = alpha * log u + beta
with R^2 > 0.999 across u-bins 10^2..10^6.

Empirical alpha values are 1.4-12x SMALLER than §13's k_1^2/(2 k_2)
prediction. Discrepancy grows with k_2/k_1 ratio. Suggests
alpha_{L, k_2} decays roughly like (1/2)^{k_2 - L} super-exponentially.

Implication: the §13/§20 single-dominant-k_1 framework predicts much
stronger exclusion than actually exists. Cross-stratum exclusion via
k_1 = L alone is weak. The conjecture's truth must rely on cumulative
multi-k_1 exclusion across all k_1 < k_2.

**For next session: try multi-k_1 cumulative bound**

Define heuristic upper bound:
  rho^*_{k_2}(x) := prod_{k_1=1..k_2-1} P(delta_{k_1}(b) >= x)
                  = prod (1 - rho^{(k_1)}_{k_2})
assuming approximate independence across k_1. (Independence isn't
exactly true but is a starting heuristic.)

Compute rho^*_{k_2}(x) using §22 empirical alpha values and
Gaussian-tail approximation for std. Then check if
sum_{k_2} a_{k_2}(x) rho^*_{k_2}(x) stays <= 1 + o(1) as x -> inf.

If yes: the multi-k_1 framework is plausibly enough.
If no: need genuinely non-pairwise primitivity arguments.

**Files modified this session**

- proof_strategy.md — added Section 22 (~145 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 23 update.
- proof_open_questions.jsonl — Q22 claimed and resolved.
- proof_journal.jsonl — round 23 entry.
- 1 new record in records/.

**qid in flight**: none. Next is Q23.

**Status**

23 rounds across 14 sessions. 23 keeps. 0 disproofs. Conjecture
remains open. The §22 empirical data is the cleanest quantitative
input the loop has produced — replaces §13/§20's heuristic guess
with measured slopes. Lemma 3 still open but the framework is now
aligned with empirical reality.
