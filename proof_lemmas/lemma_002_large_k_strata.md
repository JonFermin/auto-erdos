---
id: large_k_strata
status: open
depends_on: [stratification]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 2 — Large-$k$ strata contribute negligibly

**Statement.** For any primitive set $A \subset [x, \infty)$ and any $K \geq 1$,

$$\sum_{k > K} \sum_{a \in A_k} \frac{1}{a \ln a}
  \leq \sum_{k > K} \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \ln n}
  =: R(K, x).$$

Moreover, $R(K, x) \to 0$ as either $K \to \infty$ (fixed $x$) or
$x \to \infty$ (fixed $K$).

**Status: open.** The inequality is trivial (each stratum's contribution is
bounded by the full stratum's sum, which is $\geq 0$).  The limit statements
require controlling the tail $\sum_{k > K} T_k(x)$ where
$T_k(x) = \sum_{n \geq x, \Omega(n)=k} 1/(n \ln n)$.

**Approach.** By F3 (cited from the ledger), $\sum_{n: \Omega(n)=k} 1/(n \ln n)
= 1 - (c+o(1))k^2/2^k$ for $k \to \infty$.  This gives the full-stratum
sum for each $k$, but $T_k(x)$ is the TAIL starting from $x$, not the
full sum.  We need:
$$T_k(x) = \sum_{n \geq x, \Omega(n)=k} \frac{1}{n \ln n}
  \leq \sum_{n: \Omega(n)=k} \frac{1}{n \ln n} \leq 1 \quad \forall k \geq 1$$
(using F3 and the sign disambiguation: the full stratum sum $< 1$ for large $k$,
and is $< e^\gamma \pi/4 \approx 1.399$ for all $k$ by F1).

For the sum of tail sums over $k > K$: $\sum_{k>K} T_k(x) \leq \sum_{k>K} S_k$
where $S_k = \sum_{n: \Omega(n)=k} 1/(n \ln n)$.  By F3, $S_k < 1$ for large $k$.
But $\sum_{k>K} 1 = \infty$, so this bound is too crude.

**The gap (current obstacle).** We need a quantitative bound on $S_k$ as a
function of $k$: specifically, $S_k \leq 1 - \delta_k$ where $\sum_{k>K} \delta_k \to \infty$
fast enough to make $\sum_{k>K} S_k$ finite.  F3 gives $S_k = 1 - (c+o(1))k^2/2^k$,
so $\delta_k \approx ck^2/2^k$.  Then:
$$\sum_{k>K} S_k \leq \sum_{k>K} \left(1 - ck^2/2^k + O(k^{-1/2+o(1)})\right)$$
which still diverges because of the "$1$" in each term.

This reveals that the **naive stratum-by-stratum bound** (adding $S_k$ over all
$k$) is USELESS — the sum diverges.  The primitive constraint is therefore
ESSENTIAL: a primitive set cannot simultaneously have elements in all strata.

**Conclusion.** The large-$k$ strata by themselves are individually bounded
($S_k < 1$), but the Lemma 2 bound "$\sum_{k>K}$ stratum-sum $\leq \sum_{k>K} S_k$"
is not summable.  A different approach is needed — see Lemma 3.
