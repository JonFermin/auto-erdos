---
id: cross_stratum_sum
status: open
depends_on: [stratum_bound]
discharged_by_round: null
introduced_at_round: 4
---

# Lemma cross_stratum_sum: Total sum across all strata

**Statement.** For any primitive set $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A \cap A_k} \frac{1}{a \log a} < 1 + o(1)$$
as $x \to \infty$.

---

## Partial result 1: F1 gives the bound with constant 1.399 (PROVED from given facts)

By F1 (Zhang 1993, in the given-facts ledger), for ANY primitive set $A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

In particular, for $A \subset [x, \infty)$, the cross-stratum sum is bounded above by $1.399 + o(1)$.
This is a **proved partial result** from the given facts; the gap to the conjectured constant $1$ is what remains open.

---

## Partial result 2: Tail argument shows low-$k$ strata vanish as $x \to \infty$ (PROVED from F3)

**Claim.** For any fixed $K \geq 1$:
$$\sum_{k=1}^{K} \sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{k=1}^{K} \sum_{\substack{a \in A_k \\ a \geq x}} \frac{1}{a \log a} = o(1) \quad \text{as } x \to \infty.$$

**Proof.** By F3, for each $k \geq 1$ the full stratum sum converges:
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} < \infty.$$

Since $A \cap A_k \subseteq A_k \cap [x, \infty)$, the contribution from stratum $k$ is at most the tail
$$T_k(x) := \sum_{\substack{a \in A_k \\ a \geq x}} \frac{1}{a \log a}.$$

Because $\sum_{a \in A_k} 1/(a \log a)$ is a convergent series of positive terms, its tail $T_k(x) \to 0$ as $x \to \infty$ for each fixed $k$. Summing over finitely many strata $k = 1, \ldots, K$:
$$\sum_{k=1}^{K} \sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{k=1}^{K} T_k(x) \to 0 \quad \text{as } x \to \infty. \qquad \square$$

**Limitation.** $K$ must remain fixed. The argument does not control the sum over ALL strata simultaneously because $\sum_{k \geq 1} 1 = \infty$ — the bound $T_k(x) \leq 1$ (from F3) is too crude when summing over all $k$.

---

## The core obstacle: controlling the high-$k$ tail (OPEN)

Split the sum at threshold $K = K(x)$:
$$\sum_{a \in A} \frac{1}{a \log a} = \underbrace{\sum_{k=1}^{K} \sum_{a \in A \cap A_k} f(a)}_{=\, o(1) \text{ by Partial result 2}} + \underbrace{\sum_{k > K} \sum_{a \in A \cap A_k} f(a)}_{\text{high-}k \text{ contribution}}.$$

For the high-$k$ contribution, note that for $k > \lfloor \log_2 x \rfloor$, every $k$-almost-prime satisfies $a \geq 2^k > x$ (since $a$ has at least $k$ prime factors, each $\geq 2$, so $a \geq 2^k$). Thus the tail restriction $a \geq x$ is automatic for $k > \log_2 x$. Using the stratum bound from Lemma stratum_bound:
$$\sum_{k > K} \sum_{a \in A \cap A_k} f(a) \leq \sum_{k > K} \left(1 - (c+o(1))\frac{k^2}{2^k}\right).$$

However, $\sum_{k > K} 1$ diverges, so this bound is useless. The primitive-set constraint (that $A$ is an antichain) must be invoked to show that $A$ cannot simultaneously use a large fraction of EVERY high-$k$ stratum.

**Key question (OPEN).** Does the primitive-set constraint force
$$\sum_{k > K} \sum_{a \in A \cap A_k} f(a) < 1 - o(1)?$$
Equivalently, is it impossible for a primitive $A \subset [x, \infty)$ to simultaneously take a large fraction of each high-$k$ stratum while keeping the total sum from diverging?

---

## Approach 3: F1 bound with restricted support (most promising)

Since F1 gives $\sum_{a \in A} f(a) < 1.399$ for any primitive $A$, and Partial result 2 shows low-$k$ strata contribute $o(1)$, we can write:
$$\sum_{a \in A} f(a) = \underbrace{\sum_{k=1}^{K} \sum_{a \in A \cap A_k} f(a)}_{\leq \, o_K(1)} + \underbrace{\sum_{k > K} \sum_{a \in A \cap A_k} f(a)}_{\leq 1.399 - o_K(1)},$$
where $o_K(1) \to 0$ as $x \to \infty$ for fixed $K$. This shows the high-$k$ contribution is bounded away from $1.399$ by the low-$k$ tail, but still doesn't give a bound below $1.399 + \epsilon$ for the total.

To close the gap to $1 + o(1)$, one would need to show the high-$k$ sum is bounded by $1 - \delta(x)$ for some $\delta(x) \to 0.399$ as $x \to \infty$. This requires a new analytic argument using the primitive-set structure, which is not available from F1/F2/F3 alone.

---

## Status summary

| Sub-claim | Status | Follows from |
|-----------|--------|--------------|
| Cross-stratum sum < 1.399 | **Proved** | F1 directly |
| Low-k strata ($k \leq K$ fixed) contribute $o(1)$ as $x \to \infty$ | **Proved** | F3 (stratum sums converge) |
| High-k strata bounded by primitive antichain constraint | **Open** | Requires new argument beyond F1/F2/F3 |
| Full bound < $1 + o(1)$ | **Open** | The conjecture itself |
