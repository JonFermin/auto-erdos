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

**Conjecture (Erdős primitive-set bound, tightened form).**
For any $x \geq 2$, if $A \subset [x, \infty)$ is a *primitive* set of
integers — meaning no distinct $a, b \in A$ satisfies $a \mid b$ — then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ term tends to $0$ as $x \to \infty$.

**Status**: OPEN. No claim of resolution may appear in this file without a
verifier-accepted `<!-- WITNESS -->` block (`witness_valid == 1`).

---

### Given Facts

**F1 (Erdős–Zhang upper bound).**
For any primitive set $A \subseteq \mathbb{N}$,

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign/direction*: UPPER bound; sum is STRICTLY LESS THAN $\approx 1.399$.
F1 is weaker than the conjecture (which posits $< 1 + o(1)$). It does NOT
show the sum exceeds $1$. Reading F1 as a lower bound is a sign error.

**F2 (Omega-stratum lower bound, UNSIGNED big-O).**
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$:

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign/direction*: The $O(\cdot)$ term is **unsigned** (bounded in absolute
value, possibly negative). The inequality says the sum is $\geq 1$ minus
something of size $O(k^{-1/2+o(1)})$, NOT $\geq 1$ plus a positive quantity.
Concluding $\sum_{A_k} > 1$ from F2 alone is `unsigned-O-sign-confusion`.

**F3 (Exact asymptotic for $A_k$).**
For $A_k$ as above:

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$

*Sign/direction*: The leading correction is $-(c+o(1))k^2/2^k < 0$.
The sum approaches $1$ from **below** as $k \to \infty$; it is strictly
less than $1$ for every finite $k \geq 1$. F3 is consistent with F2 once
the unsigned-O in F2 is read correctly. Treating F3 as approach from above
is `f3-from-above-misread`.

---

### Witness Contract

Disproof requires a finite primitive set $A \subset [x_{\mathrm{floor}}, \infty)$
with rigorously verified sum $\sum_{a \in A} 1/(a \log a) > 1.0$, via
`library.primitive_set_witness.verify_witness`. Schema:

```json
{
  "x_floor": 100,
  "elements": [101, 103, ...],
  "claimed_sum_lower_bound": 1.005
}
```

Embed as a `<!-- WITNESS ... WITNESS -->` block at the bottom of this file.
The verifier uses stdlib `decimal` with ULP-bumped `math.log` for ~50-digit
rigor. A witness exceeding $1$ at finite $x_{\mathrm{floor}}$ is a *candidate*
counterexample; the conjecture's $o(1)$ caveat means an additional analytical
estimate of the $o(1)$ gap at $x_{\mathrm{floor}}$ is needed to confirm.

---

## Body (ongoing)

### Section 2: Numerical Evidence (Q2 — pending)

### Section 3: Prime-sum Analysis (Q3 — pending)

### Section 4: Proof Structure / Lemma Outline (Q5 — pending)
