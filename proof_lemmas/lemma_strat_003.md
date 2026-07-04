---
id: strat_003
status: open
depends_on: [strat_001, strat_002]
discharged_by_round: null
introduced_at_round: 2
---

# Lemma strat_003: Cross-stratum primitivity constraint (the crux)

## Statement

Let $A \subset [x, \infty)$ be a primitive set. For each prime $p \in A$
(i.e., $p \in A^{(1)}$), ALL multiples of $p$ are excluded from $A$:
$$\text{If } p \in A, \quad \text{then } kp \notin A \text{ for all } k \geq 2.$$

More generally, if $a \in A^{(j)}$ and $b \in A^{(k)}$ with $a \neq b$,
then $a \nmid b$ and $b \nmid a$.

## Why this is the crux

The crude per-stratum bound (Lemma strat_001) bounds $f(A)$ by
$\sum_k f_k$ which diverges. Using cross-stratum primitivity, the
actual constraint is much tighter. Heuristically:

- If $A$ contains a prime $p$, then the $k$-stratum elements of $A$
  must avoid all multiples of $p$ in $A_k$. This removes a proportion
  roughly $1/p$ of each $A_k$ for each prime in $A$.
- Conversely, if $A$ contains many $k$-almost primes, they cannot
  share too many prime factors (lest one divide another).

The classical machinery for making this precise involves:
- **Brun's sieve**: bounds the sum over elements of a multiplicative
  structure with forbidden prime factors.
- **Plünnecke–Ruzsa inequality**: relates the size of a sum-set to the
  density of a set.
- **Mertens-type estimates**: $\sum_{p \leq x} 1/p \sim \log \log x$.

## Key difficulty

Quantifying how much primitivity reduces the weight across ALL strata
simultaneously. A simple sieve argument for one stratum does not
easily compose into a global bound.

## Approach attempt: "Exclusion principle"

For a primitive $A \subset [x, \infty)$ with $p \in A \cap A_1$, define
$R_k(p) = \{n \in A_k : p | n\}$. Then $A^{(k)} \cap R_k(p) = \emptyset$,
so
$$S_k(A) \leq \sum_{a \in A_k, a \geq x, p \nmid a} \frac{1}{a \log a}
= S_k(A_k \cap [x,\infty)) - \sum_{a \in A_k, a \geq x, p | a} \frac{1}{a \log a}.$$

For $p | a$ with $a \in A_k$, write $a = p \cdot b$ where $\Omega(b) = k-1$
and $b \geq x/p$. So
$$\sum_{a \in A_k, p | a, a \geq x} \frac{1}{a \log a}
= \sum_{b: \Omega(b)=k-1, b \geq x/p} \frac{1}{pb \log(pb)}.$$

This recurrence connects the $k$-stratum exclusion to the $(k-1)$-stratum,
hinting at an inductive argument.

## Status

Open. The approach above gives a recurrence but does not yet close into
a uniform bound. The issue is summing the exclusion contributions from
ALL primes in $A$, which depends on the primes chosen (a self-referential
constraint).

## Next move (suggested)

Try to bound $f(A)$ using the fact that for a primitive $A$, the sum
$\sum_{p | a, p \in A} 1$ is 0 for all $a \in A$ (no element of $A$
has a prime factor that is itself in $A$, unless that element IS that
prime). This might allow a multiplicative-function estimate on the
density of $A$ in each stratum.
