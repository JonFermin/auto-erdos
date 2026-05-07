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

## Section 1: Setup — The Claim, Facts, and Witness Contract

### The Claim (in plain language)

Fix any $x \geq 2$. Let $A \subset [x, \infty)$ be any **primitive set** —
a set of integers in which no element divides any other. The conjecture of
Erdős asserts that the weighted count

$$S(A) := \sum_{a \in A} \frac{1}{a \log a}$$

satisfies $S(A) < 1 + o(1)$ where the $o(1)$ error tends to $0$ as $x \to \infty$.

In other words: for every primitive set entirely above a sufficiently large
threshold $x$, the sum $S(A)$ stays strictly below $1$ (by a margin that
grows as $x$ grows). The conjecture says primes (the "canonical" extremal
primitive set) are essentially the worst case, and even primes stay below
$\log 2 \approx 0.693 < 1$ for large $x$ (the sum over primes $\geq x$
converges and shrinks). The conjecture has not been resolved.

### The Three Given Facts

**F1 (Erdős–Zhang upper bound, 1935/1993).**
For ANY primitive set $A \subseteq \mathbb{N}$ (not just $A \subset [x,\infty)$),
$$S(A) = \sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

Sign note: This is a STRICT UPPER BOUND. It says the sum is less than ~1.399,
which is consistent with the conjecture (which claims a tighter bound of 1).
F1 does NOT say the sum can reach 1.399; it is not a lower bound.

**F2 (Omega-stratum lower bound, unsigned big-O).**
For $A_k := \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity),
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$

Sign note: The big-O term $O(k^{-1/2+o(1)})$ is UNSIGNED — its sign is
unknown. The inequality says "sum $\geq 1$ minus something of size
$O(k^{-1/2+o(1)})$", NOT "sum $\geq 1$ plus something positive." Deducing
"sum $> 1$" from F2 alone is a sign error. F2 is a weaker statement: it says
the sum is at least $1 - C k^{-1/2+o(1)}$ for some $C > 0$, approaching 1
from below.

**F3 (Exact asymptotic, approaches 1 from below).**
For the same $A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

Sign note: The leading correction $-(c+o(1))k^2/2^k$ is NEGATIVE (since
$c > 0$). The sum is therefore STRICTLY LESS THAN 1 for every $k \geq 1$,
approaching 1 from below as $k \to \infty$. This is consistent with the
conjecture. Note also that $A_k$ is not a subset of $[x, \infty)$ for any
fixed $x$ (it spans all of $\mathbb{N}$), so F3 directly applies to the
full Omega-stratum, not to a restricted version.

### The Witness Contract

The only route to claiming a counterexample is a **verified witness**:

- A finite set $A \subset [x_{\text{floor}}, \infty)$ for some explicit $x_{\text{floor}}$.
- $A$ must be primitive (no $a | b$ for distinct $a, b \in A$).
- The verifier `library.primitive_set_witness.verify_witness` must confirm
  $S(A) > 1.0$ (the witness threshold).
- The witness JSON must be embedded in `proof_strategy.md` inside the
  `<!-- WITNESS ... WITNESS -->` block.
- Even a verified witness at finite $x_{\text{floor}}$ is only a
  **candidate counterexample**: the conjecture's $o(1)$ caveat means
  a witness that exceeds 1 by a tiny margin at finite $x$ is not conclusive
  without an additional argument that the $o(1)$ gap is already negligible
  at $x_{\text{floor}}$. Human review is required before claiming a real result.

### What "proof" means here

Since the conjecture is open, "proving" it in this loop means one of:
(a) Producing a verified witness $A \subset [x_{\text{floor}}, \infty)$ with
    $S(A) > 1.0$ (disproof / counterexample direction).
(b) Developing partial structural results: lemmas that constrain $S(A)$ for
    specific subclasses, narrowing the gap between F1's bound of 1.399 and
    the conjectured bound of 1.

This session pursues both directions: search for witnesses (Q4) and develop
lemma structure (Q5).

## Section 2: Numerical Evidence

*(To be filled in Q2 and Q3.)*

## Section 3: Proof Structure and Lemmas

*(To be filled in Q5.)*
