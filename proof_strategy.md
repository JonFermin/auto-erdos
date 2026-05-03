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
$c > 0$). The sum approaches $1$ from **BELOW** as $k \to \infty$, and is
**strictly less than $1$** for every finite $k \geq 1$. F3 is consistent
with F2 once F2's unsigned-$O$ is read correctly: F2 gives a lower bound
of roughly $1 - k^{-1/2}$, and F3 pins the exact value as $1 - ck^2/2^k$
(which is also roughly $1 - k^{-1/2}$ for the relevant range of $k$ in the
 sense that $k^2/2^k$ decays to $0$, so $\sum > 1 - \varepsilon$ for large $k$).

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

This section (Q1) is complete. Next: Q2 (numerical evidence for F3).
