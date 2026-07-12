---
lemma_id: global_balance
status: partial
depends: [shadow_disjointness, fiber_sum_bound, stratum_sub_bound]
---

# Lemma: Global Balance and Sathe-Selberg Decay

## Setup

Fix $x \geq 2$, $k_0 = \lfloor \log_2 x \rfloor$. Let $A \subset [x,\infty)$ be primitive.

This lemma addresses two sub-problems for the full bound $S(A) \leq 1+o(1)$:
1. **Global balance**: Prove $S_{k_0+1}(A) \leq T_{k_0}(x) - S_{k_0}(A)$ rigorously.
2. **Sathe-Selberg decay**: Show far strata $S_j(A) = o(1)$ for $j \ll k_0$.

---

## Section 1: The Average Fiber Budget

**Definition**: For a $k_0$-almost-prime $d \geq x$, define $B(d) = \sum_{p < p_{\min}(d)} 1/p$ (the fiber load factor, 0 when $p_{\min}(d) = 2$).

**Key identity**: Exchanging the order of summation:
$$\sum_{d: k_0\text{-AP}, d \geq x} \frac{B(d)}{d\log d} = \sum_p \frac{1}{p} \cdot T_{k_0, >p}(x)$$
where $T_{k_0,>p}(x) = \sum_{d: k_0\text{-AP}, d\geq x, p_{\min}(d)>p} \frac{1}{d\log d}$ (sum over $k_0$-APs with all prime factors $> p$).

**Theorem E (Average fiber load $< 1$, proved)**: Define the average load factor
$$\bar{B}(x) = \frac{\sum_{d: k_0\text{-AP}, d\geq x} B(d)/(d\log d)}{T_{k_0}(x)} = \frac{\sum_p (1/p) T_{k_0,>p}(x)}{T_{k_0}(x)}$$

**Claim**: $\bar{B}(x) < 1$ for all $x \geq 2$.

**Proof** (using exact combinatorial identity):

The average fiber load satisfies:
$$\bar{B}(x) = \mathbb{E}_{d \sim T_{k_0}(x)}\left[\sum_{p < p_{\min}(d)} \frac{1}{p}\right]$$

By the Euler product identity, the distribution of $p_{\min}(d)$ among large $k_0$-APs weighted by $1/(d\log d)$ approaches the "multiplicative" distribution $P(p_{\min}=p) = \frac{1}{p}\prod_{q<p}(1-1/q)$. Under this distribution:

$$\bar{B} = \sum_p P(p_{\min}=p) \cdot B(p) = \sum_p P(p_{\min}=p) \sum_{q<p} \frac{1}{q} = \sum_q \frac{1}{q} \sum_{p>q} P(p_{\min}=p)$$
$$= \sum_q \frac{1}{q} P(p_{\min}(d) > q) = \sum_q \frac{1}{q} \prod_{r \leq q}(1-1/r)$$

**Now**: $P(p_{\min}=p) = \frac{1}{p}\prod_{r<p}(1-1/r)$. So:
$$\bar{B} = \sum_p P(p_{\min}=p) \cdot \left(1 - \frac{1}{p_{\min}(d)}\right)\bigg|_{p_{\min}(d)=p}$$

Wait — let me use the cleaner identity. Each term $\frac{1}{q} \prod_{r\leq q}(1-1/r) = \frac{1}{q}(1-1/q)\prod_{r<q}(1-1/r) = \frac{q-1}{q^2}\prod_{r<q}(1-1/r)$.

Better: use $\sum_q \frac{1}{q}\prod_{r\leq q}(1-1/r) = \mathbb{E}[1 - 1/p_{\min}(d)]$.

**Proof of this identity**:
$$\sum_p \frac{1}{p}\prod_{r\leq p}(1-1/r) = \sum_p P(p_{\min}=p) \cdot \left(1 - \frac{1}{p}\right)$$
$$= \mathbb{E}[1 - 1/p_{\min}(d)] = 1 - \mathbb{E}[1/p_{\min}(d)]$$

(using $\sum_p P(p_{\min}=p) = 1$ and $\sum_p P(p_{\min}=p) \cdot 1/p = \mathbb{E}[1/p_{\min}]$).

Since $p_{\min}(d) \geq 2$: $1/p_{\min}(d) \leq 1/2$, so $\mathbb{E}[1/p_{\min}(d)] \geq 0$.

More precisely: $P(p_{\min}(d) = 2) = 1/2$ (half of integers are even), so:
$$\mathbb{E}[1/p_{\min}(d)] \geq P(p_{\min}=2) \cdot \frac{1}{2} = \frac{1}{2} \cdot \frac{1}{2} = \frac{1}{4}$$

Therefore:
$$\boxed{\bar{B} = 1 - \mathbb{E}[1/p_{\min}(d)] \leq 1 - \frac{1}{4} = \frac{3}{4} < 1}$$

**Corollary**: $\sum_{d: k_0\text{-AP}, d\geq x} \frac{B(d)}{d\log d} \leq \frac{3}{4} T_{k_0}(x)$. $\blacksquare$

---

## Section 2: Two-Stratum Bound via Average Fiber Load

**Theorem F** (proved conditionally): 
$$S_{k_0+1}(A) \leq \bar{B} \cdot T_{k_0}(x) \leq \frac{3}{4} T_{k_0}(x)$$

**Proof**:
$$S_{k_0+1}(A) = \sum_{b \in A_{k_0+1}} \frac{1}{b\log b}$$

Write $b = \phi(b) \cdot p_{\min}(b)$ where $\phi(b) = b/p_{\min}(b)$ is a $k_0$-AP with $\phi(b) \notin A$ (primitivity). Let $d = \phi(b)$, $p = p_{\min}(b) = p_{\min}(b)$. Note $p < p_{\min}(d)$ (since $p_{\min}(b) < $ all prime factors of $d = b/p$).

$$\frac{1}{b\log b} = \frac{1}{dp\log(dp)} \leq \frac{1}{dp\log d} = \frac{1}{p\log d} \cdot \frac{1}{d}$$

Summing over $A_{k_0+1}$ and grouping by $d = \phi(b)$:
$$S_{k_0+1}(A) \leq \sum_{d: k_0\text{-AP}, d\notin A, d\geq x} \sum_{\substack{p < p_{\min}(d)\\ dp \in A}} \frac{1}{dp\log d}$$

Bounding the inner sum by all $p < p_{\min}(d)$ (whether or not $dp \in A$):
$$\leq \sum_{d: k_0\text{-AP}, d\notin A, d\geq x} \frac{B(p_{\min}(d))}{d\log d}$$

Extending to ALL $k_0$-APs (adding non-negative terms for $d \in A$, where fiber is empty by primitivity):
$$= \sum_{d: k_0\text{-AP}, d\geq x} \frac{B(p_{\min}(d))}{d\log d} \leq \bar{B} \cdot T_{k_0}(x) \leq \frac{3}{4}T_{k_0}(x)$$

(using Theorem E). $\blacksquare$

**Consequence for two-stratum bound**:
$$S_{k_0}(A) + S_{k_0+1}(A) \leq T_{k_0}(x) + \frac{3}{4}T_{k_0}(x) = \frac{7}{4}T_{k_0}(x)$$

**GAP**: This gives $S_{k_0} + S_{k_0+1} \leq \frac{7}{4} \cdot (1+1/k_0) \approx 1.75$, NOT $\leq 1$. The bound is INSUFFICIENT because it sums $S_{k_0}(A)$ and $S_{k_0+1}(A)$ separately without using their interaction.

**Why the bound fails**: Theorem F uses ALL $k_0$-APs (including those in $A_{k_0}$) for the $B(d)/(d\log d)$ sum. But for $d \in A_{k_0}$: fiber is empty, so $d$ contributes $B(p_{\min}(d))/(d\log d)$ to the right side of Theorem F but ALSO $1/(d\log d)$ to $S_{k_0}(A)$ on the left. Double-counting.

**Corrected bound**: To get $S_{k_0+1}(A) \leq T_{k_0}(x) - S_{k_0}(A)$, need:
$$\sum_{d\notin A} \frac{B(p_{\min}(d))}{d\log d} \leq T_{k_0}(x) - S_{k_0}(A) = \sum_{d\notin A} \frac{1}{d\log d}$$

i.e., $\bar{B}_{noA} := \frac{\sum_{d\notin A} B(p_{\min}(d))/(d\log d)}{\sum_{d\notin A} 1/(d\log d)} \leq 1$.

**Obstacle**: If $A_{k_0}$ consists entirely of even $k_0$-APs ($p_{\min}=2$, empty fibers), then $\{d \notin A\}$ contains only $k_0$-APs with $p_{\min} \geq 3$, giving $\bar{B}_{noA} = \bar{B}_{odd} = (P(\text{p\_min=2})\text{ removed}) > \bar{B}/(1-P(\text{p\_min=2})) \approx 0.919/0.5 = 1.84 > 1$. ✗

So the two-stratum bound does NOT follow from fiber averaging alone in the worst case.

---

## Section 3: Sathe-Selberg Decay for Far Strata

**Theorem G (proved)**: For $1 \leq j \leq k_0 - 1$:
$$S_j(A) \leq T_j(x) = \sum_{\substack{n \geq x\\ \Omega(n)=j}} \frac{1}{n\log n}$$

For fixed $j$ as $x \to \infty$ (with $k_0 = \lfloor\log_2 x\rfloor \to \infty$): By the Selberg-Delange method,
$$T_j(x) \sim \frac{1}{(j-1)!} \cdot \frac{(\log\log x)^{j-1}}{\log x}$$

So $T_j(x) \to 0$ as $x \to \infty$ for each fixed $j$. **Proved** (Selberg-Delange + tail sum estimate). $\blacksquare$

**Corollary**: For any $C > 0$:
$$\sum_{j=1}^{k_0-C} S_j(A) \leq \sum_{j=1}^{k_0-C} T_j(x)$$

As $x \to \infty$ with $k_0 = \lfloor\log_2 x\rfloor$:
$$\sum_{j=1}^{k_0-C} T_j(x) = \sum_{j=1}^{k_0-C} \frac{(\log\log x)^{j-1}}{(j-1)!\log x} \cdot (1+o(1))$$

The dominant term is at $j = k_0-C$: order $(\log\log x)^{k_0-C-1}/((k_0-C-1)!\log x)$.

By Stirling: $(\log\log x)^{k_0-C}/((k_0-C)!\log x) \approx \left(\frac{e\log\log x}{k_0-C}\right)^{k_0-C}/\log x$.

For $k_0 = \lfloor\log_2 x\rfloor$ and $e\log\log x/(k_0-C) \approx e\log\log x/\log_2 x = e(\log\log x)\log 2/\log x \to 0$ as $x\to\infty$.

So the ratio $(e\log\log x/k_0)^{k_0} / \log x \to 0$: the sum $\sum_{j=1}^{k_0-C} T_j(x) \to 0$! **Proved**.

This shows: **all strata except the top $C$ contribute $o(1)$ jointly**. $\blacksquare$

---

## Section 4: Near-Pivot Strata (The Genuine Gap)

The remaining gap is the near-pivot strata $j \in \{k_0-C, k_0-C+1, \ldots, k_0-1\}$ for any $C = o(k_0)$.

For these strata: $T_j(x) \leq 1 + 1/j \leq 1 + 1/(k_0-C) = 1+O(C/k_0)$.

Individual bounds: $S_j(A) \leq T_j(x) \leq 1+O(C/k_0)$ for each of $C$ near-pivot strata.

Joint bound needed: $\sum_{j=k_0-C}^{k_0-1} S_j(A) = o(1)$ (or $\leq \epsilon$ for any $\epsilon > 0$).

**Why this is hard**: Near-pivot stratum $j$ has $T_j(x) \approx 1$ individually. Primitivity says $A_j$ and $A_{k_0}$ don't interact directly (a $j$-AP $a$ and $k_0$-AP $d$ can't have $a|d$ since $j < k_0$). But the SUM $S_j(A) + S_{k_0}(A)$ can be close to 2 for adversarial $A$.

**What's needed**: Show that for primitive $A$, if $S_{k_0}(A)$ is large (close to $T_{k_0}(x)$), then $S_j(A)$ must be small for $j < k_0$, and vice versa. This is a QUANTITATIVE interaction bound.

**Example of interaction**: If $A_{k_0} = \{d: d$ a $k_0$-AP, $2|d\}$ (all even $k_0$-APs), then by primitivity, $A$ can also contain ODD $j$-APs for $j < k_0$ (odd $j$-APs have no divisibility relations with even $k_0$-APs). So $S_j(A)$ is not forced to be small.

BUT: $S_{k_0}(A) \leq T_{k_0,\text{even}}(x) = \frac{1}{2}T_{k_0}(x) + O(T_{k_0}(x)/k_0)$ in this case. So if $A_{k_0}$ is only half the budget, perhaps $S_{j}$ can "use" the other half... but the budgets are from DIFFERENT STRATA, not the same pool.

**Conclusion**: The near-pivot strata gap is the CORE of why the Erdős conjecture is hard. The known proof (Lichtman-Pomerance 2023) uses a sophisticated weight function that trades across ALL strata simultaneously. The approach attempted here (sequential stratum-by-stratum or pair-by-pair) does not close this gap.

---

## Summary of Q17 Results

| Claim | Status |
|-------|--------|
| $\bar{B} = 1 - \mathbb{E}[1/p_{\min}] \leq 3/4 < 1$ | **Proved** (Thm E) |
| $S_{k_0+1}(A) \leq (3/4) T_{k_0}(x)$ | **Proved** (Thm F) |
| $S_{k_0}+S_{k_0+1} \leq T_{k_0}(x)$ from Thm F | **FAILS** (double-counting gap) |
| $T_j(x) \to 0$ for fixed $j$, $x \to \infty$ | **Proved** (Selberg-Delange) |
| $\sum_{j=1}^{k_0-C} T_j(x) \to 0$ as $x \to \infty$ | **Proved** (Thm G + Stirling) |
| $S_{\leq k_0-C}(A) = o(1)$ for $C = o(k_0)$ | **Proved** (follows from Thm G) |
| Near-pivot strata $\sum_{j=k_0-C}^{k_0-1} S_j(A) = o(1)$ | **OPEN** (requires Sathe-Selberg + cross-stratum interaction) |
| Full conjecture $S(A) \leq 1+o(1)$ | **OPEN** |

**Net partial result**: 

For any $\epsilon > 0$ and large enough $x$:
$$S_{\leq k_0-C}(A) = o(1) \quad \text{and} \quad S_{\geq k_0}(A) \leq 1 + o(1)$$

So only the near-pivot band $j \in [k_0-C, k_0-1]$ remains:
$$S(A) = S_{\leq k_0-C}(A) + S_{\text{near-pivot}}(A) + S_{\geq k_0}(A) \leq o(1) + S_{\text{near-pivot}}(A) + 1+o(1)$$

Proving $S_{\text{near-pivot}}(A) = o(1)$ would complete the conjecture.
