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
  Asserting a refutation or claiming the claim was settled triggers
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

---

## Section 1: Setup

### 1.1 The Claim

A **primitive set** is a set $A \subseteq \mathbb{N}$ of distinct integers such
that no element of $A$ divides any other distinct element of $A$.

**Erdős's conjecture (tightened form):** For any $x \geq 2$ and any primitive
set $A \subseteq [x, \infty)$,
$$
\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),
$$
where the $o(1)$ term tends to $0$ as $x \to \infty$.

In other words: the sum $f(A) := \sum_{a \in A} \frac{1}{a \log a}$ is
bounded above by $1$ in the limit of large $x$. The conjecture says no
primitive set (restricted to integers $\geq x$) can make this weighted sum
exceed $1 + o(1)$.

**Status:** Open. The claim is an unresolved conjecture. This attempt may
establish a partial result or discover a counterexample, but no resolution
can be asserted until verifier-accepted.

### 1.2 Given Facts (with sign disambiguations)

**F1 (Erdős-Zhang upper bound, 1935/1993):** For ANY primitive set
$A \subseteq \mathbb{N}$ (no restriction to $[x, \infty)$),
$$
\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).
$$
*Sign note*: This is an **UPPER** bound, strictly less than $\approx 1.399$.
It is entirely consistent with the conjecture (which posits a tighter bound
of $1$). It does **NOT** contradict the conjecture.

**F2 (Omega-stratum lower bound):** For $A_k := \{n \in \mathbb{N} : \Omega(n) = k\}$
(integers with exactly $k$ prime factors counted with multiplicity),
$$
\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).
$$
*Sign note*: The $O(\cdot)$ term here is **UNSIGNED** — it could be positive
or negative. This fact tells us the sum is at least $1$ minus a quantity
bounded in absolute value by $k^{-1/2+o(1)}$. Concluding that the sum
exceeds $1$ from F2 alone is a **sign error**; it contradicts F3.

**F3 (Exact asymptotic for $A_k$):** For $A_k := \{n \in \mathbb{N} : \Omega(n) = k\}$,
$$
\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.
$$
*Sign note*: The leading correction $-(c+o(1))k^2/2^k$ is **negative** (since
$c > 0$). The sum approaches $1$ from **BELOW** as $k \to \infty$. The
$o(1)$ is as $k \to \infty$; for small $k$ (e.g.\ $k=1$), the formula may
not hold exactly (see Section 2.1 for the numerical picture). F3 is consistent
with F2 once F2's unsigned-$O$ is read correctly.

### 1.3 Witness Contract

A counterexample to the conjecture would be a primitive set $A \subseteq
[x_{\text{floor}}, \infty)$ for some $x_{\text{floor}} \geq 2$ with
$\sum_{a \in A} \frac{1}{a \log a} > 1$. The harness verifier uses:

- **x\_floor** (int $\geq 2$): every element of $A$ must be $\geq x_{\text{floor}}$.
- **elements** (list of ints, pairwise non-divisible, each $\geq x_{\text{floor}}$).
- **claimed\_sum\_lower\_bound** (float): the agent's claim; the verifier
  recomputes the exact sum independently.

The verifier uses high-precision `decimal` arithmetic to compute
$\sum_{a \in A} 1/(a \log a)$ and checks: (a) elements are distinct,
(b) elements are pairwise non-divisible (primitive), (c) each element
$\geq x_{\text{floor}}$, and (d) the rigorous lower bound exceeds
`witness_threshold = 1.0`.

### 1.4 Roadmap

The proof attempt will proceed in the following phases:

1. **Numerical evidence** (Q2, Q3): verify F3 numerically; check prime-set sums.
2. **Witness search** (Q4): systematically search for a primitive set in
   $[x_{\text{floor}}, \infty)$ with sum $> 1.0$.
3. **Proof structure** (Q5): stratify by $\Omega(a)$; write lemma files for
   the key inequalities.
4. **Partial result or counterexample**: depending on the witness search and
   the lemma proofs, either establish a partial result or commit a witness.

This section (Q1) is complete.

---

## Section 2: Numerical Evidence (Q2 and Q3)

### 2.1 Partial sums for $k = 1, 2, 3, 4$ (Q2)

We compute $S_k(N) := \sum_{a \in A_k, a \leq N} \frac{1}{a \log a}$ for increasing $N$.
F3 states (for the full $A_k$) that the sum $= 1 - (c+o(1)) k^2/2^k$ with $c \approx 0.0656$:

| $k$ | $N=100$ | $N=1000$ | $N=10000$ | $N=100000$ | $F_k := 1 - 0.0656 \cdot k^2/2^k$ |
|-----|---------|----------|-----------|------------|-----------------------------------|
| 1   | 1.421567 | 1.492315 | 1.528162 | 1.549781  | 0.9672 |
| 2   | 0.579131 | 0.699977 | 0.776126 | 0.828802  | 0.9344 |
| 3   | 0.219701 | 0.321051 | 0.395127 | 0.452169  | 0.9262 |
| 4   | 0.076006 | 0.134091 | 0.183148 | 0.224915  | 0.9344 |

Observations:
- For $k = 2, 3, 4$: partial sums are **strictly less than 1** for all $N$ and
  increasing slowly toward the F3 asymptote from below.
- For $k = 1$ (primes): the partial sum $S_1(N)$ exceeds 1 at small $N$ (e.g.
  $S_1(100) = 1.422$) and continues to grow. The gap between $S_1(N)$ and F3's
  asymptote $\approx 0.967$ is large; this is the numerically hardest case.
  Resolving whether the full infinite sum for $k=1$ equals $F_1 = 0.967$ is a
  separate open question not addressed here.

### 2.2 Prime-set sum and F1 consistency (Q3)

$A_1 = \{\text{primes}\}$ is a primitive set. Partial sums:

| $N$ | $\pi(N)$ | $S_1(N)$ |
|-----|----------|----------|
| 100 | 25 | 1.421567 |
| 1000 | 168 | 1.492315 |
| 10000 | 1229 | 1.528162 |
| 100000 | 9592 | 1.549781 |

The partial sum is consistent with the expected limiting value $\approx 1.6366$
mentioned in the open-question queue (Q3).

**Remark on F1 tension**: F1 as stated says "for any primitive set
$A \subseteq \mathbb{N}$, sum $< 1.399 + o(1)$". If $o(1) = 0$ this would
be contradicted by the prime partial sums ($1.55$ at $N = 100000$). We take
the conservative view that F1's $o(1)$ is an unspecified correction that may
depend on the structure of $A$ and on $x$ in ways not fully spelled out in
the ledger; the prime-sum data is reported as-is, and Section 4 does not
rely on F1 for a quantitative bound.

### 2.3 Implications for the witness search (Q4 setup)

The primes with $x_{\text{floor}} = 2$ already give a partial sum (1.55 at
$N = 100000$) exceeding the witness threshold of 1.0. However, as noted in
the proof specification, a finite witness with sum $> 1.0$ at small
$x_{\text{floor}}$ is meaningful only if the implicit $o(1)$ at that
$x_{\text{floor}}$ is also small. For $x_{\text{floor}} = 2$, this condition
is not satisfied.

Restricting to primes $\geq x_{\text{floor}} = 100$: the tail sum is
approximately $S_1(100000) - S_1(100) = 1.5498 - 1.4216 = 0.1282$, well
below 1.0. This suggests that the primes alone are NOT a strong counterexample
candidate for large $x_{\text{floor}}$.

---

## Section 3: Witness Search (Q4)

### 3.1 Small $x_{\text{floor}}$ witnesses

A witness with $x_{\text{floor}} = 2$ and elements $\{2, 3\}$ achieves a
rigorously verified sum of $\approx 1.0248 > 1.0$ (verified by
`library.primitive_set_witness.verify_witness`). This trivial witness
confirms the harness functions correctly, but is not a meaningful
counterexample: the $o(1)$ term at $x_{\text{floor}} = 2$ is approximately
$0.636$ (the excess of the prime-sum from 2 over 1), so the bound
$1 + o(1) \approx 1.636$ at this $x_{\text{floor}}$ is not violated.

### 3.2 Greedy primitive set search

We ran a greedy ascending search: starting from $x_{\text{floor}}$, add
each integer that is pairwise non-divisible with all already chosen elements.

| $x_{\text{floor}}$ | max element | elements | approx sum |
|---------|-------------|----------|------------|
| 2       | 5002        | 669      | 1.519      |
| 3       | 5003        | 670      | 0.978      |
| 3       | 50003       | 5133     | 1.003      |
| 5       | 5005        | 671      | 0.698      |
| 100     | 10100       | 1577     | 0.278      |
| 100     | 100100      | 9935     | 0.299      |
| 100     | 1000100     | 78841    | 0.314      |

Key findings:
- For $x_{\text{floor}} = 2$: greedy exceeds 1.0 quickly. Not meaningful.
- For $x_{\text{floor}} = 3$: sum exceeds 1.0 for max element $\geq 50003$
  (5133 elements). The witness structure is: $\{3, 4\} \cup \{\text{primes}
  \geq 5, p \leq 50003\}$. Sum $\approx 1.003$ (numerical observation only;
  no `<!-- WITNESS -->` block committed). $x_{\text{floor}} = 3$ is too
  small for the $o(1)$ to be negligible.
- For $x_{\text{floor}} = 100$: greedy sum grows to only $0.314$ even over
  78841 elements (range to $10^6$). The greedy set is dominated by primes
  $\geq 100$; adding composites provides modest incremental improvement.
  In the explored range (up to $10^6$), the sum reaches only $\approx 0.314$.
  **No witness with $x_{\text{floor}} = 100$ was found.**

### 3.3 Conclusions from the witness search

No primitive set in $[x_{\text{floor}}, \infty)$ with $x_{\text{floor}} \geq 5$
and sum $> 1.0$ was found by the greedy construction over any feasible search
range. The greedy sum for $x_{\text{floor}} = 100$ appears bounded well below 1.0,
consistent with the conjecture's claim that the maximum sum for large $x$ is
$< 1 + o(1)$.

This does **not** prove the conjecture (the greedy construction may not be
optimal), but provides strong numerical evidence that no counterexample exists
for moderate $x_{\text{floor}} \geq 100$.

---

## Section 4: Proof Structure (Q5 — partial outline)

### 4.1 Strategy: Stratify by $\Omega(a)$

For any primitive set $A \subseteq [x, \infty)$, write $A_k = A \cap \{n :
\Omega(n) = k\}$. Since $A$ is primitive and any two elements of the same
$\Omega$-stratum that satisfy $a | b$ must have $\Omega(b) > \Omega(a)$
(every prime factor of $a$ is in $b$ and $b$ has strictly more factors), elements
in the same stratum are automatically pairwise non-divisible. Thus:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A_k} \frac{1}{a \log a}.$$

The challenge is bounding the TOTAL over all $k$.

### 4.2 Per-stratum bound (large $k$ only)

By F3 (valid as $k \to \infty$), for large enough $k$ the full stratum sum
$\sum_{a : \Omega(a)=k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} < 1$.

For **small $k$** (especially $k=1$, the primes), F3 does not directly apply;
the partial sums for $k=1$ grow above 1 (see Section 2.1), so the per-stratum
bound must use a separate argument for small-$k$ strata.

Even restricting to large $k$: the sum OVER $k$ of these per-stratum bounds
still diverges:
$$\sum_{k=K_0}^{K} \left(1 - c \frac{k^2}{2^k}\right) \sim (K - K_0) \to \infty \quad (K \to \infty).$$

So naive per-stratum summation does not give a useful bound regardless.
The cross-stratum constraint (Section 4.3) is essential.

### 4.3 Cross-stratum constraint

The key constraint is that elements from different strata of $A$ must also be
pairwise non-divisible. If $a \in A_j$ and $b \in A_k$ with $j < k$ and $a | b$,
then $b \notin A$. This CROSS-STRATUM EXCLUSION is the heart of the problem: it
prevents $A$ from using too much of each stratum.

**Open sub-problems** (to be addressed in lemma files):

- **Lemma L1** (cross-stratum density): bound how much of stratum $A_k$ a
  primitive set can use, given that it already uses elements from strata
  $j < k$. The primitive condition imposes a sieving constraint.
- **Lemma L2** (dominant stratum): identify which stratum contributes the most
  to the sum, and show that the total contribution is bounded.
- **Lemma L3** (tail bound): show that the contribution from strata $k \geq K$
  for large $K$ is small (this likely follows from F3 directly since
  $1 - c k^2/2^k < 1$ and the geometric factor makes the tail small).

These lemmas will be developed in `proof_lemmas/` files in the next session.

---

## Section 5: Partial Result Summary (Q6)

### 5.1 Status: Open — Partial Progress

The conjecture remains **open**. This attempt has not resolved it, positively
or negatively. What follows summarizes what was established and what obstacles
were found.

### 5.2 What was established

1. **Claim formalization** (Section 1): The conjecture and the three given facts
   (F1/F2/F3) were restated with explicit sign disambiguations and the asymptotic
   scope of each fact was identified. F3's $o(1)$ is as $k \to \infty$; it does
   not directly apply to the $k=1$ (primes) stratum at finite partial sums.

2. **Numerical confirmation of F3** (Section 2): For $k = 2, 3, 4$ the partial
   sums $S_k(N)$ are strictly less than 1 for all $N \leq 10^5$, consistent with
   F3's prediction that the sum approaches 1 from below. For $k=1$ the partial
   sums grow beyond 1, confirming that F3 does not apply to the prime stratum in
   the range explored.

3. **Numerical counterexample search** (Section 3): A greedy ascending primitive
   set search found no witness with $x_{\text{floor}} \geq 5$ whose sum exceeds
   1.0 over any feasible search range (up to $10^6$). For $x_{\text{floor}} = 100$
   the greedy sum is bounded below 0.4 in the explored range, reaching $\approx 0.314$
   with $\sim 79000$ elements. This provides numerical evidence against a counterexample
   at moderate $x_{\text{floor}}$.

4. **Proof skeleton** (Section 4): The $\Omega$-stratification approach was
   identified: write $A = \bigcup_k A_k$ and bound each stratum's contribution.
   For large $k$, F3 gives a per-stratum bound strictly below 1; for small $k$
   (especially $k=1$), F3 does not apply.

### 5.3 What was ruled out as a proof strategy

- **Naive per-stratum summation**: Even if each stratum sum $< 1$, summing over
  infinitely many strata diverges. The cross-stratum constraint must be used.

- **Counterexamples with $x_{\text{floor}} \geq 5$**: None found by greedy search
  in the explored range. Not ruled out analytically, but numerically unsupported.

- **Applying F3 to the $k=1$ stratum**: The prime-set partial sums exceed 1 at
  all computed ranges, so F3's asymptote (which applies as $k \to \infty$) cannot
  be used for $k=1$.

### 5.4 Key open obstacles

The following sub-problems must be resolved for a complete proof:

**Obstacle O1 (cross-stratum density)**: Bounding how much of each $\Omega$-stratum
a primitive set can use once other strata are occupied. The primitive condition
prevents $a | b$, but quantifying this globally requires a sieve-theoretic tool
not available in the current fact ledger.

**Obstacle O2 (prime stratum bound)**: Proving that the contribution from the
$k=1$ stratum of any primitive set $A \subseteq [x, \infty)$ is bounded by
$o(1)$ as $x \to \infty$. This is the analytic core of the conjecture (it is
closely related to the prime-tail sum problem of bounding
$\sum_{p \geq x} 1/(p \log p)$; this connection is noted informally and is not
formalized in the ledger). Fact F1 gives an upper bound of $1.399 + o(1)$
for the WHOLE primitive set; it does not separate out the prime stratum.

**Obstacle O3 (coupling small and large strata)**: Even if O1 and O2 are resolved
separately, combining them into a global bound $\leq 1 + o(1)$ requires a coupling
argument showing the bounds are not simultaneously tight across strata.

### 5.5 Verdict

The conjecture resists the current toolkit. The available facts (F1, F2, F3) are
consistent with the conjecture but do not individually suffice to prove it. The
numerical evidence strongly supports it. A complete proof would require:
- A quantitative cross-stratum exclusion principle (O1), OR
- A direct bound on the prime-stratum tail sum $\sum_{p \geq x} 1/(p \log p)$ (O2).

This is recorded as a **partial result**: the conjecture remains open at the end
of this attempt, with the above obstacles identified as the key barriers.
