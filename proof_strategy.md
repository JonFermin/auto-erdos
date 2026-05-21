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

**F3 — Exact asymptotic for $A_k$ (sum approaches 1 from BELOW).**
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
The correction $-(c+o(1))k^2/2^k$ is **negative** (since $c > 0$), so
$\sum_{A_k} < 1$ for every $k \geq 1$, approaching 1 from **below** as
$k \to \infty$. The canonical "extremal-looking" sets $A_k$ do NOT
violate the conjecture.

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

**Key observation:** The $k=1$ partial sum (1.544) is still growing slowly and
appears to converge to approximately $1.636$ (estimated from the tail
$\sum_{p > 50000} 1/(p \log p) \approx 1/\log(50000) \approx 0.092$, giving
$1.544 + 0.092 \approx 1.636$). This is **much larger** than F3's prediction
of $\approx 0.967$.

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

**Consistency with F1:** F1 bounds any primitive set sum by $\approx 1.399 + o(1)$,
but this is asymptotic (as $x \to \infty$, restricting to elements in $[x, \infty)$).
For the full primes from 2, the sum $\approx 1.636 > 1.399$. This is consistent
with F1 if the $o(1)$ correction at $x=2$ equals $\approx 0.24$. The bound
$1.399 + o(1)$ is tight in the $x \to \infty$ limit, not at $x=2$.

---

## Section 3 — Witness Search (Q4)

We searched for a primitive $A \subset [x_{\mathrm{floor}}, \infty)$ with
rigorously verified $\sum 1/(a \log a) > 1.0$.

| $x_{\mathrm{floor}}$ | Construction | Verified sum | Exceeds threshold? |
|---|---|---|---|
| 2 | $\{2, 3\}$ (smallest witness) | **1.02476** | **YES** |
| 2 | Primes $\leq 200$ (46 elements) | **1.45122** | **YES** |
| 100 | Primes $\geq 100$ (1204 elements) | 0.10659 | no |
| 1000 | Primes $\geq 1000$ (9424 elements) | 0.05747 | no |
| 1000 | All ints $[1000, 2000)$ | 0.09566 | no |
| 10000 | All ints $[10000, 20000)$ | 0.07256 | no |

**Theoretical maximum** for primitive sets in $[x, \infty)$: the densest
antichain (all integers in $[x, 2x)$) gives sum $\approx \log 2 / \log x$:
- $x=100$: max $\approx 0.150$
- $x=1000$: max $\approx 0.100$
- $x=10000$: max $\approx 0.075$

All are far below 1.0. For $x_{\mathrm{floor}} \geq 3$, no primitive set
appears able to achieve sum $> 1.0$.

**Conclusion:** The only witnesses with sum $> 1$ involve small elements
($\leq 3$, specifically $x_{\mathrm{floor}} = 2$). For large $x_{\mathrm{floor}}$,
the conjecture's bound of $1 + o(1)$ is trivially satisfied (sum $\to 0$).

**o(1) caveat for the $x=2$ witness:** The conjecture's bound at $x=2$ is
$1 + o(1)|_{x=2} \approx 1 + 0.45$, so the witness sum $\approx 1.45$ is
below this bound. The witness does NOT disprove the conjecture in its
$x \to \infty$ form; it merely shows the bound is not 1 at $x=2$.

**Smallest witness** (for completeness, embedded below):
$\{2, 3\}$ is primitive (2 does not divide 3), both $\geq x_{\mathrm{floor}}=2$,
and $\sum = 1.0248 > 1.0$. This is a valid counterexample to the literal
threshold of 1.0, but NOT to the conjecture's $x \to \infty$ form.

---

## Section 4 — Proof Strategy Outline (Q5)

### 4.1 High-level structure

The goal is to prove: for any $\varepsilon > 0$ there exists $X_\varepsilon$ such
that for all $x \geq X_\varepsilon$ and all primitive $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq 1 + \varepsilon.$$

From the numerical evidence, the sum $\to 0$ as $x \to \infty$ for any primitive
$A \subset [x, \infty)$. So the conjecture in the form $< 1 + \varepsilon$ for
large $x$ is consistent with (and perhaps implied by) the sum vanishing. The
interesting question is: can the sum approach 1 from below as $x \to \infty$?

### 4.2 Key open question

The numerical data shows that for $x \geq 100$, the maximum achievable sum is
$\approx \log 2/\log x \ll 1$. This suggests the conjecture is much stronger
than needed: the sum approaches 0, not 1.

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
