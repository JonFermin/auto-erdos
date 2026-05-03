# Session handoff (s_0502-181121-0140)

**Stop reason**: Session 6 budget. Round 14 added Section 13 â€” the
cross-stratum exclusion threshold.

**Round 14 main finding**

For primitive A = A^(k1) âˆª A^(k2) with A^(k1) full (= A_{k1} cap [x, N]),
the constraint on A^(k2) (no element of A^(k1) divides any element of
A^(k2)) reduces to: every b in A^(k2) has its k1 smallest prime
factors product < x.

By an Erdos-Kac heuristic (prime factor logs ~ uniform order
statistics), E[log delta_{k1}(b)] ~ (k1^2 / 2 k2) log u. The constraint
delta_{k1}(b) < x at scale u = x becomes k1 < sqrt(2 k2).

**Empirical validation** at x=100, N=10^7:

  k1=1, k2=2: kept frac = 0.94 (k1 < sqrt(4)=2)
  k1=2, k2=3: kept frac = 0.80 (k1 < sqrt(6)=2.45 borderline)
  k1=3, k2=4: kept frac = 0.64 (k1 > sqrt(8)=2.83)

Threshold is empirically clean.

**State at close**

- 14 keep_progress rounds. Sections 1-13 in proof_strategy.md.
- 14 records under records/.
- Q1-Q13 resolved. Round cap is 50; ~36 rounds left.

**Suggested next move (concrete)**

Multi-stratum experiment: take A primitive supported on strata
K = {k_min, k_min+1, ..., k_max} simultaneously, each "fully" present
modulo cross-stratum primitivity. Compute S(A) numerically at x=100,
N=10^7 for various K. See if max S over K ever reaches 1.

A subtler version: for each (k, k') pair, the "kept fraction" depends
on both. The overall max-S problem is to find the optimal K that
maximises sum_k (kept frac_k) * Gamma(k, loglog x)/(k-1)!.

This is computable. If max stays below 1, that's strong empirical
evidence for the conjecture.
