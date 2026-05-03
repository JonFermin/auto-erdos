# Session handoff (session s_0503-173716-486b)

**Stop reason**: One round logged. Returning to /loop driver.

**This session's contribution (Round 20, sect 19)**

Derived a closed form for the tail-stratum sum:
  a_k(x; inf) ~ (1/log x) * sum_{j=0..k-1} (loglog x)^j / j!
              = (1/log x) * P(Poisson(loglog x) <= k-1)

Method: partial summation from sect 11.1's
Sigma_{A_k}(t) ~ (loglog t)^k / k!, with substitution
v = loglog t reducing the integral to upper-incomplete gamma.

NUMERICAL VALIDATION at x=10^7: k=1 gives
S_obs + a_pred = 1.5746 + 0.0620 = 1.6366, exactly matching the
literature value of Erdos's prime-tail constant
sum_p 1/(p log p) = 1.6366... — strong validation.

For k=3..10, S_obs + a_pred is within 1% of 1, confirming
S(A_k) -> 1 as k grows. (k=2 is borderline — L=2.78 is just past
k=2 so asymptotic only barely applies.)

GOAL RESTATEMENT (sect 19.5): Lemma 3 reduces to
  prove sum_{k=L..L^2/2} rho_k(x) = o(log x) uniformly as x->inf.
This is the single missing analytic step.

**For next session: tackle the goal directly**

Try a saddle-point / Erdos-Kac argument for rho_k(x) on
L <= k <= L^2/2. The setup:
- L = loglog x.
- For k = k_2 in [L, L^2/2], rho_{k_2}(x) is the fraction of
  b in A_{k_2} cap [x, inf) with smallest k_1-divisor < x for
  every k_1 < k_2.
- The dominant exclusion comes from k_1 = L (the dominant
  single-stratum). So a tractable upper bound:
  rho_{k_2}(x) <= P(b in A_{k_2}: smallest L-divisor of b < x)
- For random b ~ A_{k_2} of size u, this is the §13 quantity.
  Erdos-Kac gives the smallest L-divisor at scale
  u^(L^2 / (2 k_2)), so the constraint
  smallest-L-div < x becomes u < x^(2 k_2/L^2).
- For u ~ x (the floor), this is restrictive when k_2 < L^2/2,
  and slack when k_2 >= L^2/2 — exactly the gap that needs to
  be bounded.

A round that quantifies rho_{k_2}(x) <= exp(-c (k_2 - L)^2 / L)
or similar Gaussian decay would close it. The §11.3 gaussian-
saddle-point factor is a model.

**Files modified this session**

- proof_strategy.md — added Section 19 (~150 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 20 update.
- proof_open_questions.jsonl — Q19 claimed and resolved.
- proof_journal.jsonl — round 20 entry.
- 1 new record in records/.

**qid in flight**: none. Next is Q20 (the saddle-point on rho_k).

**Status**

20 rounds across 11 sessions. 20 keeps. 0 disproofs. The
§11+§12+§13+§18+§19 chain is now articulated. Lemma 3 has a
single, concrete missing step. This is the cleanest state of
the proof attempt to date.
