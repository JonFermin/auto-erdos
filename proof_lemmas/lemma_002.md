---
id: strat_cross_k_bound
status: open
depends_on: [strat_per_k_bound]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 2 — Cross-Stratum Interaction (OPEN)

**Statement (conjecture)**: Let $x \geq 2$ and $A \subseteq [x, \infty)$ be a primitive set
spanning multiple $\Omega$-strata. Then:
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o_x(1)$$
where $o_x(1) \to 0$ as $x \to \infty$.

**Why this requires primitivity**:

The naive stratum-sum bound $\sum_k \sum_{a \in A \cap A_k} 1/(a \log a) \leq \sum_k \text{tail}_k(x)$
equals $\sum_{n \geq x} 1/(n \log n)$, which diverges as $n \to \infty$ for fixed $x$. So the
infinite sum over all strata is useless. Primitivity is essential.

**Primitivity constraint across strata**: If $a \in A \cap A_j$ and $b \in A \cap A_k$ with
$j < k$, then $a \nmid b$ (otherwise $A$ is not primitive). This means:
- Each prime $p \in A$ (stratum $k=1$) excludes all its prime-power multiples $pq, pqr, \ldots$
  from $A$.
- More generally: any element in a lower stratum "shadows" (excludes) many elements in higher strata.

**What's known (from F1)**:

Fact F1 gives a bound of $1.399 + o(1)$ for any primitive $A \subseteq [x, \infty)$. This
uses primitivity in a deep way (Davenport-Erdős / Beurling-Nyman type argument). F1 is a
proven upper bound, but it does not tighten to 1 as $x \to \infty$; it holds uniformly for
all $x$.

**Gap to close**: The conjecture requires tightening F1 from $1.399$ to $1 + o_x(1)$.
The $x$-dependence is the key: for large $x$, elements of $A$ are large, making individual
terms $1/(a \log a)$ small, but there could be many of them.

**Candidate approach** (partial, not yet closed):

Let $K(x) = \lfloor \log \log x \rfloor$ be the "typical" stratum near $x$ (most integers $n$
near $x$ have $\Omega(n) \approx \log \log x$). Decompose:
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \leq K(x)} \underbrace{\sum_{a \in A \cap A_k} \frac{1}{a\log a}}_{\text{low-stratum contribution}} + \sum_{k > K(x)} \underbrace{\sum_{a \in A \cap A_k} \frac{1}{a\log a}}_{\text{high-stratum contribution}}$$

**Low-stratum part** ($k \leq K(x) = O(\log \log x)$): Each such $k$-stratum contributes
$\leq \text{tail}_k(x)$ (by Lemma 1). For primitive $A$, elements from stratum $k$ with small $k$
are "far apart" (no two can be comparable in the divisibility order), but bounding the SUM
requires more than just per-stratum estimates.

**High-stratum part** ($k > K(x)$): Elements with $k > K(x)$ prime factors are "super-smooth"
numbers near $x$. The number of such elements $\leq N$ with $\Omega(n) = k$ is roughly
$N (\log \log N)^{k-1} / ((k-1)! \log N)$, which for $k \gg \log \log N$ is extremely small.
So this part is negligible.

**Obstacle**: The low-stratum part requires bounding $\sum_{k=1}^{K(x)} \text{tail}_k(x)$ for
a PRIMITIVE $A$, not just any set. A simple estimate gives $\sum_{k=1}^{K(x)} \text{tail}_k(x)$
as the sum over integers $n \geq x$ with $\Omega(n) \leq K(x)$, which may still be $> 1$.
The primitivity constraint must further restrict which $k$-tuples $(A \cap A_1, A \cap A_2, \ldots)$
are simultaneously realizable.

**Current status**: Open. The single-stratum lemma (Lemma 1) proves the $k$-fixed case.
The cross-stratum case requires a Davenport-Erdős type argument beyond F1/F2/F3 alone.
A complete proof would likely either:
1. Use the Banks-Martin / Lichtman result that primes MAXIMIZE $f$ over primitive sets
   (which would immediately give the result since $\sum_{p \geq x} 1/(p\log p) \to 0$), or
2. Derive the cross-stratum bound directly via Dirichlet series methods.
