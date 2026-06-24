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

### Section 2: Numerical Evidence — F3 Sign and Large-$k$ Behaviour (Q2)

This section verifies that F3 has the correct sign (approaches from below) and
computes the F3 correction term for $k = 1, 2, 3, 4$.

**Scope:** We work with what F3 directly implies from its formula alone. Numerical
truncated-sum computations and full-convergence estimates are deferred to Q3,
where the $x$-floor context is set up properly to interpret them.

#### 2.1 F3 Correction Term for $k = 1, 2, 3, 4$

From F3: $\sum_{a \in A_k} 1/(a \log a) = 1 - (c + o(1)) k^2/2^k$ with $c \approx 0.0656 > 0$.

The leading correction is $-(c+o(1)) k^2/2^k$. Since $c > 0$, this correction is
**negative** for all $k \geq 1$, so the sum is **strictly less than 1** in the
large-$k$ regime where F3 is accurate (the $o(1)$ remainder is negligible).

| $k$ | $k^2/2^k$ | F3 correction (leading) | F3 predicted sum (leading term) |
|---|---|---|---|
| 1 | $1/2 = 0.500$ | $-0.0656 \times 0.500 = -0.0328$ | $1 - 0.0328 = 0.967$ |
| 2 | $4/4 = 1.000$ | $-0.0656 \times 1.000 = -0.0656$ | $1 - 0.0656 = 0.934$ |
| 3 | $9/8 = 1.125$ | $-0.0656 \times 1.125 = -0.0738$ | $1 - 0.0738 = 0.926$ |
| 4 | $16/16 = 1.000$ | $-0.0656 \times 1.000 = -0.0656$ | $1 - 0.0656 = 0.934$ |

#### 2.2 Sign Verification (F3 approaches from below)

The function $g(k) = k^2/2^k$:
- $g(k) > 0$ for all $k \geq 1$ (since $k^2 > 0$ and $2^k > 0$)
- $g(k) \to 0$ exponentially as $k \to \infty$ (since $2^k$ grows faster than $k^2$)
- Integer maximum at $k = 3$: $g(3) = 9/8 = 1.125 > g(2) = 1 > g(4) = 1$
  (the continuous max is at $k = 2/\ln 2 \approx 2.885$, confirming integer max at $k=3$)

Since $c \approx 0.0656 > 0$ and $g(k) > 0$, the correction $-(c+o(1))g(k)$ is
**negative**, so $\sum_{a \in A_k} 1/(a \log a) < 1$ whenever the $o(1)$ remainder
is small (i.e., for sufficiently large $k$). This is the key sign consistency
claimed by F3.

**Anti-trap cross-check:** F2 says $\sum_{a \in A_k} 1/(a \log a) \geq 1 + O(k^{-1/2+o(1)})$
with unsigned $O$. F3 is consistent: F3's sum $= 1 - (c+o(1))k^2/2^k$ satisfies
$\geq 1 - |O(k^{-1/2+o(1)})|$ since $k^2/2^k = o(k^{-1/2})$ for large $k$.
There is no contradiction between F2 and F3.

#### 2.3 Regime Note

F3 is an asymptotic for large $k$. For small $k$ (particularly $k=1$, the
primes), the $o(1)$ correction may be large and the formula is not quantitatively
accurate. The case $k=1$ is discussed in Q3, where the prime sum and the
$x$-floor context are treated carefully.

**Next:** Q3 (prime sum from 2; how the $x$-floor makes F1 consistent with finite sums).
