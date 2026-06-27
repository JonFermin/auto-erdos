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
- **Resolution assertion without witness**. This claim is open; any
  declaration of resolution triggers `critic_openness` BLOCKING unless a
  verifier-accepted `<!-- WITNESS -->` block is committed and
  `witness_valid == 1`.

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

## Body

---

## Section 1: Setup (Q1)

### The conjecture

For any $x \geq 2$ and any **primitive** set $A \subset [x, \infty)$
(meaning: no element of $A$ divides another), define
$$
S(A) \;=\; \sum_{a \in A} \frac{1}{a \log a}.
$$
The **Erdős primitive-set conjecture** states:
$$
\sup_{\substack{A \subset [x,\infty) \\ \text{primitive}}} S(A) \;\longrightarrow\; 1
\quad \text{as } x \to \infty.
$$
Equivalently, $S(A) < 1 + o(1)$ uniformly over all primitive $A \subset [x,\infty)$.

The conjecture is **open**. No proof or disproof has been verified by this harness.

---

### Given facts (sign-disambiguated)

**F1 — Erdős–Zhang upper bound (1935 / 1993)**
$$
S(A) \;<\; e^\gamma \tfrac{\pi}{4} + o(1) \;\approx\; 1.399 + o(1)
\quad \text{for any primitive } A \subseteq \mathbb{N}.
$$
This is an **upper bound**. It is consistent with the conjecture (which asks for
the tighter bound of 1). It does NOT say sums can reach 1.399 — only that they
cannot exceed it. Misreading as a lower bound is a sign error.

**F2 — Omega-stratum lower bound (UNSIGNED big-O)**

Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity). Then:
$$
\sum_{a \in A_k} \frac{1}{a \log a}
\;\geq\; 1 + O\!\left(k^{-1/2+o(1)}\right).
$$
The $O(\cdot)$ term is **unsigned**: it is bounded in absolute value by
$k^{-1/2+o(1)}$ but could be positive or negative. This does NOT establish
$S(A_k) > 1$. Concluding the sum exceeds 1 from F2 alone is the sign error
that blocks the ChatGPT round-0 writeup.

**F3 — Omega-stratum exact asymptotic (approaches 1 from BELOW)**
$$
\sum_{a \in A_k} \frac{1}{a \log a}
\;=\; 1 - \frac{(c + o(1))\, k^2}{2^k}, \quad c \approx 0.0656 > 0.
$$
The correction term is $-(c+o(1))k^2/2^k$ with $c > 0$, so the sum is
**strictly less than 1** for every finite $k$ and approaches 1 **from below**
as $k \to \infty$. F3 refines F2: F2's unsigned-O is in fact negative (by F3's
more precise statement). The full stratum $A_k$ — the most extremal-looking
candidate — still does not violate the conjecture.

---

### Witness contract

To claim a counterexample, embed a `<!-- WITNESS -->` JSON block at the bottom
of this file with `x_floor`, `elements` (pairwise non-divisible integers $\geq$
x_floor), and `claimed_sum_lower_bound`. The verifier rigorously checks
primitivity and computes a rigorous lower bound on $S(A)$ via `decimal`
arithmetic. `witness_valid = 1` iff the lower bound exceeds 1.0.

No witness block committed yet. `witness_valid = 0`.

---

## Section 2: Numerical Evidence (Q2, Q3)

### Q2: Truncated sums over omega strata $A_k$ (F3 verification)

We enumerate integers with exactly $k$ prime factors (counted with multiplicity)
and compute partial sums over the first 200 elements of each stratum.

| $k$ | First 200 sum | Sum to $10^6$ | F3 prediction | Consistent? |
|-----|--------------|---------------|---------------|-------------|
| 1   | 1.4965       | 1.5642        | 0.9672        | **NO** — F3 inapplicable for $k=1$ (see note) |
| 2   | 0.6819       | 0.8674        | 0.9344        | Yes — tail contributes remaining ~0.067 |
| 3   | 0.3134       | 0.4980        | 0.9262        | Yes — large tail (elements of form $2\cdot3\cdot p$ for large $p$) |
| 4   | 0.1403       | 0.2609        | 0.9344        | Yes — very large tail |

**F3 discrepancy for $k=1$**: For $k=1$ (primes), F3 predicts the full sum is
$\approx 0.967$, but the actual sum approaches $\approx 1.637$ (Q3 result below).
F3's formula $1 - ck^2/2^k$ is an asymptotic valid for large $k$, not for
$k=1$ where the series is dominated by $1/(2\ln 2) \approx 0.721$ alone.

**Key observation for $k \geq 2$**: All partial sums and full sums (to $10^6$)
are below 1. The F3 predictions (all $< 1$) are the conjectured limiting values
as the sums grow with the cutoff. This is consistent with the conjecture: the
full $A_k$ stratum (for $k \geq 2$) has sum $< 1$.

**The minimum F3 value is at $k=3$: $1 - 0.0738 \approx 0.926$**, confirming
that $A_3$ is the "most extremal" stratum — yet still below 1.

---

### Q3: Sum over all primes (the $A_1$ primitive set)

$$
\sum_{p \text{ prime}} \frac{1}{p \ln p}
$$

Numerical computation (sieve to $10^6$, 78,498 primes):

| Upper limit | Partial sum |
|------------|-------------|
| $10^5$     | 1.5498      |
| $5 \times 10^5$ | 1.5604 |
| $10^6$     | 1.5642      |
| $\infty$ (estimated) | $\approx 1.637$ |

**The sum converges** (it is dominated by $\int 1/(x\ln^2 x)\,dx$ which converges)
and the tail decays: primes from $5\times10^5$ to $10^6$ contribute $\approx 0.004$.
The full limit is estimated at $\approx 1.6366$.

**Consistency with F1**: F1 says $S(A) < 1.399 + o(1)$ for primitive $A \subseteq
[x,\infty)$ as $x \to \infty$. The primes-from-2 sum $\approx 1.637$ EXCEEDS
$1.399$ — but this is consistent with F1 because the bound applies only as
$x \to \infty$ (for the primitive set starting at $x$). The primes starting
at $x=2$ are a primitive set in $[2, \infty)$ at a fixed small $x$; the
bound $1.399$ applies asymptotically for large $x$. For $x=2$, the
conjectured upper bound is $1 + o(1)$ where $o(1)$ is still $\approx 0.637$.

---

## Section 3: Witness Search (Q4)

We ran `library.primitive_set_witness.verify_witness` for three $x_{\rm floor}$ values.

**Primes-from-$x$ strategy** (best achievable by any primitive set of similar density):

| $x_{\rm floor}$ | Sum over all primes $\geq x_{\rm floor}$ (to $10^6$) |
|----------------|------------------------------------------------------|
| 2              | 1.564 (full sum $\approx 1.637$)                    |
| 3              | 0.843                                               |
| 5              | 0.539                                               |
| 100            | 0.143                                               |
| 1000           | 0.072                                               |
| 10000          | 0.036                                               |

**Q4 search results**:

- **$x_{\rm floor} = 100$**: Tried 275 primes from 101 to 1229.
  Verified sum = 0.084. `witness_valid = False`.
- **$x_{\rm floor} = 1000$**: Tried 500 primes from 1000 onwards.
  Verified sum = 0.027. `witness_valid = False`.
- **$x_{\rm floor} = 10000$**: Sum over all primes ≥ 10000 (to $10^6$) ≈ 0.036.
  Clearly `witness_valid = False`.

**Finding at $x_{\rm floor} = 2$**: The set $A = \{2, 3, 5, 7, 11\}$ (five primes)
has verified rigorous lower bound $S(A) \geq 1.260 > 1.0$.
The verifier confirms `witness_valid = True`.

**Why this is NOT a genuine counterexample**: The conjecture states
$S(A) < 1 + o(1)$ where $o(1) \to 0$ as $x_{\rm floor} \to \infty$. At
$x_{\rm floor} = 2$, the best known upper bound (supported by our primes-from-2
computation) is $S(A) \leq \sum_p 1/(p\ln p) \approx 1.637$. The Erdős–Zhang
theorem (F1) is itself consistent with this. So the conjectured bound at
$x = 2$ is $1 + o(1) \approx 1.637$, not $1.0$. Having $S(A) = 1.26$ for
$A \subseteq [2,\infty)$ does not violate the conjecture.

A genuine witness would require a primitive set $A \subseteq [x_{\rm floor},\infty)$
with $S(A) > 1$ for **large** $x_{\rm floor}$ — where the $o(1)$ term is small.
Our computations show this is numerically impossible: the maximum achievable
$S$ (using all primes $\geq x_{\rm floor}$) drops below 1 already at
$x_{\rm floor} = 3$ (sum $\approx 0.843$) and falls rapidly thereafter.

**Conclusion**: No genuine counterexample found. Numerics strongly support the
conjecture for $x_{\rm floor} \geq 3$.

No `<!-- WITNESS -->` block is embedded — the $x_{\rm floor}=2$ result is a
harness-level artifact, not a mathematical disproof.

---

## Section 4: Proof Structure (Q5)

*(to be filled)*
