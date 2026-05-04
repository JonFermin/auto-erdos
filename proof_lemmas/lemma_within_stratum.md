---
id: within_stratum
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 7
---

# Lemma: within-stratum primitivity is vacuous

**Claim**: If $S \subset \mathbb{Z}_{\geq 2}$ is any set of distinct integers
all satisfying $\Omega(s) = k$ for a fixed $k \geq 1$, then $S$ is
automatically primitive (no element of $S$ divides another).

**Proof sketch**: Suppose $a, b \in S$ with $a | b$ and $a \neq b$. Since
$\Omega$ is completely additive, $\Omega(b) = \Omega(a) + \Omega(b/a)$.
With $\Omega(a) = \Omega(b) = k$, we get $\Omega(b/a) = 0$, so $b/a = 1$,
i.e., $a = b$ — contradicting $a \neq b$. Therefore no proper divisibility
relation exists within a same-$\Omega$ set, and any such set is primitive.

**Consequence**: The primitive-set constraint "$a \nmid b$ for distinct
$a, b \in A$" is vacuous when $A$ is confined to a single $\Omega$-stratum.
The stratum $A_k$ can be any subset of $\{n \in \mathbb{Z}_{\geq 2} : \Omega(n) = k\}$
without violating primitivity.

This means the primitivity constraint in the Erdős conjecture is an
*inter-stratum* condition: an element $a \in A_k$ can block elements from
$A_j$ for $j \neq k$ (specifically, any $a$-multiple in $A_j$ with $j > k$,
or any divisor of $a$ in $A_j$ with $j < k$, must be excluded), but it
imposes no constraint within the $k$-th stratum itself.

**Implication for the proof strategy**: No within-stratum argument alone
can prove the conjecture. The bound $\sum_{a \in A} 1/(a \log a) \leq 1+o(1)$
must come from inter-stratum interactions. See `lemma_cross_stratum.md`.

**Status**: The claim above is proved (the proof sketch is complete and
elementary). The *lemma* is marked open because the desired within-stratum
*quantitative bound* on $S_k(A)$ remains unproved — the primitivity result
only tells us what is NOT a constraint, not what IS bounded.
