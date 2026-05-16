---
id: Ak_primitive
status: proved
depends_on: []
discharged_by_round: 4
introduced_at_round: 4
---

## Lemma Ak_primitive: Each $A_k$ is a Primitive Set

**Statement**: For each $k \geq 1$, the set
$A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ is primitive.

**Proof**: Let $a, b \in A_k$ with $a \neq b$. Suppose for contradiction that
$a \mid b$, i.e., $b = am$ for some integer $m \geq 1$. Since $\Omega$ is
completely additive ($\Omega(mn) = \Omega(m) + \Omega(n)$), we have
$\Omega(b) = \Omega(a) + \Omega(m) = k + \Omega(m)$. Since $b \in A_k$,
$\Omega(b) = k$, so $\Omega(m) = 0$. But $\Omega(m) = 0$ implies $m = 1$,
hence $b = a$ — contradicting $a \neq b$. $\square$

**Corollary**: Every subset $A_k \cap S$ is also primitive.
