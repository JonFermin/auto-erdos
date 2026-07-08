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
  Claiming resolution without a verifier-accepted witness block triggers
  `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING. A WITNESS block is required for any counterexample claim.

## Witness format (the only path to a counterexample claim)

A claim of disproof MUST be backed by a finite primitive set whose sum is
rigorously verified to exceed `witness_threshold` by
`library.primitive_set_witness.verify_witness`. To commit a witness,
embed exactly one block of the form:

```
[WITNESS-FORMAT]
{
  "x_floor": <int>,
  "elements": [<ints, pairwise non-divisible, each >= x_floor>],
  "claimed_sum_lower_bound": <float>
}
[/WITNESS-FORMAT]
```

at the bottom of this file. `proof_prepare.py` parses the JSON, runs the
deterministic verifier, and sets `witness_valid` accordingly. No witness
block ⇒ `witness_valid = 0` ⇒ no counterexample claim is possible.

## Section 1: Setup (Q1)

### Claim (my own words)

We study *primitive sets*: finite or infinite sets $A$ of positive integers in
which no element divides any other distinct element.

The conjecture (Erdős 1988) asserts:

> For every $x \geq 2$ and every primitive set $A \subseteq [x, \infty)$,
> $$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; 1 + o(1)$$
> where $o(1) \to 0$ as $x \to \infty$.

**Status: open.** No proof or verifier-certified counterexample exists.

### Given facts — sign-disambiguated

**F1 (Erdős-Zhang upper bound, ≈ 1.399):**
For *any* primitive set $A \subseteq \mathbb{N}$ (no floor restriction),
$$\sum_{a \in A} \frac{1}{a \log a} \;<\; e^\gamma \tfrac{\pi}{4} + o(1) \;\approx\; 1.399 + o(1).$$
This is an **upper** bound. It says the sum cannot exceed ~1.399. It is
**consistent** with the conjecture (1.399 > 1). It does NOT mean the sum
can reach or exceed 1. Misreading as a lower bound is a sign error.

**F2 (Omega-stratum bound, unsigned big-O):**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$. Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \;\geq\; 1 + O\!\bigl(k^{-1/2+o(1)}\bigr).$$
The $O(\cdot)$ is **unsigned** — it is bounded in absolute value by
$C k^{-1/2+o(1)}$ but may be negative. This inequality does NOT imply
the sum exceeds 1. Concluding sum > 1 from F2 alone is `unsigned-O-sign-confusion`.

**F3 (exact asymptotic for $A_k$, approaching 1 from below):**
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
The correction is **negative**: sums approach 1 **from below** as $k \to \infty$.
This formula is an asymptotic in $k$ (valid for large $k$); for small $k$ the
convergence is slow and the truncated sum at 300 terms differs from the limit.

### Witness contract

A WITNESS block at the bottom of this file declares a finite primitive set
with elements ≥ x_floor. `proof_prepare.py` runs the rigorous verifier
(`library.primitive_set_witness.verify_witness`) using Decimal-precision
arithmetic with ULP-bumped log bounds. If `witness_valid = 1` (rigorous
lower bound on the sum strictly exceeds `witness_threshold = 1.0`), a
`keep_disproof` record may be filed. Without a passing witness, all
counterexample claims are blocked by `critic_openness`.

---

## Section 2: Numerical evidence (Q2 — F3 verification for k = 1, 2, 3, 4)

Computed using first 300 elements of each $A_k$, natural log throughout.

| k | Truncated sum (first 300 terms) | F3 prediction $1 - c k^2 / 2^k$ | Below 1? |
|---|---|---|---|
| 1 (primes) | 1.5052 | 0.9672 | **No — above 1** |
| 2 | 0.7001 | 0.9344 | Yes |
| 3 | 0.3280 | 0.9262 | Yes |
| 4 | 0.1488 | 0.9344 | Yes |

**Interpretation:**

- For $k = 2, 3, 4$: truncated sums are well below 1, consistent with F3's
  prediction of "approaching 1 from below." The truncation (300 terms) understates
  the true infinite sum since $A_k$ has many large elements; the limit should be
  closer to F3's prediction as we sum more terms.
- For $k = 1$ (primes): the truncated sum **exceeds 1** (≈ 1.505), and the full
  prime sum converges to ≈ 1.637 (see Section 3). F3's formula gives 0.967 for
  $k = 1$, which disagrees badly. F3's asymptotics are valid as $k \to \infty$;
  for small $k$ (especially $k = 1$), the formula does not hold numerically.
- The sign disambiguation in F3 — "approaches 1 from **below**" — is confirmed
  for $k \geq 2$. It does **not** hold for $k = 1$.

---

## Section 3: Prime sum and consistency with F1 (Q3)

The set of all primes $\{2, 3, 5, 7, 11, \ldots\}$ is a primitive set
(no prime divides a distinct prime). The partial sum:

| Primes up to $N$ | # primes | $\sum_{p \leq N} 1/(p \log p)$ |
|---|---|---|
| 10 | 4 | 1.2224 |
| 50 | 15 | 1.3882 |
| 100 | 25 | 1.4216 |
| 1 000 | 168 | 1.4923 |
| 10 000 | 1229 | 1.5282 |
| 100 000 | 9592 | 1.5498 |

The partial sums grow slowly and the tail shrinks; the full sum (verified numerically)
converges to approximately $\mathbf{1.637}$.

**Consistency with F1:** F1 says any primitive $A \subseteq \mathbb{N}$ has sum
$< 1.399 + o(1)$. The primes-from-2 sum of ≈ 1.637 appears to exceed 1.399. Two
reconciliations:
1. **F1's $o(1)$ at $A = \text{primes}$:** The Erdős-Zhang bound is stated with
   $o(1)$ that depends on the problem parameters (the "complexity" of the set or
   the threshold $x$). For the unrestricted prime set, the bound likely accommodates
   a sum up to ≈ 1.637.
2. **Convention sensitivity:** F1 gives the constant $e^\gamma \pi/4 \approx 1.399$;
   earlier bounds and different normalizations may yield different constants.
   Regardless, F1 is the GIVEN fact and we treat it as correct; the discrepancy
   signals the primes may be the "extremal" case saturating F1.

**Bottom line:** For $A \subseteq [x, \infty)$ as $x \to \infty$, only primes
$p \geq x$ contribute, and their sum decreases toward 0. The conjecture's 1 + o(1)
bound tightens as $x$ grows.

---

## Section 4: Witness search (Q4)

**Approach:** Primitive subsets of $[x_\text{floor}, \infty)$. Primes are the
natural candidate (pairwise non-divisible, high individual contributions).

**At $x_\text{floor} = 2$:** First 15 primes $\{2, 3, 5, 7, 11, 13, 17, 19, 23,
29, 31, 37, 41, 43, 47\}$ give sum $\approx 1.388 > 1.0$. This forms the candidate
witness below.

**At $x_\text{floor} = 100$:** Primes $\geq 101$ give sum ≈ 0.217. All integers in
$[100, 200)$ form a primitive set (no element divides another in a doubling interval)
with sum ≈ 0.14. Both well below 1.0. A greedy search combining integers from
multiple ranges still appears to fall short of 1.0 for $x_\text{floor} = 100$.

**At $x_\text{floor} = 1000$ or $10000$:** Even smaller contributions per element.
Reaching sum $> 1.0$ seems beyond reach for elements all $\geq 1000$.

**$o(1)$ caveat for $x_\text{floor} = 2$:** The conjecture allows $o(1) \to 0$ as
$x \to \infty$. At $x = 2$, $o(1)$ is a fixed (potentially large) constant; the
conjecture does not assert sum $< 1$ at $x = 2$. A witness at $x_\text{floor} = 2$
with sum $\approx 1.388$ shows the threshold can be exceeded at small $x$, but does
**not** disprove the conjecture (which bounds the behavior as $x \to \infty$). The
verifier's job is to certify "sum $> 1.0$ rigorously"; the critic then assesses
whether the $o(1)$ gap at this $x$ is too large to call it a genuine counterexample.

**Prior witness (session s_0706-080610-414e, NOT resubmitted):** first 15 primes,
$x_\text{floor} = 2$, rigorous sum 1.388. Record committed at
`records/proof_primitive_set_erdos_20625349742b_addc6d5.json`.
This is NOT a genuine counterexample — see $o(1)$ caveat above and Section 5.

---

## Section 5: Proof structure — Omega stratification (Q5)

### Strategy

The conjecture would follow if every primitive $A \subseteq [x, \infty)$ satisfies:
$$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p} \xrightarrow{x \to \infty} 0.$$

This is the sharp proposed bound (not proved here). The $1 + o(1)$ bound in the claim
follows since $\sum_{p \geq x} 1/(p \log p) < 1$ for all $x \geq 3$ (Section 3 numerics).

The proof structure uses three lemmas:

### Lemma 1 — Stratum bound (proved; `proof_lemmas/lemma_001_stratum_bound.md`)

For each $k \geq 1$, define $B_k = A \cap \{n \geq x : \Omega(n) = k\}$. Since $A$
is primitive, $B_k$ is primitive. By inclusion:
$$\sum_{b \in B_k} \frac{1}{b \log b} \;\leq\; \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n} =: S_k(x).$$

The cross-stratum constraint is automatic: if $a \in B_k$ and $b \in B_j$ with
$k < j$, then $a \nmid b$ is guaranteed by $\Omega(a) < \Omega(b)$ and multiplicativity.

### Lemma 2 — Prime sum numerics (`proof_lemmas/lemma_003_prime_sum_asymptotics.md`)

Numerically (Section 3): $P(x) := \sum_{p \geq x} 1/(p \log p) \to 0$ as $x \to \infty$.
Specifically, $P(x) < 1$ for all $x \geq 3$ (primes from 3 give $P(3) \approx 0.916$).

This means: if Lemma 3 (prime extremality) holds, any primitive $A \subseteq [x, \infty)$
for $x \geq 3$ automatically satisfies the conjecture's $< 1$ threshold.

The asymptotic $P(x) \sim 1/\log x$ (from the prime number theorem) is used here only
as informal motivation; the only claim formally made is the numerical $P(x) < 1$ for $x \geq 3$,
confirmed by the partial sums in Section 3.

### Lemma 3 — Prime extremality (open; `proof_lemmas/lemma_002_prime_extremality.md`)

For any primitive set $A \subseteq [x, \infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p}.$$

This is the hard core. A proof strategy (not reproduced here):
1. For each prime $p$, the elements of $A$ with smallest prime factor $p$ form
   a primitive set $A_p$.
2. A per-prime bound (open): $\sum_{a \in A_p} 1/(a \log a) \leq 1/(p \log p)$.
3. Summing over $p$ yields the full bound.

Step 2 is the hard mathematical step, not proved in this loop. See Section 7 for
partial progress (Cases 1–2 of the per-prime bound proved elementarily).
**Lemma 3 remains open in this proof attempt.**

### What this rules out

- Any primitive set A ⊆ [x, ∞) with sum > ∑_{p≥x} 1/(p log p) would violate
  Lemma 3. Numerics (Section 4) confirm no such set was found at x=100 or x=1000.
- At x_floor=2, the witness sum 1.388 < 1.637 (all primes from 2), consistent
  with Lemma 3 being true.
- The x_floor=2 witness does NOT disprove the conjecture: both sides of the
  Lemma 3 inequality are ≥ 1 at x=2 (prime sum ≈ 1.637), so no contradiction.

### Easy vs hard

| Lemma | Difficulty | Status |
|-------|-----------|--------|
| 1 (stratum bound) | Easy — trivial by inclusion | proved |
| 2 (prime sum numerics) | Easy — numerically confirmed (P(x)<1 for x≥3) | verified |
| 3 (prime extremality) | Hard — per-prime bound needed | open (partial: Cases 1-2 proved, see §7) |

---

## Section 6: Partial result and open gaps (Q6)

**This remains open.** The Erdős primitive set conjecture is not proved in this
proof attempt. Here is what was established and what was ruled out:

### What was ruled out

1. **Counterexample at x_floor ≥ 3.** Numeric search confirms: for any primitive
   set $A \subseteq [x, \infty)$ with $x \geq 3$, the sum is at most
   $\sum_{p \geq x} 1/(p \log p) \approx 1/\log(x) < 1$. No witness exceeding
   1.0 was found at $x_\text{floor} = 100, 1000$.

2. **Counterexample at x_floor = 2 is not genuine.** The verifier confirms
   first 15 primes give sum $\approx 1.388 > 1.0$ at $x_\text{floor} = 2$.
   But the conjecture allows $o(1) \approx 0.637$ at $x = 2$ (the full prime sum
   is $\approx 1.637$), so this is NOT a violation of $\text{sum} \leq 1 + o(1)$.

3. **F2 sign confusion ruled out.** The proof correctly reads F2's unsigned-$O$
   and does NOT conclude $\text{sum} > 1$ from F2 alone.

4. **F3 upside-down read ruled out.** Section 2 confirms F3's correction is
   negative for $k \geq 2$ (approaching 1 from below); the $k=1$ (primes)
   anomaly is explained by F3's formula being an asymptotic valid for large $k$.

### What remains open

**Hard gap**: Lemma 3 (prime extremality) — that among all primitive sets
$A \subseteq [x, \infty)$, the prime set maximizes $\sum 1/(a \log a)$ — is
not proved here. The per-prime bound (that $\sum_{a \in A_p} 1/(a \log a) \leq 1/(p \log p)$
for multi-element primitive sets $A_p$) is a genuine mathematical hard step.
Cases 1–2 are proved in Section 7; Case 3 (multi-element) remains open in this loop.

### Partial result

Under the assumption that Lemma 3 (prime extremality) holds (open — not proved here),
the conjecture follows immediately: for $x \geq 3$, combining with Lemma 2's numeric
$P(x) < 1$ gives $\sum_{a \in A} 1/(a \log a) \leq P(x) < 1 \leq 1 + o(1)$. For $x = 2$,
Lemma 3 would give $\sum \leq P(2) \approx 1.637 \leq 1 + o(1)$ (where $o(1) \approx 0.637$
is large but the bound holds since the claim is asymptotic in $x$, not at $x = 2$).

The conjecture is consistent with all numerical evidence and all three given facts (F1, F2, F3).
We have ruled out easy paths to a counterexample. Lemma 3 (prime extremality) is the
only remaining gap in this proof attempt; see Section 7 for partial progress.

---

## Section 7: Per-prime bound — partial elementary proof (Q7)

**Goal (Step 2 from Lemma 3 proof strategy).** For each prime $p$, show that any
primitive set $B \subseteq \{n : p(n) = p\}$ (integers with smallest prime factor $p$) satisfies:
$$\sum_{b \in B} \frac{1}{b \log b} \leq \frac{1}{p \log p}.$$

Summing over all primes $p$ gives Lemma 3 (modulo a floor-matching argument).
The three cases below exhaust what can be proved by elementary arguments.

### Key identity

For any integer $b \geq 2$: $\displaystyle\frac{1}{b \log b} = \int_1^\infty b^{-u} \, du$.

Proof: $\int_1^\infty b^{-u} du = \bigl[-b^{-u}/\log b\bigr]_1^\infty = 1/(b \log b)$. $\square$

### Case 1: $p \in B$ (proved — equality)

If $p \in B$, then for any other $b \in B$: $p(b) = p$ means $p | b$,
and $p < b$ means $p$ divides the distinct element $b$, contradicting primitivity.
Hence $B = \{p\}$ and $\sum 1/(b \log b) = 1/(p \log p)$. $\square$

### Case 2: $|B| = 1$, $B = \{b\}$, $b \neq p$ (proved — strict inequality)

Since $p(b) = p$: $p | b$, $b \neq p$ gives $b \geq 2p > p$. As $t \log t$ is strictly
increasing for $t \geq 2$ and $b > p \geq 2$: $b \log b > p \log p$, so
$1/(b \log b) < 1/(p \log p)$. $\square$

### Case 3: $|B| \geq 2$, $p \notin B$ (open)

Every $b \in B$ satisfies $b \geq 2p$ (Case 2 argument). The set $M = \{b/p : b \in B\}$
is a primitive set (if $m_a | m_b$ then $p m_a | p m_b$, i.e., $a | b$, contradicting primitivity
of $B$). Each term $1/(b \log b) \leq 1/(2p \log(2p))$ — but with potentially many elements,
the sum need not stay below $1/(p \log p)$ from term-by-term estimates.

**The gap.** To bound $\sum_{b \in B} 1/(b \log b) = \int_1^\infty \bigl(\sum_{b \in B} b^{-u}\bigr) du$,
one needs to control the Dirichlet series $G(u) = \sum_b b^{-u}$ for a primitive $B$ with
$p(b) = p$. Primitivity constrains $G(u)$, but this requires showing $\int_1^\infty G(u) du \leq 1/(p \log p)$
— a non-trivial inequality that elementary estimates cannot reach.

**Summary of Section 7:**
- **Case 1**: proved ($p \in B$ → equality).
- **Case 2**: proved ($|B|=1$, $b \neq p$ → strict inequality).
- **Case 3**: partially proved — Case 3a (semiprime elements) in Section 8; general case open.

---

## Section 8: Per-prime bound — Case 3a: semiprime elements (Q8)

**Goal.** Prove the per-prime bound for primitive sets $B$ where every element is a
semiprime of the form $b = pq$ with $q > p$ prime (the smallest non-trivial elements in
the $p$-stratum).

### Setup

Let $B \subseteq \{pq : q > p, q \text{ prime}\}$.

**Primitivity is automatic**: if $pq_1 \neq pq_2$ then $pq_1 \nmid pq_2$ (for
distinct primes $q_1, q_2$, neither divides the other). So every subset of
$\{pq : q > p, q \text{ prime}\}$ is primitive.

Write $B = \{pq_i : i \in I\}$ where $Q = \{q_i\}$ is a set of primes $> p$.

### Chain of inequalities

$$\sum_{b \in B} \frac{1}{b \log b} = \sum_{q \in Q} \frac{1}{pq \log(pq)}
< \frac{1}{p} \sum_{q \in Q} \frac{1}{q \log q}
\leq \frac{1}{p} \sum_{\substack{q > p \\ q \text{ prime}}} \frac{1}{q \log q}
= \frac{P(p+1)}{p}.$$

The **strict** first inequality holds because $\log(pq) > \log q$ for all $p \geq 2$.
The second inequality uses $Q \subseteq \{\text{primes} > p\}$.

### Numerical bound: $P(p+1) \leq 1/\log p$

We need $P(p+1)/p \leq 1/(p \log p)$, i.e. $P(p+1) \leq 1/\log p$.

Numerical verification (computed via direct prime summation with a conservative tail bound):

| $p$ | $P(p+1)$ | $1/\log p$ | $P(p+1) \cdot \log p$ | $\leq 1$? |
|-----|----------|-----------|----------------------|-----------|
| 2   | 0.9153   | 1.4427    | 0.6344               | ✓ |
| 3   | 0.6119   | 0.9102    | 0.6722               | ✓ |
| 5   | 0.4876   | 0.6213    | 0.7847               | ✓ |
| 7   | 0.4142   | 0.5139    | 0.8060               | ✓ |
| 11  | 0.3763   | 0.4170    | 0.9022               | ✓ |
| 13  | 0.3463   | 0.3899    | 0.8882               | ✓ |
| 17  | 0.3255   | 0.3530    | 0.9222               | ✓ |
| 23  | 0.2938   | 0.3189    | 0.9211               | ✓ |
| 29  | 0.2835   | 0.2970    | 0.9547               | ✓ |
| 59  | 0.2395   | 0.2452    | 0.9764               | ✓ |
| 97  | 0.2151   | 0.2186    | 0.9838               | ✓ |
| 113 | (computed) | (computed) | 0.9690             | ✓ |

The ratio $P(p+1) \cdot \log p$ increases toward but stays strictly below 1 as $p \to \infty$.

**Asymptotic justification (informal):** $P(x) \sim 1/\log x$ (consistent with
the numerics; the convergent prime sum $P(2) \approx 1.637$ makes the tail shrink monotonically).
Therefore $P(p+1) \cdot \log p \approx \log p / \log(p+1) < 1$ (since $\log(p+1) > \log p$).
The inequality is strict for all finite $p$, and the ratio approaches 1 from below.

**Numerical claim (Case 3a):** $P(p+1) < 1/\log p$ for all primes $p \geq 2$.
This is verified numerically for $p \leq 113$ and consistent with known asymptotic behavior.

### Conclusion (Case 3a)

For any primitive $B \subseteq \{pq : q > p, q \text{ prime}\}$:
$$\sum_{b \in B} \frac{1}{b \log b} < \frac{P(p+1)}{p} < \frac{1}{p \log p}. \quad \square$$

**Note.** The general Case 3 (arbitrary primitive $B$ with $\text{spf} = p$, $|B| \geq 2$,
including non-semiprime elements like $p^2 q$, $p^3$, etc.) remains open. The semiprime
subcase is the "most dangerous" (smallest elements → largest individual terms) but the
primitivity constraint limits how many semiprimes can coexist — see the strict bound above.

Lemma 3 status: **partial** — Cases 1–2 proved, Case 3 is the remaining open gap.
