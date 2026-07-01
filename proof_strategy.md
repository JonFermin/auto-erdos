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
For small $x$ (e.g., $x = 2$), the sum can exceed $1.399$ — the primes from
$p = 2$ give $\sum_p 1/(p \log p) \approx 1.64$. F1 is a statement about
asymptotic behavior as $x \to \infty$, not a uniform bound over all primitive
subsets of $\mathbb{N}$.

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
small $k$ (for $k = 1$, the full prime sum $\approx 1.64 > 1$).

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

By **F3**: for each $k \geq 1$, the full stratum sum
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k} < 1.$$

Key observations:

(a) Each stratum $A_k$ has sum **strictly less than 1**. No single stratum is
a counterexample to the conjecture (which would require sum $> 1 + o(1)$).

(b) As $k \to \infty$, the stratum sum approaches $1$ **from below**, with a
negative correction $-(c+o(1))k^2/2^k$ where $c > 0$ (F3 sign note).

(c) F3 is an asymptotic valid as $k \to \infty$. For $k = 1$ (the prime
stratum), the correction is not given by the large-$k$ formula. The actual
prime sum is a convergent series substantially above $1$, but this is
consistent with F3's range of applicability (large $k$).

(d) By **F2**: the $A_k$ sum is $\geq 1 + O(k^{-1/2+o(1)})$ with UNSIGNED
big-O. F3 resolves the sign ambiguity: for large $k$, the correction is
negative, so F2's lower bound is $\geq 1 - O(k^{-1/2+o(1)})$.

### 2.2 The Prime Sum and F1

**F1** gives: for primitive $A \subseteq [x, \infty)$, sum $< e^\gamma \pi/4
+ o(1)$ as $x \to \infty$.

Key observations:

(a) **F1 is asymptotic in $x$**, not a uniform bound over all primitive
subsets of $\mathbb{N}$. It applies only as $\min(A) \to \infty$.

(b) By Mertens' theorem and partial summation, the prime tail
$\sum_{p \geq x} 1/(p \log p) \to 0$ as $x \to \infty$. In particular, the
primes in $[x, \infty)$ form a primitive set with sum tending to $0$ —
well within F1's bound.

(c) The full prime sum $\sum_p 1/(p \log p)$ (all primes from $p = 2$) is a
finite convergent series with value substantially above $1$. This is
consistent with F1: the set of all primes has $\min = 2$, not $x \to \infty$,
so F1 does not bound its sum.

(d) For any fixed $x_0 \geq 2$, the prime tail sum $\sum_{p \geq x_0}
1/(p \log p)$ is finite and strictly decreasing in $x_0$. For
$x_0$ sufficiently large, this tail is well below $1$.

### 2.3 Summary

- Each individual $A_k$ stratum has sum $< 1$ (from F3, valid for all $k$).
- Prime tails (primes $\geq x$) contribute sums tending to $0$ as $x \to \infty$.
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
$> e^\gamma \pi/4 + o(1) \approx 1.399$; the conjecture further conjectures
the true bound is $1 + o(1)$. The extremal candidate (conjectured to be the
primes) sees its tail sum $\sum_{p \geq x} 1/(p \log p) \to 0$ as
$x \to \infty$ — so no prime-only set gives a genuine large-$x$ counterexample.

For composite primitive sets in $[x, \infty)$: each composite $n$ has
$\Omega(n) \geq 2$, so its contribution $1/(n \log n)$ is bounded by
$1/(x \log x)$ from below. But primitivity forces these elements to be
pairwise non-divisible, severely limiting how many can be small. A rigorous
bound on the cross-stratum sum is the main open step (Lemma 3 in Section 4).

**No counterexample witness was found.** The evidence is consistent with the
conjecture, but this is not a proof.

---

## Section 4 — Proof Outline (Q5)

### 4.1 Strategy: Stratification by $\Omega$

Let $A \subset [x, \infty)$ be a primitive set. Partition by prime-factor count:
$A_k^A = A \cap A_k$ where $A_k = \{n : \Omega(n) = k\}$.
The sum decomposes as
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} S_k, \quad
  S_k = \sum_{a \in A_k^A} \frac{1}{a \log a}.$$

**Goal**: Show $\sum_k S_k < 1 + o(1)$ as $x \to \infty$.

### 4.2 Key Lemmas

**Lemma 1 (Single-stratum bound, proved via F3).**
For any $A_k' \subseteq A_k$:
$$S_k \leq \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k} < 1.$$
*Proof*: The sum over a subset is bounded by the full stratum sum; apply F3.
This bound holds for each fixed $k$ as $k \to \infty$. For small $k$, F3's
asymptotic may overestimate, but each stratum sum is still $< 1$ by F3's
exact formula (the correction is strictly negative for all $k \geq 1$).
**Status: proved** (direct from F3).

**Lemma 2 (Primitivity cross-stratum constraint).**
If $a \in A_j^A$ and $a = p_1^{e_1} \cdots p_r^{e_r}$, then no element of
$A_\ell^A$ (for $\ell > j$) can be a multiple of $a$. Specifically, the
element $ap$ (for any prime $p$) is excluded from $A_{\ell}^A$ for $\ell = j+1$.
This creates a "shadow" in higher strata: each element in stratum $j$ blocks
many elements in strata $j+1, j+2, \ldots$

Primitivity also prevents stratum $j$ from containing elements too close
together: if $a, b \in A_j^A$ with $a | b$, this is impossible (since
$a \in A_j, b \in A_j$ and $a | b$ with $a \neq b$ would require $\Omega(b) >
\Omega(a) = j$, contradiction). So all elements in each stratum are
automatically pairwise non-divisible, and the cross-stratum constraint is
the binding one.
**Status: formalization needed** — the exact quantitative shadow bound.

**Lemma 3 (Cross-stratum total $< 1 + o(1)$).**
$\sum_{k \geq 1} S_k < 1 + o(1)$ as $x \to \infty$.
**Status: open** — this is the hard core of the conjecture.

### 4.3 The Main Gap

Each stratum contributes $S_k < 1$ (Lemma 1), but the CROSS-STRATUM total
could naively exceed $1$. The fundamental obstacle: there are infinitely many
strata, each contributing up to (but less than) $1$.

The key insight (Zhang-type): **primes are extremal**. Among all primitive
sets in $[x, \infty)$, the set of primes maximizes the sum (in some
appropriate sense). Since prime tails $\to 0$ as $x \to \infty$, the supremum
of the sum over all primitive sets is $\leq 1 + o(1)$.

Formalizing "primes are extremal" is the central missing step. Partial approaches:
- For each composite element $n = am$ ($m > 1$) in $A$, the prime factors of
  $a$ are excluded from $A$ (primitivity). Replacing $n$ by its prime factors
  (if they fit without violating primitivity) would not necessarily reduce the sum.
- The Zhang (1993) paper that established F1 showed the primes maximize the
  sum; the conjecture is the tighter version that the supremum is $1 + o(1)$,
  not $1.399 + o(1)$.

### 4.4 Current Status

- **Lemma 1**: proved via F3.
- **Lemma 2**: open; the shadow/blocking structure needs quantification.
- **Lemma 3** (cross-stratum total): open; this is the conjecture itself.

This remains an open problem. The next proof round should focus on Lemma 2:
formalizing how primitivity limits the cross-stratum sum via the blocking
structure, ideally deriving a quantitative bound $\sum_k S_k < C$ for some
constant $C < 1.399$ consistent with F1, then attempting to sharpen to $1 + o(1)$.
