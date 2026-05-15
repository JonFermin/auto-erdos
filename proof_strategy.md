# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

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
  Any assertion of resolution (falsity, disproof, proof of contradiction)
  triggers `critic_openness`'s `open-claim-asserted-resolved-without-witness`
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

## Section 1 — Setup

### 1.1 The Conjecture

Let a **primitive set** be a set $A$ of positive integers with the property
that no element of $A$ divides any other distinct element. The Erdős
primitive-set conjecture (tightened form, from `proofs/primitive_set_erdos.json`)
asserts:

> **Claim**: For any $x \geq 2$ and any primitive set $A \subset [x, \infty)$,
> $$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
> where the $o(1)$ term tends to $0$ as $x \to \infty$.

In other words, the supremum of the weighted sum over all primitive subsets
of $[x, \infty)$ approaches at most $1$ as the lower bound $x$ grows. The
claim is **open** (status in `proofs/primitive_set_erdos.json`: `open`);
no unconditional proof has been logged in this harness.

### 1.2 Given Facts Ledger

The proof may cite the following three facts. All are recorded in
`proofs/primitive_set_erdos.json` as `given_facts`; citing any fact not in
this ledger triggers `critic_ledger` (BLOCKING).

**F1 — Erdős–Zhang upper bound** *(Erdős 1935; Zhang 1993)*:

> For any primitive set $A \subseteq \mathbb{N}$,
> $$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign disambiguation (critical)*: This is a strict **upper** bound.
The constant $e^\gamma \pi/4 \approx 1.399$ is *larger* than $1$.
F1 is consistent with the conjecture — it does NOT say the sum can
exceed $1$; it merely gives a weaker bound than what the conjecture claims.
Reading F1 as evidence that the sum *can* reach $1.399$ is NOT a sign
error; but claiming F1 implies the sum is $\geq 1.399$ IS a sign error.

**F2 — $\Omega$-stratum lower bound** *(stated as F2)*:

> For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
> $k$ prime factors, counted with multiplicity),
> $$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign disambiguation (critical)*: The $O(\cdot)$ term here is
**unsigned** — it could be positive or negative, bounded in absolute value
by $k^{-1/2+o(1)}$. The inequality reads: the sum is at least
$1 - |O(\ldots)|$, NOT $1 +$ (something positive). Concluding
$\sum > 1$ from F2 alone is a **sign error** (`unsigned-O-sign-confusion`,
BLOCKING). F2 is consistent with F3 once the unsigned-$O$ is read correctly.
The canonical ChatGPT failure cited in the test fixtures (`tests/fixtures/`)
made exactly this error.

**F3 — Exact asymptotic for $A_k$** *(stated as F3)*:

> For $A_k$ as above, as $k \to \infty$,
> $$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
> \quad c \approx 0.0656 > 0.$$

*Sign disambiguation (critical)*: The leading correction is
$-(c+o(1)) k^2/2^k$ with $c > 0$ and $k^2/2^k > 0$, so the sign is
strictly **negative**. The sum approaches $1$ from **below** as
$k \to \infty$. For every fixed $k \geq 1$, the sum is strictly $< 1$.
F3 shows that the $A_k$ sequences are asymptotically extremal (approaching
the bound $1$ from below), but $A_k$ itself never exceeds $1$.
Reading F3 as saying the sum approaches $1$ from above (`f3-from-above-misread`)
is BLOCKING.

### 1.3 Witness Contract

A claimed **counterexample** to the conjecture requires:

1. A finite set $\{a_1, a_2, \ldots, a_m\}$ of distinct positive integers,
   all $\geq x_\text{floor}$ for some declared $x_\text{floor} \geq 2$.
2. Pairwise **non-divisibility**: $a_i \nmid a_j$ for all $i \neq j$.
3. Rigorously verified sum $> 1.0$ (the `witness_threshold`), computed
   by `library.primitive_set_witness.verify_witness` (not self-reported).

The verifier recomputes the sum independently; a `claimed_sum_lower_bound`
is accepted only if the verifier's own computation also exceeds $1.0$.

**Important caveat**: The conjecture's $o(1)$ correction means a witness
with small $x_\text{floor}$ (say $x_\text{floor} = 2$) that barely exceeds
$1.0$ is *consistent* with the conjecture for large $x$. A genuinely
compelling counterexample would need $x_\text{floor}$ large enough that the
$o(1)$ term is demonstrably small, yet the sum still exceeds $1 + \delta$
for some $\delta > 0$. The `critic_openness` pass judges this in context.

---

## Section 2 — Numerical Evidence

*(To be filled in Round 2 and Round 3.)*

---

## Section 3 — Proof Structure and Lemmas

*(To be filled starting Round 5.)*

---

## Body

The main proof attempt begins below. Current status: **Section 1 complete**.
Next: numerical verification (Q2 and Q3), then witness search (Q4), then
lemma decomposition (Q5).
