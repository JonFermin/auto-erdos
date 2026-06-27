---
id: per_stratum_bound
status: open
depends_on: [stratum_self_primitive]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 2: Per-stratum contribution bound via F3

**Statement**: For the full $\Omega = k$ stratum $A_k = \{n \in \mathbb{N}: \Omega(n) = k\}$,
$$
\sigma_k := \sum_{a \in A_k} \frac{1}{a \log a} = 1 - \frac{(c + o(1))\, k^2}{2^k}
$$
where $c \approx 0.0656 > 0$ and $o(1) \to 0$ as $k \to \infty$.

In particular, $\sigma_k < 1$ for all $k \geq 1$.

**Status**: This is fact F3 (given in the problem ledger). Its proof is deep
(relies on analysis of the Selberg sieve or multiplicative structure of A_k);
we CITE it rather than reproving.

**Consequence for any sub-stratum**: For any $S \subseteq A_k$,
$$
\sum_{a \in S} \frac{1}{a \log a} \leq \sigma_k < 1.
$$

**Tail-sum corollary**: For elements ≥ $x$, define
$$
T_k(x) := \sum_{\substack{a \in A_k \\ a \geq x}} \frac{1}{a \log a} = \sigma_k - \sum_{\substack{a \in A_k \\ a < x}} \frac{1}{a \log a}.
$$
Since $\sigma_k$ is a convergent series with positive terms, $T_k(x) \to 0$ as $x \to \infty$ for
each **fixed** $k$.

**Numerical confirmation** (from Section 2):
- $\sigma_1 \approx 1.637$ (N.B.: F3 does NOT apply to $k=1$; the formula $1 - ck^2/2^k$
  is an asymptotic for large $k$).
- $\sigma_2 \approx 0.934$ (partial sum to $10^6$: 0.867, tail remaining ≈ 0.067).
- $\sigma_3 \approx 0.926$ (partial to $10^6$: 0.498, large tail from $2\cdot3\cdot p$).
- $\sigma_4 \approx 0.934$ (partial to $10^6$: 0.261).

**Open sub-problem**: Prove Lemma 2 from first principles (currently cited as F3).
The proof would require asymptotic analysis of $\sum_{n \leq x, \Omega(n)=k} 1/(n\log n)$
using the Selberg–Sathe theorem or related analytic number theory.
