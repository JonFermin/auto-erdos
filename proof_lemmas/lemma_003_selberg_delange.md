---
id: selberg_delange
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 3 — Selberg-Delange asymptotic for restricted Omega strata

**Statement (to be made rigorous).** For fixed $k \geq 1$ and $x \to \infty$:
$$f(A_k^x) = \sum_{a \geq x,\, \Omega(a)=k} \frac{1}{a \log a} \asymp \frac{(\log \log x)^{k-1}}{(k-1)!\, \log x}.$$

Summing over $k \geq 1$:
$$\sum_{k \geq 1} f(A_k^x) \asymp \frac{1}{\log x} \sum_{k \geq 1} \frac{(\log \log x)^{k-1}}{(k-1)!} \cdot C_k$$
where $C_k$ are bounded constants. Since $\sum_{k \geq 1} (\log \log x)^{k-1}/(k-1)! = e^{\log \log x} = \log x$,
this gives $\sum_k f(A_k^x) \asymp 1$, consistent with but not proving $\leq 1$.

**Approach.** The Selberg-Delange method (see Tenenbaum, "Introduction to
Analytic and Probabilistic Number Theory", Chapter II.5) gives: for $z \in \mathbb{C}$
with $\mathrm{Re}(z) > 0$,
$$\sum_{n \leq x} n^{-s} \mathbf{1}[\Omega(n) = k] \asymp C_{s,k} \frac{x^{1-s}}{(1-s)^{1-z}} \frac{(\log \log x)^{k-1}}{(k-1)!}$$
for suitable $z$ related to $s$. For $s = 1$, this degenerates; the correct
statement involves $\sum_{n \leq x, \Omega(n)=k} 1/n \cdot (\log \log x)^{k-1} / ((k-1)! \log x)$.

**Key quantity.** We want $\sum_{n \geq x, \Omega(n)=k} 1/(n \log n)$.
This is a tail sum, related to partial summation of $\sum_{n \leq x, \Omega(n)=k} 1/n$.
By Mertens and Selberg-Delange, $\sum_{n \leq x, \Omega(n)=k} 1/n \sim C_k (\log \log x)^k / k!$
for large $x$. Hence by Abel summation:
$$\sum_{n \geq x, \Omega(n)=k} \frac{1}{n \log n} \sim \frac{C_k (\log \log x)^{k-1}}{(k-1)! \log x}$$
with $C_k$ depending on the Euler product structure.

**Status: open.** The precise value of $C_k$ and the uniformity in $k$ are
not established in this lemma file. The key claim needed for the proof is:
$$\sum_{k=1}^\infty C_k \frac{(\log \log x)^{k-1}}{(k-1)! \log x} \leq \frac{1 + o(1)}{\log x} \cdot \log x = 1 + o(1).$$
This holds iff $\sum_k C_k (\log \log x)^{k-1}/(k-1)! \leq \log x + o(\log x)$,
which holds iff $\sum_k C_k z^{k-1}/(k-1)!$ evaluated at $z = \log \log x$ is
$\leq \log x + o(\log x)$. Since $\log \log x = e^{\log \log \log x}$... this
analysis is not conclusive at this level of generality.

**Current obstacle.** We need to know the generating function $\sum_k C_k z^{k-1}/(k-1)!$
and check its growth at $z = \log \log x$. This requires the full Selberg-Delange
machinery beyond the scope of a single proof session.

**Next move.** Either:
(a) Cite Granville-Koukoulopoulos (2022) as a "given" (if it's provable from the ledger), or
(b) Try a simpler approach: use the Mertens-type estimate directly for the k=1 case (primes only) and bound the remaining strata using F1 as a whole.
