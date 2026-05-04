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

## Sign and Ledger Cautions

- **F2 sign**: $O(k^{-1/2+o(1)})$ in F2 is unsigned — cannot conclude sum $> 1$.
- **F3 direction**: the correction $-(c+o(1))k^2/2^k$ is negative; the sum
  approaches 1 from **below**, not from above.
- **No resolution without witness**: this remains open; no claim of proof or
  disproof may appear without a verifier-accepted WITNESS block.

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

### Section 1 — Context and Facts

**Claim** (from `proofs/primitive_set_erdos.json`): For any primitive set
$A \subset \mathbb{Z}_{\geq 2}$ with $\min A \geq x$, as $x \to \infty$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1).$$

**F1** (cited from ledger): The Erdős–Zhang result gives an unconditional
upper bound of approximately $1.399$ on $\sum_{a \in A} 1/(a \log a)$ for
any primitive set $A$. This is the global ceiling; no primitive set
construction currently known achieves a sum above this value.

**F2** (cited from ledger, with sign caution): The $\Omega$-stratum lower
bound is $\Omega(k^{-1/2+o(1)})$. The error term is an *unsigned*
big-$O$, so F2 cannot be used to conclude that any particular sum exceeds 1.
Any argument of the form "by F2 the sum is $> 1$" is invalid.

**F3** (cited from ledger, direction caution): The canonical extremal sum,
formed by taking $A$ to be the set of primes in a short interval, approaches
1 from **below** as $x \to \infty$. The correction term $-(c + o(1))k^2/2^k$
is negative, confirming the direction. No element of $A_k$ (the $k$-th
$\Omega$-stratum) contributes a net positive overshoot relative to 1 in
this extremal family.

### Section 2 — Witness Search (Open)

A counterexample to the conjecture requires a finite primitive set
$A \subset [x_\text{floor}, \infty)$ whose rigorous lower bound on
$\sum 1/(a \log a)$ exceeds the threshold $1.0$, as verified by
`library.primitive_set_witness.verify_witness`.

Witness candidates were sampled at $x_\text{floor} \in \{100, 1000, 10000\}$.
No set tested achieved a rigorous lower bound exceeding $1.0$ at any of
these floors. The natural candidate families — prime intervals, dense
semiprime sets, mixed-$\Omega$ sets — all produced sums well below $1.0$
when restricted to $[x_\text{floor}, \infty)$ for $x_\text{floor} \geq 100$.

The search is incomplete; exhaustive enumeration at large $x_\text{floor}$
is computationally infeasible. This remains open.

### Section 3 — Stratification Approach and Obstacles

**Stratification.** For a primitive set $A$, partition by $\Omega(a) = k$:
$$A = \bigsqcup_{k \geq 1} A_k, \quad A_k = \{a \in A : \Omega(a) = k\}.$$
The sum decomposes as $\sum_{a \in A} 1/(a \log a) = \sum_{k \geq 1} S_k(A)$
where $S_k(A) = \sum_{a \in A_k} 1/(a \log a)$.

**Within each stratum.** F1 bounds the total; F3 identifies the $k$-th
stratum's extremal contribution. For large $k$, elements of $A_k$ are
large (since $\Omega(a) = k$ implies $a \geq 2^k$), so $1/(a \log a) \leq
1/(2^k \log 2^k) = 1/(k \cdot 2^k \log 2)$. The stratum $A_k$ can contain
at most polynomially many elements before pairs from different strata become
comparable, so $S_k(A)$ decays rapidly.

**Cross-stratum interaction (main obstacle).** When $A$ contains elements
from multiple strata simultaneously, the primitive-set constraint (no element
divides another) imposes correlations that are hard to exploit analytically.
Specifically, if $a \in A_1$ (a prime $p$) and $b \in A_2$ with $p | b$,
then $b \notin A$. This exclusion reduces $A_2$'s density but may leave other
large-$\Omega$ elements unconstrained. Quantifying the net effect on the sum
via only F1/F2/F3 has not been accomplished; the cross-stratum term remains
the key obstacle.

**Sub-problems filed**: see `proof_open_questions.jsonl` for qids Q1–Q5
(cross-stratum bound, F2 interpretation, extremal families, witness search
structure, and lemma-filing plan). Q5 (cross-stratum lemma) is in progress
in `proof_lemmas/`.
