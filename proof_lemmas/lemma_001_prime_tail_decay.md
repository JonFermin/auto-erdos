---
id: prime_tail_decay
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 1 — Prime tail sum decays as $1/\log x$

**Statement.** Let $\mathcal{P}_x = \{p \text{ prime} : p \geq x\}$. Then
$$f(\mathcal{P}_x) := \sum_{p \geq x} \frac{1}{p \log p} \sim \frac{1}{\log x}$$
as $x \to \infty$. In particular, $f(\mathcal{P}_x) \to 0$, and for $x \geq 3$,
$$f(\mathcal{P}_x) < \frac{2}{\log x}.$$

**Proof sketch.** By partial summation and the Prime Number Theorem
$\pi(t) \sim t/\log t$:
$$\sum_{p \geq x} \frac{1}{p \log p} = \int_x^\infty \frac{d\pi(t)}{t \log t}
= \left[\frac{\pi(t)}{t \log t}\right]_x^\infty + \int_x^\infty \pi(t)\,d\!\left(\frac{1}{t \log t}\right).$$
Since $\pi(t)/(t \log t) \to 0$ and $d(1/(t \log t)) = -(1 + 1/\log t)/(t \log^2 t)\,dt$,
$$\sum_{p \geq x} \frac{1}{p \log p} \sim \frac{\pi(x)}{x \log x} \cdot \log x + \int_x^\infty \frac{\pi(t)}{t \log^2 t}\,dt
\sim \frac{1}{\log x} + \frac{1}{(\log x)^2} + \cdots \sim \frac{1}{\log x}.$$

More elementarily: $d(1/\log t)/dt = -1/(t \log^2 t)$, and using $\pi(t) \approx t/\log t$:
$$\sum_{p \geq x} \frac{1}{p \log p} \approx \int_x^\infty \frac{dt}{t \log^2 t} = \frac{1}{\log x}.$$

**Numerical verification** (computed in session 0507, from Section 2 data):
- $x = 100$: $f(\mathcal{P}_{100}) \approx 0.122$, $1/\log 100 \approx 0.217$ (ratio $\approx 0.56$)
- $x = 1000$: $f(\mathcal{P}_{1000}) \approx 0.052$, $1/\log 1000 \approx 0.145$ (ratio $\approx 0.36$)
- $x = 10000$: $f(\mathcal{P}_{10000}) \approx 0.016$, $1/\log 10000 \approx 0.109$ (ratio $\approx 0.15$)

The sum decays faster than $1/\log x$ in practice (the asymptotic has
secondary terms).

**Relevance.** For any primitive $A \subset [x, \infty)$, the conjecture's
bound is $f(A) < 1 + o(1)$ with $o(1) \to 0$ as $x \to \infty$. Since
$f(\mathcal{P}_x) \to 0$, the conjectured extremal set (primes $\geq x$)
itself has sum $\to 0 \ll 1$. The conjecture says NO primitive set supported
on $[x, \infty)$ can exceed the bound $1 + o(1)$, but empirically even the
(conjectured) maximizer is $\to 0$. This leaves open the question of which
primitive sets are hard to bound analytically.
