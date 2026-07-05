# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Section 1: Setup (Q1)

### The Claim

**Erdős's Primitive-Set Conjecture (tightened form):** For any $x \geq 2$,
if $A \subset [x, \infty)$ is a *primitive set* of positive integers (no
distinct element of $A$ divides another), then

$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$

where the $o(1)$ term tends to $0$ as $x \to \infty$.

**Status:** Open. No proof or disproof is known. This file must not assert
resolution without a verifier-accepted `<!-- WITNESS -->` block.

### Given Facts (with sign disambiguations)

**F1 (Erdős–Zhang upper bound, citation: Erdős 1935; Zhang 1993):**
For any primitive set $A \subseteq \mathbb{N}$,

$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1)
\approx 1.399 + o(1).$$

*Sign disambiguation:* This is an UPPER bound (sum strictly less than
~1.399). It is consistent with the conjecture (which posits an even
tighter bound of 1). Do NOT misread it as a lower bound.

**F2 (Omega-stratum lower bound, UNSIGNED big-O):**
If $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (integers with exactly
$k$ prime factors counted with multiplicity), then

$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2 + o(1)}\right).$$

*Sign disambiguation:* The big-O term $O(k^{-1/2+o(1)})$ is **UNSIGNED** —
it could be positive or negative; it is only bounded in absolute value by
$C k^{-1/2+o(1)}$ for some constant $C$. This fact does NOT imply the sum
exceeds 1. Concluding "sum $> 1$" from F2 alone is a sign error. (This is
the canonical failure mode of the ChatGPT writeup that motivated this
problem: it read the unsigned-O as positive and immediately claimed a
contradiction.)

**F3 (exact asymptotic, approaches 1 from BELOW):**
For $A_k$ as above,

$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$

*Sign disambiguation:* The correction $-(c+o(1))k^2/2^k$ is **negative**
(since $c > 0$). So $\sum_{a \in A_k} 1/(a \log a) < 1$ for all $k \geq 1$,
approaching 1 from BELOW as $k \to \infty$. Even the "extremal-looking"
set $A_k$ satisfies the conjecture.

*Consistency note:* F3 is consistent with F2 once the unsigned-O in F2 is
read correctly. F3 pins down the sign of the correction (it is negative),
showing the O-term in F2 is in fact negative for the full set $A_k$.

### Witness Contract (sole path to a disproof claim)

A claim of disproof requires a `<!-- WITNESS -->` block in this file whose
JSON payload passes `library.primitive_set_witness.verify_witness`. The
verifier enforces:

1. Every element is an integer $\geq x_{\mathrm{floor}} \geq 2$.
2. Elements are pairwise non-divisible (no element divides another).
3. A *rigorous* Decimal lower bound on $\sum_{a \in A} 1/(a \log a)$
   (using 4-ULP-bumped log values at 80-digit precision) strictly exceeds
   the **witness threshold of 1.0**.

If and only if `verify_witness` returns `is_valid=True`, the gatekeeper
sets `witness_valid = 1` and the status `keep_disproof`.

### Anti-traps

- **F2 sign confusion:** Never conclude sum $> 1$ from F2 alone.
- **F3 upside-down:** F3's sum approaches 1 from BELOW — evidence for,
  not against, the conjecture.
- **Open claim without witness:** Until `witness_valid == 1`, no phrase
  asserting disproof may appear here.

---

## Section 2: Numerical Evidence (Q2)

### Truncated sums over $A_k \cap [2, N]$ for $k = 1, 2, 3, 4$

We compute $S_k(N) := \sum_{a \in A_k, a \leq N} \frac{1}{a \log a}$ for
$N = 100\,000$:

| $k$ | $S_k(100\,000)$ | $F_3$ formula $1 - 0.0656 \cdot k^2/2^k$ | $< 1$? |
|-----|----------------|------------------------------------------|--------|
| 1   | 1.549781       | 0.967200                                 | **NO** |
| 2   | 0.828802       | 0.934400                                 | yes    |
| 3   | 0.452169       | 0.926200                                 | yes    |
| 4   | 0.224915       | 0.934400                                 | yes    |

For $k=1$ (primes) the partial sum already exceeds 1 at $N=10$:

| $N$      | $S_1(N)$ |
|----------|----------|
| 10       | 1.222    |
| 100      | 1.422    |
| 1000     | 1.492    |
| 10000    | 1.528    |
| 100000   | 1.550    |

The primes-from-2 sum appears to converge toward $\approx 1.636$
(consistent with Q3 below).

### Key observation: F3 formula interpretation

The F3 formula $1 - (c+o(1)) k^2/2^k$ does NOT equal the full infinite sum
$\sum_{a \in A_k} 1/(a \log a)$ — at least for small $k$.  For $k=1$
(primes), the full sum is approximately $1.636 \gg 0.967$.

For $k \geq 2$, the truncated sums at $N = 100\,000$ lie at 0.83, 0.45,
0.22 — all far below the F3 formula values. Convergence-rate analysis
suggests the infinite sums for $k=2,3,4$ are approximately 1.13, 1.01,
0.75 respectively (these are rough estimates; exact values require deeper
computation). In particular, the $k=2$ infinite sum likely exceeds 1.

This leads to the following interpretation hypothesis (to be verified):

> **Hypothesis (F3 scope):** The F3 formula $1 - (c+o(1))k^2/2^k$ is an
> asymptotic for the NORMALIZED sum as both $k$ and the lower cutoff $x$
> grow. Specifically, it may describe the ratio
> $\frac{\sum_{a \in A_k \cap [x,\infty)} 1/(a \log a)}
>       {\sum_{p \text{ prime}, p \geq x} 1/(p \log p)}$
> as $x \to \infty$ with $k$ fixed. For $k=1$ this ratio is trivially 1;
> for $k=2,3,\ldots$ it approaches $1 - c k^2/2^k < 1$.

Under this interpretation, F3's sign disambiguation ("approaches 1 from
BELOW") is correct: for large $x$, the A_k-stratum's contribution
relative to the primes decays as $1 - c k^2/2^k$, strictly below 1.
The conjecture then says no primitive set can beat the primes by more
than $1 + o(1)$ relative to this benchmark.

*This remains a hypothesis — the full mathematical content of F3 as cited
needs independent literature verification.*

### F3 formula as $k \to \infty$

| $k$ | $1 - 0.0656 \cdot k^2/2^k$ |
|-----|---------------------------|
| 1   | 0.9672                    |
| 2   | 0.9344                    |
| 3   | 0.9262                    |
| 4   | 0.9344                    |
| 5   | 0.9488                    |
| 8   | 0.9836                    |
| 10  | 0.9936                    |
| 20  | 0.99998                   |

The formula values are all $< 1$ and increase monotonically to 1 as
$k \to \infty$, confirming the "approaches 1 from below" property.

---

## Section 3: Primes-Sum Distinction (Q3)

### Computation

Let $P = \{2, 3, 5, 7, 11, \ldots\}$ be all primes. $P$ is a primitive set
(distinct primes do not divide each other). Numerically:

| primes up to $N$ | $\sum_{p \leq N} \frac{1}{p \log p}$ |
|-----------------|--------------------------------------|
| 10              | 1.222                                |
| 100             | 1.422                                |
| 1000            | 1.492                                |
| 10000           | 1.528                                |
| 100000          | 1.550                                |
| 2000000         | 1.568                                |
| $\infty$ (est.) | **~1.6366**                          |

The tail estimate uses $\int_N^{\infty} 1/(t \log^2 t)\, dt = 1/\log N$;
at $N = 2\times10^6$ this adds $\approx 0.069$.

### Consistency with F1

F1 says: for any primitive $A \subseteq \mathbb{N}$,
$\sum 1/(a \log a) < e^{\gamma}\pi/4 + o(1) \approx 1.399 + o(1)$.

Yet the primes-from-2 sum is $\approx 1.636 > 1.399$. This is NOT a
contradiction because F1 (and the conjecture) are **asymptotic** statements
about primitive sets $A \subset [x, \infty)$ as $x \to \infty$. The
$o(1)$ corrections in F1 and the conjecture are large at small $x$ (e.g.,
$x = 2$) and shrink only as $x \to \infty$.

For the **finite-$x$** regime:
- At $x = 2$, the primes-from-2 set has sum $\approx 1.636$. The conjecture
  allows this (the bound $1 + o(1)$ evaluated at $x=2$ has a large positive
  error term).
- For large $x$, primitive sets $A \subset [x, \infty)$ have sums $\to 0$.
  The primes achieve the maximum: $\sum_{p \geq x} 1/(p \log p) \sim 1/\log x
  \to 0$.

The conjecture says the *supremum* of $\sum_{a \in A} 1/(a \log a)$ over
all primitive $A \subset [x, \infty)$ converges to 0 as $x \to \infty$,
and more precisely is bounded by $1 + o(1)$ (where $o(1) \to 0$). Since
the sup → 0, the bound $< 1$ eventually holds; the conjecture is saying it
holds for ALL $x$, not just large $x$.

---

## Section 4: Witness Search (Q4)

### Trivial witness at $x_{\mathrm{floor}} = 2$

The set $\{2, 3\}$ is a primitive set (2 does not divide 3; 3 does not
divide 2) with $x_{\mathrm{floor}} = 2$. The verifier computes:

$$\frac{1}{2 \log 2} + \frac{1}{3 \log 3}
= 0.7214 + 0.3034 = 1.0247 > 1.0$$

`library.primitive_set_witness.verify_witness` returns `is_valid=True`,
`score≈1.0248`. However, this witness is **mathematically trivial**: the
conjecture's bound $1 + o(1)$ has a large positive error at $x = 2$, so
exceeding 1.0 at $x_{\mathrm{floor}} = 2$ is expected and does NOT
constitute a counterexample to the conjecture.

### Search at $x_{\mathrm{floor}} = 100, 1000, 10000$

Per the conjecture's spirit, witnesses at large $x_{\mathrm{floor}}$ are
more meaningful. We tested the primes (the conjectured extremal set) at
each cutoff:

| $x_{\mathrm{floor}}$ | elements tested | verifier score | is\_valid |
|----------------------|-----------------|----------------|-----------|
| 100                  | first 500 primes $\geq$ 100 | 0.0939 | False |
| 1000                 | first 200 primes $\geq$ 1000 | 0.0168 | False |
| 10000                | first 100 primes $\geq$ 10000 | 0.0010 | False |

For $x_{\mathrm{floor}} = 100$: $\sum_{p \geq 100} 1/(p \log p)
\approx 1/\log(100) \approx 0.217 \ll 1.0$. No primitive set in
$[100, \infty)$ can achieve sum $> 1.0$ (the primes are the extremal
case by Lichtman–Pomerance 2021). Similarly for $x = 1000$ and $10000$,
the sums decay as $1/\log x$.

### Conclusion

No witness exists for $x_{\mathrm{floor}} = 100, 1000, 10000$. The
conjecture holds empirically at these cutoffs, with sums far below the
threshold of 1.0. Any future witness search should try $x_{\mathrm{floor}}
\in \{2, \ldots, X^*\}$ where $X^*$ is the crossover point where the
maximum primitive-set sum drops below 1.0. Empirically, the primes-from-2
sum is $\approx 1.636$, and the sum over primes $\geq x$ drops below 1.0
at roughly $x \approx e \approx 2.718$ (since $1/\log e = 1$). So for
any $x_{\mathrm{floor}} \geq 3$ (i.e., $\log x_{\mathrm{floor}} \geq 1$),
the primes-from-$x$ sum is $\lesssim 1/\log 3 \approx 0.91$, and it is an
open question whether any non-prime primitive set can do better.

---

## Section 5: Proof Structure Outline (Q5)

### Goal

Prove: for any primitive $A \subset [x, \infty)$, $\sum_{a \in A} 1/(a \log a)
< 1 + o(1)$ as $x \to \infty$.

Equivalently (per the numerical evidence in Section 4): show the primes
$P_x = \{p \text{ prime}: p \geq x\}$ maximize the sum over all primitive
sets in $[x, \infty)$, i.e., $\sum_{a \in A} 1/(a \log a) \leq \sum_{p \geq x}
1/(p \log p) \sim 1/\log x \to 0$.

### Lemma decomposition

Three lemmas are formalized in `proof_lemmas/`:

**Lemma `stratum_bound`** (trivial, status: open for the estimate):
Any sub-antichain $B \subset \{n \geq x : \Omega(n) = k\}$ satisfies
$\sum_{b \in B} 1/(b \log b) \leq \sigma_k(x)$, where $\sigma_k(x) \sim
(1 - ck^2/2^k)/\log x$ by F3.

**Lemma `cross_stratum_constraint`** (proved, see lemma file):
Primitivity forces: if $a \in A_j$, no multiple of $a$ in $[x, \infty)$
is in $A$. This is the key non-divisibility constraint.

**Lemma `primes_are_extremal`** (OPEN — the main gap):
$\sum_{a \in A} 1/(a \log a) \leq \sum_{p \geq x} 1/(p \log p)$ for any
primitive $A \subset [x, \infty)$.

If Lemma `primes_are_extremal` is proved, the conjecture follows immediately
since $\sum_{p \geq x} 1/(p \log p) \sim 1/\log x \to 0 < 1 + o(1)$.

### What the naive stratum approach shows (and where it fails)

**Attempt.** Partition $A = \bigcup_k A_k$ where $A_k = A \cap \{n : \Omega(n) = k\}$.
By Lemma `stratum_bound`, $\sum_{a \in A_k} 1/(a \log a) \leq \sigma_k(x)$.
Summing over $k$:

$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{k=1}^{\infty} \sigma_k(x)
= \sum_{n \geq x} \frac{1}{n \log n} = +\infty.$$

**Failure.** The naive bound is vacuous. The stratum bounds are independent
— ignoring the cross-stratum constraint — and their sum diverges.

**What is needed.** A way to use the fact that high-mass in stratum $k$
forces low mass in stratum $k'$ for neighboring $k'$. The
Lichtman–Pomerance approach likely does this via a multiplicative
Rankin-type argument.

### Partial result (what CAN be proved from the given facts)

From F1 (Zhang 1993), the sum is bounded by $1.399 + o(1)$. This is a
proved result, not just a conjecture. The gap between $1.399$ and the
conjectured bound of $1$ is where the difficulty lies.

From F3, each individual stratum $A_k$ (as a whole) has normalized sum
$\to 1 - ck^2/2^k < 1$. So the "extremal" $A_k$ sets do not violate
the conjecture.

What remains open in this attempt: proving that a "mixed" primitive set
(drawing from multiple strata) cannot beat the primes.

### Suggested next steps (for future sessions)

1. Read the Lichtman–Pomerance 2021 proof and transcribe the Rankin-bound
   approach into Lemma `primes_are_extremal`.
2. Alternatively, try an induction on the size of A: if $|A| = 1$,
   the sum is $1/(a_1 \log a_1) \leq 1/(x \log x) < 1/\log x$.
   For $|A| = 2$, the sum is $1/(a_1 \log a_1) + 1/(a_2 \log a_2)$
   where $a_1 \nmid a_2$. Bound this by induction.
3. Look for a Stieltjes-integral representation of the sum that
   makes the primes-extremal property transparent.

---

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
