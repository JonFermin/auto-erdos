# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

## Section 1 — Setup

### The claim

**Erdős's primitive-set conjecture (tightened form)**: for any $x \geq 2$,
let $A \subset [x, \infty)$ be a *primitive set* of integers — a set where
no distinct element divides another. Then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where $o(1) \to 0$ as $x \to \infty$. The conjecture posits that primes in
$[x, \infty)$ are extremal in the limit.

**Claim status**: open. Resolution requires either a proof or a
verifier-accepted witness (see Witness contract below).

---

### Given facts (with sign disambiguations)

**F1 (Erdős 1935; Zhang 1993 — UPPER bound).**  
For any primitive $A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
This is an **upper** bound — the sum is less than $\approx 1.399$. It is
consistent with the conjecture (which asks for the tighter bound of
$1 + o(1)$). Misreading it as a lower bound is a sign error.

**F2 ($\Omega$-stratum lower bound — UNSIGNED big-O).**  
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity):
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$
The $O(\cdot)$ is **unsigned** — it could be positive or negative. This
says the sum is at least $1$ minus some quantity bounded in absolute value
by $k^{-1/2+o(1)}$. It does **not** imply the sum exceeds $1$. Using F2
alone to conclude $\sum > 1$ is a sign error — `unsigned-O-sign-confusion`.

**F3 (exact asymptotic — sum approaches $1$ from BELOW).**  
For $A_k$ as above:
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
The leading correction is **negative** for all $k \geq 1$. The sum is
strictly less than $1$ and approaches $1$ from below as $k \to \infty$.
The full $\Omega(n) = k$ stratum is consistent with the conjecture.

---

### Witness contract

To attempt a counterexample: embed a `<!-- WITNESS ... WITNESS -->` block
at the bottom of this file with fields `x_floor` (int $\geq 2$),
`elements` (list of pairwise non-divisible integers each $\geq x_\text{floor}$),
and `claimed_sum_lower_bound` (float). The verifier recomputes the sum in
high-precision arithmetic. If the rigorous lower bound exceeds $1.0$,
`witness_valid` is set to 1 and the round is `keep_disproof`.

Even a valid witness requires human review: the conjecture has an $o(1)$
caveat, so a witness barely exceeding $1$ at small $x_\text{floor}$ may
fall within the $o(1)$ margin.

---

## Section 2 — Numerical Evidence

*(To be filled: F3 numerical check for k=1,2,3,4 and prime-sum check.)*

---

## Section 3 — Proof Strategy

*(To be filled: lemma decomposition and stratum bound argument.)*
