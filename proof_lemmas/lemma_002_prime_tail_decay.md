---
id: prime_tail_decay
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 2: Prime-tail sum decays as x grows

**Statement.** The sum of $1/(p \log p)$ over primes $p \geq x$ satisfies
$$\sum_{p \geq x} \frac{1}{p \log p} \to 0 \quad \text{as } x \to \infty.$$

More precisely, by partial summation using the prime number theorem $\pi(t) \sim t/\log t$:
$$\sum_{p \geq x} \frac{1}{p \log p} \approx \frac{1}{\log x} \quad \text{(rough estimate)}.$$

**Proof.** Since $\sum_{p} 1/(p \log p)$ converges (as the full series $\sum_p 1/(p\log p) < \infty$ by comparison with $\sum_p 1/p^{1+\varepsilon}$ or by direct PNT estimate $\int_2^\infty 1/(x \log^2 x) dx < \infty$), the tail sum $\sum_{p \geq x} 1/(p \log p)$ is the tail of a convergent series and hence $\to 0$.

**Numerical verification** (from Q3 computation):
- $x=2$: sum $\approx 1.575$
- $x=3$: sum $\approx 0.853$
- $x=5$: sum $\approx 0.550$
- $x=100$: sum $\approx 0.153$
- $x=1000$: sum $\approx 0.082$

The sum drops below $1$ already at $x=3$. **QED.**

**Relevance to the main conjecture**: If the conjecture reduces to showing that
any primitive $A \subset [x, \infty)$ has sum $\leq \sum_{p \geq x} 1/(p \log p) + \text{error}(x)$, then this lemma (combined with a bounding lemma for the error) would suffice. The challenge is establishing that primitive-set sums are comparable to the prime-tail sum — this is Lemma 3 (open).
