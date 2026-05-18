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

## Section 1 — Setup

### The claim

**Erdős's primitive-set conjecture (tightened form).**  Let $x \geq 2$ and let
$A \subseteq [x, \infty)$ be a *primitive set* of positive integers (no distinct
element of $A$ divides another).  Then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ error term depends only on $x$ and tends to $0$ as
$x \to \infty$.

Informally: the supremum of the weighted sum over all primitive subsets of
$[x, \infty)$ is at most $1 + \varepsilon(x)$ with $\varepsilon(x) \to 0$.
The weight $1/(a \log a)$ is the "Erdős weight" for an integer $a$.

The claim is **open**; no proof or disproof is known as of the start of this
attempt.  This file will not assert the claim proved or disproved unless a
verifier-accepted `<!-- WITNESS -->` block appears below (`critic_openness`
enforces this).

---

### Given facts

**F1 — Erdős–Zhang global upper bound (UPPER bound, consistent with the
conjecture).**

For *any* primitive set $A \subseteq \mathbb{N}$ (no floor restriction),

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign note.* This is a strict upper bound.  It does **not** say the sum can
reach $1.399$; it says the sum stays below $1.399 + o(1)$.  F1 is
**consistent** with the conjecture (which posits a tighter bound of $1 + o(1)$
for the restricted family $A \subseteq [x, \infty)$).  Misreading F1 as a
lower bound is a sign error.

*Citation.* Erdős 1935; Zhang 1993.

---

**F2 — Omega-stratum lower bound (UNSIGNED big-O — do NOT conclude sum > 1
from F2 alone).**

For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity),

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign note.* The $O(\cdot)$ term is **unsigned** — it may be positive or
negative with absolute value bounded by $k^{-1/2+o(1)}$.  This inequality
says the sum is at least $1 - C k^{-1/2+o(1)}$ for some constant $C > 0$,
**not** that the sum is at least $1 + Ck^{-1/2+o(1)}$.  Any chain that
concludes "$\sum > 1$" from F2 alone, without a separate positivity argument
for the error term, is committing a sign error (`critic_sign` flags this
BLOCKING).  This is precisely the failure mode of the ChatGPT writeup in
`tests/fixtures/chatgpt_primitive_set_round0.md`.

---

**F3 — Exact asymptotic for $A_k$: sum approaches 1 from BELOW.**

For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},$$

where $c \approx 0.0656 > 0$.

*Sign note.* The leading correction $-(c+o(1))k^2/2^k$ is **negative** (since
$c > 0$).  Therefore the sum for $A_k$ is **strictly less than 1** for every
$k \geq 1$, and it approaches $1$ from **below** as $k \to \infty$.  The
canonical "extremal-looking" primitive set $A_k$ does **not** violate the
conjecture.  Treating the approach as from above is `f3-from-above-misread`
BLOCKING.

*Consistency with F2.* F3 is consistent with F2: F2's unsigned-$O$ is
negative for all finite $k$, with magnitude $(c+o(1))k^2/2^k$.

---

### Witness contract

A disproof claim requires a finite primitive set
$A = \{a_1, \ldots, a_m\} \subset [x_\text{floor}, \infty)$ (no element
divides another, all $a_i \geq x_\text{floor}$) such that
`library.primitive_set_witness.verify_witness` confirms

$$\sum_{i=1}^{m} \frac{1}{a_i \log a_i} > 1.0 \quad \text{(the witness threshold)}.$$

The block must be embedded in this file in the exact format specified in the
"Witness format" section above.  Until such a block is committed and
`witness_valid == 1`, the claim remains **open** by construction.

*Caveats on small $x_\text{floor}$.* The conjecture's $o(1)$ term can be
large for small $x$.  A witness at $x_\text{floor} = 2$ with sum $> 1$ is
consistent with the conjecture if $1 + o(1)$ at $x = 2$ still exceeds the
witness sum.  A meaningful disproof requires either (a) a witness at large
$x_\text{floor}$ where $o(1)$ is provably tiny, or (b) an argument that the
$o(1)$ at the witness's $x_\text{floor}$ is smaller than the excess above $1$.

---

### Road map for this attempt

1. **Numerical evidence (Q2, Q3)**: verify F3 computationally for $k = 1, \ldots, 4$
   and confirm the primes-from-2 sum is ~$1.6366$ (consistent with F1 + F3).
2. **Witness search (Q4)**: run `library.primitive_set_witness.verify_witness`
   at $x_\text{floor} \in \{100, 1000, 10000\}$ with candidate primitive sets
   aiming for sum $> 1.0$.  (Expectation: hard for large $x_\text{floor}$, but
   trivial for small $x_\text{floor}$ — the interesting question is whether any
   large-$x$ witness can be constructed.)
3. **Proof structure (Q5)**: outline an omega-stratified approach; for each
   stratum $k$, bound the contribution of $A \cap A_k$ using F3.  Identify
   the cross-stratum gluing lemma as the main obstacle.
4. **Partial result or convergence (Q6)**: if gaps remain, document what has
   been ruled out.
