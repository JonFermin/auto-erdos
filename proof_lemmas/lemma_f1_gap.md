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

**What F1 gives.** By F1 (Zhang 1993), the bound $< 1.399 + o(1)$ holds for ANY primitive set in $\mathbb{N}$. The improvement needed is from the constant 1.399 to 1, with the gain coming from the $x \to \infty$ restriction.

**Intuition for why the bound should tighten.** When $A \subset [x, \infty)$ for large $x$, each element satisfies $a \geq x$, so $1/(a \log a) \leq 1/(x \log x)$. The total sum is $|A| / (x \log x)$ at most. For this to be $> 1$, we'd need $|A| > x \log x$. But a primitive set in $[x, 2x]$ has at most $\sim x$ elements (antichain bound), contributing $\sim 1/\log x \to 0$. Summing across $[2^j x, 2^{j+1} x]$ for $j = 0, 1, 2, \ldots$ gives a telescoping series bounded above by a constant depending on $x$ that shrinks to 0.

**Why this naive bound is not tight enough.** The above argument gives an upper bound of $O(1/\log x)$ for each "interval contribution," but summing over all intervals gives $O(1)$ or worse. More care is needed.

**Known technique: Sieve / Mertens-type estimate.** The Erdős approach and Zhang's refinement both use Mertens-type estimates. To get $< 1 + \varepsilon$, we need: for large $x$, the Mertens correction term is $< \varepsilon$.

**Current status.** Open. This lemma is the core of the conjecture and likely requires techniques beyond the given facts (F1, F2, F3). Closing it would be a significant mathematical result. Current approaches: (1) sharpening Zhang's sieve; (2) using F3's exact asymptotic to do a stratum-by-stratum analysis.
