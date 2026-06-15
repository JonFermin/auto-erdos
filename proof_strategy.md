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

### Q2: Stratum sum bounds from F3

By F3, for all $k \geq 1$:
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} < 1.$$

This is an ANALYTIC result from the given-facts ledger (F3). No numerical verification is needed: the inequality $< 1$ follows from $c > 0$ and $k^2/2^k > 0$. All sums approach 1 from below as $k \to \infty$ (since $k^2/2^k \to 0$); for any fixed $k$, the sum is strictly less than 1.

This sub-question (Q2) is answered directly by F3 and needs no further computation.

### Q3: Primes restricted to $[x, \infty)$

The prime set $A_1 = \{2, 3, 5, 7, \ldots\}$ is a primitive set. Restricting to $[x, \infty)$ gives $A_1 \cap [x, \infty)$. By F3, the full stratum sum $\sum_{a \in A_1} 1/(a\log a)$ is finite; hence its tail $\sum_{p \geq x} 1/(p\log p) \to 0$ as $x \to \infty$. For large $x$, the restricted prime sum is well within the conjecture's $1 + o(1)$ bound.

### Q4: Witness search results (summary)

Checked whether any primitive set in $[x_\text{floor}, \infty)$ achieves rigorous sum $> 1.0$ via `library.primitive_set_witness.verify_witness`.

Several candidates were tested: primes in $[x, \infty)$ for various $x$; fat antichains $\{N, N+1, \ldots, 2N-1\}$ (which are automatically primitive since $b/a \in (1,2)$ is never an integer); and $k$-almost-primes in intervals. All produced sums well below 1.0.

The fat antichain $\{N, N+1, \ldots, 2N-1\}$ is the densest possible primitive set in a dyadic interval. By Lemma single\_interval (with $x = N$), its sum is $< \log 2/\log N \to 0$ as $N \to \infty$.

This shows the densest single-block primitive set already has sum $\to 0$. No witness achieving sum $\geq 1$ was found.

**Conclusion**: No counterexample found across all candidate structures tested. The conjecture appears numerically robust.

## Section 3: Proof Structure and Lemma Decomposition (Q5)

The proof is decomposed into three lemmas, ordered by difficulty:

### Lemma stratum_bound (PROVED — from F3 and monotonicity)

For any primitive set $A$ and any $k \geq 1$:
$$\sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} < 1.$$

The first inequality holds because $A \cap A_k \subseteq A_k$ and all terms are positive. The equality is F3. The $< 1$ follows from F3's sign disambiguation ($c > 0$). Status: **proved** (round 5).

See `proof_lemmas/lemma_stratum_bound.md`.

### Lemma single_interval (PROVED — elementary calculus, no ledger facts)

For any $A \subseteq [x, 2x)$ (which is automatically primitive, since $b/a \in (1,2)$ for any $a < b$ in the interval):
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{\log 2}{\log x} \to 0 \quad \text{as } x \to \infty.$$

Proof: integral comparison with the antiderivative of $1/(t \log t)$; no F1/F2/F3 needed. See `proof_lemmas/lemma_single_interval.md`.

This proves the SINGLE-BLOCK CASE of Lemma f1_gap: for $A$ contained in one dyadic interval, the sum is $o(1)$. Status: **proved** (round 5).

See `proof_lemmas/lemma_single_interval.md`.

### Lemma cross_stratum_sum (HARD — partial proof available)

For any primitive $A \subset [x, \infty)$, the TOTAL sum across all strata satisfies:
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A \cap A_k} \frac{1}{a \log a} < 1 + o(1).$$

**Partial proof (proved from given facts):**
- **F1-based bound**: By F1 directly, the sum is $< 1.399 + o(1)$ for any primitive $A$. This is a proved bound with the wrong constant.
- **Tail argument (fixed $K$)**: For any fixed $K$, the strata $k = 1, \ldots, K$ contribute $o(1)$ as $x \to \infty$. By F3, each stratum sum $\sum_{a \in A_k} 1/(a \log a)$ is a finite positive real; hence its restriction to elements $\geq x$ vanishes as $x \to \infty$. Since $A \cap A_k \subseteq A_k \cap [x, \infty)$, the low-$k$ contribution vanishes.

**Remaining gap (OPEN):** The high-$k$ strata ($k > K$) need a new cross-stratum bound using the primitive antichain constraint. The naive stratum bound gives $\leq 1$ per stratum; summing over all $k > K$ diverges. The primitive constraint must prevent simultaneous large contributions across many high-$k$ strata, but this cannot be proved from F1/F2/F3 alone.

See `proof_lemmas/lemma_cross_stratum_sum.md`.

### Lemma f1_gap (HARD — dyadic analysis identifies the obstacle)

Closing the gap between F1 ($< 1.399 + o(1)$) and the conjecture ($< 1 + o(1)$).

**Dyadic decomposition analysis:** Splitting $A = \bigsqcup_{j \geq 0} A \cap [2^j x, 2^{j+1} x)$, the naive bound gives contribution $< \log 2/\log(2^j x)$ per block. For any FIXED $K$, Lemma multi\_block\_finite (Section 5) gives finite sum $< K\log 2/\log x \to 0$. However, when $A$ spans infinitely many blocks, the per-block bounds cannot be summed to a finite limit (as $K$ grows, the total bound grows without bound); the naive strategy fails for infinite-extent sets. The single-block triviality (every subset of $[N, 2N)$ is primitive) means the antichain constraint contributes nothing within a block — only cross-block constraints matter.

**Key obstacle:** The restriction $A \subset [x, \infty)$ does NOT prevent elements from having small prime factors ($p = 2, 3, \ldots$). Elements of $A$ are large but can be highly composite with small prime factors. The upper bound F1 holds for any primitive set regardless of element size; the $x$-restriction alone does not improve the constant 1.399. Closing the gap from $1.399$ to $1$ requires either (a) a new argument that explicitly uses the large-element constraint, or (b) a smooth-number decomposition separating rough-part (all factors $\geq y$) from smooth-part (some factor $< y$).

See `proof_lemmas/lemma_f1_gap.md`.

### Summary of proof strategy

The proof outline is:
1. By Lemma stratum_bound (easy, proved from F3): each stratum contributes $< 1$.
2. By Lemma cross_stratum_sum (partially proved, open for constant 1): the total is $< 1.399$ (proved via F1) and $< 1 + o(1)$ (open).
3. Lemma f1_gap (OPEN): provides the F1 → 1 improvement; dyadic decomposition identifies the core obstacle.

**Proved partial results:**
- $\sum_{a \in A} f(a) < 1.399$ for any primitive $A$ (F1) — **proved**.
- Lemma `stratum_bound`: each stratum contributes $< 1$ (F3 + monotonicity) — **proved** (round 5).
- Lemma `single_interval`: for $A \subseteq [x, 2x)$, sum $< \log 2/\log x \to 0$ (calculus) — **proved** (round 5).
- For any fixed $K$: the low-$k$ strata contribute $o(1)$ as $x \to \infty$ (F3 convergence) — **proved**.

**Remaining open gaps:**
- Lemma `cross_stratum_sum` (high-$k$ part): the primitive antichain constraint must suppress simultaneous large contributions across all high-$k$ strata. Not provable from F1/F2/F3 alone.
- Lemma `f1_gap` (multi-block case): extending Lemma single_interval from one dyadic block to $A$ spanning multiple blocks. This is the core of the conjecture.

Closing either gap would constitute a significant new result beyond Zhang 1993.

## Section 4: Partial Result and Open Status (Q6, Q7, Q8)

**Q7 (cross_stratum_sum partial proof):** F1 directly gives sum $< 1.399$; for any fixed $K$, strata $k \leq K$ contribute $o(1)$ as $x \to \infty$ (F3 tail vanishing). High-$k$ coupling across strata remains open.

**Q8 (f1_gap):** Dyadic decomposition gives per-block bound $\log 2/\log(2^j x)$; infinitely many blocks give unbounded total — the within-block antichain constraint is vacuous. Cross-block primitivity is the hard gap.

**Cumulative proved results (Q6–Q8):**
1. `stratum_bound` (F3 + monotonicity): each stratum $< 1$ — **proved**.
2. `single_interval` (calculus): sum over $A \subseteq [x, 2x)$ is $< \log 2/\log x \to 0$ — **proved**.
3. Partial cross\_stratum (F1): sum $< 1.399$ — **proved**.

## Section 5: Finite Dyadic Range (Q9)

### Lemma multi_block_finite (PROVED)

**Statement.** For any set $A \subseteq [x, 4x)$ (two consecutive dyadic blocks), $\sum_{a \in A} 1/(a \log a) \to 0$ as $x \to \infty$.

**Proof.** Apply Lemma single\_interval (with parameter $x$) to $A \cap [x,2x)$: contribution $< \log 2/\log x$. Apply Lemma single\_interval (with parameter $x' = 2x$) to $A \cap [2x,4x)$: contribution $< \log 2/\log(2x)$. Both $\log 2/\log x$ and $\log 2/\log(2x)$ tend to $0$ as $x \to \infty$, so the sum of contributions tends to $0$. $\square$

No primitivity is needed; the bound holds for any $A \subseteq [x,4x)$.

**General case — Lemma multi\_block\_finite (K blocks).** For any $A \subseteq [x, 2^K x)$ and integer $K \geq 1$:
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{K \log 2}{\log x}.$$

*Proof (induction on $K$; $K$ is a fixed positive integer; all bounds are for fixed $K$ and $x \to \infty$).* $K=1$: Lemma single\_interval with parameter $x$. $K \to K+1$: split $[x, 2^{K+1}x) = [x, 2^Kx) \cup [2^Kx, 2^{K+1}x)$. By induction (fixed $K$), the first piece gives sum $< K\log 2/\log x$. By Lemma single\_interval (with parameter $x' = 2^K x$), the second piece gives sum $< \log 2/\log(2^K x) \leq \log 2/\log x$ (since $\log(2^K x) \geq \log x$ for $K \geq 1$). Adding: total $< (K+1)\log 2/\log x$. $\square$

Status: **proved** (Q9); see also `proof_lemmas/lemma_multi_block_finite.md`.

**Corollary.** The conjecture $\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ holds for any primitive set $A$ confined to a bounded ratio above $x$. The genuine difficulty is the infinite-extent case, where the per-block bound does not sum to a finite quantity — closing that gap requires cross-block primitive constraints beyond F1/F2/F3.

**Updated cumulative proved results:**
1. Lemma `stratum_bound` (F3): each stratum $< 1$ — **proved**.
2. Lemma `single_interval` (calculus): $A \subseteq [x,2x) \Rightarrow$ sum $< \log 2/\log x \to 0$ — **proved**.
3. Lemma `multi_block_finite` (two-block): $A \subseteq [x,4x) \Rightarrow$ sum $< \log 2/\log x + \log 2/\log(2x) \to 0$ — **proved** (Q9).
4. Cross-stratum bound (F1): sum $< 1.399$ for any primitive $A$ — **proved**.
5. Low-$k$ tail (F3): strata $k \leq K$ contribute $o(1)$ — **proved**.

## Section 6: Gap Analysis and Ledger Requirements (Q11)

### Why the hard gaps require additional tools

Both remaining gaps — the high-$k$ cross-stratum coupling and the multi-block f1\_gap — cannot be closed from F1, F2, F3, and elementary calculus alone. This section documents precisely what additional ingredient is needed.

**Gap 1 (high-$k$ cross-stratum coupling):** The primitive antichain constraint across strata $k > K$ must prevent the total from exceeding $1 + o(1)$. Closing this gap requires analytic estimates involving the distribution of prime factors that are not available from F1, F2, F3, and elementary calculus alone. These estimates are not in the given-facts ledger; adding them as explicit facts would enable the argument.

**Gap 2 (F1 to 1 improvement):** Elements of $A \subseteq [x, \infty)$ can have small prime factors even though the elements themselves are large. The large-element condition should provide an extra saving beyond F1's bound, but extracting it requires structural information about how element size interacts with prime factorization — information not derivable from F1, F2, F3 alone.

**Status of open questions:**
- Q1 through Q9: complete (see Sections 1–5 above).
- Q10: obstacle confirmed — finite-range analysis shows the infinite-extent case requires arguments beyond dyadic block decomposition.
- Q11: this section — gap analysis complete.
- **What remains**: adding analytic prime-sum tools to the given-facts ledger, or finding a purely elementary argument that avoids them. The partial result stands as the best provable outcome from the current ledger.

## Section 7: Bounded-Support Case (Q12)

### Theorem bounded\_support (PROVED — calculus only, no ledger facts)

**Statement.** For any $M \geq 2$ and any primitive set $A \subseteq [x, Mx)$:
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{\lceil \log_2 M \rceil \cdot \log 2}{\log x} \to 0 \quad \text{as } x \to \infty.$$

In particular, the Erdős primitive-set conjecture's bound $\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ is confirmed for any primitive set $A$ with bounded support ratio $\max(A)/\min(A) \leq M$ (fixed $M$).

**Proof.** Let $K = \lceil \log_2 M \rceil$. Then $[x, Mx) \subseteq [x, 2^K x)$, and $A \subseteq [x, Mx) \subseteq [x, 2^K x)$. By the general-$K$ Lemma multi\_block\_finite (proved by induction in Section 5):
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{K \log 2}{\log x} \to 0. \qquad \square$$

**Scope.** The conjecture holds for all "finite-range" primitive sets — those where elements span at most a fixed multiplicative factor. Covered cases:
- $A \subseteq [x, 2x)$: Lemma single\_interval (sum $< \log 2/\log x$).
- $A \subseteq [x, 4x)$: Lemma multi\_block\_finite, two-block (Q9).
- $A \subseteq [x, 2^K x)$: this theorem (general $K$).

**The remaining open case.** The conjecture is still open for primitive sets $A \subseteq [x, \infty)$ with UNBOUNDED support ratio (infinitely many dyadic blocks). The best available bound for this case is F1: sum $< 1.399 + o(1)$. Closing the gap to $1 + o(1)$ requires prime-sum estimates not in the current ledger (Section 6).

**Summary table — resolved vs. open:**

| Case | Status | Bound |
|---|---|---|
| $A \subseteq [x, Mx)$, fixed $M$ | **Proved** (Theorem bounded\_support) | $o(1)$ as $x \to \infty$ |
| $A \subseteq [x, \infty)$, all primitive $A$ | **Open** (hard gap) | $< 1.399$ from F1 |
| Full conjecture: $A \subseteq [x, \infty)$ | **Conjectured** | $< 1 + o(1)$ |

## Section 8: Single-Stratum Sub-Case (Q13)

### Theorem single\_stratum (PROVED — F3 and tail argument)

**Statement.** For any fixed $k \geq 1$ and any $A \subseteq A_k \cap [x, \infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{a \in A_k \cap [x,\infty)} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

In particular, $\sum_{a \in A} 1/(a \log a) < 1 + o(1)$ holds for all primitive $A$ contained in a single stratum $A_k$ above $x$.

**Proof.** By F3, the full stratum sum $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k$ is a finite positive real (for each fixed $k$). Since all terms are positive, it is a convergent series of positive terms. For any convergent positive series, its tail $\sum_{a \geq x} (\text{term})$ tends to $0$ as $x \to \infty$. Since $A \subseteq A_k \cap [x, \infty)$, we have:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{a \in A_k, a \geq x} \frac{1}{a \log a} \to 0. \qquad \square$$

**Special case ($k=1$, primes).** Taking $A = A_1 \cap [x,\infty)$ (primes $\geq x$): applying the theorem above with $k=1$, the tail $\sum_{p \geq x} 1/(p\log p) \to 0$ as $x \to \infty$.

**Multi-stratum extension.** For $A \subseteq \bigcup_{k=1}^{K} A_k \cap [x,\infty)$ with fixed $K$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{k=1}^K \sum_{a \in A_k, a \geq x} \frac{1}{a \log a} \to 0,$$
since each of the finitely many summands $\to 0$ by F3 + tail argument. This covers the already-proved low-$k$ tail result (Section 4) and confirms the conjecture for all sets supported on finitely many strata.

**Updated cumulative proved results (all from F1/F3 or calculus):**
1. Lemma `stratum_bound`: each stratum $< 1$ — **proved**.
2. Lemma `single_interval`: $A \subseteq [x,2x) \Rightarrow$ sum $\to 0$ — **proved**.
3. Lemma `multi_block_finite` (K blocks): $A \subseteq [x,2^Kx) \Rightarrow$ sum $< K\log 2/\log x \to 0$ — **proved**.
4. Theorem `bounded_support`: $A \subseteq [x,Mx)$ (fixed $M$) $\Rightarrow$ sum $\to 0$ — **proved**.
5. Theorem `single_stratum`: $A \subseteq A_k \cap [x,\infty)$ (fixed $k$) $\Rightarrow$ sum $\to 0$ — **proved** (Q13).
6. Multi-stratum: $A \subseteq \bigcup_{k=1}^K A_k \cap [x,\infty)$ (fixed $K$) $\Rightarrow$ sum $\to 0$ — **proved** (Q13).

**Open case.** All proved results require either (a) bounded support ratio, or (b) support on finitely many strata. The hard open case is $A \subseteq [x, \infty)$ spanning BOTH infinitely many dyadic blocks AND infinitely many strata. This remains open (see Section 6).

## Section 9: Hybrid Case (Q14)

### Theorem hybrid\_case (PROVED — combines bounded\_support and single\_stratum)

**Statement.** Fix $M \geq 2$ and $K \geq 1$. Let $A \subseteq [x, \infty)$ be a primitive set such that every element of $A$ outside $[x, Mx)$ comes from at most $K$ strata:
$$A \cap [Mx, \infty) \subseteq \bigcup_{k=1}^K A_k.$$
Then:
$$\sum_{a \in A} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$
In particular the Erdős conjecture's bound $< 1 + o(1)$ holds for this class.

**Proof.** Decompose $A = A_{\text{near}} \cup A_{\text{far}}$ where $A_{\text{near}} = A \cap [x, Mx)$ and $A_{\text{far}} = A \cap [Mx, \infty)$.

*Near part.* By Theorem bounded\_support (Section 7) with bound $M$ and base $x$:
$$\sum_{a \in A_{\text{near}}} \frac{1}{a \log a} < \frac{\lceil \log_2 M \rceil \log 2}{\log x} \to 0.$$

*Far part.* By hypothesis $A_{\text{far}} \subseteq \bigcup_{k=1}^K A_k$. For each fixed $k \in \{1,\ldots,K\}$:
$$\sum_{a \in A_{\text{far}} \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k,\, a \geq Mx} \frac{1}{a \log a} \to 0,$$
since (by F3) the full $k$-stratum series $\sum_{a \in A_k} 1/(a\log a)$ converges and its tail vanishes. Summing over $k = 1, \ldots, K$:
$$\sum_{a \in A_{\text{far}}} \frac{1}{a \log a} \leq \sum_{k=1}^K \sum_{a \in A_k,\, a \geq Mx} \frac{1}{a \log a} \to 0.$$

*Conclusion.* Both parts tend to $0$, so the total $\to 0$. $\square$

**Scope.** This theorem covers sets that are "spread out" at large scales but concentrated on finitely many prime-factor-count strata above the threshold $Mx$. It generalises:
- Theorem bounded\_support: take $A \subseteq [x, Mx)$ entirely (no far part).
- Theorem single\_stratum: take $K = 1$ and $M$ arbitrary (all far elements in one stratum).

**Updated cumulative proved results:**
1. Lemma `stratum_bound` — each stratum $< 1$ (F3) — **proved**.
2. Lemma `single_interval` — $A \subseteq [x,2x) \Rightarrow$ sum $\to 0$ — **proved**.
3. Lemma `multi_block_finite` — $A \subseteq [x,2^Kx) \Rightarrow$ sum $\to 0$ — **proved**.
4. Theorem `bounded_support` — $A \subseteq [x,Mx)$ (fixed $M$) $\Rightarrow$ sum $\to 0$ — **proved**.
5. Theorem `single_stratum` — $A \subseteq A_k \cap [x,\infty)$ (fixed $k$) $\Rightarrow$ sum $\to 0$ — **proved**.
6. Multi-stratum — $A \subseteq \bigcup_{k \leq K} A_k \cap [x,\infty)$ (fixed $K$) $\Rightarrow$ sum $\to 0$ — **proved**.
7. Theorem `hybrid_case` — near part bounded, far part in $K$ strata $\Rightarrow$ sum $\to 0$ — **proved** (Q14).

**The remaining open case.** A primitive $A \subseteq [x,\infty)$ with BOTH: (i) unbounded support (not confined to any $[x,Mx)$), AND (ii) infinitely many strata above every threshold $Mx$. Closing this requires analytic cross-stratum tools not in F1/F2/F3.

## Section 10: Sparse Stratum Lemma (Q15)

### Lemma sparse\_stratum (PROVED — elementary, no ledger facts needed)

**Statement.** Let $A \subseteq [x, \infty)$ be a set (not necessarily primitive) satisfying $|A \cap A_k| \leq 1$ for every $k \geq 1$. Then:
$$\sum_{a \in A} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

In particular the Erdős conjecture holds (sum $< 1 + o(1)$) for all such $A$.

**Proof.** Let $K = \lfloor \log_2 x \rfloor$. Decompose the sum by "low strata" ($k \leq K$) and "high strata" ($k > K$).

*Low strata ($k \leq K$, at most $K$ terms).* For each $k \leq K$ with $A \cap A_k \neq \emptyset$, let $a_k$ be the unique element. Since $a_k \geq x$:
$$\sum_{k \leq K} \frac{1}{a_k \log a_k} \leq \frac{K}{x \log x} \to 0,$$
because $K = \lfloor \log_2 x \rfloor = O(\log x)$ while $x \log x$ grows faster.

*High strata ($k > K$, possibly infinitely many terms).* For any $k$-almost prime $n$, since all prime factors are $\geq 2$, we have $n \geq 2^k$. Hence for each $a_k \in A_k$:
$$\frac{1}{a_k \log a_k} \leq \frac{1}{2^k \cdot k \log 2}.$$
The series $\sum_{k \geq 1} \frac{1}{k \cdot 2^k \cdot \log 2}$ converges (by comparison: since $k \log 2 \geq \log 2 > 1/2$ for all $k \geq 1$, we have $1/(k \cdot 2^k \cdot \log 2) < 1/2^{k-1}$, and $\sum_{k \geq 1} 1/2^{k-1} = 2 < \infty$). For any convergent positive series, its tail vanishes: as $K = \lfloor \log_2 x \rfloor \to \infty$:
$$\sum_{k > K} \frac{1}{a_k \log a_k} \leq \sum_{k > K} \frac{1}{k \cdot 2^k \cdot \log 2} \to 0.$$

*Conclusion.* Both parts tend to $0$, so the total $\to 0$. $\square$

**Significance.** This is the first proved result for a class of primitive sets with UNBOUNDED support AND potentially infinitely many strata (if $A$ has one element from each of infinitely many strata, it spans infinitely many strata). The key constraint is the "sparse" condition $|A \cap A_k| \leq 1$. The proof does not use F1, F2, or F3 — only the elementary bound $2^k \leq$ (any $k$-almost prime).

**Updated cumulative proved results:**
1. `stratum_bound`: each stratum $< 1$ (F3) — **proved**.
2. `single_interval`: $A \subseteq [x,2x) \Rightarrow$ sum $\to 0$ — **proved**.
3. `multi_block_finite`: $A \subseteq [x,2^K x) \Rightarrow$ sum $\to 0$ — **proved**.
4. `bounded_support`: $A \subseteq [x,Mx)$ (fixed $M$) $\Rightarrow$ sum $\to 0$ — **proved**.
5. `single_stratum`: $A \subseteq A_k \cap [x,\infty)$ (fixed $k$) $\Rightarrow$ sum $\to 0$ — **proved**.
6. `multi_stratum`: $A \subseteq \bigcup_{k \leq K} A_k \cap [x,\infty)$ (fixed $K$) $\Rightarrow$ sum $\to 0$ — **proved**.
7. `hybrid_case`: near part bounded, far part $K$ strata $\Rightarrow$ sum $\to 0$ — **proved**.
8. `sparse_stratum`: $|A \cap A_k| \leq 1$ for all $k$ (infinitely many strata allowed) $\Rightarrow$ sum $\to 0$ — **proved** (Q15).

**Open case (refined).** The hard open case requires both: (i) unbounded support (elements in $[x, \infty)$ at all scales), AND (ii) MULTIPLE elements in at least one stratum — specifically, $|A \cap A_k| \geq 2$ for some $k$ (or infinitely many $k$). The sparse\_stratum lemma covers all cases where no stratum contributes more than one element.

## Section 11: Linear Density Lemma (Q16)

### Lemma linear\_density (PROVED — elementary, no ledger facts needed)

**Statement.** Let $A \subseteq [x, \infty)$ be any set satisfying $|A \cap A_k| \leq k$ for every $k \geq 1$ (at most $k$ elements from the $k$-th stratum). Then:
$$\sum_{a \in A} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

**Proof.** Let $K = \lfloor \log_2 x \rfloor$. Split into low strata ($k \leq K$) and high strata ($k > K$).

*Low strata ($k \leq K$).* Each stratum $k$ contributes at most $k$ elements, each $\geq x$. Per-stratum contribution: $\leq k/(x \log x)$. Sum over $k = 1,\ldots,K$:
$$\sum_{k \leq K} \frac{k}{x \log x} = \frac{K(K+1)}{2 x \log x} \to 0,$$
since $K = \lfloor \log_2 x \rfloor$ grows at most logarithmically while $x \log x \to \infty$ much faster.

*High strata ($k > K$).* Any $k$-almost prime satisfies $n \geq 2^k$, so each of the $\leq k$ elements $a_i \in A \cap A_k$ satisfies $1/(a_i \log a_i) \leq 1/(k \log 2 \cdot 2^k)$. Per-stratum contribution:
$$\text{(stratum } k \text{)} \leq k \cdot \frac{1}{k \log 2 \cdot 2^k} = \frac{1}{\log 2 \cdot 2^k}.$$
The factor of $k$ in the density bound cancels the $k$ in the denominator. Summing over all $k > K$:
$$\sum_{k > K} \frac{1}{\log 2 \cdot 2^k} = \frac{1}{\log 2} \cdot \frac{1}{2^K} \to 0 \quad (K \to \infty).$$

*Conclusion.* Both parts tend to $0$, so the total $\to 0$. $\square$

**Updated cumulative proved results:**
1. `stratum_bound`: each stratum $< 1$ (F3) — **proved**.
2. `single_interval`: $A \subseteq [x,2x) \Rightarrow$ sum $\to 0$ — **proved**.
3. `multi_block_finite`: $A \subseteq [x,2^Kx)$ (fixed $K$) $\Rightarrow$ sum $\to 0$ — **proved**.
4. `bounded_support`: $A \subseteq [x,Mx)$ (fixed $M$) $\Rightarrow$ sum $\to 0$ — **proved**.
5. `single_stratum`: $A \subseteq A_k \cap [x,\infty)$ (fixed $k$) $\Rightarrow$ sum $\to 0$ — **proved**.
6. `multi_stratum`: $A \subseteq \bigcup_{k \leq K} A_k \cap [x,\infty)$ (fixed $K$) $\Rightarrow$ sum $\to 0$ — **proved**.
7. `hybrid_case`: near part bounded, far part in $K$ strata $\Rightarrow$ sum $\to 0$ — **proved**.
8. `sparse_stratum`: $|A \cap A_k| \leq 1$ for all $k \Rightarrow$ sum $\to 0$ — **proved**.
9. `linear_density`: $|A \cap A_k| \leq k$ for all $k \Rightarrow$ sum $\to 0$ — **proved** (Q16).

**Open case (final).** The sub-exponential threshold: when $|A \cap A_k| = o(2^k)$, the high-strata sum is controlled by the geometric tail. The genuinely hard open case requires understanding sets where some strata have near-maximal occupancy (proportional to the stratum size $|A_k|$).

## Section 12: Polynomial Density (Q17)

### Lemma polynomial\_density (PROVED — elementary ratio test, no ledger facts)

**Statement.** Let $m \geq 1$ be a fixed integer. Let $A \subseteq [x, \infty)$ satisfy $|A \cap A_k| \leq k^m$ for every $k \geq 1$. Then:
$$\sum_{a \in A} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

**Proof.** Let $K = \lfloor \log_2 x \rfloor$. Split into low and high strata.

*Low strata ($k \leq K$).* Each of the $\leq k^m$ elements in $A \cap A_k$ satisfies $a \geq x$. Per-stratum contribution $\leq k^m/(x \log x)$. Summing over $k = 1,\ldots,K$: the sum is $\leq K^{m+1}/(x\log x)$. Since $K = \lfloor \log_2 x \rfloor$ grows only logarithmically while $x\log x \to \infty$ much faster (for any fixed $m$), this tends to $0$.

*High strata ($k > K$).* Each of the $\leq k^m$ elements in $A \cap A_k$ satisfies $a \geq 2^k$, so $1/(a\log a) \leq 1/(k\log2 \cdot 2^k)$. Per-stratum contribution: $\leq k^m \cdot 1/(k\log2 \cdot 2^k) = k^{m-1}/(\log2 \cdot 2^k)$. The series $\sum_{k \geq 1} k^{m-1}/2^k$ converges by the ratio test:
$$\frac{(k+1)^{m-1}/2^{k+1}}{k^{m-1}/2^k} = \frac{1}{2}\left(1 + \frac{1}{k}\right)^{m-1} \to \frac{1}{2} < 1 \quad (k \to \infty).$$
For any convergent positive series, its tail vanishes as the truncation point $K \to \infty$:
$$\sum_{k > K} \frac{k^{m-1}}{\log 2 \cdot 2^k} \to 0.$$

*Conclusion.* Both parts tend to $0$, so the total $\to 0$. $\square$

**Note.** This includes the linear-density case ($m=1$) as a special case (ratio test gives limit $1/2$), and extends to all polynomial growth rates. The key is that $k^{m-1}/2^k \to 0$ exponentially fast for any fixed $m$, no matter how large.

**Updated cumulative proved results:**
1.–9. (see Sections 10–11)
10. `polynomial_density`: $|A \cap A_k| \leq k^m$ (fixed $m \geq 1$) for all $k \Rightarrow$ sum $\to 0$ — **proved** (Q17).

The density threshold is now: sub-polynomial growth (up to any $k^m$) is covered. Exponential growth $|A \cap A_k| \sim 2^k$ is the open boundary.

## Section 13: Sub-Exponential Geometric Density (Q18)

### Lemma sub\_exponential\_density (PROVED — ratio test, no ledger facts)

**Statement.** Let $C < 2$ be a fixed real with $C \geq 1$. Let $A \subseteq [x, \infty)$ satisfy $|A \cap A_k| \leq C^k$ for every $k \geq 1$. Then:
$$\sum_{a \in A} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

**Proof.** Let $K = \lfloor \log_2 x \rfloor$. Split into low strata ($k \leq K$) and high strata ($k > K$).

*Low strata ($k \leq K$).* Each of the $\leq C^k$ elements in $A \cap A_k$ satisfies $a \geq x$ (since $A \subseteq [x,\infty)$), giving $1/(a\log a) \leq 1/(x\log x)$. Per-stratum contribution $\leq C^k/(x\log x)$. Summing over $k = 1,\ldots,K$:
$$\sum_{k=1}^K \frac{C^k}{x \log x} \leq \frac{C^{K+1}}{(C-1)\, x \log x}.$$
(For $C = 1$ the geometric sum equals $K/(x\log x)$, which also $\to 0$.)
Now $C^K \leq C^{\log_2 x} = x^{\log_2 C}$. Since $C < 2$, we have $\log_2 C < 1$, so
$$\frac{C^{K+1}}{x \log x} \leq \frac{C \cdot x^{\log_2 C}}{x \log x} = \frac{C}{x^{1 - \log_2 C} \log x} \to 0,$$
because $1 - \log_2 C > 0$.

*High strata ($k > K$).* Any $k$-almost prime satisfies $a \geq 2^k$, so $1/(a\log a) \leq 1/(k\log 2 \cdot 2^k)$. Per-stratum contribution:
$$\leq \frac{C^k}{k \log 2 \cdot 2^k} = \frac{1}{k\log 2} \left(\frac{C}{2}\right)^k.$$
Since $C < 2$, the ratio $C/2 < 1$. By the ratio test:
$$\frac{(k+1)^{-1}(C/2)^{k+1}}{k^{-1}(C/2)^k} = \frac{k}{k+1} \cdot \frac{C}{2} \to \frac{C}{2} < 1 \quad (k \to \infty).$$
Hence $\sum_{k \geq 1} (C/2)^k/(k\log 2)$ converges. Its tail vanishes: as $K = \lfloor \log_2 x \rfloor \to \infty$,
$$\sum_{k > K} \frac{(C/2)^k}{k \log 2} \to 0. \qquad \square$$

*Conclusion.* Both the low-strata and high-strata contributions tend to $0$, so the total $\to 0$.

**Scope and relation to earlier lemmas.** This lemma strictly generalises all previously proved density results:
- **Sparse** ($|A \cap A_k| \leq 1 = 1^k$, i.e., $C = 1$): covered (use $C = 1$ with the $K/(x\log x)$ variant).
- **Linear** ($|A \cap A_k| \leq k \leq k^1$): since $k = o(C^k)$ for any $C > 1$, choose $C = 3/2$; or note $k < (3/2)^k$ for all $k \geq 1$.
- **Polynomial** ($|A \cap A_k| \leq k^m$): for any fixed $m$, $k^m < (3/2)^k$ for all sufficiently large $k$, so split at a fixed $k_0$ and apply the lemma for large $k$.
- **Sub-exponential geometric**: exactly the statement of this lemma with $1 \leq C < 2$.

**The open boundary (C = 2).** If $|A \cap A_k| = 2^k$, the high-strata series becomes $\sum_{k>K} 1/(k\log 2)$, which diverges (harmonic). The ratio test fails. This is the genuine analytic difficulty: near-full-density primitive sets in each stratum.

**Updated cumulative proved results:**
1. `stratum_bound`: each stratum $< 1$ (F3) — **proved**.
2. `single_interval`: $A \subseteq [x,2x) \Rightarrow$ sum $\to 0$ — **proved**.
3. `multi_block_finite`: $A \subseteq [x,2^K x)$ (fixed $K$) $\Rightarrow$ sum $\to 0$ — **proved**.
4. `bounded_support`: $A \subseteq [x,Mx)$ (fixed $M$) $\Rightarrow$ sum $\to 0$ — **proved**.
5. `single_stratum`: $A \subseteq A_k \cap [x,\infty)$ (fixed $k$) $\Rightarrow$ sum $\to 0$ — **proved**.
6. `multi_stratum`: $A \subseteq \bigcup_{k \leq K} A_k \cap [x,\infty)$ (fixed $K$) $\Rightarrow$ sum $\to 0$ — **proved**.
7. `hybrid_case`: near part bounded, far part in $K$ strata $\Rightarrow$ sum $\to 0$ — **proved**.
8. `sparse_stratum`: $|A \cap A_k| \leq 1$ for all $k \Rightarrow$ sum $\to 0$ — **proved**.
9. `linear_density`: $|A \cap A_k| \leq k$ for all $k \Rightarrow$ sum $\to 0$ — **proved**.
10. `polynomial_density`: $|A \cap A_k| \leq k^m$ (fixed $m$) for all $k \Rightarrow$ sum $\to 0$ — **proved**.
11. `sub_exponential_density`: $|A \cap A_k| \leq C^k$ (fixed $C < 2$) for all $k \Rightarrow$ sum $\to 0$ — **proved** (Q18).

**Open case.** The remaining open case is $|A \cap A_k| \sim 2^k$ (or any density where $|A \cap A_k|/(k 2^k)$ has divergent sum). The precise density threshold is: the conjecture holds whenever $\sum_{k \geq 1} |A \cap A_k|/(k 2^k) < \infty$; the open boundary is the set of $A$ where this series diverges.

## Section 14: Density Convergence Theorem (Q19)

### Theorem density\_convergence (PROVED — comparison and tail, no ledger facts)

**Statement.** Let $A_0 \subseteq \mathbb{N}$ be a **fixed** set (not necessarily primitive). Define the **density series**:
$$D(A_0) := \sum_{k=1}^{\infty} \frac{|A_0 \cap A_k|}{k \cdot 2^k}.$$
If $D(A_0) < \infty$, then the tail sum tends to $0$ as the threshold $x \to \infty$:
$$\sum_{\substack{a \in A_0 \\ a \geq x}} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

**Proof.** The fixed set $A_0$ is treated as a single (possibly infinite) object; $x$ is an external threshold that we send to $\infty$.

For any $k \geq 1$ and any $a \in A_k$, we have $a \geq 2^k$ (since $a$ has $k$ prime factors, each $\geq 2$), so:
$$\frac{1}{a \log a} \leq \frac{1}{2^k \cdot k \log 2}.$$
Summing over all $a \in A_0$:
$$\sum_{a \in A_0} \frac{1}{a \log a}
\leq \sum_{k \geq 1} |A_0 \cap A_k| \cdot \frac{1}{k \log 2 \cdot 2^k} = \frac{D(A_0)}{\log 2} < \infty.$$

Thus $\sum_{a \in A_0} 1/(a\log a)$ is a convergent series (of positive terms) over the fixed index set $A_0$. For any convergent series of positive terms, the tail sum $\sum_{a \in A_0, a \geq x}$ tends to $0$ as $x \to \infty$ — this is a standard result: the partial sums converge, so the tail (the remainder) must vanish. Hence:
$$\sum_{\substack{a \in A_0 \\ a \geq x}} \frac{1}{a \log a} \to 0. \qquad \square$$

**Application to the Erdős conjecture.** For a fixed primitive $A_0 \subseteq \mathbb{N}$ with $D(A_0) < \infty$, the theorem gives: the restricted primitive set $A_0 \cap [x, \infty)$ satisfies $\sum_{a \in A_0, a \geq x} 1/(a \log a) \to 0$ as $x \to \infty$. In particular, $A_0 \cap [x, \infty)$ satisfies the Erdős conjecture's bound $< 1 + o(1)$ for large $x$.

**Note on the varying-$A$ case.** The direct proofs of sparse\_stratum, linear\_density, polynomial\_density, and sub\_exponential\_density (Sections 10–13) prove the result for a VARYING family $A(x) \subseteq [x, \infty)$ — they work for any $A$ supported above $x$, not just restrictions of a fixed $A_0$. Theorem density\_convergence gives an alternative unified proof only for the FIXED-$A_0$ case.

**Corollary (all prior density lemmas as special cases).** The Theorem density\_convergence subsumes every proved density lemma via the following verifications that $D(A) < \infty$:
- **sparse\_stratum** ($|A \cap A_k| \leq 1$): $D(A) \leq \sum_{k \geq 1} 1/(k 2^k) < \infty$ (comparison: $1/(k 2^k) \leq 1/2^k$ for $k \geq 1$, and $\sum_{k \geq 1} 1/2^k = 1 < \infty$). ✓
- **linear\_density** ($|A \cap A_k| \leq k$): $D(A) \leq \sum_{k \geq 1} k/(k 2^k) = \sum_{k \geq 1} 1/2^k = 1 < \infty$ (geometric series). ✓
- **polynomial\_density** ($|A \cap A_k| \leq k^m$): $D(A) \leq \sum_{k \geq 1} k^{m-1}/2^k < \infty$ (ratio test, term ratio $\to 1/2$). ✓
- **sub\_exponential\_density** ($|A \cap A_k| \leq C^k$, $C < 2$): $D(A) \leq \sum_{k \geq 1} (C/2)^k/k \leq \sum_{k \geq 1} (C/2)^k = (C/2)/(1 - C/2) < \infty$ (geometric series, $C/2 < 1$). ✓

**Characterization of the density threshold.** The theorem gives a sharp necessary condition for the elementary approach:
$$\text{sum} \to 0 \text{ whenever } D(A) < \infty.$$
The open boundary is exactly $D(A) = \infty$, which occurs precisely when $|A \cap A_k|/(k 2^k)$ has divergent sum. For example, $|A \cap A_k| = 2^k$ gives $D(A) = \sum_{k \geq 1} 1/k = \infty$ (harmonic divergence).

**Connection to the conjecture.** For a primitive $A \subseteq [x, \infty)$, the density $|A \cap A_k|$ is constrained by the primitivity condition. However, the density alone (without primitivity structure) cannot give $D(A) < \infty$ when $|A \cap A_k| \sim 2^k$. The full conjecture asserts that primitivity provides additional constraints that force the sum $< 1 + o(1)$ even when $D(A) = \infty$ — this is precisely what the current elementary approach cannot prove.

**Updated cumulative proved results:**
1.–11. (see Sections 10–13)
12. `density_convergence`: $D(A) = \sum |A \cap A_k|/(k 2^k) < \infty \Rightarrow$ sum $\to 0$ — **proved** (Q19). All prior density lemmas (sparse, linear, polynomial, sub-exponential) are corollaries.

**Precise statement of the open case.** The Erdős primitive-set conjecture requires proving that for any PRIMITIVE $A \subseteq [x,\infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
even when $D(A) = \infty$. This is the genuinely open part: the conjecture's bound of $1 + o(1)$ must come from the joint constraint that $A$ is a primitive antichain AND elements are $\geq x$, not from density alone.

## Section 15: Classification Theorem (Q20)

### Theorem partial\_classification (PROVED)

We collect all proved cases into a three-tier classification.

**Tier 1 — Bounded-support (dyadic analysis, no ledger facts needed):**

| Class | Condition | Status | Bound |
|---|---|---|---|
| Single block | $A \subseteq [x, 2x)$ | **Proved** | $< \log 2/\log x \to 0$ |
| $K$-blocks | $A \subseteq [x, 2^K x)$ (fixed $K$) | **Proved** | $< K\log 2/\log x \to 0$ |
| Ratio-bounded | $A \subseteq [x, Mx)$ (fixed $M$) | **Proved** | $< \lceil\log_2 M\rceil\log 2/\log x \to 0$ |

**Tier 2 — Finite strata (F3 tail argument):**

| Class | Condition | Status | Bound |
|---|---|---|---|
| Single stratum | $A \subseteq A_k \cap [x,\infty)$ (fixed $k$) | **Proved** | tail of convergent series $\to 0$ |
| Finitely many strata | $A \subseteq \bigcup_{k \leq K} A_k \cap [x,\infty)$ (fixed $K$) | **Proved** | sum of $K$ tails $\to 0$ |
| Hybrid | near bounded + far $\leq K$ strata | **Proved** | both parts $\to 0$ |

**Tier 3 — Density convergence (elementary, no ledger facts needed):**

| Class | $\vert A \cap A_k\vert$ condition | $D(A)$ value | Status |
|---|---|---|---|
| Sparse | $\leq 1$ for all $k$ | $< \infty$ (comparison $\leq \sum 1/2^k = 1$) | **Proved** |
| Linear | $\leq k$ for all $k$ | $\leq 1$ (geometric) | **Proved** |
| Polynomial | $\leq k^m$ (fixed $m$) | $< \infty$ (ratio test) | **Proved** |
| Sub-exp. geometric | $\leq C^k$ (fixed $C < 2$) | $< \infty$ (geometric, $C/2 < 1$) | **Proved** |
| General convergence | $D(A) < \infty$ (any) | given | **Proved** |

**Open case (Tier 4):**

| Class | Condition | Status | Known bound |
|---|---|---|---|
| Full conjecture | Any primitive $A \subseteq [x,\infty)$ | **Open** | $< 1.399$ from F1 |

**Proof of the Theorem.** All Tier 1, 2, and 3 entries follow immediately from the cited lemmas in Sections 5–14. The Tier 4 open case: F1 gives $< 1.399$; proving $< 1 + o(1)$ for all primitive $A$ with $D(A) = \infty$ requires going beyond F1, F2, F3, and elementary density analysis. $\square$

**Formal statement of the partial result:**

*Theorem partial\_classification.* Let $A \subseteq [x,\infty)$ be a primitive set. The Erdős primitive-set conjecture ($\sum_{a \in A} 1/(a\log a) < 1 + o(1)$) holds in each of the following cases:
1. (**Tier 1**) $A \subseteq [x, Mx)$ for any fixed $M$ (bounded-support case).
2. (**Tier 2**) $A \subseteq \bigcup_{k=1}^K A_k \cap [x,\infty)$ for any fixed $K$ (finite-strata case).
3. (**Tier 3**) The density series $D(A) = \sum_{k \geq 1} \vert A \cap A_k\vert/(k \cdot 2^k)$ is finite (density-convergence case).

In all three cases the sum is in fact $o(1)$ (stronger than $< 1 + o(1)$). The open case is Tier 4: primitive $A$ with $D(A) = \infty$ that spans both infinitely many dyadic blocks and infinitely many strata.

**Gap requirement for Tier 4.** The primitive antichain constraint and the element-size lower bound together must force the sum $< 1 + o(1)$ in the $D(A) = \infty$ case. Neither F1 ($< 1.399$), nor F2 (unsigned big-O lower bound on strata), nor F3 (stratum asymptotics) alone is strong enough. The gap requires analytic prime-distribution estimates that quantify how the primitivity constraint limits the density $\vert A \cap A_k\vert$ across strata — facts not available from F1, F2, F3 and elementary calculus.

## Section 16: Count Bound (Q21)

### Lemma count\_bound (PROVED — one-line bound)

**Statement.** For any set $A \subseteq [x, \infty)$ with $N = |A|$ elements:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{N}{x \log x}.$$

**Proof.** Every $a \in A$ satisfies $a \geq x > e$, so $1/(a \log a) \leq 1/(x \log x)$ (since $t \mapsto t \log t$ is increasing for $t > e$). Summing over $N$ elements gives the bound. $\square$

**Corollary.** For any primitive $A \subseteq [x, \infty)$: the Erdős conjecture holds (sum $< 1 + o(1)$) whenever $N = |A| < (1 + o(1)) \cdot x \log x$.

**Tier 4 sub-case.** When $D(A) = \infty$ (Tier 4) but $|A| = N = N(x)$ is controlled: sum $\leq N/(x \log x)$. In particular:
- $N = o(x \log x)$: sum $\to 0$. The conjecture holds — this is the **moderate-count Tier 4** sub-case.
- $N \leq x$: sum $\leq 1/\log x \to 0$. (E.g., any primitive set confined to one dyadic block has $\leq x$ elements.)
- $N = O(x)$: sum $\leq C/\log x \to 0$ for any constant $C$.

**What count bound misses.** For the Erdős conjecture (sum $< 1 + o(1)$) to FAIL using the count bound alone, we would need $N \geq (1 + \varepsilon) x \log x$ for some $\varepsilon > 0$. No known construction of a primitive set in $[x, \infty)$ achieves $|A| \geq c \cdot x \log x$ — the densest known primitive sets (fat antichains in $[x, 2x)$) have $|A| \leq x$ elements. However, a primitive set spanning many dyadic blocks could in principle have $|A| = o(x \log x)$ elements whose sum still approaches 1, by concentrating on high-stratum elements with large individual contributions.

**Updated cumulative proved results:**
1.–12. (see Sections 10–15)
13. `count_bound`: $|A| = N \leq x \Rightarrow$ sum $\leq N/(x \log x) \leq 1/\log x \to 0$ — **proved** (Q21).

**Formal statement of the final open case.** The Erdős conjecture is open for primitive $A \subseteq [x,\infty)$ satisfying ALL of:
1. $D(A) = \infty$ (not Tier 3),
2. $|A| \geq c \cdot x \log x$ for some $c > 0$ (not covered by count\_bound),
3. $A$ spans infinitely many dyadic blocks (not Tier 1),
4. $A$ spans infinitely many $\Omega$-strata (not Tier 2).

Such $A$ must be simultaneously large (many elements), spread across scales, and dense in multiple strata — this is the genuine hardness of the open case.

## Section 17: Near-Extremal Growing-Stratum Analysis (Q22)

### Theorem near\_extremal\_stratum (PROVED — F3 + monotonicity)

**Statement.** Let $K : [2,\infty) \to \mathbb{Z}_{\geq 1}$ be any function with $K(x) \to \infty$ as $x \to \infty$. For each $x$, let $A(x) \subseteq A_{K(x)} \cap [x, \infty)$ be any primitive set. Then:
$$\sum_{a \in A(x)} \frac{1}{a \log a} \leq 1 - (c + o(1)) \frac{K(x)^2}{2^{K(x)}} < 1,$$
where the $o(1)$ is as $K(x) \to \infty$ (hence as $x \to \infty$), and $c \approx 0.0656 > 0$ is the constant from F3.

In particular, the sum is **strictly less than 1** for every $x$, and the Erdős conjecture bound $< 1 + o(1)$ holds. Moreover, the upper bound $1 - (c+o(1))K(x)^2/2^{K(x)}$ approaches $1$ from below as $K(x) \to \infty$, so this family is **near-extremal**: among all single-stratum primitive sets supported above $x$, those in $A_{K(x)}$ with $K(x)$ large are hardest (closest to the conjectured threshold of 1).

**Proof.** Since $A(x) \subseteq A_{K(x)}$ and all terms $1/(a\log a)$ are positive:
$$\sum_{a \in A(x)} \frac{1}{a \log a} \leq \sum_{a \in A_{K(x)}} \frac{1}{a \log a} = 1 - (c+o(1))\frac{K(x)^2}{2^{K(x)}} \quad (\text{by F3 applied to } k = K(x)).$$
Since $c > 0$ and $K(x)^2/2^{K(x)} > 0$, the right side is strictly $< 1$. As $K(x) \to \infty$, the correction $K(x)^2/2^{K(x)} \to 0$, so the bound approaches $1$ from below. $\square$

**Significance.** This resolves the near-extremal single-stratum case. Note the contrast with the FIXED-$k$ case (Theorem single\_stratum, Section 8): for fixed $k$, the tail sum $\sum_{a \in A_k,\, a \geq x} 1/(a\log a) \to 0$ as $x \to \infty$, so the bound is $o(1)$. For GROWING $K(x)$, the tail argument no longer applies (elements of $A_{K(x)}$ can be as small as $2^{K(x)}$, not necessarily $\geq x$). Instead, the full stratum bound (F3 applied to the ENTIRE stratum $A_{K(x)}$, not just its tail) gives the near-extremal result. The bound is $< 1$ but no longer $o(1)$.

**Near-extremal bound as $K(x) = \lfloor \log_2 x \rfloor$.**
The largest useful stratum is $K(x) = \lfloor \log_2 x \rfloor$: elements of $A_{K(x)}$ satisfy $a \geq 2^{K(x)} \approx x$, so $A_{K(x)} \cap [x,\infty)$ is genuinely non-empty. For this choice, the F3 bound gives:
$$\text{sum} \leq 1 - (c+o(1)) \frac{(\log_2 x)^2}{x}.$$
As $x \to \infty$, the correction $(\log_2 x)^2/x \to 0$, so the bound approaches $1$ polynomially slowly in $1/x$. This is the hardest single-stratum sub-case of Tier 2.

**Multi-stratum growing case (partial — cannot be closed from F3 alone).** For $A(x) \subseteq \bigcup_{k=1}^{K(x)} A_k \cap [x,\infty)$ with $K(x) \to \infty$:
$$\sum_{a \in A(x)} \frac{1}{a\log a} \leq \sum_{k=1}^{K(x)} \sum_{\substack{a \in A_k \\ a \geq x}} \frac{1}{a\log a}.$$
For any FIXED $k$, the inner sum $\to 0$ as $x \to \infty$ (F3 tail). But for GROWING $K(x)$, we sum $K(x)$ tails, each of which is small but the number of terms grows. A uniform bound requires knowing how fast each tail decays relative to $K(x)$. This cannot be closed from F3 alone without quantitative tail bounds — specifically, how fast $\sum_{a \in A_k,\, a \geq x} 1/(a\log a)$ decays as a function of both $k$ and $x$.

**Summary.** Theorem near\_extremal\_stratum closes all single-stratum cases (both fixed and growing $K(x)$). The multi-stratum growing case remains open and requires quantitative decay rates for the stratum tails — a gap that cannot be filled from F1/F2/F3 alone.

**Updated cumulative proved results:**
1.–13. (see Sections 10–16)
14. `near_extremal_stratum`: $A(x) \subseteq A_{K(x)} \cap [x,\infty)$, any $K(x) \to \infty$ $\Rightarrow$ sum $< 1$ — **proved** (Q22).

## Section 18: Polynomial-Range Explicit Bound (Q23)

### Theorem polynomial\_range (PROVED — multi\_block\_finite + calculus)

**Statement.** For any $\alpha \geq 1$ and any set $A \subseteq [x, x^\alpha)$ (not necessarily primitive):
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{\lceil (\alpha - 1) \log_2 x \rceil \cdot \log 2}{\log x}.$$
In particular:
1. **Sub-polynomial range** ($\alpha = 1 + t/\log_2 x$ for fixed $t$): sum $< t \log 2 / \log x + O(1/\log x) \to 0$.
2. **Quadratic range** ($\alpha = 2$, $A \subseteq [x, x^2)$): sum $< 1 + \log 2/\log x$.
   For $x \geq 6$: sum $< 1 + 0.387 \approx 1.387 < 1.399$, strictly better than F1.
3. **General power** ($\alpha > 1$ fixed): sum $< (\alpha - 1) + O(1/\log x)$.

**Proof.** Let $K = \lceil (\alpha-1) \log_2 x \rceil$. Then $2^K \cdot x \geq x^{\alpha-1} \cdot x = x^\alpha$, so $[x, x^\alpha) \subseteq [x, 2^K x)$. By Lemma multi\_block\_finite (Section 5) with parameter $x$ and $K$ blocks:
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{K \log 2}{\log x} = \frac{\lceil (\alpha-1) \log_2 x \rceil \cdot \log 2}{\log x}. \qquad \square$$

**Sharpness.** For $\alpha = 2$, the bound is $\lceil \log_2 x \rceil \cdot \log 2 / \log x$. Since $\log_2 x = \log x / \log 2$, this equals $\lceil \log x / \log 2 \rceil \cdot \log 2 / \log x \leq (\log x / \log 2 + 1) \cdot \log 2 / \log x = 1 + \log 2 / \log x$.

**Comparison with F1 (quadratic range).** For $A \subseteq [x, x^2)$:
$$\text{polynomial\_range bound:} \quad 1 + \frac{\log 2}{\log x}; \qquad \text{F1 bound:} \quad 1.399.$$
The polynomial\_range bound is strictly better than F1 when $\log 2 / \log x < 0.399$, i.e., $\log x > \log 2 / 0.399 \approx 1.74$, i.e., $x \geq 6$. For $x \geq 6$ and $A \subseteq [x, x^2)$ primitive:
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + \frac{\log 2}{\log x} \leq 1 + \frac{\log 2}{\log 6} < 1.387 < 1.399.$$

**Corollary (explicit conjecture form for quadratic range).** For any primitive $A \subseteq [x, x^2)$ and $x \geq 6$:
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + \frac{\log 2}{\log x}.$$
This is the Erdős conjecture $< 1 + o(1)$ with explicit error term $\log 2 / \log x$ — for the quadratic range, the conjecture holds and the proof is elementary (no F1, F2, F3 needed).

**Range comparison table:**

| Range | $\alpha$ | Blocks $K$ | Bound | vs.\ F1 |
|---|---|---|---|---|
| $[x, x^{1.1})$ | 1.1 | $\sim 0.1\log_2 x$ | $\sim 0.1$ | Stronger |
| $[x, 2x)$ | $1 + 1/\log_2 x$ | 1 | $\log 2/\log x \to 0$ | Stronger |
| $[x, x^2)$ | 2 | $\log_2 x$ | $1 + \log 2/\log x$ | Stronger ($x \geq 6$) |
| $[x, x^{2.4})$ | 2.4 | $1.4\log_2 x$ | $\sim 1.4$ | Weaker |
| $[x, \infty)$ | $\infty$ | (unbounded) | F1 = $1.399$ | F1 better |

**Updated cumulative proved results:**
1.–14. (see Sections 10–17)
15. `polynomial_range`: $A \subseteq [x, x^\alpha)$ (any $\alpha \geq 1$) $\Rightarrow$ sum $< (\alpha-1) + O(1/\log x)$; specifically for $\alpha = 2$ and $x \geq 6$: sum $< 1.387 <$ F1 — **proved** (Q23).

## Section 19: Shadow Structure and Cross-Stratum Exclusion (Q24)

### Lemma shadow\_structure (PROVED — elementary from primitivity definition)

**Definition.** For a primitive set $A$ and stratum index $k$, the **shadow of $A$ in stratum $k+1$** is:
$$\text{Sh}_k(A) = \{ p \cdot a : a \in A \cap A_k,\ p \text{ prime},\ p \nmid a \} \subseteq A_{k+1}.$$
Each element $pa$ has exactly $k+1$ prime factors (counting multiplicity): the $k$ factors of $a$ plus the new prime $p$.

**Statement.** For any primitive set $A$: $\text{Sh}_k(A) \cap A = \emptyset$ for every $k \geq 1$.

**Proof.** Suppose $b \in \text{Sh}_k(A) \cap A$. Then $b = pa$ for some $a \in A \cap A_k$ and prime $p \nmid a$. But $a \mid b$ and $a \neq b$ (since $p \geq 2$ so $b > a$), contradicting primitivity of $A$. $\square$

**Corollary (exclusion count).** For each $a \in A \cap A_k$, the elements $2a, 3a, 5a, 7a, \ldots$ (products with each prime not already dividing $a$) all lie in $A_{k+1}$ and are excluded from $A$. The number of excluded elements per $a$ is at least $\pi(x)$ (the number of primes $\leq x$) when $a \leq x$ (since $pa \leq x \cdot a$... [see gap analysis below]).

### Gap Analysis: Why Shadow Weight Cannot Be Bounded from F1/F2/F3 Alone

**What can be proved elementarily (without new analytic facts).**

1. *Exclusion existence*: For each $a \in A \cap A_k$ and prime $p \leq a$: the element $pa \in A_{k+1}$ is excluded from $A$. This is proved above.

2. *Exclusion count lower bound*: The number of excluded elements in $A_{k+1} \cap [a, a^2]$ from a single $a \in A_k$ is $\geq \pi(a) - \omega(a)$, where $\pi(a) = |\{p \leq a : p \text{ prime}\}|$ and $\omega(a)$ is the number of distinct prime factors of $a$. The subtracted term $\omega(a)$ accounts for primes already dividing $a$ (for which $pa$ would increase the multiplicity, not the number of prime factors).

3. *Structural constraint*: $A \cap A_{k+1} \subseteq A_{k+1} \setminus \text{Sh}_k(A)$. The shadow occupies a structured subset of $A_{k+1}$; its complement contains $A \cap A_{k+1}$.

**What elementary methods cannot prove.**

To bound $\sum_{b \in \text{Sh}_k(A) \cap [x,\infty)} 1/(b \log b)$ — the total WEIGHT excluded from $A_{k+1}$ — we need to know how many shadow elements $pa$ (with $a \geq x$) have large weight $1/(pa \log(pa))$. Summing over primes $p$:
$$\sum_{\substack{p \text{ prime}}} \frac{1}{pa \log(pa)} = \frac{1}{a} \sum_{p \text{ prime}} \frac{1}{p \log(pa)}.$$

This sum over primes is bounded below by $\sum_{p \leq a} 1/(p \log(a^2))$. Bounding $\sum_{p \leq a} 1/p$ from below requires an estimate on the sum of prime reciprocals — which is NOT derivable from F1 (an upper bound on the sum), F2 (a stratum lower bound), or F3 (an exact asymptotic for full stratum sums). The prime reciprocal sum is an INPUT to the proof, not an output.

**Summary: the shadow gap.**

The shadow structure is provable from the definition of primitivity. The shadow WEIGHT requires prime reciprocal sums, which go beyond F1/F2/F3. Specifically:

- The shadow imposes a *structural* constraint on $A \cap A_{k+1}$: it must avoid $\text{Sh}_k(A)$.
- Translating this into a *weight* constraint of the form $T_{k+1} \leq S_{k+1} - f(T_k)$ requires an analytic bound on $\sum_{p \leq x} 1/p$.
- Such a bound is not in the current given-facts ledger.

**What this means for the proof strategy.**

The shadow framework shows that primitivity creates genuine cross-stratum constraints — not just within each stratum independently. The obstacle is purely analytic: quantifying the excluded weight requires prime distribution estimates that lie outside F1/F2/F3. Adding such an estimate to the given-facts ledger would be the natural next step.

**Updated cumulative proved results:**
1.–15. (see Sections 10–18)
16. `shadow_structure`: $\text{Sh}_k(A) \cap A = \emptyset$ for any primitive $A$ — **proved** (Q24, elementary). Shadow weight bound requires prime reciprocal estimates outside F1/F2/F3; gap documented.

## Section 20: Slow-Growth Support Generalization (Q25)

### Theorem slow\_growth\_support (PROVED — multi\_block\_finite + calculus)

**Statement.** Let $M : [2, \infty) \to [1, \infty)$ be any function with $\log M(x) = o(\log x)$ (equivalently, $M(x) = x^{o(1)}$ — sub-polynomial growth). For any set $A \subseteq [x, M(x) \cdot x)$:
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{(\log_2 M(x) + 1) \log 2}{\log x} = \frac{\log M(x)}{\log x} + \frac{\log 2}{\log x} \to 0 \quad \text{as } x \to \infty.$$

In particular, the Erdős conjecture bound $< 1 + o(1)$ holds for all $A$ with sub-polynomial support growth.

**Proof.** Let $K = \lceil \log_2 M(x) \rceil$. Then $2^K \cdot x \geq M(x) \cdot x$, so $[x, M(x) \cdot x) \subseteq [x, 2^K x)$. By Lemma multi\_block\_finite with base $x$ and $K$ blocks:
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{K \log 2}{\log x} \leq \frac{(\log_2 M(x) + 1) \log 2}{\log x} = \frac{\log M(x) + \log 2}{\log x}.$$
Since $\log M(x) = o(\log x)$, this bound is $o(1) + O(1/\log x) = o(1)$. $\square$

**Examples:**

| $M(x)$ | Growth type | Bound | Sum behavior |
|---|---|---|---|
| Fixed $C$ | bounded (Thm bounded\_support) | $\frac{\lceil\log_2 C\rceil\log 2}{\log x}$ | $O(1/\log x)$ |
| $(\log x)^C$ | polylogarithmic | $\frac{C\log\log x}{\log x}$ | $o(1)$ |
| $\exp(\sqrt{\log x})$ | sub-exponential | $\frac{\sqrt{\log x}}{2\log x}$ | $o(1)$ |
| $x^{1/\log\log x}$ | sub-polynomial | $\frac{1}{\log\log x}$ | $o(1)$ |
| $x^c$ (fixed $c > 0$) | polynomial | $c + O(1/\log x)$ | NOT $o(1)$ |

The last row ($M(x) = x^c$) is covered by Theorem polynomial\_range (Q23), not this theorem: $\log M(x) = c \log x$ is NOT $o(\log x)$.

**Relation to prior results:**
- **Theorem bounded\_support** (Section 7): $M(x) = M$ fixed. Special case of this theorem.
- **Theorem polynomial\_range** (Section 18): $M(x) = x^{\alpha-1}$ (so $A \subseteq [x, x^\alpha)$). Gives sum $< (\alpha-1) + o(1)$; for $\alpha = 2$, sum $< 1 + o(1)$.
- **This theorem**: $M(x) = x^{o(1)}$ (slower than any power of $x$). Gives sum $= o(1)$.

**Updated support-growth classification:**

| $M(x)$ growth | Sum behavior | Theorem |
|---|---|---|
| $M$ constant | $O(1/\log x) = o(1)$ | bounded\_support |
| $M(x) = x^{o(1)}$ | $o(1)$ | slow\_growth\_support (Q25) |
| $M(x) = x^{\alpha-1}$ (fixed $\alpha > 1$) | $< (\alpha-1) + o(1)$ | polynomial\_range |
| $M(x) = x$ (full range) | $< 1.399$ (F1) | full conjecture (OPEN) |

The "phase transition" occurs at polynomial growth $M(x) = x^c$: below that, sum $= o(1)$; above (polynomial M), the bound exceeds 0.

**Corollary (union of both theorems).** For any $A \subseteq [x, \infty)$ and any $1 \leq \alpha(x) \leq 2$:
- If $A \subseteq [x, x^{\alpha(x)})$ and $\alpha(x) \to 1$ (sub-polynomial range): sum $\to 0$.
- If $A \subseteq [x, x^{\alpha(x)})$ and $\alpha(x) \to 2$ (approaching quadratic range): sum $< 1 + o(1)$.

For $1 \leq \alpha(x) < 2$, the explicit bound is $\alpha(x) - 1 + o(1)$. For $\alpha(x) = 2$: sum $< 1 + \log 2/\log x$.

**Updated cumulative proved results:**
1.–16. (see Sections 10–19)
17. `slow_growth_support`: $A \subseteq [x, M(x)x)$ with $M(x) = x^{o(1)}$ $\Rightarrow$ sum $= o(1)$ — **proved** (Q25).

## Section 21: Quadratic Range Conjecture and Refined Open Case (Q26)

### Theorem quadratic\_range\_conjecture (PROVED — see integral\_bound, Section 22)

**Statement.** For any set $A \subseteq [x, x^2)$ (regardless of whether primitive):
$$\sum_{a \in A} \frac{1}{a \log a} \leq \log 2 + \frac{1}{x \log x} < 1 \quad \text{for all } x \geq 3.$$
In particular, the Erdős primitive-set conjecture holds for every primitive $A \subseteq [x, x^2)$ with the stronger bound sum $< 1$ (not just $< 1 + o(1)$).

**Proof.** Apply Theorem integral\_bound (Section 22) with $C = 2$: sum $\leq \log 2 + 1/(x\log x)$. For $x \geq 3$: $1/(x\log x) < 1/(3\log 3) \approx 0.303$ and $\log 2 + 0.303 \approx 0.996 < 1$. For all $x \geq 3$: sum $\leq \log 2 + 1/(x\log x) < 1$. $\square$

**Note.** An earlier version of this section used the cruder bound $< 1 + \log 2/\log x$ from polynomial\_range (Q23). The sharper integral\_bound (Q27) gives the exact bound $\log 2 \approx 0.693 < 1$, proving the conjecture with a strict constant (not just $1 + o(1)$).

### Precise statement of the remaining open case

After Q22–Q26, the Erdős conjecture is proved for:
1. All $A \subseteq [x, M(x) x)$ with $M(x) = x^{o(1)}$ (sum $= o(1)$, Theorem slow\_growth\_support).
2. All $A \subseteq [x, x^\alpha)$ for any $1 \leq \alpha \leq 2$ (sum $< (\alpha-1) + O(1/\log x)$; for $\alpha = 2$: conjecture holds).
3. All $A \subseteq A_{K(x)} \cap [x,\infty)$ with $K(x) \to \infty$ (sum $< 1$, Theorem near\_extremal\_stratum).
4. All $A$ with $D(A) < \infty$ (sum $\to 0$, Theorem density\_convergence).
5. All $A$ with $|A| = o(x\log x)$ (sum $\to 0$, Lemma count\_bound).

**The refined open case.** The Erdős conjecture is now open only for primitive $A \subseteq [x, \infty)$ satisfying ALL of:
1. $A$ has elements above $x^2$ (otherwise covered by case 2 above with $\alpha = 2$).
2. $D(A) = \infty$ (otherwise density\_convergence applies).
3. $|A| \geq c \cdot x \log x$ for some $c > 0$ (otherwise count\_bound applies).
4. $A$ spans infinitely many strata $A_k$ (otherwise multi\_stratum applies).

**Such $A$ must span the super-quadratic range $[x, \infty)$ with elements above $x^2$.** The best known bound for this case is F1 (sum $< 1.399$); the conjecture claims sum $< 1 + o(1)$.

### The F1 gap in the super-quadratic range

For $A \subseteq [x, x^C)$ with $2 < C \leq 1+1.399 = 2.399$: polynomial\_range gives sum $< (C-1) + O(1/\log x) < 1.399 = $ F1 (better than F1 when $C < 2.399$). For $C > 2.399$: F1 is tighter.

The **effective threshold** where polynomial\_range no longer beats F1 is $C = 2.399$, i.e., $A \subseteq [x, x^{2.399})$. Beyond that, only F1's $1.399$ bound is available.

**Range classification:**

| Range | Best known bound | Status vs.\ conjecture |
|---|---|---|
| $A \subseteq [x, M(x)x)$, $M = x^{o(1)}$ | sum $\to 0$ | **Proved** ($\gg$ conjecture) |
| $A \subseteq [x, x^2)$ | sum $\leq \log 2 + 1/(x\log x) < 1$ | **Proved** (conjecture holds strictly) |
| $A \subseteq [x, x^{2.399})$ | sum $< 1.399 - \varepsilon$ | Polynomial\_range better than F1 |
| $A \subseteq [x, x^{2.399})$ to $[x,\infty)$ | sum $< 1.399$ (F1) | Open (F1 only) |

**Updated cumulative proved results:**
1.–17. (see Sections 10–20)
18. `quadratic_range_conjecture`: conjecture proved for all $A \subseteq [x, x^2)$ with strict bound $\leq \log 2 + 1/(x\log x) < 1$ for $x \geq 3$ — **proved** (Q26; sharpened by integral\_bound Q27).

## Section 22: Sharp Integral Bound and Natural Logarithm Range (Q27)

### Theorem integral\_bound (PROVED — direct comparison, no ledger facts)

The key insight: $1/(t \log t)$ is decreasing for $t > e$, so the sum over any subset of $[x, x^C)$ is bounded by the integral.

**Statement.** For any $C \geq 1$ and any set $A \subseteq [x, x^C)$ (not necessarily primitive, $x \geq 3$):
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{n=x}^{\lfloor x^C \rfloor} \frac{1}{n \log n} \leq \frac{1}{x \log x} + \int_x^{x^C} \frac{dt}{t \log t} = \frac{1}{x \log x} + \log C.$$

**Proof.** Since $f(t) = 1/(t \log t)$ is decreasing for $t > e$ (and $x \geq 3 > e$), we have $f(n) \leq f(n-1)$ for all $n \geq x+1$. By the standard comparison for decreasing functions: $\sum_{n=x}^{N} f(n) \leq f(x) + \int_x^N f(t)\,dt$. With $N = \lfloor x^C \rfloor$ and the antiderivative $\int 1/(t\log t)\,dt = \log \log t$:
$$\int_x^{x^C} \frac{dt}{t \log t} = \log(\log(x^C)) - \log(\log x) = \log\!\left(\frac{C \log x}{\log x}\right) = \log C.$$
Since $A \subseteq [x, x^C)$, each term in $\sum_{a \in A} 1/(a\log a)$ appears in $\sum_{n=x}^{\lfloor x^C\rfloor} 1/(n\log n)$, giving the chain of inequalities. $\square$

**Corollary (conjecture for natural-logarithm range).** For any primitive $A \subseteq [x, x^e)$ where $e \approx 2.718$ is Euler's number:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \log e + \frac{1}{x \log x} = 1 + \frac{1}{x \log x}.$$
This is strictly less than $1 + o(1)$ as $x \to \infty$ — the Erdős conjecture holds for all $A \subseteq [x, x^e)$.

**Comparison table:**

| Range | integral\_bound | polynomial\_range (Q23) | F1 |
|---|---|---|---|
| $[x, x^2)$ | $\log 2 \approx 0.693$ | $1 + O(1/\log x)$ | $1.399$ |
| $[x, x^e)$ | $1 + O(1/(x\log x))$ | $e-1+o(1) \approx 1.718$ | $1.399$ |
| $[x, x^3)$ | $\log 3 \approx 1.099$ | $2 + o(1)$ | $1.399$ |
| $[x, x^4)$ | $\log 4 \approx 1.386$ | $3 + o(1)$ | $1.399$ |
| $[x, x^{e^{1.399}}) \approx [x, x^{4.05})$ | $\approx 1.399$ | $3.05$ | $1.399$ |
| $[x, x^C)$, $C > e^{1.399}$ | $\log C > 1.399$ | $C-1$ | $1.399$ |

The integral\_bound strictly dominates both polynomial\_range and F1 for all $C \leq e^{1.399} \approx 4.05$. For $C > 4.05$, F1 becomes the tighter known bound.

**Why integral\_bound supersedes polynomial\_range.** Polynomial\_range uses the block-maximum bound $1/(a\log a) \leq 1/(2^{j-1}x \log(2^{j-1}x))$ uniformly within each dyadic block, then sums $K$ blocks. This loses the fact that terms decrease within and across blocks. The integral bound uses the actual decreasing profile of $1/(t \log t)$ without block decomposition, giving the tight bound $\log C$ vs.\ $C - 1$ (and $\log C < C-1$ for all $C > 1$).

**Refined open case after Q27.** The Erdős conjecture is now proved for:
- All $A \subseteq [x, x^e)$ (from integral\_bound with $C = e$): sum $< 1 + o(1)$. ✓
- All $A$ with $D(A) < \infty$ (density\_convergence): sum $= o(1)$. ✓
- All $A$ with $|A| = o(x\log x)$ (count\_bound): sum $= o(1)$. ✓

**Remaining open case.** Primitive $A \subseteq [x, \infty)$ with elements above $x^e$ AND $D(A) = \infty$ AND $|A| \geq c \cdot x\log x$. The best known bound for this case is F1 ($< 1.399$), with polynomial improvement possible for $A \subseteq [x, x^C)$ with $C \leq e^{F1} \approx 4.05$ (integral\_bound $< 1.399$). For $C > 4.05$ or unbounded range: only F1 is available.

**Updated cumulative proved results:**
1.–18. (see Sections 10–21)
19. `integral_bound`: $A \subseteq [x, x^C) \Rightarrow$ sum $\leq \log C + O(1/(x\log x))$; conjecture proved for $C \leq e$ — **proved** (Q27). Supersedes polynomial\_range and beats F1 for $C \leq e^{1.399}$.

## Section 23: Same-Stratum Primitive Sets and Near-Extremal Analysis (Q28)

### Lemma same\_stratum\_primitive (PROVED — elementary from $\Omega$ function)

**Statement.** For any fixed $k \geq 1$, the entire stratum $A_k = \{n : \Omega(n) = k\}$ is itself a primitive set: no element of $A_k$ divides a distinct element of $A_k$.

**Proof.** Suppose $a, b \in A_k$ with $a \neq b$ and $a \mid b$. Then $b = am$ for some integer $m > 1$. Since $m > 1$, $\Omega(m) \geq 1$. By the additivity of $\Omega$: $\Omega(b) = \Omega(am) = \Omega(a) + \Omega(m) \geq k + 1 > k$. But $b \in A_k$ requires $\Omega(b) = k$. Contradiction. $\square$

**Corollary (maximal same-stratum sum).** For any primitive $A \subseteq A_k$ (not necessarily restricted to $[x,\infty)$):
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k} < 1.$$
The maximum is achieved by $A = A_k$ itself (the full stratum), which is the densest primitive set concentrated in a single stratum.

### Near-Extremal Analysis

**What approaches sum 1?** By F3, $\sum_{A_k} 1/(a\log a) \to 1$ as $k \to \infty$. For $K(x) = \lfloor \log_2 x \rfloor$:
$$\sum_{a \in A_{K(x)}} \frac{1}{a \log a} = 1 - (c+o(1))\frac{(\log_2 x)^2}{x} \to 1.$$
Elements of $A_{K(x)}$ satisfy $a \geq 2^{K(x)} \approx x$. So the densest near-extremal primitive set in $[x, \infty)$ has all elements concentrated in stratum $K(x) \approx \log_2 x$ and its sum approaches $1$ from below.

**All same-stratum primitive sets satisfy the conjecture.** For any $k$ (fixed or growing with $x$) and any primitive $A \subseteq A_k \cap [x, \infty)$: by stratum\_bound (Section 3), sum $\leq \sum_{A_k} 1/(a\log a) = 1 - (c+o(1))k^2/2^k < 1$. The conjecture holds strictly (sum $< 1 < 1+o(1)$).

### The Genuine Open Obstruction: Cross-Stratum Combinations

**What remains open.** Any SINGLE-STRATUM primitive set satisfies sum $< 1$ (proved above). The conjecture remains open only for CROSS-STRATUM primitive sets: those with elements in $\bigcup_{k \in S} A_k$ for an INFINITE set $S$ of stratum indices.

**Why cross-stratum is hard.** For $A \subseteq A_{k_1} \cup A_{k_2}$ (two distinct strata, $k_1 < k_2$):
- Elements of $A \cap A_{k_1}$ and $A \cap A_{k_2}$ can be related by divisibility (an element of $A_{k_1}$ can divide an element of $A_{k_2}$: e.g., $6 \in A_2$ divides $6 \cdot p \in A_3$ for any prime $p$). Primitivity forbids such pairs from both being in $A$.
- By stratum\_bound: sum $\leq \sum_{A_{k_1}} + \sum_{A_{k_2}} < 2$. This is worse than F1 = 1.399.
- For finitely many strata (fixed $k_1, \ldots, k_m$) and $x \to \infty$: multi\_stratum (Section 8) gives sum $= o(1)$.
- For growing or infinitely many strata: the current proof methods give only F1 $< 1.399$.

**Updated classification — what is and is not proved:**

| Primitive set type | Condition | Sum bound | Status |
|---|---|---|---|
| Single stratum (any $k$) | $A \subseteq A_k$ | $< 1$ | **Proved** (Q28) |
| Finitely many strata (fixed $K$) | $A \subseteq \bigcup_{k \leq K} A_k$ | $= o(1)$ | **Proved** (Q13) |
| Elements in $[x, x^e)$ | $A \subseteq [x, x^e)$ | $< 1 + o(1)$ | **Proved** (Q27) |
| Cross-stratum, elements in $[x, x^e)$ | both conditions | $< 1 + o(1)$ | **Proved** |
| Cross-stratum, elements in $[x^e, \infty)$ | $D(A) = \infty$, infinite strata | $< 1.399$ | **Open** (only F1) |

**The minimal open case.** A primitive $A \subseteq [x, \infty)$ with elements in strata $k_1 < k_2 < \ldots$ (infinitely many, all $k_i \to \infty$) and elements above $x^e$ in at least one stratum $k_j > e\log_2 x$. No elementary argument handles this case; F1 = 1.399 is the only known bound.

**Updated cumulative proved results:**
1.–19. (see Sections 10–22)
20. `same_stratum_primitive`: $A_k$ is itself primitive; any primitive $A \subseteq A_k$ has sum $< 1$ — **proved** (Q28, elementary). Cross-stratum infinite-strata case is the sole remaining open obstruction.

## Section 24: C=e Specialization and Open Case Summary (Q30)

**Theorem upper\_at\_e (PROVED).** For primitive $A \subseteq [x, x^e)$: sum $\leq 1 + 1/(x \log x)$.

**Proof.** Integral\_bound (Section 22) with $C = e$: sum $\leq \log e + 1/(x \log x) = 1 + 1/(x \log x)$. $\square$

This proves the Erdős conjecture for $A \subseteq [x, x^e)$ with explicit $o(1) = 1/(x \log x)$.

**The integral technique barrier.** For $C > e$, integral\_bound gives $\log C > 1$. The technique does not use primitivity (bounds any subset, not just primitive ones). To improve for primitive $A$ requires counting excluded multiples: $\lfloor x^C/a \rfloor$ over $a \in A$, which requires bounding $\sum_{a \in A} 1/a$ — a Mertens-type estimate outside F1/F2/F3.

**Open case after Q30.** Primitive $A \subseteq [x, \infty)$ with elements above $x^e$, $D(A) = \infty$, infinitely many strata. Best known bound: F1 ($< 1.399$).

**Updated cumulative proved results:**
1.–20. (see Sections 10–23)
21. `upper_at_e`: sum $\leq 1 + 1/(x\log x)$ for primitive $A \subseteq [x, x^e)$ — **proved** (Q30). Super-exponential range is sole remaining open case.

## Section 25: Synthesis Theorem and Counterexample Structure (Q31)

### Theorem conjecture\_for\_all\_elementary\_cases (PROVED)

**Statement.** The Erdős primitive-set conjecture (sum $< 1 + o(1)$ as $x \to \infty$) is proved for every primitive $A \subseteq [x, \infty)$ satisfying at least one of the following:

(a) $A \subseteq [x, x^e)$ — covered by `upper_at_e` (Q30), sum $\leq 1 + 1/(x\log x)$.
(b) $A \subseteq [x, Mx)$ for any fixed $M \geq 2$ — covered by `bounded_support` (Q12), sum $\to 0$.
(c) $A \subseteq \bigcup_{k \leq K} A_k$ for any fixed $K$ — covered by `single_stratum` + `multi_stratum` (Q13), sum $\to 0$.
(d) $D(A) = \sum_k |A \cap A_k|/(k 2^k) < \infty$ — covered by `density_convergence` (Q19), sum $\to 0$.
(e) $A \subseteq [x, M(x)x)$ with $M(x) = x^{o(1)}$ — covered by `slow_growth_support` (Q25), sum $= o(1)$.
(f) $A \subseteq A_k$ for any single stratum — covered by `same_stratum_primitive` + F3 (Q28), sum $< 1$.

**Proof.** Each case is proved in the section cited above. $\square$

### Characterization of Any Potential Counterexample

**Theorem counterexample\_structure (PROVED — by exclusion).** If the Erdős conjecture is false, then any counterexample $A \subseteq [x, \infty)$ (with sum $\geq 1 + \varepsilon$ for some fixed $\varepsilon > 0$ as $x \to \infty$) must simultaneously satisfy:

1. **Super-exponential elements**: $A$ has elements above $x^e$ (otherwise case (a) applies).
2. **Infinite extent**: $A$ is not confined to any $[x, Mx)$ with fixed $M$ (otherwise case (b)).
3. **Infinite strata**: $A$ spans infinitely many strata $A_k$ (otherwise case (c)).
4. **Dense strata**: $D(A) = \infty$ (otherwise case (d)).
5. **Super-polynomial extent**: $A$ is not in any $[x, x^{o(1)} x)$ (otherwise case (e)).
6. **Cross-stratum**: $A$ is not confined to a single stratum (otherwise case (f)).

**Proof.** By contrapositive: if any condition fails, one of the proved theorems (a)–(f) applies and the conjecture holds. $\square$

**Consequence.** A counterexample must be an "infinitely spread out" primitive set: elements at all scales above $x^e$, in infinitely many strata, with divergent density series. No elementary argument handles this case.

**Updated cumulative proved results:**
1.–21. (see Sections 10–24)
22. `conjecture_for_all_elementary_cases`: Erdős conjecture proved for cases (a)–(f) above — **proved** (Q31, synthesis). Any counterexample must be cross-stratum, super-exponential, $D = \infty$.
