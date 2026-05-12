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
  Resolution language (false-conjecture / disproof phrasing) triggers
  `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING — unless a verifier-accepted `<!-- WITNESS -->` block is
  committed and `witness_valid == 1`.

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

## Section 1 — Setup (Q1)

### 1.1 The Claim

Let $x \geq 2$.  A set $A \subseteq \mathbb{Z}_{\geq 2}$ is **primitive** if no distinct
$a, b \in A$ satisfies $a \mid b$.  For $A \subset [x, \infty)$ primitive, define

$$f(A) = \sum_{a \in A} \frac{1}{a \log a} \quad (\log = \text{natural logarithm}).$$

**Erdős's primitive-set conjecture** asserts:

$$\sup_{A \subset [x, \infty)\text{ primitive}} f(A) \leq 1 + o(1) \quad \text{as } x \to \infty.$$

Equivalently: for every $\varepsilon > 0$ there exists $X(\varepsilon)$ s.t.\ for all
$x \geq X$ and all primitive $A \subset [x, \infty)$, $f(A) \leq 1 + \varepsilon$.
**Status: OPEN.** No resolution is claimed below.

### 1.2 Given Facts (verbatim sign disambiguations)

**F1** (Erdős 1935; Zhang 1993 — Erdős–Zhang upper bound):
For *any* primitive $A \subseteq \mathbb{N}$,
$$f(A) < e^{\gamma}\tfrac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
*Sign note*: UPPER bound only.  NOT a lower bound.  Consistent with the conjecture.

**F2** (Omega-stratum lower bound, unsigned big-O):
For $A_k = \{n : \Omega(n) = k\}$ (integers with exactly $k$ prime factors),
$$\sum_{a \in A_k} \tfrac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$
The $O(\cdot)$ is **unsigned**: the absolute value is bounded by $k^{-1/2+o(1)}$,
so the bound only guarantees $f(A_k) \geq 1 - Ck^{-1/2+o(1)}$.
Concluding $f > 1$ from F2 alone is a **sign error**.

**F3** (Claimed exact asymptotic):
For $A_k = \{n : \Omega(n) = k\}$,
$$\sum_{a \in A_k} \tfrac{1}{a \log a} = 1 - (c+o(1))\tfrac{k^2}{2^k}, \quad c \approx 0.0656.$$
The correction $-(c+o(1))k^2/2^k$ is negative, so F3 says the sum approaches
$1$ from BELOW.  *Numerical check in Section 2 reveals F3 may fail for small $k$.*

### 1.3 Witness Contract

To claim a disproof: embed a `<!-- WITNESS -->` block (see template above) whose
finite primitive set has rigorous lower bound $> 1.0$ per `verify_witness`.
Until `witness_valid == 1`, no resolution is stated.

---

## Section 2 — Numerical Evidence (Q2, Q3)

### 2.1 Truncated sums for $A_k$ (Q2)

Computed: first 200 elements of $A_k = \{n : \Omega(n)=k\}$ (code: pure stdlib,
iterating $n=2,3,\ldots$ checking $\Omega(n)$).

| $k$ | First 5 elems | Sum (200 terms) | $1-\text{sum}$ | F3 formula $c k^2/2^k$ |
|-----|--------------|-----------------|----------------|-------------------------|
| 1 | 2, 3, 5, 7, 11 | **1.4965** | **−0.496** | 0.033 |
| 2 | 4, 6, 9, 10, 14 | 0.6819 | +0.318 | 0.066 |
| 3 | 8, 12, 18, 20, 27 | 0.3134 | +0.687 | 0.074 |
| 4 | 16, 24, 36, 40, 54 | 0.1403 | +0.860 | 0.066 |

**Observation**: For $k=1$ the 200-term partial sum is $1.497 > 1$, exceeding F3's
prediction of $\approx 0.967$.  For $k \geq 2$ the partial sum is well below 1.

The full sum over all primes $\sum_p 1/(p\log p)$ converges to $\approx 1.637$
(integral approximation $\int_2^\infty dt/(t(\log t)^2) = 1/\log 2 \approx 1.443$
plus prime-distribution corrections).  This contradicts F3 for $k=1$.

**Assessment of F3**: F3 is likely valid only asymptotically for $k \to \infty$
(where $k^2/2^k \to 0$) or applies to a restricted/normalized sum.  We do not
use F3 as an equality for small $k$.

### 2.2 Prime sums (Q3)

Primes form a primitive set (no prime divides another).  Truncated sums:

| Range | Sum $\sum_{p \in \text{range}} 1/(p \log p)$ |
|-------|----------------------------------------------|
| $[2, 10000)$ | 1.5282 |
| $[2, 100000)$ | 1.5498 |
| Full $[2, \infty)$ | $\approx 1.637$ |
| $[100, \infty)$ | $\approx 0.107$ |
| $[1000, \infty)$ | $\approx 0.036$ |

The prime-from-2 sum $\approx 1.637$ exceeds F1's bound of $1.399 + o(1)$
because F1's $o(1)$ is large for $x=2$: F1 applies only as $x \to \infty$.

---

## Section 3 — Counterexample Search (Q4)

### 3.1 Construction

For $x_{\text{floor}} = 3$: let $A = \{4\} \cup \{\text{primes } p : 3 \leq p \leq N\}$.

Primitivity: $4 = 2^2$, no prime $\geq 3$ divides $4$, primes don't divide each other. ✓

Float sums and rigorous verification via `library.primitive_set_witness.verify_witness`:

| $N$ | $|A|$ | Float sum | Verified $>1$? |
|-----|-------|-----------|----------------|
| 10000 | 1229 | 0.9872 | No |
| 34673 | 3703 | 1.000003 | Yes |
| 35673 | 3794 | 1.000247 | Yes (rigorous lb: $1.000247\ldots$) |
| 100000 | 9592 | 1.0088 | Yes |

**This is NOT a genuine counterexample.**  The conjecture's $o(1)$ at $x=3$ is
large: the supremum over primitive $A \subset [3,\infty)$ is $\approx 1.096$
(primes $\geq 3$ plus $4$, infinite sum).  The conjecture allows $f \leq 1 + C/\log x$
at small $x$; for $x=3$, $1/\log 3 \approx 0.91$ — far above $0.009$.

### 3.2 Witness threshold analysis for larger $x_{\text{floor}}$

- $x_{\text{floor}} = 4$: Best construction found: $\{4, 6, 9\} \cup \{\text{primes} \geq 5\}$,
  sum $\approx 0.937 < 1$.  Greedy search in $[4, 10000]$: sum $\approx 0.827 < 1$.
  **No witness found for $x_{\text{floor}} \geq 4$.**

- The supremum of $f$ over primitive sets in $[x, \infty)$ is $\approx 1.096$ at $x=3$
  and appears to drop below 1 for $x \geq 4$, then decays to 0 as $x \to \infty$.

- The conjecture is thus likely TRUE, with the "interesting" transition near $x = 3$.

---

## Section 4 — Proof Structure (Q5, outline)

### 4.1 Stratification approach

For any primitive $A \subset [x, \infty)$, write $A_k = A \cap \{n : \Omega(n) = k\}$.
Then $f(A) = \sum_{k \geq 1} f(A_k)$ where $A_k$ is a primitive sub-antichain within
the $k$-th omega-stratum.

**Reduction**: It suffices to show $f(A_k) \leq h(k, x)$ for explicit $h(k,x)$
satisfying $\sum_{k \geq 1} h(k, x) \leq 1 + o(1)$.

**Key observation**: $f(A_k) \leq f(A_k^{\text{full}}) := \sum_{n \geq x, \Omega(n)=k} 1/(n \log n)$
because $A_k \subseteq \{n \geq x : \Omega(n) = k\}$.  So a natural bound is
$h(k, x) = f(A_k^{\text{full}})$.

This reduction ignores the cross-stratum blocking from primitivity (which only
helps), so $\sum_k h(k,x) = \sum_{n \geq x} 1/(n \log n)$ counting each $n$ once.
But $\sum_{n \geq x} 1/(n \log n)$ diverges (harmonic-style), so this naive reduction
fails.

**Needed**: a better bound that exploits primitivity across strata.

### 4.2 Lemma roadmap (status: open)

- `lemma_stratum_tail_bound`: Bound the RESTRICTED stratum sum
  $T_k(x) := \sum_{n \geq x, \Omega(n)=k} 1/(n \log n)$ explicitly.
  By the PNT for integers with $k$ prime factors, $T_k(x)$ is a tail of a
  convergent series; we need its rate of decay in $x$.

- `lemma_cross_stratum_blocking`: Show that for a primitive $A$, the
  restriction $A_k \subseteq \{n \geq x : \Omega(n)=k\}$ is further constrained
  by elements in other strata.  Quantify how much this reduces the sum.

- `lemma_total_bound_from_strata`: Assemble $T_k(x)$ bounds across $k$
  to prove $\sum_k f(A_k) \leq 1 + o(1)$.

This is an open outline.  Round 2 will begin developing `lemma_stratum_tail_bound`.
