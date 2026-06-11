---
id: stratum_bound
status: proved
depends_on: []
discharged_by_round: 5
introduced_at_round: 4
---

# Lemma stratum_bound: Per-stratum contribution bound

**Statement.** For any primitive set $A$ and any $k \geq 1$, the stratum contribution satisfies
$$\sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} < 1.$$

**Proof sketch.** The first inequality holds because $A \cap A_k \subseteq A_k$ and all terms are positive. The equality is F3. The final $< 1$ follows from F3's sign disambiguation (c > 0, k^2/2^k > 0).

**Status note.** This lemma follows immediately from F3 and monotonicity of positive sums. The key open sub-problem is not this per-stratum bound (which is easy) but the CROSS-STRATUM SUMMATION in Lemma cross_stratum_sum.

**Why this is the easy part.** Lemma stratum_bound bounds each stratum contribution by $< 1$. But summing over all strata $k \geq 1$ gives $\sum_k < 1 = $ diverges naively — the strata are NOT disjoint in their contribution to the total. We need a coupling argument.
