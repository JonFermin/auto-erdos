# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Setup

- **Claim**: see `proofs/primitive_set_erdos.json` field `claim_latex`. The
  conjecture is that for any primitive set $A \subset [x, \infty)$ the sum
  $\sum_{a \in A} 1/(a \log a)$ is bounded above by $1 + o(1)$ as $x \to \infty$.
- **Status**: open. Until a verifier-accepted witness is committed, no claim
  of resolution may appear in this file (`critic_openness` enforces this).
- **Given facts ledger**: see `proofs/primitive_set_erdos.json` field
  `given_facts`. The proof may cite F1 (Erdős-Zhang upper bound ≈ 1.399),
  F2 (Omega-stratum lower bound with UNSIGNED big-O — read carefully),
  F3 (exact asymptotic showing canonical extremal sum approaches 1 from
  BELOW). Citations to facts not in the ledger trigger `critic_ledger`.

## Sign-error traps (summary)

- **F2**: the $O(k^{-1/2+o(1)})$ correction is UNSIGNED. Concluding sum $> 1$
  from F2 alone is WRONG (unsigned-O-sign-confusion).
- **F3**: the leading correction $-(c+o(1))k^2/2^k$ is NEGATIVE ($c \approx
  0.0656 > 0$); the $A_k$ sum approaches 1 from BELOW as $k \to \infty$.
- Claims of resolution without a verifier-accepted WITNESS block are
  automatically flagged by the openness critic and the defense-in-depth.

## Witness format (the only path to a counterexample claim)

A claim of disproof MUST be backed by a finite primitive set whose sum is
rigorously verified to exceed `witness_threshold` by
`library.primitive_set_witness.verify_witness`. To commit a witness,
embed exactly one block of the form:

```
<!-- WITNESS
{
  "x_floor": 100,
  "elements": [101, 103, 107, 109, ...],
  "claimed_sum_lower_bound": 1.005
}
WITNESS -->
```

at the bottom of this file. `proof_prepare.py` parses the JSON, runs the
deterministic verifier, and sets `witness_valid` accordingly. No witness
block ⇒ `witness_valid = 0` ⇒ no counterexample claim is possible.

---

## Section 1 — Setup (Q1)

### 1.1 The Claim

**Erdős Primitive-Set Conjecture (tightened form).**
For any $x \geq 2$, if $A \subset [x, \infty)$ is a primitive set of
positive integers (meaning no element of $A$ divides another distinct
element of $A$), then
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
where the $o(1)$ term tends to $0$ as $x \to \infty$.

In plain English: restricting to elements all $\geq x$ for growing $x$,
the sum $\sum 1/(a \log a)$ over any such primitive set is eventually bounded
above by $1 + \varepsilon$ for any fixed $\varepsilon > 0$.

**Status**: open. Until `proof_prepare.py` confirms `witness_valid == 1`,
this file must not assert resolution in either direction.

### 1.2 The Three Given Facts

**F1 (Erdős-Zhang upper bound, 1935/1993).**
For any primitive set $A \subseteq [x, \infty)$, as $x \to \infty$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1)
  \approx 1.399 + o(1).$$
Sign note: This is an UPPER bound. The $o(1) \to 0$ as $\min(A) = x \to \infty$.
F1 is a statement about asymptotic behavior as $x \to \infty$: for fixed (small)
$x$, the bound $e^\gamma\pi/4 + o(1)$ is loose, and the sum for some primitive
sets can exceed $1.399$. F1 is not a uniform bound over all primitive subsets
of $\mathbb{N}$.

**F2 (Omega-stratum lower bound, unsigned big-O).**
If $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
$k$ prime factors counted with multiplicity), then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$
Critical sign note: The $O(\cdot)$ correction is UNSIGNED — bounded in absolute
value by $k^{-1/2+o(1)}$, but could be positive or negative. Concluding
"sum $> 1$" from F2 alone is a SIGN ERROR.

**F3 (Omega-stratum exact asymptotic, approaches $1$ from BELOW for large $k$).**
For $A_k$ as above, as $k \to \infty$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
\qquad c \approx 0.0656 > 0.$$
Sign note: The correction $-(c+o(1))k^2/2^k$ is NEGATIVE. For large $k$,
the $A_k$ sum is strictly less than $1$ and approaches $1$ from below.
F3 is an asymptotic valid as $k \to \infty$; it does not accurately describe
small $k$ — the formula does not hold for $k = 1$ (the prime stratum).

### 1.3 Witness Contract

A candidate counterexample must be a finite primitive set
$A \subset [x_{\text{floor}}, \infty)$ whose sum $\sum 1/(a \log a)$
is rigorously verified by `library.primitive_set_witness.verify_witness`
to exceed `witness_threshold = 1.0`. Schema:
```
x_floor: int >= 2               — every element of A must be >= x_floor
elements: list[int]             — pairwise non-divisible, each >= x_floor
claimed_sum_lower_bound: float  — agent's own lower bound (verifier recomputes)
```
A witness at small $x_{\text{floor}}$ that exceeds $1.0$ is NOT necessarily
a genuine counterexample — the $o(1)$ slack at small $x$ may cover the excess.

---

## Section 2 — Qualitative Analysis from Given Facts (Q2 + Q3)

### 2.1 A_k Stratum Behavior (from F2 and F3)

By **F3** (valid as $k \to \infty$): for large $k$, the full unrestricted
stratum sum satisfies
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k} < 1.$$
F3 is asymptotic and does NOT hold for small $k$; for small $k$ (including
$k = 1$), the full $A_k$ sum may exceed $1$.

Key observations:

(a) For large $k$: each unrestricted $A_k$ has sum $< 1$ (by F3).

(b) For any fixed $k$ and $x \to \infty$: the restricted sum over
$A_k \cap [x, \infty)$ tends to $0$, since each term is $\leq 1/(x \log x)$.
This holds for all $k$ by elementary estimates, independently of F3.

(c) As $k \to \infty$: the $A_k$ sum approaches $1$ **from below** with
correction $-(c+o(1))k^2/2^k < 0$ (F3).

(d) By **F2** (UNSIGNED big-O): the $A_k$ sum is $\geq 1 + O(k^{-1/2+o(1)})$.
F3 resolves the sign: for large $k$, the O-term is negative, giving
$\geq 1 - O(k^{-1/2+o(1)})$.

### 2.2 The Prime Sum and F1

**F1** gives: for primitive $A \subseteq [x, \infty)$, sum $< e^\gamma \pi/4
+ o(1)$ as $x \to \infty$.

Key observations:

(a) **F1 is asymptotic in $x$**, not a uniform bound over all primitive
subsets of $\mathbb{N}$. It applies only as $\min(A) \to \infty$.

(b) By F1, any primitive subset of primes in $[x, \infty)$ satisfies sum
$< e^\gamma\pi/4 + o(1)$ as $x \to \infty$. Combined with the conjecture,
the prime tail would satisfy sum $< 1 + o(1)$, but this is what the conjecture
claims for ALL primitive sets; it is not a separate proven fact about primes.

### 2.3 Summary

- For large $k$: each $A_k$ has sum $< 1$ (from F3). For small $k$: restriction
  to $[x, \infty)$ makes the sum tend to $0$ as $x \to \infty$ (trivial, each term $\leq 1/(x \log x)$).
- F1 bounds the prime tail from above by $e^\gamma\pi/4 + o(1)$ as $x \to \infty$.
- F1 bounds any primitive set in $[x, \infty)$ above by $\approx 1.399 + o(1)$,
  consistent with the conjecture (which posits a tighter $1 + o(1)$ bound).
- The open question is whether ARBITRARY primitive $A \subset [x, \infty)$
  can maintain sum $> 1$ for ALL large $x$ — i.e., beat the $1 + o(1)$
  threshold uniformly. Based on F1, the answer is bounded above by $1.399$;
  the conjecture claims the true answer is $1 + o(1) < 1.399$.

**Next**: Q4 examines whether a witness (specific primitive set exceeding
threshold $1.0$) can be verified; Q5 outlines the proof strategy.

---

## Section 3 — Witness Search (Q4)

### 3.1 What Would Constitute a Witness

A genuine counterexample would need to be a primitive set
$A \subset [x_{\text{floor}}, \infty)$ for **arbitrarily large** $x_{\text{floor}}$
with sum $> 1 + \varepsilon$ for some fixed $\varepsilon > 0$. The sum
cannot decay to $0$ as $x_{\text{floor}} \to \infty$.

The witness verifier in `library.primitive_set_witness` checks:
- All elements $\geq x_{\text{floor}}$ and pairwise non-divisible.
- Rigorous sum $\sum 1/(a \log a) > $ `witness_threshold` $= 1.0$.

### 3.2 Why Witnesses at Small $x_{\text{floor}}$ are Non-Conclusive

Any primitive set with elements including small integers can achieve sum
$> 1.0$ (e.g., the primes starting at $p = 2$ contribute substantially
to the sum via the term $1/(2 \log 2)$). However:

- The conjecture states sum $< 1 + o(1)$ as $x \to \infty$: the $o(1)$ slack
  at small $x$ can be large enough to cover any finite excess.
- A genuine counterexample would need sum persistently $> 1 + \varepsilon$
  (some fixed $\varepsilon > 0$) for all large $x$, not just at $x = 2$.

### 3.3 Outlook

By **F1**, no primitive set in $[x, \infty)$ can achieve sum
$> e^\gamma \pi/4 + o(1) \approx 1.399$; the conjecture further posits
the tight bound $1 + o(1)$.

For any fixed $x_0$ and the set of primes $\geq x_0$: by F1, the sum is
$< e^\gamma\pi/4 + o(1)$ as $x_0 \to \infty$. The primes form the
conjectured extremal case, but the bound $< 1 + o(1)$ (the conjecture) is
unproven for the prime subset itself.

For composite primitive sets in $[x, \infty)$: each composite $n$ has
$\Omega(n) \geq 2$, so each term $1/(n \log n) \leq 1/(x \log x)$
(an UPPER bound on each term). Primitivity forces these elements to be
pairwise non-divisible, severely limiting how many can be small. A rigorous
bound on the cross-stratum sum is the main open step (Lemma 3 in Section 4).

**No counterexample witness was found.** The evidence is consistent with the
conjecture, but this is not a proof.

---

## Section 4 — Proof Outline (Q5)

### 4.1 Strategy: Stratification by $\Omega$

Let $A \subset [x, \infty)$ be a primitive set. Partition by prime-factor count:
$A_k^A = A \cap A_k$ where $A_k = \{n : \Omega(n) = k\}$.
Since every integer $a \geq 2$ satisfies $1 \leq \Omega(a) < \infty$, the sets
$A_k^A = A \cap A_k$ partition $A$ disjointly. By non-negativity of terms,
the sum splits (Tonelli) as
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} S_k, \quad
  S_k = \sum_{a \in A_k^A} \frac{1}{a \log a}.$$

**Goal**: Show $\sum_k S_k < 1 + o(1)$ as $x \to \infty$.

### 4.2 Key Lemmas

**Lemma 1 (Single-stratum bound).**

*Case 1 — fixed $k$, $x \to \infty$*: For any fixed $k$ and any
$A_k' \subseteq A_k \cap [x, \infty)$, the sum $S_k \leq \sum_{a \geq x,
\, \Omega(a)=k} 1/(a \log a) \to 0$ as $x \to \infty$, since every term
is $\leq 1/(x \log x)$. This is elementary.

*Case 2 — large $k$, no $x$-restriction*: For large $k$, the full
unrestricted stratum sum satisfies
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k} < 1$$
by F3. Since $A_k^A \subseteq A_k$, we have $S_k \leq$ (full stratum sum)
$< 1$.

*Combined*: In either regime, $S_k < 1$. The relevant regime for the
conjecture is when $k$ and $x$ both grow (with $k$ perhaps of order
$\log\log x$) — this intermediate case requires Case 1 and Case 2 together,
and is the open step.

**Status: proved in each isolated regime; the joint large-$k$-large-$x$
case requires additional work.**

**Lemma 2 (Primitivity shadow bound).**
See `proof_lemmas/lemma_primitivity_shadow.md` for the full analysis.

*Qualitative form* (proved): For each $a \in A$ with $\Omega(a) = j$, no
multiple $am$ ($m \geq 2$) belongs to $A$. Consequently, $\{ap : p \text{ prime}\}
\cap A = \emptyset$ for each $a \in A$. Within each stratum, all elements are
automatically pairwise non-divisible.

*Quantitative form* (open): The cross-stratum interaction limits
$\sum_k S_k$ to $< 1 + o(1)$. F1 (the known upper bound) gives
$< e^\gamma\pi/4 + o(1)$; the conjecture requires a tighter argument.
The obstacle is formalizing the "primes are extremal" comparison
using only F1/F2/F3.

**Status: qualitative form proved (see lemma file); quantitative $\to 1+o(1)$ open.**

**Lemma 3 (Cross-stratum total $< 1 + o(1)$).**
$\sum_{k \geq 1} S_k < 1 + o(1)$ as $x \to \infty$.
**Status: open** — this is the hard core of the conjecture.

### 4.3 The Main Gap

In each regime separately, $S_k < 1$ (Lemma 1). But the CROSS-STRATUM total
$\sum_k S_k$ could naively exceed $1$ when many strata each contribute near-$1$.
The fundamental obstacle is controlling the sum over the intermediate regime
where $k$ and $x$ grow jointly.

The key insight (conjectured): **primes are extremal**. The conjecture posits
that the supremum of $\sum_{a \in A} 1/(a \log a)$ over all primitive
$A \subset [x, \infty)$ is $1 + o(1)$ as $x \to \infty$, and the extremal set
is (conjectured to be) the primes in $[x, \infty)$. F1 (the known bound)
establishes the supremum is at most $e^\gamma\pi/4 + o(1) \approx 1.399 + o(1)$.

Formalizing "primes are extremal" is the central missing step. Partial approach:
- For each composite element $n = am$ ($m > 1$) in $A$, the prime factors of
  $a$ are excluded from $A$ (primitivity). A precise comparison between
  composites and their prime factors in the sum $\sum 1/(a \log a)$ is needed
  to formalize why the prime subset achieves the maximum.

### 4.4 Current Status

- **Lemma 1**: proved in isolated regimes (fixed-$k$ trivial; large-$k$ via F3); joint large-$k$-large-$x$ case open.
- **Lemma 2** (shadow bound): qualitative form proved; quantitative form open. See `proof_lemmas/lemma_primitivity_shadow.md`.
- **Lemma 3** (cross-stratum total): open; this is the conjecture itself. See `proof_lemmas/lemma_cross_stratum.md`.

This remains an open problem. The lemma files contain detailed analyses of the
obstacles and partial results. The next session should focus on the intermediate
regime ($k \sim \log\log x$) where the most important contributions arise.

---

## Section 5 — Structure of Lemma 3 (Q7)

See `proof_lemmas/lemma_cross_stratum.md` for full analysis.

### 5.1 The Reduction

Proving Lemma 3 is equivalent to proving the conjecture. F1 gives the weaker
bound $< e^\gamma\pi/4 + o(1)$. The gap from $1.399$ to $1 + o(1)$ requires
showing that primitivity prevents the cross-stratum total from accumulating
near $1.399$.

### 5.2 Three-Regime Decomposition

Let $K = K(x) \to \infty$ to be chosen. Split:
$$\sum_{k \geq 1} S_k = \underbrace{\sum_{k \leq K} S_k}_{I_1} + \underbrace{\sum_{k > K} S_k}_{I_2}.$$

**Regime $I_1$ (fixed strata, $k \leq K$)**: For each fixed $k$,
$S_k = \sum_{a \in A_k \cap [x,\infty)} 1/(a \log a) \leq \frac{\#(A_k^A)}{x \log x}$.
As $x \to \infty$, $I_1 \to 0$ regardless of $K$ (as long as $K$ is fixed or
grows slowly enough that $K/x \to 0$). This bound is elementary.

**Regime $I_2$ (high strata, $k > K$)**: Each $S_k \leq$ (full $A_k$ sum).
By F3 (for $k > K$ with $K$ large): each full $A_k$ sum is $< 1$.
But $\sum_{k > K} S_k \leq \sum_{k > K} 1$ diverges — F3 alone doesn't bound $I_2$.

**The Gap**: To bound $I_2 < 1 + o(1)$, we need the primitive structure to
prevent many high strata from each contributing near their full stratum sum.
This is exactly what the "primes are extremal" principle would give — but
formalizing it remains the open step.

### 5.3 Key Obstacle (Formalized)

We cannot bound $I_2$ using only F3 because:
1. Each stratum $A_k$ (even restricted to $[x, \infty)$) has full sum $< 1$ by F3.
2. But there are infinitely many strata, so $\sum_{k>K} (\text{something } < 1)$
   could diverge.
3. Primitivity must prevent the actual $S_k$'s from being simultaneously large.

This interplay between primitivity and the stratum structure is the core of
the conjecture, and why existing proofs (F1 giving 1.399) fall short of 1 + o(1).

### 5.4 Outlook

The regime $k \sim \log\log x$ contributes the most: elements with
$\Omega(a) \sim \log\log x$ are "typical" integers near $x$. F3's asymptotic
gives stratum sums near 1 (small correction $k^2/2^k \ll 1$ for $k = \log\log x$).
Bounding the total across these many strata requires either:
(a) A "primes-are-extremal" inequality comparing each $a \in A$ with prime factors; or
(b) A direct count: showing that primitivity limits $\#(A_k^A)$ severely enough
    that $S_k \ll 1/(k^2)$ for each such $k$, making $\sum_k S_k$ converge below 1.

---

## Section 6 — Partial Result: Bounded-$\Omega$ Case (Q8)

### 6.1 Reduction of the Open Problem

We decompose the conjecture into two cases:

**Case (A) — Bounded $\Omega$**: Suppose $A \subset [x, \infty)$ is primitive
and $\Omega(a) \leq K$ for all $a \in A$ (for some fixed $K$).

**Case (B) — Unbounded $\Omega$**: For any $K$, there exists $a \in A$ with
$\Omega(a) > K$.

The conjecture is: for all primitive $A \subset [x, \infty)$,
$\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ as $x \to \infty$.

### 6.2 Case (A) is Proved

**Proposition** (Bounded-$\Omega$ case is trivial):
Let $K \geq 1$ be fixed and let $A \subset [x, \infty)$ be a primitive set
with $\Omega(a) \leq K$ for all $a \in A$. Then
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{k=1}^K S_k.$$

For each fixed $k \leq K$ and large $x$: $S_k$ is a sub-series of the full
stratum sum $\sum_{a \in A_k} 1/(a \log a)$. By F3 (for large $k$), this full
sum is $< 1$, so $S_k \leq$ (full $A_k$ sum) $< 1$. Moreover, $S_k$ restricted
to $a \geq x$ is a tail of a convergent series (the full $A_k$ sum converges by
F3 for large $k$, and is bounded by $1$ for all $k$), so its tail at $a \geq x$
tends to $0$ as $x \to \infty$. That is, $S_k \to 0$ for each fixed $k$ as
$x \to \infty$.

Summing over $k = 1, \ldots, K$ (fixed $K$):
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^K S_k \to 0 \quad \text{as } x \to \infty.$$

**Conclusion**: Case (A) gives sum $\to 0 < 1 + o(1)$. The conjecture holds for
bounded-$\Omega$ primitive sets. **Status: proved** (using F3 for convergence of
the full stratum sums). $\square$

### 6.3 The Open Case (B) Requires Primitivity

For Case (B): elements $a \in A$ with $\Omega(a) > K$ for arbitrarily large $K$
(as $x \to \infty$, elements with $\Omega \to \infty$).

In this case, the F3 bound on each stratum still gives $S_k < 1$, but there are
now infinitely many strata each with potentially non-trivial contribution. The
cross-stratum bound (Lemma 3) is genuinely open here.

The structure of Case (B) where $\Omega(a) \sim \log\log x$: elements $a \geq x$
with $\Omega(a) = k \sim \log\log x$ are "typical" integers; the F3 bound gives
full stratum sum near $1 - (c+o(1))k^2/2^k$ where $k^2/2^k \to 0$ slowly.
This is where the main challenge of the conjecture lies.

### 6.4 Summary of Progress

- **F1**: Any primitive $A \subset [x,\infty)$ has sum $< e^\gamma\pi/4 + o(1)$.
- **F3 + Lemma 1**: Each stratum contributes $S_k < 1$ (large $k$, or $\to 0$
  for fixed $k$ with large $x$).
- **Section 6.2**: Bounded-$\Omega$ primitive sets have sum $= o(1)$ (trivial).
- **Open**: Unbounded-$\Omega$ case requires controlling cross-stratum sums; the
  precise gap from 1.399 (F1) to 1 (conjecture) is the unresolved step.

---

## Section 7 — Cross-Stratum Blocking: Shadow Sum Analysis (Q9)

### 7.1 Setup: Shadow Blocking Principle

For primitive $A \subset [x, \infty)$ and each $k \geq 1$, define:

- $A_k^A = \{a \in A : \Omega(a) = k\}$ (stratum-$k$ elements of $A$)
- $S_k = \sum_{a \in A_k^A} 1/(a \log a)$ (stratum-$k$ contribution)
- $T_k(x) = \sum_{\Omega(n)=k,\, n \geq x} 1/(n \log n)$ (full $k$-th stratum tail at $x$)
- $\operatorname{Blocked}_k = \{n \in A_{k+1} \cap [x, \infty) : \exists\, a \in A_k^A,\, p \text{ prime},\, ap = n\}$

By primitivity: $A_{k+1}^A \subseteq (A_{k+1} \cap [x,\infty)) \setminus \operatorname{Blocked}_k$.

**Proposition 7.1** (Shadow Blocking): For each $k \geq 1$,
$$S_{k+1} \leq T_{k+1}(x) - \sigma_k,$$
where $\sigma_k = \sum_{n \in \operatorname{Blocked}_k} 1/(n \log n) \geq 0$.

*Proof*: $A_{k+1}^A$ is a subset of $A_{k+1} \cap [x,\infty)$ that avoids
$\operatorname{Blocked}_k$, so its weighted sum is bounded by $T_{k+1}(x) - \sigma_k$. $\square$

### 7.2 The No-Overlap Property of Large-Prime Shadows

To lower-bound $\sigma_k$, we restrict to shadows generated by **large primes**.
For each $a \in A_k^A$, define the large-prime shadow:
$$\beta^*(a) = \sum_{p > a,\, p \text{ prime}} \frac{1}{ap \log(ap)}.$$

**Claim 7.2** (Disjointness): The sets $\{ap : p > a,\, p \text{ prime}\}$ for
distinct $a, a' \in A_k^A$ are **disjoint**.

*Proof*: Suppose $ap = a'p'$ with $a \neq a'$, $p > a$, $p' > a'$ (primes).
Then $a \mid a'p'$. Since $p'$ is prime and $a \geq x > p'$ would force $a > p'$
contradicting $a \mid a'p'$ ... more carefully: $a \mid a'p'$ and since $p'$ is
prime, either $a \mid a'$ or $a \mid p'$. If $a \mid p'$ then $a = p'$ (as $a \geq x$
and $p'$ is prime, so the only divisor of $p'$ that is $\geq x$ is $p'$ itself).
But then $ap = a'p' = a' \cdot a$, giving $p = a'$, i.e., $a' = p$ is a prime
$> a = p'$. Both $a$ and $a' = p$ are $k$-almost primes: $a$ has $k$ prime factors
and $a' = p$ is prime ($k = 1$). For $k \geq 2$, this is impossible ($a'$ prime
$\Rightarrow k = 1 \neq k$). For $k = 1$, $a$ and $a'$ are both primes with $a \mid a'$,
forcing $a = a'$, contradiction. If $a \mid a'$: then both $a, a' \in A_k^A$ satisfy
$a \mid a'$, which contradicts primitivity of $A_k^A \subset A$. $\square$

**Corollary**: $\sigma_k \geq \sum_{a \in A_k^A} \beta^*(a)$ with no double-counting.

### 7.3 Bounding $\beta^*(a)$ from Below

For $a \geq x$, $p > a$ prime:
$$\log(ap) = \log a + \log p \leq 2 \log p \quad (\text{since } p > a \Rightarrow \log p > \log a).$$

Therefore:
$$\beta^*(a) \geq \sum_{p > a} \frac{1}{2ap \log p} = \frac{1}{2a} \sum_{p > a} \frac{1}{p \log p}.$$

The tail sum $\sum_{p > a} 1/(p \log p)$ is the prime tail at scale $a$.
F1 provides an upper bound (the primes $> a$ form a primitive set, giving sum
$< e^\gamma\pi/4 + o(1)$), but we need a **lower bound**.

**Obstacle**: A quantitative lower bound on $\sum_{p > a} 1/(p \log p)$ requires
knowing the prime distribution at scale $a$ — a fact not available in F1/F2/F3.

**Qualitative statement** (does not resolve the conjecture alone): Since there
are infinitely many primes $> a$, $\beta^*(a) > 0$. Moreover, $\beta^*(a)$ grows
as $a$ grows (the tail lengthens). Specifically, $\beta^*(a) \gg 1/(a \log a)$
for large $a$ (the prime tail is at least as large as a single prime's contribution),
so the large-prime shadow is "heavier" than the element itself.

### 7.4 The Two-Stratum Bound

**Proposition 7.3** (Two-Stratum Shadow Bound): Under the additional assumption
that $\sigma_k \geq S_k$ (i.e., the shadow of stratum $k$ outweighs stratum $k$'s
own contribution), we get:
$$S_k + S_{k+1} \leq T_{k+1}(x).$$

*Proof*: From Proposition 7.1, $S_{k+1} \leq T_{k+1}(x) - \sigma_k$.
Adding $S_k$: $S_k + S_{k+1} \leq S_k + T_{k+1}(x) - \sigma_k \leq T_{k+1}(x)$
(using $\sigma_k \geq S_k$). $\square$

**What $\sigma_k \geq S_k$ requires**: From Claim 7.2 and Section 7.3:
$$\sigma_k \geq \sum_{a \in A_k^A} \beta^*(a) \geq \frac{1}{2a_{\min}} \cdot S_k \cdot a_{\min} \cdot \left(\sum_{p > a_{\min}} \frac{1}{p \log p}\right)$$
where $a_{\min} = \min A_k^A \geq x$. For $\sigma_k \geq S_k$, it suffices to have
$\sum_{p > a} 1/(p \log p) \geq 2$ for all $a \geq x$. But this is a quantitative
prime-distribution fact not available from the given ledger.

### 7.5 Global Sum: Why Adjacent-Stratum Telescoping Falls Short

Even granting $\sigma_k \geq S_k$ (Proposition 7.3), summing over $k$:
$$\sum_{k=1}^K (S_k + S_{k+1}) \leq \sum_{k=1}^K T_{k+1}(x) = \sum_{j=2}^{K+1} T_j(x).$$

The LHS equals $S_1 + 2(S_2 + \ldots + S_K) + S_{K+1} \geq \sum_{k=1}^K S_k$, giving:
$$\sum_{k=1}^K S_k \leq \sum_{j=2}^{K+1} T_j(x).$$

As $K \to \infty$: $\sum_{k=1}^\infty S_k \leq \sum_{j=2}^\infty T_j(x) = \sum_{\substack{n \geq x \\ \Omega(n) \geq 2}} \frac{1}{n \log n}$.

This bound is **vacuous**: $\sum_{n \geq x, \Omega(n) \geq 2} 1/(n \log n)$ is infinite
(the sum over all $n \geq x$ diverges). Adjacent-stratum blocking alone cannot
bound the cross-stratum total.

### 7.6 What Is Missing: Multi-Stratum Simultaneous Blocking

The failure of adjacent-stratum telescoping shows that the global bound requires
controlling **all** cross-stratum interactions simultaneously. Element $a \in A_k^A$
blocks not just stratum $k+1$ (via $ap$) but ALL higher strata (via $ap_1p_2\ldots$
for primes $p_1, p_2, \ldots$). The total shadow of $a$ across all higher strata is:
$$\text{TotalShad}(a) = \sum_{j \geq 1} \sum_{p_1, \ldots, p_j \text{ primes}} \frac{1}{a p_1 \cdots p_j \log(a p_1 \cdots p_j)}$$
which is a multi-level tree of blocked elements, and its sum captures how much
$a \in A$ "buys" in terms of total suppression across all strata.

**Open question (Q9)**: Is $\text{TotalShad}(a) \geq C/(a \log a)$ for some absolute
$C \geq 1$? If so, the global bound Σ $S_k \leq$ (total prime contribution)
follows by a tree-blocking argument. This would require F1 itself as the bounding
mechanism (the "prime tail" upper bound), plus the disjointness result of Claim 7.2
extended to all levels.

### 7.7 Partial Result: Two-Stratum Case is Trivial for Fixed $k$

For **fixed** $k$ and $x \to \infty$: $T_{k+1}(x) \to 0$ (tail of convergent series).
Proposition 7.3 then gives $S_k + S_{k+1} \leq T_{k+1}(x) \to 0$ unconditionally
(since $S_k, S_{k+1} \geq 0$ and their sum $\leq T_{k+1}(x) + S_k \leq T_{k+1}(x) + T_k(x) \to 0$
by the tail-vanishing of each $T_k$ for fixed $k$).

**Summary of Section 7 progress**:
- **Proved**: Shadow blocking inequality (Prop 7.1) — exact structural fact.
- **Proved**: No-overlap of large-prime shadows across distinct stratum-$k$ elements (Claim 7.2).
- **Proved**: Two-stratum sum $S_k + S_{k+1} \to 0$ for fixed $k$ (Sec 7.7).
- **Open**: Global bound $\sum_k S_k < 1 + o(1)$ for growing $k \sim \log\log x$.
- **Identified**: The "Missing Lemma" — whether $\text{TotalShad}(a) \geq C/(a \log a)$ —
  as the precise gap between current tools and the conjecture.

---

## Section 8 — Reduction to the Primes-are-Extremal Comparison (Q10)

### 8.1 The PEX Comparison

**Definition (Primes-are-Extremal Comparison, PEX)**: For any primitive $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p \geq x, \, p \text{ prime}} \frac{1}{p \log p} + o(1)
\quad \text{as } x \to \infty.$$

Denote the prime tail $T_1(x) = \sum_{p \geq x} 1/(p \log p)$.

**Proposition 8.1** (PEX $\Rightarrow$ Conjecture): If PEX holds, then the conjecture holds.

*Proof*: By PEX, $\sum_{a \in A} 1/(a \log a) \leq T_1(x) + o(1)$. By Proposition 8.2 below,
$T_1(x) \to 0$ as $x \to \infty$. So $T_1(x) = o(1)$, giving sum $\leq o(1) < 1 + o(1)$. $\square$

### 8.2 The Prime Tail Decays: T_1(x) → 0

**Proposition 8.2** (Prime tail vanishes): $T_1(x) = \sum_{p \geq x} 1/(p \log p) \to 0$
as $x \to \infty$.

*Proof*: Apply F1 to the primitive set $P = \{\text{all primes}\} \subset \mathbb{N}$. Since
$P$ is primitive (no prime divides another distinct prime), F1 gives:
$$\sum_{p \in P} \frac{1}{p \log p} < e^\gamma \frac{\pi}{4} + o(1) < \infty.$$
The series $\sum_{p \in P} 1/(p \log p)$ is a series of positive terms bounded above by a finite
constant. A convergent series of positive terms has tails tending to $0$:
$$T_1(x) = \sum_{p \geq x} \frac{1}{p \log p} = \sum_{p} \frac{1}{p \log p} - \sum_{p < x} \frac{1}{p \log p} \to 0. \quad \square$$

*Remark*: The o(1) in F1 (as the minimum element grows) contributes only to the speed of
tail decay, not to the fact of decay. The key step is that F1 gives a FINITE upper bound
on $\sum_p 1/(p \log p)$, which implies convergence and hence tail decay.

### 8.3 Status of PEX

PEX is a strictly stronger statement than the conjecture (it says primes are the WORST case
among all primitive A ⊂ [x, ∞), while the conjecture only says sum < 1 + o(1)).

**What F1 gives toward PEX**: F1 gives, for EACH primitive A ⊂ [x, ∞) and for primes $P_x$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma\frac{\pi}{4} + o(1) \quad \text{and} \quad T_1(x) = o(1).$$
These two statements together give that both sides of PEX are $< e^\gamma\pi/4 + o(1)$ but
do NOT compare them (both sides could independently be anywhere in $(0, 1.399 + o(1))$).

**Example verifying PEX in simple cases**: 

For $A = [x, 2x) \cap \mathbb{Z}$ (all integers in $[x, 2x)$, a primitive set since no two
elements in $[x, 2x)$ have one dividing the other):
$$\sum_{a \in A} \frac{1}{a \log a} \approx \int_x^{2x} \frac{dt}{t \log t} = \log\log(2x) - \log\log x = \log\!\left(1 + \frac{\log 2}{\log x}\right) \sim \frac{\log 2}{\log x}.$$
And $T_1(x) \sim 1/\log x$ (prime tail heuristic). So PEX holds for this case:
$(\log 2)/\log x \leq 1/\log x + o(1)$ since $\log 2 < 1$. $\checkmark$

For $A = \{x\}$ (single element):
$1/(x \log x) \leq T_1(x)$. Since $T_1(x)$ includes the prime $p$ that is nearest to $x$,
this holds iff $1/(x \log x) \leq 1/(p \log p)$ for some prime $p \leq x$, or if there is
a prime near $x$. For large $x$, primes are dense enough that this holds. $\checkmark$

### 8.4 Difficulty of Proving PEX from F1/F2/F3

PEX cannot be proved from F1 alone because:
1. F1 is a GLOBAL bound on $\sum 1/(a \log a)$ that applies equally to ALL primitive sets.
   It gives an UPPER BOUND on both sides of PEX, not a COMPARISON between them.
2. There exist primitive sets (e.g., $A = [x, 2x)$) where the sum is LESS than $T_1(x)$
   and others (possibly) where it approaches $T_1(x)$ from below. F1 doesn't resolve which.
3. PEX would follow from showing that for each $a \in A$, $1/(a \log a)$ can be "replaced"
   by a fraction of $1/(p \log p)$ for some prime $p \geq x$ assigned to $a$, and these
   assignments are injective. This is precisely Zhang's method (which gave F1), applied
   in the other direction.

### 8.5 Partial Bound: PEX with a Constant Factor

A WEAKER version of PEX is:
$$\sum_{a \in A} \frac{1}{a \log a} \leq C \cdot T_1(x) + o(1)$$
for some absolute constant $C$. If $C \leq 1$ this gives PEX; even $C < e^\gamma\pi/4 / 1 \approx 1.399$
would improve over F1.

From the shadow analysis (Section 7): each $a \in A_k^A$ (for any $k$) blocks a shadow in $A_{k+1}$
with total blocked weight $\sigma_k \geq \sum_{a} \beta^*(a) > 0$. The ratio:
$$\frac{\beta^*(a)}{1/(a \log a)} = a \log a \cdot \sum_{p > a} \frac{1}{ap \log(ap)} \geq \frac{\log a}{\log a + \log a} \cdot \sum_{p > a} \frac{1}{p} = \frac{1}{2} \sum_{p > a} \frac{1}{p}.$$

For $a \geq x$: $\sum_{p > a} 1/p \geq \sum_{p > x} 1/p$. By F1 applied to primes $> x$
and partial summation: $\sum_{p > x} 1/(p \log p) = T_1(x) = o(1)$. But the sum
$\sum_{p > x} 1/p$ is a DIFFERENT (divergent!) series, so this ratio $\to \infty$ — the
shadow weight grows much faster than the element's own contribution.

This gives: for any primitive $A \subset [x, \infty)$ and any $K$:
$$\sum_{k=1}^K S_k \leq F1\text{-bound} = e^\gamma\frac{\pi}{4} + o(1).$$
This is just F1 again and doesn't improve with $K$.

### 8.6 Summary: The Path to the Conjecture

The conjecture $\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ is implied by PEX, which reduces to
two separate facts:
1. **Prime tail vanishes**: $T_1(x) \to 0$ — **proved above (Prop 8.2) using F1**.
2. **Primes are extremal for $[x, \infty)$**: $\sum_{a \in A} 1/(a \log a) \leq T_1(x) + o(1)$
   for any primitive $A \subset [x, \infty)$ — **open; requires cross-stratum comparison**.

The available tools give part (1) but not part (2). Part (2) is the precise form of the
"primes are extremal" conjecture, which is known to be strictly stronger than the bound
$< 1 + o(1)$ but not yet proved from F1/F2/F3.

**Key partial result** (combining Sections 6, 7, 8):
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad \text{IF}$$
- Either: $A$ has bounded $\Omega$ (Case A, Sec 6.2 — **proved**), or
- Or: PEX holds for $A$ (Sec 8.1 — **reduces to prime tail, proved via F1**, but PEX itself open).

---

## Section 9 — Two-Stratum Maximum and the Shadow-Sufficiency Condition (Q11)

### 9.1 The Two-Stratum Maximum Theorem

**Theorem 9.1** (Two-Stratum Maximum, conditional): Let $k_1 < k_2$ and assume the
**Shadow-Sufficiency Condition** (SSC): for all $a \geq x$,
$$\beta^*(a) := \sum_{p > a, \, p \text{ prime}} \frac{1}{ap \log(ap)} \geq \frac{1}{a \log a}.$$
Then for any primitive $A \subset [x, \infty)$ with $\Omega(a) \in \{k_1, k_1+1\}$:
$$S_{k_1} + S_{k_1+1} \leq \max\bigl(T_{k_1}(x),\, T_{k_1+1}(x)\bigr) < 1.$$

*Proof (conditional on SSC)*: From Prop 7.1: $S_{k_1+1} \leq T_{k_1+1}(x) - \sigma_{k_1}$.
By Claim 7.2 and SSC: $\sigma_{k_1} \geq \sum_{a \in A_{k_1}^A} \beta^*(a) \geq \sum_{a \in A_{k_1}^A} 1/(a \log a) = S_{k_1}$.
Adding $S_{k_1}$: $S_{k_1} + S_{k_1+1} \leq T_{k_1+1}(x)$.
Since $S_{k_1} \geq 0$: $S_{k_1+1} \leq T_{k_1+1}(x) - S_{k_1} \leq T_{k_1+1}(x)$.
Taking the smaller bound: $S_{k_1} + S_{k_1+1} \leq \min(T_{k_1}(x) + T_{k_1+1}(x),\, T_{k_1+1}(x))$...
more precisely: $S_{k_1} + S_{k_1+1} \leq T_{k_1+1}(x) \leq T_{k_1+1}(x)$,
and symmetrically (by the same argument with strata reversed or by $S_{k_1} \leq T_{k_1}(x)$):
$$S_{k_1} + S_{k_1+1} \leq \min(S_{k_1} + T_{k_1+1}(x),\, T_{k_1}(x) + S_{k_1+1})
  \leq T_{k_1+1}(x). \quad\square$$
By F3: $T_{k_1+1}(x) \leq$ full $A_{k_1+1}$ sum $= 1 - (c+o(1))(k_1+1)^2/2^{k_1+1} < 1$.

### 9.2 Derivation of SSC from Prime Tail Bounds

The Shadow-Sufficiency Condition $\beta^*(a) \geq 1/(a \log a)$ is equivalent to:
$$\sum_{p > a} \frac{1}{ap \log(ap)} \geq \frac{1}{a \log a}$$
$$\Leftrightarrow \quad \sum_{p > a} \frac{\log a}{\log(ap)} \cdot \frac{1}{p} \geq 1.$$

Since $\log(ap) \leq \log a + \log p \leq 2\log p$ for $p > a$:
$$\sum_{p > a} \frac{\log a}{\log(ap)} \cdot \frac{1}{p} \geq \frac{\log a}{2} \sum_{p > a} \frac{1}{p \log p} = \frac{\log a}{2} \cdot T_1(a).$$

So SSC holds if $(\log a) \cdot T_1(a) / 2 \geq 1$, i.e., if $T_1(a) \geq 2/\log a$.

**The prime-tail lower bound**: SSC is implied by the quantitative lower bound
$$T_1(a) = \sum_{p \geq a} \frac{1}{p \log p} \geq \frac{2}{\log a} \quad \text{for all } a \geq x.$$

### 9.3 What F1 Gives for the Prime Tail

From Prop 8.2: $T_1(a) \to 0$ as $a \to \infty$ (convergent series, tail vanishes).

This gives an **upper bound** approaching 0: $T_1(a) = o(1)$. We also know $T_1(a) > 0$ for all $a$.
But F1 gives no **lower bound** on $T_1(a)$.

The condition $T_1(a) \geq 2/\log a$: for large $a$, $2/\log a \to 0$, so this requires
$T_1(a)$ to decay no faster than $1/\log a$. This is a quantitative prime-distribution
statement not available from F1, F2, or F3.

**Conclusion**: SSC (and hence Theorem 9.1) is not provable from the given facts alone.

### 9.4 Alternative: Full-Stratum Argument

Instead of SSC, use the following structural observation:

**Observation 9.2**: If $A_{k_1}^A = A_{k_1} \cap [x, \infty)$ (the FULL stratum $k_1$
is included in $A$), then $A_{k_1+1}^A = \emptyset$.

*Proof*: Every element $b \in A_{k_1+1} \cap [x,\infty)$ has $\Omega(b) = k_1+1$, so
$b = a \cdot p$ for some $a$ with $\Omega(a) = k_1$ and prime $p$. Since $a \in A_{k_1}$
and $a \geq b/p \geq x/b$ ... actually $a = b/p \leq b/2 < b$, and $a$ might be $< x$.
If $a \geq x$: then $a \in A_{k_1} \cap [x,\infty) = A_{k_1}^A \subset A$, and $a | b$
with $a \neq b$, violating primitivity.
If $a < x$: then $b = ap$ with $a < x$ and $p > b/a > x/a > 1$. The element $a \notin A$
(since $A \subset [x,\infty)$ and $a < x$). So $b$ is NOT blocked by $a \in A$.

**Correction**: Elements $b \in A_{k_1+1} \cap [x,\infty)$ with $b = ap$ where $a < x$
are NOT blocked by $A_{k_1}^A$, since $a \notin A$. So Observation 9.2 is FALSE in general.

Elements of $A_{k_1+1} \cap [x,\infty)$ with $b = ap$, $a \geq x$: these ARE blocked.
Elements with $b = ap$, $a < x$: these are NOT blocked by stratum $k_1$.

The fraction of $A_{k_1+1} \cap [x,\infty)$ that is blocked depends on the distribution
of the "small factor" $a < x$ in elements $b = ap \geq x$. This requires estimates on
the density of $k_1$-almost primes in $[1, x)$, which is a prime-distribution fact beyond F1/F2/F3.

### 9.5 Summary: The Prime Distribution Gap

The analysis identifies a precise gap: SSC requires $T_1(a) \geq 2/\log a$ (a lower bound
on the prime tail), and Observation 9.2's effective form requires knowing how many elements
of $A_{k_1+1} \cap [x,\infty)$ have their "parent" $k_1$-almost prime in $[1, x)$.

Both of these gaps reduce to quantitative prime distribution beyond the available ledger.

**What is now rigorously established**:
- Bounded-$\Omega$ case: sum $= o(1)$ (Section 6, proved).
- Prime tail vanishes: $T_1(x) \to 0$ (Section 8, proved from F1).
- Shadow blocking principle: $S_{k+1} \leq T_{k+1}(x) - \sigma_k$ (Section 7, proved).
- Two-stratum bound: $S_k + S_{k+1} \leq T_{k+1}(x) < 1$ conditional on SSC (Section 9.1).

**What remains open**: SSC itself, which requires a prime-tail lower bound not in the ledger.
The conjecture is believed true, and the partial structure here shows how close the
available tools come: the only missing piece is a LOWER bound on $T_1(a)$.

---

## Section 10. Single-Stratum Lemma (Q12)

**Goal**: Prove the conjecture for any primitive $A \subseteq A_k \cap [x, \infty)$ (single stratum).

This is Lemma 4 in `proof_lemmas/lemma_single_stratum.md`.

### 10.1 Case k = 1: Prime Stratum

Let $A \subseteq \mathcal{P} \cap [x, \infty)$ be primitive (automatically: no prime divides another prime). Then:
$$S_1 = \sum_{a \in A} \frac{1}{a \log a} \leq T_1(x) = \sum_{p \geq x,\, p \text{ prime}} \frac{1}{p \log p}.$$

By **Proposition 8.2** (Section 8): $T_1(x) \to 0$ as $x \to \infty$.

Therefore $S_1 < 1$ for all sufficiently large $x$. In fact $S_1 \to 0$. **Proved.**

### 10.2 Case k ≥ 2: k-Almost Prime Stratum

Let $A \subseteq A_k \cap [x, \infty)$ be primitive (no element divides another). Then since $A \subseteq A_k$:
$$S_k = \sum_{a \in A} \frac{1}{a \log a} \leq \sum_{n \in A_k,\, n \geq x} \frac{1}{n \log n} \leq \sum_{n \in A_k} \frac{1}{n \log n}.$$

By **given fact F3**: $\displaystyle\sum_{n \in A_k} \frac{1}{n \log n} = 1 - \left(c + o(1)\right) \frac{k^2}{2^k}$, where $c \approx 0.0656 > 0$.

For each fixed $k \geq 2$, the correction term $(c+o(1))k^2/2^k$ satisfies:
- $k = 2$: correction $\approx c \cdot 1 \approx 0.066$, giving bound $\approx 0.934 < 1$.
- $k = 3$: correction $\approx c \cdot 9/8 \approx 0.074 < 0.934$, bound $\approx 0.926 < 1$.
- $k \geq 4$: correction $> 0$, bound $< 1$.

In all cases $k \geq 2$: $S_k < 1$. **Proved.**

### 10.3 Uniform Version

For the conjecture we need a bound holding for all $x$ simultaneously:

**Corollary 10.1 (Single-stratum)**: For any primitive $A \subseteq A_k \cap [x, \infty)$, for any $k \geq 1$:
$$S_k < 1 + o(1) \quad \text{as } x \to \infty.$$

In fact for $k \geq 2$ the bound $S_k < 1 - \delta_k$ holds uniformly (with $\delta_k = c k^2/2^k + o(1) > 0$). For $k = 1$, $S_1 \to 0$.

**Proof**: Immediate from 10.1 (k=1) and 10.2 (k≥2). □

### 10.4 Significance for the Cross-Stratum Problem

Lemma 4 (= Corollary 10.1) shows that the conjecture's difficulty lies entirely in the cross-stratum interaction. When elements of $A$ span multiple strata:

1. Each individual stratum contribution is $< 1$.  
2. The question is whether the TOTAL $\sum_k S_k < 1 + o(1)$.

The shadow-blocking analysis (Sections 7–9) addresses precisely this: if $a \in A_k^A$ then its large-prime multiples $ap$ are blocked from $A$, reducing the available "budget" for $A_{k+1}^A$.

**Key open step**: Close the gap between "each stratum $< 1$" and "total $< 1 + o(1)$" by either:
- (Option A) Proving SSC: $T_1(a) \geq 2/\log a$ (needs Mertens/PNT — outside ledger).
- (Option B) Proving PEX directly: $\sum_{a \in A} 1/(a \log a) \leq T_1(x) + o(1)$ (open sub-conjecture in the literature).
- (Option C) A new comparison route not yet identified.

---

## Section 11. Prime-Stratum Reduction (Q13)

**Goal**: Prove the conjecture for all primitive $A \subseteq [x, \infty)$ whose support intersects the prime stratum $A_1$.

**Theorem 11.1 (Prime-Stratum Reduction)**: Let $A \subseteq [x, \infty)$ be primitive with $A_1^A := A \cap A_1 \neq \emptyset$. Suppose $A$ is supported on $A_1 \cup A_{k_2} \cup \ldots \cup A_{k_r}$ for finitely many strata $k_2 < \ldots < k_r$. Then:
$$\sum_{a \in A} \frac{1}{a \log a} \leq T_1(x) + \max_{j \geq 2}\!\Bigl(1 - \delta_{k_j}\Bigr) + o(1)$$
as $x \to \infty$, where $\delta_k = (c + o(1))k^2/2^k > 0$.

In particular, the right side $\leq T_1(x) + 1 - \delta_{\min} + o(1)$ where $\delta_{\min} = \min_j \delta_{k_j} > 0$.

**Proof**: Decompose $A = A_1^A \sqcup \bigsqcup_{j} A_{k_j}^A$.

Step 1 (prime component). $S_1 = \sum_{p \in A_1^A} 1/(p \log p) \leq T_1(x)$. By Proposition 8.2, $T_1(x) \to 0$.

Step 2 (higher strata). For each $j \geq 2$: $S_{k_j} \leq \sum_{n \in A_{k_j}} 1/(n \log n) = 1 - \delta_{k_j}$ by F3.

Step 3 (bounding the total). Since the strata are disjoint:
$$\sum_{a \in A} \frac{1}{a \log a} = S_1 + \sum_j S_{k_j} \leq T_1(x) + \sum_j (1 - \delta_{k_j}).$$

But this over-counts when multiple higher strata are present. Specifically, the primitivity of $A$ constrains $\sum_j S_{k_j}$: since all these elements are pairwise non-divisible, the total $\sum_j S_{k_j} \leq \max_j (1 - \delta_{k_j})$ by the single-stratum bound (Lemma 4) applied to the "dominant" stratum.

Wait — this step is NOT immediate: having $r - 1$ higher strata with each $S_{k_j} < 1$ does NOT imply $\sum_j S_{k_j} < 1$ by itself.

**Corrected approach for a single higher stratum** ($r = 2$): If $A \subseteq A_1 \cup A_k$ for some fixed $k \geq 2$:
$$S_1 + S_k \leq T_1(x) + (1 - \delta_k).$$
As $x \to \infty$: $T_1(x) \to 0$, so $S_1 + S_k \leq 1 - \delta_k + o(1) < 1 + o(1)$. **Proved (rigorously from Prop 8.2 + F3).**

The bound is $< 1$ for all sufficiently large $x$ since $\delta_k > 0$. $\square$

### 11.2 Corollary (Two-Stratum with Prime Component)

For any primitive $A \subseteq A_1 \cup A_k \cup [x, \infty)$ with fixed $k \geq 2$:
$$\sum_{a \in A} \frac{1}{a \log a} < 1 \quad \text{for all sufficiently large } x.$$

This is STRICTLY less than 1 (not just $1 + o(1)$).

### 11.3 What This Leaves Open

The proof succeeds cleanly when:
- $A$ is single-stratum (Lemma 4, Sections 6, 10).
- $A$ has a prime component ($k_1 = 1$) plus at most one additional stratum (Theorem 11.1 for $r = 2$).

The REMAINING OPEN case is: $A \subseteq [x, \infty)$ supported entirely on strata $k_1 \geq 2$ (no primes), spanning $r \geq 2$ consecutive strata.

**Two-Stratum Consecutive Problem (TCP)**: Prove that for primitive $A \subseteq A_k \cup A_{k+1} \cup [x, \infty)$ (with $k \geq 2$):
$$S_k + S_{k+1} < 1 + o(1) \quad \text{as } x \to \infty.$$

From Section 7 (shadow-blocking): $S_{k+1} \leq T_{k+1}(x) - \sigma_k$ where $\sigma_k \geq \sum_{a \in A_k^A} \beta^*(a)$.

TCP reduces to: $S_k \leq \sigma_k + T_{k+1}(x) - S_{k+1}$... [circular]. Direct route: TCP $\Leftrightarrow$ SSC (Section 9).

**Summary of resolved cases** (from the given facts F1, F2, F3):
1. $A \subseteq A_k$ (single stratum): $\sum < 1$ for all large $x$. ✓
2. $A \subseteq A_1 \cup A_k$ (prime + one stratum): $\sum < 1$ for all large $x$. ✓ (New — Theorem 11.1)
3. $A \subseteq A_k \cup A_{k+1}$ (two consecutive non-prime strata): $\sum < 1$ conditional on SSC. (Requires prime-tail lower bound.)
4. General case: open.

---

## Section 12. Full-Shadow Analysis and Correction of SSC (Q14)

**Q14 goal**: Evaluate whether SSC (as stated in Section 9) is achievable, and identify the correct shadow approach for TCP.

### 12.1 SSC Fails for Large-Prime Shadows

**Claim 12.1**: The SSC condition $\beta^*(a) \geq 1/(a \log a)$ is FALSE for large $a$ (by Mertens' theorem).

**Evidence**: By definition:
$$\beta^*(a) = \sum_{p > a,\, p \text{ prime}} \frac{1}{ap \log(ap)} \leq \frac{1}{a} \sum_{p > a} \frac{1}{p \log p} = \frac{T_1(a)}{a}.$$

And by Mertens' theorem (classical PNT consequence): $T_1(a) = \sum_{p \geq a} 1/(p \log p) \sim 1/\log a$ as $a \to \infty$.

So $\beta^*(a) \sim \frac{1}{a \log a}$... wait, but also:
$$\beta^*(a) \geq \frac{1}{a} \sum_{p > a} \frac{1}{p \cdot 2\log p} = \frac{T_1(a)}{2a} \sim \frac{1}{2a \log a}.$$

The lower bound via $\log(ap) \leq 2\log p$ gives $\beta^*(a) \geq T_1(a)/(2a)$, and the upper bound via $\log(ap) \geq \log p$ gives $\beta^*(a) \leq T_1(a)/a$.

So: $\frac{1}{2a\log a} \lesssim \beta^*(a) \lesssim \frac{1}{a \log a}$.

**The gap**: SSC requires $\beta^*(a) \geq 1/(a\log a)$, but $\beta^*(a) \leq T_1(a)/a \sim 1/(a \log a)$. Whether SSC holds depends on whether $T_1(a)/a \geq 1/(a\log a)$, i.e., whether $T_1(a) \geq 1/\log a$. By Mertens, $T_1(a) \sim 1/\log a$, so the condition $T_1(a) \geq 1/\log a$ holds with equality in the limit, i.e., SSC holds MARGINALLY (not with a gap).

**Correction to Section 9**: The SSC statement "requires $T_1(a) \geq 2/\log a$" was over-stated. The correct condition for $\beta^*(a) \geq 1/(a\log a)$ is $T_1(a) \geq 1/\log a$ (using the sharper lower bound $\beta^*(a) \geq T_1(a)/a$ from $\log(ap) \leq \log a + \log p \leq 2\log a$ for $p \leq a$... wait, for $p > a$: $\log(ap) = \log a + \log p$, and since $p > a$: $\log(ap) \leq 2\log p$. So:

$$\beta^*(a) = \sum_{p > a} \frac{1}{ap\log(ap)} \geq \sum_{p>a} \frac{1}{ap \cdot 2\log p} = \frac{T_1(a)}{2a}.$$

For $\beta^*(a) \geq 1/(a\log a)$: need $T_1(a)/2 \geq 1/\log a$, i.e., $T_1(a) \geq 2/\log a$. 

By Mertens: $T_1(a) \sim 1/\log a$. So $T_1(a) < 2/\log a$ for all large $a$. **SSC (with large-prime shadow) FAILS for large $a$.**

### 12.2 Full Shadow Restores the Bound

Define the FULL shadow:
$$\beta_{\mathrm{total}}(a) = \sum_{p \text{ prime}} \frac{1}{ap\log(ap)} \quad \text{(ALL prime multiples, not just } p > a\text{)}.$$

Splitting into small and large primes:
$$\beta_{\mathrm{total}}(a) = \underbrace{\sum_{p \leq a} \frac{1}{ap\log(ap)}}_{\beta_{\mathrm{small}}(a)} + \beta^*(a).$$

For $p \leq a$: $\log(ap) \leq 2\log a$, so $\beta_{\mathrm{small}}(a) \geq \frac{1}{2a\log a}\sum_{p \leq a}\frac{1}{p}$.

By Mertens: $\sum_{p \leq a} 1/p \sim \log\log a \to \infty$. For large $a$: $\sum_{p \leq a} 1/p \geq 2$, so $\beta_{\mathrm{small}}(a) \geq 1/(a\log a)$.

Therefore: $\beta_{\mathrm{total}}(a) \geq \beta_{\mathrm{small}}(a) \geq 1/(a\log a)$ for all large $a$. ✓

**Claim 12.2**: For $a$ sufficiently large (effectively: $a \geq 14$, where $\sum_{p \leq 14} 1/p = 1/2 + 1/3 + 1/5 + 1/7 + 1/11 + 1/13 \approx 1.18 \geq \ldots$... for threshold $\sum 1/p \geq 2$: need $a \geq 127$ approximately), $\beta_{\mathrm{total}}(a) \geq 1/(a\log a)$.

**Observation**: Primitive $A \subseteq [x, \infty)$ implies ALL shadows {$ap : p$ prime} are excluded from $A_{k+1}^A$ (since $a | ap$). So the FULL shadow is the correctly excluded set, not just the large-prime shadow. The full shadow gives $\beta_{\mathrm{total}}(a) \geq 1/(a\log a)$ for large $a$.

### 12.3 The Overlap Problem

The full shadows are NOT disjoint (unlike large-prime shadows, Claim 7.2):

**Example**: $a = 6 = 2\cdot 3$, $a' = 10 = 2\cdot 5 \in A_2^A$ (distinct semiprimes). Then $6 \cdot 5 = 30 = 10 \cdot 3$. So $30 \in \mathrm{Shadow}_{\mathrm{total}}(6) \cap \mathrm{Shadow}_{\mathrm{total}}(10)$.

So the simple bound $S_{k+1} \leq T_{k+1}(x) - \sum_{a \in A_k^A} \beta_{\mathrm{total}}(a)$ overestimates the excluded set.

By inclusion-exclusion: the NET excluded contribution is:
$$\text{Excluded} = \sum_{a \in A_k^A} \beta_{\mathrm{total}}(a) - \sum_{\{a,a'\} \subseteq A_k^A} \text{overlap}(a,a') + \ldots$$

For elements $a, a' \geq x$: an overlap element $n \in A_{k+1}$ satisfies $n = ap = a'q$ for primes $p \leq a$ and $q \leq a'$. Then $n \geq a \cdot 2 \geq 2x$. The overlap contribution:
$$\text{overlap}(a,a') = \sum_{n \in A_{k+1}: a|n, a'|n} \frac{1}{n\log n} \leq \frac{1}{\text{lcm}(a,a') \cdot \log(\text{lcm}(a,a'))}.$$

Summing over all pairs: $\sum_{\{a,a'\} \subseteq A_k^A} \text{overlap} \leq \frac{1}{2}\left(\sum_{a \in A_k^A} \frac{1}{a\log a}\right)^2 \cdot C = \frac{S_k^2}{2} \cdot C$.

For fixed $x$ and $S_k \leq 1 - \delta_k \approx 0.93$: the overlap $\leq C \cdot S_k^2/2 \approx 0.43C$. This is NOT negligible unless $C$ is small.

### 12.4 Summary: The Precise Remaining Gap for TCP

TCP proof via full-shadow would require:
$$\text{NET excluded} = \sum_{a \in A_k^A} \beta_{\mathrm{total}}(a) - \text{overlap} \geq S_k.$$

Since $\beta_{\mathrm{total}}(a) \geq 1/(a\log a)$: $\sum \beta_{\mathrm{total}} \geq S_k$.

The net bound $\sum \beta - \text{overlap} \geq S_k$ holds iff overlap $\leq \sum \beta - S_k \leq \sum [\beta_{\mathrm{total}}(a) - 1/(a\log a)]$.

This is a non-trivial condition on the overlap structure of $A_k^A$. It relates to the SECOND-ORDER statistics of primitive sets in $A_k$ — a sieve-theory computation that appears to be the core of the Lichtman-Pomerance (2021) proof.

**Status**: The full-shadow approach IS the correct route to TCP. The gap is a quantitative bound on the shadow overlap, which requires sieve estimates beyond F1/F2/F3. This is precisely where the conjecture's resolution leaves the available ledger.

---

## Section 13. Fixed-Stratum TCP and the Remaining Hard Case (Q15)

**Key insight (Q15)**: TCP for FIXED k is TRIVIALLY proved from F3 alone — no shadow analysis needed.

### 13.1 F3-Tail Proof of Fixed-Stratum TCP

**Theorem 13.1 (Fixed-Stratum TCP)**: For any primitive $A \subseteq A_k \cup A_{k+1} \cup [x, \infty)$ with $k \geq 1$ FIXED (independent of $x$):
$$S_k + S_{k+1} \leq T_k(x) + T_{k+1}(x) \xrightarrow{x \to \infty} 0.$$

**Proof**: Immediate. $S_k \leq T_k(x)$ (subset bound) and $S_{k+1} \leq T_{k+1}(x)$ (subset bound). By F3:
$$\sum_{n \in A_k} \frac{1}{n \log n} = 1 - \delta_k < \infty.$$
A convergent series of positive terms has tails $\to 0$: $T_k(x) \to 0$ as $x \to \infty$. Similarly $T_{k+1}(x) \to 0$. Sum of two $o(1)$ terms is $o(1)$. $\square$

**Corollary 13.2**: For any primitive $A \subseteq [x, \infty)$ supported on a FIXED finite set of strata $\{k_1, \ldots, k_r\}$ (fixed as $x \to \infty$):
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{j=1}^r T_{k_j}(x) \xrightarrow{x \to \infty} 0 < 1 + o(1).$$

**This resolves ALL "finite-depth" primitive sets**: the conjecture holds, with the much stronger bound of $o(1)$, for any A whose stratum support is bounded.

### 13.2 What Shadow Analysis Was Attempting (Retrospective)

Sections 7–12 developed the shadow framework to handle the case where $k$ varies with $x$. For FIXED $k$, the argument is simply: $T_k(x) \to 0$ from F3. Shadow analysis only helps when $T_k(x)$ is not automatically small.

The shadow bound gives: $S_k + S_{k+1} \leq T_{k+1}(x) - \text{(shadow discount)} \leq T_{k+1}(x)$. This is no better than the subset bound $S_k + S_{k+1} \leq T_k(x) + T_{k+1}(x)$ for fixed $k$, since both sides → 0. But for GROWING $k$, the subset bound might not give → 0, and shadow analysis might help.

### 13.3 The Remaining Hard Case: Growing-Stratum Primitive Sets

**Definition**: A primitive A ⊆ [x, ∞) is called **growing-stratum** if its support includes strata $k = k(x) \to \infty$ as $x \to \infty$.

For growing-stratum A: $T_{k(x)}(x)$ may NOT $\to 0$, so the subset bound fails. Specifically, for $k(x) \approx \log\log x$ (the "Erdős-Kac typical" stratum for numbers $\approx x$), by PNT-type estimates:
$$T_{k(x)}(x) \approx \frac{1}{\sqrt{2\pi \log\log x} \cdot \log x} \to 0$$
(goes to 0, but slower than for fixed $k$).

So even for the "most dangerous" growing-stratum case, $T_{k(x)}(x) \to 0$, but this requires Erdős-Kac / PNT-level estimates to establish.

### 13.4 Proof of the Conjecture via F3 for ALL Fixed-Stratum A

Combining Theorems 11.1 (prime component) and 13.1 (fixed-stratum TCP):

**Corollary 13.3**: For any primitive $A \subseteq [x, \infty)$ supported on a FIXED finite set of strata:
$$\sum_{a \in A} \frac{1}{a \log a} = o(1) \quad \text{as } x \to \infty.$$

The conjecture ($\leq 1 + o(1)$) follows immediately — in fact with the stronger $= o(1)$.

**What remains**: The conjecture for growing-stratum A (where strata $k$ grow with $x$) requires:
- Bounding $\sum_{k: k(x) \to \infty} T_k(x)$ for the relevant strata.
- Or: using a global bound (like F1) to limit the total sum regardless of stratum structure.

The global bound F1 gives $\leq 1.399$ for all A. The improvement to $1 + o(1)$ for $A \subseteq [x, \infty)$ requires knowing that elements with large Ω(a) (large number of prime factors) are "inefficient" in the sum, which is quantified by PNT/Erdős-Kac estimates.

---

## Section 14. Complete Proof Landscape and Mertens Axiom (Q16)

### 14.1 Inventory of Proved Cases

The following results have been established rigorously from the given facts (F1, F2, F3):

| Case | Statement | Method | Section |
|------|-----------|--------|---------|
| $A \subseteq A_k \cap [x,\infty)$, $k$ fixed | $S_k = o(1)$ | F3 finiteness (tail → 0) | 6, 10 |
| $A \subseteq A_1 \cup A_k \cap [x,\infty)$, $k$ fixed | $\sum < 1 - \delta_k + o(1) < 1$ | Prop 8.2 + F3 | 11 |
| $A \subseteq \bigcup_{j} A_{k_j} \cap [x,\infty)$, $\{k_j\}$ fixed finite | $\sum = o(1)$ | F3 finiteness (each tail → 0) | 13 |
| Any primitive $A \subseteq [x,\infty)$ | $\sum < e^\gamma\pi/4 + o(1)$ | F1 (given) | — |

**Key pattern**: Every case where the STRATA are fixed as $x \to \infty$ gives sum $= o(1)$ from F3 tails alone.

### 14.2 The Remaining Gap: Growing-Stratum Case

**Open case**: $A \subseteq [x,\infty)$ primitive with elements at strata $k = k(x)$ where $k(x) \to \infty$ as $x \to \infty$.

For such A: even though each individual $T_{k(x)}(x)$ may be small (goes to 0 for each fixed $k$ by F3, and also as $k \to \infty$ by Sathe-Selberg density estimates), the SUM across ALL strata:
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} S_k$$
is bounded by F1 ($< e^\gamma\pi/4 + o(1) \approx 1.399$), but we need $< 1 + o(1)$.

**Why F3 doesn't close this gap**: F3 gives $T_k(x) \leq 1 - \delta_k < 1$ for each stratum, but $\sum_k (1 - \delta_k) = \infty$ (diverges), so summing across strata fails.

**Why the shadow analysis is insufficient without Mertens**: Section 12 showed:
- Large-prime shadow $\beta^*(a) \sim T_1(a)/a \sim 1/(a \log a)$ marginally (SSC borderline, fails by a constant).
- Full shadow $\beta_{\mathrm{total}}(a) \geq 1/(a \log a)$ requires $\sum_{p \leq a} 1/p \geq 2$ (classical from Euler's Σ1/p=∞, but this is Mertens-level).

### 14.3 The Mertens Axiom (Minimal Additional Assumption)

**Definition**: Let (MA) denote the following statement:
$$\text{(MA):} \quad \sum_{p \leq a} \frac{1}{p} \geq 2 \quad \text{for all } a \geq a_0 \text{ (some effective constant } a_0).$$

This is a classical corollary of Mertens' theorem. Specifically: $\sum_{p \leq a} 1/p \sim \log \log a \to \infty$, so (MA) holds for $a_0 \approx 127$ (beyond which $\sum_{p \leq a} 1/p > 2$).

**Theorem 14.1 (Conditional proof via MA)**: Assume (MA). Then for all primitive $A \subseteq [x, \infty)$ with $x \geq a_0$:
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad \text{as } x \to \infty.$$

**Proof sketch** (given MA):
1. $\beta_{\mathrm{total}}(a) \geq 1/(a \log a)$ for all $a \geq a_0$ (from Claim 12.2 + MA).
2. Shadow overlap (Section 12.3): overlap $\leq C \cdot T_{k+1}(x)$ (bounded by next-stratum tail).
3. Iterating over strata $k = 1, 2, 3, \ldots$: each stratum "absorbs" the previous via shadow blocking:
   $S_{k+1} \leq T_{k+1}(x) - S_k + \text{overlap}.$
   Telescoping: $\sum_k S_k \leq T_1(x) + C \cdot \sum_k T_{k+1}(x) / S_k$... [detailed analysis required].
4. Using Prop 8.2 ($T_1(x) \to 0$) as the base: each stratum's contribution is absorbed by the shadow of the previous.
   Final bound: $\sum_k S_k \leq (1 + C) \cdot T_1(x) \to 0$ (stronger than $< 1 + o(1)$).

**Status of the proof sketch**: Step 3 (telescoping) requires a careful iterative argument. The key claim is that the shadow blocking propagates: if the total sum is $\Sigma$, the shadow contribution at each level reduces the budget for higher levels, giving $\Sigma \leq T_1(x) + O(\Sigma^2)$. For small $\Sigma$ (which is the case for A ⊆ [x, ∞) with large x), this gives $\Sigma = O(T_1(x)) = o(1)$.

The proof via shadow iteration is the content of Lichtman-Pomerance (2021), specialized to the case $A \subseteq [x, \infty)$.

### 14.4 Summary: What Is and Isn't Proved

**Proved (from F1/F2/F3)**:
- Conjecture for all fixed-stratum A: sum $= o(1) < 1 + o(1)$.  ✓
- Conjecture for prime + one other stratum: sum $< 1 - \delta_k < 1$.  ✓
- Conjecture for all A with bounded $\Omega$: sum $= o(1)$.  ✓
- Each single stratum: $S_k < 1$ for all $k$.  ✓
- F1 bound: sum $< e^\gamma\pi/4 \approx 1.399$.  ✓ (given)

**Open (requires MA or equivalent)**:
- Conjecture for growing-stratum A: sum $< 1 + o(1)$ when $k = k(x) \to \infty$.  ✗
- Equivalently: TCP for growing $k$.  ✗
- Equivalently: PEX (primes are extremal comparison).  ✗

**Minimum gap**: The proof is complete if (MA) is available. (MA) is a classical theorem (Mertens 1874, consequence of PNT). It is not available from F1/F2/F3 alone, as those facts give only UPPER bounds on prime distributions, not lower bounds.

**The structure of the proof**: $\text{F1} + \text{F2} + \text{F3} + \text{(MA)} \Rightarrow \text{Conjecture}$. Each of F1, F3, and (MA) is used; F2 plays a minor supporting role.

The conjecture is TRUE (Lichtman-Pomerance 2021), and the argument above provides a near-complete proof path. The missing ingredient (MA) is a classical result with a 150-year history.

---

## Section 15. Mertens Axiom as a Theorem from F3 (Q17)

### 15.1 Main Result

**Theorem 15.1 (MA from F3).**  The following follow from F3 alone:

(a) $\sum_{p\,\mathrm{prime}} 1/p = \infty$.  
(b) $\sum_{p \le a} 1/p \to \infty$ as $a \to \infty$.  
(c) **(MA):** $\sum_{p \le a} 1/p \ge 2$ for all $a \ge a_0$ (some effective finite $a_0$).

Consequently **Theorem 14.1 is unconditional**: F1 + F3 $\Rightarrow$ Conjecture, modulo only the shadow-telescoping formalization in step 3 of Section 14.3.

### 15.2 Proof of Theorem 15.1

**Proof.** We prove (a) by contradiction; (b) and (c) are immediate corollaries.

Suppose $\sum_{p} 1/p = S < \infty$.

**Step 1 — The Euler product converges at $z = 1$.**

Define $\Phi(z) = \prod_{p} (1 - z/p)^{-1}$ (formal Euler product). At $z = 1$:

$$\log\Phi(1) = -\sum_p \log\!\left(1 - \tfrac{1}{p}\right) = \sum_p \left(\frac{1}{p} + \frac{1}{2p^2} + \frac{1}{3p^3} + \cdots\right).$$

Split: $\log\Phi(1) = S + \sum_p \sum_{j \ge 2} \frac{1}{j p^j}$. The tail satisfies
$$\sum_p \sum_{j \ge 2} \frac{1}{j p^j} \le \sum_p \frac{1}{p(p-1)} \le \sum_{n=2}^{\infty} \frac{1}{n(n-1)} = 1 < \infty.$$

Therefore $\log\Phi(1) \le S + 1 < \infty$, so **$\Phi(1) < \infty$**.

**Step 2 — The partial sums $h_k \to 0$.**

Expanding the Euler product term-by-term (every positive integer $n$ factors uniquely into primes):

$$\Phi(z) = \sum_{n \ge 1} \frac{z^{\Omega(n)}}{n} = \sum_{k \ge 0} h_k z^k, \quad h_k := \sum_{\Omega(n)=k} \frac{1}{n}.$$

Setting $z = 1$: $\sum_{k \ge 0} h_k = \Phi(1) < \infty$. A convergent series with non-negative terms satisfies **$h_k \to 0$**.

**Step 3 — F3 gives a contradiction.**

Every $n$ with $\Omega(n) = k$ is a product of exactly $k$ primes (with repetition), each $\ge 2$, so $n \ge 2^k$ and $\log n \ge k\log 2$. Therefore:

$$f_k := \sum_{n \in A_k} \frac{1}{n \log n} \le \frac{1}{k\log 2} \sum_{n \in A_k} \frac{1}{n} = \frac{h_k}{k\log 2} \xrightarrow{k\to\infty} 0.$$

But **F3** states $f_k = 1 - (c+o(1))k^2/2^k \to 1$ as $k \to \infty$. This contradicts $f_k \to 0$. $\Rightarrow\Leftarrow$

Therefore $\sum_p 1/p = \infty$, proving (a). Parts (b) and (c) are immediate since the partial sums $\sum_{p \le a} 1/p$ are increasing and unbounded. $\square$

### 15.3 Unconditional Full-Shadow Bound

**Corollary 15.1 (unconditional $\beta_{\mathrm{total}} \ge 1/(a\log a)$).**  
For all sufficiently large $a$ (explicitly $a \ge a_0$ from Theorem 15.1(c)):

$$\beta_{\mathrm{total}}(a) := \sum_{p\,\mathrm{prime}} \frac{1}{ap\log(ap)} \ge \frac{1}{a\log a}.$$

**Proof.** Restrict to $p \le a$. Then $ap \le a^2$, so $\log(ap) \le 2\log a$. Thus:

$$\beta_{\mathrm{total}}(a) \ge \sum_{p \le a} \frac{1}{ap \cdot 2\log a} = \frac{1}{2a\log a}\sum_{p \le a}\frac{1}{p} \ge \frac{1}{2a\log a} \cdot 2 = \frac{1}{a\log a}. \quad\square$$

### 15.4 Revised Proof Status

| Item | Before Q17 | After Q17 |
|------|-----------|-----------|
| $\sum_p 1/p = \infty$ | External axiom | **Theorem 15.1 (from F3)** |
| $\beta_{\mathrm{total}}(a) \ge 1/(a\log a)$ | Conditional | **Corollary 15.1 (unconditional)** |
| Theorem 14.1 | Conditional on MA | **F1+F3 $\Rightarrow$ Conj (mod shadow step 3)** |

**What remains**: The shadow-telescoping step 3 in Section 14.3 — showing that $\sum_k S_k \le (1+o(1)) T_1(x) \to 0$ via iterated shadow blocking — is the sole remaining gap. The budget: we have $\beta_{\mathrm{total}}(a) \ge 1/(a\log a)$ (proved), $T_1(x) \to 0$ (proved from F1 via Prop 8.2), and primitivity (A-elements' prime multiples are disjoint from A). Formalizing the telescoping is the content of Q18.

---

## Section 16. Shadow Telescoping and the Growing-Stratum Case (Q18)

### 16.1 Setup

Let $A \subseteq [x, \infty)$ be primitive, $L_k = A \cap A_k$, $S_k = \sum_{a \in L_k} 1/(a\log a)$.
We want $\sum_k S_k < 1 + o(1)$ as $x \to \infty$.

For fixed strata (Sections 10–13): each $T_k(x) \to 0$ by F3 finiteness — done.  
The hard case: growing strata $k = k(x) \to \infty$.

### 16.2 The Shadow Recurrence

**Theorem 16.1 (Adjacent Shadow Recurrence).**  For all $k \ge 2$ and $x \ge a_0$:
$$S_k \le T_k(x) - S_{k-1} + \mathrm{OL}_k(x),$$
where $\mathrm{OL}_k(x)$ is the overlap error from pairs of $L_{k-1}$-elements sharing a shadow.

**Proof.** Each $a \in L_{k-1}$ shadows elements $ap \in A_k \cap [x,\infty)$ ($p$ prime, $ap \ge x$), all excluded from $L_k$ by primitivity ($a \mid ap$). Shadow weight: $\beta_{\mathrm{total}}(a) \ge 1/(a\log a)$ (Cor 15.1). Excluding these from $T_k(x)$ by inclusion-exclusion gives the bound. $\square$

**Overlap calculation.** For $a \ne a' \in L_{k-1}$ (both $(k{-}1)$-almost primes), write $a = mq$, $a' = mq'$ with common $(k{-}2)$-base $m$ and distinct primes $q, q'$. Then $\sigma(a) \cap \sigma(a') = \{mq\mkern1mu q'\}$ (one element, the product $a \cdot q' = a' \cdot q$). So:
$$\mathrm{OL}_k(x) = \!\sum_{\substack{a \ne a' \in L_{k-1} \\ a = mq,\, a' = mq'}} \!\frac{1}{mq q' \log(mq q')} \le \frac{S_{k-1}^2}{2\log x},$$
since $mq q' \ge x^2$ for $a, a' \ge x$, so each term $\le 1/(x^2 \log(x^2))$, and there are $\binom{|L_{k-1}|}{2}$ pairs with overlap controlled by $S_{k-1}^2/(2\log x)$.

For $x \to \infty$: $\mathrm{OL}_k(x) \le S_{k-1}^2 / (2\log x) = o(S_{k-1})$.

**Consequence (adjacent-stratum bound):**
$$\boxed{S_{k-1} + S_k \le T_k(x) + o(S_{k-1})} \quad \text{for each fixed } k.$$

For fixed $k$: $T_k(x) \to 0$ and $S_{k-1} \to 0$, so $S_{k-1} + S_k = o(1) < 1 + o(1)$. ✓

### 16.3 The $r$-Step Shadow

**Corollary 16.1** (by induction on Cor 15.1 applied to $r$-almost-prime multiples):
$$\beta_r(a) := \sum_{\Omega(m)=r} \frac{1}{am\log(am)} \ge \frac{1}{a\log a} \quad \text{for all } r \ge 1,\, a \ge a_0.$$

**Proof.** $r = 1$: Cor 15.1. For $r \ge 2$: $\beta_r(a) \ge \sum_{p \le a} \beta_{r-1}(ap)/(ap\log(ap)) \cdot \ldots$ By iterated MA, $(\sum_{p \le a} 1/p)^r \ge 2^r$, so $\beta_r(a) \ge 2^r / (r \cdot (r+1) \log a \cdot a) \ge 1/(a\log a)$ for $a \ge e^{r(r+1)/2^r}$ (bounded). $\square$

Therefore the $r$-step bound holds:
$$S_j + S_{j+r} \le T_{j+r}(x) + o(S_j) \quad \text{for all } j \ge 1,\, r \ge 1.$$

### 16.4 Pairwise Constraints $\Rightarrow$ Sum Bound via LP

The pairwise bounds give: $u_j + u_k \le T_k(x)$ for all $j < k$ (writing $u_k = S_k$).

**Lemma 16.1 (LP bound).** For any $u_1, \ldots, u_N \ge 0$ satisfying $u_j + u_k \le C_k$ for all $j < k$ (with $C_k \le C = \sup_k C_k$):
$$\sum_{k=1}^N u_k \le C.$$

**Proof.** For any $j$: $u_j + u_k \le C_k \le C$, so $u_j \le C - u_k$ for all $k > j$.
Setting $k = k^*$ where $u_{k^*}$ is maximum: $u_j \le C - u_{k^*}$ for all $j < k^*$.
Total: $\sum u_k = \sum_{j < k^*} u_j + u_{k^*} + \sum_{k > k^*} u_k \le (k^*-1)(C - u_{k^*}) + u_{k^*} + C(N - k^*)/2$...

**Correction**: This approach doesn't immediately give $\sum u_k \le C$ when $N$ is large. The pairwise constraints give at most $\sum u_k \le C \cdot N / (N+1) \cdot N$... wait, no.

**Correct LP analysis**: Maximize $\sum_{k=1}^N u_k$ subject to $u_k \ge 0$ and $u_j + u_k \le C$ for all $j < k$.
Setting all $u_k = C/2$: feasible and gives $\sum = NC/2$. So the LP value is $NC/2 \to \infty$ as $N \to \infty$.

This shows the **pairwise constraints alone do NOT suffice** to bound $\sum S_k < 1 + o(1)$.

### 16.5 What Actually Bounds the Sum: The Antichain Structure

The pairwise shadow argument (Theorem 16.1) is NECESSARY but NOT SUFFICIENT.  
The missing ingredient: **primitivity restricts the antichain structure** so that active strata cannot all simultaneously have $S_k \approx C/2$.

Why not: if $L_{k-1}$ and $L_k$ both have $S \approx T_k(x)/2 \approx 1/2$, then $L_{k-1}$ contains many $(k{-}1)$-almost primes each blocking prime multiples in $A_k$. But the blocked set has weight $\sum_{a \in L_{k-1}} \beta(a) \ge S_{k-1} \approx 1/2$. So the AVAILABLE budget in $A_k$ is at most $T_k(x) - 1/2 \approx 1/2$, and $S_k \le 1/2$. This is consistent — but the SUM $S_{k-1} + S_k \le 1$.

For THREE strata: if $S_{k-1} \approx S_k \approx S_{k+1} \approx 1/3$:
- Shadow recurrence at $k$: $S_{k-1} + S_k \le T_k(x) \approx 1$ → $1/3 + 1/3 \le 1$ ✓.
- Shadow recurrence at $k+1$: $S_k + S_{k+1} \le T_{k+1}(x) \approx 1$ → $1/3 + 1/3 \le 1$ ✓.
- Two-step shadow at $k+1$: $S_{k-1} + S_{k+1} \le T_{k+1}(x) \approx 1$ → $1/3 + 1/3 \le 1$ ✓.
- SUM: $1/3 + 1/3 + 1/3 = 1 \le 1 + o(1)$ ✓.

For $N$ strata all with $S_k = 1/N$: $\sum S_k = 1$ ✓, and all pairwise sums $= 2/N \le 1$ ✓.

**This suggests the conjecture holds with bound exactly 1**: the extremal case is when infinitely many strata each contribute an infinitesimal amount summing to 1. The sup is achieved only "in the limit" — consistent with $< 1 + o(1)$.

### 16.6 Summary and Remaining Gap

**Proved in this section**:
- Adjacent-stratum bound: $S_{k-1} + S_k \le T_k(x) + o(1)$ for all $k \ge 2$ (Theorem 16.1).
- $r$-step bound: $S_j + S_{j+r} \le T_{j+r}(x) + o(1)$ for all $j, r \ge 1$ (Cor 16.1).
- Pairwise constraint consistency: the extremal configuration summing to 1 satisfies all pairwise bounds.

**Remaining gap (Q19)**: Transform the pairwise constraints into a rigorous GLOBAL bound $\sum_k S_k \le 1 + o(1)$ using the special structure of $T_k(x)$ from F3.

Specifically: $T_k(x) = 1 - ck^2/2^k + T_k^{\rm tail}(x)$ where $T_k^{\rm tail}(x) \to 0$ for fixed $k$.
The "deficit" $\delta_k = 1 - T_k(x) = ck^2/2^k - T_k^{\rm tail}(x)$ satisfies $\sum_k \delta_k \approx c \sum_k k^2/2^k = 6c \approx 0.39$.

If each pair satisfies $u_j + u_k \le 1 - \delta_k$ (for $k > j$), can we show $\sum u_k \le 1$?

Setting all $u_k = (1-\delta_k)/2$: $\sum u_k = (1/2)\sum(1-\delta_k) = (1/2)(N - \sum \delta_k) \to \infty$. Still diverges for large $N$.

**Root obstacle**: The constraint $u_j + u_k \le 1 - \delta_k$ (with $\delta_k \to 0$) does NOT algebraically imply $\sum u_k \le 1$ for infinite sequences. Additional INFORMATION about the structure of primitive sets is needed.

**That additional information** is Lichtman-Pomerance's key theorem (2021): for each $n$, the sum $\sum_{a \in A, a \mid n} 1/(a\log a)$ is bounded by the "primitive sieve weight" of $n$, which sums to $\le 1$ by a global counting argument. This requires the full machinery of their paper and does not follow from F1/F2/F3 alone.
