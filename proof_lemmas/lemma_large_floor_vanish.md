---
id: large_floor_vanish
status: proved
depends_on: [stratum_sub_bound]
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma: per-stratum contribution vanishes as x → ∞

**Statement**: For each fixed $k \geq 1$,
$$T_k(x) := \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n}
  \to 0 \quad \text{as } x \to \infty.$$

**Proof**:

The series $\sum_{n \geq 2, \Omega(n)=k} 1/(n \log n)$ converges to a finite value
$T_k(2) < \infty$ for every fixed $k \geq 1$: the count of $k$-almost primes $\leq N$
is $O(N(\log\log N)^{k-1}/\log N)$, so the sum is bounded by comparison with a
convergent series. (By F3, $T_k(2) \to 1$ from below as $k \to \infty$; for small
fixed $k$, $T_k(2)$ is a definite positive constant that may exceed 1.)

For any convergent series $\sum_{n} a_n$ with $a_n \geq 0$, the tail sum
$\sum_{n \geq N} a_n \to 0$ as $N \to \infty$ (this is a standard consequence
of absolute convergence: the partial sums form a Cauchy sequence).

Here the "terms" are indexed by $n$ ranging over $k$-almost primes, and
$a_n = 1/(n \log n) > 0$. As $x \to \infty$, $T_k(x)$ is the tail of the
convergent series from $x$, hence $T_k(x) \to 0$. $\square$

**Corollary**: For any fixed $K \geq 1$ and any primitive set $A \subset [x,\infty)$,
$$\sum_{k=1}^{K} \sum_{\substack{a \in A \\ \Omega(a)=k}} \frac{1}{a \log a}
  \leq \sum_{k=1}^K T_k(x) \to 0 \quad (x \to \infty).$$

Each term $T_k(x) \to 0$ by the lemma (convergent sum, tail vanishes). The
finite sum of $K$ such terms also vanishes.

**Notes**:
- This lemma shows that the "low-stratum" contribution ($k \leq K$ for any
  fixed $K$) is $o(1)$ as $x \to \infty$.
- It does NOT help with "high strata" ($k \to \infty$ as $x \to \infty$), where
  the constraint $n \geq x$ bites less and the per-stratum sum stays close to 1.
- For $k > \log_2 x$, the smallest $k$-almost prime is $2^k > x$, so $T_k(x) =
  T_k(2)$ (no lower cutoff effect). By F3 (asymptotic as $k \to \infty$),
  $T_k(2) \to 1$ from below, so the sum approaches 1 as $k \to \infty$. The
  "high-stratum" regime ($k \sim \log_2 x$) is the hard part; see
  `lemma_cross_stratum_control.md`.
