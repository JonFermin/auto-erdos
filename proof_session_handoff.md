# Session handoff (session s_0504-053221-985a)

**Stop reason**: One round logged. Returning to /loop driver.

**Round 40 contribution (§29.5b–c, CORRECTION)**

Significant numerical correction to the §26.3 estimate of
sigma(x) := sup S(A) - S(M(x; infty)).

Key observation: A_2 cap [x, infty) — full semiprimes from x on —
is itself primitive (any two distinct semiprimes are incomparable
under divisibility). By §19's closed form:
  S(A_2 cap [x, infty)) ~ (1 + loglog x) / log x.

Comparing to §28's exact S(M):
  x=100:  S(A_2) = 0.549 vs S(M) = 0.386, gap = +0.163
  x=300:  +0.140
  x=1000: +0.138
  x=3000: +0.134

So sigma(x) >= 0.13 UNIFORMLY across tested x — substantially
larger than the §26.3 finite-N estimate of ~0.06.

Asymptotic ratio: S(A_2)/S(M) -> e^gamma ~ 1.78 as x -> infty.
So S(A_2) ~ 1.78 * S(M) asymptotically; sigma(x) ~ 0.78 * S(M).

The conjecture's sup S <= 1 + o(1) is still CONSISTENT (since
A_2 also decays as loglog x / log x), but with smaller margin
than I'd previously estimated.

This is a meaningful correction to the loop's prior assessment.
The §26.3 finite-N analysis truncated multi-stratum tails
inappropriately.

**Status**

40 rounds, 30 sessions, 40 keeps, 0 disproofs.

The proof attempt's empirical understanding has been refined:
the gap between known constructions and S(M) is bigger than
finite-N analyses suggested. Still consistent with conjecture.

**Files modified this session**

- proof_strategy.md — added §29.5b–c (~85 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 40 update.
- proof_open_questions.jsonl — Q39 claimed and resolved.
- proof_journal.jsonl — round 40 entry.
- 1 new record in records/.

**qid in flight**: none.
