---
id: strat_001
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma strat_001: Per-stratum bound for primitive subsets

## Statement

Let $A \subset [x, \infty)$ be a primitive set and let $k \geq 1$ be
fixed. Write $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ and
$A^{(k)} = A \cap A_k$. Then
$$\sum_{a \in A^{(k)}} \frac{1}{a \log a} \leq \sum_{a \in A_k, a \geq x} \frac{1}{a \log a}.$$

In words: the weight of the stratum-$k$ part of $A$ is at most the weight
of the ENTIRE stratum $A_k$ restricted to $[x, \infty)$.

## Proof sketch

$A^{(k)} \subseteq A_k \cap [x, \infty)$, so the inequality is trivially
$\sum_{a \in A^{(k)}} f(a) \leq \sum_{a \in A_k, a \geq x} f(a)$
since all terms $f(a) = 1/(a \log a) > 0$. **This lemma holds as
an inclusion.** Primitivity within $A^{(k)}$ (elements of $A$ in the
same stratum are pairwise non-divisible) gives no additional savings
over the crude bound above.

## Current obstacle

The per-stratum bound is easy and gives
$$\sum_{a \in A} \frac{1}{a \log a}
= \sum_{k \geq 1} \sum_{a \in A^{(k)}} \frac{1}{a \log a}
\leq \sum_{k \geq 1} \sum_{a \in A_k, a \geq x} \frac{1}{a \log a}$$
but the right side sums over ALL of $\cup_k A_k \cap [x, \infty)$,
which is ALL integers $\geq x$. The sum $\sum_{n \geq x} 1/(n \log n)$
diverges (the sum $\sum_{n \geq 2} 1/(n \log n)$ diverges by comparison
with $\int 1/(t \log t) dt = \log \log t$). So this per-stratum bound
is USELESS without using cross-stratum primitivity.

## Next step

Lemma strat_003 must provide the cross-stratum constraint that makes the
bound non-trivial. The key observation: if $a \in A^{(1)}$ (a prime $p$)
and $b \in A^{(k)}$ for $k \geq 2$, primitivity requires $p \nmid b$
(else $p | b$ and both $p, b \in A$). This means each prime in $A$
"blocks" all its multiples from ALL strata. The question is whether this
exclusion rule reduces the total weight enough.
