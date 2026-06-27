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
- **Resolution assertion without witness**. This claim is open; any
  declaration of resolution triggers `critic_openness` BLOCKING unless a
  verifier-accepted `<!-- WITNESS -->` block is committed and
  `witness_valid == 1`.

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

---

## Section 1: Setup (Q1)

### The conjecture

For any $x \geq 2$ and any **primitive** set $A \subset [x, \infty)$
(meaning: no element of $A$ divides another), define
$$
S(A) \;=\; \sum_{a \in A} \frac{1}{a \log a}.
$$
The **Erdős primitive-set conjecture** states:
$$
\sup_{\substack{A \subset [x,\infty) \\ \text{primitive}}} S(A) \;\longrightarrow\; 1
\quad \text{as } x \to \infty.
$$
Equivalently, $S(A) < 1 + o(1)$ uniformly over all primitive $A \subset [x,\infty)$.

The conjecture is **open**. No proof or disproof has been verified by this harness.

---

### Given facts (sign-disambiguated)

**F1 — Erdős–Zhang upper bound (1935 / 1993)**
$$
S(A) \;<\; e^\gamma \tfrac{\pi}{4} + o(1) \;\approx\; 1.399 + o(1)
\quad \text{for any primitive } A \subseteq \mathbb{N}.
$$
This is an **upper bound**. It is consistent with the conjecture (which asks for
the tighter bound of 1). It does NOT say sums can reach 1.399 — only that they
cannot exceed it. Misreading as a lower bound is a sign error.

**F2 — Omega-stratum lower bound (UNSIGNED big-O)**

Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity). Then:
$$
\sum_{a \in A_k} \frac{1}{a \log a}
\;\geq\; 1 + O\!\left(k^{-1/2+o(1)}\right).
$$
The $O(\cdot)$ term is **unsigned**: it is bounded in absolute value by
$k^{-1/2+o(1)}$ but could be positive or negative. This does NOT establish
$S(A_k) > 1$. Concluding the sum exceeds 1 from F2 alone is the sign error
that blocks the ChatGPT round-0 writeup.

**F3 — Omega-stratum exact asymptotic (approaches 1 from BELOW)**
$$
\sum_{a \in A_k} \frac{1}{a \log a}
\;=\; 1 - \frac{(c + o(1))\, k^2}{2^k}, \quad c \approx 0.0656 > 0.
$$
The correction term is $-(c+o(1))k^2/2^k$ with $c > 0$, so the sum is
**strictly less than 1** for every finite $k$ and approaches 1 **from below**
as $k \to \infty$. F3 refines F2: F2's unsigned-O is in fact negative (by F3's
more precise statement). The full stratum $A_k$ — the most extremal-looking
candidate — still does not violate the conjecture.

---

### Witness contract

To claim a counterexample, embed a `<!-- WITNESS -->` JSON block at the bottom
of this file with `x_floor`, `elements` (pairwise non-divisible integers $\geq$
x_floor), and `claimed_sum_lower_bound`. The verifier rigorously checks
primitivity and computes a rigorous lower bound on $S(A)$ via `decimal`
arithmetic. `witness_valid = 1` iff the lower bound exceeds 1.0.

No witness block committed yet. `witness_valid = 0`.

---

## Section 2: Numerical Evidence (Q2, Q3)

*(to be filled)*

## Section 3: Witness Search (Q4)

*(to be filled)*

## Section 4: Proof Structure (Q5)

*(to be filled)*
