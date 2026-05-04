# Session handoff (session s_0504-061922-d853)

**Stop reason**: One round logged. Returning to /loop driver.

**Round 41 contribution (§29.5e, MAJOR CORRECTION)**

Identified an EXPLICIT WITNESS that the conjecture's bound is
TIGHT, not loose:

  Set k_x := ceil(log_2 x). Smallest element of A_{k_x} is 2^{k_x}
  >= x. So A_{k_x} subset [x, infty), and A_{k_x} is primitive.
  By Sathe-Selberg (§11.5), S(A_{k_x}) = 1 - O((log x)^2 / x) -> 1.

So sup_{A primitive in [x, infty)} S(A) -> 1 as x -> infty —
EXACTLY matching the conjecture's claimed bound. The conjecture's
1 + o(1) is TIGHT, attained asymptotically.

This is a major correction to my earlier picture:
- §29.5a's "sigma(x) bounded" intuition: WRONG. sigma(x) -> 1.
- "M is approximately the sup": WRONG. M is far below sup.
- The sup is attained by HIGH-stratum A_k (k = log_2 x), not low.

The §17 sieve data did not detect this because A_{k} for large k
has its mass at u_k = e^{e^k}, way beyond any feasible sieve. But
the asymptotic S(A_k) -> 1 from §11/§12 makes it rigorous.

**Status**

41 rounds, 31 sessions, 41 keeps, 0 disproofs.

The proof attempt now has a SHARPER picture:
- sup_A S(A) -> 1 (proven via A_{k_x} witness, §29.5e).
- conjecture's <= 1 + o(1) is TIGHT.
- The remaining open piece is the matching upper bound: prove
  sup S <= 1 + o(1) (no primitive set exceeds 1 substantially).
- §25 / Lemma B / §28 etc. give bounds on S(M), but not on the
  sup over all primitive sets.

The picture is now: "Erdős–Zhang gives sup <= 1.399; conjecture
asks for sup <= 1; by §29.5e sup -> 1 from below; the gap of
0.399 is what cross-stratum primitivity should close." Same as
the literature framing.

**Files modified this session**

- proof_strategy.md — added §29.5e–g (~80 lines, with corrections).
- proof_lemmas/lemma_003_cross_stratum.md — Round 41 update.
- proof_open_questions.jsonl — Q40 claimed and resolved.
- proof_journal.jsonl — round 41 entry.
- 1 new record in records/.

**qid in flight**: none.
