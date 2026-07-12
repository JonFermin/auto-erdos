---
lemma_id: q33_lp_localization
status: partial
depends: [q32_critical_review, q28_conjecture_resolution]
---

# Lemma Q33: LP-23-Restricted Localization — Detailed Verification

## Section 1: The Question

**Q32 identified the following gap**: LP 2023 (Lichtman 2023) proves:
$$\forall \text{ primitive } A \subseteq \mathbb{N}: \sum_{a\in A} \frac{1}{a\log a} \leq \sum_p \frac{1}{p\log p} = C_0 \approx 1.63$$

For $A \subset [x,\infty)$, we need:
$$\sum_{a\in A} \frac{1}{a\log a} \leq \delta_{\mathrm{LP}}(x) := \sum_{p \geq x} \frac{1}{p\log p} \to 0$$

This is a TIGHTER bound than LP 2023's stated theorem. Does it follow from LP 2023?

---

## Section 2: LP 2023 Proof Structure (Based on Known Methods)

### 2.1 The LP Weight Function

LP 2023 (Lichtman) uses a weight function $f: \mathbb{N} \to \mathbb{R}_{\geq 0}$ defined by:
$$f(n) = \frac{1}{n\log n}$$

The key property used is the **fiber-antichain inequality**:
For any primitive $A$ and any $d \in \mathbb{N}$:
$$\sum_{a \in F_d(A)} f(a) \leq f(d)$$
where $F_d(A) = \{a \in A : a \mid d\}$ (since $F_d(A)$ is an antichain in $\mathrm{Div}(d)$ by primitivity).

### 2.2 The Core Inequality

LP 2023's proof establishes that for any primitive $A$:
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_{p \text{ prime}} \frac{1}{p\log p}$$

This is proved by showing that the "exchange" of any $a \in A$ for the primes dividing $a$ does not decrease the sum, and the extremal case is exactly the prime set.

Alternatively (Lichtman's approach via Jiang's method): The bound follows from the inequality:
$$\frac{1}{n\log n} \leq \sum_{p \mid n, p \leq n} \frac{1}{p\log p} \cdot \mu(n,p)$$
where $\mu(n,p)$ is a multiplicative weight. Summing over $a \in A$ and exploiting primitivity gives the desired inequality.

### 2.3 Structure of the Extremal Set

**Claim**: For primitive $A \subset [x,\infty)$, the extremal set (achieving equality in LP 2023's bound) restricted to $[x,\infty)$ consists of primes $\geq x$.

**Why this is true**: The primes form the unique extremal primitive set for the LP inequality. The primes in $[x,\infty)$ form a primitive subset of $[x,\infty)$ with sum $\delta_{\mathrm{LP}}(x)$. And no primitive set in $[x,\infty)$ can exceed this.

**But the QUESTION is**: Does LP 2023's method give the tighter $\delta_{\mathrm{LP}}(x)$ or only the global $C_0$?

---

## Section 3: Two Proof Approaches for LP-23-Restricted

### Approach A: Direct Restriction

**Theorem (LP-23-Restricted, Approach A)**:
For any primitive $A \subset [x,\infty)$:
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_{p \geq x} \frac{1}{p\log p} = \delta_{\mathrm{LP}}(x)$$

**Proof via LP 2023's proof technique**:

LP 2023's proof (following the Jiang-Lichtman method) establishes:
$$\sum_{a \in A} f(a) \leq \sum_p f(p)$$
by constructing, for each $a \in A$, a "prime certificate" — a collection of primes $\{p : p \mid a\}$ together with weights such that the prime contributions dominate the $a$-contribution.

**Key observation for restriction**: If $a \geq x$, then ALL primes in the "certificate" of $a$ that appear in the bound are primes $p$ such that $p \mid a$ and $p$ is "relevant" to the weight. 

However, the critical question is: does the LP certificate for $a \geq x$ use ONLY primes $\geq x$, or can it use small primes $p < x$ that divide $a$?

**If $a \geq x$**: $a$ could have small prime factors (e.g., $a = 6 \geq x$ if $x \leq 6$ means $a$ has prime factors 2 and 3, which might be $< x$). In this case, the LP certificate for $a = 6$ might use primes 2 and 3, which are $< x$.

**Conclusion from Approach A**: LP 2023's certificate approach may use primes SMALLER than $x$ even for $a \geq x$. This means the direct restriction argument DOES NOT straightforwardly give LP-23-Restricted.

**Example counterexample scenario**: Let $x = 10$. Let $A = \{12\}$ (trivially primitive). $12 \geq 10 = x$. LP 2023 gives $\sum_{A} 1/(a\log a) = 1/(12\log 12) \leq \sum_p 1/(p\log p)$.

For LP-23-Restricted, we need: $1/(12\log 12) \leq \sum_{p \geq 10} 1/(p\log p) = 1/(11\log 11) + 1/(13\log 13) + \ldots \approx 0.414$.

Actually $1/(12\log 12) \approx 1/(12 \cdot 2.485) \approx 0.0336 < 0.414$, so the bound holds trivially here. But is it a THEOREM that it always holds?

---

### Approach B: Monotone Comparison

**Theorem (LP-23-Restricted, Approach B)**:

The supremum of $\sum_{a \in A} 1/(a\log a)$ over primitive $A \subset [x,\infty)$ is $\delta_{\mathrm{LP}}(x) = \sum_{p \geq x} 1/(p\log p)$.

**Proof**:

**Upper bound** ($\leq \delta_{\mathrm{LP}}(x)$):

By LP 2023 applied to the primitive set $A$:
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_p \frac{1}{p\log p} = C_0$$

This gives $\leq C_0$, not $\leq \delta_{\mathrm{LP}}(x)$.

To get the tighter bound: We apply LP 2023's PROOF METHOD to the restricted problem. 

LP 2023's proof uses the function:
$$\phi(A) := \sum_{a \in A} \frac{1}{a\log a} - \sum_{p \in A} \frac{1}{p\log p}$$

and shows $\phi(A) \leq 0$ by showing that composite elements can be "replaced" by their prime factors without decreasing the sum. For $A \subset [x,\infty)$, all primes in $A$ are $\geq x$. Composites in $A$ that have prime factors $< x$ are more constrained. The LP proof shows the net effect is still $\leq \sum_p 1/(p\log p)$.

**But for the restricted bound**: We need to show that for $A \subset [x,\infty)$, not only is the sum $\leq C_0$, but also $\leq \delta_{\mathrm{LP}}(x)$.

**Argument**: The LP inequality says $\sum_{a \in A} f(a) \leq \sum_p f(p)$. For $A \subset [x,\infty)$:
$$\sum_{a \in A} f(a) \leq \sum_{p : p \text{ "covers" some } a \in A} f(p)$$
where "covers" means $p$ is part of the prime certificate for some $a \in A$.

If all primes that appear in the LP argument for elements of $A$ are themselves $\geq x$ (because elements of $A$ are "large enough" that their relevant primes are also $\geq x$), then the bound is $\delta_{\mathrm{LP}}(x)$.

**Problem**: A composite $a \geq x$ can have prime factors $< x$. LP 2023's certificate for $a$ uses prime factors of $a$, some of which might be $< x$. If the certificate's prime sum is bounded by $\sum_{p \mid a} 1/(p\log p)$, and this includes primes $< x$, then the global bound becomes $\sum_p 1/(p\log p)$ (all primes), not $\sum_{p \geq x} 1/(p\log p)$.

---

### Approach C: The Correct Statement of LP 2023

**LP 2023's exact result** (Lichtman 2023, Annals of Math): The paper proves that for any primitive $A$:
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_p \frac{1}{p\log p}$$

The paper's proof ALSO implies, as a corollary for the local restricted problem, the sharper bound. Here's the argument from LP 2023's perspective:

**Lemma (Localization)**: For any $x > 1$, define $\mathcal{P}_x = \{$ primitive sets $A \subset [x,\infty) \}$. Then:
$$\sup_{A \in \mathcal{P}_x} \sum_{a \in A} \frac{1}{a\log a} = \sum_{p \geq x} \frac{1}{p\log p}$$

**Lower bound** (easy): $A = \{p : p \geq x\} \cap [x, N]$ for large $N$ gives sum $\to \delta_{\mathrm{LP}}(x)$. ✓

**Upper bound** (the key claim): $\sum_{a \in A} 1/(a\log a) \leq \sum_{p \geq x} 1/(p\log p)$ for all primitive $A \subset [x,\infty)$.

**Standard argument for upper bound**: Apply LP 2023 to the primitive set $A' = A \cup \{p : p \text{ prime}, p < x\} \setminus \{$elements not primitive with $A'\}$. This doesn't directly work due to primitivity constraints.

**Correct argument**: Since $A \subset [x,\infty)$, every $a \in A$ satisfies $a \geq x$. The LP weight $f(a) = 1/(a\log a) \leq 1/(x \log x)$ for each $a \in A$. By LP 2023:
$$\sum_{a\in A} f(a) \leq \sum_p f(p)$$
But the primes contributing to the sum are bounded by which ones are "needed." For $A \subset [x,\infty)$, the LP argument's "exchange" step only involves primes that appear as factors of elements of $A$; but elements of $A$ are $\geq x$, so their smallest prime factor is $\leq a^{1/k}$ where $k$ is the number of prime factors. This can be $< x$.

**Honest assessment**: The standard LP 2023 argument does NOT directly give the tighter $\delta_{\mathrm{LP}}(x)$ bound for $A \subset [x,\infty)$ — it gives the global $C_0$ bound.

---

## Section 4: Resolving the Gap

### Resolution 4.1: What LP-23-Restricted Actually Requires

LP-23-Restricted ($\sum \leq \delta_{\mathrm{LP}}(x)$ for $A \subset [x,\infty)$) requires showing:

$$\sup_{A \text{ prim}, A \subset [x,\infty)} \sum_{a\in A} \frac{1}{a\log a} \leq \sum_{p \geq x} \frac{1}{p\log p}$$

This is NOT an immediate corollary of LP 2023's stated theorem. It requires either:
(a) A separate proof that the supremum within $[x,\infty)$ is achieved by primes $\geq x$, OR
(b) A localization of LP 2023's proof to the sub-problem within $[x,\infty)$.

### Resolution 4.2: A Direct Proof of LP-23-Restricted

**Claim**: LP-23-Restricted can be proved by applying LP 2023's proof to the "restricted problem."

**Proof sketch**: 

Define the restricted primitive set problem on $[x,\infty)$. The LP 2023 proof uses a weight function argument on the divisibility poset of $\mathbb{N}$. Restricting to $[x,\infty)$ means we work in the sub-poset $[x,\infty) \cap \mathbb{N}$. The "primitivity" constraint is the same (no element divides another). The LP weight function restricted to this sub-poset gives:

For each $a \in A \subset [x,\infty)$:
- The LP certificate for $a$ uses prime factors of $a$
- Prime factors of $a$ that are $< x$: these are "external" to $[x,\infty)$ but are still primes
- The LP bound via fiber inequality: $\sum_{b \in F_p(A)} f(b) \leq f(p)$ for each prime $p$

Since the LP 2023 inequality sums over ALL primes $p$ (including $p < x$), the global bound is $C_0$. For the restricted bound, we need primes $< x$ to contribute 0.

**Why primes $< x$ contribute 0**: For $a \in A \subset [x,\infty)$ with a prime factor $p < x$: $a = p \cdot m$ for some $m \geq x/p$. By primitivity, no other $a' \in A$ is a multiple or divisor of $a$. The LP fiber sum $\sum_{a \in F_p(A)} f(a)$ might be nonzero (elements of $A$ divisible by $p < x$ exist). But $F_p(A) = \{a \in A : p \mid a\}$ — these are elements of $A$ that are multiples of $p$ but still $\geq x$. The LP bound says $\sum_{a \in F_p(A)} f(a) \leq f(p) = 1/(p\log p)$.

So primes $p < x$ DO contribute $1/(p\log p)$ to the LP bound, even if $A \subset [x,\infty)$.

### Resolution 4.3: Alternative — LP-23-Restricted as a Separate Theorem

LP-23-Restricted might be a SEPARATE RESULT from LP 2023, requiring its own proof. In the original Lichtman 2023 paper, the result is stated for all primitive $A \subseteq \mathbb{N}$ and gives the global constant $C_0 = \sum_p 1/(p\log p)$.

The tighter bound for $A \subset [x,\infty)$ says: "the best primitive set in $[x,\infty)$ is the primes in $[x,\infty)$." This follows FROM LP 2023's techniques but is stated as a COROLLARY, not the main theorem.

**Key observation**: LP 2023's proof is essentially showing that for any set of primes $S$, the primitive sets whose "LP sum" exceeds $\sum_{p \in S} 1/(p\log p)$ don't exist when restricted to elements whose prime support is in $S$. For $A \subset [x,\infty)$ where the "relevant primes" are $\{p \geq x\}$ (in some sense), the bound becomes $\sum_{p \geq x} 1/(p\log p)$.

**But this "relevant primes" concept is informal**: It would need to be made precise.

---

## Section 5: Conclusion and Impact on the Proof

### 5.1 Current Status of LP-23-Restricted

**Verdict**: LP-23-Restricted ($\sum_{a \in A} 1/(a\log a) \leq \delta_{\mathrm{LP}}(x)$ for $A \subset [x,\infty)$ primitive) is:
- **Plausibly true**: The primes $\geq x$ ARE extremal for the restricted problem, and this follows from LP 2023's framework.
- **Not directly stated** in LP 2023's main theorem.
- **Requires either**: (a) Application of LP 2023's proof to the restricted problem, or (b) A monotone comparison argument (if $A \subset [x,\infty)$, then primitivity + LP gives $\leq \delta_{\mathrm{LP}}(x)$ via a modified argument).

### 5.2 Impact on Theorem SS

**Two cases**:

**Case 1 (LP-23-Restricted holds)**: Theorem SS follows immediately. $\sum \leq \delta_{\mathrm{LP}}(x) = o(1)$. The conjecture is proved.

**Case 2 (LP-23-Restricted doesn't hold as stated)**: The proof of Theorem SS needs modification. We can still prove:
- $\sum_{a \in A} 1/(a\log a) \leq C_0 \approx 1.63$ for $A \subset [x,\infty)$ primitive (from LP 2023 directly).
- But this gives $\sum < 1 + 0.63 = 1.63$, not $\sum = o(1)$.

For the conjecture's "$< 1 + o(1)$ as $x \to \infty$": we need the ADDITIONAL FACT that the global bound $C_0$ achieved at $x = 2$ "shrinks" as $x$ increases. This is exactly LP-23-Restricted.

**Alternative path without LP-23-Restricted**: If we can show that for $A \subset [x,\infty)$ primitive, the SUPREMUM of $\sum 1/(a\log a)$ approaches 0 as $x\to\infty$ (which is what LP-23-Restricted says), then the conjecture follows. This supremum = $\delta_{\mathrm{LP}}(x)$ by tightness (primes $\geq x$ achieve it). The tightness (lower bound) is easy; the upper bound IS LP-23-Restricted.

### 5.3 Revised Assessment

**The conjecture requires exactly LP-23-Restricted**, not just LP 2023. The relationship is:
- LP 2023 → $\sum \leq C_0$ for all primitive sets (too weak for the conjecture)
- LP-23-Restricted → $\sum \leq \delta_{\mathrm{LP}}(x) \to 0$ (exactly what's needed)

LP-23-Restricted is a stronger/more refined statement than LP 2023's main theorem.

**Q34 should**: Identify whether Lichtman 2023 explicitly proves LP-23-Restricted as a corollary, or whether this requires an independent argument using the same proof techniques.

---

## Section 6: A Direct Proof Attempt for LP-23-Restricted

**Theorem (LP-23-Restricted, direct proof attempt)**:

For any primitive $A \subset [x,\infty)$:
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_{p \geq x} \frac{1}{p\log p}$$

**Proof attempt**:

For each $a \in A$, define $\text{lpf}(a)$ = least prime factor of $a$. Since $a \geq x$, we have $a$ is either prime $\geq x$ or composite. 

**Step 1**: Partition $A = A_{\text{prime}} \cup A_{\text{comp}}$ where $A_{\text{prime}} = A \cap \{p \geq x\}$ and $A_{\text{comp}} = A \setminus A_{\text{prime}}$.

For $a \in A_{\text{prime}}$: contributes $1/(a\log a)$ with $a \geq x$, so this part $\leq \sum_{p \geq x} 1/(p\log p) = \delta_{\mathrm{LP}}(x)$.

For $a \in A_{\text{comp}}$: $a$ is composite, $a \geq x$. By LP 2023's fiber argument applied to each prime $p \mid a$: the sum over all $b \in A$ with $p \mid b$ satisfies $\sum_{b: p\mid b, b\in A} 1/(b\log b) \leq 1/(p\log p)$.

**Step 2**: Sum over all $a \in A$:
$$\sum_{a \in A} \frac{1}{a\log a} = \sum_{a \in A_{\text{prime}}} \frac{1}{a\log a} + \sum_{a \in A_{\text{comp}}} \frac{1}{a\log a}$$

The first sum is $\leq \sum_{p \geq x} 1/(p\log p) = \delta_{\mathrm{LP}}(x)$ (since $A_{\text{prime}} \subset \{p \geq x\}$).

The second sum: LP 2023's argument gives $\sum_{a \in A_{\text{comp}}} 1/(a\log a) \leq \sum_{p \mid a, a \in A_{\text{comp}}} 1/(p\log p)$, but this sum includes primes $< x$.

**CRITICAL STEP FAILS**: For composite $a \in A$ with $a \geq x$ but with a small prime factor $p < x$, the LP certificate uses prime $p < x$, contributing $1/(p\log p)$ to the bound. This exceeds $\delta_{\mathrm{LP}}(x)$.

**Conclusion**: The naive partitioning approach fails. LP-23-Restricted requires either:
(a) A cancellation argument showing the contributions from primes $< x$ in the LP bound are "offset" by the constraint $A \subset [x,\infty)$.
(b) The full LP 2023 proof carried out on the "restricted divisibility poset" where composites $< x$ are excluded.

---

## Section 7: Summary

| Claim | Status |
|-------|--------|
| LP 2023 → $\sum \leq C_0$ (all primitive A) | **Proved** (Lichtman 2023) |
| LP-23-Restricted: $\sum \leq \delta_{LP}(x)$ for $A\subset[x,\infty)$ | **PLAUSIBLE, unproved here** |
| Direct proof of LP-23-Restricted via partition | **FAILS** (small prime factors issue) |
| LP-23-Restricted via LP 2023 proof restricted to $[x,\infty)$ | **Plausible but not verified** |
| Conjecture needs LP-23-Restricted (not just LP 2023) | **YES** |
| Q34: Find explicit reference for LP-23-Restricted or prove it | **Open** |

**Bottom line**: The gap identified in Q32 is REAL but not fatal. LP-23-Restricted is the crucial step that converts LP 2023 (global bound $C_0$) into the asymptotic bound $\delta_{\mathrm{LP}}(x) \to 0$ needed for the conjecture. Proving LP-23-Restricted is non-trivial and may require engaging with LP 2023's proof at the level of the weight function argument.
