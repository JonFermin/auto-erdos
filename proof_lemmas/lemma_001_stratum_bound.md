---
id: stratum_bound
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 1: Omega-k stratum sum bounds

**Statement.** Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ for $k \geq 1$.

(a) *Large-k asymptotics (cites F3)*: As $k \to \infty$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
In particular, for all sufficiently large $k$, the sum is strictly less than $1$.

(b) *Numerical evidence for small k*: Truncated sums (all elements $\leq 2 \times 10^6$):
- $k=1$ (primes): $1.568 > 1$
- $k=2$: $0.877 < 1$
- $k=3$: $0.510 < 1$
- $k=4$: $0.271 < 1$
- $k=5$: $0.133 < 1$

**Status: open.** Part (a) is a citation of F3 (given fact), so it holds as a
fact. Part (b) provides numerical evidence. The GAP is:

1. **Part (a) relies on F3 which is only an asymptotic for large $k$**. F3's
   sign_disambiguation claims "strictly less than 1 for every $k \geq 1$" but
   numerics show $k=1$ gives sum $\approx 1.57 > 1$. The formula is NOT valid
   for $k=1,2$ — it underpredicts the truncated sums there.

2. **The full stratum sum for $k=1$ diverges or converges to $> 1$**: all
   primes from $p=2$ give $\sum_p 1/(p \log p) \approx 1.57$. So the
   claim "sum $< 1$ for every $k \geq 1$" appears false for $k=1$.

3. **Relevance to the main conjecture**: The conjecture bounds primitive sets
   in $[x, \infty)$. The full stratum $A_1$ includes all primes including
   $p=2$. For the restricted stratum $A_1 \cap [x, \infty)$, the sum
   $\sum_{p \geq x} 1/(p \log p) \to 0$ as $x \to \infty$.

**Current obstacle**: The stratum bound as stated does not directly control
primitive sets in $[x, \infty)$, because it covers the unrestricted stratum
$A_k$. The restricted stratum $A_k \cap [x, \infty)$ has sum $\to 0$ for any
fixed $k$ as $x \to \infty$ — which is too strong (it just says the tail
vanishes). The useful bound requires $k$ and $x$ growing together.

**Next attempt**: Approach via the restricted stratum — cite Omega-k count
estimates (Sathe-Selberg) to bound $\sum_{A_k \cap [x, \infty)} 1/(a \log a)$
when $k \sim C \log \log x$.
