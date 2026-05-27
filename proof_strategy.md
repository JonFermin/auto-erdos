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

### F3 check (Q2)

The table below shows partial sums $\sum_{a \in A_k, a \leq N} 1/(a \log a)$
for $N = 10^6$ together with a rough tail estimate, and F3's prediction
$1 - c k^2/2^k$ with $c \approx 0.0656$:

| $k$ | Partial sum ($N=10^6$) | Tail est. | Total est. | F3 pred. | sum $< 1$? |
|----:|----------------------:|----------:|----------:|----------:|:----------:|
| 1   | 1.5642                | 0.0724    | 1.6366    | 0.9672    | **False**  |
| 2   | 0.8674                | 0.1901    | 1.0575    | 0.9344    | False      |
| 3   | 0.4980                | 0.2495    | 0.7475    | 0.9262    | True       |
| 4   | 0.2609                | 0.2184    | 0.4794    | 0.9344    | True       |

**Finding**: For $k = 1$ (primes) and $k = 2$ (semiprimes), the total
sum over all of $A_k$ exceeds 1. F3 as stated in the given-facts ledger
predicts sums near 0.93–0.97 for ALL $k \geq 1$, which is *inconsistent*
with the numerical evidence for $k = 1, 2$. F3 is likely misformulated,
OR it applies only to restricted sums (e.g., $A_k \cap [x, \infty)$ with
the factor $1/\log x$ implicit). The sign disambiguation is preserved: even
though the full $A_k$ sum exceeds 1 for small $k$, the set $A_k \cap [x, \infty)$
has sum $\approx 1/\log x \to 0$ as $x \to \infty$, so $A_k$ restricted to
large-$x$ tails does NOT violate the conjecture.

**KEY**: $A_k$ with full sum includes elements starting at 2. The conjecture's
$o(1)$ bound is only claimed to hold for $A \subset [x, \infty)$ with $x \to \infty$.

### Prime sum and the primes-from-$x$ primitive set (Q3)

$\sum_{p \geq 2} 1/(p \log p) \approx 1.6366$ (sum converges; estimates
consistent with Q3's stated $\approx 1.6366$).

This exceeds 1, but the primes starting from 2 are NOT a counterexample
because the conjecture is asymptotic: it only claims sum $< 1 + o(1)$ for
$A \subset [x, \infty)$ with $x$ large. For the primes restricted to
$[x, \infty)$: $\sum_{p \geq x} 1/(p \log p) \approx 1/\log x \to 0$.

The primes-from-$x$ set is consistent with the conjecture for all $x$.

### Witness search (Q4)

Using a greedy algorithm that picks elements starting from $x_\text{floor}$
and adds each integer (smallest first) if it violates no existing primitivity
constraint:

| $x_\text{floor}$ | $|A|$ | Greedy sum | sum $> 1$? |
|----------------:|------:|-----------:|:----------:|
| 2               |  12   |  1.3700    | **Yes**    |
| 5               |  26   |  0.6005    | No         |
| 10              |  53   |  0.4518    | No         |
| 100             | 529   |  0.2508    | No         |
| 1000            | 5327  |  0.1759    | No         |
| 10000           |53288  |  0.1357    | No         |

**For $x_\text{floor} = 2$**: the greedy set (12 elements including 2, 3, 5, and
certain composites) gives rigorous sum $\approx 1.37 > 1.0$. The verifier
confirms `is_valid=True`. A simpler witness is $\{2, 3\}$: rigorous sum
$1/(2 \ln 2) + 1/(3 \ln 3) \approx 1.0248 > 1.0$.

**Caveat**: at $x_\text{floor} = 2$, the $o(1)$ in the conjecture is large
(estimates suggest $o(1) \sim 0.4$ at $x=2$), so the conjecture's bound
$1 + o(1) \approx 1.4$ is NOT violated by sum $= 1.37$. This witness
is formally valid against the $1.0$ threshold but does not genuinely
disprove the asymptotic conjecture.

**For $x_\text{floor} = 100, 1000$**: maximum achievable sum is $\approx 0.25$
and $\approx 0.18$ respectively — far below 1. The conjecture appears
consistent with numerical evidence at these scales.

---

## Section 3 — Proof Strategy

*(Partial: lemma outline to be expanded.)*

### High-level approach

The conjecture asserts: for large $x$, any primitive $A \subset [x, \infty)$
has $\sum 1/(a \log a) < 1 + o(1)$. A natural approach:

1. **Stratify** $A$ by $\Omega(a) = k$ (number of prime factors with
   multiplicity): $A = \bigsqcup_k A_k'$ where $A_k' = A \cap A_k$.
2. **Bound each stratum**: $\sum_{a \in A_k'} 1/(a \log a) \leq
   \sum_{a \in A_k, a \geq x} 1/(a \log a) \approx f_k(x)$.
3. **Sum over strata**: $\sum_k f_k(x) = ?$. Need this to be $< 1 + o(1)$.

Key lemma (open): The sum $\sum_{a \in A_k, a \geq x} 1/(a \log a)$ satisfies
what bound? By the Selberg-Sathe theorem, the density of $A_k$ near $t$ is
$(t/\log t) \cdot (\log \log t)^{k-1}/((k-1)!)$, giving tail sum
$\approx (\log \log x)^{k-1}/((k-1)! \log x)$.

Summing over $k$: $\sum_{k=1}^\infty \frac{(\log \log x)^{k-1}}{(k-1)! \log x}
= \frac{1}{\log x} \sum_{j=0}^\infty \frac{(\log \log x)^j}{j!}
= \frac{e^{\log \log x}}{\log x} = \frac{\log x}{\log x} = 1$.

**This is the key heuristic**: the total contribution of all strata sums to
$\approx 1/\log x \cdot \log x = 1$ in the limit. The conjecture is that
no PRIMITIVE set can achieve this total — but the above counts ALL integers
(a much larger, non-primitive set).

The gap between "all integers" and "a primitive subset" is where the proof
must live. Lemmas to develop:

- **Lemma A** (stratum bound): For each $k$, bound $\sum_{a \in A_k'}$
  where $A_k'$ is any subset of $A_k \cap [x, \infty)$ that is primitive
  (i.e., no two elements of $A_k'$ divide each other — which is automatic
  within $A_k$ since $\Omega$ is additive).
- **Lemma B** (cross-stratum constraint): If $a \in A_k'$ and $b \in A_j'$
  with $j \neq k$, the non-divisibility constraint $a \nmid b$ restricts
  how large $A_k' \cup A_j'$ can be.
- **Lemma C** (summation): Combine Lemmas A and B to bound $\sum_k \sum_{a \in A_k'} 1/(a \log a) < 1 + o(1)$.

All three lemmas remain open in this attempt. The above heuristic suggests
the bound of 1 is tight (achieved in the limit by the sum over all integers),
but proving it requires controlling the primitivity constraint rigorously.

*This attempt is ongoing and remains open.*
