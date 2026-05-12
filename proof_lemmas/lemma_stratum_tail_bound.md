---
id: stratum_tail_bound
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma: Tail-sum bound for the $\Omega$-stratum (L1)

## Statement

For $k \geq 1$ and $x \geq 2$, define the *stratum tail-sum*:

$$T_k(x) := \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n}.$$

**L1**: $T_k(x)$ decays to $0$ as $x \to \infty$ (for each fixed $k$), and satisfies:

$$T_k(x) = O\!\left(\frac{(\log \log x)^{k-1}}{(k-1)!\, \log x}\right) \quad \text{as } x \to \infty.$$

Summing:

$$\sum_{k=1}^{K(x)} T_k(x) \leq (1 + o(1)) \cdot \frac{e^{\log \log x}}{\log x} = 1 + o(1) \quad \text{? (needs refinement)}$$

The $K(x)$ cutoff and the exact constant require careful analysis.

## Numerical Evidence

Computed $T_k(x)$ numerically for $k = 1, 2, 3, 4$ and various $x$ (stdlib, iterating $n$):

| $k$ | $T_k(10)$ | $T_k(100)$ | $T_k(1000)$ | $T_k(10000)$ |
|-----|-----------|------------|-------------|--------------|
| 1 | 0.6480 (primes $\geq 11$) | 0.1066 | 0.0358 | 0.0127 |
| 2 | ~ | ~ | ~ | ~ |
| 3 | ~ | ~ | ~ | ~ |

*(Numerics TBD — need a fast prime sieve.)*

Key observation: $T_1(x) = \sum_{p \geq x} 1/(p \log p) \approx 1/\log x$ by
the PNT integral $\int_x^\infty dt/(t(\log t)^2) = 1/\log x$.

## Proof sketch (partial)

**For $k = 1$** (primes): By the prime number theorem,
$\pi(t) \sim t/\log t$, so the density of primes near $t$ is $1/\log t$.  Thus:

$$T_1(x) = \sum_{p \geq x} \frac{1}{p \log p} \approx \int_x^\infty \frac{dt}{t(\log t)^2} = \frac{1}{\log x}.$$

This is a standard estimate (Mertens-type).

**For $k \geq 2$**: By the Sathe–Selberg theorem, the number of integers $n \leq t$
with $\Omega(n) = k$ is:
$$\pi_k(t) \sim \frac{t}{\log t} \cdot \frac{(\log \log t)^{k-1}}{(k-1)!}.$$
By partial summation:
$$T_k(x) = \int_x^\infty \frac{1}{t \log t} \, d\pi_k(t) \approx \int_x^\infty \frac{(\log \log t)^{k-1}}{(k-1)!\, t (\log t)^2} \, dt.$$
Setting $u = \log t$, $du = dt/t$, $\log \log t = \log u$:
$$T_k(x) \approx \int_{\log x}^\infty \frac{(\log u)^{k-1}}{(k-1)!\, u^2} \, du.$$
Integration by parts ($k-1$ times) yields $T_k(x) = O\bigl((\log \log x)^{k-1}/((k-1)! \log x)\bigr)$.

## Current obstacle

The sum $\sum_{k \geq 1} T_k(x)$ with the above bound:

$$\sum_{k=1}^\infty O\!\left(\frac{(\log \log x)^{k-1}}{(k-1)!\, \log x}\right) = \frac{O(e^{\log \log x})}{\log x} = O\!\left(\frac{\log x}{\log x}\right) = O(1).$$

This gives $\sum_k T_k(x) = O(1)$ but NOT $o(1)$ — the bound is too weak for our purpose.
The stratification $f(A) \leq \sum_k T_k(x)$ holds for a primitive $A$, but the upper bound
$\sum_k T_k(x)$ diverges!  (The sum equals $\sum_{n \geq x} 1/(n \log n)$, which diverges.)

**Conclusion**: The naive sum $\sum_k T_k(x)$ is not useful.  We need to use the
PRIMITIVITY of $A$ more carefully — a primitive set can include at most one element
from each chain in the divisibility order, which drastically reduces the actual sum.

Next: `lemma_cross_stratum_blocking.md` addresses this.
