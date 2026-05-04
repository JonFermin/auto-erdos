# Session handoff (session s_0503-193412-a47e)

**Stop reason**: One round logged. Returning to /loop driver.

**This session's contribution (Round 24, Section 23)**

Defined and analyzed the max primitive subset M(x, N) :=
{n in [x, N] : n has no proper divisor in [x, n-1]}. Proved M is
primitive (one-line argument).

Computed S(M(x, 10^6)) for x in {10^2, ..., 10^5}:
  S(M) * log x ≈ 1.44 - 1.49 over x in [100, 3000]
  S(M) decays as ~1.45 / log x (consistent with prime-tail Mertens).

M is NOT the actual sup of S over primitive A in [x, N] — the §18
two-stratum construction beats it by up to ~10% at x=100. But both
quantities decay at the same rate.

The empirical content of the conjecture is now extremely clean:
  sup S(A) for primitive A in [x, infty) appears to be ~1.5/log x
  (much stronger than the conjecture's 1 + o(1)).

But this is still numerical, not a proof. The Erdős-Zhang
unconditional bound e^gamma pi/4 = 1.399 remains the best rigorous
upper bound; the closing argument from 1.399 down to 1 + o(1) (or
the empirically-suggested 1.5/log x) is still missing.

**For next session**

Two productive moves:

(a) **Prove S(M) <= sup S(A) is an UPPER BOUND**, not just an
    example. This requires showing every primitive A is "dominated"
    by M in some sense. Probably FALSE in general (two-stratum beats
    by ~10%), but maybe a relaxation works: sup S(A) <= S(M) + small.

(b) **Try to derive the c_M = 1.45 constant analytically**. M's
    sum is dominated by sum_{p in [x, sqrt N]} 1/(p log p) for large
    N. By Mertens/partial summation, this should give c_M as some
    explicit number-theoretic constant. Connecting c_M to the
    Erdős/Zhang constant 1.399 would clarify the gap.

Recommendation: (b) first. Even an asymptotic identification of
c_M would be progress.

**Files modified this session**

- proof_strategy.md — added Section 23 (~120 lines).
- proof_lemmas/lemma_003_cross_stratum.md — Round 24 update.
- proof_open_questions.jsonl — Q23 claimed and resolved.
- proof_journal.jsonl — round 24 entry.
- 1 new record in records/.

**qid in flight**: none. Next is Q24.

**Status**

24 rounds across 15 sessions. 24 keeps. 0 disproofs. The proof
attempt has produced strong numerical and structural content.
The conjecture is empirically supported (with stronger 1.5/log x
behavior). The rigorous closing argument remains open.
