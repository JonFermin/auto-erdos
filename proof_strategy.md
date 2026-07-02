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
  Resolution phrasing (asserting the conjecture has been settled, asserting
  a complete proof or disproof without a verifier-accepted witness, etc.)
  triggers `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING — unless a verifier-accepted `<!-- WITNESS -->` block is committed
  and `witness_valid == 1`.

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

## Section 1 — Setup

### 1.1 The conjecture

**Conjecture (Erdős primitive-set).** For any $x \geq 2$, if $A \subset [x, \infty)$ is a
*primitive set* of positive integers (no element of $A$ divides any other distinct element
of $A$), then
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
where $o(1) \to 0$ as $x \to \infty$.

A **primitive set** is an antichain of positive integers under divisibility: for $a, b \in A$
with $a \neq b$, we have $a \nmid b$. The natural density of any primitive set is zero
(Erdős, 1935). The sum $\sum 1/(a \log a)$ is the Erdős-style measure that weights each
element by the reciprocal of its "logarithmic density" $1/\log a$.

The conjecture claims that restricting elements to lie above a threshold $x$ forces the
sum below $1 + o(1)$. As $x \to \infty$ the bound approaches 1 exactly.

**Claim status**: open. The best unconditional upper bound is $\approx 1.399$ (see F1).
No proof or counterexample is currently known.

---

### 1.2 Given facts ledger

Three facts are taken as given. Each carries a sign disambiguation — the canonical failure
mode for this problem is misreading an unsigned big-O as having a definite sign.

**F1 — Erdős-Zhang upper bound** (Erdős 1935; Zhang 1993):
For any primitive set $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
*Sign disambiguation*: UPPER bound, strictly less than. Does NOT contradict the conjecture.
Misreading as a lower bound is a sign error.

**F2 — Omega-stratum lower bound with unsigned big-O**:
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$. Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2 + o(1)}).$$
*Sign disambiguation*: The $O(\cdot)$ is UNSIGNED. Concluding $\sum > 1$ from F2 alone
is a sign error. Any chain that uses F2 to infer $\sum > 1$ without an independent
positivity argument for the correction term is BLOCKING.

**F3 — Exact asymptotic, sum approaches 1 from below**:
For $A_k$ as above,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
*Sign disambiguation*: The leading correction is $-(c+o(1))k^2/2^k$ with $c > 0$, so
the sum is strictly less than 1 for all $k \geq 1$ and approaches 1 from BELOW as
$k \to \infty$. F3 is consistent with F2 once F2's unsigned-O is read correctly.

---

### 1.3 Witness contract

A finite set $A \subset [x_{\text{floor}}, \infty)$ that is primitive and has
rigorously-verified $\sum_{a \in A} 1/(a \log a) > 1$ would be a candidate
counterexample. The verifier is `library.primitive_set_witness.verify_witness`, which
uses `decimal`-precision arithmetic (~50 digits) with a documented 4-ULP slack.

To embed a witness, add a `<!-- WITNESS ... WITNESS -->` block at the bottom of this
file with JSON payload:
```json
{
  "x_floor": <int, >= 2>,
  "elements": [<list of ints, pairwise non-divisible, all >= x_floor>],
  "claimed_sum_lower_bound": <float>
}
```
The verifier recomputes the sum independently. Without this block, `witness_valid = 0`.

**Caveat**: A witness at small $x_{\text{floor}}$ where the $o(1)$ gap in the conjecture
is still large is suggestive but not conclusive. Establishing a genuine counterexample
requires either showing the $o(1)$ is already negligible at the given $x_{\text{floor}}$,
or using a very large $x_{\text{floor}}$.

---

### 1.4 Proof strategy overview

The standard strategy (which this attempt will explore) is omega-stratification:

1. **Stratify**: write any primitive $A \subset [x, \infty)$ as
   $A = \bigsqcup_{k \geq 1} (A \cap A_k)$ where $A_k = \{n : \Omega(n) = k\}$.
2. **Per-stratum bound**: the contribution of the $k$-th piece is at most
   $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1))k^2/2^k < 1$ (by F3).
   Note F3 applies to the FULL $A_k$; the piece $A \cap A_k$ is a subset, so its
   contribution is at most the full-stratum sum.
3. **Combine strata**: this is the hard step. The per-stratum bounds cannot be naively
   summed (the sum $\sum_{k \geq 1} 1 = \infty$). The key insight must be that elements
   from different strata interact in a way that prevents more than one stratum from
   contributing close to 1 simultaneously.

The known F1 bound ($\approx 1.399$) uses a different argument. Improving to $1 + o(1)$
likely requires quantifying how much of each stratum a primitive set can simultaneously
use — a cross-stratum interaction estimate. This will be developed in subsequent lemmas.

Work continues in `proof_lemmas/` (see Q5).

---

**(Section 1 complete.)**

---

## Section 2 — Numerical Calibration of F3

### 2.1 The correction-term function $\phi(k) = k^2/2^k$

F3 states
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656 > 0,$$
with the $o(1)$ as $k \to \infty$. Because $c > 0$ the entire correction is negative for every $k \geq 1$, so each stratum sum is **strictly less than 1** (F3, sign disambiguation).

The function $\phi(k) = k^2/2^k$ governs how far each stratum lies below 1. Using $c = 0.0656$:

| $k$ | $\phi(k) = k^2/2^k$ | $c \cdot \phi(k)$ | Leading-order stratum sum |
|:---:|:-------------------:|:------------------:|:------------------------:|
| 1   | $1/2 = 0.5000$      | $0.0328$           | $\approx 0.967$           |
| 2   | $4/4 = 1.0000$      | $0.0656$           | $\approx 0.934$           |
| 3   | $9/8 = 1.1250$      | $0.0738$           | $\approx 0.926$           |
| 4   | $16/16 = 1.0000$    | $0.0656$           | $\approx 0.934$           |
| 5   | $25/32 = 0.7813$    | $0.0513$           | $\approx 0.949$           |
| 10  | $100/1024 = 0.0977$ | $0.0064$           | $\approx 0.994$           |

Every leading-order estimate is below 1, directly confirming F3's "<1 for all $k\geq 1$" assertion. The correction $c \cdot \phi(k)$ peaks at $k = 3$ (value $\approx 0.0738$) and decays to 0 at geometric rate $O(k^2/2^k)$.

### 2.2 Monotonicity and the approach from below

$\phi(k) = k^2/2^k$ is increasing for $k \leq 2$, peaks at $k = 2$–$3$ (the discrete maximum is at $k = 3$, $\phi(3) = 9/8 > \phi(2) = 1$), then decreasing. Concretely:
- $k = 1$: correction $= c/2 \approx 0.033$; stratum sum $\approx 0.967$ (F3).
- $k = 3$: largest correction $\approx 0.074$; stratum sum $\approx 0.926$ (furthest from 1).
- $k \geq 4$: corrections decay; sums converge monotonically toward 1 from below.

This "funnel" shape is key: the low-$k$ strata ($k \leq 3$) each sit at least 3% below 1, while the high-$k$ strata approach 1 exponentially fast.

### 2.3 Subset bound for primitive-set slices

For any primitive $A \subset [x, \infty)$ and any fixed $k$, the $k$-th slice $A \cap A_k$ is a subset of $A_k$, so
$$\sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\phi(k) < 1.$$

Each individual stratum contributes strictly less than 1. The difficulty (addressed in Section 3 / Q5) is that any *sum* $\sum_k (\text{something} < 1)$ can diverge: the strata-sum bound alone does not bound the total $\sum_{a \in A} 1/(a \log a)$.

### 2.4 What this section establishes

- **F3 is quantitatively consistent**: the correction term $c \cdot \phi(k)$ with $c = 0.0656$ is positive for all $k \geq 1$, yielding stratum sums strictly below 1.
- **The gap below 1 is smallest for $k=1$** ($\approx 3.3\%$) and for large $k$ ($\to 0\%$); the widest gap is at $k=3$ ($\approx 7.4\%$).
- **No stratum alone threatens the conjecture bound $< 1+o(1)$** — the challenge is cross-stratum accumulation.

---

**(Section 2 complete — Section 3 will address the cross-stratum argument.)**
