---
id: stratification_setup
status: proved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

> Concluded `primitive_set_erdos` attempt (claim proved in the literature,
> May 2026, arXiv:2605.00301); retained as audit trail, not load-bearing for
> any active chain. Per the falsify-critic contract, one-line sandbox
> re-derivations are not expected for this file; deterministic re-checks, if
> any, live in its CHECK blocks.

# Lemma `stratification_setup`

**Statement**: Let $A \subseteq [x, \infty)$ be a primitive set and let
$A_k = \{a \in A : \Omega(a) = k\}$. Then:

1. $A = \bigsqcup_{k \geq 1} A_k$ (disjoint partition).
2. Within each $A_k$, no element properly divides another.
3. For $j < k$, no element of $A_j$ divides any element of $A_k$.

**Proof**:

(1) Immediate: $\Omega$ assigns a unique value $\geq 1$ to each $n \geq 2$.

(2) If $a, b \in A_k$ with $a | b$ and $a \neq b$, write $b = am$ for $m \geq 2$.
Then $\Omega(b) = \Omega(a) + \Omega(m) \geq k + 1 > k$, contradicting $b \in A_k$.

(3) If $a \in A_j$, $b \in A_k$, $j \neq k$, so $a \neq b$. If $a | b$, that
contradicts the primitivity of $A$. $\square$

The total sum decomposes as $f(A) = \sum_{k \geq 1} f(A_k) \geq 0$.
