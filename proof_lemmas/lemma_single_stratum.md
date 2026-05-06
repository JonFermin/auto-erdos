---
id: single_stratum
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 4
---

# Lemma `single_stratum` — Per-stratum tail bound for elements in $[x, \infty)$

**Statement**: For each $k \geq 1$ and $x \geq 2$, let $B \subseteq \{n \geq x : \Omega(n) = k\}$
be any set of integers (necessarily primitive, since equal-$\Omega$ elements cannot divide
each other unless equal). Then

$$\sum_{b \in B} \frac{1}{b \log b} \leq g(k, x),$$

where $g(k, x) \to 0$ as $x \to \infty$ for each fixed $k$.

## Current approach (using F3)

**Step 1**: Since $B \subseteq \{n : \Omega(n) = k\}$, we have the inclusion

$$\sum_{b \in B} \frac{1}{b \log b} \leq \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n}.$$

**Step 2**: By F3, the full series $\sum_{n : \Omega(n) = k} 1/(n \log n)$ converges to
$1 - (c + o(1)) k^2/2^k$ as $k \to \infty$, with $c \approx 0.0656 > 0$. For each fixed
$k$, this is a finite value, which means the series converges. Consequently, the tail
$\sum_{n \geq x, \Omega(n) = k} 1/(n \log n)$ is a tail of a convergent series and
$g(k, x) \to 0$ as $x \to \infty$ for each fixed $k$.

## Obstacle: summing over all $k$

The qualitative bound $g(k, x) \to 0$ (fixed $k$, $x \to \infty$) does not directly
give $\sum_{k \geq 1} g(k, x) \leq 1 + o(1)$. For fixed $x$, summing over all $k$
accumulates contributions from all strata. F1 (Erdős-Zhang) gives the master bound
$\sum_k g(k,x) < 1.399 + o(1)$ as $x \to \infty$, but not the sharper $1 + o(1)$.

The crux: controlling the total across all strata by $1 + o(1)$ instead of $1.399 + o(1)$
requires exploiting the inter-stratum primitive constraint (Lemma `cross_stratum`) or
the extremality of primes (Lemma `primes_extremal`). Both remain open.

## Status

Open. The per-stratum qualitative bound ($g(k,x) \to 0$ for fixed $k$) is established
by F3. The quantitative bound summing over all $k$ to give $\leq 1 + o(1)$ is the
open core of the conjecture.
