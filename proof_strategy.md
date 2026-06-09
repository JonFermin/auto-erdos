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

Open sub-questions: see Q5 (complete — see Section 3).

## Section 2: Numerical Evidence (Q2, Q3, Q4)

### Q2: Partial-sum spot-checks for A_k (k ≥ 2)

By F3, $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k < 1$ for all $k \geq 1$. Partial sums $\sum_{a \in A_k, a \leq 200000} 1/(a \log a)$ for $k = 2, 3, 4, 5$, computed via Python:

| $k$ | Partial sum (up to 200k) | $< 1$? |
|-----|--------------------------|--------|
| 2   | 0.8416                   | Yes ✓  |
| 3   | 0.4670                   | Yes ✓  |
| 4   | 0.2363                   | Yes ✓  |
| 5   | 0.1109                   | Yes ✓  |

All partial sums are $< 1$, consistent with F3. (The full infinite sums, given by F3, are larger than the partial sums since all terms are positive, but still $< 1$.)

### Q3: Primes restricted to $[x, \infty)$

For the prime set (= $A_1$) restricted to $[x, \infty)$, the sum $\sum_{p \geq x, p \text{ prime}} 1/(p \log p)$ computed over primes up to 500k:

| $x_\text{floor}$ | Restricted prime sum | $< 1$? |
|------------------|-----------------------|--------|
| 3                | $\approx 0.839$       | Yes ✓  |
| 5                | $\approx 0.536$       | Yes ✓  |
| 100              | $\approx 0.139$       | Yes ✓  |
| 1000             | $\approx 0.062$       | Yes ✓  |

For $x \geq 3$: the sum over primes in $[x, \infty)$ is $< 1$, consistent with both F3 and the conjecture's bound. By F1, for any primitive set in $[x, \infty)$ the sum is $< 1.399 + o(1)$; the restricted prime sums here are well inside that bound.

### Q4: Witness search results

Checked whether any primitive set in $[x_\text{floor}, \infty)$ achieves rigorous sum $> 1.0$ via `library.primitive_set_witness.verify_witness`:

- **x_floor = 100**: Tested 200 smallest primes $\geq 100$. Verifier returned `is_valid=False`, rigorous lower bound $\approx 0.078 < 1.0$.
- **x_floor = 1000, 10000**: Even smaller sums (each prime $\geq x_\text{floor}$ contributes $\leq 1/(x_\text{floor} \log x_\text{floor})$, giving tiny terms). No witness found.

**Conclusion**: The witness verifier found no counterexample for $x_\text{floor} \geq 100$. The conjecture remains open but appears numerically stable for large $x$.

## Section 3: Proof Structure and Lemma Decomposition (Q5)

The proof is decomposed into three lemmas, ordered by difficulty:

### Lemma stratum_bound (easy — follows directly from F3)

For any primitive set $A$ and any $k \geq 1$:
$$\sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} < 1.$$

This follows immediately from F3 (the equality) and monotonicity. Each stratum's contribution is bounded by $< 1$.

See `proof_lemmas/lemma_stratum_bound.md`.

### Lemma cross_stratum_sum (HARD — core open problem)

For any primitive $A \subset [x, \infty)$, the TOTAL sum across all strata satisfies:
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A \cap A_k} \frac{1}{a \log a} < 1 + o(1).$$

This is the main open challenge. Lemma stratum_bound bounds each stratum by $< 1$, but naively summing over $k$ gives $\sum_{k \geq 1} 1 = \infty$. The primitive set constraint (no divisibility relations) is needed to show the total is small. Current obstacle: no known proof technique closes this using only F1/F2/F3.

See `proof_lemmas/lemma_cross_stratum_sum.md`.

### Lemma f1_gap (HARD — the key gap to close)

Closing the gap between F1 ($< 1.399 + o(1)$) and the conjecture ($< 1 + o(1)$). The improvement comes from the $x \to \infty$ restriction: elements of $A$ are large, so individual terms are small. The challenge is translating this "each term is small" intuition into a rigorous bound $< 1 + o(1)$.

See `proof_lemmas/lemma_f1_gap.md`.

### Summary of proof strategy

The proof outline is:
1. By Lemma stratum_bound (easy, proved from F3): each stratum contributes $< 1$.
2. By Lemma cross_stratum_sum (OPEN): the total is $< 1 + o(1)$.
3. Lemma f1_gap (OPEN): provides the F1 → 1 improvement.

The proof currently stands as a **partial result**: the per-stratum bound (Step 1) is tight (follows from given facts), but the cross-stratum summation (Step 2) and the F1 gap (Step 3) are open. Closing either of the hard lemmas would complete the proof.
