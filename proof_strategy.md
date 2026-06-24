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
  Resolution phrases trigger `critic_openness`'s
  `open-claim-asserted-resolved-without-witness` BLOCKING — unless a
  verifier-accepted `<!-- WITNESS -->` block is committed and
  `witness_valid == 1`. Do NOT write resolution claims in the body.

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

#### 1.1 The Claim

We are studying **Erdős's primitive-set conjecture** (tightened form):

> **Conjecture.** For any $x \geq 2$, if $A \subseteq [x, \infty)$ is a *primitive set*
> (a set of positive integers where no element divides another distinct element),
> then
> $$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1),$$
> where the $o(1)$ term tends to $0$ as $x \to \infty$.

In words: the "Erdős measure" $\sum 1/(a \log a)$ of any primitive set drawn
from $[x, \infty)$ cannot exceed $1$ once $x$ is large enough. The conjecture is
**open**. No resolution may be claimed in this file without a verifier-accepted
witness.

**Why this measure?** The function $f(a) = 1/(a \log a)$ is the natural one
for primitive sets. The weight $1/(a \log a)$ makes the sum convergent
over infinite primitive sets (unlike $\sum 1/a$ which diverges even for
the primes by Mertens' second theorem $\sum_{p \leq x} 1/p \sim \log\log x$).
Restricting to $A \subset [x, \infty)$ tames the sum further:
$\sum_{a \in A, a \geq x} 1/(a \log a) \to 0$ as $x \to \infty$ for any
fixed primitive set. F3 shows the stratum $A_k$ is the "hardest" to control:
for large $k$, the sum over $A_k$ approaches 1 from below.

#### 1.2 The Three Given Facts

**F1 — Erdős-Zhang global upper bound.**
For *any* primitive set $A \subseteq \mathbb{N}$ (with no floor restriction),
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
Sign disambiguation: this is a **strict upper bound**; the sum is less than 1.399.
It does not say the sum can reach 1.399, nor that it exceeds 1.
F1 is consistent with the conjecture (which claims the tighter bound of 1 for
$x$-restricted sets). F1 does **not** give a lower bound.

**F2 — $A_k$ lower bound (unsigned big-O).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors, counting multiplicity). Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$
Sign disambiguation: the $O(\cdot)$ term is **unsigned** — it is bounded in
*absolute value* by $k^{-1/2+o(1)}$. Equivalently: the sum is at least
$1 - C k^{-1/2+o(1)}$ for some constant $C > 0$, which is less than 1.
Concluding "sum > 1" from F2 alone is a **sign error** (the canonical
ChatGPT failure mode — see anti-trap above).

**F3 — $A_k$ exact asymptotic (approaches 1 from below).**
For the same $A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
Sign disambiguation: the correction $-(c+o(1))k^2/2^k$ is **negative** (since
$c > 0$). So the sum is **strictly less than 1** for every finite $k \geq 1$,
approaching $1$ **from below** as $k \to \infty$.
F3 refines F2: it shows not only $\geq 1 - \varepsilon_k$ but also $\leq 1 - \varepsilon_k$
(up to lower-order terms), pinning the sum to $1 - (c+o(1))k^2/2^k$.

#### 1.3 Witness Contract

A claim of counterexample **requires** a verifier-accepted witness block at the
bottom of this file. Concretely:

1. Choose an integer $x_{\text{floor}} \geq 2$.
2. Produce a finite primitive set $A \subseteq [x_{\text{floor}}, \infty)$
   (all elements $\geq x_{\text{floor}}$, pairwise non-divisible).
3. Embed in this file exactly one block:
   ```
   <!-- WITNESS
   { "x_floor": <int>, "elements": [<int>, ...], "claimed_sum_lower_bound": <float> }
   WITNESS -->
   ```
4. `proof_prepare.py` parses the JSON, invokes
   `library.primitive_set_witness.verify_witness`, and sets `witness_valid = 1`
   iff the rigorously computed sum exceeds `witness_threshold = 1.0`.
5. A counterexample claim is only valid if `witness_valid == 1`.

Without a passing witness, the conjecture remains open by this harness. Note
the $o(1)$ caveat: even a finite witness with sum $> 1$ is only a candidate
counterexample; the $o(1)$ correction at the witness's $x_{\text{floor}}$
must also be estimated to turn it into a true disproof. That analysis is a
human-review step.

#### 1.4 Proof Strategy Overview

Two complementary tracks:

**Track A (search for a counterexample):** Try to construct a primitive set in
$[x_{\text{floor}}, \infty)$ with sum $> 1.0$. Q4 explores this numerically.
Given that F3 shows the "canonical" extremal sets ($A_k$) all achieve sums
$< 1$, a counterexample (if it exists) would need to combine elements from
many different strata. This seems unlikely but has not been ruled out.

**Track B (prove the conjecture):** Stratify $A$ by $\Omega(a) = k$ and bound
the contribution of each stratum. For each stratum $A \cap A_k$, we want
the contribution to be $< 1 - (c+o(1))k^2/2^k$. The difficulty is that
summing these bounds over all $k$ gives a series $\sum_k 1$ which diverges.
The key missing ingredient is that the *sub-primitive-set* structure means
only one stratum can be "close to 1" at a time; this needs formalization.
Q5 explores whether cross-stratum sub-additivity can be made precise.

**Next:** Q2 (numerical verification of F3 for small $k$).

---

### Section 2: Numerical Evidence — F3 for Small $k$ (Q2)

We computed the partial sum $S_k(N) = \sum_{a \in A_k, a \leq N} \frac{1}{a \log a}$
for the first 200 elements of each $A_k$ using a prime-factor sieve.
**All results in this section are partial sums (finite truncations), not claims
about the full series.** Discussion of full-series limits is deferred to Q3 and Q5.

#### 2.1 Truncated Sums (first 200 elements of $A_k$)

| $k$ | Partial sum (200 elems) | $200^{\text{th}}$ element | F3 correction $-(c+o(1))k^2/2^k$ | F3 predicted total |
|---|---|---|---|---|
| 1 | 1.4965 | 1223 | $\approx -0.0328$ | 0.967 |
| 2 | 0.6819 | 669 | $\approx -0.0656$ | 0.934 |
| 3 | 0.3134 | 422 | $\approx -0.0738$ | 0.926 |
| 4 | 0.1403 | 308 | $\approx -0.0656$ | 0.934 |

Here $c \approx 0.0656$ from F3.

#### 2.2 Interpretation of the Truncated Sums

**For $k \geq 2$:** The partial sums for $k = 2, 3, 4$ are all below 1 ($0.68$, $0.31$, $0.14$
respectively). These are truncations at the 200th element; the full series
continues to grow but is bounded. F3 predicts the full sums converge to
approximately $0.93$, $0.93$, $0.93$ for $k = 2, 3, 4$.

**For $k = 1$ (primes):** The partial sum over the first 200 primes ($p_1 = 2, \ldots,
p_{200} = 1223$) is 1.4965, which exceeds 1. This is consistent with
the conjecture's $x$-floor structure: the conjecture bounds
$\sum_{a \in A, a \geq x} 1/(a \log a)$ (the TAIL starting at $x$), not the
cumulative sum from $a = 2$. The first 200 primes include the small primes
(whose contributions $1/(p \log p)$ are large), which would not appear in a
set $A \subset [x, \infty)$ for any moderate $x$.

**Critical distinction:** Q2 verifies the consistency of F3 as a large-$k$ asymptotic.
The partial sum for $k=1$ being $> 1$ does not contradict F3, which predicts
the FULL sum for $A_k$ (for large $k$) approaches 1 from below. For small $k$,
the $o(1)$ correction is large and the formula is not quantitatively accurate.

#### 2.3 F3 as a Large-$k$ Asymptotic

F3 gives $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1))k^2/2^k$ with $c > 0$.
The sign is correct: the correction is negative, so the sum approaches 1 from below.

**Maximum of the correction term:** The function $g(k) = k^2/2^k$ attains its
maximum over positive integers at $k = 3$ (where $g(3) = 9/8 = 1.125$), and
decreases to 0 exponentially as $k \to \infty$. (Treating $k$ as continuous:
$g'(k) = k(2 - k\ln 2)/2^k = 0$ at $k = 2/\ln 2 \approx 2.885$, confirming
the integer max is at $k = 3$.)

| $k$ | $k^2/2^k$ | F3 predicted sum |
|---|---|---|
| 1 | 0.500 | 0.967 |
| 2 | 1.000 | 0.934 |
| 3 | 1.125 | 0.926 (minimum) |
| 4 | 1.000 | 0.934 |
| 5 | 0.781 | 0.949 |
| 10 | 0.098 | 0.994 |
| 20 | 0.00038 | $\approx 1.000$ |

As $k \to \infty$, $k^2/2^k \to 0$, so the F3 sum approaches 1 from below.
**Consistency check:** F3's correction $-(c+o(1))k^2/2^k < 0$ keeps the sum
below 1 for all $k$, consistent with the conjecture's bound of $1 + o(1)$.

#### 2.4 Consistency with F1 and the Conjecture

F1 ($< 1.399 + o(1)$) and the conjecture ($< 1 + o(1)$) apply to sets
$A \subset [x, \infty)$ as $x \to \infty$. For a fixed large $x$:
$\sum_{a \in A_k, a \geq x} 1/(a \log a) \to 0$ for any fixed $k$, which is
trivially $< 1$. The interesting regime is when $k$ grows with $x$, and F3
shows that even in that regime the sum stays below 1.

**Next:** Q3 (prime sum structure, consistency of the $x$-floor restriction with F1).
