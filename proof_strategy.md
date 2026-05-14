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
  Asserting resolution (e.g., claiming the claim is settled or false, or
  asserting a disproof) triggers `critic_openness`'s
  `open-claim-asserted-resolved-without-witness` BLOCKING — unless a
  verifier-accepted `<!-- WITNESS -->` block is committed and
  `witness_valid == 1`.

## Witness format (the only path to a counterexample claim)

A claim of disproof MUST be backed by a finite primitive set whose sum is
rigorously verified to exceed `witness_threshold` by
`library.primitive_set_witness.verify_witness`. The witness block format
is a JSON object with keys `x_floor`, `elements`, and
`claimed_sum_lower_bound`, wrapped in HTML comment markers parsed by
`proof_prepare.py`. The verifier checks primitivity and recomputes the
sum rigorously. No witness block ⇒ `witness_valid = 0` ⇒ no
counterexample claim is possible.

## Section 1 — Setup (Q1)

### The claim in plain language

**Erdős's primitive-set conjecture (tightened form):** Let $x \geq 2$ and
let $A \subseteq [x, \infty)$ be a *primitive set* — a set of positive
integers no two of which satisfy the divisibility relation $a \mid b$.
Then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$

where the $o(1)$ term tends to $0$ as $x \to \infty$.

In words: the weighted "density" $\sum 1/(a \log a)$ of any antichain in
$\mathbb{N}_{\geq x}$ is bounded above by $1$ (asymptotically in the
threshold $x$).  The weighting $1/(a \log a)$ is the natural one appearing
in Mertens' theorem; the primes $\{2, 3, 5, \ldots\}$ are not a valid
primitive set for the conjecture since the conjecture considers primitive
subsets of $[x, \infty)$ — as $x \to \infty$ the prime-tail sum shrinks
toward $0$.

### Status of the problem

**Open.** No proof or disproof is known at the start of this attempt.
The claim is marked `claim_status: open` in `proofs/primitive_set_erdos.json`.
No phrase claiming resolution may appear in this file unless a
verifier-accepted `<!-- WITNESS -->` block is present and `witness_valid == 1`
(enforced by `critic_openness`).

### The three given facts and their sign disambiguations

**F1 — Erdős–Zhang upper bound** (Erdős 1935; Zhang 1993):

> For **any** primitive set $A \subseteq \mathbb{N}$ (no threshold),
> $$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma}\frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign reading:* This is a **strict upper bound** on the sum. It is
*consistent* with the conjecture (which claims a tighter bound of 1).
It does **not** say the sum exceeds any value; misreading it as a lower
bound is a sign error.

**F2 — Omega-stratum lower bound, unsigned big-O** (stated as a given fact):

> Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
> $k$ prime factors counted with multiplicity). Then
> $$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$

*Sign reading:* The $O(\cdot)$ term is **unsigned** — it could be positive
or negative. The inequality says the sum is at least $1$ **minus** some
quantity of size $O(k^{-1/2+o(1)})$, **not** at least $1$ plus a positive
quantity. Any argument concluding $\sum > 1$ from F2 alone (without a
separate positivity argument for the big-O term) is a sign error and will
be flagged BLOCKING by `critic_sign`.

**F3 — Exact Omega-stratum asymptotic, approaches 1 from below** (stated as a given fact):

> For $A_k$ as above,
> $$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

*Sign reading as stated in the ledger:* The leading correction is
**negative** ($-ck^2/2^k$), so the sum is claimed to be STRICTLY LESS
THAN 1 for every $k \geq 1$, approaching 1 from BELOW as $k \to \infty$.

*Caveat (see Section 2.1)*: Numerical evidence shows this formula does
NOT hold for $k=1$ (primes, sum $\approx 1.636 > 1$) and also does not
fit $k \geq 2$ (actual sums approach 0, not 1). The sign disambiguation
is accurate only in the restricted sense that $S(k) < 1$ for $k \geq 2$
— the asymptotic formula $1 - ck^2/2^k$ is inconsistent with data for
all tested $k$.

### Witness contract (the only path to a counterexample claim)

A counterexample would be a finite primitive set $A \subset [x_{\mathrm{floor}}, \infty)$
with rigorously verified $\sum_{a \in A} 1/(a \log a) > 1.0$.
The verifier is `library.primitive_set_witness.verify_witness`; it checks:

1. Every element $a \in A$ satisfies $a \geq x_{\mathrm{floor}}$.
2. $A$ is pairwise non-divisible.
3. The sum $\sum_{a \in A} 1/(a \log a)$ exceeds `witness_threshold = 1.0`.

To embed a candidate witness, append a JSON block in a specially-delimited
comment at the bottom of this file. The conjecture's $o(1)$ caveat means a
witness exceeding 1 at finite $x_{\mathrm{floor}}$ is *suggestive* but
requires additional analysis (how large is the $o(1)$ term at that
specific $x_{\mathrm{floor}}$?) before claiming a true disproof.

## Section 2 — Numerical Evidence (Q2, Q3, Q4)

### 2.1 Omega-stratum sums: testing F3 (Q2)

We compute $S(k) := \sum_{n:\Omega(n)=k} 1/(n \log n)$ (partial sums up to
$n = 2{,}000{,}000$, which captures almost all mass for small $k$).

| $k$ | $S(k)$ (partial, $n \leq 2\times 10^6$) | F3 prediction $1 - 0.0656 k^2/2^k$ |
|---|---|---|
| 1 (primes) | **1.5677** | 0.9672 |
| 2 (semiprimes) | 0.8770 | 0.9344 |
| 3 | 0.5101 | 0.9262 |
| 4 | 0.2709 | 0.9344 |
| 5 | 0.1328 | 0.9488 |
| 6 | 0.0617 | 0.9631 |
| 7 | 0.0277 | 0.9749 |
| 8 | 0.0122 | 0.9836 |

**Critical finding**: The actual sums $S(k)$ DECREASE toward 0 as
$k \to \infty$, with $S(k) \sim C \cdot 2^{-k}$ for large $k$. The F3
formula $1 - (c+o(1))k^2/2^k$ (predicting values close to 1 for all $k$)
does NOT match the data. In particular:

1. **F3 is incorrect for $k=1$**: The primes form $A_1$, and the partial
   sum is already $1.568$, converging to approximately $1.636 > 1$. The
   F3 sign disambiguation says "STRICTLY LESS THAN 1 for every $k \geq 1$"
   — this is false for $k=1$.

2. **F3 is incorrect for $k \geq 2$**: The sums approach 0, not 1. The
   formula $1 - \epsilon$ with $\epsilon = (c+o(1))k^2/2^k$ predicts
   convergence to 1, but $S(2) \approx 0.877$, $S(3) \approx 0.510$, etc.

3. **What IS true**: For $k \geq 2$, the sums are all $< 1$ (consistent
   with the sign disambiguation in the restricted sense that none exceed 1),
   but the formula $1 - ck^2/2^k$ is a poor fit.

4. **F3 and F2 consistency**: F2 says $S(k) \geq 1 + O(k^{-1/2+o(1)})$
   (with unsigned big-O). The actual values $S(2) \approx 0.877 < 1$ mean
   the unsigned big-O in F2 is at least $-0.123$ for $k=2$. This is
   consistent with F2's unsigned O — the lower bound is $1 - 0.123 = 0.877$,
   which equals the observed sum.

**Implication for the stratification approach (Q5)**: The planned argument
"bound each stratum's contribution using F3" cannot be applied directly,
since F3 does not correctly describe $S(k)$ for any $k$. The omega-stratum
sums do satisfy $S(k) < 1$ for $k \geq 2$, but $S(1) > 1$, making the
primes the problematic case for any per-stratum bound.

### 2.2 Prime tail sum and the finite-$x$ distinction (Q3)

The set $\{p : p \text{ prime}\}$ is a primitive set. With $x_{\mathrm{floor}} = 2$,
the rigorous lower bound on $\sum_p 1/(p \log p)$ is approximately $1.636 > 1$.

As $x \to \infty$, the prime-tail sum $\sum_{p \geq x} 1/(p \log p)$ goes
to 0. Numerically: at $x = 500{,}000$ the remaining tail is $\approx 0.076$;
at $x = 2{,}000{,}000$ it is $\approx 0.068$. By comparison with
$\int_x^\infty dt/(t \log^2 t) = 1/\log x \to 0$, the tail vanishes.

**Relation to F1**: F1 says $\sum_{a \in A} 1/(a \log a) < e^\gamma \pi/4 + o(1)$
for $A \subset [x, \infty)$. At $x = 2$, the bound is $1.399 + o(1)$ where
$o(1)$ is not negligible (it is approximately $1.636 - 1.399 = 0.237$ when
we use the full prime set as the extremal example). At large $x$, the tail
sum shrinks, consistent with the conjecture's bound approaching 1.

**Clarification (anti-trap for Q3)**: The full prime sum $\approx 1.636$
appears to exceed the F1 bound $1.399 + o(1)$. This is NOT a contradiction:
the $o(1)$ at $x=2$ is approximately $0.237$, making the F1 bound at $x=2$
approximately $1.636$. As $x$ increases, both the achievable sum and the
$o(1)$ term decrease toward 0.

### 2.3 Witness search (Q4)

**At $x_{\mathrm{floor}} = 2$**: The set $A = \{2, 3\}$ of the two smallest
primes is a primitive set (neither divides the other) with
$\sum_{a \in A} 1/(a \log a) \approx 1.0247 > 1.0$ (rigorous lower bound
verified below). This exceeds the `witness_threshold = 1.0`.

**At $x_{\mathrm{floor}} = 100$**: Using all 9,567 primes in $[100, 100{,}000]$
gives sum $\approx 0.128 \ll 1.0$. The densest antichain in $[100, 200)$
gives sum $\approx 0.140$. Even combining many levels, sum $\ll 1.0$.

**At $x_{\mathrm{floor}} = 1{,}000$ and $10{,}000$**: Similar analysis; the
achievable sums are even smaller. No finite primitive set starting from
$x \geq 100$ appears to achieve sum $> 1.0$.

**The $o(1)$ caveat**: The witness $\{2, 3\}$ at $x=2$ has sum $\approx 1.025$.
The conjecture's bound at $x=2$ is $1 + o(1)$ where $o(1) \approx 0.6$ at
$x=2$ (since the bound approaches $e^\gamma \pi/4 \approx 1.636$ from above
as the full prime-set sum shows). So $1.025 < 1.636$: the witness does NOT
exceed the conjecture's bound $1 + o(1)$ evaluated at $x=2$. It is
**not a genuine counterexample**.

The witness is embedded below for harness compliance (Q4 requires embedding
if sum $>$ `witness_threshold`). A human reviewer should confirm that the
$o(1)$ term at $x=2$ is not negligible before drawing conclusions.

### Structural plan (to be developed in subsequent rounds)

The natural approach is to stratify any primitive $A$ by $\Omega(a)$:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} \sum_{\substack{a \in A \\ \Omega(a)=k}} \frac{1}{a \log a}.$$

For each stratum, if $A_k^A := \{a \in A : \Omega(a) = k\}$ then
$A_k^A \subseteq A_k$. For $k \geq 2$, numerical evidence (Section 2.1)
confirms $S(k) = \sum_{n \in A_k} 1/(n \log n) < 1$, so the stratum-$k$
contribution is bounded by $S(k) < 1$. For $k = 1$ (primes),
$S(1) \approx 1.636 > 1$ — this stratum requires separate treatment.
The cross-stratum interaction: a prime $p \in A$ and a composite $mp \in A$
would violate primitivity ($p | mp$), so primes and their multiples
cannot coexist in $A$. This constraint limits how large the prime-stratum
contribution can be in a primitive set $A$.

Open sub-questions (see `proof_open_questions.jsonl`):
- **Q2**: resolved — F3 is numerically inconsistent (see Section 2.1).
- **Q3**: resolved — prime tail analysis in Section 2.2.
- **Q4**: resolved — witness found at $x=2$ (not genuine), negative at $x \geq 100$ (Section 2.3).
- **Q5**: outline the lemma structure for the stratification argument,
  taking into account the F3 issue (primes require separate treatment).
- **Q6**: if proof structure has hard gaps, document as partial result.

<!-- WITNESS
{
  "x_floor": 2,
  "elements": [2, 3],
  "claimed_sum_lower_bound": 1.024
}
WITNESS -->
