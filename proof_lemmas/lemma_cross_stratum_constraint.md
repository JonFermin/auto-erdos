---
id: cross_stratum_constraint
status: open
depends_on: [stratum_bound]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma: Cross-stratum non-divisibility constraint

**Statement.** Let $A \subset [x, \infty)$ be a primitive set. For each $k$,
let $A_k = A \cap \{n : \Omega(n) = k\}$. If $a \in A_j$ and $b \in A_k$
with $j < k$, then $a \nmid b$.

**Proof.** If $a \mid b$ with $a \neq b$, then $b/a \geq 2$, so $\Omega(b/a)
\geq 1$, giving $\Omega(b) = \Omega(a) + \Omega(b/a) \geq j + 1 > j$.
Since $\Omega(b) = k$ and $\Omega(a) = j < k$, the condition $a \mid b$
with $a \neq b$ is consistent with $\Omega$. The primitivity of $A$
forbids $a \mid b$. $\square$

**Discussion.**

This lemma is easy but its consequence is crucial: knowing which elements
appear in $A_j$ constrains which elements can appear in $A_k$ for $k > j$.

**Implication (sieve perspective).** If $p \in A_1$ (a prime in $A$),
then no multiple $pn$ with $n \geq 2$ and $pn \geq x$ can be in $A$
(because $p \mid pn$ and both would be in $A$, violating primitivity).
Thus the presence of $p$ in $A$ "excludes" all integers divisible by $p$
from $A$. The contribution of $p$ to the sum, $1/(p \log p)$, comes at
the cost of excluding all multiples.

**The hard gap.** Using this constraint to prove a global bound of
$\leq 1 + o(1)$ requires showing that the exclusion zones of primes and
higher-stratum elements collectively "cover" enough mass to keep the total
sum bounded. This is the core difficulty of the conjecture.

**Current obstacle.** A clean local-to-global argument is not yet
available. The Lichtman–Pomerance 2021 proof is the reference, but their
technique (integral inequality on multiplicative functions) has not yet
been fully transcribed here.
