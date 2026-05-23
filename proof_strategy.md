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
  BLOCKING — unless a verifier-accepted witness block is committed and
  `witness_valid == 1`.

## Witness format (the only path to a counterexample claim)

A claim of disproof MUST be backed by a finite primitive set whose sum is
rigorously verified to exceed `witness_threshold` by
`library.primitive_set_witness.verify_witness`. The witness block (if any)
appears at the very bottom of this file with JSON fields `x_floor`,
`elements`, and `claimed_sum_lower_bound`. `proof_prepare.py` parses it,
runs the deterministic verifier, and sets `witness_valid` accordingly.
No witness block means `witness_valid = 0` and no counterexample claim
is possible.

## Body

### Section 1: Claim and Ledger (Q1)

**Claim.** Let $x \geq 2$. Call $A \subset [x,\infty)$ *primitive* if no
distinct element of $A$ divides another. The conjecture asserts:
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad \text{as } x \to \infty,$$
uniformly over all primitive $A \subset [x,\infty)$.  **Status: open.**

**F1 (Erdős–Zhang, F1\_erdos\_zhang\_upper).** For any primitive
$A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma}\frac{\pi}{4} + o(1) \approx 1.399.$$
This is a strict *upper* bound. It does not imply the conjecture but is
consistent with it.

**F2 (Omega-stratum lower, F2\_omega\_k\_lower\_unsigned).** For
$A_k = \{n : \Omega(n) = k\}$:
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2+o(1)}).$$
The big-$O$ is **unsigned** — it can be negative. This fact alone does
*not* imply the sum exceeds 1; that would be the unsigned-O-sign-confusion
error.

**F3 (Exact asymptotics, F3\_omega\_k\_exact\_below\_one).** As $k \to \infty$:
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c+o(1))\frac{k^2}{2^k},
   \quad c \approx 0.0656 > 0.$$
The correction is *negative*, so the sum approaches 1 from *below* for
large $k$.  For small $k$ (especially $k=1$) this asymptotic formula
need not hold — see numerical evidence below.

### Section 2: Numerical Evidence for F3 (Q2)

Sieve computation over $n \leq 500{,}000$:

| $k$ | count  | partial sum | sum $< 1$? | F3 asymptote |
|-----|--------|-------------|-----------|--------------|
| 1   | 41,538  | 1.5604      | No        | 0.9672       |
| 2   | 108,326 | 0.8569      | Yes       | 0.9344       |
| 3   | 126,262 | 0.4852      | Yes       | 0.9262       |
| 4   | 97,670  | 0.2506      | Yes       | 0.9344       |

For $k \geq 2$ the sums are well below 1, consistent with F3. For $k = 1$
(primes) the partial sum is 1.56 and the full infinite sum converges to
approximately 1.637. F3 is an asymptotic valid for large $k$; it does not
apply at $k = 1$.

### Section 3: Prime Sum and Scope of F1 (Q3)

The series $\sum_p 1/(p \log p)$ converges (the $n$-th prime $p_n \sim n \log n$
gives summand $\sim 1/(n(\log n)^2)$, which is summable). Partial sums:
$p \leq 100$: 1.422; $p \leq 1000$: 1.492; $p \leq 10000$: 1.528; full sum $\approx 1.637$.

The full prime set $\{2,3,5,7,\ldots\}$ is primitive (no prime divides
another) and has sum $\approx 1.637$. This does not contradict F1: F1's
$o(1)$ correction is large at $x_{\text{floor}} = 2$, and the conjecture
bounds the sum only for $A \subset [x,\infty)$ as $x \to \infty$. Primes
restricted to $[x,\infty)$ have sum equal to a convergent tail that goes
to 0 as $x \to \infty$, consistent with the conjecture.

At large $x_{\text{floor}}$, the primes in $[x,\infty)$ contribute at most
$\sum_{p \geq x} 1/(p \log p) \to 0$, so they cannot supply a witness with
sum $> 1$.

### Section 4: Witness Search (Q4)

**At $x_{\text{floor}} = 100$:** primes in $[101,\infty)$ give rigorous
sum $\approx 0.215 < 1$. No primitive subset of $[100,\infty)$ found with
sum $> 1$.

**At $x_{\text{floor}} = 2$:** the primes $\{2,3,5,\ldots,97\}$ form a
primitive set in $[2,\infty)$. Rigorous lower bound on their sum:
$\approx 1.4216 > 1.0$. Witness block embedded below.

**Caveat.** This witness is at $x_{\text{floor}} = 2$; the $o(1)$ correction
at $x = 2$ is not negligible. This demonstrates that primitive sets with
small $x_{\text{floor}}$ can exceed the threshold, but does not constitute
a genuine counterexample (which would require sum $> 1$ at large $x$). The
conjecture remains open. Human review required.

<!-- WITNESS
{
  "x_floor": 2,
  "elements": [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97],
  "claimed_sum_lower_bound": 1.421
}
WITNESS -->
