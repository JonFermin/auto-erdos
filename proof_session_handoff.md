# Session handoff (s_0502-174202-ad99)

**Stop reason**: Session 5 budget. Round 13 derived the exact
incomplete-Gamma representation for truncated stratum sums.

**Round 13 main finding**

S(A_k cap [x, infty)) ~ Gamma(k, loglog x) / (k-1)!  =  P(Poisson(loglog x) < k)

This is exact (modulo standard Hardy-Ramanujan / Sathe-Selberg
uniformity), and validated numerically against direct sums for
k in main range. The probabilistic interpretation aligns with
Erdos-Kac.

Consequence: the single-stratum supremum
max_k S(A_k cap [x, infty))  ~  max_k P(Poisson(loglog x) < k)
tends to 1 from below as x -> infty, matching the conjecture's
ceiling. So Lemma 3's single-stratum case is now rigorous via Section
11 + 12 â€” the truncated stratum sup IS the conjecture's bound.

The cross-stratum case is still open; Sections 11.3-11.4 sketched but
didn't quantify the primitivity deficit.

**State at close**

- 13 keep_progress rounds. Sections 1-12 in proof_strategy.md.
- 13 records under records/.
- Q1-Q12 resolved.

**Suggested next move**

Quantify the cross-stratum deficit. Take A primitive with
contributions in two strata k_1, k_2 (k_1 < k_2). By the analysis in
11.4: the b in A^{(k_2)} is restricted to b < x p_min(b). Estimate
S(A^{(k_2)}) under this restriction. Compare to
S(A^{(k_2)} unrestricted) = Gamma(k_2, loglog x)/(k_2-1)!.

If the restriction reduces S(A^{(k_2)}) by a factor f(k_1) such that
S(A^{(k_1)}) + f(k_1) * S(A^{(k_2)}) <= max(S(A^{(k_1)}), S(A^{(k_2)})) + o(1),
the cross-stratum part of Lemma 3 follows.

This is a doable computation; primitive obstacle is Mertens-type
estimates on smooth-numbers density.
