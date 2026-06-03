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

### 1.1 The Conjecture

A set $A \subset \mathbb{N}$ is **primitive** if no element of $A$ divides any other
distinct element of $A$.

**Conjecture (Erdős)**: For any primitive set $A \subset [x, \infty)$,

$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1) \quad \text{as } x \to \infty,$$

where the $o(1)$ term tends to $0$ as $x \to \infty$. Equivalently, the sum is bounded
above by $1$ in the limit.

This is an open problem. No claim of resolution is made in this document
unless a verifier-accepted `<!-- WITNESS -->` block is committed (counterexample
path) or the proof is completed (upper bound path).

### 1.2 Given Facts

Three facts are available from the ledger (`proofs/primitive_set_erdos.json`):

**F1 (Erdős-Zhang upper bound)**: For ANY primitive set $A \subseteq \mathbb{N}$ (no
floor restriction),

$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign note*: This is a STRICT UPPER bound of $\approx 1.399$, NOT a lower bound.
It is consistent with the conjecture (which posits the tighter bound 1). Misreading
F1 as a lower bound is a sign error.

**F2 (Omega-stratum lower, unsigned)**: Define $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$
(integers with exactly $k$ prime factors counted with multiplicity). Then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2 + o(1)}).$$

*Sign note*: The $O(\cdot)$ term is UNSIGNED — it can be positive or negative.
The inequality only says the sum is at least $1 - (\text{something bounded by } k^{-1/2+o(1)})$.
Concluding sum $> 1$ from F2 alone is a sign error.

**F3 (Exact asymptotic, approaches from below)**: For the same $A_k$,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

*Sign note*: The leading correction is $-(c + o(1)) k^2 / 2^k$ with $c > 0$, so the
sum is STRICTLY LESS THAN 1 for all $k \geq 1$, approaching 1 from BELOW as $k \to \infty$.
The sets $A_k$ are "extremal-looking" but do NOT violate the conjecture.

### 1.3 Witness Contract

The only path to claiming a counterexample is a verifier-accepted witness: a finite
primitive set $A \subset [x_{\text{floor}}, \infty)$ whose rigorous sum exceeds
`witness_threshold = 1.0`. The witness must be embedded as a `<!-- WITNESS -->` JSON
block in this file; `proof_prepare.py` then runs `library.primitive_set_witness.verify_witness`
and sets `witness_valid = 1` on success.

Required fields:
- `x_floor` (int ≥ 2): every element of `elements` must be ≥ `x_floor`.
- `elements` (list[int]): pairwise non-divisible integers, each ≥ `x_floor`.
- `claimed_sum_lower_bound` (float): agent's estimate; verifier recomputes rigorously.

### 1.4 Proof Strategy Outline

Two possible outcomes:
1. **Upper-bound proof** (confirm the conjecture): Show $\sum_{a \in A} 1/(a \log a) \leq 1 + o(1)$
   for any primitive $A \subset [x, \infty)$. F3 suggests $A_k$ are the extremal sets; the
   challenge is bounding cross-stratum sums and non-$A_k$ primitives.
2. **Counterexample** (disprove the conjecture): Find a specific primitive $A \subset [x_{\text{floor}}, \infty)$
   with verified sum $> 1.0$. Q4 pursues this numerically.

We begin with numerical grounding (Q2, Q3, Q4) before deciding which path is
more promising.

## Body

(Subsequent sections are added by each round. Current state: Section 1 complete.)
