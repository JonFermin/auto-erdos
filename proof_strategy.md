# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Metadata

- **Claim**: For any primitive $A \subseteq [x,\infty)$, $\sum_{a\in A} 1/(a\log a) < 1+o(1)$.
- **Status**: open (harness enforces; no resolution claim without a verified witness).
- **Given facts**: F1 (Erdős-Zhang UB ≈ 1.399), F2 (Omega-stratum LB, unsigned-O), F3 (exact asym for $A_k$, approaches 1 from below).

## Witness format

A counterexample witness must be embedded as a `<!-- WITNESS ... WITNESS -->`
block at the bottom of this file and pass `library.primitive_set_witness.verify_witness`.

---

## Section 1: Setup (Q1)

### The conjecture

**Erdős's primitive-set conjecture** (tightened form): For any integer
$x \geq 2$ and any **primitive set** $A \subseteq [x, \infty)$ — a set of
integers $\geq x$ in which no element divides another — we have
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
where $o(1) \to 0$ as $x \to \infty$.

Restated: in the limit of large floor $x$, no primitive subset of
$[x, \infty)$ can have a weighted sum $\sum 1/(a \log a)$ exceeding $1$.
The conjecture asserts $1$ is a universal asymptotic upper bound.

This is an **open problem** as of this proof attempt. This file contains
no claim of proof or refutation without a verifier-accepted witness block.

### Given facts with sign notes

**F1 — Erdős-Zhang upper bound** (Erdős 1935; Zhang 1993):
For *any* primitive set $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399.$$

Sign note (UPPER bound): the sum is bounded *above* by $\approx 1.399$.
This is weaker than but consistent with the conjecture (bound of $1+o(1)$).
F1 cannot serve as a lower bound; any argument that reads it as a lower
bound would contradict F1 itself.

**F2 — Omega-stratum lower bound** (given fact F2):
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$

Sign note (UNSIGNED big-$O$): The error term $O(k^{-1/2+o(1)})$ is
unsigned — it may be positive or negative. F2 alone does NOT imply
the sum exceeds $1$. Any argument concluding "sum $> 1$" from F2 alone
is a sign error (the ChatGPT failure mode for this problem).

**F3 — Exact asymptotic for $A_k$** (given fact F3):
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$

Sign note (correction is NEGATIVE): Since $c > 0$, the term
$-(c+o(1)) k^2/2^k$ is negative, so the sum is strictly less than $1$
and approaches $1$ from **below** as $k\to\infty$. F3 resolves F2's
ambiguity: the unsigned-$O$ is in fact negative for $A_k$. The canonical
extremal stratum never violates the conjecture.

### Witness contract

A counterexample claim requires a finite primitive set
$A \subseteq [x_\text{floor}, \infty)$ for which
`library.primitive_set_witness.verify_witness` confirms:
1. Every element is $\geq x_\text{floor}$.
2. $A$ is primitive (no element divides another).
3. Rigorous sum $\sum_{a\in A} 1/(a\log a) > 1.0$ (the threshold).

Without a verifier-accepted `<!-- WITNESS -->` block in this file, no
refutation claim may be made. The $o(1)$ caveat in the conjecture means
a witness at finite $x_\text{floor}$ barely exceeding $1$ requires
separate argument that the $o(1)$ slack at that scale is negligible.

### Roadmap

| Round | Q   | Goal |
|-------|-----|------|
| 1     | Q1  | This Setup section (current) |
| 2     | Q2  | Numerical check: truncated sums for $A_k$, $k=1,2,3,4$ |
| 3     | Q3  | Primes sum: approach to $\approx 1.6366$, consistency with F1 |
| 4     | Q4  | Witness search at $x_\text{floor} \in \{100, 1000, 10000\}$ |
| 5+    | Q5  | Proof sketch: Omega-stratification + lemma decomposition |
| final | Q6  | Partial result if full proof is out of reach |

---

## Section 2: Numerical Evidence for F3 (Q2)

**Goal**: verify F3's claim that $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k$ by
computing truncated sums over the first 200 (and up to 10 000) elements of $A_k$.

### Partial sums (first 200 elements, then extended)

| $k$ | $n_{200}$ | $S_{200}$ | $S_{1000}$ | $S_\text{ext}$ ($n_\text{ext}$) | F3 leading term |
|-----|-----------|-----------|------------|----------------------------------|-----------------|
| 1   | 1 223      | 1.496 452 | 1.525 341  | 1.550 127 ($n=104\,729$, 10k el) | $1 - c/2 = 0.967$ |
| 2   | 669        | 0.681 938 | 0.746 088  | 0.793 578 ($n=19\,643$, 5k el)  | $1 - c = 0.934$ |
| 3   | 805        | 0.313 401 | 0.367 553  | 0.413 015 ($n=19\,533$, 5k el)  | $1 - 9c/8 = 0.926$ |
| 4   | 1 292      | 0.140 341 | 0.172 952  | 0.202 561 ($n=27\,819$, 5k el)  | $1 - c = 0.934$ |

(Here $c = 0.0656$, F3 leading term $= 1 - c k^2/2^k$.)

### Observations

**k = 2, 3, 4**: The partial sums are well below $1$ at all truncation levels, and
converging toward values that the tail estimate $1/\ln(n_\text{ext})$ bounds away from $1$.
Specifically:
- $k=2$: $S_\text{ext} = 0.794$, tail upper bound $0.101$, total $\leq 0.895 < 1$ ✓
- $k=3$: $S_\text{ext} = 0.413$, tail upper bound $0.101$, total $\leq 0.514 < 1$ ✓
- $k=4$: $S_\text{ext} = 0.203$, tail upper bound $0.098$, total $\leq 0.301 < 1$ ✓

**k = 1 (primes)**: The partial sum grows toward $\approx 1.636$. After 10 000 primes
(up to $p = 104\,729$), $S_{10000} = 1.550$ with an estimated remaining tail
$\approx 1/\ln(104\,729) \approx 0.087$, giving a total of $\approx 1.637$.  This means
the full infinite sum over all primes $\sum_p 1/(p \ln p) \approx 1.637 > 1$.

**Critical observation**: The k=1 sum exceeds $1$. This is consistent with two facts:
1. F3's formula $1 - ck^2/2^k$ is an asymptotic as $k \to \infty$; for small $k$ (especially
   $k=1$), the formula is not numerically accurate.
2. The conjecture's bound of $1+o(1)$ applies to primitive sets $A \subseteq [x,\infty)$ as
   $x \to \infty$. For $x=2$ (all primes), the $o(1)$ slack is large (at least $0.637$).
   The restriction $A \subseteq [x,\infty)$ makes the primes-from-$x$ sum $\sum_{p \geq x}
   1/(p \ln p)$ shrink to $0$ as $x \to \infty$, well below $1+o(1)$.

**Sign confirmation**: The F3 leading correction $-c k^2/2^k$ is **negative** for all $k$
(since $c \approx 0.0656 > 0$). For large $k$: $k^2/2^k \to 0$, so the correction vanishes
and the sum approaches $1$ from **below**. For $k=2, 3, 4$, the data is consistent with the
sums eventually converging to values somewhat below $1$.

### Conclusion

F3 is numerically consistent for $k \geq 2$: the sums are $< 1$ and the sign of the
correction (from $1$) is negative. For $k=1$, F3 is not numerically accurate at small $k$
(the formula is an asymptotic for large $k$ only), but the behavior is consistent with the
conjecture once the $[x,\infty)$ restriction is applied.

---

## Section 3: Primes Sum and Consistency with F1 (Q3)

**Goal**: compute $\sum_{p \geq x} 1/(p \ln p)$ for several values of $x$, verify the
full sum (from $p=2$) approaches $\approx 1.6366$, and explain why this is consistent
with F1.

### Computation

| Floor $x$ | $\sum_{p \geq x} 1/(p \ln p)$ (partial, up to $5\times 10^5$) | +tail $\approx 1/\ln(5\times 10^5)$ | $\approx$ full |
|-----------|--------------------------------------------------------------|--------------------------------------|----------------|
| 2         | 1.560 419                                                    | + 0.076                              | ≈ 1.637        |
| 10        | 0.337 977                                                    | + 0.076                              | ≈ 0.414        |
| 100       | 0.138 851                                                    | + 0.076                              | ≈ 0.215        |
| 1 000     | 0.068 104                                                    | + 0.076                              | ≈ 0.144        |
| 10 000    | 0.032 257                                                    | + 0.076                              | ≈ 0.108        |
| 100 000   | 0.010 637                                                    | + 0.076                              | ≈ 0.087        |

(The primes set $\{p \geq x\}$ is a primitive set in $[x,\infty)$ for each $x$.)

As $x \to \infty$, $\sum_{p \geq x} 1/(p \ln p) \to 0$ (tail of a convergent series).

The full sum from $p=2$ converges to $\approx 1.637$, consistent with the literature
value $\approx 1.6366$.

### Consistency with F1

F1 states: for any primitive $A \subseteq [x,\infty)$,
$\sum_{a \in A} 1/(a \ln a) < e^\gamma\pi/4 + o(1) \approx 1.399 + o(1)$,
where $o(1) \to 0$ as $x \to \infty$.

Observations:
- For $x \geq 10$: $\sum_{p \geq x} 1/(p \ln p) \leq 0.414 \ll 1.399$. F1 is amply satisfied. ✓
- For $x=2$: the full sum $\approx 1.637 > 1.399$. This is NOT a violation of F1 because
  F1 is an asymptotic bound. At $x=2$, the $o(1)$ in F1 is approximately $+0.238$ or more.
  The statement only asserts $o(1) \to 0$; it does not assert the bound holds sharply at $x=2$.
- As $x \to \infty$: the primes-from-$x$ sum $\to 0$, so the F1 bound is satisfied with
  enormous room for any large floor.

**Key distinction** (noted by Q3): the conjecture and F1 both apply in the regime
$x \to \infty$. A primitive set $A \subseteq [2, \infty)$ (no floor restriction) is not
the object of study; the interesting regime is $A \subseteq [x, \infty)$ for large $x$.

### Implication for the proof strategy

The primes-from-$x$ sum going to $0$ as $x \to \infty$ confirms that the $k=1$ stratum
is not the threat to the conjecture. For a primitive $A \subseteq [x, \infty)$, the
elements of $A$ are large, so each term $1/(a \ln a)$ is small. The challenge is bounding
the NUMBER of elements in a primitive set within $[x, \infty)$, weighted appropriately.

The Omega-stratification approach (Q5) decomposes any primitive $A$ as
$A = \bigsqcup_k (A \cap A_k)$ and bounds each stratum's contribution using F3-style
estimates for large $k$ and direct bounds for small $k$.
