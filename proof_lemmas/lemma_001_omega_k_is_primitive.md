---
id: lemma_001_omega_k_is_primitive
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 1 — $A_k$ is a primitive set

**Statement.** For every integer $k \geq 1$, the set
$A_k = \{\, n \in \mathbb{Z}_{\geq 2} : \Omega(n) = k \,\}$ — all
positive integers with exactly $k$ prime factors counted with
multiplicity — is a *primitive* set: no two distinct elements of $A_k$
divide one another.

**Proof.** Let $a, b \in A_k$ with $a \mid b$. Write $b = a \cdot t$
for some $t \in \mathbb{Z}_{\geq 1}$. Then $\Omega$ is completely
additive: $\Omega(b) = \Omega(a) + \Omega(t)$. Since $a, b \in A_k$
both have $\Omega = k$,
$$
k \;=\; \Omega(b) \;=\; \Omega(a) + \Omega(t) \;=\; k + \Omega(t),
$$
so $\Omega(t) = 0$, which forces $t = 1$ and hence $a = b$. Thus no
distinct $a, b \in A_k$ satisfy $a \mid b$. $\square$

**Use.** This lemma is cited by `proof_strategy.md` §2.4 to license
the framing of $A_k$ (and any subset $A_k \cap [x, \infty)$) as a
*primitive set* in $[x, \infty)$, so that F3 directly applies to its
sum. Without this, references to "the stratum $A_k$" as a primitive
set would be unfounded.
