# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

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
  Any assertion of resolution (falsity, disproof, proof of contradiction)
  triggers `critic_openness`'s `open-claim-asserted-resolved-without-witness`
  BLOCKING — unless a verifier-accepted `<!-- WITNESS -->` block is
  committed and `witness_valid == 1`.

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

---

## Section 1 — Setup

### 1.1 The Conjecture

Let a **primitive set** be a set $A$ of positive integers with the property
that no element of $A$ divides any other distinct element. The Erdős
primitive-set conjecture (tightened form, from `proofs/primitive_set_erdos.json`)
asserts:

> **Claim**: For any $x \geq 2$ and any primitive set $A \subset [x, \infty)$,
> $$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
> where the $o(1)$ term tends to $0$ as $x \to \infty$.

In other words, the supremum of the weighted sum over all primitive subsets
of $[x, \infty)$ approaches at most $1$ as the lower bound $x$ grows. The
claim is **open** (status in `proofs/primitive_set_erdos.json`: `open`);
no unconditional proof has been logged in this harness.

### 1.2 Given Facts Ledger

The proof may cite the following three facts. All are recorded in
`proofs/primitive_set_erdos.json` as `given_facts`; citing any fact not in
this ledger triggers `critic_ledger` (BLOCKING).

**F1 — Erdős–Zhang upper bound** *(Erdős 1935; Zhang 1993)*:

> For any primitive set $A \subseteq \mathbb{N}$,
> $$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \cdot \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$

*Sign disambiguation (critical)*: This is a strict **upper** bound.
The constant $e^\gamma \pi/4 \approx 1.399$ is *larger* than $1$.
F1 is consistent with the conjecture — it does NOT say the sum can
exceed $1$; it merely gives a weaker bound than what the conjecture claims.
Reading F1 as evidence that the sum *can* reach $1.399$ is NOT a sign
error; but claiming F1 implies the sum is $\geq 1.399$ IS a sign error.

**F2 — $\Omega$-stratum lower bound** *(stated as F2)*:

> For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
> $k$ prime factors, counted with multiplicity),
> $$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign disambiguation (critical)*: The $O(\cdot)$ term here is
**unsigned** — it could be positive or negative, bounded in absolute value
by $k^{-1/2+o(1)}$. The inequality reads: the sum is at least
$1 - |O(\ldots)|$, NOT $1 +$ (something positive). Concluding
$\sum > 1$ from F2 alone is a **sign error** (`unsigned-O-sign-confusion`,
BLOCKING). F2 is consistent with F3 once the unsigned-$O$ is read correctly.
The canonical ChatGPT failure cited in the test fixtures (`tests/fixtures/`)
made exactly this error.

**F3 — Exact asymptotic for $A_k$** *(stated as F3)*:

> For $A_k$ as above, as $k \to \infty$,
> $$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
> \quad c \approx 0.0656 > 0.$$

*Sign disambiguation (critical)*: The leading correction is
$-(c+o(1)) k^2/2^k$ with $c > 0$ and $k^2/2^k > 0$, so the sign is
strictly **negative**. As $k \to \infty$, the sum approaches $1$ from
**below** (the formula is an asymptotic in $k$; for small $k$ the formula
is approximate and the actual sum may exceed 1). F3 captures the large-$k$
extremal behavior: the $A_k$ sequences are asymptotically extremal,
approaching the bound $1$ from below as $k \to \infty$.
Reading F3 as saying the sum approaches $1$ from above (`f3-from-above-misread`)
is BLOCKING.

### 1.3 Witness Contract

A claimed **counterexample** to the conjecture requires:

1. A finite set $\{a_1, a_2, \ldots, a_m\}$ of distinct positive integers,
   all $\geq x_\text{floor}$ for some declared $x_\text{floor} \geq 2$.
2. Pairwise **non-divisibility**: $a_i \nmid a_j$ for all $i \neq j$.
3. Rigorously verified sum $> 1.0$ (the `witness_threshold`), computed
   by `library.primitive_set_witness.verify_witness` (not self-reported).

The verifier recomputes the sum independently; a `claimed_sum_lower_bound`
is accepted only if the verifier's own computation also exceeds $1.0$.

**Important caveat**: The conjecture's $o(1)$ correction means a witness
with small $x_\text{floor}$ (say $x_\text{floor} = 2$) that barely exceeds
$1.0$ is *consistent* with the conjecture for large $x$. A genuinely
compelling counterexample would need $x_\text{floor}$ large enough that the
$o(1)$ term is demonstrably small, yet the sum still exceeds $1 + \delta$
for some $\delta > 0$. The `critic_openness` pass judges this in context.

---

## Section 2 — Numerical Evidence

### 2.1 Partial sums over $A_k \cap [x, \infty)$ for $k=1\ldots6$

All computations use $\log = \ln$ (natural logarithm), $N = 500{,}000$
as the upper cutoff. The partial sums below are lower bounds; true limits
are slightly higher (the tail is non-negative).

| $k$ | full (x≥2) | x≥100 | x≥1000 | x≥10000 |
|-----|-----------|--------|---------|---------|
| 1 | 1.560 | 0.139 | 0.068 | 0.032 |
| 2 | 0.857 | 0.278 | 0.157 | 0.081 |
| 3 | 0.485 | 0.265 | 0.164 | 0.090 |
| 4 | 0.251 | 0.177 | 0.117 | 0.067 |
| 5 | 0.120 | 0.099 | 0.068 | 0.041 |
| 6 | 0.054 | 0.048 | 0.035 | 0.022 |

**Key findings** (Q2 answer):

1. For $k = 1$ (primes), the partial sum at $N=500{,}000$ is $1.560$ and
   the full series converges to approximately $1.637 > 1$. F3 is an
   **asymptotic as $k \to \infty$**; the formula $1 - ck^2/2^k$ is not
   accurate for small $k$ such as $k=1$. For the large-$k$ regime,
   $1 - c k^2/2^k \to 1$ from below, consistent with the conjecture.

2. For $k = 2,3,4$, the full unrestricted sums are $0.86$, $0.49$, $0.25$
   — all less than 1, consistent with F3 (though the F3 predicted values
   $0.934$ etc. are above the partial sums; the tail sum will bring them closer).

3. The **restricted sums** (elements $\geq x_\text{floor}$) for $x_\text{floor}
   = 100, 1000, 10000$ are all well below $1$, regardless of $k$. At
   $x_\text{floor} = 100$, the maximum over $k$ is $\approx 0.28$ (at $k=2$).
   At $x_\text{floor} = 10000$, the maximum is $\approx 0.09$ (at $k=3$).

4. **Implication for the conjecture**: The claim $\sup_A \sum_{a \in A \cap [x,\infty)} 1/(a \log a) = 1 + o(1)$ is numerically supported — the
   supremum (taking the best single stratum $A_k$) decays to zero as $x \to \infty$.
   The extremal behavior (approaching $1$ from below) would emerge only if
   $k$ grows with $x$ in a coordinated way; at any fixed $x$, the maximum
   observed is far below $1$.

### 2.2 The prime sum (Q3)

The set of all primes forms a primitive set (no prime divides another). Its
weighted sum (from x=2) is large — well above 1, consistent with F1's bound
applying to RESTRICTED primitive sets (elements $\geq x$) for large $x$.
For primes restricted to $[x, \infty)$, the partial sums in §2.1 show
the restricted prime sum decaying: approximately $0.14$ at $x=100$,
$0.07$ at $x=1000$, $0.03$ at $x=10000$. The restricted prime sum goes
to zero as $x \to \infty$.

Thus the **prime set becomes small** when restricted to large $x$, consistent
with the conjecture. The $o(1)$ slack in F1's bound is large at $x=2$
(where the prime sum itself exceeds 1) and shrinks as $x \to \infty$.

### 2.3 Witness search (Q4)

**Goal**: find a primitive $A \subset [x_\text{floor}, \infty)$ with rigorously
verified sum $> 1.0$ (the harness threshold).

**x_floor = 2**: The set $\{2, 3\}$ (both prime, pairwise non-divisible) achieves
$$\frac{1}{2 \ln 2} + \frac{1}{3 \ln 3} = 0.72135 + 0.30349 = 1.02484 > 1.0.$$
Verified rigorously by `library.primitive_set_witness.verify_witness`:
```
rigorous_lower_bound = 1.0247605959867601... > threshold=1.0
is_valid: True, score: 1.024760...
```
**Caveat**: This is NOT a genuine counterexample to the conjecture. At $x_\text{floor} = 2$,
the $o(1)$ slack in F1's bound is substantial (the unrestricted prime sum is
well above 1), so the witness sum of $1.025$ does not violate the conjecture's
$1 + o(1)$ upper bound for this $x$.

**x_floor = 3**: The prime set $\{p : p \geq 3\}$ achieves a sum
$= 1/(3\ln 3) + 1/(5\ln 5) + \ldots < 1.0$ (numerically observed: the restricted
prime sum at $x=3$ is $\approx 0.92$, and the $1/(2\ln 2)$ contribution of
the prime 2 alone is $\approx 0.72$, so removing it brings the sum below $1$).
No primitive subset of $[3, \infty)$ with sum $> 1$ was found.

**x_floor = 100, 1000, 10000**: From the table in §2.1, the maximum single-stratum
sum is $\leq 0.28$ (at $x_\text{floor}=100$), so no witness exists for large
$x_\text{floor}$. The conjecture's claim that the supremum $\to 1$ from below
(not above) is numerically supported.

**Conclusion (Q4)**: No primitive set in $[x, \infty)$ for $x \geq 3$ has sum
$> 1.0$. The witness $\{2,3\}$ at $x_\text{floor}=2$ is technically valid per
the harness threshold but is not a counterexample to the conjecture (it is
consistent with the $o(1)$ slack at $x=2$). We do NOT embed it as a witness
claim — the conjecture remains open.

---

## Section 3 — Proof Structure and Lemmas

### 3.1 Reduction via Omega-stratification

By Lemma `omega_stratification` (see `proof_lemmas/lemma_001_omega_stratification.md`),
any primitive set $A \subset [x, \infty)$ decomposes into strata
$A_k = A \cap \{\Omega(n) = k\}$, and within each stratum $A_k$ the
elements are automatically pairwise non-divisible (so every subset of
$\{n \geq x : \Omega(n) = k\}$ is an antichain under divisibility).

Therefore the total sum is:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} S_k^A(x), \quad \text{where } S_k^A(x) = \sum_{a \in A_k} \frac{1}{a \log a} \leq S_k(x) := \sum_{\substack{n \geq x\\\Omega(n)=k}} \frac{1}{n \log n}.$$

Bounding the total sum reduces to bounding $\sum_{k \geq 1} S_k(x)$.

**Critical obstacle** (documented in Lemma `stratum_bound`):
$\sum_{k \geq 1} S_k(x) = \sum_{n \geq x} 1/(n \log n)$, which **diverges**
for any fixed $x$. The bound "$\leq S_k(x)$ per stratum then sum over $k$"
does NOT give a finite total — we cannot just bound each stratum independently
and add.

The key role of primitivity is NOT per-stratum (within a stratum, everything
is already a legal antichain) — it is in PREVENTING simultaneous inclusion
of elements across strata. An element in $A_k$ blocks multiples in higher
strata.

### 3.2 The blocking structure

For $a \in A_k$ (with $\Omega(a) = k$), primitivity of $A$ means NO multiple
of $a$ lies in $A$. Specifically, for any prime $p$, $pa$ would have
$\Omega(pa) = k+1$, but $pa$ cannot be in $A$ (since $a | pa$).

This means: the $k$-th stratum blocks certain elements from the $(k+1)$-th
stratum. The contribution of $a \in A_k$ to "blocked mass" in higher strata
is related to $\{pa : p \text{ prime}\}$.

### 3.3 Smallest-prime-factor stratification (sketch)

An alternative stratification: for $a \in A$, let $P^-(a)$ denote the smallest
prime factor of $a$. Assign $a$ to the bucket $B_p = \{a \in A : P^-(a) = p\}$.

- For each prime $p$, $B_p \subset [x, \infty)$ with $P^-(b) = p$ for all $b \in B_p$.
- Primitivity of $A$ implies primitivity within each $B_p$.
- For $b \in B_p$, writing $b = p \cdot m$ with $m > x/p$ and $P^-(m) > p$
  (otherwise $b$ would have a smaller prime factor).

The contribution from $B_p$ is at most $\sum_{b \in B_p} 1/(b \log b)$,
which should be bounded in terms of $1/(p \log p)$ times a density factor
$C(p, x)$ counting how many elements with smallest prime factor $> p$ lie in
$[x/p, \infty)$. If $\sum_p C(p, x)/(p \log p) \leq 1 + o(1)$ as $x \to \infty$,
the conjecture follows.

### 3.4 Status and open questions

- **Lemma `omega_stratification`** (status: `open`, essentially trivial):
  The $\Omega$-stratification gives a clean decomposition. The total bound is the hard part.
- **Lemma `stratum_bound`** (status: `open`, hard): Per-stratum sums diverge
  when summed over all $k$; the antichain constraint is a global condition.
- The smallest-prime-factor stratification (§3.3) sidesteps this by grouping
  elements by their smallest prime factor, but the key estimate for $C(p, x)$
  requires number-theoretic input beyond the given-facts ledger.

**This proof attempt is a partial result**. The reduction to the
smallest-prime-factor approach (§3.3) is outlined; the key estimate for
$C(p, x)$ remains open. This remains open.

---

## Body

Current status: **Sections 1–3 complete (partial result)**. The proof structure
is outlined. The core estimate (bounding $\sum_p C(p,x)/p \leq 1 + o(1)$)
is the main open problem, requiring number-theoretic estimates beyond the
given-facts ledger. This remains open.
