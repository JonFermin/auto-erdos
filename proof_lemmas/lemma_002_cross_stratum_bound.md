---
id: cross_stratum_bound
status: open
depends_on: [single_stratum_bound]
discharged_by_round: null
introduced_at_round: 4
---

# Lemma 2 (cross_stratum_bound): Primitivity constrains cross-stratum accumulation

## Statement (target)

For any primitive $A \subseteq [x, \infty)$ and any $K \geq 1$,
$$\sum_{k=1}^{K} \sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq 1 + o(1) \text{ as } x \to \infty.$$

This is essentially the full conjecture for elements of bounded omega-complexity; combining it with the tail bound for $k > K$ (see Lemma `tail_bound`) would finish the proof.

## Why this is hard

By Lemma `single_stratum_bound`, each stratum contributes at most $1 - c k^2/2^k < 1$. Naively summing $K$ such bounds gives $K < K \cdot 1 = K \to \infty$, which is useless. The key question is:

> *Can a single primitive set $A$ capture a significant fraction of multiple strata simultaneously?*

The answer is constrained by **primitivity**: if $a \in A \cap A_j$ (j prime factors) and $b \in A \cap A_k$ (k prime factors, $j < k$), then $a \nmid b$. This means $b$ cannot be a multiple of $a$.

**Why this constrains the total.** If a prime $p \in A \cap A_1$, then ALL multiples of $p$ (which form a substantial fraction of each $A_k$ for $k \geq 2$) are excluded from $A$. More precisely: for any $n \in A_k$ with $p | n$, we have $p \mid n$ so $n \notin A$ if $p \in A$. This removes $\sim 1/p$ of the elements of $A_k$ (heuristically).

Conversely, if we put many composite numbers in $A \cap A_k$ (not divisible by small primes), those composites "prevent" their own prime factors from appearing in $A \cap A_1$.

## Known result and gap

By **F1** (Erdős-Zhang), $\sum_{a \in A} 1/(a \log a) < e^\gamma \pi/4 + o(1) \approx 1.399 + o(1)$ for any primitive $A \subseteq [x, \infty)$. This already cross-stratifies: F1 gives a global bound summing all strata at once, beating the trivial per-stratum estimate by a factor of $\infty$.

However, F1 achieves a bound of $\approx 1.399$, not $1 + o(1)$. Improving the constant from $1.399$ to $1$ (as $x \to \infty$) is the open heart of the conjecture.

## Current obstacle

The primitivity constraint creates a "trade-off" between strata: gaining weight in stratum $k$ costs weight in other strata. Making this trade-off quantitative is the central open problem. Current approaches (Zhang 1993) handle the trade-off multiplicatively (via Euler products) but do not tighten the constant below $e^\gamma \pi/4$.

## The excluded-sum reformulation (Section 9)

Define the **excluded sum** for the two-stratum case $A \subseteq (A_j \cup A_k) \cap [x,\infty)$:
$$E := \sum_{\substack{n \in A_k \cap [x,\infty) \\ \exists a \in A \cap A_j: a \mid n}} \frac{1}{n \log n} \geq 0.$$

By F3, $S_k \leq (1 - c\phi(k)) - E + o(1)$, so $S_j + S_k \leq S_j + (1-c\phi(k)) - E + o(1)$.
The target $S_j + S_k < 1 + o(1)$ requires $E > S_j - c\phi(k) + o(1)$, i.e.,
the excluded sum must offset the $j$-stratum contribution.

**The precise missing fact (F4 refined)**: For any such $A$ and $\kappa := E / S_j$,
we need $\kappa \geq \kappa_0(j,k)$ for some $\kappa_0$ large enough to give $S < 1+o(1)$.
The value of $\kappa_0$ depends on $j,k$ and is an open analytic number theory problem.

**Status: open. The lemma is equivalent to establishing F4 (the exclusion coefficient lower bound).**
