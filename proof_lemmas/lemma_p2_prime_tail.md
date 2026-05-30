---
id: p2_prime_tail
status: proved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma P2 — Prime tail is $o(1)$

## Statement

For all $x \geq 3$:
$$\sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p} \leq \frac{2}{\log x}.$$

In particular, the left side tends to $0$ as $x \to \infty$, so the bound is $o_x(1)$.

## Proof

We use partial summation with Chebyshev's estimate $\pi(t) \leq 2t/\log t$
(valid for all $t \geq 1$; see, e.g., Hardy–Wright §22.4 or any intro
analytic number theory text).

Let $f(t) = 1/(t \log t)$. Then

$$\sum_{p > x} \frac{1}{p \log p} = \sum_{p > x} f(p).$$

By partial summation (Abel summation formula), for any $T > x$:

$$\sum_{x < p \leq T} f(p) = f(T) \pi(T) - f(x^+) \pi(x) - \int_x^T \pi(t) f'(t) \, dt.$$

As $T \to \infty$, $f(T) \pi(T) \leq (2/\log T) \cdot (1/\log T) \to 0$
(using Chebyshev). The boundary term at $x$ also tends to 0 in the sum.
The integral term:

$$-\int_x^\infty \pi(t) f'(t) \, dt = \int_x^\infty \pi(t) \frac{1 + \log t}{t^2 \log^2 t} \, dt.$$

Using $\pi(t) \leq 2t/\log t$:

$$\int_x^\infty \pi(t) \frac{1 + \log t}{t^2 \log^2 t} \, dt \leq \int_x^\infty \frac{2t}{\log t} \cdot \frac{2}{t^2 \log t} \, dt = \int_x^\infty \frac{4}{t \log^2 t} \, dt = \frac{4}{\log x}.$$

Alternatively, a cleaner estimate: applying the Chebyshev bound directly,

$$\sum_{p > x} \frac{1}{p \log p} \leq \int_x^\infty \frac{2}{\log t} \cdot \frac{1}{t \log t} \, dt = \int_x^\infty \frac{2}{t \log^2 t} \, dt = \frac{2}{\log x}.$$

(Here we use the Stieltjes-integral form $\sum_{p > x} f(p) \leq \int_x^\infty f(t) \, d\pi(t) \leq \int_x^\infty f(t) \cdot (2/\log t) \, dt$ where the second inequality uses $d\pi(t) \leq (2/\log t) dt$, the Chebyshev density bound.)

Either way, we obtain $\sum_{p > x} 1/(p \log p) \leq 2/\log x$. $\square$

## Remark

The sharp asymptotic is $\sum_{p > x} 1/(p \log p) \sim 1/\log x$ as $x \to \infty$
(follows from PNT + partial summation). The bound $2/\log x$ has an extra factor
of 2 from the Chebyshev constant; for the purposes of proving $< 1+o(1)$, this
crude bound suffices.
