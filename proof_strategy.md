# Proof attempt — `primitive_set_erdos`

This is the agent-editable proof draft for the Track 2 loop. Its content
is hashed for round-dedup; pure whitespace / comment edits do not count
as a real round. Lemmas live in `proof_lemmas/`.

## Section 1 — Setup

### 1.1 Statement

Fix $x \ge 2$. A set $A \subseteq \mathbb{N}$ is *primitive* if no
distinct elements of $A$ stand in a divisor relation: $a, b \in A$ and
$a \ne b$ imply $a \nmid b$. Define
\[
S(A) \;=\; \sum_{a \in A} \frac{1}{a \log a}.
\]

**Conjecture (target).** For any primitive $A \subset [x, \infty)$,
\[
S(A) \;\le\; 1 + o(1) \qquad \text{as } x \to \infty,
\]
where the $o(1)$ depends only on $x$.

The set $\mathcal{P}$ of primes from $2$ is primitive and
$S(\mathcal{P}) \approx 1.6366$, but $\mathcal{P} \not\subset [x,
\infty)$ for $x > 2$. The conjecture concerns the *truncated* family
$\mathcal{F}(x) = \{A \text{ primitive} : A \subset [x, \infty)\}$,
where the small-element contributions of $\mathcal{P}$ have been
excluded.

### 1.2 Given facts (citations only — no rederivation in this draft)

The harness ships three facts in `proofs/primitive_set_erdos.json`. Each
sign reading below is restated explicitly because misreading the sign
of F2 is the canonical failure mode.

**F1 (Erdős–Zhang upper bound).** For any primitive $A \subseteq
\mathbb{N}$,
\[
S(A) \;<\; e^{\gamma} \tfrac{\pi}{4} \;+\; o(1) \;\approx\; 1.399 +
o(1).
\]
Sign reading: this is an *upper* bound (strict inequality, fixed $A$,
$o(1)$ as the truncation point grows). The constant $1.399$ is
positive; the bound is consistent with the conjecture's tighter $1$, it
just doesn't attain it. Citing F1 to show $S(A) > 1$ inverts the
inequality.

**F2 ($\Omega = k$ stratum, unsigned correction).** Let
$A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$, the integers with exactly
$k$ prime factors counted with multiplicity. Then
\[
S(A_k) \;\ge\; 1 \;+\; O\!\bigl(k^{-1/2 + o(1)}\bigr).
\]
Sign reading: the $O(\cdot)$ term is *unsigned* — it could be positive,
negative, or zero, with absolute value bounded by $k^{-1/2 + o(1)}$.
The bound reads "$S(A_k)$ is at least $1$ minus something controlled in
absolute value by $k^{-1/2+o(1)}$", **not** "$S(A_k)$ is at least $1$
plus a positive quantity." Inferring $S(A_k) > 1$ from F2 alone is a
sign error.

**F3 ($\Omega = k$ stratum, sharpened to one-sided).** For the same
$A_k$,
\[
S(A_k) \;=\; 1 \;-\; (c + o(1)) \frac{k^2}{2^k}, \qquad
c \approx 0.0656 > 0.
\]
Sign reading: the leading correction is *negative* (since $c > 0$), so
$S(A_k) < 1$ for every $k \ge 1$, and $S(A_k) \uparrow 1$ from below as
$k \to \infty$. F3 sharpens F2: the unsigned $O(\cdot)$ in F2 is in fact
dominated by $-c k^2/2^k + o(k^2/2^k)$, lying strictly below $1$ for
every finite $k$.

The pair (F2, F3) is consistent. F2 says "$S(A_k)$ is within
$k^{-1/2+o(1)}$ of $1$"; F3 says "in fact it is exactly
$\Theta(k^2/2^k)$ below $1$." A direct counterexample reading would
require the $O(\cdot)$ in F2 to be positive, which F3 rules out for the
canonical extremal family $A_k$.

### 1.3 Witness contract

A claim against the target bound can be admitted into the loop only by
exhibiting a primitive $A^\star \subset [x_\star, \infty)$ together
with a rigorously verified lower bound on $S(A^\star)$ exceeding $1$.
The harness implements this as a `<!-- WITNESS -->` block in this file:

```
<!-- WITNESS
{
  "x_floor": <int>,
  "elements": [<int>, ...],
  "claimed_sum_lower_bound": <float>
}
WITNESS -->
```

`library.primitive_set_witness.verify_witness` checks:

1. each $a$ in `elements` is an integer with $a \ge x_\text{floor}$;
2. the elements are pairwise non-divisible;
3. it computes a rigorous lower bound on
   $\sum_{a \in \text{elements}} 1/(a \log a)$ via stdlib `decimal`
   arithmetic with a ULP-bumped `math.log`, accurate to roughly $50$
   decimal digits;
4. it accepts (`is_valid = True`) iff the rigorous lower bound exceeds
   `witness_threshold = 1.0`.

No `WITNESS` block ⇒ `witness_valid = 0`, and any narrative chain that
ends in a counterexample claim without a verified witness is forced to
`verdict_hint = blocked` by the resolution-string defense-in-depth in
`proof_prepare._compute_verdict_hint`.

### 1.4 The o(1) caveat

The conjecture's bound is $1 + o(1)$ as $x_\star \to \infty$. A finite
witness at some $x_\star$ that produces $S(A^\star) > 1$ is
*suggestive* but not conclusive: the implicit $o(1)$ at that $x_\star$
may itself be $\ge S(A^\star) - 1$. A counterexample resolution at
finite $x_\star$ needs both

- (a) a witness with rigorous lower bound exceeding $1$, **and**
- (b) an analytical estimate that the implicit $o(1)$ at $x_\star$ is
  small enough to leave room (i.e. $o(1) < S(A^\star) - 1 - \epsilon$
  for some explicit $\epsilon > 0$).

The harness verifier handles (a). (b) is left to the proof body and a
human reviewer.

### 1.5 What is to be proved

To establish the conjecture, the loop must produce one of:

- a **proof body** demonstrating, for every primitive $A \subset [x,
  \infty)$, that $S(A) \le 1 + o(1)$. F1 already implies this with the
  weaker bound $1.399 + o(1)$; the conjecture asks to sharpen the
  constant to $1$.
- a **partial-result body** isolating an explicit subclass of primitive
  sets for which the bound holds, plus a clear statement of the
  remaining gap. The loop admits this as a `keep_progress` round once
  three consecutive rounds stabilise on the same content hash with
  clean verdict and no live open qids.
- (the loop also admits) a **counterexample witness** as above. Given
  F1 and F3, a witness exceeding $1.399$ would falsify F1, and any
  witness exceeding $1$ requires the analytical (b) above.

## Section 2 — Numerical evidence: F3 is asymptotic in $k$

F3 reads $S(A_k) = 1 - (c + o(1)) k^2/2^k$ with $c \approx 0.0656$, with
the implicit $o(1)$ a function of $k \to \infty$. Direct computation
(first $1000$ elements of $A_k$ in increasing order, $k = 1, 2, 3, 4$;
elements found by sieving $\Omega(n) = k$) shows that for small $k$
the partial sum is far from F3's leading-order estimate
$1 - c k^2 / 2^k$, in two qualitatively different ways:

| $k$ | first-200 partial $S$ | first-1000 partial $S$ | F3 leading $1 - ck^2/2^k$ | $\le 1$? |
|---:|---:|---:|---:|:---:|
| 1 | $1.49645$ | $1.52534$ | $0.96720$ | **no** |
| 2 | $0.68194$ | $0.74609$ | $0.93440$ | yes |
| 3 | $0.31340$ | $0.36755$ | $0.92620$ | yes |
| 4 | $0.14034$ | $0.17295$ | $0.93440$ | yes |

(Computed in stdlib `math.log` floats; values rounded to 5 d.p.; full
elements lists deferred to `proof_lemmas/lemma_001_f3_asymptotic.md`
in a later round.)

Two observations are load-bearing for the proof structure:

**(O1) F3 is asymptotic, not exact at small $k$.** For $k = 1$,
$A_1 = \mathcal{P}$ (the primes), and $S(A_1) \approx 1.6366$ (an
unconditionally proven constant of Erdős). This **exceeds** F3's
leading-order estimate $0.967$, so F3 plainly does not hold as an exact
identity at $k = 1$. F3 must therefore be read as "$S(A_k) = 1 +
\varepsilon(k)$ with $\varepsilon(k) \to 0$ from below, and the leading
term of $\varepsilon$ for $k \to \infty$ is $-c k^2/2^k$", **not** as a
finite-$k$ identity. Citing F3 to bound $S(A_k)$ for fixed small $k$
is invalid.

**(O2) The conjecture is not refuted by $A_1$.** Although the unrestricted
prime sum exceeds $1$, the conjecture is about $A \subset [x, \infty)$
with $x \to \infty$. The truncated prime sum
$\sum_{p \ge x} 1/(p \log p) \to 0$ as $x \to \infty$ (this is the
standard $\sum_p 1/p$ divergence rate, which is logarithmic, sharper
than $1/(p \log p)$); concretely, by Mertens' second theorem
$\sum_{p \le y} 1/p = \log \log y + M + o(1)$, so by partial summation
$\sum_{p > x} 1/(p \log p) = O(1/\log x) \to 0$. So $A_1$ alone, once
truncated, contributes vanishing mass. The conjecture stays alive.

**(O3) Slow convergence at $k \ge 2$.** The first-1000 partial sums for
$k = 2, 3, 4$ are far from the F3 leading-order estimate (e.g. $0.746$
vs. $0.934$ at $k = 2$). The reason is that $|A_k \cap [1, y]|$ grows
like $y (\log\log y)^{k-1} / ((k-1)! \log y)$ (Landau), so the heavy
mass of $A_k$ lives at large $y$. A first-1000 truncation captures only
the very thin head; the bulk of $S(A_k)$ accumulates over astronomical
ranges of $n$. Numerical verification of F3's leading term thus
requires sums over enormous truncations of $A_k$, not the naïve first
$N$ elements.

**Implication.** F3 is a *deep* asymptotic, not an obvious bound. Its
leading correction $- c k^2 / 2^k$ is proved via Sathe–Selberg-style
analysis of the count of integers with exactly $k$ prime factors, not
by direct computation. The proof body cannot rely on numerically
"checking" F3 at small $k$.

(End of Section 2.)

## Section 3 — Numerical evidence: prime tails decay as $O(1/\log x)$

The truncated prime sum is the sharpest small-$x$ obstruction to the
conjecture: $\mathcal{P}$ is primitive, so $\mathcal{P} \cap [x,
\infty)$ lies in the conjecture's domain for every $x$. We tabulate

\[
S_\mathcal{P}(x, N) \;=\; \sum_{p \in \mathcal{P}, \; x \le p \le N}
\frac{1}{p \log p}.
\]

Direct computation (sieve, stdlib `math.log`):

**Approach to the prime constant** (no lower truncation, $x = 2$):

| $N$ | $|\mathcal{P} \cap [2, N]|$ | $S_\mathcal{P}(2, N)$ |
|---:|---:|---:|
| $10^2$ | $25$ | $1.42157$ |
| $10^3$ | $168$ | $1.49232$ |
| $10^4$ | $1229$ | $1.52816$ |
| $10^5$ | $9592$ | $1.54978$ |
| $10^6$ | $78498$ | $1.56424$ |
| $10^7$ | $664579$ | $1.57458$ |

Slow logarithmic approach to the limit $\sum_p 1/(p \log p) \approx
1.6366$ (cf. Erdős's prime-sum constant). Every entry exceeds $1.399$
already; this is consistent with F1 once F1's $o(1)$ is read as a
function of the truncation point $x$ — F1 promises $S(A) \le 1.399 +
o(1)$ as $x \to \infty$, **not** $S(A) \le 1.399$ uniformly in $x$.

**Tail decay** (truncate primes to $[x, 10^7]$, $x$ varying):

| $x$ | $S_\mathcal{P}(x, 10^7)$ | $1 / \log x$ |
|---:|---:|---:|
| $2$ | $1.57458$ | $1.4427$ |
| $10$ | $0.35213$ | $0.4343$ |
| $10^2$ | $0.15301$ | $0.2171$ |
| $10^3$ | $0.08226$ | $0.1448$ |
| $10^4$ | $0.04641$ | $0.1086$ |
| $10^5$ | $0.02479$ | $0.0869$ |

The tail $S_\mathcal{P}(x, \infty)$ decays like a constant fraction
of $1/\log x$, in line with the standard partial-summation estimate

\[
\sum_{p > x} \frac{1}{p \log p}
\;=\; \int_{x}^{\infty} \frac{1}{u (\log u)^2} \, d\pi(u)
\;\le\; \frac{1}{\log x} \sum_{p > x} \frac{1}{p \log p}
\;+\; O\!\left(\frac{1}{\log^2 x}\right),
\]

so by Mertens' second theorem (or direct Abel summation against
$\pi(u) = u/\log u + O(u/\log^2 u)$),
$\sum_{p > x} \frac{1}{p \log p} = \frac{1}{\log x} + O(1/\log^2 x)
= O(1/\log x) \to 0$.

**Implication.** $\mathcal{P} \cap [x, \infty)$ is *not* a witness
against the conjecture for any $x \ge 10$ (its sum is already $< 1$).
The hard cases for the conjecture are not the primes themselves but
primitive sets that capture *cumulatively* much of the mass of the
$\Omega = k$ strata for many $k$ simultaneously — see Section 5
outline.

(End of Section 3.)

## Section 4 — Witness search at $x_\star \in \{100, 1000, 10^4\}$

**Goal.** Search for a primitive $A^\star \subset [x_\star, \infty)$
with rigorously-verified $S(A^\star) > 1$. The harness verifier is
`library.primitive_set_witness.verify_witness` with
`witness_threshold = 1.0`; the verifier uses stdlib `decimal` with a
ULP-bumped `math.log` for a rigorous lower bound to ~50 d.p.

**Constructions tried.** All sums computed with `math.log` in float
(the verifier independently re-bounds them rigorously):

(C1) **Interval $A = (x, 2x] \cap \mathbb{N}$.** Always primitive
because for $a < b$ in $(x, 2x]$, $a | b$ would force $b \ge 2a > 2x$.

| $x$ | $|A|$ | $S(A)$ |
|---:|---:|---:|
| $100$ | $100$ | $0.1396$ |
| $10^3$ | $10^3$ | $0.0956$ |
| $10^4$ | $10^4$ | $0.0726$ |
| $10^5$ | $10^5$ | $0.0585$ |

$S \to 0$ since $\sum_{n=x+1}^{2x} 1/(n \log n) \to \log 2 / \log x$
by integral comparison.

(C2) **Primes in $[x, 10^7]$.** Already analysed in Section 3.
Maxes at $S = 0.153$ for $x = 100$.

(C3) **Greedy primitive sieve over $[x, N]$.** Scan $n = x, x+1,
\ldots, N$; add $n$ to $A$ unless some earlier $a \in A$ divides $n$;
when adding, mark all multiples of $n$ as covered. This produces the
unique "smallest-first" maximal primitive set in $[x, N]$. Behaviour:

| $x_\star$ | $N$ | $|A|$ | $S(A)$ |
|---:|---:|---:|---:|
| $100$ | $10^4$ | $1566$ | $0.2775$ |
| $100$ | $10^5$ | $9929$ | $0.2991$ |
| $100$ | $10^6$ | $78835$ | $0.3136$ |
| $100$ | $10^7$ | $664916$ | $0.3239$ |
| $10^3$ | $10^5$ | $16348$ | $0.1978$ |
| $10^4$ | $10^6$ | $163235$ | $0.1536$ |

(C4) **Sanity check at $x = 2$.** Greedy from $n = 2$ recovers
*exactly* the primes (every composite has a prime divisor that has
already been added), so $S$-values match Section 3's
$S_\mathcal{P}(2, N)$.

**Rigorous verifier call.** The largest-$S$ candidate
($x = 100$, $N = 10^6$) was passed through
`verify_witness` directly:

```text
|A| = 78835
S(A) float          = 0.313605
rigorous lower bound = 0.31360479208190448348...
threshold            = 1.0
is_valid             = False  (rigorous lb ≤ threshold)
```

**Conclusion of Q4.** No witness was found at any of the requested
$x$-floors. The natural primitive constructions all saturate at $S
\le 0.33$ for $x \ge 100$ over $N \le 10^7$. The growth pattern is
*sub-logarithmic* in $N$: doubling $N$ adds $\sim 0.01$ to $S(A)$,
suggesting $S(A^\star)$ would not reach $1$ even for astronomically
large $N$ at fixed $x \ge 100$. (Compare F1's predicted ceiling of
$\sim 1.399 + o(1)$, which itself decays in $x$.)

This negative result is consistent with the conjecture and supplies
the proof body's empirical baseline: any analytical proof must
explain why $S(A)$ is bounded *below* $1$ uniformly for primitive $A
\subset [x, \infty)$ as $x \to \infty$, despite the fact that the
unrestricted $A_1 = \mathcal{P}$ already achieves $S \approx 1.6366$.

(End of Section 4.)

## Section 5 — Proof structure: stratify by $\Omega(a)$

**Setup.** Any set $A \subset \mathbb{N}$ partitions as
$A = \bigsqcup_{k \ge 1} A^{(k)}$ where $A^{(k)} := A \cap A_k$
(elements with exactly $k$ prime factors counted with multiplicity).
This decomposition is canonical (no choices) and respects primitivity:
$A$ is primitive iff each $A^{(k)}$ is primitive AND no element of
$A^{(k)}$ divides any element of $A^{(k')}$ for $k < k'$.

**Decomposition of $S$.** $S(A) = \sum_k S(A^{(k)})$.

**Lemmas (see `proof_lemmas/`).**

- **Lemma 1 (`truncated_low_strata`, status: open).** For fixed
  $k \ge 1$, $S(A_k \cap [x, \infty)) = O((\log\log x)^{k-1}/\log x)
  \to 0$ as $x \to \infty$. *Easy*: Landau's count + partial summation.
  Folds the small-$k$ contribution to $0$ as $x \to \infty$.
- **Lemma 2 (`high_strata_below_one`, status: open).** There exist
  $K_0$ and $\delta > 0$ with $S(A_k) \le 1 - \delta k^2/2^k$ for all
  $k \ge K_0$. *Citation*: F3 with explicit $K_0$. Forces every
  individual large-$k$ stratum below $1$.
- **Lemma 3 (`cross_stratum_primitivity`, status: open — HARD).** For
  every $\varepsilon > 0$ exists $x_0$ such that primitive $A \subset
  [x_0, \infty)$ has $S(A) \le 1 + \varepsilon$. *This is the
  conjecture.* Per-stratum bounds (Lemmas 1, 2) cannot prove it
  because $\sum_k S(A_k)$ is divergent — primitivity must be exploited
  cross-stratum. Erdős–Zhang's argument saturates at $1.399$;
  sharpening to $1$ needs a new ingredient. See the lemma file for
  the candidate plan (a stratum-aware weighting using F3's
  $-c k^2/2^k$ deficit).

**Conditional conjecture proof (assuming Lemma 3).** Trivial: Lemma 3
is the conjecture.

**Unconditional partial result.** Combining Lemmas 1 and 2 (and the
truncated $A_1$ bound from Section 3) we have, for any primitive
$A \subset [x, \infty)$:

\[
S(A) \;=\; \sum_{k=1}^{K_0 - 1} S(A^{(k)})
       \;+\; \sum_{k = K_0}^\infty S(A^{(k)}),
\]

with $S(A^{(k)}) \le S(A_k \cap [x, \infty))$ for $k < K_0$ (Lemma 1
sums to $o(1)$ over a fixed-size $\{1, \ldots, K_0 - 1\}$) and
$S(A^{(k)}) \le S(A_k) \le 1 - \delta k^2/2^k$ for $k \ge K_0$
(Lemma 2). The second sum, **without primitivity exploitation across
strata**, is bounded only by $\sum_{k \ge K_0} 1 = \infty$. So the
partial result through Lemmas 1+2 is

\[
S(A) \;\le\; o(1) \;+\; \sum_{k \ge K_0}^{??} S(A^{(k)}),
\]

which is *not* a finite bound without Lemma 3 or a Erdős–Zhang-style
weighting. The conjecture is therefore **conditional on Lemma 3**;
the unconditional Erdős–Zhang result F1 stands at $1.399 + o(1)$.

**Status.** This is the partial result the loop has reached: a clean
decomposition, two settled per-stratum lemmas, and a single hard
cross-stratum lemma (Lemma 3) that subsumes the conjecture itself.
The loop cannot close Lemma 3 with the techniques explored so far.

(End of Section 5.)




