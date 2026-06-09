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
  with the $O(\cdot)$ term **unsigned**. The big-O can be negative; the
  inequality does NOT establish that the sum exceeds 1. Claiming otherwise
  is a sign error — `critic_sign` will emit `unsigned-O-sign-confusion` BLOCKING.
- **F3 read upside-down**. F3 gives a sum STRICTLY LESS THAN 1 for every
  $k \geq 1$. The leading correction $-(c+o(1)) k^2/2^k$ is negative.
  Treating the sum as exceeding 1 from F3 is `f3-from-above-misread` BLOCKING.
- **Openness**. The claim is open. Any assertion of a counterexample or proof
  of the upper bound must be backed by a verifier-accepted `<!-- WITNESS -->`
  block (`witness_valid == 1`), or the `critic_openness` pass will block it.

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

### The Claim

For any $x \geq 2$, if $A \subset [x, \infty)$ is a **primitive set** of positive integers (no distinct element of $A$ divides another), then
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
where $o(1) \to 0$ as $x \to \infty$.

In words: the weighted reciprocal sum over any primitive set supported above $x$ is uniformly bounded by $1 + o(1)$. The conjecture asserts that the $A_k = \{n : \Omega(n) = k\}$ strata are near-extremal (they approach 1 from below by F3) and no primitive set can push the sum above 1 once $x$ is large enough.

### Given Facts (with sign disambiguations)

**F1 (Erdős–Zhang upper bound — UPPER bound, consistent with conjecture).**
For *any* primitive set $A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
Sign note: this is an UPPER bound — the sum is *strictly less than* 1.399. This does NOT contradict the conjecture (which claims a tighter bound of 1); it is merely a weaker known result. Misreading F1 as a lower bound is a sign error.

**F2 (Omega-stratum lower bound — UNSIGNED big-O, read carefully).**
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$:
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2 + o(1)}).$$
Sign note: the $O(k^{-1/2+o(1)})$ term is **unsigned** — it can be positive or negative. The inequality says the sum is at least $1 - |O(\ldots)|$, NOT at least $1 + (\text{positive quantity})$. Concluding that $\sum_{a \in A_k} > 1$ from F2 alone (without an additional positivity argument for the big-O term) is a sign error.

**F3 (Omega-stratum exact asymptotic — approaches 1 from BELOW).**
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$:
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
Sign note: the leading correction is $-(c+o(1)) k^2/2^k$ with $c > 0$, so the sum is **strictly less than 1** for every $k \geq 1$, approaching 1 from BELOW as $k \to \infty$. F3 directly rules out $A_k$ itself as a counterexample. F3 is consistent with F2 once F2's unsigned-O is read correctly.

### Witness Contract

To claim a counterexample (disproof of the conjecture), one must exhibit a finite primitive set $A \subset [x_\text{floor}, \infty)$ and have `library.primitive_set_witness.verify_witness` rigorously confirm the sum exceeds `witness_threshold = 1.0`. Required payload:
- `x_floor`: int $\geq 2$ — every element of `elements` must be $\geq x_\text{floor}$.
- `elements`: list of ints, pairwise non-divisible, each $\geq x_\text{floor}$.
- `claimed_sum_lower_bound`: float — agent's own claim; verifier recomputes rigorously.

A finite-$x$ witness exceeding 1 is suggestive but the conjecture's $o(1)$ caveat means a human reviewer must also argue the $o(1)$ gap is small at that $x_\text{floor}$.

### High-Level Proof Strategy (to be elaborated in subsequent rounds)

The natural attack is stratification by $\Omega(a)$:
1. For each stratum $k$, F3 gives $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k < 1$.
2. A primitive $A$ is a subset of $\bigcup_k A_k$, and $A \cap A_k$ is itself a primitive antichain within $A_k$.
3. The challenge: bounding $\sum_k \sum_{a \in A \cap A_k} 1/(a \log a)$ simultaneously across all strata, and showing the total is $< 1 + o(1)$.

Open sub-questions: see Q2 (numerical verification of F3), Q3 (primes-from-2 case), Q4 (counterexample search), Q5 (lemma decomposition).
