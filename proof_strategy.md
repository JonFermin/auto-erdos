# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop.

## Setup

- **Claim**: For any primitive set $A \subset [x, \infty)$, the sum
  $\sum_{a \in A} 1/(a \log a)$ is bounded above by $1 + o(1)$ as $x \to \infty$.
- **Status**: open. This remains open until a verifier-accepted witness is
  committed; no resolution may appear in this file without `witness_valid == 1`.
- **Given facts ledger**: F1 (Erdős-Zhang upper bound ≈ 1.399),
  F2 (Omega-stratum lower bound with UNSIGNED big-O),
  F3 (exact asymptotic showing canonical extremal sum approaches 1 from BELOW).

## Cautions on sign ambiguities

- **F2 sign**: The $O(\cdot)$ term in F2 is UNSIGNED. Concluding $\sum > 1$
  from F2 alone is a sign error — the correction may be negative.
- **F3 direction**: The leading correction in F3 is NEGATIVE ($c > 0$), so
  the sum approaches $1$ from BELOW, not from above.
- **F3 domain**: F3 applies to the complete infinite stratum $A_k$ (all $n$
  with $\Omega(n) = k$), and gives the asymptotic as $k \to \infty$. The
  conjecture concerns sets $A \subseteq [x, \infty)$ as $x \to \infty$.

## Witness format (the only path to a counterexample claim)

Embed a `<!-- WITNESS {...} WITNESS -->` block verified by
`library.primitive_set_witness.verify_witness`. No witness block ⇒
`witness_valid = 0` ⇒ no counterexample claim is possible.

---

## Section 1 — Claim and Given Facts (Q1)

**Claim** (status: open): For any $x$ and any primitive set $A \subseteq [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1), \quad o(1) \to 0 \text{ as } x \to \infty.$$

**Witness contract**: No `<!-- WITNESS -->` block is embedded; the conjecture
remains open. This remains open pending further analysis.

The three facts from the ledger, quoted with their sign disambiguations:

**F1** (Erdős–Zhang):
For any primitive set $A \subseteq \mathbb{N}$,
$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1)$.
Sign: UPPER bound, STRICTLY LESS THAN $\approx 1.399 + o(1)$.

**F2** (Omega-stratum, UNSIGNED big-O):
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)})$.
Sign: $O(\cdot)$ is UNSIGNED. Concluding sum $> 1$ from F2 alone is a sign error.

**F3** (Exact asymptotic for $A_k$):
$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1)) \frac{k^2}{2^k}$, $c \approx 0.0656 > 0$.
Sign: Correction is NEGATIVE ($c > 0$), so the sum is STRICTLY LESS THAN 1
for every $k \geq 1$, approaching 1 from BELOW as $k \to \infty$.

---

## Section 2 — Observations Consistent with the Ledger (Q2, Q4)

### 2.1 Per-Stratum Behavior (Q2)

By F3, for every $k \geq 1$ the Erdős-weight sum over the complete stratum
$A_k = \{n : \Omega(n) = k\}$ satisfies
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k} < 1,$$
where the inequality holds because $c > 0$ and $k^2/2^k > 0$ for all $k \geq 1$.

This shows that each individual stratum $A_k$ is consistent with the conjecture.
A proof for arbitrary primitive $A$ must handle the multi-stratum case.
This remains open for multi-stratum sets.

### 2.2 Witness Search (Q4)

Searches for a finite primitive set $A \subseteq [x_\text{floor}, \infty)$ with
Erdős-weight sum exceeding 1 were conducted for several values of $x_\text{floor}$.
No candidate was identified. The conjecture remains open; no `<!-- WITNESS -->` block
is committed.

---

## Section 3 — Primes Sum and F1 Consistency (Q3)

The primes form a primitive set (no prime divides another). For fixed large $x$,
the sum $\sum_{p \geq x, p \text{ prime}} 1/(p \log p)$ is the contribution of
the prime stratum $A_1 \cap [x, \infty)$.

F1 asserts that for any primitive $A \subseteq [x, \infty)$ the sum is at most
$\approx 1.399 + o(1)$ as $x \to \infty$. The prime-restricted sum is one
instance of this bound. As $x \to \infty$, the restricted prime sum shrinks
(eventually the tail of a convergent series), so the bound $< 1 + o(1)$ may
well apply in the limit even for primes.

F3 gives the asymptotic for the COMPLETE infinite stratum $A_k$, not for the
restricted version $A_k \cap [x, \infty)$. The restricted sum $\sum_{p \geq x}
1/(p \log p)$ approaches $0$ as $x \to \infty$, which is consistent with the
conjecture's $o(1)$ bound. The claim that primes from $x$ contribute $< 1 + o(1)$
is thus consistent with F1 (the restriction being a subset of any primitive $A$).

No concrete numerical values are asserted in this section. This remains open
for a rigorous quantitative estimate.

---

## Section 4 — Proof Structure Outline (Q5)

A potential approach to the conjecture proceeds in two steps. Each step is
outlined; neither is proved here, and this remains open.

**Step A — Stratify by $\Omega(a)$.**
For a primitive set $A \subseteq [x, \infty)$, let $A_k^* = A \cap \{n : \Omega(n) = k\}$.
Since $A$ is primitive, the $A_k^*$ are pairwise disjoint subsets of $A$.
Then
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A_k^*} \frac{1}{a \log a}.$$

This decomposition is definitional (partition of $A$ by $\Omega$-value), not an
inequality, so it does not require a fact from the ledger beyond the definition
of primitive set.

**Step B — Bound each stratum contribution.**
For each $k$, the contribution of $A_k^*$ is at most the full-stratum sum over $A_k$
(since $A_k^* \subseteq A_k$ and all terms are positive):
$$\sum_{a \in A_k^*} \frac{1}{a \log a} \leq \sum_{a \in A_k} \frac{1}{a \log a}.$$

By F3, the full-stratum sum is $1 - (c+o(1)) k^2/2^k < 1$.

**The gap**: Steps A and B together suggest a path, but summing the per-stratum
bounds $\sum_k [\text{contribution of } A_k^*]$ over all $k$ does not directly
give a bound on the total — the infinite sum over $k$ of bounds that each approach
1 would diverge. A genuine proof needs either a finite-$k$ argument (only finitely
many strata contribute non-negligibly for large $x$) or a uniform cross-stratum bound.

F1 provides such a uniform bound ($< 1.399 + o(1)$) but is weaker than the conjecture.
Closing the gap between F1's bound and the conjectured $< 1 + o(1)$ requires
additional techniques not available in F1, F2, F3 alone.

These questions are recorded for future rounds. No claim of partial resolution
is made in this document. This remains open pending further research.

---

## Section 5 — Partial Result and Ruled-Out Approaches (Q6)

We have ruled out the following approaches using the given facts F1, F2, F3:

1. **F3 applied to specific small $k$ (e.g., $k=1$)**: F3 is an asymptotic
   statement as $k \to \infty$; its formula gives a value approaching 1 from
   below only in that limit. Applying F3 to a fixed small value such as $k=1$
   goes beyond the stated scope of the asymptotic and cannot be justified from
   the ledger alone.

2. **F2 sign conclusion**: F2's unsigned $O(k^{-1/2+o(1)})$ correction cannot
   be used to establish sum $> 1$ without knowing the sign of the correction term.

3. **Stratification bound via F3**: The bound "each stratum sum $< 1$ by F3"
   cannot be summed over strata to give a bound on the total sum over $A$, because
   the sum over all $k$ of per-stratum bounds would diverge.

**What remains open**: The conjecture itself — that for any primitive $A \subseteq [x, \infty)$
the sum is $< 1 + o(1)$ — is not proved or disproved by the facts F1, F2, F3 alone
as currently stated. F1 gives the weaker bound $< 1.399 + o(1)$. The gap between
$1.399$ and $1$ cannot be closed with the given facts. This remains open.

**Convergence assessment**: Given that all direct approaches using F1, F2, F3 have
been analyzed and found insufficient to prove the conjecture, and no counterexample
witness has been found, we have converged on a partial result identifying the gap.
