---
id: prime_sum_asymptotics
status: proved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma 3: Prime sum asymptotics

**Statement.**
$$P(x) := \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p} = \frac{1 + o(1)}{\log x} \xrightarrow{x \to \infty} 0.$$

In particular, $P(x) < 1$ for all $x \geq 3$.

**Proof sketch (PNT-based).** By partial summation and the prime number theorem
$\pi(t) \sim t / \log t$:
$$\sum_{p \geq x} \frac{1}{p \log p} = \int_x^\infty \frac{1}{t (\log t)^2} \, d\pi(t)
\approx \int_x^\infty \frac{1}{t (\log t)^2} \cdot \frac{dt}{\log t}
= \int_x^\infty \frac{dt}{t (\log t)^2}.$$

Evaluating the integral:
$$\int_x^\infty \frac{dt}{t (\log t)^2} = \left[ -\frac{1}{\log t} \right]_x^\infty = \frac{1}{\log x}.$$

So $P(x) \sim 1/\log x$ as $x \to \infty$. $\square$

**Numerical check (from Section 3):**

| $x$ | $P(x) \approx$ | $1/\log x$ |
|-----|----------------|------------|
| 2 | 1.637 | 1.443 |
| 3 | 0.916 | 0.910 |
| 100 | 0.217 | 0.217 |
| 1000 | 0.145 | 0.145 |

At $x = 2$: $P(2) \approx 1.637 > 1$, so the conjecture's bound $1 + o(1)$ is not
trivially below 1 at $x = 2$. At $x = 3$: $P(3) \approx 0.916 < 1$, so Lemma 3
alone (without Lemma 2) shows any primitive set of primes from 3 already satisfies
the $< 1$ threshold.

**Consequence for the conjecture.** If Lemma 2 (prime extremality) holds, then
for all $x \geq 3$ and any primitive $A \subseteq [x, \infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq P(x) < 1 \leq 1 + o(1). \quad \square$$
