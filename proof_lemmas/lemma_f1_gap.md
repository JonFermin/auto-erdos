---
id: f1_gap
status: open
depends_on: [cross_stratum_sum]
discharged_by_round: null
introduced_at_round: 4
---

# Lemma f1_gap: Closing the gap from F1 (1.399) to the conjectured bound (1)

**Statement.** For any primitive set $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$
where $o(1) \to 0$ as $x \to \infty$.

---

## What F1 gives and the gap to close

By F1 (Zhang 1993), for ANY primitive $A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < 1.399 + o(1).$$

The improvement from $1.399$ to $1$ is the open gap. The restriction $A \subset [x, \infty)$ should help because large $x$ forces each term $1/(a \log a) \leq 1/(x \log x) \to 0$; the question is whether this "small-term" effect can be parlayed into a global bound.

---

## Partial result: Dyadic decomposition upper bound (OPEN — gap in argument)

Partition $A$ by dyadic intervals: $A = \bigsqcup_{j \geq 0} A^{(j)}$ where $A^{(j)} = A \cap [2^j x, 2^{j+1} x)$.

For elements in dyadic block $j$:
$$\sum_{a \in A^{(j)}} \frac{1}{a \log a} \leq \frac{|A^{(j)}|}{2^j x \cdot \log(2^j x)}.$$

Since every subset of $[N, 2N)$ is a primitive set (no element in $[N, 2N)$ divides another, because $b/a \in (1, 2)$ for $N \leq a < b < 2N$, which is never an integer), the primitivity constraint does NOT restrict $|A^{(j)}|$ within a single dyadic block. We only have $|A^{(j)}| \leq 2^j x$.

Substituting: the contribution from block $j$ is at most
$$\frac{2^j x}{2^j x \cdot \log(2^j x)} = \frac{1}{\log(2^j x)} = \frac{1}{\log x + j \log 2}.$$

Summing over $j \geq 0$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{j \geq 0} \frac{1}{\log x + j \log 2}.$$

This sum DIVERGES (it is a harmonic-type series). So the dyadic decomposition with the trivial antichain bound is too crude.

**The failure mode.** The triviality that every subset of $[N, 2N)$ is primitive means the antichain constraint contributes nothing within a single dyadic interval. The primitivity must be used ACROSS dyadic intervals to limit the total density.

---

## Approach: Cross-interval primitivity constraint

When $a \in A^{(j)}$ and $b \in A^{(j')}$ with $j' > j$, primitivity requires $a \nmid b$. This cross-interval constraint means: fixing $a \in A^{(j)}$, the elements $b = 2a, 3a, \ldots$ are excluded from $A$. How many elements does this eliminate?

For $a \in [2^j x, 2^{j+1} x)$ and $b \in [2^{j'} x, 2^{j'+1} x)$ with $b = ma$ (integer $m \geq 2$):
- $m \approx 2^{j'-j}$, so multiples $ma$ with $m \in [2^{j'-j}, 2^{j'-j+1})$ land in block $j'$.
- There are $\sim 2^j x$ elements in $A^{(j)}$, each excluding $\sim 1$ multiple per block $j' > j$.

The total number of "exclusions" from all $a \in A^{(j)}$ in block $j'$ is at most $|A^{(j)}|$ (since each $a$ excludes at most one multiple in $[2^{j'} x, 2^{j'+1} x)$ per specific multiple $m$). This argument limits $|A^{(j')}|$ based on $|A^{(j)}|$, but turning this into a quantitative bound on the sum requires a recursive estimate — which is exactly the sieve approach used by Erdős and Zhang.

---

## Connection to F1 proof structure

Zhang's proof of the $1.399$ bound proceeds by:
1. Bounding $\sum_{a \in A} f(a)$ by a product over prime factors of elements in $A$.
2. Using Mertens' theorem to bound the prime product by $e^{\gamma} \pi/4 \approx 1.399$.

The improvement from $1.399$ to $1 + o(1)$ with the $x$-restriction would require:
- Showing that for $A \subset [x, \infty)$, the "prime product" in Zhang's argument is bounded by $1 + C/\log x$, not $1.399$.
- This would follow if the small-prime contributions to the product vanish when $A \subset [x, \infty)$ — but small primes ($p < x$) can still divide elements of $A$ even when $A \subset [x, \infty)$.

**Fundamental obstacle.** An element $a \in A$ with $a \geq x$ can have a prime factor $p = 2$ (e.g., $a = 2m$ for any large $m$). Thus the restriction $A \subset [x, \infty)$ does NOT prevent small primes from appearing as factors. The sieve argument is not straightforwardly improved by the $x$-restriction.

---

## Alternative approach: Smooth number filtering

One approach to improve F1: restrict to elements of $A$ with ALL prime factors $\geq y$ for some threshold $y = y(x)$.

- For $a \in A$ with smallest prime factor $p(a) \geq y$: each such $a \geq y^k$ for $k$-almost-primes, so elements are spread more sparsely.
- For $a \in A$ with $p(a) < y$: these are $y$-smooth-above elements; their contribution can be bounded using the $y$-smooth number counting function.

This decomposition (rough-part / smooth-part) is used in analytic number theory to sharpen sieve bounds. Whether it can push the constant below $1.399$ when $A \subset [x, \infty)$ is an open question — it would require the smooth-part contribution to be $o(1)$ and the rough-part to be $\leq 1 + o(1)$.

---

## Status summary

| Sub-claim | Status | Follows from |
|-----------|--------|--------------|
| Sum < 1.399 for any primitive $A \subset [x, \infty)$ | **Proved** | F1 |
| Dyadic decomposition gives finite bound | **Partial** — bound diverges without cross-interval constraint | — |
| Cross-interval primitivity limits total density | **Plausible** — requires sieve/product argument | Qualitative, not proved |
| Sum < $1 + o(1)$ via smooth-number decomposition | **Open** — approach outlined but not closed | Requires new estimate |
| Full lemma f1_gap: sum < $1 + o(1)$ | **Open** | The conjecture itself |
