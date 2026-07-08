---
id: prime_extremality
status: open
depends_on: [stratum_bound]
discharged_by_round: null
introduced_at_round: 1
---

# Lemma 2: Prime extremality (the hard lemma)

**Statement.** For any primitive set $A \subseteq [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p}.$$

**Significance.** This is the core of the Erdős primitive set conjecture. Combined
with Lemma 2 (prime sum asymptotics), it gives the full conjecture: the sum over any
primitive $A \subseteq [x, \infty)$ is bounded by $(1+o(1))/\log x \to 0$.

**Known proof strategy (not reproduced here; see Section 7 for elementary partial progress).**

1. **Smallest-prime-factor partition.** For each prime $p$, let
   $A_p = \{a \in A : p(a) = p\}$ where $p(a)$ is the smallest prime factor of $a$.
   Since $A \subseteq [x, \infty)$, elements with $p < x$ can appear but the total sum
   is still bounded (floor-matching argument).

2. **Per-prime bound (open in this loop):**
   $$\sum_{a \in A_p} \frac{1}{a \log a} \;\leq\; \frac{1}{p \log p}.$$
   Cases 1–2 are proved in Section 7 (singleton or single-element case).
   The general multi-element case requires a Dirichlet series comparison for primitive
   sets with fixed smallest prime factor — a hard mathematical step not formalized here.

3. **Summation.** Summing over all $p$ yields the full bound (assuming Step 2 holds).

**Status: open (partial).** Cases 1–2 of Step 2 proved (Section 7). Case 3 (general
multi-element) is the remaining hard gap. This lemma is **not proved in this proof attempt**.
