# Proof attempt — `primitive_set_erdos`

## Setup

**Claim**: For any primitive set $A \subseteq [x, \infty)$ (no distinct $a, b \in A$
with $a | b$), $\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$ as $x \to \infty$.

**Status**: open. This is an open conjecture; no counterexample or proof exists.
No resolution claim is made here.

**Given facts** (ledger: F1, F2, F3 only):

- **F1**: For any primitive $A \subseteq \mathbb{N}$,
  $\sum_{a \in A} 1/(a \log a) < e^\gamma \pi/4 + o(1) \approx 1.399 + o(1)$.
  UPPER bound; consistent with the conjecture.

- **F2**: For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
  $\sum_{a \in A_k} 1/(a \log a) \geq 1 + O(k^{-1/2+o(1)})$.
  The $O$-term is UNSIGNED — do not infer sum $> 1$ from F2 alone.

- **F3**: For $A_k$ as above,
  $\sum_{a \in A_k} 1/(a \log a) = 1 - (c + o(1)) k^2/2^k$, $c \approx 0.0656 > 0$.
  Correction is NEGATIVE; sum approaches 1 from BELOW.

## Section 1: Omega-Stratification Structure

Let $A \subseteq [x, \infty)$ be a primitive set. Define:
$$A_k = \{a \in A : \Omega(a) = k\}, \quad k \geq 1.$$
Then $A = \bigsqcup_{k \geq 1} A_k$ and:
$$f(A) := \sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} f(A_k), \quad
f(A_k) = \sum_{a \in A_k} \frac{1}{a \log a}.$$

By Lemma `stratification_setup` (proved):

1. Within each $A_k$, no element properly divides another.
2. For $j < k$, $a \in A_j$, $b \in A_k$: primitivity forces $a \nmid b$.

## Section 2: Single-Stratum Bound (Easy)

By Lemma `single_stratum_f3_bound` (proved):

For each $k \geq 1$, $f(A_k) \leq \sum_{n \geq 2, \Omega(n)=k} 1/(n \log n)$.
By F3 (correction NEGATIVE), this full-stratum sum equals $1 - (c+o(1))k^2/2^k < 1$.
Therefore:
$$f(A_k) < 1 \quad \text{for each } k \geq 1.$$

**Critical limitation**: Summing across $k$ gives $f(A) < +\infty$ — vacuous.
Bounding the TOTAL requires the cross-stratum constraint.

## Section 3: The Proof Gap (Cross-Stratum Interaction)

By Lemma `cross_stratum_interaction` (status: open):

To show $f(A) = \sum_{k \geq 1} f(A_k) < 1 + o(1)$, we need to use the
cross-stratum constraint: for $j < k$, elements of $A_j$ cannot divide
elements of $A_k$.

**What the available facts yield**:
- F1 gives $f(A) < 1.399 + o(1)$ as a black-box bound. This does not close
  the gap to $1 + o(1)$.
- F2 has an unsigned $O$-term and supplies no positivity.
- F3 bounds each stratum individually; summing naively is vacuous.

**The obstacle**: Even knowing each $A_k$ contributes $< 1$, and that elements
of lower strata block higher-stratum elements, we cannot derive a bound of
$1 + o(1)$ on the total using F1, F2, F3 alone. The required cross-stratum
reduction estimate is not in the given-facts ledger.

## Section 4: Partial Result

This constitutes a **partial result**:

- Proved: $f(A_k) < 1$ for each stratum (Lemma `single_stratum_f3_bound`, via F3).
- Proved: stratification structure and cross-stratum constraint
  (Lemma `stratification_setup`).
- Identified: the genuine open gap is a quantitative cross-stratum bound
  (Lemma `cross_stratum_interaction`).

**What this session rules out**:
- No single-stratum argument can prove the conjecture; each stratum is
  individually bounded but their sum is not bounded by a single-stratum approach.
- F2 alone (with unsigned $O$) cannot establish any sum exceeds 1.
- F3 alone (with negative correction) cannot bound the multi-stratum total.

The conjecture remains open. This session documents the proof structure and
identifies the hard subproblem (cross-stratum quantitative exclusion) as the
key obstacle.
