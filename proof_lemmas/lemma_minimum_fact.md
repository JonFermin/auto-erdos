---
id: minimum_fact
status: open
depends_on: [octave_bound]
discharged_by_round: null
introduced_at_round: 6
---

# Lemma: Minimum necessary fact for the conjecture (Q13)

## What this lemma is

The octave bound (`lemma_octave_bound.md`) shows each octave $[2^j x, 2^{j+1} x]$
contributes at most $2 / (j \log 2 + \log x) \to 0$. Summing over all $j \geq 0$
diverges. This lemma identifies what additional fact would close the gap.

## The minimum necessary fact (Fact X)

**Fact X (conjectural, not in ledger):** For any primitive set $A \subseteq [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a} = O(\log x) \quad \text{as } x \to \infty,$$
where the implicit constant is absolute (independent of $A$).

If Fact X holds, then since $1/(a \log a) = (1/\log a) \cdot (1/a) \leq (1/\log x) \cdot (1/a)$
for all $a \geq x$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{1}{\log x} \sum_{a \in A} \frac{1}{a}
= \frac{O(\log x)}{\log x} = O(1).$$

For the tighter form $\sum_{a \in A} 1/a \leq (1 + o(1)) \log x$, the bound becomes
$\sum 1/(a \log a) \leq 1 + o(1)$, which IS the conjecture.

## Why Fact X is plausible

For the specific case $A = \{n : n \in [x, 2x]\} \cap \text{primes}$:
By the prime number theorem (not in ledger), $\sum_{p \in [x, 2x]} 1/p \approx \log\log(2x) - \log\log(x) \approx \frac{\log 2}{\log x}$,
which is $o(\log x)$, consistent with Fact X (in fact, much smaller).

For denser primitive sets like squarefree numbers in $[x, 2x]$: there are $\approx x(1 - 1/2)(1 - 1/3) \cdots \approx x/\log x$ squarefree numbers in $[x, 2x]$, but squarefree numbers do NOT form a primitive set (6 | 30, for instance).

## Why Fact X is not derivable from F1, F2, F3

- F1 bounds $\sum 1/(a \log a) \leq 1.399$ but says nothing about $\sum 1/a$.
- F2 is a lower bound on a stratum sum; irrelevant for bounding $\sum 1/a$.
- F3 gives the full $A_k$ sum, not a density statement about $\sum 1/a$.

None of F1/F2/F3 are density results for primitive sets. Fact X is a density result.

## Cross-octave exclusion as an alternative path

Instead of Fact X, the conjecture might be provable via a cross-octave exclusion principle:
if $a \in A \cap [2^j x, 2^{j+1} x]$, then all multiples $ka$ are excluded from later
octaves. If $A$ is "dense" in octave $j$, it is "sparse" in octaves $j+1, j+2, \ldots$
because many multiples are excluded.

**Precise form (speculative):** If octave $j$ contributes $S_j$ to the sum, then
the exclusion principle implies octaves $j+1, j+2, \ldots$ contribute at most
$C(1 - S_j)$ in total for some universal constant $C$.

Formalizing this exclusion principle requires knowing the density of multiples
of elements in a primitive set — another statement not explicitly in the ledger.

**Status:** open — the minimum necessary fact is identified; whether it is provable
from the given ledger is unknown. This remains the central open question.
