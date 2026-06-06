---
id: cross_stratum_interaction
status: open
depends_on: [stratification, prime_stratum_obstacle]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 4 — Cross-stratum interaction (the core difficulty)

**Statement (informal).** Let $A \subset [x, \infty)$ be primitive.  If
$a \in A$ with $\Omega(a) = j$, then no multiple of $a$ (i.e., $ka$ for
$k \geq 2$) can appear in $A$.  This "exclusion" constrains the joint
distribution of elements across strata.

More precisely: let $A_j$ and $A_k$ ($j < k$) be the strata of $A$.
The primitive condition says: for each $a \in A_j$, no element of $A_k$
is a multiple of $a$.  This means $A_k$ is not just any subset of
$\{n \geq x: \Omega(n) = k\}$ — it avoids all multiples of elements of
$A_j$, of $A_{j-1}$, etc.

**Why this matters.** The naive stratum bound (Lemma 2) ignores this
cross-stratum constraint and gives a divergent sum.  The cross-stratum
interaction is what makes the sum over a primitive set finite and
(conjectured) bounded by $1 + o(1)$.

**The approach used in the literature (F1, F2 proofs).** The Erdős (1935) /
Zhang (1993) approach uses a Dirichlet series / Euler product argument:

For a primitive set $A$, the generating function $D_A(s) = \sum_{a \in A} a^{-s}$
satisfies constraints because of primitivity.  In particular, if $a \in A$,
then no $a' = a \cdot m$ (for $m \geq 2$) is in $A$.  Writing $a = a_j \in A_j$:
$$D_A(s) = \sum_{j \geq 1} D_{A_j}(s)$$
and the primitive constraint bounds the "interaction" between $D_{A_j}$ and
$D_{A_k}$ for $j \neq k$.

The key identity used is:
$$\frac{1}{a \ln a} = \int_0^\infty a^{-(1+t)} dt,$$
which allows $\sum_{a \in A} 1/(a \ln a) = \int_0^\infty D_A(1+t) dt$.
The primitive condition then bounds $D_A(1+t)$ via the Euler factorization.

**Status: open (hard).** The cross-stratum interaction has been analyzed in
the literature (Erdős 1935, Zhang 1993, further improvements in the 2020s),
but reproducing or improving on those bounds requires:
- A rigorous sieve estimate for the density of elements in $A_k$ that avoid
  multiples of elements in $A_{j<k}$.
- An Euler-product bound on $D_A(s)$ using the multiplicative structure.
- A partial-summation argument for the integral $\int_0^\infty D_A(1+t) dt$.

**Current obstacle.** This lemma is the deepest open item.  Progress on this
lemma would require:
1. Citing or proving a bound on $D_A(1+t)$ for primitive $A \subset [x, \infty)$.
2. Integrating the bound over $t \in [0, \infty)$ to get the conjectured
   $< 1 + o(1)$ bound.

**Suggested next move for a future session.**
Investigate whether the bound $D_A(1+t) < \prod_p (1 + p^{-(1+t)})$ for
some product over primes can be established and integrated.  This is related
to the Euler product $\prod_p (1 - p^{-(1+t)})^{-1} = \zeta(1+t)$ but
restricted to the "antichain" (primitive) constraint.
