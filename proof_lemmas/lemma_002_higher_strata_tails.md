---
id: higher_strata_tails
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 2: Higher Strata Tail Bounds

**Statement**: For each fixed $k \geq 2$ and $A \subseteq [x, \infty)$ primitive:
$$\sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \ln a}
\leq \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \ln n} =: T_k(x) \to 0
\quad \text{as } x \to \infty.$$

Moreover, $T_k(x) = O(1/(\ln x)^c)$ for some $c > 0$ depending on $k$.

**Partial argument**: The first inequality is trivial: $A \cap A_k \subseteq A_k$. The
convergence $T_k(x) \to 0$ follows from the fact that $\sum_{n: \Omega(n)=k} 1/(n \ln n)$
converges for each $k \geq 2$ (the series is a "tail" of a convergent sum, and removing
all $n < x$ gives a remainder going to 0).

**Remaining obstacle (convergence of full series)**: We need the series
$\sum_{n: \Omega(n)=k} 1/(n \ln n)$ to converge for each $k \geq 2$. Numerical evidence
(from the Q2 computation) suggests convergence for $k=2,3,4$ with the tail bounded above
by $1/\ln(\max \text{ element computed})$. A rigorous proof of convergence would use:

The Selberg-Delange method or Dirichlet series analysis: letting
$F_k(s) = \sum_{n: \Omega(n)=k} n^{-s}$, one shows $F_k(s)$ converges for $\Re(s) > 1$
(absolute convergence from $\sum n^{-s} = \zeta(s)$ and the $k$-almost-primes series
being a subseries). At $s=1$: the conditional convergence of $\sum_{n: \Omega(n)=k} 1/n$
is subtle (it actually diverges for all $k$, like $\sum_p 1/p$). But $1/(n \ln n)$ decays
faster than $1/n$, so:

$\sum_{n: \Omega(n)=k} 1/(n \ln n)$ converges for $k=1$ (primes, verified numerically to
$\approx 1.637$) and should converge for $k \geq 2$ as well (numerical evidence from Q2:
partial sums up to $n = 2\times10^4$ are 0.79, 0.41, 0.20 for $k=2,3,4$ and converging).

**Rate $T_k(x) \to 0$**: By PNT-type estimates, $|\{n \leq y : \Omega(n)=k\}| \sim
y (\ln\ln y)^{k-1}/((k-1)! \ln y)$, so by Abel summation:
$T_k(x) \approx \int_x^\infty \frac{(\ln\ln t)^{k-1}}{(k-1)!(\ln t)^2} \frac{dt}{t}$.
This integral converges and equals $O((\ln\ln x)^{k-1}/(\ln x))$ by substitution.
For large $x$: $T_k(x) \to 0$.

**Current obstacle**: The formal estimate is not fully rigorous (needs a careful
Selberg-Delange application to bound the error terms). The conclusion $T_k(x) \to 0$
is morally correct; a full proof requires number-theoretic input beyond the given facts.
