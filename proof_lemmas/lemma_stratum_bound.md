---
id: stratum_bound
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 5
---

# Lemma: Single-stratum bound

**Statement.** Let $k \geq 1$ and $x \geq 2$. Let $B \subseteq \{n \geq x : \Omega(n) = k\}$
be a primitive set (no element divides another). Then

$$\sum_{b \in B} \frac{1}{b \log b} \leq \sigma_k(x)$$

where $\sigma_k(x) := \sum_{n \geq x, \Omega(n) = k} \frac{1}{n \log n}$
denotes the full sum over the $k$-th stratum starting at $x$.

**Proof sketch.** Since $B$ is a subset of all integers with $\Omega(n) = k$ and
$n \geq x$, and each term $1/(b \log b) > 0$, the sum over $B$ is bounded
above by the sum over the full stratum. $\square$

**Discussion.**

This bound is trivial (subset sums are bounded by whole-set sums). Its
value lies in the estimate of $\sigma_k(x)$, which by F3 (under the
scope interpretation in Section 2) is:

$$\sigma_k(x) \sim (1 - c k^2/2^k) \cdot \frac{1}{\log x} \quad (x \to \infty)$$

with $c \approx 0.0656$. In particular $\sigma_k(x) < 1/\log x$ for all
$k \geq 1$ and all $x$, and $\sigma_k(x) \to 0$ as $x \to \infty$.

**Obstacle.** The sum of bounds over all strata,
$\sum_{k=1}^{\infty} \sigma_k(x)$, diverges (the strata partition the integers,
so $\sum_k \sigma_k(x) = \sum_{n \geq x} 1/(n \log n) = \infty$).
Simply summing per-stratum bounds does NOT give a useful global bound —
the cross-stratum constraint (Lemma `cross_stratum_constraint`) must be
used to prune the sum.
