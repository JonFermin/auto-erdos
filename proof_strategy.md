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
  Phrases like "the conjecture is false" / "we disprove" trigger
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
For *any* primitive set $A \subseteq \mathbb{N}$ (not restricted to
$[x, \infty)$),
$$\sum_{a \in A} \frac{1}{a \log a} < e^\gamma \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
Sign: strictly LESS THAN 1.399. This is an UPPER bound. It is consistent
with the conjecture (which aims for 1); it does not prove it (since 1.399 > 1).
A primitive set achieving sum close to 1.399 would disprove the conjecture.

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
(since $c > 0$), so the formula predicts each $A_k$ sum is strictly less than 1
and the sequence of sums approaches 1 from **below** as $k \to \infty$.
**Warning:** F3 as given makes this claim for each $k$ via the asymptotic formula,
but the formula's accuracy for small $k$ (especially $k=1$) is not established in
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
Numerically the sum is $\approx 1.636 > 1$. The formula might hold asymptotically
as $k \to \infty$ (both sides approach 1) but does **not** match numerical
evidence at $k=1$. This discrepancy does not affect the proof attempt (F3 is
correctly read as "each $A_k$ sum approaches 1 from below for large $k$") but
the $k=1$ row is an anomaly worth noting. **We do NOT use F3 to claim $A_1$
sum $< 1$** — F3's sign warning (the sum approaches 1 from *below* for large
$k$) is about $k \to \infty$, not $k=1$.

For $k \geq 2$: partial sums are below 1 and still growing toward their limits.
F3 predicts limits close to 1 (from below), consistent with $k \geq 2$ rows
growing toward values approaching 1.

### 2.2 Sum over primes from 2 (Q3)

The primes form a primitive set (no prime divides another). The partial sum
$\sum_{p \leq N} 1/(p \log p)$ grows toward $\approx 1.636$.

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

**Consistency with F1:** F1 (as stated) gives an upper bound $e^\gamma\pi/4 + o(1) \approx 1.399 + o(1)$
for any primitive set $A \subseteq \mathbb{N}$. The full primes-from-2 sum $\approx 1.636 > 1.399$
appears to contradict F1. However, the $o(1)$ term in F1 is not defined in the ledger —
its sign and magnitude are unspecified, so F1 does NOT say the sum is $< 1.399$ for all
finite primitive sets; the bound is an asymptotic one. We take F1 at face value and do
not use it to bound the primes-from-2 sum.

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

The numerical data (Section 2–3) suggests the sum decreases to 0 as $x \to \infty$
for the constructions we tested, well below the conjectured bound of 1. A formal
proof that the sum is bounded would likely proceed via Lemma 1 (density bound) —
which is currently open.

### 4.2 Key open question

The numerical data shows that for $x \geq 100$, tested constructions give sum
at most $\approx \log 2/\log x \ll 1$, suggesting the conjecture may be much
stronger than needed: the sum appears to approach 0, not merely stay $< 1$.
This is a heuristic observation; Lemma 1 below states the formal bound to be proved.

**Reformulation:** Perhaps the conjecture is about a NORMALIZED sum
$\log x \cdot \sum_{a \in A} 1/(a \log a)$ approaching some constant $\leq 1$?
This normalized form would be $O(1)$ for the densest antichain in $[x, 2x)$:
$$\log x \cdot \frac{\log 2}{\log x} = \log 2 < 1.$$

Or perhaps the conjecture involves the Erdős function $f(A, x) = \max_{B \subset A \cap [x,\infty)} \sum 1/(b \log b)$?

### 4.3 Lemma outline (to be developed in proof_lemmas/)

**Lemma 1 (density bound):** For any primitive $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{\log 2}{\log x} + O\!\left(\frac{1}{(\log x)^2}\right).$$
*Status: open. Proof sketch: use the fact that every integer has a unique odd
part; the densest antichain in $[x, \infty)$ is [x, 2x).*

**Lemma 2 (omega-stratum bound):** For each $k$, the stratum $A_k = A \cap \{n : \Omega(n) = k\}$
satisfies $\sum_{a \in A_k} 1/(a \log a) \leq C_k / k$ for some absolute constant $C_k$.
*Status: open.*

*[Further lemma files will be created in proof_lemmas/ in subsequent rounds.]*

---

## Section 5 — Lemma Files

*Lemmas will be created in `proof_lemmas/lemma_*.md`.*
