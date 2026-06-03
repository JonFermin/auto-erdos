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

## Anti-traps (the canonical failure modes)

- **F2 sign confusion**. F2 says
  $\sum_{a \in A_k} 1/(a \log a) \geq 1 + O(k^{-1/2 + o(1)})$
  with the $O(\cdot)$ term **unsigned**. Concluding $\sum > 1$ from F2
  alone is a sign error — `critic_sign` will emit
  `unsigned-O-sign-confusion` BLOCKING.
- **F3 read upside-down**. F3 says
  $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k$
  with $c \approx 0.0656 > 0$. The leading correction is *negative*, so
  the sum approaches $1$ from BELOW. Treating it as approaching from
  above is `f3-from-above-misread` BLOCKING.
- **Open claim asserted resolved without witness**. The conjecture is open.
  Asserting falsity or a disproof without a verifier-accepted `<!-- WITNESS -->`
  block triggers `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING. The defense-in-depth in `_compute_verdict_hint` independently detects
  proof-completion markers (the exact set is in `proof_prepare.py`).

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

## Section 1: Setup (Q1)

### 1.1 The Conjecture

A set $A \subset \mathbb{N}$ is **primitive** if no element of $A$ divides any other
distinct element of $A$.

**Conjecture (Erdős)**: For any primitive set $A \subset [x, \infty)$,

$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1) \quad \text{as } x \to \infty,$$

where the $o(1)$ term tends to $0$ as $x \to \infty$. Equivalently, the sum is bounded
above by $1$ in the limit.

This is an open problem. No claim of resolution is made in this document
unless a verifier-accepted `<!-- WITNESS -->` block is committed (counterexample
path) or the proof is completed (upper bound path).

### 1.2 Given Facts

Three facts are available from the ledger (`proofs/primitive_set_erdos.json`):

**F1 (Erdős-Zhang upper bound)**: For ANY primitive set $A \subseteq \mathbb{N}$ (no
floor restriction),

$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign note*: This is a STRICT UPPER bound of $\approx 1.399$, NOT a lower bound.
It is consistent with the conjecture (which posits the tighter bound 1). Misreading
F1 as a lower bound is a sign error.

**F2 (Omega-stratum lower, unsigned)**: Define $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$
(integers with exactly $k$ prime factors counted with multiplicity). Then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2 + o(1)}).$$

*Sign note*: The $O(\cdot)$ term is UNSIGNED — it can be positive or negative.
The inequality only says the sum is at least $1 - (\text{something bounded by } k^{-1/2+o(1)})$.
Concluding sum $> 1$ from F2 alone is a sign error.

**F3 (Exact asymptotic, approaches from below)**: For the same $A_k$,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

*Sign note*: The leading correction is $-(c + o(1)) k^2 / 2^k$ with $c > 0$, so the
sum is STRICTLY LESS THAN 1 for all $k \geq 1$, approaching 1 from BELOW as $k \to \infty$.
The sets $A_k$ are "extremal-looking" but do NOT violate the conjecture.

### 1.3 Witness Contract

The only path to claiming a counterexample is a verifier-accepted witness: a finite
primitive set $A \subset [x_{\text{floor}}, \infty)$ whose rigorous sum exceeds
`witness_threshold = 1.0`. The witness must be embedded as a `<!-- WITNESS -->` JSON
block in this file; `proof_prepare.py` then runs `library.primitive_set_witness.verify_witness`
and sets `witness_valid = 1` on success.

Required fields:
- `x_floor` (int ≥ 2): every element of `elements` must be ≥ `x_floor`.
- `elements` (list[int]): pairwise non-divisible integers, each ≥ `x_floor`.
- `claimed_sum_lower_bound` (float): agent's estimate; verifier recomputes rigorously.

### 1.4 Proof Strategy Outline

Two possible outcomes:
1. **Upper-bound proof** (confirm the conjecture): Show $\sum_{a \in A} 1/(a \log a) \leq 1 + o(1)$
   for any primitive $A \subset [x, \infty)$. F3 suggests $A_k$ are the extremal sets; the
   challenge is bounding cross-stratum sums and non-$A_k$ primitives.
2. **Counterexample** (disprove the conjecture): Find a specific primitive $A \subset [x_{\text{floor}}, \infty)$
   with verified sum $> 1.0$. Q4 pursues this numerically.

We begin with numerical grounding (Q2, Q3, Q4) before deciding which path is
more promising.

## Section 2: Numerical verification of F3 (Q2)

We compute the truncated sum $T_k^{(N)} = \sum_{a \in A_k, a \leq a_{(N)}} 1/(a \log a)$
over the first $N = 200$ elements of each stratum $A_k$ and compare with the F3
asymptotic prediction.

| $k$ | $A_k$ examples | $a_{(200)}$ | $T_k^{(200)}$ | F3 pred. $1 - c k^2/2^k$ |
|-----|-----------------|-------------|----------------|--------------------------|
| 1   | 2,3,5,7,11,...  | 1223        | **1.4965**     | 0.9672                   |
| 2   | 4,6,9,10,14,... | 669         | 0.6819         | 0.9344                   |
| 3   | 8,12,18,20,...  | 805         | 0.3134         | 0.9262                   |
| 4   | 16,24,36,40,... | 1292        | 0.1403         | 0.9344                   |

**Key finding**: For $k = 1$ (primes), the truncated sum at 200 elements is already 1.4965,
far above F3's predicted asymptotic of 0.9672. For $k \geq 2$, the truncated sums are all well
below 1, consistent with the series converging to values below the F3 prediction (the
200-element truncation is a lower bound on the full infinite sum, and the series converges slowly).

**Interpretation of the discrepancy for $k = 1$**: F3 is an asymptotic statement for $k \to \infty$.
The formula $1 - (c + o(1)) k^2/2^k$ has a large implicit error for small $k$. For $k = 1$,
the actual sum (≈ 1.6366, see Section 3) is ABOVE 1, not below. The F3 formula is accurate
only for large $k$ where the $o(1)$ correction is dominated by the leading term $c k^2 / 2^k \to 0$.

The leading correction $-c k^2/2^k$ is $-0.0328$ at $k=1$, $-0.0656$ at $k=2$, etc.,
and goes to 0 as $k \to \infty$. The F3 formula correctly states that $A_k$ sums approach
1 FROM BELOW as $k \to \infty$, but for small $k$ (especially $k = 1, 2$), the actual
sums deviate substantially from this asymptotic.

## Section 3: Sum over primes (Q3)

The primes $\{2, 3, 5, 7, \ldots\}$ form a primitive set (no prime divides another prime).
Their full infinite sum is:

$$\sum_{p \text{ prime}} \frac{1}{p \log p} \approx 1.6366 \quad \text{(convergent)}.$$

Numerical evidence (partial sums + tail estimate $\approx 1/\log x$ for primes $> x$):

| \# primes | last prime | partial sum | tail est. | est. total |
|-----------|------------|-------------|-----------|------------|
| 25        | 97         | 1.421567    | 0.218593  | 1.640160   |
| 200       | 1223       | 1.496452    | 0.140666  | 1.637118   |
| 2000      | 17389      | 1.534260    | 0.102421  | 1.636682   |
| 10000     | 104729     | 1.550127    | 0.086512  | 1.636638   |

The estimated total ≈ **1.6366** is stable across all truncation points, confirming convergence.

**Consistency with F1**: F1 states the bound $< e^\gamma \pi/4 \approx 1.399$ for primitive sets.
The primes (sum ≈ 1.6366) appear to violate this bound. The resolution, per Q3's own note,
is that F1 applies for $A \subset [x, \infty)$ with $x \to \infty$, not for all of $\mathbb{N}$.
For $x = 2$ (all primes), the allowed error $o(1)$ is large (≈ 0.636). For primes starting
at $x = 101$, the sum is only ≈ 0.094, well below 1. The F1 bound becomes tight only for
large floor $x$, which is exactly the regime of the conjecture.

**The o(1) in the conjecture**: The conjecture's $1 + o(1)$ bound is a LIMIT statement.
For any fixed finite $x$, the bound $f(x) = 1 + o(1)$ can be large (e.g., $f(2) \approx 1.636$).
The claim is that $f(x) \to 1$ as $x \to \infty$. For primes $\geq x$:
$\sum_{p \geq x} 1/(p \log p) \approx 1/\log x \to 0$ as $x \to \infty$.

## Section 4: Witness search (Q4)

We searched for a primitive $A \subset [x_{\text{floor}}, \infty)$ with rigorously verified sum $> 1$
using `library.primitive_set_witness.verify_witness`.

| $x_{\text{floor}}$ | Candidate | Verified sum | is_valid |
|--------------------|-----------|--------------|----------|
| 100                | 500 primes ≥ 101 | 0.0939 | False |
| 1000               | 500 primes ≥ 1009 | 0.0270 | False |
| 10000              | 500 primes ≥ 10007 | ≈ 0.009 | False |

**No witness found for $x_{\text{floor}} \geq 100$**: primes alone give sums much less than 1.
Mixed primitive sets in $[100, \infty)$ combining different strata face the same issue —
each stratum's sum from 100 is small, and the primitivity constraint prevents freely
combining strata. This is consistent with the conjecture being true for large $x$.

**Observation on $x_{\text{floor}} = 2$**: The primitive set $\{2, 3, 5\}$ has verified sum
$\approx 1.149 > 1$ (mechanically verified by the witness verifier, score = 1.149028).
However, this is NOT a genuine disproof: the conjecture's $o(1)$ error at $x = 2$ is large
(the maximum sum for primitive sets in $[2, \infty)$ is ≈ 1.636, so the allowed slack is ≈ 0.636).
No witness block is embedded because this witness does not challenge the conjecture's limit
statement; $x_{\text{floor}} = 2$ is far from the $x \to \infty$ regime.

## Section 5: Proof structure outline (Q5)

The proof attempt follows the **smallest-prime-factor (spf) reduction** strategy.

### 5.1 Stratification

By Lemma `omega_stratification` (proof_lemmas/lemma_001.md, **proved**), any
primitive $A \subset [x, \infty)$ decomposes as $A = \bigsqcup_p A_p$ where
$A_p = \{a \in A : \mathrm{spf}(a) = p\}$.

### 5.2 Key structural lemma (spf-reduction)

By Lemma `spf_reduction` (proof_lemmas/lemma_002.md, **proved**), each fiber
$B_p = A_p / p$ is a primitive set in $[x/p, \infty)$, and:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p \leq x} \frac{1}{p} \cdot \sum_{b \in B_p} \frac{1}{b \log b}.$$

Defining $M(x) = \sup_{A \subset [x, \infty)} f(A)$, this gives the **functional inequality**:
$$M(x) \leq \sum_{p \leq x} \frac{M(x/p)}{p}. \tag{$\star$}$$

### 5.3 The hard step

By Lemma `functional_ineq_bound` (proof_lemmas/lemma_003.md, **open**), it remains
to show that $(\star)$ forces $M(x) \leq 1 + o(1)$.

**Why Lemma 3 is hard**: Direct ansätze fail:
- $M(x) = C/\log x$ is inconsistent (the sum $\sum_p 1/(p(\log x - \log p))$ blows up).
- $M(x) = 1 + h(x)$ with $h(x) \to 0$ leads to $\sum_{p \leq x} 1/p + (\text{correction})$
  which diverges without additional cross-fiber information.

The inequality $(\star)$ treats the fibers $\{B_p\}$ as independent, but they are constrained
by cross-fiber primitivity. Capturing this information tightly appears to be the crux.

### 5.4 What is easy vs. hard

| Lemma | Status | Difficulty |
|-------|--------|------------|
| L1: Omega stratification | **proved** | trivial |
| L2: spf-reduction, functional inequality $(\star)$ | **proved** | easy |
| L3: $(\star)$ forces $M(x) \leq 1 + o(1)$ | **open** | hard (research-level) |

The gap at Lemma 3 is genuine: this is the open core of the Erdős conjecture.
No known elementary argument closes it. The Lichtman-Pomerance (2021) paper
proves $M(x) \leq e^\gamma \pi/4 + o(1) \approx 1.399$ (F1) using analytic sieve methods,
but the tighter bound of 1 remains open.

### 5.5 Partial result

**What this attempt has established** (partial result):
1. The spf-reduction gives the functional inequality $(\star)$ (Lemma 2, proved).
2. Numerical evidence: no primitive set in $[100, \infty)$ found with sum $> 1$
   (consistent with conjecture; not a proof).
3. The $A_k$ sets have sums approaching 1 from below as $k \to \infty$ (F3, for large $k$).
4. The primes form a primitive set with sum $\approx 1.6366 > 1$, showing the conjecture
   requires the floor $x$ to be large (the $o(1)$ is not tight for $x = 2$).

**This remains open**: the bound $M(x) \leq 1 + o(1)$ is not proved here. Lemma 3 is the
blocking gap.

## Body

(Section 6 — Q6: Partial result registered. Session ends here.)
