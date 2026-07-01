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

## Section 2 — Numerical Evidence (Q2 + Q3)

### 2.1 A_k Stratum Sums

We compute truncated sums $S_k^{(500)}$ over the first $500$ elements
of $A_k = \{n : \Omega(n) = k\}$. We also record the large-$k$ asymptotic
from F3: $F_3(k) = 1 - 0.0656 k^2 / 2^k$.

| $k$ | $S_k^{(500)}$ (truncated sum) | $F_3(k)$ (large-$k$ formula) |
|-----|-------------------------------|-------------------------------|
| 1   | 1.5146                        | 0.9672 (not applicable)       |
| 2   | 0.7209                        | 0.9344 (not applicable)       |
| 3   | 0.3455                        | 0.9262 (not applicable)       |
| 4   | 0.1593                        | 0.9344 (not applicable)       |

**Observations**:

(a) For $k = 1$ (primes), the truncated sum over the first 500 primes
is already $> 1.5$. This is because the smallest primes ($p = 2, 3, 5$)
contribute $\approx 0.721 + 0.303 + 0.124 = 1.149$ alone.

(b) For $k \geq 2$, the truncated sums are well below 1.

(c) The $F_3(k)$ formula is an ASYMPTOTIC for $k \to \infty$ and gives poor
approximations for small $k$. For $k = 1$, the formula predicts $0.967$
while the actual sum is $\approx 1.64$ — a substantial discrepancy showing
F3 is not applicable at $k = 1$.

(d) The leading-correction formula is consistent with F2's unsigned $O(k^{-1/2})$:
for large $k$, the correction is negative (as F3 makes precise), resolving
the sign ambiguity. The sum approaches 1 from below.

### 2.2 Prime Sum and Relation to F1

Partial sums $\sum_{p \leq P} 1/(p \log p)$ converge to approximately 1.636:

| Cutoff $P$ | Partial sum |
|-----------|-------------|
| $p = 2$   | 0.7213      |
| $p = 5$   | 1.1490 (exceeds 1) |
| $p = 13$  | 1.2903      |
| $p = 10^7$| 1.5746      |
| all primes (estimated) | $\approx 1.636$ |

This full sum $\approx 1.636 > e^\gamma \pi/4 \approx 1.399$ is NOT a
contradiction to F1, because F1 bounds the sum for $A \subset [x, \infty)$
as $x \to \infty$. At $x = 2$, the F1 bound does not constrain the sum.

**Prime tails** (sums over primes $p \geq x$ for various $x$):

| $x$ | $\sum_{p \geq x} 1/(p \log p)$ (approx) |
|-----|------------------------------------------|
| 2   | $\approx 1.636$                          |
| 3   | $\approx 0.915$ (subtract $1/(2 \log 2) \approx 0.721$) |
| 5   | $\approx 0.611$                          |
| 100 | $\approx 0.217$ (from $\approx 1/\log 100$) |

For $x \geq 3$, the prime tail is already $< 1$. So a primitive set
consisting only of primes in $[x, \infty)$ for $x \geq 3$ cannot achieve
sum $> 1$.

**Next steps**: The open question (Q4) is whether any non-prime primitive
set in $[x, \infty)$ for large $x$ achieves sum $> 1$. Based on the
reasoning that primes are the extremal example (the Zhang-type result),
such a set likely does not exist for $x \geq 3$, consistent with the
conjecture. Q5 will pursue the proof structure.
