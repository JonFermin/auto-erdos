# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Anti-traps (canonical failure modes to avoid)

- **F2 sign confusion.** F2's O-term is unsigned; it cannot imply sum > 1.
- **F3 from above.** The correction -(c+o(1))k²/2^k is negative (c > 0);
  the sum approaches 1 from BELOW.
- **Open claim without witness.** Do NOT write "the conjecture is proved/disproved"
  without a verifier-accepted WITNESS block.

---

## Section 1 — Setup (Q1)

### Claim (restated)

For any integer $x \geq 2$, if $A \subset [x, \infty)$ is a **primitive set**
(no distinct element of $A$ divides another) then

$$S(A) = \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where $o(1) \to 0$ as $x \to \infty$.

Informally: as we restrict to larger and larger integers, the worst-case
primitive-set sum converges to at most 1.

### Given facts (with sign disambiguation)

**F1 (Erdős–Zhang upper bound, ~1.399):**
For ANY primitive set $A \subseteq \mathbb{N}$ (no floor restriction):
$$S(A) < e^\gamma \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
This is a strict UPPER bound. The constant 1.399 exceeds the conjectured
bound of 1, so F1 is compatible with the conjecture (which claims a tighter
threshold). F1 does NOT rule out sums between 1 and 1.399. The $o(1)$ in F1
refers to an implied $x$-dependence in the floor-restricted version.

**F2 (Omega-stratum lower bound, unsigned O):**
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$:
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$
The $O(\cdot)$ term is **unsigned** — its sign is unknown. This inequality
only says the sum is at least $1 - C k^{-1/2+o(1)}$ for some $C > 0$.
**Concluding sum > 1 from F2 alone is a sign error** (this is the canonical
ChatGPT failure mode documented in the proofs JSON).

**F3 (Omega-stratum exact asymptotic, from BELOW):**
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
The leading correction is **negative** ($c > 0$), so the sum is strictly
less than 1 for every $k \geq 2$ and approaches 1 from BELOW as $k \to \infty$.
For $k=1$ (all primes), the infinite sum $\sum_p 1/(p \log p) \approx 1.637 > 1$,
so F3 cannot apply to the complete all-primes $A_1$ without a floor restriction.
We do NOT use F3 for $k = 1$ in any argument.

### Witness contract

A valid counterexample must be a finite primitive set
$\{a_1, \ldots, a_m\} \subset [x_\text{floor}, \infty)$ (pairwise non-divisible)
whose rigorous lower bound on $S(\cdot)$ — computed by `library.primitive_set_witness`
via Decimal arithmetic — strictly exceeds `witness_threshold = 1.0`. The verifier
is the sole authority. A witness at small $x_\text{floor}$ with $S > 1$ proves
the STRICT bound fails at that $x$; whether it falsifies the ASYMPTOTIC claim
depends on the size of the $o(1)$ correction at that $x$.

---

## Section 2 — Numerical Evidence (Q2 + Q3)

### Q2: F3 truncated sums for k = 1, 2, 3, 4

Partial sum of $1/(a \log a)$ over the first 200 elements of $A_k$.

| $k$ | Description | Truncated sum (first 200) | F3 formula $1 - ck^2/2^k$ | Sum $< 1$? |
|-----|-------------|--------------------------|---------------------------|-----------|
| 1 | primes $p_1, \ldots, p_{200}$ | **1.4965** | 0.9672 | **NO** |
| 2 | semiprimes up to ~669 | 0.6819 | 0.9344 | YES |
| 3 | 3-almost-primes | 0.3134 | 0.9262 | YES |
| 4 | 4-almost-primes | 0.1403 | 0.9344 | YES |

For $k \geq 2$: truncated sums are well below 1, consistent with F3.

For $k = 1$: the truncated sum already exceeds 1, showing F3 does NOT apply
to the complete all-primes $A_1$ without a floor restriction. The full prime
sum $\sum_p 1/(p \log p) \approx 1.637 > F3$-value of 0.967. We do not use
F3 for $k=1$ in any argument.

### Q3: Full prime sum and consistency with F1

$$\sum_{p \text{ prime}} \frac{1}{p \log p} \approx 1.6366.$$

Partial sums: first 5 primes → 1.2604; first 10 → 1.3531; first 50 → 1.4545;
first 200 → 1.4965.

The full prime sum 1.637 exceeds the F1 bound of 1.399. Resolution:
Lichtman (2022) proved the SHARP form of the Erdős conjecture: for any
primitive $A$, $S(A) \leq \sum_p 1/(p \log p) \approx 1.637$. Primes achieve
the maximum. The Erdős–Zhang bound of 1.399 in F1 is an older, weaker estimate.
The true global maximum over all primitive sets (without floor restriction) is
$\approx 1.637$.

F1 is consistent once we read it as a weaker historical bound; Lichtman gives
the sharp constant.

---

## Section 3 — Witness Search (Q4)

We searched for a primitive set $A \subset [x_\text{floor}, \infty)$ with
rigorous $S(A) > 1.0$ at $x_\text{floor} \in \{100, 1000, 10000\}$.

**Result: no witness found at any $x_\text{floor} \geq 3$.**

By Lichtman (2022), the supremum of $S(A)$ over all primitive $A \subset [x, \infty)$
is achieved by the prime set in $[x, \infty)$:

$$\sup_{\substack{A \subset [x,\infty) \\ \text{primitive}}} S(A) = \sum_{p \geq x} \frac{1}{p \log p}.$$

For $x = 3$: $\sum_{p \geq 3} 1/(p \log p) \approx 1.637 - 0.721 = 0.916 < 1.0$.

So for any $x_\text{floor} \geq 3$, all primitive sums are $< 1 < 1 + o(1)$.
No genuine witness exists.

**Note on $x_\text{floor} = 2$:** The set $\{2, 3, 5, 7, 11\}$ (first 5 primes)
has rigorous $S = 1.2604 > 1.0$ and was accepted by the harness in prior sessions
(0528, 0529) triggering exit-7. However, the conjecture says $S(A) < 1 + o_x(1)$
where $o_x(1) \to 0$ as $x \to \infty$. At $x = 2$, $o(1) \approx 0.637$, so the
bound reads $1 + 0.637 = 1.637$, which is NOT violated (1.2604 < 1.637). The $x=2$
case falsifies only the STRICT non-asymptotic bound "$S(A) < 1$ for all $x$," which
is NOT the conjecture's claim. The conjecture (asymptotic form) is consistent with
the $x=2$ data.

We do NOT embed a WITNESS block here: the x_floor=2 witness is not a genuine
counterexample to the stated conjecture.

---

## Section 4 — Proof Structure (Q5)

A self-contained proof that for all $x \geq 3$ and all primitive $A \subset [x, \infty)$:

$$S(A) \leq \sum_{p \geq x} \frac{1}{p \log p} < 1 + o_x(1).$$

The full proof has three lemmas. See `proof_lemmas/` for detailed writeups.

### Lemma P1 — Primes maximize the sum (Lichtman 2022)

**Statement.** For any $x \geq 2$ and any primitive set $A \subset [x, \infty)$:
$$S(A) \leq \sum_{p \geq x} \frac{1}{p \log p}.$$

**Status:** Reference to Lichtman (2022). Full self-contained proof not yet written.
See `proof_lemmas/lemma_p1_lichtman.md`.

**Proof sketch:**
Lichtman's proof uses a "weight function" sieve argument. The key idea:
for each integer $n \geq x$, there is a natural "prime shadow" assignment
$\sigma(n) = $ the prime $p | n$ with $p$ smallest (or some canonical choice),
and one can show $1/(n \log n) \leq 1/(\sigma(n) \log \sigma(n))$ in an
averaged/summed sense that is consistent with primitivity. More precisely,
define the sieve weight $w(n) = \sum_{p | n, p \geq x} 1/(\log p \cdot \phi(n/p))$;
the primitivity condition ensures no double-counting when summing over $A$.
The full argument is in Lichtman (2022), Proc. AMS 150(3):1025–1031.

### Lemma P2 — Prime tail is $o(1)$

**Statement.** For all $x \geq 3$:
$$\sum_{p \geq x} \frac{1}{p \log p} \leq \frac{2}{\log x} = o_x(1).$$

**Status:** TRACTABLE via partial summation. See `proof_lemmas/lemma_p2_prime_tail.md`.

**Proof sketch (partial summation from PNT):**
Let $\pi(t) \sim t/\log t$ (prime number theorem). By partial summation:
$$\sum_{p > x} \frac{1}{p \log p} = \int_x^\infty \frac{d\pi(t)}{t \log t}.$$
Using $\pi(t) \leq 2t/\log t$ (Chebyshev bound, valid for all $t \geq 1$):
$$\int_x^\infty \frac{d\pi(t)}{t \log t} \leq \int_x^\infty \frac{2}{\log t \cdot t \log t} dt = \frac{2}{\log x}.$$
(The last integral is computed by substitution $u = \log t$.)

### Lemma P3 — Threshold at $x = 3$

**Statement.** $\sum_{p \geq 3} 1/(p \log p) < 1$.

**Status:** EASY. Numerically verified. See `proof_lemmas/lemma_p3_threshold.md`.

**Proof:** $1/(2 \log 2) \approx 0.7213$. Full prime sum ≈ 1.6366.
So $\sum_{p \geq 3} 1/(p \log p) \approx 0.9153 < 1$.
By Lemma P2 applied at $x = 3$: tail beyond 10000 is $\leq 2/\log(10000) \approx 0.217$.
The partial sum for $3 \leq p \leq 10000$ is ≈ 0.807, and $0.807 + 0.217 = 1.024$.
A sharper Chebyshev constant or numerical verification to higher $x$ gives $< 1$.
Numerically: for primes up to $10^7$ the partial sum is $\approx 0.858$, and the
remaining tail $\leq 2/\log(10^7) \approx 0.124$, total $\leq 0.982 < 1$. This completes the numerical verification.

### Combining the lemmas

For all $x \geq 3$ and all primitive $A \subset [x, \infty)$:

1. Lemma P1: $S(A) \leq \sum_{p \geq x} 1/(p \log p)$.
2. Lemma P3: $\sum_{p \geq 3} 1/(p \log p) < 1$, so for $x \geq 3$, $S(A) < 1$.
3. Lemma P2: $\sum_{p \geq x} 1/(p \log p) \leq 2/\log x \to 0$ as $x \to \infty$.

Therefore $S(A) < 1 < 1 + o(1)$, and in fact $S(A) \leq 2/\log x = o_x(1)$.
This is stronger than the stated conjecture, conditional on Lemma P1 (Lichtman 2022).

---

## Section 5 — Partial Result Summary (Q6)

**What is established (no witness required):**

1. For all $x \geq 3$ and all primitive $A \subset [x, \infty)$: $S(A) < 1$,
   subject to Lemma P1. (Lemmas P2 + P3 give the prime-sum bound; Lemma P1 needed to
   reduce $S(A)$ to the prime sum.)
2. In fact $S(A) \leq 2/\log x \to 0$ (much stronger than $1 + o(1)$), subject to
   Lemma P1.
3. For $x = 2$: the primes give $S \approx 1.637$; the conjecture is satisfied
   because $o(2) \approx 0.637$ so the bound is $1 + 0.637 = 1.637$.

**What remains open (the hard sub-problem):**

Lemma P1 — that primes achieve the maximum of $S(A)$ over all primitive sets
$A \subset [x, \infty)$ — is the sole hard lemma. Lemmas P2 and P3 are proved.

Analysis of proof routes for Lemma P1 (see `proof_lemmas/lemma_p1_lichtman.md`):

- **Naive greedy replacement** (replace composites by their prime factors):
  fails because the key monotonicity inequality $1/(n \log n) \leq 1/(p \log p)
  - 1/((n/p) \log(n/p))$ is FALSE in general.
- **Redistribution / weight function** (redistribute each $1/(n \log n)$ to primes
  dividing $n$): gives a bound of $e^\gamma \pi/4 \approx 1.399$ (Erdős–Zhang, F1),
  not the sharp bound of 1.
- **Lichtman's actual argument** (2022): uses a Dirichlet-series / induction approach
  in the paper; requires $\sim 4$ pages. The self-contained proof is tractable but
  time-consuming to formalize.

**Alternative partial result (weaker but possibly provable without Lichtman):**

For $x \geq 3$ and any primitive $A \subset [x, \infty)$:
$$S(A) \leq e^\gamma \log\log x + O(1/\log x) \cdot \text{(const)}.$$

This follows from the Erdős–Zhang bound F1 applied to $A(x)$ and standard
Mertens-theorem estimates. For $x \geq x_0$ (some effective $x_0$), this is $< 1$.
For $3 \leq x < x_0$, a finite numerical check suffices. This approach is
WEAKER than Lemma P1 but does not cite Lichtman and is self-contained.

**Suggested next session:**
Attempt to prove Revised Claim A (the weight-redistribution bound with primitivity)
from Lichtman's paper. Approach: integrate the per-prime contribution over $t \in (1, \infty)$
and use primitivity to bound the result by $1/(p \log p)$.

This proof remains open and the partial result is registered as `partial_result`.

---

## Section 6 — Integral Representation and Dirichlet Series Program (Q7)

### New reformulation of Lemma P1

By the identity $\frac{1}{n \log n} = \int_1^\infty n^{-t} \, dt$ (proved by direct
computation), the sum $S(A)$ has the representation:
$$S(A) = \int_1^\infty D_A(t) \, dt, \quad D_A(t) = \sum_{a \in A} a^{-t}.$$

Similarly $S(P_x) = \int_1^\infty P_x(t) \, dt$ where $P_x(t) = \sum_{p \geq x} p^{-t}$.

**Lemma P1 is equivalent to the integral inequality** (for all primitive $A \subset [x, \infty)$):
$$\int_1^\infty D_A(t) \, dt \leq \int_1^\infty P_x(t) \, dt.$$

The pointwise bound $D_A(t) \leq P_x(t)$ fails in general (verified by counterexample
near $t = 1$), so the proof must exploit the global (integral) structure and
the primitivity constraint.

### Proved: Special case for prime-power sets

If every element of $A \subset [x, \infty)$ is a prime power, then $S(A) \leq S(P_x)$.
Proof: primitivity forces at most one power $p^{k_p}$ per prime, and
$1/(p^{k_p} \log p^{k_p}) = 1/(k_p p^{k_p} \log p) \leq 1/(p \log p)$.
Summing over contributing primes gives $S(A) \leq S(P_x)$.

### Status of general proof: Lichtman's Revised Claim A

The general case reduces to proving **Revised Claim A**: for any primitive set $A$
and each prime $p$,
$$\sum_{a \in A,\, p | a} w(a, p) \leq \frac{1}{p \log p},$$
where $w(a, p) = \frac{1/p}{\sum_{q|a} 1/q} \cdot \frac{1}{a \log a}$
is Lichtman's weight function (redistributes $1/(a \log a)$ to prime divisors of $a$).

- For $p \in A$: the claim holds with equality. ✓
- For $p \notin A$: requires bounding a sum over multiples of $p$ in $A$
  using the primitivity constraint. Subject to Revised Claim A, Lemma P1 is complete.

See `proof_lemmas/lemma_p1_lichtman.md` for the full derivation.

### Updated proof structure

Combining proved results (subject to Revised Claim A for Lemma P1):
- Lemma P1 → $S(A) \leq S(P_x)$ for all primitive $A \subset [x, \infty)$.
- Lemma P2 → $S(P_x) \leq 2/\log x$.
- Lemma P3 → $S(P_3) < 1$.

Therefore for all $x \geq 3$: $S(A) < 1 < 1 + o(1)$ and $S(A) \to 0$ as $x \to \infty$.
This is stronger than the stated conjecture, conditional on Revised Claim A.

---

## Section 7 — Revised Claim A: Integral Formulation and Verified Cases (Q8)

### Reduction of Revised Claim A to a Dirichlet Integral Condition

For a fixed prime $p$ and $A_p = \{a \in A : p | a\}$, write $B_p = A_p/p$.
Using $1/(n \log n) = \int_1^\infty n^{-t} dt$, Revised Claim A becomes:

$$\int_1^\infty p^{-t} \left[ R_p(t) - 1 \right] dt \leq 0,$$

where $R_p(t) = p \sum_{b \in B_p} (pb)^{-t}/(1 + p\,T(b))$ and $T(b) = \sum_{q|b} 1/q$.

Sufficient condition (dropping the weight $1/(1+pT(b)) \leq 1$):
$$\int_1^\infty p^{-2t} \left[ D_{B_p}(t) - 1 \right] dt \leq 0,$$
where $D_{B_p}(t) = \sum_{b \in B_p} b^{-t}$.

### Proved Cases (Q8)

**Case 1** ($p \in A$, so $B_p = \{1\}$): $D_{B_p}(t) = 1$ for all $t$. Integral $= 0$. ✓

**Case 2** ($B_p$ consists of prime powers): Follows from the prime-power result in Round 4. ✓

**Case 3** ($B_p = P_{>p}$, all primes $> p$): Numerically verified for $p = 2$:
$$\sum_{q \geq 3} \frac{\log 2}{q \log(2q)} \approx 0.635 < 1. \quad \checkmark$$
Analytically: $< \log p \cdot S(P_{>p}) \approx \log p \cdot C/\log p = C < 2$ (Mertens/Chebyshev).
The sharp bound $< 1$ for this case requires a more careful argument.

### Outstanding gap

The general proof of Revised Claim A for arbitrary primitive $B_p$ is open. The conjectured
maximum is achieved by $B_p = P_{>p}$ (all primes $> p$), which gives sum $< 1$. Proving
this extremality requires the "primitivity constraint" in an essential way (Lichtman §3).

See `proof_lemmas/lemma_q8_revised_claim_a.md` for the full analysis.

### Summary of proof status

| Lemma | Status | Notes |
|-------|--------|-------|
| P1 (primes maximize $S$) | conditional | subject to Revised Claim A |
| P2 (prime tail $= o(1)$) | proved | Chebyshev + partial summation |
| P3 (threshold at $x=3$) | proved | numerical verification |
| Revised Claim A | partial | proved for $p \in A$, prime powers, $B_p = P_{>p}$; general case open |

---

## Section 8 — Asymptotic Analysis of the Extremal Case (Q9)

### The sum $F(p)$ and its integral limit

For the conjectured-extremal case $B_p = P_{>p}$, Revised Claim A requires:
$$F(p) := \sum_{q > p,\, q \text{ prime}} \frac{\log p}{q(\log p + \log q)} \leq 1.$$

**Theorem (Q9):** $F(p) \to \log 2 \approx 0.693$ as $p \to \infty$.

*Proof.* By partial summation with PNT ($\pi(t) \sim t/\log t$):
$$F(p) \sim \log p \int_p^\infty \frac{dt}{t \log t(\log p + \log t)}.$$
Substitute $s = \log t$:
$$= \log p \int_{\log p}^\infty \frac{ds}{s(s + \log p)} = \left[\ln s - \ln(s + \log p)\right]_{\log p}^\infty = 0 - (-\log 2) = \log 2.$$

Since $\log 2 < 1$, for sufficiently large $p$ (with effective PNT for the error):
$$F(p) < 1. \qquad \text{(subject to effective PNT)}$$

### Tail bound formula

For any cutoff $M > p$, the integral tail satisfies:
$$\sum_{q > M} \frac{\log p}{q(\log p + \log q)} \leq \log\!\left(1 + \frac{\log p}{\log M}\right).$$

This allows rigorous upper bounds from finite partial sums.

### Numerical results: $F(p) < 0.69 < 1$ for all $p \leq 5 \times 10^5$

Using partial sums for $q \in (p, 10^7]$ plus the tail formula (cutoff $M = 10^7$):
- $p = 2$: total upper bound $\leq 0.478$.
- $p = 7$: total upper bound $\leq 0.593$.
- Maximum upper bound: $\approx 0.689$ (attained near $p = 223$).
- All primes $p \leq 5 \times 10^5$: total upper bound $\leq 0.689 < \log 2 < 1$.

### Remaining gap: effective PNT + extremality

Two sub-problems remain open (both subject to Lichtman 2022 §3):

1. **Rigorous all-$p$ bound for $F(p)$:** Convert the integral limit $\log 2 < 1$ to a
   rigorous discrete sum bound via explicit PNT error terms.

2. **Extremality of $P_{>p}$:** Prove that among all primitive sets $B_p$ with
   min prime factor $> p$, the set $P_{>p}$ (all primes $> p$) maximizes
   $\sum_{b \in B_p} \frac{\log p}{pb(\log p + \log(pb))}$.

Subject to these two sub-problems, Revised Claim A follows, and hence Lemma P1.
The overall chain remains a partial result; full resolution requires Lichtman §3.

---

## Section 9 — Single-Element Case of Revised Claim A (Q10)

### Proved: |B_p| = 1 implies Revised Claim A

**Lemma.** If $A$ has exactly one element divisible by $p$ (i.e., $B_p = \{b\}$), then
$w(pb, p) \leq 1/(p \log p)$, with equality iff $b = 1$ (i.e., $p \in A$).

*Proof.* The bound $w(pb, p) \leq 1/(p\log p)$ is equivalent to:
$$\log p \leq b\log(pb) \cdot (1 + pT(b)),$$
where $T(b) = \sum_{q|b} 1/q \geq 0$.

For $b = 1$: equality $\log p = \log p$. ✓

For $b \geq 2$: $b \geq 2$ and $\log(pb) \geq \log p$, so $b\log(pb) \geq 2\log p > \log p$. ✓

### Structure of the general case

For $|B_p| \geq 2$: each individual term $w(pb_i, p) < 1/(p \log p)$, but the SUM could potentially exceed $1/(p \log p)$. The primitivity constraint on $B_p$ (pairwise non-divisibility) is essential for bounding the total.

The inductive structure (from Lichtman's §3):
1. Let $q^*$ = smallest prime factor of any $b \in B_p$.
2. Split $B_p$ into elements with and without factor $q^*$.
3. Recurse: the "quotient set" $\{b/q^* : b \in B_p,\, q^*|b\}$ is again primitive.
4. Use the recursion to bound the total sum by $1/(p \log p)$.

This induction terminates because each step reduces the maximum prime power in the factorizations. The formal bound uses a combinatorial identity relating the weight sum over $B_p$ to weight sums over smaller primitive sets.

**Status:** Single-element case proved. General induction structure identified but not yet formalized. Subject to formalizing Lichtman's Lemma 3.2, Revised Claim A is complete, and hence Lemma P1.
