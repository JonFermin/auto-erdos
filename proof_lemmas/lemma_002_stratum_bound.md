---
id: stratum_bound
status: open
depends_on: [omega_stratification]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 2 — Per-stratum sum bound

**Statement**: For each $k \geq 1$ and $x \geq 2$, define

$$S_k(x) = \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n}.$$

We want a bound $S_k(x) \leq B_k(x)$ such that $\sum_{k \geq 1} B_k(x) \leq 1 + o(1)$
as $x \to \infty$.

**Numerical observations** (from §2.1 of proof_strategy.md):

| $k$ | $S_k(x)$ at $x=100$ | at $x=1000$ | at $x=10000$ |
|-----|---------------------|-------------|--------------|
| 1 | 0.139 | 0.068 | 0.032 |
| 2 | 0.278 | 0.157 | 0.081 |
| 3 | 0.265 | 0.164 | 0.090 |
| 4 | 0.177 | 0.117 | 0.067 |
| 5 | 0.099 | 0.068 | 0.041 |
| 6 | 0.048 | 0.035 | 0.022 |
| **total** | **≈ 1.006** | **≈ 0.609** | **≈ 0.333** |

(These are lower bounds on the true $S_k(x)$, as the upper cutoff is $N=500{,}000$.)

**Key difficulty**: The sum $\sum_{k \geq 1} S_k(x)$ is $\sum_{n \geq x} 1/(n \log n)$
over integers $n \geq x$ with any $\Omega$-value. This trivially
$= \sum_{n \geq x} 1/(n \log n)$, which diverges for any fixed $x$ (since
$1/(n \log n)$ is like $1/n$ up to log factors, and $\sum 1/n$ diverges).

Wait — this is a crucial point. **The sum $\sum_{n \geq x} 1/(n \log n)$
diverges** (it grows like $\log \log N$ as the upper cutoff $N \to \infty$).
So the sum over ALL $A_k$ is unbounded.

The conjecture is about a PRIMITIVE SET $A \subset [x, \infty)$, NOT about
all of $[x, \infty)$. The primitivity constraint is what limits the sum!

**Revised approach**: The correct bound is NOT over a single stratum but
over any primitive antichain. The optimal primitive set is NOT all integers
$\geq x$; it's an antichain that balances density vs. weight.

**Key insight**: By Dilworth's theorem, the maximum antichain in $[x, 2x)$
under divisibility is all of $[x, 2x)$ (an interval of ratio 2 is always
an antichain). But this set has sum $\sum_{n=x}^{2x} 1/(n \log n) \approx
\int_x^{2x} dt/(t \log t) = \log(1 + \log 2/\log x) \to 0$ as $x \to \infty$.

**Alternative**: The $A_k$ idea: for a single stratum with $k$ large, all
of $A_k \cap [x, \infty)$ is an antichain (within the stratum), and numerically
$S_k(x)$ is maximized around $k = 2$ or $k = 3$ for small $x$. As $x$ grows,
the sum over any single stratum goes to 0.

**What we need to prove**: For any antichain (primitive set) $A \subset [x, \infty)$,
$\sum_{a \in A} 1/(a \log a) \leq 1 + o(1)$. Since the sum over $A_k$ is
$S_k(x) \to 0$ for each fixed $k$, the challenge is to rule out clever
combinations of elements across strata that could maintain a sum near 1.

**Current obstacle**: The proof seems to require bounding $\sum_k S_k(x)$
RESTRICTED to the antichain constraint, which is a global constraint. The
stratification reduces to bounding each $S_k(x)$ separately, but the sum
over all $k$ at any fixed $x$ is unbounded (diverges) — the antichain
constraint provides the magic that keeps the total finite.

**Promising direction**: The Erdős–Zhang proof strategy may use the following:
assign each $a \in A$ to its smallest prime factor $p(a)$. Bound the
contribution from elements with $p(a) = p$ by $1/p \cdot f(p, x)$ for some
$f$. Sum over $p$.
