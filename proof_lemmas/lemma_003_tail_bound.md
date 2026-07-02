---
id: tail_bound
status: open
depends_on: [single_stratum_bound]
discharged_by_round: null
introduced_at_round: 4
---

# Lemma 3 (tail_bound): High-omega strata contribute negligibly in total

## Statement

For any primitive $A \subseteq [x, \infty)$ and any $K \geq 1$,
$$\sum_{k > K} \sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{k > K} \left(1 - (c+o(1))\frac{k^2}{2^k}\right) \leq \sum_{k > K} 1.$$

Hmm — this is not immediately useful because $\sum_{k > K} 1 = \infty$. A more useful version:

## Useful version

By Lemma `single_stratum_bound`, the $k$-th stratum contributes at most $1 - c k^2/2^k + o(k^2/2^k)$. For $k > K$, the sum $\sum_{k > K} (1 - ck^2/2^k)$ diverges.

However, for any element $a \geq x$ with $\Omega(a) = k$, the smallest such element is $2^k$. So if $x > 2^K$, then $A \cap A_k = \emptyset$ for $k > \log_2 x$: there are no elements of $A_k$ below $2^k$, and if $x > 2^k$ then no element of $A_k$ lies in $[x, \infty)$... wait, this is backwards.

**Corrected argument.** If $a \in A \cap A_k$ and $a \geq x$, then $a \geq x$ and $\Omega(a) = k$. The smallest element of $A_k$ is $2^k$, so $k \leq \log_2(a) \leq \log_2(\max A)$. But this only gives an UPPER bound on $k$; we want to show high-$k$ strata contribute little.

## Status: partially open

For large $k$, the contribution $1 - ck^2/2^k$ approaches 1, so high-$k$ strata can contribute CLOSE to 1 each — this does NOT tail off. The issue is that a primitive set $A$ can have elements from many high-$k$ strata simultaneously.

The key saving: for large $k$, elements of $A_k$ that lie in $[x, \infty)$ are rare (most small elements of $A_k$ are below $x$). For a fixed $x$, the set $\{n \geq x : \Omega(n) = k\}$ gets smaller relative to all of $A_k$ as $k$ grows (since the smallest element of $A_k$ is $2^k$; for $k \leq \log_2 x$, ALL of $A_k$ is in $[2^k, \infty)$ but may be partly below $x$).

**Conclusion**: This lemma as stated is not proved. The tail bound requires a different argument — possibly using the density of high-$\Omega$ numbers near $x$ or an asymptotic sieve.

## Revised status: open

The tail bound for $k \gg \log x$ might follow from noting that $A_k \cap [x, \infty)$ has density $\ll x (\log\log x)^{k-1}/((k-1)! \log x)$ (by the Sathe-Selberg formula), but converting this to a sum bound requires more work.

**Status: open. Current obstacle: turning a density bound on $A_k \cap [x,\infty)$ into a sum bound $\sum_{a \in A \cap A_k} 1/(a\log a)$.**
