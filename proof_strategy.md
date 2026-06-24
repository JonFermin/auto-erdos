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
for primitive sets because the primes form a primitive set and
$\sum_p 1/(p \log p)$ diverges (Mertens); restricting to $[x, \infty)$
tames the sum ($\sum_{p \geq x} 1/(p \log p) \to 0$), and the Omega-stratification
(see F3) shows the stratum $A_k$ is the "hardest" to control.

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

We computed the partial sum $S_k(N) = \sum_{a \in A_k, a \leq N} \frac{1}{a \log a}$ using a
prime-factor sieve up to $N = 3 \times 10^6$, and estimated the tail via the
Sathe-Selberg asymptotic density.

#### 2.1 Computed Values

| $k$ | $S_k(N)$ (partial, $N=3\text{M}$) | Elements counted | Tail estimate | Total estimate | F3 formula |
|---|---|---|---|---|---|
| 1 | 1.5696 | 216,816 | 0.067 | **1.637** | 0.967 |
| 2 | 0.8824 | 600,446 | ~0.25 | ~1.13 | 0.934 |
| 3 | 0.5169 | 743,937 | ~0.25 | ~0.76 | 0.926 |
| 4 | 0.2765 | 605,280 | ~0.22 | ~0.50 | 0.934 |

**F3 leading correction** $-(c+o(1))k^2/2^k$ with $c \approx 0.0656$:
- $k=1$: correction $\approx -0.0328$, predicted total $\approx 0.967$
- $k=2$: correction $\approx -0.0656$, predicted total $\approx 0.934$
- $k=3$: correction $\approx -0.0738$, predicted total $\approx 0.926$
- $k=4$: correction $\approx -0.0656$, predicted total $\approx 0.934$

#### 2.2 Key Discrepancy for $k=1$ and the Sign-Disambiguation Lesson

For $k=1$ ($A_1$ = all primes), the total $\sum_p 1/(p\log p) \approx 1.637$, confirmed
numerically by tracking partial sums and tail estimates via
$\text{tail} \approx 1/\log p_N$. This is the value from Q3's reference and is the
maximum of the Erdős measure over all primitive sets (the Lichtman-Pomerance
theorem).

**F3's formula $0.967$ is not close to $1.637$ for $k=1$.** This confirms that
F3 is an asymptotic as $k \to \infty$, not a formula valid for small $k$.
The $o(1)$ remainder in F3 is large (of order 1) for small $k$, and only
becomes negligible for $k \gg 1$.

#### 2.3 Consistency with the Conjecture and F1

The conjecture concerns $A \subset [x, \infty)$: restricting the floor to large $x$
makes ALL $A_k$ sums small (for fixed $k$, $\sum_{a \in A_k, a \geq x} 1/(a\log a) \to 0$).
The interesting regime is when $x$ is moderate and $k$ is large enough that
$A_k \cap [x, \infty)$ is non-trivially large.

F1 ($\leq 1.399 + o(1)$) and the conjecture ($\leq 1 + o(1)$) both apply to sets
in $[x, \infty)$ as $x \to \infty$. For $x = 2$ (no floor restriction), the
Lichtman-Pomerance bound is $\leq \sum_p 1/(p\log p) \approx 1.637$, which the
primes attain.

#### 2.4 Partial-Sum Checks (sign of F3 approach)

For $k \geq 3$, the partial sum $S_k(N)$ is well below 1 even for the first 200
elements (e.g., $S_3(200\text{th element}) \approx 0.313$, $S_4 \approx 0.140$).
The full sum for $k=3$ converges to roughly $0.76$ (with significant tail
uncertainty), and for $k=4$ to roughly $0.50$ — both well below 1.

For $k=2$, the full sum appears to converge to approximately $1.0$–$1.1$ (the
tail estimate is uncertain at $N = 3\text{M}$), possibly exceeding 1.

**Observation:** The Sathe-Selberg density estimate $\pi_k(x) \sim x(\log\log x)^{k-1} / ((k-1)! \log x)$
implies the total sum converges (the integral $\int_2^\infty (\log\log t)^{k-1} / (t \log^2 t) dt$
converges for all $k$), but convergence is very slow for $k \leq 3$.

**Working hypothesis:** F3 is reliable as $k \to \infty$ (where corrections are $O(k^2/2^k)$),
but for $k = 1, 2, 3, 4$ the true total sums are larger than the F3 formula predicts.
The evidence is compatible with F3 being correct in the limit and incorrect for small $k$.

**Next:** Q3 (prime sum from 2 onwards; consistency with F1 for finite x).
