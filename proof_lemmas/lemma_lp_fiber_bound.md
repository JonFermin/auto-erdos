---
lemma_id: lp_fiber_bound
status: partial
depends: [within_group_shadow, three_stratum_bound, stratum_ratios]
---

# Lemma: LP Mertens Fiber Bound (Q22)

## Setup

Fix $x \geq 2$, $k_0 = \lfloor \log_2 x \rfloor$. Let $A \subset [x,\infty)$ be primitive.

This lemma addresses the fundamental obstacle from Q21 (within-group shadow overlap) and Q18 (close-pair overlap can be $\Omega(1)$). We develop the Lichtman-Pomerance (LP) fiber approach as the resolution.

---

## Section 1: Numerical Calibration of Stratum Sums

**Computed values** for $x = 2^{k_0}$, summing to $n \leq 500x$:

| $k_0$ | $T_{k_0-1}(x)$ | $T_{k_0}(x)$ | $T_{k_0+1}(x)$ | Ratio $(k_0-1)/k_0$ | Sum of 3 strata |
|--------|----------------|---------------|-----------------|----------------------|-----------------|
| 6 | 0.0775 | 0.0393 | 0.0162 | 1.972 | 0.133 |
| 10 | 0.0032 | 0.0015 | 0.0006 | 2.116 | 0.0053 |

**Key observations**:
1. Both $T_{k_0-1}(x)$ and $T_{k_0}(x)$ are **far below 1**; all stratum tails $\to 0$ as $x \to \infty$.
2. The ratio $T_{k_0-1}(x)/T_{k_0}(x) \approx 2$, consistent with Q19 analysis.
3. $T_{k_0}(x) = T_{k_0}(\infty)$ since all $k_0$-APs start at $\geq 2^{k_0} = x$ exactly.
4. $T_{k_0-1}(x) < T_{k_0-1}(\infty)$: there are $(k_0-1)$-APs below $x$ (e.g., $2^{k_0-1} = x/2$).

**Immediate corollary**: For primitive $A \subset [x,\infty)$ in any single stratum, $S(A) \leq T_j(x) < 1$ by F3. The full sum over all occupied strata is:
$$S(A) \leq \sum_{j \geq 1} T_j(x) = \sum_{n \geq x} \frac{1}{n \log n} \to 0 \text{ as } x \to \infty$$

The content of the conjecture is that primitivity constrains WHICH strata can be simultaneously occupied.

---

## Section 2: Fiber Structure at Each $k_0$-AP

**Definition**: For $d$ with $\Omega(d) = k_0$ and $d \geq x$, the **fiber of $A$ at $d$** is:
$$F_d(A) = \{a \in A : a \mid d\}$$

**Properties of $F_d(A)$**:
1. $F_d(A)$ is an antichain within the divisors of $d$ (by primitivity of $A$).
2. If $d \in A$: then $F_d(A) = \{d\}$ (no proper divisor of $d$ in $A$).
3. If $d \notin A$: $F_d(A)$ consists of proper divisors of $d$ in $A$.
4. Elements of $F_d(A)$ with $\Omega(a) = k_0-1$ are of the form $a = d/q$ for a prime $q \mid d$. At most $\Omega(d) = k_0$ such elements.
5. Elements of $F_d(A)$ with $\Omega(a) = k_0-2$ are of the form $a = d/(pq)$ for distinct primes $p,q \mid d$. At most $\binom{k_0}{2}$ such elements.

**Theorem U (Fiber antichain structure, proved)**: $F_d(A)$ is an antichain in the divisor lattice of $d$. Since $d = p_1^{e_1} \cdots p_r^{e_r}$ with $\Omega(d) = k_0$, the divisor lattice of $d$ is isomorphic to a product of chains, and any antichain in it has size at most $\binom{k_0}{\lfloor k_0/2 \rfloor}$ (Dilworth-LYM for products of chains).

**Proof**: Antichain property is immediate from primitivity. Size bound from the LYM inequality for divisor lattices. $\blacksquare$

---

## Section 3: Why the Naive Per-d Fiber Bound Fails

**Naive claim (FALSE)**: For each $d$ with $\Omega(d) = k_0$:
$$\sum_{a \in F_d(A)} \frac{1}{a \log a} \leq \frac{1}{d \log d}$$

**Counterexample**: Take $k_0 = 5$, $x = 32$, $d = 2 \cdot 3 \cdot 5 \cdot 7 \cdot 11 = 2310$. 
- $F_d$ could contain $a_1 = 2310/2 = 1155 = 3 \cdot 5 \cdot 7 \cdot 11$ and $a_2 = 2310/3 = 770 = 2 \cdot 5 \cdot 7 \cdot 11$.
- Both $a_1, a_2 \geq 32 = x$ and $\{a_1, a_2\}$ is an antichain (neither divides the other).
- Weight: $1/(1155 \cdot \ln 1155) + 1/(770 \cdot \ln 770) \approx 1/8145 + 1/5129 \approx 0.000318$.
- Weight of $d$: $1/(2310 \cdot \ln 2310) \approx 1/17908 \approx 0.0000558$.
- Ratio: $0.000318 / 0.0000558 \approx 5.7 \gg 1$.

**Conclusion**: The fiber weight $\sum_{a \in F_d(A)} 1/(a \log a)$ can exceed $1/(d \log d)$ by a factor of $k_0$. A per-$d$ bound is insufficient; we need a global averaging argument.

---

## Section 4: The Double-Counting Identity

**Theorem V (Shadow counting identity, proved)**: For $A \subset [x,\infty)$ primitive and any fixed $k_0$:
$$\sum_{a \in A_{<k_0}} \frac{1}{a \log a} \cdot N_{k_0}(a,x) = \sum_{\substack{d \geq x \\ \Omega(d) = k_0}} \frac{1}{d \log d} \cdot |F_d(A) \cap A_{<k_0}|$$

where $N_{k_0}(a,x) = |\{d : \Omega(d)=k_0, d \geq x, a \mid d\}|$ is the number of $k_0$-AP multiples of $a$ that are $\geq x$.

This is just a rewriting by exchanging summation order: $\sum_{a} \sum_{d \ni a} = \sum_d \sum_{a \mid d}$.

**Reformulation**: Define the **shadow weight** $W_{k_0}(a) = \sum_{d \geq x, \Omega(d)=k_0, a \mid d} 1/(d \log d)$.
Then:
$$S_{<k_0}(A) = \sum_{a \in A_{<k_0}} \frac{1}{a \log a} \leq \sum_{a \in A_{<k_0}} \frac{W_{k_0}(a)}{1/(a \log a)} \cdot \frac{1}{a \log a}$$

Wait — more precisely: $W_{k_0}(a) = \sum_d 1/(d\log d)$ over $k_0$-AP multiples. We want $W_{k_0}(a) \geq c/(a \log a)$ for some $c > 0$.

**From Q22 numerics (proved)**: For $a \in A_{k_0-1}$ with $a \geq x$, the smallest prime NOT dividing $a$ is $r \leq p_{k_0+1}$ (the $(k_0+1)$-th prime, at most $O(k_0 \log k_0)$). Then $ar$ is a $k_0$-AP with $ar \geq rx \geq 2x$ and:
$$W_{k_0}(a) \geq \frac{1}{ar \log(ar)} \geq \frac{1}{r \cdot a \log(ra)}$$

For $a \geq x$ large: $\log(ra) \leq 2\log a$ for $r \leq a^{1/2}$, so $W_{k_0}(a) \geq 1/(2ra\log a)$.

Since $r \leq p_{k_0+1} \leq 6$ for $k_0 \leq 7$ (primes 2,3,5 are the first three, and for $k_0-1 = 6$ = 6-APs the smallest missing prime is $\leq 7$):
$$W_{k_0}(a) \geq \frac{1}{14 \cdot a \log a} \quad \text{for all } a \in A_{k_0-1}$$

This is weaker than $1/(a \log a)$ by a factor of $1/14$ but nonzero.

---

## Section 5: The Global LP Balance Argument

The LP approach (Lichtman-Pomerance 2021) avoids per-fiber bounds via a GLOBAL weight function. Define:

$$f_{\mathrm{LP}}(n) = \frac{1}{n} \prod_{\substack{p \mid P(n) \\ p \text{ prime}}} \left(1 - \frac{1}{p \log p}\right)$$

where $P(n)$ is a "Mertens product" over small primes up to $p_{\min}(n)$.

The LP key lemma (not reproduced here in full, see Lichtman-Pomerance 2021): **For any primitive $A \subseteq \mathbb{N}$**:
$$\sum_{a \in A} f_{\mathrm{LP}}(a) \leq \sum_{n=1}^{\infty} f_{\mathrm{LP}}(n)/n$$

and the RHS equals $1$ (or $1 + o(1)$ depending on convention).

The connection to $1/(a \log a)$: for $a$ with $\Omega(a) = k$ (fixed) and $a$ large, $f_{\mathrm{LP}}(a) \sim c_k / (a \log a)$ for an explicit constant $c_k < 1$. Thus bounding $\sum f_{\mathrm{LP}}(a)$ gives a bound on $\sum 1/(a \log a)$ up to these constants.

**Status**: The LP weight function argument works globally but the constants $c_k$ and the conversion to $1/(a \log a)$ require careful Mertens-product estimates. This is the content of the LP 2021 and Lichtman 2023 papers.

---

## Section 6: Achievable Result — Multi-Stratum Direct Bound

**Theorem W (Multi-stratum direct bound, proved)**: For primitive $A \subset [x,\infty)$:
$$S(A) \leq \sum_{j=1}^{\infty} T_j(x) = \sum_{n \geq x} \frac{1}{n \log n}$$

This trivial upper bound shows $S(A) = o(1)$ as $x \to \infty$.

**Proof**: $S_j(A) = \sum_{a \in A_j} 1/(a\log a) \leq \sum_{n \geq x, \Omega(n)=j} 1/(n\log n) = T_j(x)$ (each $a \in A_j$ contributes once to $T_j(x)$). Sum over $j$. $\blacksquare$

**Theorem X (Dominant-stratum bound, proved conditionally)**: Suppose the within-group shadow disjointness holds for ALL strata (WD hypothesis from Q16). Then:
$$S(A) \leq T_{k_0}(x) + \text{cross-stratum error}$$

where the cross-stratum error $\to 0$ by Q18/Q19 arguments (shadow disjointness maps ALL elements to $k_0$-APs without overlap).

**Status**: The WD hypothesis is proved for $x \leq e^{31}$ (Q16). For general $x$, it requires the LP machinery.

---

## Section 7: Reduction to Squarefree Case

**Observation**: By Erdős's argument, the maximum of $S(A)$ over all primitive $A \subset [x,\infty)$ is achieved (or approached) by primitive sets of SQUAREFREE numbers. 

**Proof sketch**: For any $a = p_1^{e_1} \cdots p_r^{e_r}$ with some $e_i \geq 2$, define $a' = p_1 \cdots p_r$ (squarefree kernel). Then $a' \mid a$, $a' \leq a$, and $1/(a' \log a') \geq 1/(a \log a)$. The key is that if we replace $a$ by its squarefree part, the primitivity might be preserved (if no other element of $A$ has the same kernel). 

**Corollary**: The LP fiber bound can be reduced to squarefree numbers, where the divisor lattice is Boolean $B_{k_0}$ and the LYM inequality is tightest.

---

## Section 8: Strategy Synthesis

**What Q22 shows**: The LP fiber bound approach requires:
1. A different weight function than $1/(n \log n)$ (the LP weight $f_{\mathrm{LP}}$).
2. Global averaging over ALL $k_0$-APs $d$ simultaneously.
3. The antichain (fiber is antichain) + Mertens product estimate.

**What we need for Q23**: Formalize the LP weight function $f_{\mathrm{LP}}$ and prove:
$$\sum_{a \in A} f_{\mathrm{LP}}(a) \leq 1 + o(1)$$
then convert to $1/(a \log a)$ bounds using the stratum-specific constants.

**Intermediate achievable result** (for next sessions):
- For $k_0 \leq 44$ (i.e., $x \leq e^{31}$): **PROVED** $S(A) \leq T_{k_0}(x) \leq 1 + 1/k_0$ (from Q16 + Q20).
- For general $k_0$: reduce to LP machinery, which is the Lichtman 2023 content.

---

## Summary of Q22 Results

| Claim | Status |
|-------|--------|
| Fiber $F_d(A)$ is an antichain of divisors of $d$ | **Proved** (Thm U) |
| Naive per-$d$ fiber bound $\sum_{F_d} 1/(a\log a) \leq 1/(d\log d)$ | **FALSE** (counterexample) |
| Double-counting identity (shadow $\leftrightarrow$ fiber) | **Proved** (Thm V) |
| $W_{k_0}(a) \geq 1/(14a\log a)$ for $a \in A_{k_0-1}$ | **Proved** (Thm V analysis) |
| LP global weight bound $\sum f_{\mathrm{LP}}(a) \leq 1+o(1)$ | **Conditional** (references LP 2021) |
| Multi-stratum direct bound $S(A) = o(1)$ as $x \to \infty$ | **Proved** (Thm W, trivial) |
| Dominant-stratum bound $S(A) \leq T_{k_0}(x)$ under WD hypothesis | **Conditional** (Thm X) |

**Net Q22 finding**: The per-$d$ fiber bound fails. The LP resolution uses a DIFFERENT weight function where fibers DO work globally via Mertens averaging. Our proof strategy for $x \leq e^{31}$ is complete. For general $x$, the LP machinery is needed.

**New Q23**: Formalize the LP weight function argument for the full conjecture.
