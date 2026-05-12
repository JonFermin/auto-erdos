---
id: cross_stratum_blocking
status: open
depends_on: [stratum_tail_bound]
discharged_by_round: null
introduced_at_round: 2
---

# Lemma: Cross-stratum blocking for primitive sets (L2)

## Statement

Let $A \subset [x, \infty)$ be a primitive set.  For any fixed $a \in A$ with
$\Omega(a) = j$, the divisors of $a$ and the multiples of $a$ in $[x, \infty)$
are all excluded from $A$.

**L2 (informal)**: For each $a \in A$ with $\Omega(a) = j$, the "blocked" elements
include at minimum all $n \geq x$ with $a \mid n$.  The contribution of these
blocked elements to $\sum_k T_k(x)$ is:

$$\sum_{\substack{n \geq x \\ a \mid n}} \frac{1}{n \log n} = \frac{1}{a} \sum_{\substack{m \geq x/a}} \frac{1}{m \log(am)} \approx \frac{1}{a \log a}.$$

In other words: by including $a$ in $A$ (contributing $1/(a \log a)$), we block
approximately $1/(a \log a)$ worth of other elements from $\sum_k T_k(x)$.

**Rough consequence**: the "effective" sum after accounting for blocking is much
smaller than $\sum_k T_k(x)$.

## Motivation

If the contribution of $a$ to $f(A)$ ($=1/(a \log a)$) equals the contribution
blocked from $T_k$ by $a$'s presence (also $\approx 1/(a \log a)$), then every
element of $A$ "pays for itself" by blocking an equal amount from the ambient
tail-sum.  This is the intuition behind why $f(A) \leq 1 + o(1)$.

## Formal approach

Define the "weight" of a primitive set $A$:

$$W(A, x) := \sum_{a \in A} \frac{1}{a \log a} \cdot \left(1 + \sum_{\substack{n \geq x/a \\ a \nmid n}} \frac{a}{n \log(an)}\right)^{-1}.$$

This is too complex to evaluate directly.  Instead, use the standard "Erdős–Turán"
approach: bound $f(A)$ by a product formula or a sieve.

## Alternative: direct sieve approach

For any primitive $A \subset [x, \infty)$ and any parameter $y$, partition
$A$ into:
- $A_{\text{small}} = \{a \in A : \text{all prime factors of } a \leq y\}$
- $A_{\text{large}} = A \setminus A_{\text{small}}$

**$A_{\text{small}}$**: These are $y$-smooth numbers $\geq x$.  For fixed $y$ and
$x \to \infty$, there are few such numbers (the smooth count $\Psi(t, y)/t \to 0$
as $t \to \infty$ for fixed $y$), so $f(A_{\text{small}}) \to 0$.

**$A_{\text{large}}$**: Each element has a prime factor $> y$.  Elements of $A_{\text{large}}$
sharing the same "large" prime factor cannot both be in $A$ (one would divide a multiple
of the other by the large prime).  This gives a bound on $|A_{\text{large}} \cap [t, 2t)|$
that limits $f(A_{\text{large}})$.

## Current obstacle

This approach gives $f(A) \leq f(A_{\text{small}}) + f(A_{\text{large}}) \leq o(1) + f(A_{\text{large}})$,
but bounding $f(A_{\text{large}})$ by 1 requires careful analysis of how often two elements
of $A$ can share a large prime factor.  This is essentially a problem about the
"multiplicity" of large primes in a primitive set, and it is the hard core of the
conjecture.

The difficulty is that elements of $A$ can have many distinct large prime factors,
so the blocking argument does not trivially give a factor of 1.

Next: `lemma_total_bound.md` summarizes what we've established and identifies
the precise gap.
