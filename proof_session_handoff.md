# Session handoff (s_0502-184222-1387)

**Stop reason**: Session 7. Round 15 added Section 14 â€” multi-stratum
empirical max-S.

**Round 15 main finding**

At x=100, N=10^6:
- best single-stratum K={k}: K={2}, S=0.288
- best pair: K={2,4}, S=0.337
- best multi-stratum: K={2,3,4,5}, S=0.366

So multi-stratum gain over single is 27%. Including k=1 (primes) hurts
because each prime excludes a large downward cone of higher-stratum
multiples.

Empirical sup_A S(A) >= 0.366 at x=100, N=10^6. Conjecture ceiling
is 1+o(1), so safe by 3x at this scale.

**State at close**

- 15 keep_progress rounds. Sections 1-14 in proof_strategy.md.
- 15 records under records/.
- Q1-Q14 resolved. Round cap 50; ~35 left.

**Suggested next move**

Two viable directions:

(a) Push N larger (currently 10^6 sieve cap; with more memory could
    do 10^8). See if multi-stratum sup grows. Conjectured: sup grows
    slowly toward 1 from below.

(b) Try simulated annealing or ILP to tighten the lower bound from
    0.366 above. If SA finds something significantly larger (e.g.,
    > 0.5), that would suggest greedy is far from optimal.

If neither pans out within a session, document the empirical envelope
and consider this branch's loop has plateaued â€” call exit-4 by
hitting the round cap or a manual session_end "loop plateau".

Status: the loop has produced rich material on Lemma 3 (Sections
7-14) but cannot close the open conjecture without a new analytical
ingredient (CST conjecture / stratum-aware Behrend).
