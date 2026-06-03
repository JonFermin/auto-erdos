---
id: omega_stratification
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 1 — Omega-stratification

**Statement**: Let $A \subset [x, \infty)$ be a primitive set. For each $k \geq 1$, define
$A^{(k)} = A \cap \{n : \Omega(n) = k\}$ (elements of $A$ with exactly $k$ prime factors,
counted with multiplicity). Then $A = \bigsqcup_{k \geq 1} A^{(k)}$ (disjoint union), and
each $A^{(k)} \subseteq A_k \cap [x, \infty)$.

**Proof**: Every integer $n \geq 2$ satisfies $\Omega(n) = k$ for some unique $k \geq 1$
(since $\Omega$ is well-defined). So the sets $\{A^{(k)}\}$ are disjoint and cover $A$.
The inclusion $A^{(k)} \subseteq A_k$ is immediate from the definitions. Each element of
$A^{(k)}$ is in $A \subset [x, \infty)$, so $A^{(k)} \subseteq A_k \cap [x, \infty)$. $\square$

**Remark**: Lemma 1 alone is not sufficient to bound the sum. While
$\sum_{a \in A^{(k)}} 1/(a \log a) \leq T_k(x) := \sum_{a \in A_k \cap [x, \infty)} 1/(a \log a)$,
the sum $\sum_k T_k(x) = \sum_{n \geq x} 1/(n \log n)$ diverges (by integral comparison).
The proof must use the primitivity constraint to show the strata cannot all contribute at
full capacity simultaneously. This motivates Lemma 2 (spf-reduction).
