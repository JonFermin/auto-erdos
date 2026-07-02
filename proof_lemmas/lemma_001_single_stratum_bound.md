---
id: single_stratum_bound
status: proved
depends_on: []
discharged_by_round: 4
introduced_at_round: 4
---

# Lemma 1 (single_stratum_bound): Each stratum contributes strictly less than 1

## Statement

For any primitive set $A \subseteq [x, \infty)$ and any $k \geq 1$, let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$. Then
$$\sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k} < 1,$$
where $c \approx 0.0656 > 0$ and the $o(1)$ is as $k \to \infty$.

## Proof

**Step 1 (monotonicity).** $A \cap A_k \subseteq A_k$ as a set. Since every term $1/(a \log a) > 0$, we have
$$\sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a}.$$

**Step 2 (F3 exact asymptotic).** By **F3**, $\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))k^2/2^k$ with $c \approx 0.0656 > 0$.

**Step 3 (negative correction).** Since $c > 0$ and $k^2/2^k > 0$ for all $k \geq 1$, the correction $(c+o(1))k^2/2^k$ is positive for all sufficiently large $k$ (and for all $k \geq 1$ as asserted by F3's sign disambiguation). Therefore $1 - (c+o(1))k^2/2^k < 1$.

Combining Steps 1–3: $\sum_{a \in A \cap A_k} 1/(a \log a) < 1$ for every $k \geq 1$. $\square$

## Remark

This lemma is **easy** — it follows immediately from F3 and monotonicity. The hard step is combining these per-stratum bounds across all strata $k \geq 1$ (see Lemma `cross_stratum_bound`), since $\sum_{k \geq 1} 1 = \infty$ and the per-stratum bounds alone do not sum to a finite limit.
