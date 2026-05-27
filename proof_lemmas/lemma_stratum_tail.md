---
id: stratum_tail
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 3
---

# Lemma: Stratum tail bound

**Statement**: For each $k \geq 1$ and any $x \geq 2$,

$$S_k(x) := \sum_{\substack{a \geq x \\ \Omega(a) = k}} \frac{1}{a \log a}
\;\leq\; \frac{C_k(\log \log x)^{k-1}}{(k-1)!\, \log x}$$

for some absolute constant $C_k$. In particular, $S_k(x) \to 0$ as $x \to \infty$
for every fixed $k$.

**Context**: This bounds the contribution of each $\Omega$-stratum to the sum
over any primitive $A \subset [x, \infty)$, since
$\sum_{a \in A, \Omega(a)=k} 1/(a \log a) \leq S_k(x)$.

**Approach using Selberg-Sathe**: The count of integers $n \leq t$ with $\Omega(n)=k$ is

$$\sum_{n \leq t, \Omega(n)=k} 1 \;\sim\; \frac{t}{\log t} \cdot \frac{(\log \log t)^{k-1}}{(k-1)!}$$

by the Selberg-Sathe theorem (or the simpler Hardy-Ramanujan estimate for moderate $k$).
By partial summation:

$$S_k(x) = \int_x^\infty \frac{1}{t \log t} \, d\!\left(\sum_{n \leq t, \Omega(n)=k} 1\right)
\;\approx\; \int_x^\infty \frac{(\log \log t)^{k-1}}{(k-1)!\, t \log^2 t} \, dt.$$

Substituting $u = \log t$:

$$S_k(x) \approx \frac{1}{(k-1)!} \int_{\log x}^\infty \frac{(\log u)^{k-1}}{u^2} \, du.$$

This integral converges for all $k \geq 1$, giving $S_k(x) = O\!\left((\log \log x)^{k-1} / \log x\right)$.

**Status**: The asymptotic estimate is essentially immediate from Selberg-Sathe.
Converting it to a rigorous proved lemma requires a specific reference or a
short proof sketch. **Current obstacle**: need to pin down the constants (or
use a big-$O$ with explicit constant). The precise bound is:

$$S_k(x) \leq \frac{(1 + o(1))(\log \log x)^{k-1}}{(k-1)!\, \log x}.$$

**Sum over $k$**: $\sum_{k=1}^\infty S_k(x) \approx \frac{1}{\log x} \sum_{k=1}^\infty
\frac{(\log \log x)^{k-1}}{(k-1)!} = \frac{e^{\log \log x}}{\log x} = 1 + o(1)$.

This heuristic shows the SUM OVER ALL STRATA is $\approx 1$. But this counts
every integer $\geq x$ once — not a primitive set. The primitivity constraint
means $A$ can use at most a FRACTION of each stratum; see
`lemma_cross_stratum.md` for why this doesn't immediately give $< 1$.

**Obstacle**: The bound $\sum_k S_k(x) \approx 1$ is for the FULL strata
(all integers $\geq x$). For a primitive $A$, we only use a subset of each
stratum. But WHICH subsets can we use simultaneously? The cross-stratum
primitivity constraint is the hard part.
