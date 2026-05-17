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

## Sign cautions (F2 and F3)

- **F2 big-O is unsigned**: F2's lower bound $\geq 1 + O(k^{-1/2+o(1)})$ does NOT
  imply the sum exceeds 1 — the $O(\cdot)$ may be negative. Concluding
  $\sum_{A_k} > 1$ from F2 alone is a sign error.
- **F3 correction is negative**: F3 gives $= 1 - (c+o(1)) k^2/2^k$ with $c > 0$,
  so the sum is strictly below 1 for all $k \geq 1$.

## Witness contract

A counterexample requires embedding a verified witness block at the bottom of
this file (format: `<!-- WITNESS { "x_floor":..., "elements":[...],
"claimed_sum_lower_bound":... } WITNESS -->`). Without it, `witness_valid = 0`
and no counterexample claim is possible.

## Section 1 — Problem setup (Q1)

### The conjecture

Fix $x \geq 2$. Let $A \subseteq [x, \infty)$ be a **primitive set** — a set
of integers $\geq x$ with no element dividing another. Define

$$f(x) \;:=\; \sup_{\substack{A \subseteq [x,\infty) \\ A \text{ primitive}}} \;\sum_{a \in A} \frac{1}{a \log a}.$$

The conjecture asserts $f(x) = 1 + o_x(1)$, i.e., $f(x) \to 1$ as $x \to \infty$.

**Status**: open. No proof or counterexample exists. This file may not assert
resolution without a verifier-accepted witness.

### Ledger facts

**F1** (Erdős–Zhang upper bound): For any primitive $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \tfrac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
Sign: strict upper bound; consistent with the conjecture which posits a tighter bound.

**F2** (Omega-stratum, unsigned lower bound): For $A_k = \{n : \Omega(n) = k\}$,
$$\sum_{a \in A_k} \frac{1}{a \log a} \;\geq\; 1 + O(k^{-1/2+o(1)}).$$
Sign: the big-$O$ is unsigned (can be negative); this does NOT give sum $> 1$.

**F3** (exact Omega-$k$ asymptotic, approaches 1 from below): For $A_k$ as above,
$$\sum_{a \in A_k} \frac{1}{a \log a} \;=\; 1 - (c+o(1))\tfrac{k^2}{2^k}, \quad c \approx 0.0656 > 0.$$
Sign: correction is $-ck^2/2^k < 0$; sum is strictly less than 1 for all $k$.

F1 and F3 are consistent: F3 shows each $A_k$ stratum has sum $< 1 \leq 1.399$.
F2 and F3 are consistent: F3 confirms the exact value of the $O$-term in F2
(the term is negative for all $k$).

### What the facts imply

By F3, the canonical primitive sets $A_k$ (integers with exactly $k$ prime
factors counted with multiplicity) have sums approaching $1$ from below:
$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1)) k^2/2^k \to 1^-$ as $k \to \infty$.
These are conjectured to be near-extremal for the problem.

By F1, any primitive $A$ (unrestricted) has sum $< 1.399$. The conjecture asserts
the bound tightens to $1 + o_x(1)$ when $A \subseteq [x, \infty)$ for large $x$.

The ledger provides no fact that closes the gap between F1 ($\approx 1.399$) and
the conjectured bound ($1$) directly — that is the content of this proof attempt.

### Questions being pursued

- **Q2+Q3**: ✓ Numerical evidence (see Section 2 below).
- **Q4**: Witness search — try to construct a verified primitive set with sum $> 1$.
- **Q5**: Proof structure — stratify by $\Omega(a)$ and bound cross-stratum interaction.

## Section 2 — Numerical evidence (Q2 + Q3)

### Truncated $A_k$ sums for $k = 2, 3, 4$ (first 200 elements each)

Let $S_k^{(200)}$ = sum $1/(a\log a)$ over the first 200 elements of $A_k$ by
size, and $T_k$ = F3 leading-term value $1 - c k^2/2^k$, $c = 0.0656$.

| $k$ | $S_k^{(200)}$ | $T_k$ (F3 leading) | largest element |
|-----|-------------|-------------------|----------------|
| 2   | 0.6819      | 0.9344            | 669             |
| 3   | 0.3134      | 0.9262            | 805             |
| 4   | 0.1403      | 0.9344            | 1292            |

Each $S_k^{(200)}$ is strictly below 1, consistent with F3's statement that
the full $A_k$ sums are $< 1$. The partial sums are well below the F3
leading-term prediction $T_k$, indicating substantial tail contributions
from large elements; the series converges slowly from below to $T_k$.

The $k=1$ case (primes) is treated separately in Q4 (witness search), since
even the two-element set $\{2, 3\}$ has sum $\approx 1.024 > 1$, making it a
natural witness candidate (x_floor = 2).

### Primes restricted to $[x, \infty)$ for various $x$

A primitive subset of $\{p : p \geq x\}$ (a sub-set of primes $\geq x$) has
a sum bounded above by $\sum_{p \geq x} 1/(p \log p)$. Partial computations
(sieve to 200k, plus tail estimate $\approx 0.062$) give:

| $x_{\text{floor}}$ | partial sum (primes in $[x, 200\text{k}]$) |
|---|---|
| 5   | 0.530 |
| 10  | 0.332 |
| 100 | 0.133 |
| 1000 | 0.062 |

For $x \geq 5$, the full prime tail is $< 0.60 < 1$, so no finite or infinite
subset of primes in $[x, \infty)$ for $x \geq 5$ can achieve sum $\geq 1$.
This is consistent with the conjecture for $x \geq 5$.

For $x = 2$: the primes $\{2, 3\}$ already exceed sum $= 1$, making $x_{\text{floor}} = 2$
the regime of interest for the witness search (Q4).
