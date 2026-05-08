---
id: single_stratum_bound
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 1: Single-stratum tail sum bound

**Statement.** For any $k \geq 1$ and any $\varepsilon > 0$, there exists
$X = X(k, \varepsilon)$ such that for all $x \geq X$:
$$\sum_{\substack{a \geq x \\ \Omega(a) = k}} \frac{1}{a \log a} < \varepsilon.$$

In particular, for any fixed $k$, the tail sum of $k$-almost primes goes to $0$
as $x \to \infty$.

**Difficulty.** EASY — this is essentially an exercise in partial summation +
PNT for k-almost primes.

**Proof sketch (to be formalized).**

Let $\pi_k(x) = \#\{n \leq x : \Omega(n) = k\}$. By the Selberg-Sathe theorem
(or Sathe-Selberg formula), $\pi_k(x) \sim \frac{x}{\log x} \cdot \frac{(\log \log x)^{k-1}}{(k-1)!}$.
The density of k-almost primes is well-understood.

The tail sum satisfies:
$$\sum_{\substack{a \geq x \\ \Omega(a) = k}} \frac{1}{a \log a}
= \int_x^\infty \frac{d(\pi_k(t))}{t \log t}
\leq \int_x^\infty \frac{C_k \, (\log \log t)^{k-1}}{(\log t)^2} \, dt$$
where the last step uses $d(\pi_k(t)) \leq C_k (\log\log t)^{k-1}/\log t \, dt$.

For fixed $k$, the integrand is $O((\log\log t)^{k-1}/(\log t)^2)$, which
is integrable and the integral from $x$ to $\infty$ goes to $0$ as $x \to \infty$.

**Current obstacle.** Need to formalize the integration-by-parts and verify
the Selberg-Sathe bound in a form that gives the $\varepsilon$ conclusion.
Also need to check whether $k$-uniformity holds (i.e., can $k$ depend on $x$?).

**Corollary (trivially):** For any one-stratum set $A \subset \{n: \Omega(n)=k, n \geq x\}$,
$S(A) \leq S(B_k^x) \to 0$ as $x \to \infty$ for fixed $k$.
