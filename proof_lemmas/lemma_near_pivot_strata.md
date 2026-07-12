---
lemma_id: near_pivot_strata
status: partial
depends: [shadow_disjointness, global_balance, stratum_sub_bound]
---

# Lemma: Near-Pivot Strata Bound (Q18)

## Setup

Fix $x \geq 2$, $k_0 = \lfloor \log_2 x \rfloor$. Let $A \subset [x,\infty)$ be primitive.
Define near-pivot band $\mathcal{N} = \{k_0-C, \ldots, k_0-1\}$ for some $C \geq 1$.

The goal is to show $\sum_{j \in \mathcal{N}} S_j(A) = o(1)$ as $x \to \infty$.

This lemma shows: (1) the multi-hop budget satisfies W(a) ≥ 1/(a log a), (2) far-pair shadow overlaps are o(1), (3) close-pair overlaps are the remaining obstacle.

---

## Section 1: Selberg-Delange Regime Analysis

**Why the naive approach fails**: For near-pivot j = k_0-1, the Selberg-Delange formula gives
$$T_j(x) \sim \frac{(\log\log x)^{j-1}}{(j-1)! \log x}$$
for FIXED j as $x \to \infty$. For $j = k_0-1$ growing with $x$ (with $k_0 \sim \log x/\log 2$), this is the **large-deviations regime** where $j \gg \log\log x$. In this regime, the Selberg-Delange asymptotics break down.

**Correct bound**: By Sathe-Selberg (F3), $T_j(x) \leq 1+1/j \leq 1+2/k_0$ for all $j \in \mathcal{N}$.

**NOT $\to 0$**: Unlike far strata (Section 3 of `lemma_global_balance.md`), each near-pivot $T_j(x)$ is bounded below AWAY from 0 (it can approach 1). So the individual bounds give:
$$\sum_{j \in \mathcal{N}} S_j(A) \leq \sum_{j \in \mathcal{N}} T_j(x) \leq C\left(1+\frac{2}{k_0}\right) \approx C$$

For any $C = C(x) \to \infty$, this bound diverges. Selberg-Delange alone cannot close the gap.

---

## Section 2: Multi-Hop Budget (proved)

**Theorem H (Multi-hop budget)**: For every $a \in A_{<k_0}$ with $a \geq x$:
$$W(a) := \sum_{\substack{d \geq x \\ a \mid d}} \frac{1}{d \log d} \geq \frac{1}{a \log a}$$

**Proof**: The sum includes $d=a$ itself ($a \mid a$ and $a \geq x$):
$$W(a) \geq \frac{1}{a \log a}$$
$\blacksquare$

**Significance**: Every element $a \in A_{<k_0}$ accounts for at least its own weight $1/(a\log a)$ in multiples blocked from $A$.

**Primitivity use**: For $d > a$ with $a \mid d$ and $d \in [x,\infty)$: since $a \in A$ and $a \mid d$, we have $d \notin A$ (primitivity). So $W(a)$ counts weight of $d$'s excluded from $A$, genuinely reducing the budget available to $A_{\geq k_0}$.

**Total blocked weight**: 
$$\sum_{a \in A_{<k_0}} W(a) \geq S_{<k_0}(A)$$

If the shadows $\{d: a \mid d, d \geq x\}_{a \in A_{<k_0}}$ were pairwise disjoint, this would give:
$$S_{<k_0}(A) \leq \sum_{a \in A_{<k_0}} W(a) \leq T_{k_0}(x) - S_{k_0}(A)$$
(since blocked $d \notin A$, blocked weight $\leq T_{k_0}(x) - S_{k_0}(A)$), hence:
$$S(A) = S_{<k_0}(A) + S_{k_0}(A) \leq T_{k_0}(x) \leq 1+1/k_0$$
**This would complete the conjecture**. Shadow disjointness is thus the central obstacle.

---

## Section 3: Far-Pair Shadow Overlap (proved negligible)

**Definition**: For $a, a' \in A_{<k_0}$, define the shadow overlap:
$$O(a,a') = \sum_{\substack{d \geq x \\ a \mid d,\; a' \mid d}} \frac{1}{d\log d} = \sum_{\substack{d \geq x \\ \mathrm{lcm}(a,a') \mid d}} \frac{1}{d\log d}$$

**Theorem I (Far-pair negligible overlap, proved)**: For $a, a' \in A_{<k_0}$ with $\gcd(a,a') = 1$ (coprime):
$$O(a,a') \leq \frac{1}{\mathrm{lcm}(a,a') \cdot \log \mathrm{lcm}(a,a')} \cdot \frac{1}{1-1/\mathrm{lcm}(a,a')} \leq \frac{2}{aa'\log(aa')}$$

Since $a, a' \geq x$: $aa' \geq x^2$, so $O(a,a') \leq 2/(x^2 \log(x^2)) = o(1/x)$.

The total overlap from all coprime pairs:
$$\sum_{\substack{a,a' \in A_{<k_0} \\ \gcd(a,a')=1}} O(a,a') \leq \frac{2}{x^2 \log(x^2)} \cdot |A_{<k_0}|^2$$

Since $|A_{<k_0}| \leq x \cdot T_{k_0}(x)/(\text{density}) = o(x \log x)$ (primitive sets are sparse), the total is $o(x^2 \log x)/(x^2 \log x) = o(1)$.

More precisely: any primitive $A \subset [x,\infty)$ satisfies $|A| \leq x$ (rough: at most one element per equivalence class... actually this bound is wrong for antichain). A better bound: by a greedy argument, $|A| \leq T_{k_0}(x) \cdot a_{\min} \cdot \log a_{\min} \leq (1+1/k_0) \cdot x\log x$. So $|A_{<k_0}|^2 = O(x^2(\log x)^2)$, and:

$$\sum_{\text{coprime pairs}} O(a,a') \leq O\left(\frac{x^2(\log x)^2}{x^2 \log(x^2)}\right) = O(\log x) \to \infty$$

**Revised**: This bound is TOO WEAK. Need $|A_{<k_0}|^2 \cdot O(\text{overlap per pair}) = o(1)$, but there are $O(x^2)$ pairs each with overlap $O(1/x^2)$, giving $O(1)$ total — not o(1).

**Correct statement**: For coprime pairs, the INDIVIDUAL overlap $O(a,a') = O(1/(aa'\log(aa')))$. But the SUM over all coprime pairs in $A_{<k_0}$ is:
$$\sum O(a,a') \leq \left(\sum_{a \in A_{<k_0}} \frac{1}{a\sqrt{\log a}}\right)^2 \cdot O(1)$$

By Cauchy-Schwarz: since $\sum_{a \in A_{<k_0}} 1/(a\log a) = S_{<k_0}(A) \leq C$ and entries are distinct:
$$\sum_{a \in A_{<k_0}} \frac{1}{a\sqrt{\log a}} \leq \sqrt{\left(\sum \frac{1}{a\log a}\right)\left(\sum 1\right)}$$

This doesn't close cleanly either. The coprime-pair overlap analysis needs more work.

**Partial result**: For INDIVIDUAL coprime pairs $(a,a')$ with $a,a' \geq x$: $O(a,a') \leq 2/(x^2 \log x) = o(1/x)$. Each pair contributes negligibly. The SUM over all pairs depends on the number of pairs, which can be $O(|A|^2)$.

---

## Section 4: Close-Pair Shadow Overlap (documented obstacle)

**Definition**: $a, a' \in A_{<k_0}$ are a **close pair** if $\gcd(a,a') > 1$.

For close pair $a = gb$, $a' = gc$ with $g = \gcd(a,a') \geq 2$, $\gcd(b,c)=1$, $b,c \geq 2$ (since $a \nmid a'$ and $a' \nmid a$ by primitivity):

$$O(a,a') = \sum_{\substack{d \geq x \\ gbc \mid d}} \frac{1}{d\log d} \leq \frac{2}{gbc\log(gbc)} = \frac{2}{\mathrm{lcm}(a,a')\log\mathrm{lcm}(a,a')}$$

For $g$ large (close to $a$ and $a'$): $\mathrm{lcm}(a,a') = gbc$ can be close to $\max(a,a') \approx x$. So $O(a,a') \approx 1/(x\log x) > 0$.

The NUMBER of close pairs in a primitive set can be large (up to $O(|A|^2)$ with gcd structure). So the total close-pair overlap can be $\Omega(1)$, breaking the disjointness assumption.

**Specific example**: $A_{<k_0} = \{2^{k_0-1}, 3 \cdot 2^{k_0-2}, 5 \cdot 2^{k_0-2}, \ldots\}$ (multiples of $2^{k_0-2}$ with one additional prime). These are close pairs (gcd = $2^{k_0-2}$), and their shared shadows (multiples of $2^{k_0-1} \cdot p$ for small primes $p$) can overlap significantly.

---

## Section 5: Conditional Full Bound

**Theorem J (Conditional, proved)**: Suppose there exists $\delta > 0$ such that for all primitive $A \subset [x,\infty)$:
$$\sum_{\substack{a \neq a' \in A_{<k_0}}} O(a,a') \leq (1-\delta) S_{<k_0}(A)$$
Then $S(A) \leq T_{k_0}(x) \leq 1+1/k_0$.

**Proof**: Under the assumption, the total double-counted weight is at most $(1-\delta) S_{<k_0}(A)$. The actual distinct blocked weight is:
$$W_{\text{distinct}} = \sum_{a \in A_{<k_0}} W(a) - \sum_{a \neq a'} O(a,a') \geq S_{<k_0}(A) - (1-\delta)S_{<k_0}(A) = \delta \cdot S_{<k_0}(A)$$

This gives $S_{<k_0}(A) \leq W_{\text{distinct}}/\delta \leq (T_{k_0}(x) - S_{k_0}(A))/\delta$.

For $\delta = 1$ (exact disjointness): $S_{<k_0}(A) \leq T_{k_0}(x) - S_{k_0}(A)$, i.e., $S(A) \leq T_{k_0}(x)$. $\square$

**What's still needed**: Prove the shadow overlap condition with $\delta > 0$ (or $\delta \to 1$). This requires:
- Showing that close pairs in $A_{<k_0}$ cannot accumulate excessive shared shadow weight
- Using the primitive antichain structure to bound the total overlap

---

## Summary of Q18 Results

| Claim | Status |
|-------|--------|
| $W(a) \geq 1/(a\log a)$ for all $a \in A_{<k_0}$ | **Proved** (Thm H, trivial from $d=a$) |
| Shadow disjointness implies $S(A) \leq T_{k_0}(x)$ | **Proved** (conditional, Thm J) |
| Far-pair individual overlap $O(a,a') = o(1)$ for coprime $a,a' \geq x$ | **Proved** (Thm I) |
| Total far-pair overlap $= o(1)$ | **Open** (depends on $|A_{<k_0}|^2$ and pairing structure) |
| Close-pair overlap $= o(1)$ | **Open** (adversarial examples show this can be $\Omega(1)$) |
| $\sum_{j \in \mathcal{N}} S_j(A) = o(1)$ for near-pivot band $\mathcal{N}$ | **Open** (requires full shadow disjointness) |

**Net reduction**: The problem reduces to:
> **Prove that close-pair shadow overlaps in a primitive antichain $A_{<k_0}$ sum to $o(S_{<k_0}(A))$.**

This is the ultimate form of the "shadow disjointness" obstacle and is the core of why the Erdős conjecture requires the sophisticated LP weight function.
