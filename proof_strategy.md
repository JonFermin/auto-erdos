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

## Section 1: Setup (Q1)

### The Claim

Erdős's primitive-set conjecture asserts: for any primitive set
$A \subseteq [x, \infty)$ (where "primitive" means no element of $A$ divides
another distinct element of $A$), the Erdős function

$$f(A) = \sum_{a \in A} \frac{1}{a \log a}$$

satisfies $f(A) < 1 + o(1)$ as $x \to \infty$.

In other words, once we restrict to integers all at least as large as $x$,
the sum is bounded near 1, and this bound tightens as $x$ grows.

**Status**: open conjecture. No resolution may be claimed without a
verifier-accepted witness block (see below).

### Given Facts (with Sign Disambiguations)

**F1 (Erdős–Zhang upper bound, Zhang 1993)**:
For *any* primitive set $A \subseteq \mathbb{N}$ (no floor constraint),
$$f(A) = \sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign note*: This is an **upper** bound. It says the sum is *less than*
approximately 1.399, which is consistent with the conjecture (which
conjectures an even tighter upper bound of 1 + o(1) for the $x$-floored
version). F1 does NOT say the sum is close to 1.399 from below; it gives
a ceiling.

**F2 (Omega-stratum lower bound)**:
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ be the set of integers
with exactly $k$ prime factors (counted with multiplicity). Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$

*Sign note*: The $O(\cdot)$ term here is **unsigned** — it could be
positive or negative. The statement means the sum is at least
$1 - C k^{-1/2+o(1)}$ for some fixed constant $C > 0$, NOT that it
exceeds 1. Concluding $f(A_k) > 1$ from F2 alone is a sign error.

**F3 (Exact asymptotic for $A_k$)**:
For the same $A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},$$
where $c \approx 0.0656 > 0$.

*Sign note*: The leading correction term is $-(c+o(1)) k^2/2^k$ with
$c > 0$, so the sum is **strictly less than 1** for every finite $k \geq 1$,
and approaches 1 **from below** as $k \to \infty$. F3 is compatible with
both F2 (once F2's unsigned big-O is read correctly) and with the conjecture
(the canonical extremal-looking primitive set $A_k$ does NOT violate it).

### Witness Contract

A disproof of the conjecture requires exhibiting a finite primitive set
$A \subseteq [x_{\text{floor}}, \infty)$ with $f(A) > 1.0$, verified
rigorously by `library.primitive_set_witness.verify_witness`. If such a
witness is found, it must be embedded as a `<!-- WITNESS ... WITNESS -->`
block in this file (see the template in the header). The verifier recomputes
$f(A)$ exactly (using Python's arbitrary-precision arithmetic via `math.log`)
and checks pairwise non-divisibility.

Parameters:
- `x_floor`: integer $\geq 2$; every element of `elements` must be $\geq x_{\text{floor}}$.
- `elements`: list of integers, pairwise non-divisible, each $\geq x_{\text{floor}}$.
- `claimed_sum_lower_bound`: float; the verifier recomputes independently.

The conjecture's $o(1)$ caveat means a finite-$x$ witness that just barely
exceeds 1.0 might be misleading — the true supremum of $f(A)$ over all
primitive $A \subseteq [x, \infty)$ might still tend to $\leq 1$ as
$x \to \infty$. The openness critic will flag any premature conclusion.

### Proof Strategy Overview

Two independent threads to pursue in parallel:

**Thread A (search for counterexample)**: Try to find a primitive
$A \subseteq [x_{\text{floor}}, \infty)$ with $f(A) > 1.0$. Start with
greedy construction at $x_{\text{floor}} \in \{100, 1000, 10000\}$. If
this fails (consistent with the conjecture being true), document why.

**Thread B (structural proof)**: Attempt to bound $f(A)$ for arbitrary
primitive $A$ via Omega-stratification. The key question is: given F3's
exact formula, can we control the cross-stratum interaction?
