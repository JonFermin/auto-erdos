---
id: rankin_integral
status: open
depends_on: [primes_are_extremal]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma: Rankin integral representation

**Statement.** For any primitive set $A \subset [x, \infty)$,

$$\sum_{a \in A} \frac{1}{a \log a} = \int_1^{\infty} F_A(u) \, du$$

where $F_A(u) = \sum_{a \in A} a^{-u}$ is the Dirichlet series of $A$
(convergent for $u > 1$).

**Proof.** For each $a \geq 2$: $\int_1^{\infty} a^{-u} \, du = [-a^{-u} / \log a]_1^{\infty}
= 0 - (-1/(a \log a)) = 1/(a \log a)$. Summing over $a \in A$ and
interchanging sum and integral (justified by Tonelli since all terms are
non-negative): $\sum_{a \in A} 1/(a \log a) = \int_1^{\infty} F_A(u) \, du$. $\square$

**Reduction to sub-claim.** The conjecture $\sum_A \leq \sum_P$ follows if
we can show $F_A(u) \leq F_P(u)$ for all $u > 1$, since then:

$$\int_1^{\infty} F_A(u) \, du \leq \int_1^{\infty} F_P(u) \, du
= \sum_p \frac{1}{p \log p}.$$

**Sub-claim (OPEN)**: For any primitive set $A$ and any $u > 1$:
$$\sum_{a \in A} a^{-u} \leq \sum_p p^{-u}.$$

**Evidence for sub-claim.** Tested on:
- $A = \{6, 10\}$ (semiprimes with spf 2): $6^{-u} + 10^{-u} = 2^{-u}(3^{-u} + 5^{-u}) \leq 2^{-u} < \sum_p p^{-u}$. ✓
- $A = \{p^k : p \text{ prime}\}$ (prime powers, primitive): $\sum p^{-ku} \leq \sum p^{-u}$ since $ku > u$. ✓
- $A = $ any subset of primes: $F_A(u) = \sum_{p \in A} p^{-u} \leq F_P(u)$. ✓

**Difficulty.** For $A = \{6, 10, 21, 35, \ldots\}$ (semiprimes pairwise
non-divisible involving distinct primes), the sub-claim needs a global bound.
The challenge is that multiple composites with the same smallest prime factor
can coexist in $A$ (e.g., $\{6, 10\}$ both have spf $= 2$).

**Partial proof of sub-claim for $u \geq 2$:**
For any $a \in A$ with $a = p_1^{e_1} \cdots p_k^{e_k}$ ($k \geq 1$,
$e_i \geq 1$):
$$a^{-u} = \prod_i p_i^{-e_i u} \leq \prod_i p_i^{-u} \leq p_j^{-u}$$
for any fixed $j$. This gives $a^{-u} \leq (\text{largest prime factor of } a)^{-u}$.

If the largest prime factors of elements of $A$ are distinct and $\leq$ the
full prime set, the bound follows. But distinctness is not guaranteed.

**Remaining gap.** A clean proof of $F_A(u) \leq F_P(u)$ for all $u > 1$
and all primitive $A$ has not been established here. The
Lichtman–Pomerance 2021 proof handles this; their method may involve a
continuous analog of the discrete inequality $\sum_{a \in A} 1 \leq \sum_p 1$
(which is trivially false globally but holds locally per prime).
