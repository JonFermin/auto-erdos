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

## Section 2: Numerical evidence

Computed with Python `math.log` (natural logarithm, base $e$).  These are
floating-point computations; they are informational context, not formal proof steps.

### 2.1 Omega-stratum evidence (Q2)

Each stratum $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ is a primitive set:
if $a \mid b$ with $a, b \in A_k$ then $\Omega(b) \geq \Omega(a) + 1 > k$, contradicting $b \in A_k$.
By F3, $\sum_{a \in A_k} 1/(a \log a)$ approaches $1$ from below as $k \to \infty$.
These strata are extremal-looking but still consistent with the conjecture.

### 2.2 Prime sums from $x$ (Q3)

Primes $\{p \geq x\}$ form a primitive set in $[x, \infty)$.
Agent-computed partial sums using Python `math.log` (not cited from any external source):
primes $p \in [x, 200{,}000)$, for $x \geq 3$
(since $x = 2$ is the regime where the conjecture's $o(1)$ correction is large):

| $x$   | $\sum_{p \in [x, 200000)} 1/(p \log p)$ (agent-computed) |
|-------|-----------------------------------------------------------|
| 3     | 0.8334                                                    |
| 10    | 0.3323                                                    |
| 100   | 0.1331                                                    |
| 1000  | 0.0624                                                    |
| 10000 | 0.0265                                                    |

All agent-computed truncated prime sums are below 1, and the sum decreases as $x$ grows.
Consistent with the sub-goal L1 for these values of $x$.

### 2.3 Witness search (Q4)

Agent-computed greedy primitive sets (not cited from any external source):
built by adding integers from $x$ upward while maintaining pairwise non-divisibility:

| $x$   | Elements in greedy set (range $[x, x{+}5000)$) | Greedy sum (agent-computed) |
|-------|--------------------------------------------------|-----------------------------|
| 100   | 989                                              | 0.2685                      |
| 1000  | 2433                                             | 0.1479                      |
| 10000 | 5000                                             | 0.0431                      |

No primitive set with sum $> 1.0$ was found for $x \in \{100, 1000, 10000\}$.
At $x = 2$: the set $\{2, 3\}$ is a primitive set with floating-point sum
$\approx 1.025$; the regime $x = 2$ is outside the asymptotic scope where
the conjecture's $o(1)$ correction vanishes.

---

## Section 3: Proof structure and proposed lemmas

### 3.1 Proof goal and gap

Show: for any primitive $A \subseteq [x, \infty)$,
$\displaystyle\sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1)$ as $x \to \infty$.

F1 gives: for any primitive $A \subseteq \mathbb{N}$,
$\displaystyle\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399 + o(1)$.

The gap is: F1 bounds the sum at $\approx 1.399$, but the conjecture claims a
tighter bound of $1$.  Bridging this gap requires using the restriction
$A \subseteq [x, \infty)$ in an essential way.

### 3.2 Open sub-goals (detailed in proof_lemmas/)

Two open sub-goals are recorded in `proof_lemmas/`.  These are open questions being
investigated within this proof document; they are NOT claims asserted as established
results from external sources.

**Sub-goal L1 (see `proof_lemmas/lemma_L1_prime_tail.md`).**
*Question*: For all sufficiently large $x$, is the sum over primes $p \geq x$ of
$1/(p \log p)$ less than $1$?
*Agent-computed numerical support*: Table 2.2 shows this sum is well below $1$ for
all tested $x \geq 3$.
*Status*: open.  F1 bounds this prime sum at $< 1.399$ (not the needed $< 1$).

**Sub-goal L2 (see `proof_lemmas/lemma_L2_antichain_density.md`).**
*Question*: For any primitive $A \subseteq [x, \infty)$, does the sum
$\sum_{a \in A} 1/(a \log a)$ decay toward $0$ as $x \to \infty$?
*Motivation*: An affirmative answer to L2 would immediately imply the conjecture.
*Agent-computed numerical support*: Table 2.3 greedy sums fall sharply as $x$ grows.
*Status*: open — this is the central sub-goal; an affirmative answer implies the conjecture.

**Derivation chain (pending L2)**:
If sub-goal L2 is answered affirmatively (the sum decays to $0$ as $x \to \infty$),
then for any primitive $A \subseteq [x, \infty)$ and all large $x$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1),$$
which establishes the conjecture.  (Sub-goal L1 is a step toward L2 for the prime
stratum; it is not directly invoked in this derivation chain.)

### 3.3 Next steps

1. Open `proof_lemmas/lemma_L1_prime_tail.md` and attempt a self-contained proof
   of L1 from first principles.
2. Open `proof_lemmas/lemma_L2_antichain_density.md` and attempt a proof of L2,
   potentially citing L1 and the given facts F1, F2, F3.
3. If L2 is proved, update this file's Body section to record the derivation chain.

---

## Body (working proof draft)

The proof is in progress.  The logical chain is:

$$\text{L2 affirmative} \Rightarrow \text{for large } x,\ \sup_{\text{primitive } A \subseteq [x,\infty)}
\sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1).$$

### Status after Round 6

Sub-goals L1 and L2 (Section 3.2) are both OPEN.

**What $\{F1, F2, F3\}$ provide**: F1 bounds the sum for any primitive set at
$< e^\gamma \pi/4 + o(1) \approx 1.399$.  This bound holds for all primitive sets
and is independent of $x$.  F2 and F3 characterize the omega-stratum extremals
but do not give $x$-dependent decay.

**The gap**: The conjecture asks for a bound of $1 + o(1)$ as $x \to \infty$,
not the uniform bound $1.399$ that F1 provides.  Proving L2 (that the sum decays
toward $0$ as $x$ grows) requires going beyond $\{F1, F2, F3\}$.

**Counterexample search**: No primitive $A \subseteq [x, \infty)$ with sum $> 1$
was found for $x \in \{100, 1000, 10000\}$ by greedy search (Section 2.3).
The agent-computed evidence supports the conjecture but does not prove it.

### Partial result summary (Q6)

**What this proof attempt established**:

1. *Reduction*: The conjecture follows from sub-goal L2.  If for any primitive
   $A \subseteq [x,\infty)$ the sum $\sum_{a \in A} 1/(a \log a)$ decays toward
   $0$ as $x \to \infty$, then the conjecture holds.

2. *What was ruled out*: The three given facts $\{F1, F2, F3\}$ alone cannot
   establish L2 (or L1).  F1 gives a uniform $x$-independent bound of $1.399$;
   F2 is a lower bound on stratum sums; F3 gives the exact stratum asymptotic
   (approaching $1$ from below).  None of these provide the $x$-dependent decay
   that L2 asks for.

3. *Numerical evidence*: Agent-computed greedy primitive sets in $[x, \infty)$
   for $x \in \{100, 1000, 10000\}$ all have sums well below $1$, consistent
   with the conjecture.  No counterexample was found.

4. *Remaining gap*: L2 is open.  The proof of L2 requires estimates on how
   much of the total stratum sum is concentrated above $x$, which requires
   input beyond $\{F1, F2, F3\}$.

Detailed proof attempts and obstacle statements are in `proof_lemmas/`.
This attempt converges here as a partial result.
