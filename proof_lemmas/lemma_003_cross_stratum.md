---
id: cross_stratum_bound
status: open
depends_on: [stratum_self_primitive, per_stratum_bound]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 3: Cross-stratum bound (the hard lemma)

**Statement** (conjectured): Let $A \subseteq [x, \infty)$ be a primitive set. Then
$$
S(A) = \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad \text{as } x \to \infty,
$$
uniformly over all primitive $A \subseteq [x, \infty)$.

This is the conjecture itself restated. The challenge is to use the cross-stratum
primitivity constraint to prevent $S(A)$ from exceeding 1.

## Difficulty: per-stratum bounds don't directly sum to $< 1$

If we naively sum Lemma 2 over all strata:
$$
S(A) = \sum_{k \geq 1} \sum_{a \in A_k^A} \frac{1}{a\log a} \leq \sum_{k \geq 1} \sigma_k
$$
where $\sigma_k \approx 1 - ck^2/2^k$ for large $k$. But $\sum_{k\geq 1} \sigma_k = \infty$
(since $\sigma_k \to 1$). So per-stratum bounds cannot be summed naively — they
diverge. We must use the cross-stratum primitivity constraint.

## What the constraint says

For primitive $A$, if $a \in A_j^A$ and $b \in A_k^A$ with $j < k$, then $a \nmid b$.
Equivalently:
$$
A_k^A \;\subseteq\; \{n \geq x : \Omega(n)=k\} \;\setminus\; \bigcup_{a \in A_j^A} \{n : a \mid n, \Omega(n)=k\}.
$$
Each element $a \in A_j^A$ "excludes" all its $A_k$-multiples from $A_k^A$.

## A key observation

For $j = 1$ (prime elements of $A$): if prime $p \in A$, then ALL multiples of $p$
in any higher stratum are excluded from $A$. In particular, $A_k^A \subseteq \{n \geq x, \Omega(n)=k, p \nmid n \text{ for all primes } p \in A_1^A\}$.

This is a sieve condition: elements of $A$ in higher strata avoid the prime
factors that appear in stratum 1.

## Partial result: finite-stratum version

If $A$ only uses elements from strata $k = 1$ and $k = 2$:

$$
S(A) \leq \sum_{p \in A_1^A} \frac{1}{p\log p} + \sum_{\substack{a \in A_2^A \\ a \nmid \text{ by any } p \in A_1^A}} \frac{1}{a\log a}.
$$

The sieve exclusion removes all semiprimes of the form $p \cdot q$ where $p \in A_1^A$
(a prime in $A$). This removes many large-contribution elements from $A_2$.

The key difficulty: quantifying this trade-off precisely enough to show $S(A) < 1$.

## Approaches tried

1. **Direct sum over two strata** (k=1 and k=2): The primitive constraint means
   we cannot simultaneously have a prime $p$ and a semiprime $pq$ in $A$. So
   for each prime $p \in A_1^A$, we lose semiprimes $\{pq : q \text{ prime}\}$
   from $A_2^A$. The sum of lost semiprimes is $\approx \sum_{q} 1/(pq\log(pq))$
   which is substantial for small $p$ (like $p=2$: we lose $\{4, 6, 10, 14, ...\}$).

2. **Optimal mixing argument**: Given the trade-off, what is the maximum of $S(A)$
   over all primitive $A \subseteq [x, \infty)$ for fixed $x$? For small $x$,
   the optimal $A$ includes low-stratum elements. As $x$ grows, the optimal
   strategy shifts to higher strata.

## Current obstacle

The precise form of the cross-stratum trade-off is unclear. The conjecture's
bound of 1 would follow if we could show: for any primitive $A \subseteq [x, \infty)$,
the sum of "gains" (elements included in $A$) is offset by "losses" (excluded
higher-stratum elements) in a way that keeps the total below 1.

This requires a multiplicative structure argument or a Mertens-type estimate
that relates the prime and semiprime contributions under the sieve constraint.

**Status: open**. This is the crux of the conjecture and has no known proof.
