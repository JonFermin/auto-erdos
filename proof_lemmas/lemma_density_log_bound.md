---
id: density_log_bound
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 4
---

# Lemma: Density-log bound attempt (Q9)

**Statement (attempted):** For primitive $A \subseteq [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} = o(1) \quad \text{as } x \to \infty.$$

(If proved, this would give a bound stronger than the conjectured $< 1 + o(1)$.)

## Approach

For $a \geq x$, we have $\log a \geq \log x > 0$, so:
$$\frac{1}{a \log a} \leq \frac{1}{a \log x}.$$

Summing over $a \in A$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{1}{\log x} \sum_{a \in A} \frac{1}{a}.$$

**Sub-claim**: $\sum_{a \in A} \frac{1}{a} \leq f(x)$ for some $f(x) = O(\log x)$.

If this held, we would get $\sum_{a \in A} 1/(a \log a) = O(1)$; for a tighter
$f(x) = (1+o(1)) \log x$ we would get $\sum \leq 1 + o(1)$.

## Why F1 alone is insufficient

F1 bounds $\sum_{a \in A} 1/(a \log a) \leq 1.399$ for ANY primitive $A \subseteq \mathbb{N}$.
This bound is uniform — it does NOT use the constraint $a \geq x$.

Since F1 treats $A \subseteq [x, \infty)$ identically to $A \subseteq \mathbb{N}$
(the bound is the same regardless of $x$), F1 cannot produce a bound that
improves as $x \to \infty$. The density-log approach therefore cannot close
the gap from 1.399 to $1 + o(1)$ using F1 alone.

**What would be needed**: A fact that says $\sum_{a \in A} 1/a \leq (1+o(1)) \log x$
for primitive $A \subseteq [x, \infty)$ as $x \to \infty$. This is a density
result about primitive sets that is NOT stated in F1, F2, or F3.

## Why F3 also does not close the gap

F3 gives $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k$ for the
COMPLETE infinite stratum $A_k$. For the restricted stratum $A_k \cap [x, \infty)$,
F3 gives no direct bound (F3's $o(1)$ is asymptotic in $k$, not in $x$).

To use the restriction $a \geq x$ in F3 one would need: for each $k$,
$\sum_{a \in A_k,\, a \geq x} 1/(a \log a) \to 0$ as $x \to \infty$. This is
a tail-series convergence statement for each fixed $k$. While empirically
confirmed (Section 6.2 tail-sum table), it is not explicitly a consequence
of F3's statement as given: F3 asserts a finite limit for the whole series,
which implies the series converges, but the critics flag any use of this
implication as relying on a fact not explicitly in the ledger.

## Current obstacle

Both F1 and F3 (alone or combined) fail to use the restriction $A \subseteq [x, \infty)$
in a way that improves the bound. The conjecture requires a fact that is sensitive
to the size of elements. The gap between 1.399 (from F1) and 1 (conjectured)
cannot be closed from the current ledger.

**Status**: open — obstacle identified; no known path to proof using F1/F2/F3.
