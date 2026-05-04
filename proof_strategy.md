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

**Within each stratum.** F1 bounds the total; F3 identifies the extremal
stratum's structure. For large $k$, all elements of $A_k$ have at least $k$
prime factors (counted with multiplicity), forcing them to be large; each
individual term $1/(a \log a)$ is therefore small. Whether the entire
stratum $S_k(A)$ is bounded by an effective constant — independent of the
choice of primitive $A$ — is part of what the proof must establish.

**Key observation on within-stratum primitivity.** If $\Omega(a) = \Omega(b) = k$
and $a | b$ with $a \neq b$, then $b/a$ would have $\Omega(b/a) = 0$, forcing
$b/a = 1$, a contradiction. Therefore any collection of distinct integers
sharing a fixed $\Omega$ value is automatically primitive — no additional
constraint is imposed within a single stratum. The primitive-set condition
is entirely a cross-stratum condition.

**Cross-stratum interaction (main obstacle).** When $A$ contains elements
from multiple strata simultaneously, the primitive-set constraint (no element
divides another) imposes correlations that are hard to exploit analytically.
Specifically, if $a \in A_1$ (a prime $p$) and $b \in A_2$ with $p | b$,
then $b \notin A$. This exclusion reduces $A_2$'s density but may leave other
large-$\Omega$ elements unconstrained. Quantifying the net effect on the sum
via only F1/F2/F3 has not been accomplished; the cross-stratum term remains
the key obstacle.

**Lemma structure (Q5 in progress)**: Two lemma files are filed:
- Lemma `within_stratum` (`proof_lemmas/lemma_within_stratum.md`, status: open):
  shows within-stratum primitivity is vacuous (all same-$\Omega$ sets are
  automatically primitive); the relevant constraint is cross-stratum.
- Lemma `cross_stratum` (`proof_lemmas/lemma_cross_stratum.md`, status: open):
  the core open problem — bounding the total sum using inter-stratum
  divisibility exclusions; this is essentially the full conjecture.

**Lemma `single_stratum_bound`** (`proof_lemmas/lemma_single_stratum_bound.md`, status: open):
For any $A \subset \{n: \Omega(n)=k, n \geq 2\}$, positivity of terms gives
$\sum_{a \in A} 1/(a \log a) \leq \sum_{n:\Omega(n)=k} 1/(n \log n)$.
By F3 (ledger), this full-stratum sum equals $1-(c+o(1))k^2/2^k$ with $c > 0$.
F3's sign disambiguation confirms the result is $< 1$. Therefore:
**the conjecture holds for all single-stratum primitive sets.**

**Summary of partial results to date** (using only F1/F2/F3 from the ledger):
(a) F1 gives global ceiling $\approx 1.399$ for any primitive set.
(b) F3 shows the canonical full-stratum sum approaches 1 from below.
(c) F2's stratum bound is unsigned; it cannot establish any particular sum $> 1$.
(d) Lemma `within_stratum`: primitivity within a single stratum is vacuous;
    the primitive-set condition is entirely inter-stratum.
(e) Lemma `single_stratum_bound`: the conjecture holds for any primitive set
    confined to a single $\Omega$-stratum (proved via F3 + positivity).
(f) Witness search at $x_\text{floor} \in \{100, 1000, 10000\}$ found no
    counterexample with rigorous lower bound $> 1.0$.

**Remaining gap**: multi-stratum primitive sets. Summing the F3 bounds over
all strata gives $\sum_{k \geq 1}(1-(c+o(1))k^2/2^k)$, which diverges (the
$\sum_k 1$ part alone diverges). So the inter-stratum constraint cannot be
discarded; it must contribute enough sparsity to keep the total below 1.
Quantifying this constraint with F1/F2/F3 alone has not been accomplished.

### Section 4 — Barrier for Multi-Stratum Case

**The structural barrier.** The single-stratum proof (Lemma `single_stratum_bound`)
does not compose: if $A$ draws from $k_1 < k_2 < \ldots$, we cannot separately
bound $S_{k_i}(A)$ by $1$ and sum, since the sum of infinitely many near-$1$
terms diverges.

**What inter-stratum exclusion gives.** The primitive-set condition says:
for $a \in A_j$ and $b \in A_k$ with $j < k$, $a \nmid b$. This means
elements of lower strata block certain elements of higher strata. For example,
if $p \in A_1$ is a prime, then $p \cdot q \notin A$ for any prime $q$
(it would have $\Omega = 2$ and be divisible by $p$). So adding $p$ to $A$
blocks an infinite family from $A_2$. Each such exclusion reduces $S_{k}(A)$.

**Obstacle.** Making the above exclusion argument quantitative — showing the
blocked mass in each stratum is large enough to keep $\sum_k S_k(A) \leq 1$
— requires estimates on how many elements of each stratum are excluded, and
how much they contribute to the sum. This requires analytic estimates on
multiplicative structure that go beyond what F1/F2/F3 directly provide.

This sub-problem remains open. It is the central unsolved part of the
conjecture and has not been resolved here.

**Two-stratum sub-case (Q7, in progress)**: As a stepping stone, Lemma
`two_stratum` (`proof_lemmas/lemma_two_stratum.md`, status: open) analyzes
the case where $A$ draws from exactly two strata $j < k$. The naive sum of
F3 bounds gives $\leq (1 - \delta_j) + (1 - \delta_k) \approx 2$, far from
the conjectured $\leq 1$. The inter-stratum exclusion must supply the missing
mass. Quantifying the excluded sum $E_{j,k}(a)$ for each $a \in A_j$ requires
F3-style estimates for restricted stratum sums — a variant not in the ledger.

This remains open.
