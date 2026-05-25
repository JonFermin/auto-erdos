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

### 1.1 The claim

**Erdős's primitive-set conjecture (tightened form).** For any primitive set
$A \subset [x, \infty)$ — a set of integers all $\geq x$ in which no element
divides another — the weighted sum

$$\sum_{a \in A} \frac{1}{a \log a}$$

satisfies $\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$ as $x \to \infty$.

Equivalently: for every $\varepsilon > 0$ there exists $x_0(\varepsilon)$ such
that every primitive set lying entirely in $[x_0, \infty)$ has sum at most
$1 + \varepsilon$.

**Status**: open. The conjecture has not been proved or disproved in the
literature. This file may not assert resolution without a verifier-accepted
`<!-- WITNESS -->` block.

### 1.2 The given-facts ledger (read sign disambiguations carefully)

**F1 — Erdős-Zhang upper bound (≈ 1.399).**
For any primitive set $A \subseteq \mathbb{N}$ (not necessarily restricted to
$[x, \infty)$),

$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399.$$

*Sign reading*: this is an **upper bound**, strictly less than 1.399. It does
NOT establish a lower bound or contradict the conjecture (which says the true
bound is 1). F1 and the conjecture are compatible — the conjecture just claims
the constant 1.399 can be tightened to 1 as $x \to \infty$.

**F2 — Omega-stratum lower bound (UNSIGNED big-O).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors, counted with multiplicity). Then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign reading*: the $O(\cdot)$ term is **unsigned** — it may be positive or
negative. The statement says the sum is at least $1$ minus something of
absolute size $\leq k^{-1/2+o(1)}$. It does NOT say the sum exceeds 1.
Concluding $\sum_{A_k} > 1$ from F2 alone (without a positivity argument for
the error term) is the canonical sign error (`unsigned-O-sign-confusion`),
the failure mode of prior incorrect writeups.

F2 is consistent with F3 once the unsigned-O is read correctly.

**F3 — Exact asymptotic for the Omega-k stratum (APPROACHES FROM BELOW).**
For $A_k$ as above,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$

*Sign reading*: the leading correction $-(c+o(1)) k^2/2^k$ is **negative**
(since $c > 0$). Therefore the sum is **strictly less than 1** for every
$k \geq 1$, and it approaches 1 from **below** as $k \to \infty$. The
canonical extremal-looking primitive set $A_k$ does NOT violate the
conjecture, no matter how large $k$ is.

### 1.3 Witness contract (the only path to a disproof claim)

To claim a counterexample, one must exhibit a finite primitive set
$A = \{a_1, \ldots, a_m\} \subset [x_{\text{floor}}, \infty)$ (pairwise
non-divisible, all elements $\geq x_{\text{floor}} \geq 2$) such that the
rigorously computed lower bound on $\sum_{a \in A} 1/(a \log a)$ exceeds the
`witness_threshold` of **1.0**.

The verifier (`library.primitive_set_witness.verify_witness`) computes the
sum using stdlib `decimal` arithmetic with ULP-bumped `math.log` to ~50
decimal digits, guaranteeing a rigorous lower bound. A `witness_valid = 1`
flag from the verifier is required before any counterexample claim may appear
in this file.

Format for embedding a witness:

```
<!-- WITNESS
{
  "x_floor": <int>,
  "elements": [<int>, ...],
  "claimed_sum_lower_bound": <float>
}
WITNESS -->
```
