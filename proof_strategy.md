# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Section 1: Setup — claim, facts, witness contract

### The claim

The **Erdős primitive-set conjecture** asserts: for any set $A$ of positive
integers that is *primitive* (no distinct $a, b \in A$ satisfies $a \mid b$),
if every element of $A$ is at least $x$, then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$

where the $o(1)$ error tends to $0$ as $x \to \infty$.  Equivalently, as the
threshold $x$ grows, the supremum over all primitive $A \subseteq [x, \infty)$
of the above sum approaches at most $1$.

**Status**: OPEN. No proof or disproof is known. This file works toward either
a partial proof or a verified counterexample.

### Given facts (with sign disambiguations)

**F1 (Erdős–Zhang upper bound, ~1935 / 1993).**
For ANY primitive set $A \subseteq \mathbb{N}$ (not necessarily starting above
$x$), $\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx
1.399 + o(1)$.

*Sign note*: This is an UPPER bound — the sum is STRICTLY LESS THAN 1.399
(plus a vanishing correction).  F1 is consistent with the conjecture (which
claims a tighter upper bound of 1); it does NOT contradict it.  Misreading F1
as a lower bound is a sign error that would block immediately.

**F2 (Omega-stratum lower bound, unsigned big-O).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity).  Then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$

*Critical sign note*: The $O(\cdot)$ term is UNSIGNED — it could be positive or
negative, and its magnitude is $O(k^{-1/2+o(1)})$.  The inequality only says
the sum is at least $1$ MINUS some quantity bounded by $|O(k^{-1/2+o(1)})|$.
It does NOT say the sum exceeds $1$.  Concluding $\sum > 1$ from F2 alone is
the canonical sign error (`unsigned-O-sign-confusion`); any such chain is
BLOCKING.

**F3 (Exact asymptotic for the omega-k extremal, approaches 1 from below).**
For $A_k$ as above,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k}$$

where $c \approx 0.0656 > 0$.

*Sign note*: The correction $-(c+o(1))k^2/2^k$ is NEGATIVE (since $c > 0$).
The sum is STRICTLY LESS THAN 1 for every $k \geq 1$, and approaches $1$ from
BELOW as $k \to \infty$.  F3 shows that $A_k$ is "extremal-looking" but still
consistent with the conjecture.  Misreading F3 as approaching from above is
`f3-from-above-misread` BLOCKING.

### Witness contract (the path to a counterexample)

A disproof would require a primitive set $A \subseteq [x_\text{floor}, \infty)$
for some finite $x_\text{floor}$ such that $\sum_{a \in A} 1/(a \log a) > 1$,
with the sum rigorously bounded below (not just floating-point-estimated) by a
value exceeding $1.0$.

The verifier `library.primitive_set_witness.verify_witness` checks:
1. All elements $\geq x_\text{floor}$.
2. Pairwise non-divisibility (primitivity).
3. Rigorous lower bound on the sum (using `decimal` arithmetic with ULP slack)
   exceeds `witness_threshold = 1.0`.

To commit a witness, embed a `<!-- WITNESS ... WITNESS -->` block at the
bottom of this file (see format in the preamble).

**Important caveat**: Even if the verifier accepts a witness, the conjecture is
about the limit $x \to \infty$. A sum exceeding 1 at finite $x_\text{floor}$ is
only a genuine counterexample if the $o(1)$ correction at that $x_\text{floor}$
is small enough. This requires an additional analytical argument; the verifier
alone does not settle the matter.

### Anti-traps (the canonical failure modes)

- **F2 sign confusion**: Do not conclude $\sum > 1$ from F2 alone.  The
  big-O is unsigned.
- **F3 upside-down**: F3's correction is negative; the sum approaches 1 from
  BELOW, not above.
- **Asserting resolution**: Do not assert that the conjecture is settled or
  announce $\square$ / end-of-proof markers without a verifier-accepted
  `<!-- WITNESS -->` block.

---

## Section 2: Numerical evidence (Q2, Q3)

*(to be filled in Round 2)*

## Section 3: Proof structure — omega-stratification approach

*(to be filled in Round 3)*

## Body (working proof draft)

*(The agent fills in the body round by round.)*
