---
id: dense_antichain
status: proved
depends_on: []
discharged_by_round: 4
introduced_at_round: 4
---

# Lemma 1: Dense Antichain Bound for $[x, 2x)$

## Statement

For any pairwise non-divisible (primitive) set $S \subset [x, 2x)$ with $x \geq 2$,
$$\sum_{s \in S} \frac{1}{s \log s} \leq \sum_{n=x}^{2x-1} \frac{1}{n \log n} \leq \frac{\log 2}{\log x} + O\!\left(\frac{1}{(\log x)^2}\right).$$

## Proof

**Part 1: $S \subset [x, 2x)$ implies $S$ contributes at most $\sum_{n=x}^{2x-1} 1/(n \log n)$.**

Since $S \subset [x, 2x)$ is finite (as $1/(n \log n) > 0$), and each $s \in S$ satisfies
$x \leq s \leq 2x - 1$, we have trivially:
$$\sum_{s \in S} \frac{1}{s \log s} \leq \sum_{n=x}^{2x-1} \frac{1}{n \log n}.$$
Equality holds iff $S$ contains every integer in $[x, 2x)$. Note that all integers in $[x, 2x)$
are indeed pairwise non-divisible: if $a, b \in [x, 2x)$ with $a \neq b$ and $a \mid b$, then
$b \geq 2a \geq 2x$, contradicting $b < 2x$. So the maximum $S = \{x, x+1, \ldots, 2x-1\}$ is valid.

**Part 2: Bounding the full interval sum.**

$$\sum_{n=x}^{2x-1} \frac{1}{n \log n} = \int_x^{2x} \frac{dt}{t \log t} + O\!\left(\frac{1}{x \log x}\right)
= \bigl[\log \log t\bigr]_x^{2x} + O\!\left(\frac{1}{x \log x}\right).$$

$$= \log(\log 2x) - \log(\log x) + O\!\left(\frac{1}{x \log x}\right)
= \log\!\left(\frac{\log 2x}{\log x}\right) + O\!\left(\frac{1}{x \log x}\right).$$

For large $x$:
$$\frac{\log 2x}{\log x} = 1 + \frac{\log 2}{\log x}, \quad
\log\!\left(1 + \frac{\log 2}{\log x}\right) = \frac{\log 2}{\log x} - \frac{(\log 2)^2}{2(\log x)^2} + O\!\left(\frac{1}{(\log x)^3}\right).$$

Hence:
$$\sum_{n=x}^{2x-1} \frac{1}{n \log n} = \frac{\log 2}{\log x} + O\!\left(\frac{1}{(\log x)^2}\right). \quad \square$$

## Verified numerically

| $x$ | $\sum_{n=x}^{2x-1} 1/(n\log n)$ | $\log 2/\log x$ |
|---|---|---|
| 100 | 0.1408 | 0.1505 |
| 1000 | 0.0957 | 0.1003 |
| 10000 | 0.0726 | 0.0753 |

The asymptotic approximation overshoots the actual sum by $O(1/(\log x)^2)$, consistent with Lemma 1.

## Limitation (scope of this lemma)

Lemma 1 applies only to primitive sets **entirely within $[x, 2x)$**. The conjecture requires
bounding primitive sets in all of $[x, \infty)$, which includes elements well beyond $2x$.
Extending the bound to $[x, \infty)$ is the content of the open sub-conjecture in Lemma 2.

## Current obstacle

Lemma 1 proves that if A is restricted to $[x, 2x)$, the bound is $\log 2/\log x \to 0$.
For A spread across $[x, \infty)$: the contribution from $[x, 2x)$ is at most $\log 2/\log x$,
the contribution from $[2x, 4x)$ is at most $\log 2/\log(2x)$, and so on.
If A were "spread" so each layer contributes the maximum, the total would be:
$$\sum_{k=0}^{\infty} \frac{\log 2}{\log(2^k x)} = \log 2 \sum_{k=0}^{\infty} \frac{1}{k \log 2 + \log x}$$
which DIVERGES (harmonic-like series). This shows that Lemma 1 alone, applied layer by layer,
cannot bound the sum — the primitivity constraint across layers is essential.
The key cross-layer constraint: if $a \in A \cap [2^j x, 2^{j+1} x)$ and $b \in A \cap [2^k x, 2^{k+1} x)$
with $j < k$, then $a \nmid b$ by primitivity. This rules out many configurations but
the quantitative consequence requires a deeper argument (likely related to the proof in the
literature that primes maximize the sum).
