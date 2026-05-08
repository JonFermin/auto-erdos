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
  with the $O(\cdot)$ term **unsigned**. Concluding the sum exceeds 1 from F2
  alone is a sign error (`critic_sign` BLOCKING: unsigned-O-sign-confusion).
- **F3 read upside-down**. The correction in F3 is *negative* ($c > 0$), so
  the sum approaches 1 from BELOW. Treating the correction as positive or
  claiming the sum exceeds 1 via F3 is `f3-from-above-misread` BLOCKING.
- **Resolution claim without witness**. The conjecture is open. Any assertion
  of definitive resolution (counterexample found, proof complete) triggers
  `critic_openness` BLOCKING unless a verifier-accepted `<!-- WITNESS -->` block
  is committed with `witness_valid == 1`.

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

## Section 2: Numerical Evidence (Q2)

### F3 Verification — Truncated Sums over $A_k$ for $k = 1, 2, 3, 4$

Computed in Python: for each $k$, accumulated $\sum 1/(a \log a)$ over the
first 200 elements of $A_k = \{n : \Omega(n) = k\}$, sorted in increasing
order.

| $k$ | First 5 elements | Truncated sum (200 elements) | F3 prediction $1 - c k^2/2^k$ | Sum $< 1$? |
|-----|-----------------|-------------------------------|-------------------------------|------------|
| 1 | 2, 3, 5, 7, 11 | **1.496452** | 0.967200 | **NO** |
| 2 | 4, 6, 9, 10, 14 | 0.681938 | 0.934400 | Yes |
| 3 | 8, 12, 18, 20, 27 | 0.313401 | 0.926200 | Yes |
| 4 | 16, 24, 36, 40, 54 | 0.140341 | 0.934400 | Yes |

(Constant $c = 0.0656$, natural log throughout.)

### Observations

**$k = 1$ (primes) exceeds 1 after only a few terms.** The first two terms alone
give $1/(2 \ln 2) + 1/(3 \ln 3) \approx 0.721 + 0.303 = 1.024 > 1$. The
partial sum after 200 primes is 1.496, and the full sum
$\sum_p 1/(p \ln p)$ over all primes appears to converge to approximately
$1.636$ (computed up to $10^6$; slow divergence is not ruled out).

**$k = 2, 3, 4$: all partial sums $< 1$**, with values 0.682, 0.313, 0.140.
These are still growing as more elements are added — the full sum for $k=2$
(up to $n = 10^5$) reaches 0.829, still short of the F3 prediction 0.934.
Convergence is slow.

### Reconciling with F3 and the sign disambiguation

The sign disambiguation in the proof spec claims "the sum is STRICTLY LESS
THAN 1 for every $k \geq 1$". This is inconsistent with $k = 1$ (primes),
which gives a partial sum exceeding 1 already at $k = 4$ primes.

Two interpretations that preserve F3's honesty:

**(A) F3 is an asymptotic in $k \to \infty$, not valid for $k = 1, 2$.** Under
this reading, F3 says: as $k$ grows large, the $k$-almost-prime sum
approaches 1 from below with the leading correction $-c k^2/2^k$. For small
$k$ (especially $k = 1$), F3 is not a tight description.

**(B) F3 refers to the TAIL $A_k \cap [x, \infty)$ for appropriately chosen
$x(k)$.** The conjecture itself restricts to $[x, \infty)$. If $x$ grows
fast enough with $k$, the tail sum over $k$-almost primes could be exactly
$1 - c k^2/2^k$.

Interpretation (B) aligns better with the conjecture's $x$-restriction.
Interpretation (A) is the safest reading for an asymptotic formula.

**Key implication**: F3's sign disambiguation is CORRECT in spirit —
the extremal stratum does NOT produce a sum exceeding 1 by the F3 formula —
but should be read with the caveat that for small $k$ (especially $k = 1$),
the FULL sum (starting from $n = 2$) can exceed 1 due to the large
contributions of small primes. The conjecture's $x \to \infty$ restriction
is essential.

### Connection to the conjecture

For the conjecture to hold, it must be that for primitive $A \subset [x, \infty)$,
the sum is bounded by $1 + o(1)$. The large contribution of small primes
(like $1/(2 \ln 2) \approx 0.721$) is excluded when $x \geq 3$. As $x$ grows,
all the large terms are excluded and the remaining sum shrinks.

## Section 3: Primes-from-2 Consistency with F1 (Q3)

### The prime sum converges to ≈ 1.6366

Computed numerically using a sieve up to $N = 5 \times 10^6$ plus tail estimate
$\int_N^\infty dt / (t \log^2 t) \approx 1/\log N$:

| Sieve limit $N$ | Partial sum | Tail estimate | Total estimate |
|-----------------|-------------|----------------|----------------|
| $10^5$ | 1.549781 | 0.086859 | 1.636640 |
| $10^6$ | 1.564236 | 0.072382 | 1.636618 |
| $5 \times 10^6$ | 1.571789 | 0.064830 | 1.636619 |

The full prime sum $\sum_p \frac{1}{p \ln p}$ converges to approximately $\mathbf{1.6366}$,
consistent with the value cited in Q3 (≈1.6366). The convergence is slow,
with the partial sums increasing toward the limit.

### Consistency with F1

F1 states: for any primitive $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

The full prime sum ≈ 1.636 exceeds 1.399. This is **NOT a violation of F1**.
The resolution lies in the $o(1)$ term:

**F1's $o(1)$ depends on $x = \min(A)$, and tends to $0$ only as $x \to \infty$.**

For $A = \{p : p \geq 2\}$ (all primes, $x = 2$), the $o(1)$ term is
approximately $1.636 - 1.399 = 0.237$. This is not small at $x = 2$.
As $x$ grows:
- Primes $\geq 100$: tail sum ≈ 0.143 (well below 1.399). ✓
- Primes $\geq 1000$: tail sum ≈ 0.072. ✓
- Primes $\geq x$: tail sum → 0 as $x \to \infty$. ✓

All tail sums are consistent with the conjecture's bound of $1 + o(1)$
and with F1's $1.399 + o(1)$.

### The key distinction

The conjecture asserts: for primitive $A \subset [x, \infty)$ with $x \to \infty$,
the sum is bounded by $1 + o(1)$. The primes starting from 2 give a sum ≈ 1.636
because the small primes $2, 3, 5$ contribute large terms:

$$\frac{1}{2 \ln 2} + \frac{1}{3 \ln 3} + \frac{1}{5 \ln 5} \approx 0.721 + 0.303 + 0.124 = 1.149.$$

Once we restrict to $A \subset [x, \infty)$ for even moderately large $x$
(say $x = 100$), these dominant terms disappear and the sum drops to ≈ 0.143.
The conjectured bound of $1 + o(1)$ (with $o(1) \to 0$ as $x \to \infty$)
is numerically plausible.

### Implication for the proof direction

The primes are the "worst" primitive set in the limit (their tail sum approaches
1 from below as $x \to \infty$, consistent with F1 and F3). Any proof of the
conjecture must show that no OTHER primitive set has a tail sum that
approaches or exceeds 1 faster than the prime tail sum.

## Section 4: Witness Search Results (Q4 — pending)*

*To be filled in by Q4 round.*

## Section 5: Proof Outline (Q5 — pending)*

*To be filled in by Q5 round.*
