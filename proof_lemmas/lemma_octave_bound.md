---
id: octave_bound
status: proved
depends_on: []
discharged_by_round: 6
introduced_at_round: 6
---

# Lemma: Single-octave Erdős-weight bound (Q12)

**Statement:** For any set $A \subseteq [x, 2x]$ (primitive or not),
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{|A|}{x \log x} \leq \frac{x + 1}{x \log x}.$$
In particular, for any $A \subseteq [x, 2x]$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{2}{\log x} \to 0 \quad \text{as } x \to \infty.$$

## Proof (from basic arithmetic only)

For $a \in [x, 2x]$, we have $a \geq x > 0$ and $\log a \geq \log x > 0$ (for $x > 1$).
Therefore $a \log a \geq x \log x$, and taking reciprocals:
$$\frac{1}{a \log a} \leq \frac{1}{x \log x}.$$

Summing over all $a \in A \subseteq [x, 2x]$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{|A|}{x \log x}.$$

The number of integers in $[x, 2x]$ is at most $\lfloor 2x \rfloor - \lceil x \rceil + 1 \leq x + 1$.
Therefore $|A| \leq x + 1$, giving:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{x + 1}{x \log x} \leq \frac{2}{\log x}$$
for all $x \geq 2$.

This proof uses only: (a) $\log$ is monotone increasing, (b) counting integers in an interval.
No ledger facts (F1, F2, F3) are needed.

**Status**: proved — the proof is elementary and complete.

## Corollary

For primitive $A \subseteq [x, 2x]$: the same bound applies, since the lemma
holds for ANY set $A \subseteq [x, 2x]$, regardless of primitivity.

## Why this is insufficient for the full conjecture

The conjecture requires bounding the sum over $A \subseteq [x, \infty)$, not just
$A \subseteq [x, 2x]$. For an infinite primitive set $A = \bigcup_{j \geq 0} A_j$
where $A_j = A \cap [2^j x, 2^{j+1} x]$:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{j=0}^{\infty} \sum_{a \in A_j} \frac{1}{a \log a}
\leq \sum_{j=0}^{\infty} \frac{2}{\log(2^j x)} = \sum_{j=0}^{\infty} \frac{2}{j \log 2 + \log x}.$$

This sum DIVERGES (it is $\approx \frac{2}{\log 2} \sum_{j=1}^{\infty} \frac{1}{j} = \infty$).

So the per-octave bound alone does not close the conjecture. The primitivity constraint
across octaves (if $a \in A_j$, multiples of $a$ are excluded from $A_{j'}$ for $j' > j$)
MUST reduce the achievable sum across octaves. Quantifying this cross-octave exclusion
is the remaining obstacle; see `lemma_minimum_fact.md`.
