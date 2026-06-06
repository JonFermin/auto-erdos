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
  Asserting that it has been disproved, or that a counterexample has been
  constructed, without a verifier-accepted `<!-- WITNESS -->` block triggers
  `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING. Do not write resolution-language unless `witness_valid == 1`.

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

### Section 1 — Setup

**Claim (Erdős primitive-set conjecture, tightened form)**

For any $x \geq 2$, if $A \subset [x, \infty)$ is a *primitive set* of
integers — meaning no distinct element of $A$ divides another — then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where $o(1) \to 0$ as $x \to \infty$.  In other words, the sum over any
primitive subset of $[x, \infty)$ is eventually below 1.

**Primitive set definition.** A set $A \subseteq \mathbb{N}$ is primitive
if for all $a, b \in A$ with $a \neq b$, $a \nmid b$. Examples: sets of
integers all having the same number of prime factors (the $A_k$ strata),
any antichain in the divisibility poset.

---

**Given facts ledger** (READ-ONLY; citations fixed in `proofs/primitive_set_erdos.json`)

**F1 — Erdős–Zhang upper bound** (Erdős 1935; Zhang 1993):
For *any* primitive set $A \subseteq \mathbb{N}$ (no floor on elements),
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \tfrac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
*Sign note*: This is an UPPER bound, strictly less than $\approx 1.399$.
It is CONSISTENT with the conjecture (which claims a tighter bound of 1
for primitive sets bounded away from 1).  Misreading F1 as a lower bound
is a sign error.

**F2 — $A_k$ stratum lower bound (UNSIGNED big-O)** (cited as fact F2):
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
$k$ prime factors, counted with multiplicity).  Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$
**Critical sign disambiguation**: The $O(\cdot)$ term is *unsigned* — its
sign is unknown, so the bound only says the sum is within $|O(k^{-1/2+o(1)})|$
of 1, either above or below.  Any argument that concludes $\text{sum} > 1$
from F2 alone, without a separate positivity proof for the correction, is
a SIGN ERROR and will be rejected by `critic_sign`.

**F3 — $A_k$ stratum exact asymptotic** (cited as fact F3):
For $A_k$ as above,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
*Sign note*: The leading correction $-(c+o(1))k^2/2^k$ is NEGATIVE for all
$k \geq 1$.  Therefore the sum approaches 1 **from below** as $k \to \infty$.
This is consistent with F2 once F2's unsigned-O is read correctly: F3
shows the unsigned $O(k^{-1/2})$ is in fact negative to leading order.
F3 directly rules out $A_k$ as a counterexample for any $k$.

---

**Witness contract** (the only path to claiming a counterexample)

To disprove the conjecture one must exhibit a finite primitive set
$A \subset [x_\text{floor}, \infty)$ (all elements $\geq x_\text{floor} \geq 2$,
pairwise non-divisible) whose sum $\sum_{a \in A} 1/(a \log a)$ exceeds
the threshold $\tau = 1.0$, as *rigorously verified* by
`library.primitive_set_witness.verify_witness`.  The claim must be
embedded in a `<!-- WITNESS ... WITNESS -->` block in this file;
`proof_prepare.py` parses the JSON, re-runs the verifier, and sets
`witness_valid = 1` only if every check passes.

The $o(1)$ caveat in the conjecture means a finite witness exceeding 1.0
is suggestive but not necessarily conclusive — a human reviewer must
additionally estimate how large the $o(1)$ gap is at the witness's
$x_\text{floor}$ before calling it a true counterexample.  However, any
witness with $\sum > 1 + \varepsilon$ for $\varepsilon$ bounded away from
zero and $x_\text{floor}$ large would be very strong evidence.

Witness schema:
```json
{
  "x_floor": "<int >= 2>",
  "elements": "<list[int], pairwise non-divisible, each >= x_floor>",
  "claimed_sum_lower_bound": "<float, verifier recomputes rigorously>"
}
```

---

**Roadmap** (to be filled in by subsequent rounds)

- Q2: Numerically verify F3 for $k = 1, 2, 3, 4$.
- Q3: Numerically check sum over primes from 2 (primitive set), understand
  why it exceeds 1 without contradicting F1.
- Q4: Search computationally for a witness exceeding $\tau = 1.0$.
- Q5: Outline a stratified proof structure via $\Omega$-strata.
