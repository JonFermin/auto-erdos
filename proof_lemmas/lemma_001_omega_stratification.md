---
id: omega_stratification
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 1 — Omega-stratification reduction

**Statement**: Let $A \subset [x, \infty)$ be a primitive set. Define
$A_k = A \cap \{n : \Omega(n) = k\}$ (the $k$-th stratum). Then:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} \sum_{a \in A_k} \frac{1}{a \log a}.$$

Moreover, the strata $A_k$ are pairwise "non-interfering" in the following
sense: for $k \neq j$, no element of $A_k$ divides any element of $A_j$ (since
if $m | n$ with $\Omega(m) < \Omega(n)$, then $m \in A_k$ and $n \in A_j$
with $k < j$ would violate primitivity of $A$).

**Status**: The equation is trivial (disjoint partition). The non-interference
claim follows directly from the definition of primitive set: if $a \in A_k$
and $b \in A_j$ with $k < j$ and $a | b$, then $a, b \in A$ with $a | b$
and $a \neq b$, contradicting primitivity.

**What this buys**: It suffices to bound $\sum_{a \in A_k} 1/(a \log a)$
for each $k$ and then sum over $k$. However, the constraint that $A$ is a
primitive set is NOT decomposed — cross-stratum divisibility is already
forbidden, but WITHIN each stratum $A_k$, we also need primitivity (which is
automatically satisfied since all elements have the same $\Omega$-value —
no element of $A_k$ can divide another since they have equal $\Omega$, and if
$a | b$ with $a \neq b$ then $\Omega(b) > \Omega(a)$, contradiction).

**Current obstacle**: The bound on each stratum's sum is the hard part:
for stratum $k$, what is the maximum of $\sum_{a \in A_k} 1/(a \log a)$
over all primitive subsets $A_k \subset [x, \infty) \cap \{n : \Omega(n) = k\}$?
Since all elements of $A_k$ have $\Omega = k$, ANY subset is automatically
an antichain (within this stratum), so the maximum is just the full stratum
sum $\sum_{n \geq x, \Omega(n)=k} 1/(n \log n)$.

**Next step**: Lemma 2 should bound $\sum_{n \geq x, \Omega(n)=k} 1/(n \log n)$
for each $k$ and find the optimal $k$ as a function of $x$.
