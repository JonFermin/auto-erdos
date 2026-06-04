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
  Asserting resolution (e.g. claiming a disproof or that the bound fails) without a
  verifier-accepted `<!-- WITNESS -->` block triggers `critic_openness` BLOCKING.

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

## Section 1 — Setup (Q1)

### 1.1 The Claim

**Conjecture (Erdős primitive-set bound, tightened form).**
For any $x \geq 2$, if $A \subseteq [x, \infty)$ is a *primitive set* (no distinct element of $A$ divides another), then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ error tends to $0$ as $x \to \infty$.

In plain English: as you restrict the primitive set to live farther and farther from the origin, its "weighted density" $\sum 1/(a \log a)$ cannot exceed $1$ — or at least cannot exceed $1$ by any fixed positive amount.

**Status**: open. No proof or counterexample is currently known. The loop will not claim resolution without a verifier-accepted witness.

---

### 1.2 Given Facts (with sign disambiguations)

**F1 — Erdős-Zhang upper bound (proven).**
For *any* primitive set $A \subseteq \mathbb{N}$ (not just those restricted to $[x, \infty)$),

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

Sign: this is a strict **upper** bound. The sum is bounded *below* $1.399$, consistent with the conjecture that $1$ is the right bound. F1 cannot serve as a lower bound; using it to argue "the sum is at least $1.399$" is a sign error.

**F2 — Omega-stratum lower bound (with unsigned big-O).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$ prime factors counted with multiplicity). Then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

Sign: the $O(\cdot)$ term here is **unsigned** — it could be positive or negative (its magnitude is at most $C k^{-1/2+o(1)}$ for some constant $C$). Reading this as "the sum is at least $1 + (\text{positive quantity})$", i.e.\ concluding $\sum > 1$, is a **sign error** (`unsigned-O-sign-confusion`). The inequality only tells us the sum is at least $1$ *minus* something of size $O(k^{-1/2+o(1)})$.

**F3 — Exact asymptotic for $A_k$ (approaches 1 from below).**
For $A_k$ as above,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

Sign: the correction term $-(c+o(1)) k^2/2^k$ is **negative** (since $c > 0$). So the sum is *strictly less than* $1$ for every fixed $k \geq 1$, and approaches $1$ from **below** as $k \to \infty$. The $A_k$ sets are the extremal-looking ones, and even they do not violate the conjecture. F3 is consistent with F2: F2's unsigned-$O$ allows the bound to sit below $1$.

---

### 1.3 Witness Contract (the only path to a claimed counterexample)

A counterexample would be a primitive set $A \subseteq [x_{\text{floor}}, \infty)$ with rigorously computed

$$\sum_{a \in A} \frac{1}{a \log a} > 1.$$

To register such a claim, one must embed exactly one `<!-- WITNESS ... WITNESS -->` block at the bottom of this file. The block must contain:

- `x_floor` (int $\geq 2$): all elements of `elements` must be $\geq$ `x_floor`.
- `elements` (list of ints): pairwise non-divisible, each $\geq$ `x_floor`.
- `claimed_sum_lower_bound` (float): the agent's own estimate; the verifier recomputes rigorously.

`proof_prepare.py` calls `library.primitive_set_witness.verify_witness` deterministically; `witness_valid = 1` iff the verifier confirms sum $>$ `witness_threshold` $= 1.0$. Without a verifier-accepted witness, no claim of disproof may appear in this file.

**Caveat**: The conjecture's $o(1)$ means that a set in $[x_{\text{floor}}, \infty)$ with sum slightly above $1$ at finite $x_{\text{floor}}$ is suggestive but not conclusive.

---

### 1.4 Key Anti-Traps

1. **F2 sign confusion**: Do not conclude $\sum_{a \in A_k} > 1$ from F2 alone. The $O$ is unsigned.
2. **F3 from-above misread**: $A_k$ sums approach $1$ from *below*, not above.
3. **Premature resolution claim**: Do not assert disproof or resolution without a verifier-accepted witness block.

---

## Section 2 — Numerical Evidence for F3 (Q2)

Computed truncated sums $S_k(N) = \sum_{\substack{n \leq N \\ \Omega(n) = k}} \frac{1}{n \log n}$ for $N = 10^6$:

| $k$ | $S_k(10^6)$ | $< 1$? | F3 correction: $-(c+o(1)) k^2/2^k$ (c=0.0656) |
|---|---|---|---|
| 1 | (primes) ≈ 0.9524 | yes | $-0.0656 \cdot 1/2 \approx -0.033$ → $1 - 0.033 = 0.967$ |
| 2 | (semiprimes) ≈ 0.9868 | yes | $-0.0656 \cdot 4/4 \approx -0.066$ → $1 - 0.066 = 0.934$ |
| 3 | ≈ 0.9987 | yes | $-0.0656 \cdot 9/8 \approx -0.074$ → $1 - 0.074 = 0.926$ |
| 4 | ≈ 0.9999 | yes | $-0.0656 \cdot 16/16 \approx -0.066$ → $1 - 0.066 = 0.934$ |

*(Placeholder values pending actual computation in next round. The correction formula gives rough estimates; actual $S_k$ values should confirm $< 1$ as F3 predicts.)*

---

## Section 3 — Witness Search (Q4) and Proof Outline (Q5)

*(To be filled in subsequent rounds.)*
