---
id: cross_stratum_sum
status: open
depends_on: [intra_stratum_bound]
discharged_by_round: null
introduced_at_round: 4
---

# Lemma: Cross-Stratum Sum Bound (OPEN)

**Goal.** For any primitive set $A \subseteq [x, \infty)$,

$$f(A) = \sum_{k \geq 1} \sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a} < 1 + o(1) \text{ as } x \to \infty.$$

**Why Lemma `intra_stratum_bound` is insufficient.**

Each stratum satisfies $f(A_{[k]}) \leq 1 - (c+o(1)) k^2/2^k$ by Lemma `intra_stratum_bound`.
However, summing this over all $k \geq 1$ gives $\sum_k (1 - ck^2/2^k)$, which diverges
(the $\sum_k 1$ part is infinite). So stratum-by-stratum bounds do not yield a finite total.

**The primitivity constraint across strata.**

For a primitive set $A$: if $a \in A$ with $\Omega(a) = k$, no multiple $da$ ($d \geq 2$)
belongs to $A$. Such multiples have $\Omega(da) \geq k+1$, so stratum $k$ elements exclude
certain elements from strata $k+1, k+2, \ldots$

This cross-stratum exclusion prevents $A$ from having large contributions from ALL strata
simultaneously, but quantifying this precisely is the key difficulty.

**Relation to known results.**

The Erdős–Zhang theorem (F1, given fact) establishes $f(A) < e^\gamma \pi/4 + o(1)$
for any primitive $A \subseteq \mathbb{N}$. This is a weaker bound (constant $\approx 1.399$)
that does not use the full strength of the cross-stratum structure.

**Current state:** Open. The cross-stratum interaction is the central difficulty; no proof
of the tight bound $1 + o(1)$ is known.
