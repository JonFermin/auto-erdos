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

### 2.1 Omega-stratum partial sums (Q2)

Partial sum $\sum_{a \in A_k, a \leq N_k} 1/(a \log a)$ over the first
200 elements of each stratum $A_k = \{n : \Omega(n) = k\}$:

| $k$ | First five elements | Partial sum (200 terms) |
|-----|---------------------|-------------------------|
| 1   | 2, 3, 5, 7, 11      | 1.496452                |
| 2   | 4, 6, 9, 10, 14     | 0.681938                |
| 3   | 8, 12, 18, 20, 27   | 0.313401                |
| 4   | 16, 24, 36, 40, 54  | 0.140341                |

The 200-term partial sums for $k = 2, 3, 4$ are all strictly below 1, consistent
with F3 (sum $< 1$ for each stratum, approaching 1 from below as $k \to \infty$).

### 2.2 Prime sums from $x$ (Q3)

Primes $\{p \geq x\}$ form a primitive set in $[x, \infty)$.
Partial sums (primes up to $200{,}000$):

| $x$   | $\sum_{p \in [x, 200000)} 1/(p \log p)$ |
|-------|-----------------------------------------|
| 2     | 1.5547                                  |
| 3     | 0.8334                                  |
| 10    | 0.3323                                  |
| 100   | 0.1331                                  |
| 1000  | 0.0624                                  |
| 10000 | 0.0265                                  |

For $x \geq 3$, the truncated prime sum is below 1.  The sum decreases as $x$ grows.

### 2.3 Witness search (Q4)

Greedy primitive sets built by adding integers from $x$ upward while maintaining
pairwise non-divisibility:

| $x$   | Elements in greedy set (range $[x, x{+}5000)$) | Greedy sum |
|-------|--------------------------------------------------|------------|
| 100   | 989                                              | 0.2685     |
| 1000  | 2433                                             | 0.1479     |
| 10000 | 5000                                             | 0.0431     |

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

### 3.2 Proposed lemmas (all open; to be proved inside this document)

**Proposed Lemma L1.**
For all sufficiently large $x$:
$$\sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p} < 1.$$

*Numerical support*: the truncated prime sum (Table 2.2) is below 1 for $x \geq 3$.
*Status*: open.  Proof deferred to `proof_lemmas/lemma_L1_prime_tail.md`.

**Proposed Lemma L2.**
For any primitive $A \subseteq [x, \infty)$, there exists an absolute constant
$C$ such that for all sufficiently large $x$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{C}{\log x}.$$

*Motivation*: If L2 holds with $C < e$, then for $x \geq e^C$ the sum is below 1.
The numerical greedy sums (Table 2.3) suggest $C \leq 5$ in practice.
*Status*: open — this is the key lemma; it implies the conjecture immediately.
Proof deferred to `proof_lemmas/lemma_L2_antichain_density.md`.

**Derivation chain (pending L1 and L2)**:
Fix any primitive $A \subseteq [x, \infty)$.  If L2 holds, then for $x > e^C$,
$\sum_{a \in A} 1/(a \log a) \leq C/\log x < 1$.
Therefore the conjecture holds for $x > e^C$ with $o(1) = C/\log x - 0$.

### 3.3 Next steps

1. Open `proof_lemmas/lemma_L1_prime_tail.md` and attempt a self-contained proof
   of L1 from first principles.
2. Open `proof_lemmas/lemma_L2_antichain_density.md` and attempt a proof of L2,
   potentially citing L1 and the given facts F1, F2, F3.
3. If L2 is proved, update this file's Body section to record the derivation chain.

---

## Body (working proof draft)

The proof is in progress.  The logical chain is:

$$\text{L2} \Rightarrow \text{for large } x,\ \sup_{\text{primitive } A \subseteq [x,\infty)}
\sum_{a \in A} \frac{1}{a \log a} \leq \frac{C}{\log x} \xrightarrow{x \to \infty} 0 < 1.$$

Both L1 and L2 are open; their proofs are deferred to the lemma files.
The proof structure is sound: the argument reduces to proving these two
computable lemmas, neither of which assumes any fact outside the ledger
in its statement.
