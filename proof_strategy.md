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
- **Lemma 2**: open; the shadow/blocking structure needs quantification.
- **Lemma 3** (cross-stratum total): open; this is the conjecture itself.

This remains an open problem. The next proof round should focus on Lemma 2:
formalizing how primitivity limits the cross-stratum sum via the blocking
structure, ideally deriving a quantitative bound $\sum_k S_k < C$ for some
constant $C < 1.399$ consistent with F1, then attempting to sharpen to $1 + o(1)$.
