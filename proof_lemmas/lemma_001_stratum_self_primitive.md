---
id: stratum_self_primitive
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 1: Within-stratum subsets are automatically primitive

**Statement**: Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ where $\Omega(n)$ counts
prime factors with multiplicity. For any subset $S \subseteq A_k$, $S$ is primitive
(no element of $S$ divides another element of $S$).

**Proof**: Suppose $a, b \in A_k$ with $a \mid b$. Then $b = am$ for some positive
integer $m$. Since $b \neq 0$, we have $m \geq 1$. If $m = 1$ then $a = b$. If
$m \geq 2$ then $\Omega(b) = \Omega(am) = \Omega(a) + \Omega(m) \geq \Omega(a) + 1 = k + 1 > k$,
contradicting $b \in A_k$. Hence $m = 1$ and $a = b$.

Therefore, distinct elements of $A_k$ cannot divide each other. $\square$

**Consequence**: The only cross-stratum constraint in a primitive set $A = \bigcup_k A_k^A$
(where $A_k^A = A \cap \{n: \Omega(n)=k\}$) is between elements from **different** strata:
for $j < k$, $a \in A_j^A$, $b \in A_k^A$, we need $a \nmid b$.
