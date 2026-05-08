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
  Phrases like "the conjecture is false" / "we disprove" trigger
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

---

## Section 1: Setup — Claim, Facts, and Witness Contract (Q1)

### The Conjecture (in my own words)

Erdős's primitive-set conjecture says: if you take any set $A$ of positive
integers in which no element divides another (a "primitive set"), and you
restrict $A$ to integers $\geq x$, then the weighted sum

$$S(A) = \sum_{a \in A} \frac{1}{a \log a}$$

satisfies $S(A) < 1 + o(1)$, where the $o(1)$ term vanishes as
$x \to \infty$. Equivalently, for any $\varepsilon > 0$ there exists
$X(\varepsilon)$ such that for all primitive $A \subset [x, \infty)$ with
$x \geq X(\varepsilon)$ we have $S(A) < 1 + \varepsilon$.

The conjecture is **open**.

### The Three Given Facts (with sign disambiguations)

**F1 (Erdős-Zhang upper bound, citation: Erdős 1935 / Zhang 1993).**
For *any* primitive set $A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
Sign: **UPPER bound**. The sum is *strictly less than* $\approx 1.399$.
Consistent with the conjecture. Does NOT imply a lower bound of 1.399.
Misreading F1 as a lower bound is a sign error.

**F2 (Omega-stratum lower bound, unsigned big-O; id: F2_omega_k_lower_unsigned).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$. Then:
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$
Sign: The $O(k^{-1/2+o(1)})$ term is **unsigned** — it could be positive or
negative, with absolute value bounded by $k^{-1/2+o(1)}$. This says the sum
is at least $1 - C k^{-1/2+o(1)}$ for some $C > 0$, converging to 1 from
below. Concluding $S(A_k) > 1$ from F2 alone is a **SIGN ERROR** (BLOCKING).

**F3 (Omega-stratum exact asymptotic, correction is negative; id: F3_omega_k_exact_below_one).**
For the same $A_k$:
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
Sign: correction is $-(c+o(1)) k^2/2^k$ with $c > 0$, so the sum is
**strictly less than 1** for every $k \geq 1$, approaching 1 from **BELOW**.
F3 is **consistent with and supportive of** the conjecture. It also reconciles
with F2: F2's unsigned-O correction is in fact negative, as F3 shows.

### Witness Contract

To claim disproof I need a finite primitive set $A \subset [x_\text{floor}, \infty)$
with `library.primitive_set_witness.verify_witness` confirming $S(A) > 1.0$.
The `<!-- WITNESS -->` block (appended at the bottom of this file) must carry:
- `x_floor` (int ≥ 2): every element $\geq x_\text{floor}$.
- `elements`: list of integers, pairwise non-divisible, each $\geq x_\text{floor}$.
- `claimed_sum_lower_bound`: my estimate (verifier recomputes independently).

Without `witness_valid = 1`, no disproof claim is permitted.

### Proof Directions

Three paths:

1. **Prove the conjecture** — show $S(A) < 1 + o(1)$ universally. Needs a
   tighter argument than Erdős-Zhang. One natural approach: stratify $A$ by
   $\Omega(a) = k$, bound each stratum's contribution using F3-style estimates,
   and sum across strata.

2. **Find a counterexample** — exhibit $A \subset [x_\text{floor}, \infty)$
   with $S(A) > 1$. Since F3 shows $A_k$ satisfies $S(A_k) < 1$, any
   counterexample would be a "mixed-stratum" set. Q4 searches for one.

3. **Partial result** — rule out large classes of counterexamples, or tighten
   the known upper bound below 1.399 toward 1.

## Section 2: Numerical Evidence (Q2 — in progress)

*To be filled in by Q2 round.*

## Section 3: Primes-from-2 Consistency (Q3 — pending)*

*To be filled in by Q3 round.*

## Section 4: Witness Search Results (Q4 — pending)*

*To be filled in by Q4 round.*

## Section 5: Proof Outline (Q5 — pending)*

*To be filled in by Q5 round.*
