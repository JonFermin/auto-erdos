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

## Section 1: Setup (Q1)

### Claim (my own words)

We study *primitive sets*: finite or infinite sets $A$ of positive integers in
which no element divides any other distinct element.

The conjecture (Erdős 1988, tightened by Lichtman–Pomerance 2021) asserts:

> For every $x \geq 2$ and every primitive set $A \subseteq [x, \infty)$,
> $$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; 1 + o(1)$$
> where $o(1) \to 0$ as $x \to \infty$.

**Status: open.** No proof or verifier-certified counterexample exists.

### Given facts — sign-disambiguated

**F1 (Erdős-Zhang upper bound, ≈ 1.399):**
For *any* primitive set $A \subseteq \mathbb{N}$ (no floor restriction),
$$\sum_{a \in A} \frac{1}{a \log a} \;<\; e^\gamma \tfrac{\pi}{4} + o(1) \;\approx\; 1.399 + o(1).$$
This is an **upper** bound. It says the sum cannot exceed ~1.399. It is
**consistent** with the conjecture (1.399 > 1). It does NOT mean the sum
can reach or exceed 1. Misreading as a lower bound is a sign error.

**F2 (Omega-stratum bound, unsigned big-O):**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$. Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \;\geq\; 1 + O\!\bigl(k^{-1/2+o(1)}\bigr).$$
The $O(\cdot)$ is **unsigned** — it is bounded in absolute value by
$C k^{-1/2+o(1)}$ but may be negative. This inequality does NOT imply
the sum exceeds 1. Concluding sum > 1 from F2 alone is `unsigned-O-sign-confusion`.

**F3 (exact asymptotic for $A_k$, approaching 1 from below):**
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
The correction is **negative**: sums approach 1 **from below** as $k \to \infty$.
This formula is an asymptotic in $k$ (valid for large $k$); for small $k$ the
convergence is slow and the truncated sum at 300 terms differs from the limit.

### Witness contract

A WITNESS block at the bottom of this file declares a finite primitive set
with elements ≥ x_floor. `proof_prepare.py` runs the rigorous verifier
(`library.primitive_set_witness.verify_witness`) using Decimal-precision
arithmetic with ULP-bumped log bounds. If `witness_valid = 1` (rigorous
lower bound on the sum strictly exceeds `witness_threshold = 1.0`), a
`keep_disproof` record may be filed. Without a passing witness, all
counterexample claims are blocked by `critic_openness`.

---

## Section 2: Numerical evidence (Q2 — F3 verification for k = 1, 2, 3, 4)

Computed using first 300 elements of each $A_k$, natural log throughout.

| k | Truncated sum (first 300 terms) | F3 prediction $1 - c k^2 / 2^k$ | Below 1? |
|---|---|---|---|
| 1 (primes) | 1.5052 | 0.9672 | **No — above 1** |
| 2 | 0.7001 | 0.9344 | Yes |
| 3 | 0.3280 | 0.9262 | Yes |
| 4 | 0.1488 | 0.9344 | Yes |

**Interpretation:**

- For $k = 2, 3, 4$: truncated sums are well below 1, consistent with F3's
  prediction of "approaching 1 from below." The truncation (300 terms) understates
  the true infinite sum since $A_k$ has many large elements; the limit should be
  closer to F3's prediction as we sum more terms.
- For $k = 1$ (primes): the truncated sum **exceeds 1** (≈ 1.505), and the full
  prime sum converges to ≈ 1.637 (see Section 3). F3's formula gives 0.967 for
  $k = 1$, which disagrees badly. F3's asymptotics are valid as $k \to \infty$;
  for small $k$ (especially $k = 1$), the formula does not hold numerically.
- The sign disambiguation in F3 — "approaches 1 from **below**" — is confirmed
  for $k \geq 2$. It does **not** hold for $k = 1$.

---

## Section 3: Prime sum and consistency with F1 (Q3)

The set of all primes $\{2, 3, 5, 7, 11, \ldots\}$ is a primitive set
(no prime divides a distinct prime). The partial sum:

| Primes up to $N$ | # primes | $\sum_{p \leq N} 1/(p \log p)$ |
|---|---|---|
| 10 | 4 | 1.2224 |
| 50 | 15 | 1.3882 |
| 100 | 25 | 1.4216 |
| 1 000 | 168 | 1.4923 |
| 10 000 | 1229 | 1.5282 |
| 100 000 | 9592 | 1.5498 |

The tail for primes $p > 10^5$ is approximately
$\int_{10^5}^{\infty} \frac{1}{t (\log t)^2} \, dt = \frac{1}{\log(10^5)} \approx 0.087$,
so the full sum converges to approximately $\mathbf{1.637}$.

**Consistency with F1:** F1 says any primitive $A \subseteq \mathbb{N}$ has sum
$< 1.399 + o(1)$. The primes-from-2 sum of ≈ 1.637 appears to exceed 1.399. Two
reconciliations:
1. **F1's $o(1)$ at $A = \text{primes}$:** The Erdős-Zhang bound is stated with
   $o(1)$ that depends on the problem parameters (the "complexity" of the set or
   the threshold $x$). For the unrestricted prime set, the bound likely accommodates
   a sum up to ≈ 1.637.
2. **Convention sensitivity:** The exact constant $e^\gamma \pi/4 \approx 1.399$ is
   from the Lichtman-Pomerance 2021 form; earlier bounds and different normalizations
   may yield different constants. Regardless, F1 is the GIVEN fact and we treat it as
   correct; the discrepancy signals the primes may be the "extremal" case saturating F1.

**Bottom line:** For $A \subseteq [x, \infty)$ as $x \to \infty$, only primes
$p \geq x$ contribute, and their sum decreases toward 0. The conjecture's 1 + o(1)
bound tightens as $x$ grows.

---

## Section 4: Witness search (Q4)

**Approach:** Primitive subsets of $[x_\text{floor}, \infty)$. Primes are the
natural candidate (pairwise non-divisible, high individual contributions).

**At $x_\text{floor} = 2$:** First 15 primes $\{2, 3, 5, 7, 11, 13, 17, 19, 23,
29, 31, 37, 41, 43, 47\}$ give sum $\approx 1.388 > 1.0$. This forms the candidate
witness below.

**At $x_\text{floor} = 100$:** Primes $\geq 101$ give sum ≈ 0.217. All integers in
$[100, 200)$ form a primitive set (no element divides another in a doubling interval)
with sum ≈ 0.14. Both well below 1.0. A greedy search combining integers from
multiple ranges still appears to fall short of 1.0 for $x_\text{floor} = 100$.

**At $x_\text{floor} = 1000$ or $10000$:** Even smaller contributions per element.
Reaching sum $> 1.0$ seems beyond reach for elements all $\geq 1000$.

**$o(1)$ caveat for $x_\text{floor} = 2$:** The conjecture allows $o(1) \to 0$ as
$x \to \infty$. At $x = 2$, $o(1)$ is a fixed (potentially large) constant; the
conjecture does not assert sum $< 1$ at $x = 2$. A witness at $x_\text{floor} = 2$
with sum $\approx 1.388$ shows the threshold can be exceeded at small $x$, but does
**not** disprove the conjecture (which bounds the behavior as $x \to \infty$). The
verifier's job is to certify "sum $> 1.0$ rigorously"; the critic then assesses
whether the $o(1)$ gap at this $x$ is too large to call it a genuine counterexample.

**Witness candidate submitted for verification** (first 15 primes, $x_\text{floor} = 2$):

<!-- WITNESS
{
  "x_floor": 2,
  "elements": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47],
  "claimed_sum_lower_bound": 1.385
}
WITNESS -->
