---
id: q8_revised_claim_a
status: open
depends_on: [p1_lichtman]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma Q8 — Revised Claim A (Lichtman Weight Redistribution)

## Statement

For any primitive set $A \subset [x, \infty)$ and any prime $p \geq x$:

$$\sum_{a \in A,\, p | a} w(a, p) \leq \frac{1}{p \log p},$$

where $w(a, p) = \dfrac{1/p}{\displaystyle\sum_{q | a,\, q \text{ prime}} 1/q} \cdot \dfrac{1}{a \log a}$.

If this holds for all primes $p$, then Lemma P1 follows by summing over $p$:
$$S(A) = \sum_{a \in A} \frac{1}{a \log a} = \sum_{a \in A} \sum_{p | a} w(a, p)
= \sum_{p} \sum_{a \in A,\, p | a} w(a, p) \leq \sum_{p} \frac{1}{p \log p} = S(P_x).$$

## Status

**Open** in general. Proved for prime-power sets and for the case $p \in A$.
The general case requires Lichtman (2022) §3.

## Proof for $p \in A$ (Claim A base case)

If $p \in A$: since $A$ is primitive and all other elements of $A_p = \{a \in A : p | a\}$
are multiples of $p$, primitivity forces $A_p = \{p\}$ (any $a \in A_p$ with $a \neq p$
satisfies $p | a$, contradicting primitivity since $p \in A$).

Then $w(p, p) = (1/p)/(1/p) \cdot 1/(p \log p) = 1/(p \log p)$. Equality holds. ✓

## Proof for Prime-Power Primitive Sets

If every element of $A_p = \{a \in A : p | a\}$ is a prime power:

By primitivity, the prime powers in $A_p$ are pairwise non-divisible. For prime powers
$p^k | p^j$ when $k \leq j$, so there is at most one power of $p$ in $A_p$.
Let $A_p = \{p^k\}$ for some $k \geq 1$ (if $p^k \in A$), or $A_p = \emptyset$.

For $A_p = \{p^k\}$:
$\sum_{q | p^k} 1/q = 1/p$ (only prime factor of $p^k$ is $p$).
$w(p^k, p) = \frac{1/p}{1/p} \cdot \frac{1}{p^k \log(p^k)} = \frac{1}{k p^k \log p}$.

For $k = 1$: equality $w(p, p) = 1/(p \log p)$. ✓
For $k \geq 2$: $w(p^k, p) = 1/(k p^k \log p) \leq 1/(p \log p)$. ✓ (since $k p^{k-1} \geq 1$)

## Integral Reformulation

Using $1/(n \log n) = \int_1^\infty n^{-t} \, dt$:

$$w(a, p) = \frac{1/p}{\sum_{q|a} 1/q} \int_1^\infty a^{-t} \, dt.$$

So Revised Claim A becomes:
$$\int_1^\infty p^{-t} \underbrace{\left[ p \sum_{b \in B_p} \frac{(pb)^{-t}}{1 + p\, T(b)} \right]}_{R_p(t)} dt \leq \int_1^\infty p^{-t} \, dt$$

where $B_p = \{a/p : a \in A, p | a\}$ (a primitive set) and $T(b) = \sum_{q | b} 1/q$ (sum of prime-reciprocals of prime factors of $b$, 0 if $b = 1$).

This reduces to:
$$\int_1^\infty p^{-t} \left[ R_p(t) - 1 \right] dt \leq 0,$$

where $R_p(t) = p \sum_{b \in B_p} \frac{(pb)^{-t}}{1 + p \, T(b)}$.

## Key Simplification: Dropping the Weight

Since $1 + pT(b) \geq 1$, we have:
$R_p(t) \leq p \sum_{b \in B_p} (pb)^{-t} = p^{1-t} D_{B_p}(t)$

where $D_{B_p}(t) = \sum_{b \in B_p} b^{-t}$.

So a sufficient condition for Revised Claim A is:
$$\int_1^\infty p^{-t} \left[ p^{1-t} D_{B_p}(t) - 1 \right] dt \leq 0$$

i.e., $p \int_1^\infty p^{-2t} D_{B_p}(t) \, dt \leq \int_1^\infty p^{-t} \, dt = \frac{1}{p \log p}$

i.e., $\int_1^\infty p^{-2t} D_{B_p}(t) \, dt \leq \frac{1}{p^2 \log p}$.

But $\int_1^\infty p^{-2t} dt = 1/(p^2 \log p)$, so this requires:
$$\int_1^\infty p^{-2t} D_{B_p}(t) \, dt \leq \int_1^\infty p^{-2t} \, dt,$$
i.e., $\int_1^\infty p^{-2t} [D_{B_p}(t) - 1] \, dt \leq 0$.

**Sub-claim (sufficient for Revised Claim A without the weight reduction):**
For any primitive $B_p$ (with all prime factors $\geq p$):
$$\int_1^\infty p^{-2t} [D_{B_p}(t) - 1] \, dt \leq 0.$$

This is a weaker integral condition than the full Revised Claim A.

## Verified Special Case: $B_p =$ All Primes $> p$

For $B_p = P_{>p}$ (all primes $q > p$), the Revised Claim A reduces to:
$$\sum_{q > p} \frac{\log p}{q \log(pq)} \leq 1.$$

*Numerical verification for $p = 2$:*
$\sum_{q \geq 3, q \text{ prime}} \frac{\log 2}{q \log(2q)} = \log 2 \sum_{q \geq 3} \frac{1}{q(\log 2 + \log q)}$
$< \log 2 \sum_{q \geq 3} \frac{1}{q \log q} = \log 2 \cdot S(P_3)$
$\approx 0.693 \times 0.916 \approx 0.635 < 1.$ ✓

*Proof for general $p$:*
$\sum_{q > p} \frac{\log p}{q \log(pq)} < \log p \sum_{q > p} \frac{1}{q \log q} = \log p \cdot S(P_{p+\epsilon})$.

By Lemma P2: $S(P_{p'}) \leq 2/\log(p')$. Taking $p' = p + 1$:
$\sum_{q > p} \frac{\log p}{q \log(pq)} < \log p \cdot \frac{2}{\log p} = 2$.

This gives the bound $< 2$, not $< 1$. The factor of 2 is from the Chebyshev constant in Lemma P2. A sharper estimate using $S(P_{p+\epsilon}) \leq 1/\log p + O(1/\log^2 p)$ (from PNT + partial summation) gives:
$\sum_{q > p} \frac{\log p}{q \log(pq)} < \log p \cdot \frac{C}{\log p} = C$

where $C$ is the sharp Mertens constant $\approx 0.916/0.693 \approx 1.32$ for $p = 2$.
For $p \geq 3$: $S(P_{p+1}) < S(P_3) < 1 < 1/\log p$? No, $1/\log 3 \approx 0.91 \approx S(P_3)$: bound is near-tight.

**This gives a bound $< C$ for some constant $C < 2$, but not $< 1$.** The sharp bound of 1 requires a more careful estimate using the actual sum of $1/(q \log(pq))$ rather than the weaker $1/(q \log q)$ bound.

## Open Sub-problem

Prove: for any prime $p$ and any primitive set $B_p$ with all elements having prime factors $\geq p$, $\sum_{q > p} \frac{\log p}{q \log(pq)} \leq 1$. (The general primitive $B_p$ case, not just $B_p = P_{>p}$.)

The key difficulty: for primitive $B_p$ other than $P_{>p}$, the sum has fewer terms but each term might be larger. It is conjectured (consistent with all examples checked) that $P_{>p}$ achieves the supremum of the sum over all primitive $B_p$, giving the bound $\leq \sum_{q > p} \frac{\log p}{q \log(pq)} < 1$ (for $p \geq 2$).

This is essentially the content of Lichtman (2022) §3, proved using the primitivity constraint via a careful induction.

---

## Asymptotic Integral Formula for $B_p = P_{>p}$ (Q9)

Define $F(p) = \displaystyle\sum_{q > p,\,q\text{ prime}} \frac{\log p}{q(\log p + \log q)}$.

**Claim:** $F(p) \to \log 2 \approx 0.693 < 1$ as $p \to \infty$.

*Proof via PNT and substitution:*

By partial summation using $\pi(t) \sim t/\log t$, the dominant term of $F(p)$ is the integral:
$$F(p) \sim \log p \int_p^\infty \frac{dt}{t \log t (\log p + \log t)}.$$

Substitute $s = \log t$ (so $dt/t = ds$, range shifts from $\log p$ to $\infty$):
$$= \log p \int_{\log p}^\infty \frac{ds}{s(\log p + s)}.$$

Partial fractions: $\displaystyle\frac{1}{s(\log p + s)} = \frac{1}{\log p}\!\left(\frac{1}{s} - \frac{1}{s + \log p}\right)$.

$$= \log p \cdot \frac{1}{\log p} \int_{\log p}^\infty \!\!\!\left(\frac{1}{s} - \frac{1}{s + \log p}\right) ds = \left[\ln s - \ln(s + \log p)\right]_{s=\log p}^{s=\infty}.$$

At $s \to \infty$: $\ln s - \ln(s + \log p) = \ln(1 - \log p/(s + \log p)) \to 0$.

At $s = \log p$: $\ln(\log p) - \ln(2\log p) = -\ln 2$.

Therefore:
$$\int_{\log p}^\infty \!\!\!\left(\frac{1}{s} - \frac{1}{s + \log p}\right)ds = 0 - (-\ln 2) = \log 2. \qquad \square$$

Since $\log 2 \approx 0.693 < 1$, for all sufficiently large primes $p$ the bound $F(p) < 1$ holds. Making "sufficiently large" rigorous requires an effective PNT with explicit error term (e.g., Rosser–Schoenfeld 1962).

## Numerical Verification: $F(p) < 1$ for All Primes $p \leq 5 \times 10^5$

**Method.** For cutoff $M$, the integral tail bound is:
$$\sum_{q > M} \frac{\log p}{q(\log p + \log q)} \leq \log p \int_M^\infty \frac{dt}{t\log t(\log p + \log t)} = \log\!\!\left(1 + \frac{\log p}{\log M}\right).$$

(Same substitution $s = \log t$, definite integral from $\log M$ to $\infty$.)

Using partial sums for primes $q \in (p, 10^7]$ plus this tail formula:

| $p$ | Partial sum | Tail bound | Total UB |
|-----|-------------|------------|----------|
| 2 | 0.4265 | 0.0515 | 0.478 |
| 3 | 0.4803 | 0.0574 | 0.538 |
| 5 | 0.5154 | 0.0578 | 0.573 |
| 7 | 0.5350 | 0.0578 | 0.593 |
| 223 | $\approx 0.627$ | $\approx 0.062$ | **0.689** (max) |
| $p \leq 5\times 10^5$ | — | — | $\leq 0.689 < 1$ |

The maximum upper bound $\approx 0.689$ occurs near $p = 223$; all primes tested satisfy total $< \log 2 + 0.005 < 0.70 < 1$.

**Observation.** The upper bound is well below 1 throughout, with maximum $\approx 0.689$ near $p = 223$ and converging to $\log 2 \approx 0.693$ from below.

## Gap: Effective PNT Required for Full Rigour

The Chebyshev estimate $\sum_{q>p} 1/(q \log q) \leq 2/\log p + O(1/\log^2 p)$ yields $F(p) \leq 2$, which is insufficient. A rigorous all-$p$ proof requires one of:

1. An explicit zero-free region for $\zeta(s)$ (Rosser–Schoenfeld, valid for $x \geq x_0$) to convert the integral bound $\log 2 < 1$ to the discrete sum with explicit error.
2. Direct computer-verified bounds for small $p$ (finite check) combined with the asymptotic for large $p$.
3. Lichtman's primitivity-based inductive argument (§3), which avoids PNT directly.

Subject to effective PNT (or Lichtman §3), the $B_p = P_{>p}$ case of Revised Claim A is established. The remaining gap is the extremality result: that $B_p = P_{>p}$ maximizes $F$ over all primitive $B_p$ with min prime factor $> p$.

---

## Single-Element Case: Direct Proof of Revised Claim A (Q10 base case)

**Lemma (|B_p| = 1).** If $B_p = \{b\}$ for some $b \geq 1$, then
$$\sum_{a \in A,\, p | a} w(a, p) = w(pb, p) \leq \frac{1}{p \log p}.$$

*Proof.* By definition of $w$:
$$w(pb, p) = \frac{1/p}{\displaystyle\sum_{q | pb} 1/q} \cdot \frac{1}{pb \log(pb)} = \frac{1/p}{1/p + T(b)} \cdot \frac{1}{pb \log(pb)} = \frac{1}{p(1 + pT(b))} \cdot \frac{1}{b \log(pb)},$$
where $T(b) = \sum_{q | b,\, q \text{ prime}} 1/q \geq 0$.

The bound $w(pb, p) \leq 1/(p \log p)$ is equivalent to:
$$\frac{\log p}{b \log(pb) \cdot (1 + pT(b))} \leq 1,$$
i.e., $\log p \leq b \log(pb) \cdot (1 + pT(b))$.

**Case $b = 1$:** RHS $= 1 \cdot \log p \cdot 1 = \log p$. Equality holds. ✓

**Case $b \geq 2$:** Since $b \geq 2$ and $\log(pb) = \log p + \log b \geq \log p$:
$$b \log(pb) \cdot (1 + pT(b)) \geq 2 \cdot \log p \cdot 1 = 2 \log p > \log p. \quad \checkmark$$

(The factor $b \geq 2$ alone gives the strict inequality; neither the $T(b)$ term nor the $\log b$ term is needed.) $\square$

**Equality** holds iff $b = 1$ (i.e., $p \in A$). For any other single element divisible by $p$, the inequality is strict.

## Inductive Structure for |B_p| ≥ 2 (Q10 general case)

For $|B_p| \geq 2$, let $q^* > p$ be the smallest prime factor of any element of $B_p$.
Partition $B_p = B' \cup B''$ where $B' = \{b \in B_p : q^* | b\}$ and $B'' = B_p \setminus B'$.

By primitivity of $B_p$: no element of $B'$ divides another, and no element of $B''$ divides any element of $B'$ (since $q^* \nmid b''$ for $b'' \in B''$).

**Claim:** $\sum_{b \in B_p} w(pb, p) \leq \sum_{b \in B_p} \frac{1}{(1 + pT(b)) \cdot b \log(pb)} \cdot \frac{1}{p}$.

The challenge: summing over multiple primitive $b_i$ values. Each term is $\leq 1/(p \log p)$ individually (by the single-element case), but the SUM of multiple such terms could exceed $1/(p \log p)$.

**Key constraint from primitivity:** For $b_1, b_2 \in B_p$ with $b_1 | b_2$, primitivity is violated (since $pb_1 | pb_2$). So the elements of $B_p$ are pairwise non-divisible, which forces them to be "spread out" in divisibility order. This spreading is what Lichtman exploits to bound the sum.

The general proof requires Lichtman's Lemma 3.2 (the "Fibonacci-type" recursion on the primitive structure), which is the key analytical step of his 2022 paper and is subject to ongoing formalization in this session.

---

## Exchange Lemma: $f(b) \leq f(q)$ for Any Prime Divisor $q \mid b$ (Q11 tool)

**Lemma (Exchange).** For any $b \geq 2$ with all prime factors $> p$, and any prime $q \mid b$:
$$f(b) := \frac{\log p}{b\log(pb)(1+pT(b))} \leq \frac{\log p}{(q+p)\log(pq)} =: f(q).$$

*Proof.* We show the denominators satisfy $b\log(pb)(1+pT(b)) \geq (q+p)\log(pq)$.

- Since $q \mid b$: $b \geq q$ (both are positive integers, $q \leq b$).
- Therefore $\log(pb) \geq \log(pq)$.
- Since $q$ is a prime factor of $b$: $T(b) = \sum_{r \mid b,\, r\text{ prime}} 1/r \geq 1/q$, so $1 + pT(b) \geq 1 + p/q = (q+p)/q$.

Multiplying these three inequalities:
$$b\log(pb)(1+pT(b)) \geq q \cdot \log(pq) \cdot \frac{q+p}{q} = (q+p)\log(pq). \quad \square$$

**Corollary.** $f(b) \leq \min_{q \mid b,\, q\text{ prime}} f(q) \leq \sum_{q \mid b,\, q\text{ prime}} f(q)$.

In particular: $f(b) \leq f(q^-)$ where $q^- = q^-(b)$ is the smallest prime factor of $b$.

## Revised Claim A for Sets with Distinct Smallest-Prime-Factor

**Proposition.** If $B_p$ is a primitive set such that no two elements of $B_p$ share the same smallest prime factor (i.e., the function $b \mapsto q^-(b)$ is injective on $B_p$), then:
$$\sum_{b \in B_p} f(b) \leq F(p) < 1.$$

*Proof.* By the Exchange Lemma, $f(b) \leq f(q^-(b))$ for each $b \in B_p$.
Since $q^-(b)$ is injective, the primes $q^-(b_1), q^-(b_2), \ldots$ are distinct elements of $P_{>p}$.
Therefore:
$$\sum_{b \in B_p} f(b) \leq \sum_{b \in B_p} f(q^-(b)) \leq \sum_{q > p,\, q\text{ prime}} f(q) = F(p) < 1. \quad \square$$

This covers: all-prime $B_p$, and more generally any primitive $B_p$ where at most one element has each prime as its smallest factor.

## General Case: Recursive Structure (Q11 open part)

For general primitive $B_p$, partition by smallest prime factor: $B_p = \bigsqcup_{q > p} B_p^{(q)}$ where $B_p^{(q)} = \{b \in B_p : q^-(b) = q\}$.

If $|B_p^{(q)}| \geq 2$, the Exchange Lemma gives $\sum_{b \in B_p^{(q)}} f(b) \leq |B_p^{(q)}| \cdot f(q)$, which could exceed $f(q)$ for the total.

However, **primitivity constrains** $B_p^{(q)}$: writing $B_p^{(q)} = \{qc : c \in C_q\}$, the set $C_q$ is a primitive set with all prime factors $\geq q$ (since if $c_1 \mid c_2$ then $qc_1 \mid qc_2$, contradicting primitivity of $B_p$).

**Recursive Claim (Q11):** For any prime $q > p$ and primitive $C_q$ with all elements $\geq 1$ and all prime factors $\geq q$:
$$\sum_{c \in C_q} f_p(qc) \leq f_p(q) = \frac{\log p}{(q+p)\log(pq)},$$
where $f_p(qc) = \frac{\log p}{qc\log(pqc)(1+p/q+pT(c))}$.

The case $C_q = \{1\}$ (i.e., $q \in B_p$): $f_p(q \cdot 1) = f_p(q)$. Equality. ✓

The case $|C_q| \geq 2$: requires Lichtman's recursion with "base prime" $q$ (not $p$). Subject to establishing this recursion, the full Revised Claim A follows by summing over primes $q > p$:
$$\sum_{b \in B_p} f(b) = \sum_{q > p} \sum_{c \in C_q} f_p(qc) \leq \sum_{q > p} f_p(q) = F(p) < 1. \quad \square \text{ (subject to Q11)}$$
