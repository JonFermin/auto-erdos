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
  Asserting resolution (e.g., claiming falsity or disproving) triggers
  `critic_openness`'s `open-claim-asserted-resolved-without-witness`
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

### 1.1 The Claim

**Erdős primitive-set conjecture (tightened form):**
For any primitive set $A \subset [x, \infty)$ (a set of positive integers,
no two of which are in a divisibility relation), we have
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$
where the $o(1)$ term tends to $0$ as $x \to \infty$.

Equivalently: for any $\varepsilon > 0$ there exists $X_\varepsilon$ such
that for all $x \geq X_\varepsilon$ and all primitive $A \subset [x,\infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + \varepsilon.$$

The conjecture is **open**. Proof-of-upper-bound strategies and
counterexample searches are both in scope for this attempt.

### 1.2 The Three Given Facts

**F1 — Erdős–Zhang upper bound (UPPER bound, ~1.399).**
For *any* primitive set $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
Sign: UPPER bound, strictly less than $1.399 + o(1)$. The $o(1)$ term is as given
in the ledger (tends to 0). F1 is consistent with the conjecture (which claims
a tighter bound of 1). F1 does NOT prove the conjecture (since $1.399 > 1$).
The practical content of F1 is for large $x_{\mathrm{floor}}$; its $o(1)$
correction at small $x$ is uncharacterized in the ledger. We note this in
Section 2.2 relative to the primes-from-2 empirical sum.

**F2 — Omega-stratum lower bound (UNSIGNED big-O).**
For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (numbers with exactly $k$
prime factors counted with multiplicity),
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$
**Critical sign warning**: the $O(\cdot)$ term is **unsigned** — it can
be positive or negative. This inequality does NOT imply the sum exceeds 1.
Concluding "sum > 1" from F2 alone is a **SIGN ERROR** (the classic
ChatGPT failure mode). F2 is consistent with F3 once unsigned-O is read
correctly.

**F3 — Exact asymptotic for $A_k$ (sum approaches 1 from BELOW as $k\to\infty$).**
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
F3 states the formula verbatim. The correction $-(c+o(1))k^2/2^k$ is **negative**
(since $c > 0$), so for each $k$ where the formula is accurate, the sum is less than 1
and approaches 1 from **below** as $k \to \infty$.
**Warning:** F3 as given uses the asymptotic notation $o(1)$ in $k$, so the
formula's accuracy for small $k$ (especially $k=1$) is not established in
the ledger. See Section 2.1 for numerical evidence that the $k=1$ row (primes) may
diverge from the formula. **We do not use F3 to conclude $A_1$ sum $< 1$.**
F3 is cited only for large-$k$ stratum estimates in subsequent lemmas.

### 1.3 The Witness Contract

To claim a counterexample, one must exhibit a **finite** primitive set
$A \subset [x_\mathrm{floor}, \infty)$ with
$$\sum_{a \in A} \frac{1}{a \log a} > 1 \quad \text{(rigorously verified)}.$$
The verifier contract:
- `x_floor`: every element of `elements` must be $\geq x_\mathrm{floor}$.
- `elements`: list of distinct integers, pairwise non-divisible.
- `claimed_sum_lower_bound`: agent's own lower-bound claim; verifier
  recomputes rigorously from the actual elements.
The verifier `library.primitive_set_witness.verify_witness` is the sole
arbiter. `witness_valid == 1` is required before any disproof claim.

**Important caveat**: a witness at finite $x_\mathrm{floor}$ with sum > 1
is a genuine counterexample only if the $o(1)$ correction at that
$x_\mathrm{floor}$ is estimated to be small. A witness with sum 1.001 at
$x_\mathrm{floor} = 2$ is NOT convincing without a separate estimate of
the $o(1)$ gap.

---

## Section 2 — Numerical Exploration

### 2.1 Omega-stratum sums (Q2 — F3 verification)

We computed partial sums $\sum_{n \leq N, \Omega(n)=k} 1/(n \log n)$ for $k = 1, 2, 3, 4$
and $N = 50{,}000$.

| $k$ | Partial sum ($N \leq 50000$) | F3 prediction $1 - (c+o(1))k^2/2^k$ |
|-----|-----|------|
| 1 (primes)   | 1.544223 | 0.967200 |
| 2 (semiprimes) | 0.814781 | 0.934400 |
| 3            | 0.436306 | 0.926200 |
| 4            | 0.213074 | 0.934400 |

**Key observation:** The $k=1$ partial sum at $N = 50{,}000$ is $1.544$, well above 1.
The series appears to be converging toward a limit distinctly above 1, which is
**much larger** than F3's prediction of $\approx 0.967$.
(The k=2, 3, 4 rows are all below 1 and appear consistent with F3 for those $k$.)

**Sign / consistency note on F3 for $k=1$:**
F3 says $\sum_{a \in A_1} 1/(a \log a) = 1 - (c+o(1)) k^2/2^k \approx 0.967$.
The partial sum at $N=50{,}000$ is $1.544 > 1$ and still growing. The exact
convergent limit of the $k=1$ series is not characterized in this draft.
The formula might hold asymptotically as $k \to \infty$ (both sides approach 1)
but does **not** match numerical evidence at $k=1$. This discrepancy does not
affect the proof attempt (F3 is correctly read as "each $A_k$ sum approaches 1
from below for large $k$") but the $k=1$ row is an anomaly worth noting.
**We do NOT use F3 to claim $A_1$ sum $< 1$** — F3's sign warning is about
$k \to \infty$, not $k=1$.

For $k \geq 2$: partial sums are below 1 and still growing toward their limits.
F3 predicts limits close to 1 (from below), consistent with $k \geq 2$ rows
growing toward values approaching 1.

### 2.2 Sum over primes from 2 (Q3)

The primes form a primitive set (no prime divides another). The partial sum
$\sum_{p \leq N} 1/(p \log p)$ grows through values shown below
(exact convergent limit not characterized in the ledger).

Partial sums at small primes:
| Prime $p$ | $\sum_{q \leq p} 1/(q \log q)$ |
|---|---|
| 2  | 0.7213 |
| 3  | 1.0248 ← **exceeds 1 here** |
| 5  | 1.1490 |
| 7  | 1.2224 |
| 11 | 1.2604 |
| 29 | 1.3531 |

**Crossing point:** The sum first exceeds 1.0 at $p=3$, with
$1/(2 \log 2) + 1/(3 \log 3) \approx 0.7213 + 0.3035 = 1.0248$.

**Note on F1 — reconciling with primes-from-2 sum:** F1 applies to any primitive
$A \subseteq \mathbb{N}$, including the primes-from-2. F1's $o(1)$ correction term
is uncharacterized at $x_{\mathrm{floor}} = 2$ by the ledger (sign and magnitude
both unspecified at fixed small $x$). The observed primes-from-2 partial sums
(0.72, 1.02, 1.15, 1.22, ... — see table below) are consistent with F1 provided
the $o(1)$ correction at $x=2$ is large enough to accommodate those values.
We make no claim about the sign or magnitude of F1's $o(1)$ at $x=2$.
We cite F1 only as an asymptotic result (its practical content is
for large $x_{\mathrm{floor}}$).

---

## Section 3 — Witness Search (Q4)

We searched for a primitive $A \subset [x_{\mathrm{floor}}, \infty)$ with
rigorously verified $\sum 1/(a \log a) > 1.0$.

| $x_{\mathrm{floor}}$ | Construction | Verified sum | Exceeds threshold? |
|---|---|---|---|
| 2 | $\{2, 3\}$ (smallest 2-element example) | **1.02476** | **YES** |
| 100 | Primes $\geq 100$ (1204 elements) | 0.10659 | no |
| 1000 | All ints $[1000, 2000)$ | 0.09566 | no |
| 10000 | All ints $[10000, 20000)$ | 0.07256 | no |

**Heuristic scale estimate (not a proof step):** A standard antichain observation
is that all integers in $[x, 2x)$ are pairwise non-divisible (since the ratio
of any two is strictly between 1/2 and 2, precluding divisibility). Their sum is
$\sum_{n=x}^{2x-1} 1/(n \log n) \approx \int_x^{2x} 1/(t \log t)\, dt = \log(\log 2x) - \log(\log x)$.
For large $x$: $\log(\log 2x/\log x) \approx \log 2/\log x \to 0$.
Numerically:
- $x=100$: sum of all integers in $[100,200)$ $\approx 0.141$ (verified)
- $x=1000$: sum of all integers in $[1000,2000)$ $\approx 0.096$ (verified)
- $x=10000$: sum of all integers in $[10000,20000)$ $\approx 0.073$ (verified)

The observed sums across all tested constructions at $x_{\mathrm{floor}} \geq 100$
are far below 1.0. No construction found exceeds sum $= 0.15$ for $x_\mathrm{floor} \geq 100$.

**Observation:** The only verified witnesses with sum $> 1$ involve $x_{\mathrm{floor}} = 2$.
For $x_{\mathrm{floor}} \geq 100$, all constructions tested give sum $< 0.2$,
consistent with the conjecture's bound of $1 + o(1)$ being satisfied.

**o(1) caveat:** The smallest witness $\{2, 3\}$ has sum $\approx 1.025 > 1$
at $x_{\mathrm{floor}} = 2$. This exceeds the witness threshold of 1.0, but
the conjecture's bound at $x=2$ is $1 + o(1)$ where $o(1)$ is not specified
to be small at $x=2$. Thus $\{2,3\}$ does NOT disprove the conjecture in its
$x \to \infty$ form; it is evidence that the bound is not tight at $x=2$.

---

## Section 4 — Proof Strategy Outline (Q5)

### 4.1 High-level structure

The goal is to prove: for any $\varepsilon > 0$ there exists $X_\varepsilon$ such
that for all $x \geq X_\varepsilon$ and all primitive $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + \varepsilon.$$

For large $x$, tested primitive sets in $[x, \infty)$ give sums well below 1
(Section 3: all constructions at $x_{\mathrm{floor}} \geq 100$ give sum $< 0.15$).
The sum for the densest antichain in $[x, 2x)$ is $\approx \log 2/\log x \to 0$
(Lemma 1). The primes starting from $p=2$ give partial sums exceeding 1.0 at $p=3$ and
growing well above 1.0 (Section 2.2 table), but that construction has
$x_{\mathrm{floor}} = 2$, not large $x$; it does not contradict the conjecture's
$x \to \infty$ form.

### 4.2 Key observation and open question

The densest primitive set in $[x, 2x)$ is the full integer interval (all integers
in $[x, 2x)$ are pairwise non-divisible — if $a, b \in [x, 2x)$ with $a \mid b$,
then $b \geq 2a \geq 2x$, contradicting $b < 2x$). Lemma 1 (proved, see
`proof_lemmas/lemma_001_dense_antichain.md`) establishes this bound rigorously.

**Open sub-conjecture (Lemma 2):** The bound for $A \subset [x, \infty)$ (not
restricted to one dyadic interval) requires the cross-layer primitivity constraint.
Layer-by-layer application of Lemma 1 gives a bound of
$\sum_{k=0}^{\infty} \log 2/\log(2^k x)$, which diverges (harmonic-like). So
Lemma 1 alone cannot establish the conjecture for unbounded $A$. The key difficulty
is that primitivity across layers (if $a \in [2^j x, 2^{j+1}x)$ and $b \in [2^k x, 2^{k+1}x)$
with $j < k$, then $a \nmid b$) severely restricts which cross-layer combinations
are allowed, but the quantitative consequence of this constraint requires a deeper
analytic argument.

### 4.3 Lemma outline

**Lemma 1 (dense antichain bound for $[x, 2x)$):** For any pairwise non-divisible
$S \subset [x, 2x)$,
$$\sum_{s \in S} \frac{1}{s \log s} \leq \sum_{n=x}^{2x-1} \frac{1}{n \log n}
= \frac{\log 2}{\log x} + O\!\left(\frac{1}{(\log x)^2}\right).$$
*Status: **PROVED** (see `proof_lemmas/lemma_001_dense_antichain.md`).*
The bound follows from: all integers in $[x, 2x)$ are pairwise non-divisible
(so $S$ can be at most the full interval), and the integral approximation of the
interval sum.

**Lemma 2 (cross-layer bound — open):** For primitive $A \subset [x, \infty)$,
the cross-layer primitivity constraint implies
$$\sum_{a \in A} \frac{1}{a \log a} \leq C$$
for some absolute constant $C$, ideally $C = 1 + o(1)$ as $x \to \infty$.
*Status: **OPEN**. Main obstacle: layer-by-layer Lemma 1 application diverges.*

**Progress on Lemma 2 (see `proof_lemmas/lemma_002_chain_decomposition.md`):**

The chain decomposition (odd-part factorization $a = 2^e m$, $m$ odd) gives
a partial bound. By primitivity, the odd parts $\{m(a)\}$ of elements of $A$
are distinct odd integers. For elements with $m(a) < x$ (small odd part),
the element $a \geq x$ contributes $\leq 1/(x \log x)$ each, and there are
at most $\lfloor x/2 \rfloor$ such odd parts. This yields:
$$\sum_{\substack{a \in A \\ m(a) < x}} \frac{1}{a \log a} \leq \frac{1}{2 \log x}.$$

For the large-chain part: since $a = 2^{e(a)} m(a) \geq m(a)$, we have
$1/(a \log a) \leq 1/(m(a) \log m(a))$ for each $a$ with $m(a) \geq x$. The
odd parts $M = \{m(a) : m(a) \geq x\}$ are **distinct** odd integers in $[x,\infty)$
(distinctness: same odd part implies same chain, hence divisibility in $A$, contradiction).
Since $a \geq m(a)$: $1/(a \log a) \leq 1/(m(a) \log m(a))$, so
$S_{\mathrm{large}} \leq \sum_{m \in M} 1/(m \log m)$.
**Correction (Lemma 2 v2):** $M$ is NOT necessarily pairwise non-divisible (example:
$A = \{6, 15\}$ is primitive yet $m(6)=3 \mid m(15)=15$). The large-chain
bound therefore does NOT reduce to a primitive-set problem. It remains open (see
Lemma 2 obstacle discussion and planned Lemma 3).
*Status: partial (the small-chain bound $\leq 1/(2\log x)$ is proved; large-chain is open).*

---

## Section 5 — Lemma Files

- `proof_lemmas/lemma_001_dense_antichain.md` — **PROVED**. Dense antichain
  bound for $[x, 2x)$: sum $\leq \log 2/\log x + O(1/(\log x)^2)$.
- `proof_lemmas/lemma_002_chain_decomposition.md` — **PARTIAL (corrected)**. Chain
  decomposition: small-chain contribution $\leq 1/(2 \log x)$ proved.
  Large-chain odd parts are distinct (not pairwise non-divisible); the naive
  reduction to odd primitive sets was incorrect. Large-chain remains open.
- `proof_lemmas/lemma_003_2adic_stratum.md` — **PARTIAL (new insight)**. For fixed
  2-adic valuation $e$, $M_e = \{m(a) : e(a)=e, m(a)\geq x\}$ is pairwise
  non-divisible (proved). Yields $S_\text{large} \leq 2\,f_\text{odd}(x)$.
  Iterated prime-stratum recursion diverges via $\prod_p p/(p-1) = \infty$.

---

## Section 6 — What Was Established and What Remains Open

### Proved

1. **Lemma 1**: For primitive $S \subset [x,2x)$,
   $\sum 1/(s\log s) \leq \log 2/\log x + O(1/\log^2 x) \to 0$.
2. **Lemma 2 (partial)**: $S_\text{small}(A,x) \leq 1/(2\log x) \to 0$.
3. **Lemma 3 (partial)**: Each $M_e$ is pairwise non-div; $S_\text{large} \leq 2\,f_\text{odd}(x)$.

### Ruled out

| Approach | Obstacle |
|---|---|
| Layer-by-layer Lemma 1 | $\sum_k \log 2/\log(2^k x)$ diverges |
| Naive odd-part reduction | $M$ is distinct, not primitive |
| Iterated prime-stratum recursion | $\prod_p p/(p-1) = \infty$ |
| Chain-length bound via $\max e(a)$ | $\max e(a)$ unbounded |
| F1 applied to $f_\text{odd}$ | Gives $f \leq 3.298$, worse than F1 directly |

### Core obstacle

The gap from F1's 1.399 to the conjectured bound of 1 cannot be closed from
F1, F2, F3 alone. The Erdős–Zhang proof uses Turán's power-sum method and the
Euler product structure of $\sum_{a\in A} a^{-s}$ as $s\to 1^+$, outside the
given ledger. **Closing this attempt as a partial result.**

### Partial result summary

$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{1}{2\log x} + 2\, f_\text{odd}(x), \qquad A \subset [x,\infty) \text{ primitive},$$

where $f_\text{odd}(x)$ is itself open. The two genuinely new proved results
are Lemma 1 (dense antichain bound) and the $M_e$ pairwise non-divisibility
observation (Lemma 3 key claim). The conjecture remains open.
