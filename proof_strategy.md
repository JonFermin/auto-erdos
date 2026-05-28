# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

---

## Section 1 — Setup (Q1)

### 1.1 The Claim

**Erdős primitive-set conjecture (sharpened form)**. For any $x > 0$, if
$A \subset [x, \infty)$ is a *primitive set* of positive integers (no distinct
element of $A$ divides any other), then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ term tends to $0$ as $x \to \infty$. The supremum of this
sum over all primitive subsets of $[x, \infty)$ is at most $1 + o(1)$ with
the bound tightening toward $1$ as $x$ grows without bound.

The conjecture is **open**. No proof or disproof is claimed here until a
verifier-accepted witness or a complete argument is established.

### 1.2 Given Facts

**F1 (Erdős–Zhang upper bound, 1993)**.
For *any* primitive set $A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
*Sign*: **UPPER** bound — sum is strictly less than 1.399 + o(1). This does
not say the sum exceeds 1. **Scope caveat**: our computation finds
$\sum_p 1/(p \log p) \approx 1.637$, which would exceed 1.399 if the primes
form a primitive set in $\mathbb{N}$. See Section 2.1 for discussion — F1 may
apply to a restricted class or use a different formulation; it must not be
cited as an absolute upper bound without resolving this discrepancy.

**F2 (Omega-stratum lower bound)**. For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$
(integers with exactly $k$ prime factors counted with multiplicity):
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$
*Sign*: the $O(\cdot)$ term is **unsigned** (could be positive or negative).
The inequality says the sum is at least $1 - |\text{error}|$, approaching 1
from **below**. Concluding sum $> 1$ from F2 alone is a sign error.

**F3 (Exact correction for $A_k$, asymptotic for large $k$)**. For $A_k$:
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656.$$
*Sign*: $c > 0$, so the correction is **negative** — each $A_k$ has sum
**strictly less than 1**, approaching 1 from below as $k \to \infty$. This
is an asymptotic formula for large $k$; as shown in Section 2.1, it fails
badly for $k = 1$ where the actual sum is approximately 1.637.

### 1.3 Witness Contract

A claim of disproof requires a **finite** primitive set
$A \subset [x_\text{floor}, \infty)$ with rigorously verified
$\sum_{a \in A} 1/(a \log a) > 1.0$ (the witness threshold $= 1.0$).
The verifier is `library.primitive_set_witness.verify_witness`. Embed a
witness as a single `<!-- WITNESS ... WITNESS -->` block with fields
`x_floor`, `elements`, `claimed_sum_lower_bound` at the bottom of this file.

**Caveat**: a witness at small $x_\text{floor}$ with sum barely above 1.0
is NOT a definitive counterexample. The conjecture says sum $< 1 + o(1)$
where $o(1) \to 0$ as $x \to \infty$; for small $x$ the $o(1)$ slack may
absorb the excess. A true counterexample requires the excess to survive as
$x \to \infty$.

---

## Section 2 — Numerical Grounding (Q2, Q3)

### 2.1 F3 Verification: Truncated Sums for $A_k$

Sieve-computed partial sums over $n \leq 5 \times 10^6$ (each $A_k$ is
primitive: if $a \mid b$ with $\Omega(a) = \Omega(b) = k$, then $b = am$
for $m \geq 2$, forcing $\Omega(b) \geq k+1$, contradiction):

| $k$ | Trunc. sum ($n \leq 5 \times 10^6$) | F3 prediction (infinite) | Ratio |
|-----|--------------------------------------|--------------------------|-------|
| 1   | 1.5718                               | 0.9672                   | 1.63  |
| 2   | 0.8888                               | 0.9344                   | 0.95  |
| 3   | 0.5251                               | 0.9262                   | 0.57  |
| 4   | 0.2834                               | 0.9344                   | 0.30  |
| 5   | 0.1411                               | 0.9487                   | 0.15  |
| 6   | 0.0665                               | 0.9631                   | 0.07  |

**Key discrepancy at $k=1$**: the primes ($A_1$) give truncated sum 1.572
with estimated tail $\approx 1/\log(5 \times 10^6) \approx 0.066$, yielding
full infinite sum $\approx$ **1.637** — far above F3's prediction of 0.967.
This contradicts F3 as a global formula.

*Resolution*: F3 is an asymptotic valid for large $k$. The formula
$1 - (c+o(1))k^2/2^k$ approaches $1$ from below as $k \to \infty$, which is
the qualitative claim; the formula is not numerically accurate for $k = 1$ or $k = 2$.

*F1 tension*: if $\sum_p 1/(p\log p) \approx 1.637$ and the primes form a
primitive set in $\mathbb{N}$, this exceeds F1's stated bound of $\approx 1.399$.
Possible resolution: F1 may apply only to primitive sets bounded above by some
$x$, or the Lichtman–Pomerance (2021) refinement supersedes Zhang's constant
with the exact value $\sum_p 1/(p \log p)$ as the supremum. We do not rely
on F1 as an absolute bound until this is clarified.

### 2.2 Primes Sum from $x_\text{floor}$ (Q3)

$\sum_{p \geq x_\text{floor}} 1/(p \log p)$ over first 10,000 primes ($p \leq 104{,}729$):

| $x_\text{floor}$ | Primes sum | Rigorous lower bound | PNT est. $1/\log x$ |
|------------------|------------|----------------------|----------------------|
| 2                | 1.550      | 1.4965               | 1.443                |
| 3                | 0.8226     | 0.7752               | 0.910                |
| 10               | 0.3215     | 0.2745               | 0.434                |
| 100              | 0.1286     | 0.0775 (200 primes)  | 0.217                |
| 1,000            | 0.0578     | —                    | 0.145                |
| 10,000           | 0.0220     | —                    | 0.109                |

The $p = 2$ term alone contributes $1/(2 \ln 2) \approx 0.721$, explaining the
sharp drop from $x_\text{floor} = 2$ (sum $\approx 1.55$) to $x_\text{floor} = 3$
(sum $\approx 0.78$). For $x_\text{floor} \geq 3$, the primes give sum $< 1$,
consistent with the conjecture.

**Distinction from the asymptotic conjecture**: these are finite sums over
$[x_\text{floor}, \infty) \cap \mathbb{P}$, not the bound $1 + o(1)$ on all
primitive sets. The conjecture's claim is about the supremum over ALL primitive
subsets of $[x_\text{floor}, \infty)$ — which may exceed the primes-only sum
for small $x_\text{floor}$.

---

## Section 3 — Witness Search (Q4)

### 3.1 Protocol

Candidates: $A_k \cap [x_\text{floor}, 2 \times 10^6]$ for $k = 1, \ldots, 10$.
Verified via `library.primitive_set_witness.verify_witness`.

### 3.2 Results

| $x_\text{floor}$ | Best $k$ | Max trunc. sum | Witness (sum $> 1$)? |
|------------------|----------|----------------|----------------------|
| 2                | 1        | 1.568          | **YES** ($x=2$, primes) |
| 10               | 2        | 0.553          | No                   |
| 100              | 2        | 0.298          | No                   |
| 1,000            | 3        | 0.189          | No                   |
| 10,000           | 3        | 0.115          | No                   |

For $x_\text{floor} = 2$: the set $\{2, 3\}$ alone gives rigorously verified
sum $\approx 1.025 > 1.0$ (confirmed by verifier). The first 10 primes give
$\approx 1.35$ (also verified).

For $x_\text{floor} \geq 3$: no witness found with any $A_k$ construction.

### 3.3 Interpretation

The $x_\text{floor} = 2$ witness does **not** disprove the conjecture. At
$x = 2$, the conjecture's bound $1 + o(1)$ allows slack $\geq 0.025$. For a
true counterexample we would need the excess to persist for large $x_\text{floor}$,
but numerically the achievable maximum decreases rapidly (roughly
$\sim 1/\log(x_\text{floor})$). The evidence strongly supports the conjecture
being **true**: by $x_\text{floor} = 3$, no single-stratum or mixing
construction achieves sum $> 1$.

The witness below ($x_\text{floor} = 2$, first 10 primes) is included per
the Q4 protocol — it satisfies the verifier's threshold but does not
constitute a disproof.

---

## Section 4 — Proof Structure Outline (Q5, stub)

**Proposed strategy**: stratify $A \subset [x, \infty)$ by $\Omega$-value.
For each stratum $A^{(k)} = A \cap \{n : \Omega(n) = k\}$, the sum
contribution is at most $f(k, x) = \sum_{n \geq x, \Omega(n)=k} 1/(n \log n)$.

The key estimate: $f(k, x) \approx (1 + \log\log x)^{k-1} / ((k-1)! \log x)$
(from the $k$-almost prime density). Summing over all $k$, optimizing at
$k^* \approx \log\log x$:
$$\sum_{k \geq 1} f(k, x) \lesssim \frac{(\log x)^{o(1)}}{\log x} \to 0.$$

This would prove a stronger bound (sum $\to 0$) than the conjecture's "$< 1 + o(1)$".

**Open gap**: the stratification bounds the sum of ALL $A_k$ strata, but a
primitive set $A$ picks elements from strata non-uniformly. The critical lemma
is that the optimal primitive set in $[x, \infty)$ is either a single-$k$
stratum (or close to it), i.e., mixing cannot improve the bound. This is the
hard lemma to prove and is being tracked in `proof_lemmas/`.

---

<!-- WITNESS
{"x_floor": 2, "elements": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], "claimed_sum_lower_bound": 1.35}
WITNESS -->
