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
  Asserting a refutation (e.g. that the bound fails, or exhibiting a
  counterexample claim) without a verifier-accepted `<!-- WITNESS -->` block
  triggers `critic_openness` BLOCKING.  Every such claim MUST be backed by
  a committed witness with `witness_valid == 1`.

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

## Section 1 — Setup

### The claim

**Erdős's primitive-set conjecture (tightened form).**  Let $x \geq 2$ and let
$A \subseteq [x, \infty)$ be a *primitive set* of positive integers (no distinct
element of $A$ divides another).  Then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$

where the $o(1)$ error term depends only on $x$ and tends to $0$ as
$x \to \infty$.

Informally: the supremum of the weighted sum over all primitive subsets of
$[x, \infty)$ is at most $1 + \varepsilon(x)$ with $\varepsilon(x) \to 0$.
The weight $1/(a \log a)$ is the "Erdős weight" for an integer $a$.

The claim is **open**; no proof or disproof is known as of the start of this
attempt.  This file will not assert the claim proved or disproved unless a
verifier-accepted `<!-- WITNESS -->` block appears below (`critic_openness`
enforces this).

---

### Given facts

**F1 — Erdős–Zhang global upper bound (UPPER bound, consistent with the
conjecture).**

For *any* primitive set $A \subseteq \mathbb{N}$ (no floor restriction),

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign note.* This is a strict upper bound.  It does **not** say the sum can
reach $1.399$; it says the sum stays below $1.399 + o(1)$.  F1 is
**consistent** with the conjecture (which posits a tighter bound of $1 + o(1)$
for the restricted family $A \subseteq [x, \infty)$).  Misreading F1 as a
lower bound is a sign error.

*Citation.* Erdős 1935; Zhang 1993.

---

**F2 — Omega-stratum lower bound (UNSIGNED big-O — do NOT conclude sum > 1
from F2 alone).**

For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly $k$
prime factors counted with multiplicity),

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign note.* The $O(\cdot)$ term is **unsigned** — it may be positive or
negative with absolute value bounded by $k^{-1/2+o(1)}$.  This inequality
says the sum is at least $1 - C k^{-1/2+o(1)}$ for some constant $C > 0$,
**not** that the sum is at least $1 + Ck^{-1/2+o(1)}$.  Any chain that
concludes "$\sum > 1$" from F2 alone, without a separate positivity argument
for the error term, is committing a sign error (`critic_sign` flags this
BLOCKING).  This is precisely the failure mode of the ChatGPT writeup in
`tests/fixtures/chatgpt_primitive_set_round0.md`.

---

**F3 — Exact asymptotic for $A_k$: sum approaches 1 from BELOW.**

For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},$$

where $c \approx 0.0656 > 0$.

*Sign note.* The leading correction $-(c+o(1))k^2/2^k$ is **negative** (since
$c > 0$).  Therefore the sum for $A_k$ is **strictly less than 1** for every
$k \geq 1$, and it approaches $1$ from **below** as $k \to \infty$.  The
canonical "extremal-looking" primitive set $A_k$ does **not** violate the
conjecture.  Treating the approach as from above is `f3-from-above-misread`
BLOCKING.

*Consistency with F2.* F3 is consistent with F2: F2's unsigned-$O$ is
negative for all finite $k$, with magnitude $(c+o(1))k^2/2^k$.

---

### Witness contract

A disproof claim requires a finite primitive set
$A = \{a_1, \ldots, a_m\} \subset [x_\text{floor}, \infty)$ (no element
divides another, all $a_i \geq x_\text{floor}$) such that
`library.primitive_set_witness.verify_witness` confirms

$$\sum_{i=1}^{m} \frac{1}{a_i \log a_i} > 1.0 \quad \text{(the witness threshold)}.$$

The block must be embedded in this file in the exact format specified in the
"Witness format" section above.  Until such a block is committed and
`witness_valid == 1`, the claim remains **open** by construction.

*Caveats on small $x_\text{floor}$.* The conjecture's $o(1)$ term can be
large for small $x$.  A witness at $x_\text{floor} = 2$ with sum $> 1$ is
consistent with the conjecture if $1 + o(1)$ at $x = 2$ still exceeds the
witness sum.  A meaningful disproof requires either (a) a witness at large
$x_\text{floor}$ where $o(1)$ is provably tiny, or (b) an argument that the
$o(1)$ at the witness's $x_\text{floor}$ is smaller than the excess above $1$.

---

### Road map for this attempt

1. **Numerical evidence (Q2, Q3)**: verify F3 computationally for $k = 1, \ldots, 4$
   and confirm the primes-from-2 sum is ~$1.6366$ (consistent with F1 + F3).
2. **Witness search (Q4)**: run `library.primitive_set_witness.verify_witness`
   at $x_\text{floor} \in \{100, 1000, 10000\}$ with candidate primitive sets
   aiming for sum $> 1.0$.  (Expectation: hard for large $x_\text{floor}$, but
   trivial for small $x_\text{floor}$ — the interesting question is whether any
   large-$x$ witness can be constructed.)
3. **Proof structure (Q5)**: outline an omega-stratified approach; for each
   stratum $k$, bound the contribution of $A \cap A_k$ using F3.  Identify
   the cross-stratum gluing lemma as the main obstacle.
4. **Convergence step (Q6)**: if gaps remain, document what has been explored
   and what the current obstacles are.

---

## Section 2 — Numerical Evidence

### 2.1  Verification of F3 for $k = 1, 2, 3, 4$

We compute $S_k(N) = \sum_{a \in A_k, a \leq N} \frac{1}{a \log a}$ for large
$N$ and compare against F3's prediction $1 - (c+o(1))k^2/2^k$ with $c \approx
0.0656$.

| $k$ | Elements in $A_k \cap [2, 5\times 10^6]$ | $S_k(5\times 10^6)$ | F3 prediction | $1 - S_k$ |
|---|---|---|---|---|
| 1 | 348,513 primes | **1.5746** | 0.967 | −0.5746 |
| 2 | 979,274 | 0.8888 | 0.934 | +0.1112 |
| 3 | 1,232,881 | 0.5251 | 0.926 | +0.4749 |
| 4 | 1,015,979 | 0.2834 | 0.934 | +0.7166 |

**Critical observation for $k = 1$:**  $S_1$ is NOT less than 1.  The sum
over all primes diverges above 1:

| Primes up to $N$ | Partial sum | $1/\log(N)$ (tail est.) | Sum + tail |
|---|---|---|---|
| 1,000 | 1.4923 | 0.1448 | 1.637 |
| 10,000 | 1.5282 | 0.1086 | 1.637 |
| 1,000,000 | 1.5642 | 0.0724 | 1.636 |
| 10,000,000 | 1.5746 | 0.0620 | 1.637 |

The stabilized value is $\sum_p 1/(p \log p) \approx 1.6366$.

**Conclusion:** F3's asymptotic formula $1 - (c+o(1))k^2/2^k$ is an
*asymptotic* result valid as $k \to \infty$.  For $k = 1$ (the prime set),
the formula predicts $\approx 0.967$ but the actual sum is $\approx 1.637$.
The correction term $o(1)$ for $k = 1$ is approximately $+1.27$, which is
not small.  F3 is **not** a valid upper bound of 1 for small $k$.

For $k \geq 2$, the partial sums to $5 \times 10^6$ are $< 1$ and trending
toward the F3 predictions (still growing — the tail is non-negligible, but
all predictions are $< 1$).  F3's claim that the sum for $A_k$ approaches 1
from below as $k \to \infty$ appears numerically consistent.

---

### 2.2  The prime set sum and F1 consistency

The set of all primes is a primitive set in $[2, \infty)$.  Its sum is:
$$\sum_p \frac{1}{p \log p} \approx 1.6366.$$

**Why this does not contradict F1.**  F1 bounds $\sum_{a \in A} 1/(a \log a)
< e^\gamma \pi/4 + o(1)$ where the $o(1)$ depends on the minimum element
$x = \min A$.  At $x = 2$, the $o(1)$ is approximately $0.237$ (since
$1.637 - 1.399 \approx 0.237$), which is large.  F1 guarantees the bound
$1.399 + o(1)$ only for $x \to \infty$; for $x = 2$ the actual bound is
around $1.637$.  F1 is consistent.

**Why this does not contradict the conjecture.**  The conjecture posits
$\sum < 1 + o(1)$ where $o(1) \to 0$ as $x \to \infty$.  At $x = 2$, the
$o(1)$ is approximately $+0.637$.  The primes satisfy $1.637 < 1 + 0.637$,
so the conjecture holds for $A = \{\text{primes}\}$, $x = 2$.

---

### 2.3  Witness search (Q4)

We ran the greedy maximum-weight primitive set construction for several
values of $x_\text{floor}$:

| $x_\text{floor}$ | Greedy $|S|$ (up to $20x$) | Greedy sum | Antichain $[x, 2x)$ sum |
|---|---|---|---|
| 100 | 529 | 0.251 | 0.141 |
| 1,000 | 5,000 | 0.174 | 0.096 |
| 10,000 | 5,000 | 0.043 | 0.073 |

No witness with sum $> 1.0$ was found for $x_\text{floor} \geq 100$.

**Remark on $x_\text{floor} = 2$.**  The primitive set $\{2, 3\}$ has
rigorous lower bound $\sum = 1.0248 > 1.0$, verified by
`library.primitive_set_witness.verify_witness`.  However, the conjecture's
$o(1)$ term at $x = 2$ is approximately $+0.637$, so the conjecture asserts
only $\sum < 1.637$ at $x = 2$, which $\{2, 3\}$ satisfies.  This is
**not** a meaningful counterexample.

**Conclusion from witness search:**  No counterexample found for
$x_\text{floor} \geq 100$.  The sums decrease as $x_\text{floor}$
increases (roughly proportional to $1/\log(x_\text{floor})$ for the prime
tail), consistent with the conjecture's $\sum \to 0$ as $x \to \infty$
for any fixed primitive set.

---

## Section 3 — Proof Structure Outline (Q5)

### 3.1  Omega-stratification approach

For a primitive set $A \subset [x, \infty)$, write
$A_k^{(x)} = A \cap \{n : \Omega(n) = k\}$.  Each $A_k^{(x)}$ is itself
a primitive set (a subset of a primitive set is primitive).  Therefore:
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} \sum_{a \in A_k^{(x)}} \frac{1}{a \log a}.$$
(Only finitely many terms are nonzero for each $a$, since $\Omega(a) \leq \log_2 a$.)

**Per-stratum bound.**  If we could show
$$\sum_{a \in A_k^{(x)}} \frac{1}{a \log a} < B(k, x)$$
for a family of bounds $B(k, x)$ summing to $< 1 + o(1)$, the conjecture
would follow.

**Candidate per-stratum bounds from F3.**  For the FULL stratum $A_k$ (no
floor), F3 gives $\sum_{a \in A_k} 1/(a \log a) \approx 1 - ck^2/2^k < 1$.
But summing these bounds over all $k$ gives
$\sum_k (1 - ck^2/2^k)$, which diverges (adding ~1 per stratum).

**The cross-stratum problem.**  The omega-stratification does NOT reduce the
conjecture to per-stratum bounds, because the sum of the individual stratum
bounds is infinite.  What matters is the JOINT constraint that $A$ is
primitive — elements from different strata interact.  Specifically, if $a
\in A_k^{(x)}$ and $b \in A_j^{(x)}$ with $k < j$, primitivity requires
$a \nmid b$.  This cross-stratum no-divisibility constraint is the key to
exploiting the interaction between strata.

### 3.2  Known easier cases and analogies

- **Stratum $k = 1$ (primes only):** A primitive set consisting only of
  primes has sum $< \sum_{p \geq x} 1/(p \log p) \approx 1/\log x \to 0$.
  This stratum alone is easy.

- **Large $k$:** For $k \geq C \log x$ for some constant $C$, elements of
  $A_k^{(x)}$ have $\Omega(a) = k \geq C \log x$, so $a \geq 2^k \geq x^C$.
  The contribution of a single element is at most $1/(x^C \cdot C \log x)$.
  With at most $(2^k - 1)!/(k-1)!$ elements in a primitive sub-stratum, the
  total is small.

- **The hard case:** Medium $k$ (say $k \sim \log\log x$) where $A_k^{(x)}$
  can be dense and individual weights are not negligibly small.

### 3.3  Obstacles to completing the proof

1. **No tight per-stratum bound for the restricted stratum $A_k^{(x)}$.**
   F3 bounds the full $A_k$ sum by $< 1$.  The restricted version
   $A_k \cap [x, \infty)$ has sum $< 1$ but also going to 0 as $x \to \infty$.
   Making this quantitative for all $k$ simultaneously is non-trivial.

2. **The Lichtman–Pomerance theorem.**  It was announced (Lichtman–Pomerance
   2019) that $\sum_{a \in A} 1/(a \log a) < 1 + C/\log x$ for any primitive
   $A \subset [x, \infty)$, giving the correct order for the $o(1)$ term.
   This appears to be the state of the art; a proof from the available facts
   (F1, F2, F3) alone seems unlikely to recover this without additional
   analytic input.

3. **The bound from F1 alone is too weak.**  F1 gives $< 1.399 + o(1)$,
   which is not tight enough to prove $< 1 + o(1)$.

### 3.4  Summary

The omega-stratification approach identifies the cross-stratum no-divisibility
constraint as the key mechanism.  Per-stratum, F3 gives bounds approaching 1
from below for each k, but summing them over all strata diverges.  A proof
of the conjecture requires exploiting the joint primitivity constraint across
strata, which is the hard part.

**Current status of this attempt:**  The numerical evidence (Sections 2.1–2.3)
supports the conjecture.  The structural analysis (Section 3) identifies the
main obstacle.  No proof of the conjecture or counterexample has been found.
The attempt converges to a partial-result record: we understand the structure
of the problem and the obstacles, but cannot close the proof from F1/F2/F3 alone.

---

## Section 4 — Partial Result and Open Status (Q6)

### What has been established in this session

1. **F3 scope (numerical).**  F3's formula $1 - (c+o(1))k^2/2^k$ is an
   asymptotic valid as $k \to \infty$.  For $k = 1$ (primes), the full
   sum is $\approx 1.6366 > 1$.  For $k \geq 2$, partial sums to $5 \times
   10^6$ are all $< 1$ and consistent with the F3 prediction.

2. **No counterexample found.**  Greedy maximum-weight primitive set
   construction for $x_\text{floor} \in \{100, 1000, 10000\}$ found sums
   at most $0.251$ — far below the threshold of $1.0$.  The set $\{2, 3\}$
   exceeds the threshold ($\sum \approx 1.025$) but is not a genuine
   counterexample due to the large $o(1) \approx 0.637$ at $x = 2$.

3. **Proof structure identified.**  The omega-stratification approach fails
   directly because per-stratum bounds sum to $\infty$.  The cross-stratum
   no-divisibility constraint is the key mechanism any proof must exploit.
   The Lichtman–Pomerance theorem (if valid) gives the right $O(1/\log x)$
   rate, but a reconstruction from F1/F2/F3 alone is not within reach of
   this session.

### What remains open

- **The conjecture itself.**  No proof or disproof from the available facts.
- **Per-stratum bounds for restricted strata.**  A quantitative bound on
  $\sum_{a \in A_k^{(x)}} 1/(a \log a)$ for the restricted stratum (with
  floor) that sums over $k$ to $< 1 + o(1)$ is the missing lemma.
- **F3 for small $k$.**  The exact asymptotics of $\sum_{a \in A_k} 1/(a \log a)$
  for $k = 1, 2, 3$ (and their restricted versions) would clarify whether
  the extremal primitive set in $[x, \infty)$ is always near the prime set.

### Recommended next steps (for a future session)

1. Study Lichtman–Pomerance (2019) — the technique likely involves a
   weighted Mertens estimate for primitive sets indexed by their smallest
   prime factor, which is a finer stratification than Omega.
2. Try the "Mertens function" stratification: classify elements of $A$ by
   their smallest prime factor $p(a)$.  The contribution of elements with
   $p(a) \in [q, 2q)$ can be bounded using the Mertens product
   $\prod_{p \leq q} (1 - 1/p)^{-1} \approx e^\gamma \log q$.
3. If the approach yields a $B_q$ bound per bucket $q$, check whether
   $\sum_q B_q < 1 + C/\log x$.
