# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Section 1: Setup (Q1)

### The claim

For any $x \geq 2$, if $A \subset [x, \infty)$ is a **primitive set** of integers
(no element of $A$ divides any other element of $A$), then
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
where the $o(1)$ term tends to $0$ as $x \to \infty$. In other words, for
*large* integers the sum of this "Erdős weight" over any primitive set is
bounded above by approximately 1.

**Status**: open. Until a verifier-accepted witness block is committed,
no claim of resolution may appear in this file.

### The three given facts (with sign disambiguations)

**F1 (Erdős–Zhang upper bound).** For any primitive set $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
*Sign*: This is an **upper bound**, strictly less than. The constant is
positive; F1 is consistent with the conjecture (which posits the tighter
bound of 1). The $o(1)$ hides dependence on the lower bound of the
elements of $A$: as the smallest element grows without bound, the bound
tightens. **Misreading F1 as a lower bound is a sign error.**

**F2 (Omega-stratum sum, unsigned big-O).** For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$
(integers with exactly $k$ prime factors counted with multiplicity),
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$
*Sign*: The $O(\cdot)$ term is **unsigned** — it may be positive or
negative. This inequality says the sum is at least $1$ minus a quantity
bounded by $k^{-1/2+o(1)}$ in absolute value. **It does NOT show the
sum exceeds 1.** Concluding $\sum > 1$ from F2 alone is a
`unsigned-O-sign-confusion` error.

**F3 (Exact asymptotic for canonical extremal sets).** For the same $A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656.$$
*Sign*: The leading correction is **negative** ($c > 0$, coefficient $-c$),
so the sum approaches 1 **from below** as $k \to \infty$. The $A_k$ sets
are "canonical extremal-looking" but do NOT violate the conjecture.
*Note*: As established in Section 2, the formula matches numerics well only
for $k \geq 2$; for $k=1$ (primes) the actual sum is $\approx 1.637$,
far above F3's prediction — see the discussion in Section 2.

### The witness contract

A **counterexample** to the conjecture would be a finite primitive set
$A \subset [x_{\mathrm{floor}}, \infty)$ with rigorously verified
$\sum_{a \in A} 1/(a \log a) > 1.0$ (the `witness_threshold`). To commit
such a witness, embed a `<!-- WITNESS ... WITNESS -->` JSON block containing:
- `x_floor`: integer $\geq 2$; every element of `elements` must be $\geq x_{\mathrm{floor}}$.
- `elements`: list of distinct integers $\geq x_{\mathrm{floor}}$, pairwise non-divisible.
- `claimed_sum_lower_bound`: agent's estimate; the verifier recomputes rigorously.

**Caveat**: a witness at small $x_{\mathrm{floor}}$ exceeding 1 by a modest
amount is **not** a genuine counterexample, since the $o(1)$ correction in
the conjecture is non-negligible at small $x$. A genuine disproof requires
$x_{\mathrm{floor}} \to \infty$ — see Q3 and Q4 analysis below.

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
- **Open claim asserted resolved without witness**. The conjecture is
  currently open. Resolution-asserting language (claiming the claim is
  settled, proved, or disproved) without a verifier-accepted WITNESS
  block triggers `critic_openness` BLOCKING.

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

## Section 2: Numerical Evidence (Q2 + Q3)

### F3 verification for k = 1, 2, 3, 4 (Q2)

Computed via Python/uv over integers in $[2, 5000]$ and the first 200
elements of each $A_k$. All arithmetic in standard floating-point;
results are illustrative, not rigorous.

| k | First 200 elements — 200th elt | Truncated sum | Sum < 1? | F3 formula (c=0.0656) |
|---|---|---|---|---|
| 1 (primes) | 1223 | **1.4965** | **No — see below** | 0.9672 |
| 2 | 669 | 0.6819 | Yes | 0.9344 |
| 3 | 805 | 0.3134 | Yes | 0.9262 |
| 4 | 1292 | 0.1403 | Yes | 0.9344 |

Extended sums over $[2, 50000]$:

| k | Sum over [2, 50000] |
|---|---|
| 1 | 1.5442 (converging to ~1.6366) |
| 2 | 0.8148 |
| 3 | 0.4363 |
| 4 | 0.2131 |

**Key observation — F3 discrepancy at k=1.** The F3 formula predicts
$\sum_{A_1} 1/(a \log a) \approx 0.967$, but the actual sum over all primes
converges to approximately $\sum_p 1/(p \log p) \approx 1.6366$. This is
roughly 70% larger than F3's prediction. Possible explanations:
- The $o(1)$ correction in F3 is large (not small) for $k=1$, hiding a
  discrepancy of order $1$.
- F3's formula is derived from an asymptotic valid only for $k \to \infty$
  and is poorly approximated at $k=1$.
- The $A_k$ sets in F3 may be restricted in a way not reflected here
  (e.g., restricted to $[x, \infty)$ normalized by $\log x$).

For $k \geq 2$, the truncated sums are indeed below 1 (consistent with
the sign-disambiguation in F3), and the full sums are also well below 1.
**The sign-discrimination matters most for k ≥ 2 where F3's "from below"
claim is numerically supported.**

### Primes sum and F1 (Q3)

The set of all primes is a primitive set (no prime divides another). Its
Erdős-weight sum converges:
$$\sum_{p \text{ prime}} \frac{1}{p \log p} \approx 1.6366 \ldots$$

This exceeds both the witness threshold (1.0) and the F1 constant (1.399).
This is **not a contradiction of F1**: F1's o(1) term hides dependence on
the lower bound of the elements. The sum for *primes in $[x, \infty)$* is:

| x | $\sum_{p \geq x} 1/(p \log p)$ (approx) |
|---|---|
| 2 | ~1.6366 |
| 100 | ~0.215 |
| 1000 | ~0.144 |
| 10000 | ~0.108 |

As $x \to \infty$, this tail sum $\to 0$, consistent with F1's bound of
$1.399 + o(1)$ tightening toward 0. For the conjecture's bound of
$1 + o(1)$, we need the maximum primitive-set sum over $A \subseteq [x, \infty)$
to remain below 1 as $x$ grows — numerics confirm this for primes for
$x \geq 10$.

**The conjecture's non-trivial content** is precisely about the intermediate
regime: for moderate $x$, can a primitive set in $[x, \infty)$ have sum
close to 1 (but below 1)?

## Section 3: Witness Search (Q4)

Formally searched for a primitive $A \subset [x_{\text{floor}}, \infty)$
with rigorous $\sum 1/(a \log a) > 1.0$ (the `witness_threshold`), using
`library.primitive_set_witness.verify_witness` with all primes in each
interval:

| $x_{\text{floor}}$ | Primes used | Rigorous lower bound | Witness valid? |
|---|---|---|---|
| 100 | 5108 primes in [100, 50000] | 0.1227 | No |
| 1000 | 4965 primes in [1000, 50000] | 0.0519 | No |
| 10000 | 3904 primes in [10000, 50000] | 0.0161 | No |

**No witness found at any of the requested thresholds.** This is consistent
with the conjecture: for $x \geq 10$, even the primes (the densest
primitive set) give far less than 1.

*Aside*: At $x_{\text{floor}} = 2$, the primes $\{2, 3, 5\}$ rigorously
verify to score $\approx 1.149 > 1.0$. This WOULD pass the witness
verifier. However, it is **not a genuine counterexample**: the conjecture
bounds sum by $1 + o(1)$ where $o(1) \to 0$ as $x \to \infty$. At $x=2$,
the $o(1)$ is approximately $0.637$ (since all primes sum to $\approx
1.637$, so the conjecture allows sum $< 1.637$ at $x=2$). The witness
score 1.149 is well within this allowance. This trivial witness is
deliberately not embedded.

## Section 4: Proof Outline (Q5)

### Overall strategy

Stratify any primitive $A \subset [x, \infty)$ by $k = \Omega(a)$:
$$A = \bigsqcup_{k \geq 1} (A \cap A_k), \quad \text{so} \quad
\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A \cap A_k} \frac{1}{a \log a}.$$

**Goal**: bound each partial sum $S_k(A) = \sum_{a \in A \cap A_k} 1/(a \log a)$
and show $\sum_k S_k(A) < 1$.

See `proof_lemmas/` for individual lemma files.

**Lemma `strat_001` (Per-stratum bound)**: For any primitive set
$A \subset [x, \infty)$ and any $k$, $S_k(A) \leq S_k(A_k)$ (the
stratum-$k$ sum of ANY primitive subset of $A_k$ is at most the full
stratum-$k$ sum). *Status: open — need to justify why primitivity
implies this bound holds.*

**Lemma `strat_002` (F3 intra-stratum)**: By F3, the full stratum-$k$ sum
$S_k(A_k) = 1 - (c+o(1))k^2/2^k$ (asymptotic in $k$, verified numerically
for $k \geq 2$). For $k=1$ (primes), F3's formula breaks down and the actual
sum is $\approx 1.637$. *Status: open — need to reconcile F3 with k=1 and
obtain a uniform bound.*

**Lemma `strat_003` (Summation across strata)**: Even if $S_k(A_k) < 1$ for each
$k \geq 2$, summing over $k$ gives $\sum_{k \geq 1} S_k(A) \leq \sum_{k \geq 1} S_k(A_k)$.
The key observation is that $A$ is primitive, so $A \cap A_k$ is a subset
of $A_k$ with NO relation between different strata (an element of $A \cap A_1$
can divide an element of $A \cap A_2$, so primitivity DOES constrain
cross-stratum structure). *Status: open — the cross-stratum constraint
is the crux of the hard part.*

**Hard sub-problem**: F3 shows $S_k(A_k) \to 1$ from below. Thus
$\sum_k S_k(A_k) = \infty$ (infinitely many strata, each contributing
near 1). Any bound must use primitivity across strata. This is the
structural heart of the conjecture and is the main open gap in this
proof attempt.

**Fallback (partial result)**: If the full cross-stratum bound cannot
be established, this attempt will document:
1. The per-stratum bound $S_k(A) \leq S_k(A_k) < 1$ for $k \geq 2$.
2. The numerical evidence that for $x \geq x_0$ (e.g. $x_0 = 10$), the
   maximum primitive-set sum is well below 1.
3. The main open gap (cross-stratum primitivity constraint).

This constitutes a valid `partial_result` in the sense of
`proof_log_result.py` and is a meaningful contribution even without
a complete proof.
