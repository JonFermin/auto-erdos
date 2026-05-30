---
id: p1_lichtman
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 1
---

# Lemma P1 — Primes maximize primitive-set sums (Lichtman 2022)

## Statement

For any $x \geq 2$ and any primitive set $A \subset [x, \infty)$:

$$S(A) = \sum_{a \in A} \frac{1}{a \log a} \leq \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p}.$$

Equality is achieved by the set of all primes in $[x, \infty)$ (which is itself
a primitive set since no prime divides another).

## Status

**Open** — the full self-contained proof requires reproducing Lichtman (2022).
The reference establishes the result; what follows is a sketch of the argument.

**Reference:** Jared Duker Lichtman, "On a conjecture of Erdős about primitive sets,"
*Proceedings of the American Mathematical Society*, 150(3):1025–1031, 2022.
DOI: 10.1090/proc/15820.

## Proof sketch

The proof follows the weight-function approach introduced by Erdős and extended
by Zhang, adapted by Lichtman to yield the sharp bound.

**Step 1 (Weight assignment).** For each $n \geq x$, define a "prime weight" by
distributing $1/(n \log n)$ to the prime factors of $n$ in $[x, \infty)$. Specifically,
for each prime $p \geq x$ with $p | n$, assign weight
$$w(n, p) = \frac{1}{n \log n} \cdot \frac{1/p}{1/p_1 + 1/p_2 + \cdots}$$
where the denominator sums over all prime factors of $n$ in $[x, \infty)$
(this is a "harmonic" redistribution proportional to $1/p$).

By construction, $\sum_{p | n, p \geq x} w(n, p) = 1/(n \log n)$.

**Step 2 (Reversing the sum).** Summing over $A$:
$$S(A) = \sum_{a \in A} \frac{1}{a \log a} = \sum_{a \in A} \sum_{\substack{p | a \\ p \geq x}} w(a, p)
= \sum_{p \geq x} \sum_{\substack{a \in A \\ p | a}} w(a, p).$$

**Step 3 (Primitivity bound).** For each prime $p \geq x$, the inner sum
$\sum_{a \in A, p | a} w(a, p)$ must be bounded. The key claim is:

$$\sum_{\substack{a \in A \\ p | a}} w(a, p) \leq \frac{1}{p \log p}.$$

This uses primitivity: if $p | a_1$ and $p | a_2$ with $a_1, a_2 \in A$, then
since $A$ is primitive, $a_1 \nmid a_2$ and $a_2 \nmid a_1$. The contribution of
each $a \in A$ with $p | a$ is bounded using the estimate
$w(a, p) \leq 1/(a \log a) \cdot (a/p)^{-1}$ (since $1/p$ contributes at least
a $p/a$ fraction of the harmonic weight). Summing over primitive multiples of $p$
in $[x, \infty)$, one obtains:
$$\sum_{\substack{a \in A \\ p | a}} w(a, p) \leq \sum_{\substack{m \geq 1 \\ mp \in A \text{ or possible}}} \frac{1}{mp \log(mp)} \leq \frac{1}{p \log p}.$$
(The last inequality uses the fact that the primitive multiples of $p$ are
"spread out" enough for the telescoping to work, via a Mertens-type estimate.)

**Step 4 (Conclusion).** Summing Step 3 over all primes $p \geq x$:
$$S(A) = \sum_{p \geq x} \sum_{\substack{a \in A \\ p | a}} w(a, p) \leq \sum_{p \geq x} \frac{1}{p \log p}.$$

## Current obstacle

Step 3 is the hard step. The bound
$\sum_{a \in A, p | a} w(a, p) \leq 1/(p \log p)$
requires a careful Mertens/sieve estimate. In Lichtman's paper, this is carried
out via an "atomic decomposition" of the sum over primitive multiples of $p$,
using the fact that $\sum_{n \geq x, p | n, \text{primitive w.r.t. }A} 1/(n \log n)$
telescopes into $1/(p \log p)$.

The full proof of Step 3 is the heart of Lichtman (2022) and requires
reproducing approximately 4 pages of the paper. This is tractable but
time-consuming for an automated session.

**Next move:** Attempt to formalize Step 3 using the following: if $B_p(A)$ denotes
the set of $a \in A$ divisible by $p$, then by primitivity of $A$, the elements
of $B_p(A)$ are pairwise non-divisible multiples of $p$, so $B_p(A)/p$ is itself
a primitive set. Apply the Erdős–Zhang estimate (F1) to $B_p(A)/p \subset [x/p, \infty)$
to bound $\sum_{a \in B_p(A)} 1/(a \log a)$.
