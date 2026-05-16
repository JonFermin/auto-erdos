---
id: stratification
status: open
depends_on: [Ak_primitive]
discharged_by_round: null
introduced_at_round: 4
---

## Lemma stratification: Omega-Stratification of a Primitive Set

**Statement**: Let $A \subseteq [x, \infty)$ be a primitive set. For each
$k \geq 1$, let $A_k = \{a \in A : \Omega(a) = k\}$ (elements of $A$ with
exactly $k$ prime factors). Then $A = \bigsqcup_{k=1}^\infty A_k$ (disjoint
union), and:

1. Each $A_k \neq \emptyset$ for at most finitely many $k$ when $A$ is finite.
2. For infinite $A$: the partition $\{A_k\}$ exhausts $A$.
3. (Key difficulty) The cross-stratum interaction is non-trivial: primitivity
   of $A$ imposes constraints on which elements across different strata can
   coexist, but these constraints do NOT force $A_k \subseteq A_k^{(\text{full})}$
   for any clean subset.

**Proof of parts 1–2**: Any $a \in A$ has $\Omega(a) = k$ for exactly one
$k$, so the union is disjoint and exhaustive. $\square$

**Part 3 — The cross-stratum difficulty**: A primitive $A$ may contain
elements from multiple strata. For example, $A$ could contain both a prime $p$
(in $A_1$) and a squarefree semiprime $q \cdot r$ (in $A_2$) with $p \neq q, r$.
The primitivity constraint is: for $a \in A_j$ and $b \in A_k$ with $j \neq k$,
we need $a \nmid b$ AND $b \nmid a$. This is possible (e.g., $p \nmid qr$ when
$p \notin \{q, r\}$), so cross-stratum mixing IS allowed.

**Current obstacle**: bounding $\sum_{k=1}^\infty \sum_{a \in A_k} 1/(a \log a)$
requires either:
(a) Showing $\sum_{a \in A_k} 1/(a \log a) \leq f(k)$ for each stratum
    separately, where $\sum_k f(k) \leq 1 + o(1)$ — but this requires
    splitting the "budget" across strata, and the strata are not independent.
(b) An entirely different approach that does not stratify by $\Omega$.

Neither approach is currently settled. This lemma remains open as a
decomposition tool that may or may not lead to the conjecture.
