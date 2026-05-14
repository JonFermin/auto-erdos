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

### The claim in plain language

**Erdős's primitive-set conjecture (tightened form):** Let $x \geq 2$ and
let $A \subseteq [x, \infty)$ be a *primitive set* — a set of positive
integers no two of which satisfy the divisibility relation $a \mid b$.
Then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$

where the $o(1)$ term tends to $0$ as $x \to \infty$.

In words: the weighted "density" $\sum 1/(a \log a)$ of any antichain in
$\mathbb{N}_{\geq x}$ is bounded above by $1$ (asymptotically in the
threshold $x$).  The weighting $1/(a \log a)$ is the natural one that
makes the prime numbers achieve sum $\approx 1.6366$ — but they are
**not** a primitive set (they are, however, a primitive set only starting
from $x = 2$; as $x \to \infty$ the prime tail sum shrinks toward $0$).

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

*Sign reading:* The leading correction is **negative** ($-ck^2/2^k$), so
for every fixed $k \geq 1$ the sum is **strictly less than 1** and
approaches 1 from **below** as $k \to \infty$. F3 is consistent with F2
(once F2's unsigned big-O is read correctly) and directly rules out
$A_k$ being a counterexample.

### Witness contract (the only path to a counterexample claim)

A counterexample would be a finite primitive set $A \subset [x_{\mathrm{floor}}, \infty)$
with rigorously verified $\sum_{a \in A} 1/(a \log a) > 1.0$.
The verifier is `library.primitive_set_witness.verify_witness`; it checks:

1. Every element $a \in A$ satisfies $a \geq x_{\mathrm{floor}}$.
2. $A$ is pairwise non-divisible.
3. The sum $\sum_{a \in A} 1/(a \log a)$ exceeds `witness_threshold = 1.0`.

To embed a candidate witness, append a block of the form:

```
<!-- WITNESS
{"x_floor": ..., "elements": [...], "claimed_sum_lower_bound": ...}
WITNESS -->
```

at the bottom of this file. The conjecture's $o(1)$ caveat means a
witness exceeding 1 at finite $x_{\mathrm{floor}}$ is *suggestive* but
requires additional analysis (how large is the $o(1)$ term at that
specific $x_{\mathrm{floor}}$?) before claiming a true disproof.

### Structural plan (to be developed in subsequent rounds)

The natural approach is to stratify any primitive $A$ by $\Omega(a)$:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} \sum_{\substack{a \in A \\ \Omega(a)=k}} \frac{1}{a \log a}.$$

For each stratum, if $A_k^A := \{a \in A : \Omega(a) = k\}$ then
$A_k^A \subseteq A_k$, and the full set $A_k$ achieves sum $< 1$ by F3.
The difficulty is that $A$ may have elements in *multiple* strata and the
cross-stratum primitivity constraint interacts with within-stratum density
in a non-trivial way.

Open sub-questions (see `proof_open_questions.jsonl`):
- **Q2**: numerical verification of F3 for small $k$.
- **Q3**: distinguish F1 (all $A \subseteq \mathbb{N}$) from the finite
  prime-tail sum (which can exceed 1.399 at finite $x$).
- **Q4**: search for a witness primitive set with sum $> 1$.
- **Q5**: outline the lemma structure for the stratification argument.
