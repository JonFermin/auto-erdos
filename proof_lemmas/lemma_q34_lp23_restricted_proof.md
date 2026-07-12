---
lemma_id: q34_lp23_restricted_proof
status: partial
depends: [q33_lp_localization, q32_critical_review]
---

# Lemma Q34: Proving LP-23-Restricted

## Overview

Q33 showed that LP 2023's stated theorem gives $\sum \leq C_0$ (global), not $\sum \leq \delta_{\mathrm{LP}}(x)$ (restricted). The gap arises because composite elements $a \geq x$ may have prime factors $< x$, and LP 2023's certificate for $a$ uses those small primes.

This lemma attempts three approaches to LP-23-Restricted:
1. **Monotone weight argument** — show the supremum is non-increasing in $x$
2. **Coupling argument** — map primitive sets in $[x,\infty)$ to sets involving only large primes
3. **Direct inductive approach** — use LP 2023 recursively

---

## Section 1: Approach via Monotone Supremum

**Define**: $\delta(x) := \sup \{ \sum_{a \in A} 1/(a\log a) : A \subset [x,\infty) \text{ primitive} \}$.

**Claim (LP-23-Restricted)**: $\delta(x) = \delta_{\mathrm{LP}}(x) = \sum_{p \geq x} 1/(p\log p)$.

**Lower bound (easy)**: $\delta(x) \geq \sum_{p \geq x} 1/(p\log p) = \delta_{\mathrm{LP}}(x)$ because the set of primes $\geq x$ is a primitive set in $[x,\infty)$.

**Upper bound (the hard part)**: $\delta(x) \leq \delta_{\mathrm{LP}}(x)$.

**Observation 1**: $\delta(x)$ is non-increasing in $x$ (as $x$ increases, the constraint $A \subset [x,\infty)$ gets tighter, so the supremum can only decrease or stay the same).

**Observation 2**: $\delta(x) \leq C_0 = \delta(2)$ for all $x \geq 2$ (by LP 2023 applied globally).

**Observation 3**: $\delta(x) \geq \delta_{\mathrm{LP}}(x)$ (lower bound from primes $\geq x$).

If we could show $\delta(x) \leq \delta_{\mathrm{LP}}(x)$ directly, we'd be done.

**Key insight**: The PRIMES $\geq x$ achieve the supremum within $[x,\infty)$. This is the content of LP-23-Restricted. The argument should mirror LP 2023's proof but applied locally.

---

## Section 2: The Jiang-Lichtman Exchange Argument

**LP 2023's proof strategy** (following Jiang 2022/2023 + Lichtman's completion):

Define for any $n \in \mathbb{N}$ with $n > 1$:
$$g(n) := \frac{1}{n\log n} - \sum_{p \mid n, p < n} \lambda_p(n) \cdot \frac{1}{p\log p}$$
where $\lambda_p(n) > 0$ are carefully chosen weights satisfying $\sum_{p \mid n} \lambda_p(n) = 1$ (a "convex decomposition" of $1/n\log n$ over its prime factors).

If such $\lambda_p$ exist with $g(n) \leq 0$ for all composite $n$ and $g(p) = 1/(p\log p)$ for primes, then:
$$\sum_{a \in A} \frac{1}{a\log a} = \sum_{a \in A} g(a) + \sum_{a \in A} \sum_{p \mid a} \lambda_p(a) \frac{1}{p\log p}$$

For primitive $A$: the second sum telescopes/bounds by $\sum_p 1/(p\log p)$ using the fiber-antichain property.

**For LP-23-Restricted**: If $A \subset [x,\infty)$ and the only primes that appear in the fiber sums are primes $\geq x$, then the bound is $\delta_{\mathrm{LP}}(x)$.

**The issue**: For composite $a \geq x$ with prime factor $p < x$: $p$ appears in the "certificate" of $a$. The fiber sum $\sum_{a \in A: p \mid a} f(a)$ is bounded by $f(p) = 1/(p\log p)$ (LP fiber inequality). This contributes $1/(p\log p)$ to the upper bound, where $p < x$.

So the certificate for composite elements that have small prime factors "spills out" of $[x,\infty)$.

**Resolution attempt**: The LP fiber inequality says:
$$\sum_{a \in A: p \mid a} \lambda_p(a) \cdot f(a) \leq f(p)$$

For the restricted problem, if $A \subset [x,\infty)$ and $p < x$: the sum on the left is over $a \in A$ with $a \geq x$ and $p \mid a$, so $a \geq \max(x, p) = x$ (since $p < x$). Each $a \geq x$ in this fiber satisfies $f(a) = 1/(a\log a) \leq 1/(x \log x)$. So:
$$\sum_{a \in A: p \mid a, a \geq x} \lambda_p(a) f(a) \leq f(p) = \frac{1}{p\log p}$$

And the contribution to the global bound from prime $p < x$ is at most $1/(p\log p)$. This is exactly what makes the global bound $\leq C_0 = \sum_p 1/(p\log p)$.

**Can we do better?**: If the fiber $F_p(A) = \{a \in A : p \mid a\}$ is empty for all $p < x$, then no composites with small factors are in $A$, and the bound is $\sum_{p \geq x} 1/(p\log p) = \delta_{\mathrm{LP}}(x)$.

But $F_p(A)$ might be nonempty for $p < x$ if $A$ contains composites with small prime factors!

**Concrete example**: $x = 100$, $A = \{2 \cdot 101, 3 \cdot 107\} = \{202, 321\}$.
- $A \subset [100,\infty)$ ✓
- $A$ is primitive: $\gcd(202,321) = 1$ and neither divides the other ✓
- But $202 = 2 \cdot 101$ and $321 = 3 \cdot 107$ have prime factors 2, 3 which are $< 100 = x$

In this case, the LP bound for $A$ uses primes 2 and 3 (via the fiber argument), contributing $1/(2\log 2) + 1/(3\log 3) \approx 1.025$ to the certificate — way more than $\delta_{\mathrm{LP}}(100) \approx 0.20$.

But ACTUALLY: $\sum_{a \in A} 1/(a\log a) = 1/(202\log 202) + 1/(321\log 321) \approx 0.00187 + 0.00117 \approx 0.003$, which is much less than $\delta_{\mathrm{LP}}(100) \approx 0.20$.

So the LP certificate bound is VERY LOOSE for this example. The actual sum is tiny.

**Key insight from the example**: Even though the LP certificate for composite elements uses primes $< x$, the ACTUAL sum $\sum_{a \in A} 1/(a\log a)$ for $A \subset [x,\infty)$ might still be $\leq \delta_{\mathrm{LP}}(x)$. The LP certificate is an UPPER BOUND; the tightness is achieved only by primes.

---

## Section 3: A Tightness Argument for LP-23-Restricted

**Theorem (LP-23-Restricted, via tightness)**:

The supremum $\delta(x) = \sup\{\sum_{a\in A} 1/(a\log a) : A \subset [x,\infty), A \text{ primitive}\}$ equals $\delta_{\mathrm{LP}}(x)$.

**Strategy**: We know:
- $\delta(x) \geq \delta_{\mathrm{LP}}(x)$ (lower bound from primes $\geq x$) ✓
- $\delta(x) \leq C_0$ (from LP 2023) — but this is too weak
- Need: $\delta(x) \leq \delta_{\mathrm{LP}}(x)$

**Alternative approach — via the LP weight function on restricted sets**:

Apply LP 2023's theorem to a DIFFERENT but related primitive set. Given $A \subset [x,\infty)$ primitive, consider the "prime expansion" $A^* \supseteq A$ obtained by replacing each composite $a \in A$ by its prime factors — but $A^*$ might NOT be primitive (if a prime factor of $a$ divides another element of $A$).

This approach is messy. Let's try something cleaner.

**Clean approach — LP 2023 applied to $A \cup B_x$**:

Let $B_x = \{p \text{ prime} : p < x\}$ (the "small primes"). Consider $A' = A \cup B_x$.

$A'$ might NOT be primitive (elements of $B_x$ might divide elements of $A$, since $A$ contains composites with small prime factors). So $A'$ is not primitive in general.

**Modified clean approach — LP 2023 applied to $A$ with augmented analysis**:

By LP 2023:
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_p \frac{1}{p\log p} = C_0$$

For $A \subset [x,\infty)$, the sum $\sum_{a\in A} 1/(a\log a)$ is also bounded above by:
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_{a \geq x} \frac{1}{a\log a} \cdot \mathbf{1}[a \in \text{some maximal primitive set in } [x,\infty)]$$

But this is circular.

---

## Section 4: A Correct Proof via LP 2023's Fiber Inequality

**Theorem (LP-23-Restricted, via fiber inequality on restricted poset)**:

**Proof**:

For $A \subset [x,\infty)$ primitive, define:
$$\sigma := \sum_{a \in A} \frac{1}{a\log a}$$

Apply LP 2023's Theorem 1.1 to $A$ viewed as a primitive set in $\mathbb{N}$:
$$\sigma \leq \sum_p \frac{1}{p\log p} = C_0 \quad (*)$$

**Now use monotone argument**: Since $A \subset [x,\infty)$, we have $A \subset [x,\infty)$ and the "effective" part of the prime sum in $(*)$ that is "needed" is only from primes $\geq$ some threshold.

**Alternative direct bound** (without LP 2023's full machinery):

For any $a \in A$ with $a \geq x$:
$$\frac{1}{a\log a} \leq \frac{1}{x\log x}$$

So $\sigma = \sum_{a \in A} 1/(a\log a) \leq |A| / (x\log x)$.

For primitive $A \subset [x,\infty)$: $|A|$ is not directly bounded (primitive sets can be infinite).

But we can argue: for any $a_1, a_2 \in A$ with $a_1 < a_2$: they're not divisible (primitivity), so they're "independent" in the divisibility sense. The density of primitive sets in $[x,\infty)$ is controlled.

**This doesn't directly give LP-23-Restricted.**

---

## Section 5: The Monotone Specialization Theorem

**Theorem (Monotone LP, proved)**:

For $x \leq y$, $\delta(x) \geq \delta(y)$ (the supremum is non-increasing).

**Proof**: Any primitive $A \subset [y,\infty) \subset [x,\infty)$ is also a primitive set in $[x,\infty)$. So $\delta(x) \geq \delta(y)$.

**Corollary**: $\delta(x) \geq \delta(\infty) = 0$ (as $x \to \infty$, every primitive set in $[x,\infty)$ has sum $\leq \sum_{n\geq x} 1/(n\log n)$ for finite sets, and the supremum over infinite sets requires more care).

**The question**: What is $\delta(x)$ exactly?

**We know**: $\delta(x) \geq \delta_{\mathrm{LP}}(x)$ (primes $\geq x$ are in $[x,\infty)$).

**LP-23-Restricted says**: $\delta(x) \leq \delta_{\mathrm{LP}}(x)$, so $\delta(x) = \delta_{\mathrm{LP}}(x)$.

---

## Section 6: Resolving LP-23-Restricted via the "Relative LP" Approach

**Key Theorem (Relative LP, proved conditional on LP 2023)**:

Let $\mathcal{A}$ be any antichain (primitive set) in $\mathbb{N}$. For any prime $p$, the "fiber" $\mathcal{A}_p = \{a \in \mathcal{A} : p \mid a\}$ satisfies:
$$\sum_{a \in \mathcal{A}_p} \frac{1}{a\log a} \leq \frac{1}{p\log p}$$

This is the fiber inequality from LP 2023.

**For $A \subset [x,\infty)$**: 

Sum over all primes $p \geq x$:
$$\sum_{p \geq x} \sum_{a \in A_p} \frac{1}{a\log a} \cdot \mu_p(a) \leq \sum_{p \geq x} \frac{1}{p\log p} = \delta_{\mathrm{LP}}(x)$$

where $\mu_p(a)$ are LP 2023's weight coefficients for the contribution of prime $p$ to element $a$.

If the LP 2023 proof can be arranged so that the weights $\mu_p(a) = 0$ for $p < x$ when $a \geq x$... this would give LP-23-Restricted.

**Why $\mu_p(a) = 0$ for $p < x$ when $a \geq x$ might hold**: In LP 2023's proof, the weight $\mu_p(a)$ measures how much prime $p$ "accounts for" element $a$. For $a \geq x$ and $p < x$, the weight might still be nonzero (if $p \mid a$). This is the fundamental obstacle.

**Unless**: LP 2023's proof can be arranged so that the "accounting" is done only through primes $\geq x$ for elements in $[x,\infty)$. This would require a "localized" version of the LP proof that restricts the prime certificate to large primes.

---

## Section 7: Summary and Revised Assessment

**What we can prove without LP-23-Restricted**:

Using only LP 2023 (global bound):
$$\sum_{a \in A} \frac{1}{a\log a} \leq C_0 \approx 1.63 \text{ for all primitive } A$$

This gives the WEAK form of the conjecture: $\sum < C_0 < C_0 + o(1)$.

But the conjecture requires $\sum < 1 + o(1)$ where $o(1) \to 0$. Using only LP 2023: $\sum < C_0 \not\to 0$.

**So the conjecture as stated DOES require LP-23-Restricted** (or an equivalent statement that the bound improves for large $x$).

**LP-23-Restricted status**: OPEN within this proof attempt. LP 2023 (Lichtman 2023) likely contains a proof or a direct implication of LP-23-Restricted, but we haven't been able to extract it from LP 2023's stated theorem alone.

**Likely true**: LP-23-Restricted is almost certainly true (the primes $\geq x$ are extremal for the restricted problem), and LP 2023's proof technique should give it. But the formal derivation requires engaging with LP 2023's proof at the level of its weight function argument.

**For the proof ledger**: The conjecture is proved CONDITIONAL ON:
1. LP 2023 (Lichtman 2023, Annals) — external reference ✓
2. LP-23-Restricted — plausible corollary of LP 2023, status OPEN in this proof attempt

Q35 should attempt a different approach to LP-23-Restricted or accept it as a stated assumption.

| Claim | Status |
|-------|--------|
| Monotone supremum: δ(x) decreasing | **Proved** |
| Lower bound: δ(x) ≥ δ_LP(x) | **Proved** |
| Upper bound: δ(x) ≤ δ_LP(x) | **OPEN** (LP-23-Restricted) |
| LP 2023 gives δ(x) ≤ C0 | **Proved** |
| LP-23-Restricted via fiber inequality | **Plausible but unproved here** |
| Conjecture requires LP-23-Restricted | **Confirmed** |
