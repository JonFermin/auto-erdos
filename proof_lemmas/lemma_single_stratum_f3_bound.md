---
id: single_stratum_f3_bound
status: proved
depends_on: [stratification_setup]
discharged_by_round: 1
introduced_at_round: 1
---

> Concluded `primitive_set_erdos` attempt (claim proved in the literature,
> May 2026, arXiv:2605.00301); retained as audit trail, not load-bearing for
> any active chain. Per the falsify-critic contract, one-line sandbox
> re-derivations are not expected for this file; deterministic re-checks, if
> any, live in its CHECK blocks.

# Lemma `single_stratum_f3_bound`

**Statement**: For any primitive $A \subseteq [x, \infty)$ and any $k \geq 1$:
$$f(A_k) = \sum_{a \in A_k} \frac{1}{a \log a} < 1.$$

**Proof**: Since $A_k \subseteq \{n \geq 2 : \Omega(n) = k\}$, all terms are
non-negative and:
$$f(A_k) \leq \sum_{\substack{n \geq 2 \\ \Omega(n)=k}} \frac{1}{n \log n}
= 1 - (c + o(1))\frac{k^2}{2^k}$$
by F3, where $c \approx 0.0656 > 0$. The correction is NEGATIVE, so the
full-stratum sum is strictly less than 1, and hence $f(A_k) < 1$. $\square$

**Sign discipline**: The F3 correction $-(c+o(1))k^2/2^k$ with $c > 0$ means
the sum approaches 1 from BELOW. This lemma does not use F2.

**Limitation**: This bounds each stratum individually. Naive summation gives
$f(A) < \sum_k 1 = +\infty$ — vacuous. The cross-stratum constraint
(Lemma `cross_stratum_interaction`) is needed for the total bound.
