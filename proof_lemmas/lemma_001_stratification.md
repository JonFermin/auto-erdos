---
id: stratification
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 1 — Stratification decomposition

**Statement.** Let $A \subseteq \mathbb{N}$ be any set (not necessarily primitive).
Define $A_k = A \cap \{n \in \mathbb{N} : \Omega(n) = k\}$ for each $k \geq 1$.
Then $A = \bigsqcup_{k \geq 1} A_k$ (disjoint union, with finitely many or
countably many non-empty strata), and

$$\sum_{a \in A} \frac{1}{a \ln a} = \sum_{k=1}^{\infty} \sum_{a \in A_k} \frac{1}{a \ln a}.$$

**Proof.** Every integer $n \geq 2$ has a unique value $\Omega(n) = k \geq 1$
(where $\Omega$ counts prime factors with multiplicity).  Therefore the sets
$\{A_k\}_{k \geq 1}$ are pairwise disjoint and their union is $A$.
The equality of sums follows by rearranging the absolutely convergent terms
(provided the sum over $A$ is finite; if not, both sides equal $+\infty$). $\square$

**Remark.** This is a tautology: the decomposition is exact and introduces no
approximation.  The content of the proof attempt is in bounding
$\sum_{a \in A_k} 1/(a \ln a)$ for each stratum $k$ and summing.
