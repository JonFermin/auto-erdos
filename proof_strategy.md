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
  Asserting that a claim has been falsified, or claiming a completed disproof,
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

## Body

### Section 1: Setup (Q1)

**The conjecture (in my own words).** Fix any $x \geq 2$. Consider a *primitive
set* $A \subseteq [x, \infty)$: a set of integers, all at least $x$, such that
no element divides another distinct element. The conjecture asserts that for any
such $A$,
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$
where the $o(1)$ error tends to $0$ as $x \to \infty$. In particular, for very
large $x$ the sum is essentially bounded above by $1$. The claim status is
**open**.

**The three given facts and their sign traps.**

*F1 (Erdős–Zhang upper bound, ~1.399).* For any primitive set $A \subseteq
\mathbb{N}$ (not restricted to $[x,\infty)$), one has
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma}\frac{\pi}{4} + o(1) \approx
1.399 + o(1).$$
Sign note: this is an UPPER bound. It says the sum is smaller than 1.399,
which is consistent with the conjecture (the conjecture asks for the tighter
bound of 1). Reading F1 as a lower bound is a sign error.

*F2 (Omega-stratum lower bound, unsigned big-O).* Let $A_k = \{n \in \mathbb{N}
: \Omega(n) = k\}$ (integers with exactly $k$ prime factors counted with
multiplicity). Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$
Sign note: the $O(\cdot)$ term is UNSIGNED — it could be positive or
negative. The inequality guarantees only that the sum is at least $1$ minus
something of size $k^{-1/2+o(1)}$, NOT that it exceeds $1$. Any argument that
concludes $\sum > 1$ from F2 alone, without a separate positivity argument for
the big-O term, is a sign error.

*F3 (Exact asymptotic for $A_k$, approaching 1 from below).* With the same
$A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
Sign note: the leading correction is $-(c+o(1))k^2/2^k$ with $c > 0$, so
the sum is STRICTLY LESS THAN 1 for every $k \geq 1$, approaching 1 from
BELOW as $k \to \infty$. The canonical Omega-stratum sets are the
"extremal-looking" examples, but even they never violate the conjecture. F3 is
consistent with F2 once F2's unsigned-O is read correctly.

**The witness contract (the only path to a disproof).** A counterexample
requires a finite primitive set $A \subset [x_\text{floor}, \infty)$ with
a rigorous lower bound on $\sum 1/(a \log a)$ exceeding $1.0$, verified by
`library.primitive_set_witness.verify_witness`. Elements must be pairwise
non-divisible and each $\geq x_\text{floor}$. The witness is embedded as a
`<!-- WITNESS ... WITNESS -->` JSON block at the bottom of this file.

**Road map.** The current plan is to work through the open questions in order:
- Q2: numerical check of F3 for small $k$ (ground truth).
- Q3: check that the prime-set sum is ~1.64 and reconcile with F1.
- Q4: search for a witness (primitive set in $[x, \infty)$ with sum $> 1$).
- Q5: outline a proof strategy via Omega-stratification.
- Q6: if genuine barriers remain, document the partial result and close.
