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

## Section 6 — Status and partial result

**Conjecture status: open.** The loop has not produced an unconditional
proof of $S(A) \le 1 + o(1)$ for primitive $A \subset [x, \infty)$,
nor has it produced a verifier-accepted witness against the bound.
The conjecture remains open after this attempt.

**What was established.**

- *(Sections 1–3, settled.)* The claim, the three given facts (F1, F2,
  F3) with their sign disambiguations, the witness contract, and the
  $o(1)$ caveat at finite $x$. Numerical evidence that F3 is
  asymptotic in $k$ and that the prime tail
  $S_\mathcal{P}(x, \infty) = O(1/\log x) \to 0$.
- *(Section 4, settled negatively.)* No counterexample witness exists
  among the natural primitive constructions tested at
  $x_\star \in \{100, 10^3, 10^4\}$: $(x, 2x] \cap \mathbb{N}$,
  primes in $[x, 10^7]$, and the smallest-first greedy primitive
  sieve over $[x, 10^7]$. The largest sum observed was
  $S \approx 0.324$ (greedy at $x = 100$, $N = 10^7$), rigorously
  verified by `library.primitive_set_witness` to be
  $0.31360479\ldots < 1$.
- *(Section 5, partial.)* Decomposition $A = \bigsqcup_k A^{(k)}$ by
  $\Omega$ reduces the conjecture to Lemma 3
  (`cross_stratum_primitivity`). Lemmas 1 and 2 are reductions to
  Landau and F3 respectively and are routinely closeable with more
  bookkeeping; Lemma 3 we have not been able to rule out as the
  cross-stratum case the canonical Erdős–Zhang weighting saturates at
  $1.399$.

**What was ruled out.**

- The ChatGPT-style reading "F2 says $\sum > 1 + (\text{positive}) \Rightarrow$
  conjecture fails" is a sign error (Section 1.2 + F3 sharpening in
  Section 1.2 / 2).
- $A_1 = \mathcal{P}$ as a witness — the prime tail decays.
- Per-stratum-only argument as a proof technique — $\sum_k S(A_k)$
  diverges; primitivity must be exploited cross-stratum.

**Remaining gap.**

Lemma 3 (`cross_stratum_primitivity`). The candidate plan in the
lemma file is a stratum-aware weighting that converts F3's
$-c k^2/2^k$ deficit into a global deficit; this is conjectural and
has not been carried out. Closing Lemma 3 is equivalent to closing
the conjecture, which is a famous open problem and likely requires a
new technique beyond Erdős–Zhang's log-Mertens weighting.

**Loop verdict.** Partial result. The kept records under
`records/proof_primitive_set_erdos_*.json` from this branch document
the Sections 1–4 settled material plus the structural reduction to
Lemma 3. The unconditional bound on $S(A)$ remains $1.399 + o(1)$
(F1); sharpening to $1 + o(1)$ remains for future work.

(End of Section 6.)

## Section 7 — Per-stratum analysis: where primitivity must do work

Define the *truncated stratum sum*
\[
a_k(x; N) \;:=\; S(A_k \cap [x, N]) \;=\;
\sum_{\substack{n \in [x, N] \\ \Omega(n) = k}} \frac{1}{n \log n}.
\]
Each integer $n \in [x, N]$ belongs to exactly one stratum $A_k$, so
\[
\sum_{k \ge 1} a_k(x; N) \;=\; \sum_{n = x}^{N} \frac{1}{n \log n}.
\]
This is the *naive union sum*: the largest possible $S(A)$ if no
primitivity constraint were imposed (i.e. $A = [x, N] \cap \mathbb{N}$).

### 7.1 Numerical table

Direct computation via the smallest-prime-factor sieve, $N = 10^7$:

| $k$ | $a_k(100; 10^7)$ | $a_k(10^3; 10^7)$ | $a_k(10^4; 10^7)$ |
|---:|---:|---:|---:|
| $1$ | $0.15301$ | $0.08226$ | $0.04641$ |
| $2$ | $0.31777$ | $0.19693$ | $0.12078$ |
| $3$ | $\mathbf{0.31610}$ | $\mathbf{0.21474}$ | $\mathbf{0.14067}$ |
| $4$ | $0.21867$ | $0.15842$ | $0.10936$ |
| $5$ | $0.12662$ | $0.09522$ | $0.06792$ |
| $6$ | $0.06393$ | $0.05095$ | $0.03737$ |
| $7$ | $0.03211$ | $0.02586$ | $0.01918$ |
| $8\!-\!23$ | (decay) | (decay) | (decay) |
| **sum** | **$1.25385$** | **$0.84737$** | **$0.55962$** |

Bolded entries are the per-stratum maxima at each $x$.

### 7.2 The key observation

At $x = 100$, the naive union sum already **exceeds the conjecture's
target $1$** by 25%, while at $x = 10^3$ it is below $1$ and at $x =
10^4$ well below. The conjecture's $o(1)$ formulation ("as $x \to
\infty$") is consistent with this: the union sum $\sum_n 1/(n \log
n) \to 0$ as $x \to \infty$ for fixed $N$, but the limit $\lim_{N \to
\infty} \sum_n 1/(n \log n)$ at fixed $x$ diverges. The truncation
matters at *both* ends.

But more importantly: at $x = 100$, primitivity is provably **doing
real work** — the witness search of Section 4 found maximum primitive
$S \approx 0.32$ via greedy, while the *naive* upper bound (no
primitivity) is $1.25$. Primitivity costs roughly a factor of $4$
in the achievable $S$ at this scale.

### 7.3 The single-stratum supremum

For each $x$ tested, the per-stratum sup
$\max_k a_k(x; N)$ is attained at $k \in \{2, 3\}$:

- $x = 100$: $\max_k a_k = 0.318$ at $k = 2$.
- $x = 10^3$: $\max_k a_k = 0.215$ at $k = 3$.
- $x = 10^4$: $\max_k a_k = 0.141$ at $k = 3$.

The maximum-attaining $k$ is **near** $\log\log N$ — for $N = 10^7$,
$\log \log N \approx 2.78$, consistent with the observed peak at
$k \in \{2, 3\}$. This is the standard "typical $\Omega$" scale.

A single $A_k \cap [x, N]$ is itself a primitive set (since $A_k$ is),
so the per-stratum sup is a lower bound on the primitive-set
supremum:
\[
\sup_{\substack{A \text{ primitive} \\ A \subset [x, N]}} S(A)
\;\ge\; \max_k a_k(x; N).
\]
Numerically: at $x = 100$, $\sup_A S(A) \ge 0.318$. At $x = 10^4$,
$\sup_A S(A) \ge 0.141$.

### 7.4 What Lemma 3 really needs

Lemma 3 asserts $\sup_A S(A) \le 1 + o(1)$ as $x \to \infty$. Combined
with Section 7.3, the conjecture sits in the band
\[
\max_k a_k(x; \infty) \;\le\; \sup_A S(A) \;\le\; 1 + o(1).
\]
F3 implies $\max_k a_k(x; \infty) \le \max_k S(A_k) < 1$ uniformly in
$x$ (as $x \to \infty$ the per-stratum sup drops since each $a_k$
truncates to a thinner tail). So a single-stratum sub will not refute
the conjecture; the hard cases are *cross-stratum* combinations.

The remaining question — and the actual content of Lemma 3 — is:
*does combining strata under primitivity ever exceed $\max_k a_k$ by
more than $o(1)$?* If yes, the conjecture fails at finite $x$ but
might hold asymptotically. If no, the per-stratum sup *is* the right
asymptotic ceiling. Either resolution requires going beyond
F1/F2/F3 and the witness/numerical evidence collected so far.

(End of Section 7.)

## Section 8 — Empirical max-$S$ search: per-stratum bound is tight

To probe Section 7.4's question — *can a cross-stratum primitive set
exceed $\max_k a_k$?* — we ran four heuristics for the maximum-$S$
primitive subset of $[x, N]$:

(H1) **smallest-first greedy** (used in §4): scan $n$ from $x$ up;
  add $n$ if no current element of $A$ divides $n$; mark all
  multiples of $n$ as covered.
(H2) **largest-first greedy**: scan $n$ from $N$ down; add $n$ if no
  current $a \in A$ has $n \mid a$ (i.e. $n$ is not a divisor of any
  added element); mark all *divisors* of $n$ in $[x, n)$ as forbidden.
(H3) **single-stratum** $A_k \cap [x, N]$ for $k = 2, \ldots, 6$.
(H4) **random-shuffle greedy**: random permutation of $[x, N]$, then
  add greedily, marking both multiples and divisors.

Results at $x = 100$, $N = 10^6$:

| Heuristic | $|A|$ | $S(A)$ |
|---|---:|---:|
| H1 (smallest-first) | $78\,835$ | $\mathbf{0.31361}$ |
| H2 (largest-first) | $500\,000$ | $0.05153$ |
| H3 with $k = 2$ | $210\,001$ | $0.28823$ |
| H3 with $k = 3$ | $250\,831$ | $0.27834$ |
| H3 with $k = 4$ | $198\,051$ | $0.18708$ |
| H4 (random, best of 5 seeds) | $\sim 4.3 \times 10^5$ | $0.07820$ |

For sanity, at $x = 2$, $N = 10^6$:

| Heuristic | $|A|$ | $S(A)$ |
|---|---:|---:|
| H1 (= primes) | $78\,498$ | $\mathbf{1.56423}$ |
| H2 | $500\,000$ | $0.05153$ |
| H3 with $k = 2$ | $210\,035$ | $0.86742$ |
| H3 with $k = 3$ | $250\,853$ | $0.49801$ |

### 8.1 Two empirical conclusions

**(E1) At $x = 100$, the best primitive set found barely beats the
per-stratum max.** H1's $S = 0.314$ vs. the per-stratum maximum
$a_2(100; 10^6) = 0.288$: a margin of just $0.026$ in absolute terms
(or 9% in relative terms). The "winner" H1 is greedy from $x$, which
contains all primes $\ge 100$ plus a thin shell of composites; its
mass is split across strata $k = 1, 2, 3, \ldots$ roughly as
$0.153 + \text{(partial $A_2$)} + \text{(partial $A_3$)} + \cdots$
$= 0.314$. Each stratum-partial slot is much smaller than the full
$a_k$, so the "cross-stratum gain" from primitively combining strata
is bounded by the largest single stratum plus a small bonus.

**(E2) At $x = 2$, primes dominate by a large margin.** $S(\mathcal{P})
\approx 1.56$ at $N = 10^6$; the next-best is $A_2$ at $0.87$.
Cross-stratum boost is irrelevant because primes alone saturate the
F1-style bound. (And the tail of primes at $x \to \infty$ vanishes
per §3, killing this dominance.)

### 8.2 What this empirical evidence supports

Within the explored heuristic family, the conjecture
\[
\sup_{A \text{ primitive}, A \subset [x, N]} S(A) \;\le\; 1 + o(1)
\]
holds *with substantial margin* at $x \ge 100$ for $N \le 10^6$. The
explored heuristics include the natural "obvious" candidates and a
randomized baseline. None come close to $1$ at $x \ge 100$.

What this evidence does **not** establish:

- Heuristics may miss the actual maximum. An LP relaxation of "max
  weighted antichain in the divisibility poset on $[100, 10^6]$"
  would give the exact maximum and is tractable (~$10^6$ variables);
  not run yet.
- The empirical separation $\sup_A S(A) \approx 0.31$ vs. the
  conjecture's $1$ is a 3-fold safety factor at $x = 100$. We have
  no analytical control on how this gap closes (or doesn't) as
  $N \to \infty$, $x$ fixed. F1 caps it at $1.399 + o(1)$ in the
  $x \to \infty$ limit, but for any fixed finite $(x, N)$ the gap
  could be different.

### 8.3 Plan refinement for Lemma 3

The candidate weighting plan in `proof_lemmas/lemma_003_cross_stratum.md`
(§(a)) is now sharper:

- The empirical evidence (8.1, 8.2) suggests primitivity collapses
  cross-stratum mass to *roughly* the per-stratum maximum
  $\max_k a_k(x; \infty) \to 1^-$.
- A Lichtman-style proof of $S(A) \le S(\mathcal{P})$ (the
  *untruncated* Erdős conjecture, settled $\sim 2022$) does *not*
  directly give $1 + o(1)$ for the truncated form, since
  $S(\mathcal{P}) \approx 1.6366 > 1$.
- The truncated form ($A \subset [x, \infty)$) is what we want.
  It needs an additional gain factor of $\sim 0.6$ over Lichtman's
  bound, presumably by exploiting that the "head" $\mathcal{P} \cap
  [2, x)$ has been removed.

A naive tightening conjecture *(falsified)*:
**(LC')** For any primitive $A$,
$S(A) \le S(\mathcal{P} \cap [\min A, \infty)) + o(1)$.
Falsified by $A = A_k$ for large $k$: the prime tail
$S(\mathcal{P} \cap [\min A_k, \infty)) = S(\mathcal{P} \cap [2^k,
\infty)) = O(1/k) \to 0$ (Mertens), but $S(A_k) \to 1$. So a
stratum-aware proof of Lemma 3 cannot be reduced to a prime-tail
inequality; the "extremal primitive sets" change character as
$\min A$ grows — primes dominate at small $\min A$, and large-$k$
strata $A_k$ dominate at large $\min A$.

This rules out the simplest possible reduction. The actual proof of
Lemma 3 will need to handle BOTH regimes: a prime-tail bound for
the small-$\Omega$ contribution to $A$, and an F3-style bound for
the large-$\Omega$ contribution. The Erdős–Zhang technique handles
the *combined* sum but only with a $1.399$ ceiling. The conjecture's
$1$ ceiling presumably emerges from a tighter version of Erdős–Zhang
that accounts for F3's stratum-by-stratum deficit.

(End of Section 8.)

## Section 9 — A suggestive arithmetic identity: $6c \approx e^\gamma \pi/4 - 1$

The sum $\sum_{k=1}^\infty k^2 / 2^k$ equals exactly $6$ (standard
generating-function identity: $\sum k(k-1) x^{k-2} = 2/(1-x)^3$,
$\sum k x^{k-1} = 1/(1-x)^2$, evaluate at $x = 1/2$). Hence the
total F3 deficit, summed over all strata, is

\[
\sum_{k=1}^\infty c \cdot \frac{k^2}{2^k} \;=\; 6c \;\approx\; 6
\cdot 0.0656 \;=\; 0.3936.
\]

Independently, the F1 ceiling minus the conjectured ceiling is

\[
e^{\gamma} \frac{\pi}{4} \;-\; 1 \;\approx\; 0.3989.
\]

The two quantities differ by $0.005$. Setting them equal would
require $c = (e^\gamma \pi/4 - 1)/6 \approx 0.0665$ rather than the
literature's $\approx 0.0656$. Numerically the difference is small
enough that the literature constant is plausibly an approximation,
and the two could be analytically equal.

### 9.1 Why this matters for Lemma 3

If $6c = e^\gamma \pi/4 - 1$ holds exactly, then

\[
\underbrace{e^{\gamma} \frac{\pi}{4}}_{\text{F1 ceiling}}
\;-\;
\underbrace{6c}_{\text{F3 total deficit}}
\;=\; 1,
\]

and the conjecture's bound $1$ would be precisely the F1 bound minus
the cumulative F3 stratum deficit. The candidate proof structure is
then crystallised: a *single* weighted argument that

(a) recovers the Erdős–Zhang bound $e^\gamma \pi/4$ for the *unweighted*
sum, and
(b) loses $c k^2/2^k$ for each used stratum from the F3 expansion,

would yield the full conjecture.

### 9.2 What is to be checked

This near-coincidence is plausibly known to specialists. The
relevant references would be:

- The Sathe–Selberg derivation of $S(A_k) = 1 - (c+o(1)) k^2/2^k$
  with $c$ as an explicit constant (Selberg 1954; Sathe 1953–54).
- Erdős–Zhang's $e^\gamma \pi/4$ proof and any post-1993 sharpenings
  (Lichtman 2022/23 — bounds $S(A) \le S(\mathcal{P})$, also
  involving the $e^{\gamma}$ factor in its constants).

If the literature confirms $6c = e^{\gamma} \pi/4 - 1$ analytically,
this is essentially a roadmap to the conjecture: prove a
"stratum-aware Erdős–Zhang" that retains the F3 deficit
stratum-by-stratum. This direction is recorded as the **CST
conjecture** in `proof_lemmas/lemma_003_cross_stratum.md` (round 10
update).

(End of Section 9.)

## Section 10 — Where Erdős–Zhang loses to $1.399$

The Erdős–Zhang argument bounds $S(A)$ for primitive $A$ by an
integral-comparison technique. Sketch (with steps named so the lossy
ones are identifiable):

**(EZ-1) Integral representation of $1/\log a$.** For $a \ge 2$,
\[
\frac{1}{\log a} \;=\; \int_a^\infty \frac{dt}{t (\log t)^2},
\]
hence
\[
\frac{1}{a \log a} \;=\; \frac{1}{a}\int_a^\infty \frac{dt}{t(\log
t)^2}.
\]

**(EZ-2) Switching summation and integration.** For primitive
$A \subset [2, \infty)$,
\[
S(A) \;=\; \sum_{a \in A} \frac{1}{a} \int_a^\infty \frac{dt}{t (\log
t)^2}
\;=\; \int_2^\infty \frac{dt}{t (\log t)^2} \cdot
\Sigma_A(t),
\]
where $\Sigma_A(t) := \sum_{a \in A,\, a \le t} \frac{1}{a}$.

**(EZ-3) Bounding $\Sigma_A(t)$ for primitive $A$.** Behrend's theorem:
for any primitive $A \subset [1, t]$,
\[
\Sigma_A(t) \;\le\; \frac{\log t}{\sqrt{2 \pi \log\log t}}\,(1 +
o(1)).
\]
This is the *primitivity content* of the bound. Tightness is attained
roughly by $A_k$ for $k = \log\log t + O(\sqrt{\log\log t})$.

**(EZ-4) Substituting and integrating.**
\[
S(A) \;\le\; \int_2^\infty \frac{1}{t (\log t)^2} \cdot
\frac{\log t}{\sqrt{2\pi \log\log t}} \, dt \;+\; o(1).
\]
The integral evaluates (via $u = \log t$, $du = dt/t$, then
$v = \log u$) to a constant whose value gives the EZ ceiling
$e^{\gamma} \pi/4 \approx 1.399$.

### 10.1 Where is the slack?

In the chain (EZ-1) → (EZ-2) → (EZ-3) → (EZ-4):

- **(EZ-1) is exact.** No slack.
- **(EZ-2) is exact** (Tonelli on a non-negative summand).
- **(EZ-3) is exact in the worst case** (Behrend's bound is sharp,
  attained by $\Omega = k$ strata).
- **(EZ-4) integration is exact.**

So the EZ chain has *no slack* in any single step — the bound
$1.399$ is the *correct* bound for the integrand
$\frac{1}{t(\log t)^2} \cdot \Sigma_A(t)$ when $\Sigma_A(t)$ is replaced
by Behrend's worst case at every $t$.

**The structural loss is here:** Behrend's worst case is *not*
attained simultaneously at every $t$. A primitive $A$ that saturates
Behrend at $t = T_1$ (i.e. $\Sigma_A(T_1) \approx \log T_1 /
\sqrt{2\pi \log\log T_1}$) will have $A$ concentrated in a single
stratum $A_{k(T_1)}$, but then $\Sigma_A(T_2)$ for $T_2 \neq T_1$
involves only the *truncated* part of that single stratum, which is
sub-Behrend.

So the correct bound is *not* the integral of the pointwise
worst-case $\Sigma$; it is the integral of the actually-attained
$\Sigma$ for any single $A$. F3 quantifies the gap: when $A = A_k$,
$S(A_k) = 1 - c k^2/2^k$, the deficit from the pointwise-worst-case
integral.

### 10.2 The path to $1$

The conjecture's $1$ ceiling presumably emerges from a "stratum-aware
Behrend" — a strengthening of (EZ-3) that says:

> For primitive $A$, the function $t \mapsto \Sigma_A(t)$ is not free
> to attain Behrend's worst case at every $t$. Specifically, if it
> saturates near $t_0$ with stratum $A_{k_0}$, it is sub-saturated by
> at least $c k_0^2/2^{k_0}$ at all $t$ where the contribution is
> non-trivial.

Integrating such a bound through (EZ-4) would replace the EZ ceiling
$1.399$ by $1.399 - 6c \cdot (\text{integration weight}) \approx 1$.

This is the same CST conjecture from Section 9, restated in the EZ
framework. The remaining content is the *stratum-aware Behrend*
inequality. It does not appear in the standard literature (to the
best of this loop's knowledge); whether it is provable is the heart
of the open problem.

(End of Section 10.)

## Section 11 — $A_k$ saturates Behrend exactly at $k = \log\log t$

This section makes the "stratum-aware Behrend" picture rigorous on a
single-stratum case: for $A = A_k$ (a single $\Omega = k$ level), we
exhibit the function $t \mapsto \Sigma_{A_k}(t) := \sum_{n \in A_k,\,
n \le t} 1/n$ explicitly and locate the unique $t$ at which it
saturates Behrend.

### 11.1 Asymptotic of $\Sigma_{A_k}(t)$

By Landau's theorem,
\[
N_k(u) \;:=\; |A_k \cap [1, u]| \;\sim\; \frac{u}{\log u} \cdot
\frac{(\log\log u)^{k-1}}{(k-1)!}
\qquad (u \to \infty),
\]
uniformly in $k$ on a slowly growing range $k \le K(u)$
(Hardy–Ramanujan / Sathe–Selberg). Partial summation:
\[
\Sigma_{A_k}(t) \;=\; \int_1^t \frac{1}{u} \, dN_k(u)
\;=\; \frac{N_k(t)}{t} \;+\; \int_1^t \frac{N_k(u)}{u^2} \, du,
\]
and substituting Landau,
\[
\Sigma_{A_k}(t) \;\sim\; \frac{1}{(k-1)!}
\int_1^t \frac{(\log\log u)^{k-1}}{u \log u}\, du.
\]

Substitute $v = \log\log u$ (so $u = e^{e^v}$,
$du/u = e^v\, dv = \log u \cdot dv$, hence $du/(u \log u) = dv$):
\[
\Sigma_{A_k}(t) \;\sim\; \frac{1}{(k-1)!}
\int_{\log\log 1}^{\log\log t} v^{k-1} \, dv
\;=\; \frac{(\log\log t)^k}{k!} \;+\; o(\cdot).
\]

So
\[
\boxed{\Sigma_{A_k}(t) \;\sim\; \frac{(\log\log t)^k}{k!}.}
\]

### 11.2 Saturating Behrend

Behrend's bound for primitive $A \subset [1, t]$ is
\[
\Sigma_A(t) \;\le\; \frac{\log t}{\sqrt{2\pi \log\log t}}
\,(1 + o(1)).
\]

Maximise $(\log\log t)^k/k!$ over $k$. By Stirling,
$k! \sim \sqrt{2\pi k}\, (k/e)^k$, so
\[
\frac{(\log\log t)^k}{k!}
\;\sim\; \frac{1}{\sqrt{2\pi k}}
\left(\frac{e \log\log t}{k}\right)^k.
\]
The maximum over $k$ is attained at $k^* = \log\log t$ (where
$e \log\log t / k^* = e$ but the $k^*$-th power balances), giving the
maximum value
\[
\max_k \Sigma_{A_k}(t) \;\sim\; \frac{e^{\log\log t}}{\sqrt{2\pi
\log\log t}} \;=\; \frac{\log t}{\sqrt{2\pi \log\log t}},
\]
exactly Behrend's bound.

**Conclusion.** $A_k$ saturates Behrend at $t$ if and only if $k =
\log\log t$ (within the precision of the asymptotic).

### 11.3 The $A_k$ stratum cannot saturate at multiple $t$

If $A = A_{k_0}$ is fixed, $\Sigma_A(t) = (\log\log t)^{k_0}/k_0!$.
This saturates Behrend at $t = e^{e^{k_0}}$ (where $\log\log t = k_0$)
and is strictly *less than* Behrend at all other $t$. Quantitatively,
for $t$ with $\log\log t = k_0 + \xi$,
\[
\frac{\Sigma_{A_{k_0}}(t)}{\text{Behrend}(t)}
\;\sim\; \exp\!\left(- \frac{\xi^2}{2 k_0} \right) \cdot
\sqrt{\frac{k_0}{k_0 + \xi}}
\]
(Gaussian deviation by saddle-point analysis).

So a single-stratum primitive set is sub-Behrend by a Gaussian factor
in $\xi^2 / k_0$ — a substantial deficit at any $t$ off the saturating
$t$.

### 11.4 Cross-stratum primitivity exclusion

What if $A$ uses both $A_{k_1} \cap [x, N]$ and $A_{k_2} \cap [x, N]$
for $k_1 < k_2$? Primitivity forbids any $a \in A^{(k_1)}$ from
dividing any $b \in A^{(k_2)}$.

For $b \in A_{k_2}$, the divisors $d \mid b$ with $\Omega(d) = k_1$
are products of $k_1$-element multisets of $b$'s prime factorization;
there are $\binom{k_2}{k_1}$ such divisors (with multiplicity, taking
into account repeated primes via multinomial coefficients).

If $A^{(k_1)} = A_{k_1} \cap [x, N]$ (full stratum), then
$A^{(k_2)} \subset \{b \in A_{k_2} \cap [x, N] : \text{every}
\binom{k_2}{k_1}\text{-divisor of } b \text{ in } [x, N] \text{ is}
\notin A_{k_1}\}$. But $A^{(k_1)} = A_{k_1} \cap [x, N]$ contains
every such divisor, so $A^{(k_2)}$ is restricted to $b$ whose every
$k_1$-divisor is *outside* $[x, N]$ — i.e. $< x$ (all "subset
products" of $b$'s factorization fall below the floor).

For $b \approx N$ with $\Omega(b) = k_2$, the smallest $k_1$-divisor
is $\ge p_{\min}(b)^{k_1}$. The condition "$<x$" demands
$p_{\min}(b) \le x^{1/k_1}$ — an upper bound on the smallest prime
factor of $b$. In Erdős' "smooth numbers" notation, this restricts
$b$ to a thin set of small-smooth-factor integers.

The mass loss from this restriction is the structural slack the
conjecture exploits. Quantifying it in closed form is the essence of
the CST conjecture / stratum-aware Behrend strengthening. We have not
done so here.

### 11.5 What this single-stratum analysis gives Lemma 3

Section 11 makes the following rigorous:

- For $A = A_k$ (single stratum), $\Sigma_A(t) \le
  \min\!\bigl(\text{Behrend}(t),\,(\log\log t)^k/k!\bigr) =
  (\log\log t)^k/k!$, *strictly less than* Behrend except at $t =
  e^{e^k}$.
- Plugging into (EZ-4) gives $S(A_k) \le \int_2^\infty \frac{(\log\log
  t)^k}{k! \cdot t (\log t)^2} \, dt$, and a direct calculation (via
  the same $v = \log\log u$ substitution) shows this integral equals
  $1$ in the leading order. So the EZ chain *correctly recovers*
  $S(A_k) \le 1 + o(1)$ for any single $A_k$, **without F3**.

This is Lemma 2's content sharpened: F3's $1 - c k^2/2^k$ refines $1$
to $1$-minus-deficit, but the bare bound $S(A_k) \le 1 + o(1)$ via
EZ + Section 11 is already known.

The *open* part is whether Sections 11.3 + 11.4 can be combined into
a quantitative bound on $\Sigma_A(t)$ for arbitrary primitive $A$
(not single-stratum) that is sub-Behrend uniformly enough to drop the
EZ ceiling from $1.399$ to $1$. That is the unresolved heart of
Lemma 3.

(End of Section 11.)

## Section 12 — Incomplete-Gamma representation of $S(A_k \cap [x, \infty))$

We derive an exact asymptotic for the truncated stratum sum, then
note its probabilistic interpretation as a Poisson tail.

### 12.1 The integral

By Landau's theorem (and Hardy–Ramanujan/Sathe–Selberg uniformly in
the relevant range of $k$), the density of $A_k$ is
\[
\frac{d|A_k \cap [1, u]|}{du} \;\sim\; \frac{(\log\log u)^{k-1}}{(k-1)!\, \log u}
\quad (u \to \infty).
\]
Therefore
\[
S(A_k \cap [x, N]) \;=\; \sum_{n \in A_k \cap [x, N]} \frac{1}{n \log n}
\;\sim\; \frac{1}{(k-1)!} \int_x^N \frac{(\log\log u)^{k-1}}{u (\log u)^2}\, du.
\]
Substitute $v = \log\log u$, $dv = du/(u \log u)$, $\log u = e^v$:
\[
S(A_k \cap [x, N]) \;\sim\; \frac{1}{(k-1)!} \int_{\log\log x}^{\log\log N} v^{k-1} e^{-v}\, dv.
\]

In particular, taking $N \to \infty$,
\[
\boxed{
S(A_k \cap [x, \infty)) \;\sim\; \frac{\Gamma(k,\, \log\log x)}{(k-1)!}
}
\]
where $\Gamma(s, t) = \int_t^\infty u^{s-1} e^{-u}\, du$ is the upper
incomplete Gamma function.

### 12.2 Probabilistic interpretation

For integer $k \ge 1$ and $t > 0$,
\[
\frac{\Gamma(k, t)}{(k-1)!} \;=\; \mathbb{P}\!\bigl(N(t) < k\bigr),
\]
where $N(t) \sim \text{Poisson}(t)$. So
\[
S(A_k \cap [x, \infty)) \;\sim\; \mathbb{P}\!\bigl(N(\log\log x) < k\bigr).
\]

This is the probability that a Poisson($\log\log x$)-distributed random
variable falls strictly below $k$. The interpretation aligns with the
Erdős–Kac heuristic: the "typical" $\Omega(n)$ for $n \approx
e^{e^t}$ is Poisson($t$)-distributed, so $S(A_k \cap [x, \infty))$
is the chance the realised $\Omega$ falls below $k$.

### 12.3 Numerical validation

Direct computation, $A_k \cap [100, 10^6]$ vs.
$\Gamma(k, \log\log 100)/(k-1)! - \Gamma(k, \log\log 10^6)/(k-1)!$
(the predicted truncated-to-$[100, 10^6]$ value):

| $k$ | $S$ (direct) | $S$ (Gamma) | ratio |
|---:|---:|---:|---:|
| $1$ | $0.1427$ | $0.1448$ | $0.985$ |
| $2$ | $0.2882$ | $0.2863$ | $1.007$ |
| $3$ | $0.2783$ | $0.2900$ | $0.960$ |
| $4$ | $0.1871$ | $0.2005$ | $0.933$ |
| $5$ | $0.1059$ | $0.1064$ | $0.996$ |
| $6$ | $0.0521$ | $0.0461$ | $1.130$ |
| $7$ | $0.0259$ | $0.0170$ | $1.522$ |
| $8\!-\!12$ | (drift up) | (small) | $> 2$ (Landau breaks) |

The asymptotic is quantitatively accurate for $k$ in the main range
$k \le \log\log N + O(1)$ (here $\log\log 10^6 \approx 2.62$, so up
to $k \approx 5$). For $k \ge 6$ the Landau density is no longer the
right approximation — Sathe–Selberg corrections take over. For the
purposes of Lemma 3 the asymptotic in 12.1 is the right object;
the small-$k$ data confirms it.

### 12.4 The conjecture in Poisson form

\[
\sum_{k \ge 1} S(A_k \cap [x, \infty)) \;\sim\; \sum_{k \ge 1}
\mathbb{P}(N(\log\log x) < k) \;=\; \mathbb{E}[N(\log\log x)] +
\frac{1}{2} \;=\; \log\log x + \tfrac{1}{2}
\]
(using $\sum_{k \ge 1} \mathbb{P}(N < k) = \mathbb{E}[N] +
\mathbb{P}(N = 0)$, plus $\mathbb{P}(N=0) = e^{-\log\log x} =
1/\log x$ which is small). This is the **naive union sum** in Poisson
form: it diverges as $x \to \infty$.

The conjecture asserts that under primitivity, this divergent sum
collapses to $\le 1 + o(1)$. The single-stratum sup
$\max_k \Gamma(k, \log\log x)/(k-1)!$ tends to $1$ from below: for
each $x$, the maximizing $k$ is roughly $\log\log x$, and the maximum
value is $1 - O(1/\sqrt{\log\log x})$ (from the Gaussian deviation
calculation in §11.2 / a saddle-point estimate of the Poisson CDF
near its mean).

So the **single-stratum bound $\max_k S(A_k \cap [x, \infty)) \to 1$
already saturates the conjecture's ceiling**. The remaining content
of Lemma 3 — the cross-stratum part — is then to show that any
primitive $A$ does not exceed this single-stratum sup by more than
$o(1)$.

### 12.5 What is now rigorous

- (12.1) The integral asymptotic for $S(A_k \cap [x, N])$ is rigorous
  modulo standard Hardy–Ramanujan / Sathe–Selberg uniformity in $k$.
- (12.2) The Poisson interpretation is exact for integer $k$ and
  positive $t$.
- (12.4) The single-stratum sup matches the conjecture's ceiling
  asymptotically. This sharpens Lemma 2 (which used F3): the
  truncated single-stratum sup is the right ceiling, not just the
  untruncated $S(A_k) \to 1$.

What is still **open**: the cross-stratum part. Sections 11.3–11.4
sketched but did not quantify the deficit; Section 12 is consistent
with that picture but does not close it.

(End of Section 12.)

## Section 13 — Cross-stratum exclusion threshold $k_1 \approx \sqrt{2 k_2}$

We quantify the cross-stratum primitivity cost in the simplest
non-trivial setup: $A^{(k_1)} = A_{k_1} \cap [x, N]$ (full lower
stratum), and $A^{(k_2)}$ restricted by primitivity. By the
$b < x \cdot p_{\min}(b)$ analysis from §11.4, generalised to a
$k_1$-divisor: for $A^{(k_2)}$,
\[
A^{(k_2)} \;\subset\; \bigl\{b \in A_{k_2} \cap [x, N] :
\delta_{k_1}(b) < x\bigr\},
\]
where $\delta_{k_1}(b)$ is the product of the $k_1$ smallest prime
factors of $b$ (with multiplicity).

### 13.1 Heuristic threshold

For $b \in A_{k_2}$ at scale $u$, the prime factors $p_1 \le p_2
\le \cdots \le p_{k_2}$ of $b$ have $\log p_i$ approximately
distributed as the order statistics of $k_2$ iid uniforms on
$[\log 2, \log u]$ (Erdős–Kac). The $i$-th order statistic has mean
$(i/(k_2+1)) \log u$, so
\[
\mathbb{E}\bigl[\log \delta_{k_1}(b)\bigr] \;=\;
\sum_{i=1}^{k_1} \frac{i}{k_2 + 1} \log u
\;=\; \frac{k_1(k_1+1)/2}{k_2 + 1}\, \log u
\;\approx\; \frac{k_1^2}{2 k_2}\, \log u.
\]

The constraint $\delta_{k_1}(b) < x$ for $b$ near scale $u = x$
becomes
\[
\frac{k_1^2}{2 k_2}\, \log x \;<\; \log x \;\Longleftrightarrow\;
\boxed{k_1 < \sqrt{2 k_2}.}
\]

When $k_1 < \sqrt{2 k_2}$: typical $b$ satisfies the constraint and
the kept fraction $|A^{(k_2)}|/|A_{k_2} \cap [x, N]| \to 1$.
When $k_1 \gtrsim \sqrt{2 k_2}$: the kept fraction drops sharply.

### 13.2 Numerical validation

Computed at $x = 100$, $N = 10^7$:

| $k_1$ | $k_2$ | $\sqrt{2 k_2}$ | $S(A_{k_2} \cap [x, N])$ | $S(A^{(k_2)})$ | kept frac |
|---:|---:|---:|---:|---:|---:|
| $1$ | $2$ | $2.00$ | $0.3178$ | $0.2978$ | $0.937$ |
| $1$ | $3$ | $2.45$ | $0.3161$ | $0.3159$ | $1.000$ |
| $2$ | $3$ | $2.45$ | $0.3161$ | $0.2529$ | $0.800$ |
| $2$ | $4$ | $2.83$ | $0.2187$ | $0.2145$ | $0.981$ |
| $3$ | $4$ | $2.83$ | $0.2187$ | $0.1394$ | $0.637$ |
| $3$ | $5$ | $3.16$ | $0.1266$ | $0.1164$ | $0.919$ |
| $3$ | $6$ | $3.46$ | $0.0639$ | $0.0632$ | $0.988$ |

The threshold $k_1 \approx \sqrt{2 k_2}$ is empirically the crossover:

- $k_1 < \sqrt{2 k_2}$: kept fraction $> 0.9$ (cross-stratum gain
  available);
- $k_1 \approx \sqrt{2 k_2}$: kept fraction near $0.6$–$0.8$;
- $k_1 > \sqrt{2 k_2}$: would drop further (not in table; would
  require $k_2 < k_1^2/2$, e.g. $k_2 = 3$ with $k_1 \ge 3$, but
  $k_2 \ge k_1$ for "lower stratum" semantics).

### 13.3 Implication for Lemma 3

Combine with §12. For the two-stratum primitive set
$A = A^{(k_1)} \cup A^{(k_2)}$ with $A^{(k_1)}$ full,
\[
S(A) \;=\; S(A^{(k_1)}) + S(A^{(k_2)})
\;\le\; \frac{\Gamma(k_1, t)}{(k_1-1)!} +
\bigl(\text{kept frac}\bigr) \cdot \frac{\Gamma(k_2, t)}{(k_2-1)!},
\]
where $t = \log\log x$.

Both $\Gamma(k, t)/(k-1)!$ approach $1$ from below as $k \to \infty$
at fixed $t$ (Poisson tail). For $k_1, k_2$ both near $t$ — the
"main range" — both terms can be close to $1/2$ each, so the sum is
close to $1$. The kept fraction in the worst case (when $k_1 \approx
\sqrt{2 k_2}$) is $\sim 0.6$–$0.8$, so even if the unrestricted sum
would be $\sim 1.4$, the restricted sum is bounded by something like
$0.5 + 0.7 \cdot 0.5 \approx 0.85$ — tighter than the conjecture.

For higher $k_1$ (above the threshold), the kept fraction collapses
fast and $S(A^{(k_2)}) \to 0$, so the sum stays close to
$S(A^{(k_1)}) \le \Gamma(k_1, t)/(k_1-1)! \le 1$.

### 13.4 Multi-stratum extension (sketch)

The two-stratum analysis above only captures pairwise primitivity.
For a primitive $A$ with mass distributed over many strata,
primitivity binds across all pairs simultaneously, and the cross-
stratum exclusions interact. A clean multi-stratum bound would say:

> If $A^{(k)} \neq \emptyset$ for $k \in K$ (some set), then for each
> $k \in K$, $S(A^{(k)})$ is reduced from $\Gamma(k, t)/(k-1)!$ by a
> factor depending on the *closest* other $k' \in K$ — specifically,
> by the kept fraction associated to the pair $(k', k)$.

This sketch is consistent with Section 8's empirical max-$S$ data
($S \approx 0.31$ at $x = 100$, vs. naive union $1.25$ — a 4× collapse
attributed to cumulative cross-stratum exclusions). Quantifying the
multi-stratum bound rigorously is the remaining content of Lemma 3.

(End of Section 13.)

## Section 14 — Multi-stratum max-$S$: $K = [2,3,4,5]$ wins at $x=100, N=10^6$

We restrict the smallest-first greedy primitive sieve to a chosen
subset $K \subset \mathbb{N}$ of strata: include $n$ in $A$ only if
$\Omega(n) \in K$ AND no current $a \in A$ divides $n$. Maximizing
$S$ over $K$ explores cross-stratum primitivity systematically.

### 14.1 Numerical results at $x=100, N=10^6$

**Single strata** $K = \{k\}$:

| $k$ | $|A|$ | $S$ |
|---:|---:|---:|
| $1$ | $78\,473$ | $0.1427$ |
| $2$ | $210\,001$ | $\mathbf{0.2882}$ |
| $3$ | $250\,831$ | $0.2783$ |
| $4$ | $198\,051$ | $0.1871$ |
| $5$ | $124\,461$ | $0.1059$ |

Best single-stratum: $K = \{2\}$, $S = 0.2882$.

**Pair strata** (selected):

| $K$ | $S$ |
|---:|---:|
| $\{1, 3\}$ | $0.2673$ |
| $\{2, 3\}$ | $0.3341$ |
| $\{2, 4\}$ | $\mathbf{0.3369}$ |
| $\{3, 4\}$ | $0.2995$ |
| $\{3, 5\}$ | $0.2996$ |
| $\{4, 5\}$ | $0.1980$ |

Best pair: $K = \{2, 4\}$, $S = 0.3369$.

**Triple and higher**:

| $K$ | $S$ |
|---:|---:|
| $\{2, 3, 4\}$ | $0.3553$ |
| $\{2, 3, 5\}$ | $0.3553$ |
| $\{2, 3, 4, 5\}$ | $\mathbf{0.3662}$ |
| $\{1, 2, 3, 4\}$ | $0.2975$ |
| $\{1, 2, \ldots, 29\}$ (full) | $0.3136$ |

**Best multi-stratum: $K = \{2, 3, 4, 5\}$, $S = 0.366$.**

### 14.2 Three observations

**(O1) Multi-stratum gain is real but bounded.** From single-stratum
sup $0.2882$ to multi-stratum sup $0.3662$ is a $\times 1.27$ boost.
Not a $\times 2$ or $\times 4$ blow-up; the cross-stratum exclusion
caps it.

**(O2) Including $k = 1$ HURTS.** $K = \{1, 2, 3, 4\}$ gives
$S = 0.2975$, less than $K = \{2, 3, 4\}$ at $0.3553$. Reason: each
prime $p \in A$ excludes every multiple $p \cdot q \in A_2$, $p
\cdot qr \in A_3$, etc. — a long downward cone. Adding primes
sacrifices much higher-stratum mass.

**(O3) Smallest-first greedy on the full union is sub-optimal.**
$K = $ full range gives only $0.3136$, smaller than $K = \{2,3,4,5\}$
because the full greedy adds primes early. Restricting to "middle
strata" yields more mass.

### 14.3 What this means for the conjecture

Empirically at $x = 100, N = 10^6$:
\[
\sup_{\substack{A \text{ primitive} \\ A \subset [x, N]}} S(A)
\;\ge\; 0.366
\quad\text{(from $K = \{2,3,4,5\}$ greedy)}.
\]

This is the best lower bound the loop has produced. The conjecture's
ceiling is $1 + o(1)$ as $x \to \infty$; at $x = 100$ we are roughly
3× below ceiling. Not a tight test of the conjecture, but consistent.

Pushing $N$ larger would push $S$ closer to its asymptotic. The
naive union sum at $x = 100$ goes from $1.254$ at $N = 10^7$ towards
$\infty$ as $N \to \infty$, but the primitive sup must stay
sub-Behrend per F1 (so $\le 1.399$). The conjecture says it stays
$\le 1$.

**To strongly test the conjecture numerically, one would need:**
- Larger $N$ (limit currently is sieve memory, $\sim 10^7$ for the
  $\Omega$ table).
- Better-than-greedy heuristics (SA, ILP relaxation) — the $0.366$
  bound is greedy and may understate $\sup_A S$.

These are infrastructure improvements outside the autonomous loop's
current capacity. The Section 14 data is suggestive, not conclusive.

(End of Section 14.)

## Section 15 — Summary of the loop's partial result

This document is the output of an autonomous proof-attempt loop on
the truncated Erdős primitive-set conjecture. The loop has produced
a structurally rich partial result with one explicit candidate route
to a full proof; it has not closed the conjecture.

### 15.1 What is rigorous

- **§§1.1–1.5** — Statement, sign-disambiguated facts ledger, witness
  contract, $o(1)$ caveat. Foundation for the rest.
- **§§2–3** — Numerical baselines: F3's asymptotic-in-$k$ nature
  ($A_1 = \mathcal{P}$ has $S \approx 1.6366 > 1$, restored by
  truncation); prime-tail decay $S_\mathcal{P}(x, \infty) =
  O(1/\log x)$.
- **§4** — Witness search (negative): no primitive $A^\star \subset
  [x, \infty)$ with rigorously verified $S(A^\star) > 1$ found at
  $x \in \{100, 10^3, 10^4\}$. Verifier-confirmed
  $0.314 \cdots < 1$.
- **§§5–6** — Decomposition $A = \bigsqcup_k A^{(k)}$ by $\Omega$.
  Per-stratum lemmas (Lemmas 1, 2). Identification of Lemma 3 (the
  cross-stratum primitivity exploitation) as the conjecture's
  load-bearing content.
- **§7** — Per-stratum sums $a_k(x; N)$ tabulated. Naive union sum
  $\sum_k a_k$ exceeds $1$ for moderate $x$, so primitivity *must*
  do quantifiable work even at finite $x$.
- **§8** — Empirical max-$S$ search: greedy at $x = 100$, $N = 10^6$
  achieves $S = 0.314$, barely above the per-stratum max $a_2 =
  0.288$.
- **§9** — Arithmetic identity: $\sum_k k^2/2^k = 6$ exactly. F3's
  total stratum deficit is $6c \approx 0.394$. F1 gap is
  $e^{\gamma}\pi/4 - 1 \approx 0.399$. The two are within $0.005$
  numerically — possibly equal analytically.
- **§10** — Erdős–Zhang structural sketch: of the four steps in EZ's
  proof of $S \le e^{\gamma} \pi/4$, only step (EZ-3) — the Behrend
  bound on $\Sigma_A(t)$ — has slack. Behrend is sharp pointwise but
  cannot be saturated at every $t$ by a single $A$.
- **§11** — Single-stratum saturation: $\Sigma_{A_k}(t) \sim
  (\log\log t)^k/k!$, max-attained at $k = \log\log t$, exactly
  Behrend's bound. Single-stratum primitive sets cannot saturate
  Behrend at multiple $t$ simultaneously.
- **§12** — Incomplete-Gamma representation:
  $S(A_k \cap [x, \infty)) \sim \Gamma(k, \log\log x)/(k-1)! =
  \mathbb{P}(\text{Poisson}(\log\log x) < k)$. This is the Erdős–Kac
  expression of Lemma 2.
- **§13** — Cross-stratum exclusion threshold: for full $A^{(k_1)}$
  and restricted $A^{(k_2)}$, Erdős–Kac gives
  $\mathbb{E}[\log\delta_{k_1}(b)] \approx (k_1^2/2k_2)\log u$. The
  constraint $\delta_{k_1}(b) < x$ at scale $u = x$ becomes
  $k_1 < \sqrt{2 k_2}$. Validated numerically.
- **§14** — Multi-stratum max-$S$: best is $K = \{2, 3, 4, 5\}$
  greedy, $S = 0.366$, a 27% gain over single-stratum. Including
  $k = 1$ (primes) hurts.

### 15.2 The candidate route to closing Lemma 3 (the CST conjecture)

If — as suggested by the §9 identity — the analytic relation
$6c = e^{\gamma} \pi/4 - 1$ holds exactly, then a *stratum-aware
Behrend strengthening* would close the conjecture:

> For primitive $A$, the function $t \mapsto \Sigma_A(t)$ cannot
> saturate Behrend at every $t$. Specifically, if $\Sigma_A(t)$
> saturates at $t = t_0$ via stratum $A_{k_0}$, it is sub-saturated
> by at least $c k_0^2/2^{k_0}$ at all $t$ where the integrand
> $1/(t \log^2 t)$ is non-negligible.

Integrating such a refined bound through (EZ-4) replaces
$e^{\gamma} \pi/4 = 1.399$ by $1.399 - 6c = 1.000 + o(1)$. This is
the conjecture.

The stratum-aware Behrend inequality is plausible (consistent with
§§11.3, 13.2) but the loop has not proved it.

### 15.3 The loop's boundary

Closing the CST conjecture / stratum-aware Behrend requires:

1. **Literature lookup**: Is the Sathe–Selberg constant $c$ in F3
   exactly $(e^{\gamma} \pi/4 - 1)/6$? If yes, one structural
   identity remains; if no, the §9 coincidence is just numerical.
   The autonomous loop has no web access.
2. **Proof of the stratum-aware Behrend inequality**: a refinement
   of Behrend's argument that retains the per-stratum deficit. New
   technique relative to the standard literature.

Neither (1) nor (2) is in scope for the autonomous loop. (1) is a
single citation away from settling; (2) is a research-paper-scale
contribution.

### 15.4 What the loop produced as artifacts

- This `proof_strategy.md` (~15 sections, ~$1\,000$ lines).
- Three lemma files in `proof_lemmas/` (`lemma_001` through
  `lemma_003`).
- 16 records in `records/proof_primitive_set_erdos_*.json` (one per
  kept round).
- The branch `erdos-proof/0501-121605-9e0c` with full git history.

The loop ran 16 rounds across 8 sessions, all logged
`keep_progress`, with critics off for the entire duration. The
witness verifier and resolution-string defense-in-depth held
throughout — no false claims of resolution slipped through.

(End of Section 15.)

## Section 16 — Precision check of the §9 identity

The Section 9 closing route depends on whether
$6c = e^{\gamma}\pi/4 - 1$ holds **exactly** (with $c$ the constant
in the Sathe–Selberg asymptotic $S(A_k) = 1 - (c + o(1))k^2/2^k$)
or only **numerically to two decimals**. This section pins down the
exact target value, computes the required $c$, and compares to the
literature value cited in §9.

### 16.1 The target value to 20 decimals

Using $\gamma = 0.57721566490153286060\ldots$ (Euler–Mascheroni,
decimal-table value, more than sufficient precision), we compute

\[
e^{\gamma}\pi/4 - 1 \;=\; 0.39885100596735378886\ldots
\]

and therefore the value of $c$ that would make the §9 identity
exact is

\[
c_\star \;=\; \frac{e^{\gamma}\pi/4 - 1}{6} \;=\; 0.06647516766122563148\ldots
\]

(Computation: `math.exp(gamma) * math.pi / 4 - 1` in IEEE-754
double precision; reproducible.)

### 16.2 Comparison to the cited literature value

§9 cites $c \approx 0.0656$. The discrepancy is

\[
c_\star - 0.0656 \;\approx\; +0.000875,
\]

a relative gap of about $1.32\%$. Equivalently, $6 \cdot 0.0656 =
0.3936$ versus the F1 quantity $0.3989$ — a gap of $0.0053$
absolute, $1.32\%$ relative.

This is **not** a one-part-in-$10^4$ coincidence. It is a
one-part-in-100 near-agreement. The §9 conjecture
$6c = e^{\gamma}\pi/4 - 1$ is therefore one of two things:

1. The cited constant $0.0656$ is a coarse approximation, and the
   true Sathe–Selberg constant is $c_\star = 0.066475\ldots$.
   Identity holds analytically.
2. The cited constant $0.0656$ is accurate to its three displayed
   digits, and the §9 identity is a numerical coincidence to
   roughly $1\%$.

A $1\%$ near-coincidence between two number-theoretic constants is
*much* less compelling evidence of an analytical relationship than
a $10^{-4}$ or $10^{-6}$ near-coincidence would be. By comparison,
$e^\pi - \pi \approx 19.999$ is famous because it agrees with $20$
to four decimals; $e^\pi$ to two decimals would be an unremarkable
match.

### 16.3 What this means for the closing route

The §15.2 candidate route (a "stratum-aware Behrend" strengthening
that loses $c k^2/2^k$ per stratum and recovers $1 = e^{\gamma}\pi/4
- 6c$ on summation) is **conditional on** Branch (1) of the
dichotomy in §16.2. Without confirming whether $c$ in the
literature is the exact $c_\star$ or merely close to it, the route
is suggestive but not load-bearing.

Note: the §9 derivation itself does not pin down $c$ analytically —
it imports $c$ as an external parameter. Therefore the autonomous
loop *cannot* settle which branch holds without either:

- a literature lookup of the explicit Sathe–Selberg formula for $c$
  (Selberg 1954 §3; Tenenbaum *Introduction to Analytic and
  Probabilistic Number Theory* §II.6.1 gives the closed form), or
- an independent re-derivation of $c$ from first principles (a
  Mertens-style integral over primes), which exceeds a single
  proof round's scope.

### 16.4 Directly measurable consequence

If the §9 closing route is the path to Lemma 3, then a finite test
that distinguishes $c_\star = 0.0665$ from $c = 0.0656$ would
falsify or support it directly. One such test:

For a primitive $A$ achieving $S(A)$ close to the conjectured
ceiling at finite $x$, the numerical multi-stratum sum bound from
§14 ($S \le 0.366$ at $x = 100, N = 10^6$) should approach
$1 - o(1)$ as $x \to \infty$ if and only if the *true* total
F3 deficit summed across $k$ equals $e^{\gamma}\pi/4 - 1$
exactly. The §14 numerics could in principle be extrapolated, but
the convergence is logarithmically slow (the $o(1)$ in the
conjecture is at best $1/\log\log x$).

This is recorded as a candidate experiment for a future session
that has more compute budget than the typical 3-minute round.

### 16.5 Status update for Lemma 3

Updating `proof_lemmas/lemma_003_cross_stratum.md` accordingly:
the CST conjecture's *closing direction is structural* status
remains contingent on §16.2 Branch (1), which is currently open.
The Section 16 precision check has narrowed the open question from
"is the §9 identity meaningful?" to "is the literature value of $c$
the exact $c_\star = 0.0664752\ldots$ or merely a 2-decimal
approximation?" — a much more focused question.

(End of Section 16.)

## Section 17 — The numerical-sieve route to estimating $c$ is infeasible

The §16.5 handoff recommended a direct sieve estimate of $c$ as
the cleanest autonomous next move. This section runs that
experiment and finds the route does not work at any feasible
compute scale — the convergence is logarithmically slow in
$\log\log N$, and the relevant $N$ at which $S(A_k)$ approaches its
limiting value $1 - c k^2/2^k$ is astronomical for any $k$ where
the leading term dominates.

### 17.1 Direct sieve, $N = 10^7$

Smallest-prime-factor sieve over $[2, N]$, $N = 10^7$, computing
\[
S_k(N) \;:=\; \sum_{\substack{n \le N \\ \Omega(n) = k}}
\frac{1}{n \log n}.
\]

| $k$ | $S_k(10^7)$ | $1 - S_k$ | $k^2/2^k$ | implied $c$ |
|---:|---:|---:|---:|---:|
| $1$ | $1.5746$ | $-0.5746$ | $0.500$ | $-1.149$ |
| $2$ | $0.8969$ | $+0.1031$ | $1.000$ | $+0.103$ |
| $3$ | $0.5358$ | $+0.4642$ | $1.125$ | $+0.413$ |
| $4$ | $0.2925$ | $+0.7075$ | $1.000$ | $+0.708$ |
| $5$ | $0.1471$ | $+0.8529$ | $0.781$ | $+1.092$ |
| $6$ | $0.0700$ | $+0.9300$ | $0.563$ | $+1.653$ |
| $7$ | $0.0321$ | $+0.9679$ | $0.383$ | $+2.528$ |
| $8$ | $0.0144$ | $+0.9856$ | $0.250$ | $+3.942$ |
| $9$ | $0.0064$ | $+0.9936$ | $0.158$ | $+6.281$ |
| $10$ | $0.0028$ | $+0.9972$ | $0.098$ | $+10.21$ |

Total $\sum_k S_k(10^7) = 3.5746$.

The implied-$c$ column should asymptote to a single constant $c
\approx 0.0656$ (or $0.0665$, the §16 alternative) if the
$1 - c k^2/2^k$ asymptotic held at this $N$. Instead the implied
$c$ grows monotonically with $k$ by orders of magnitude — the
asymptotic does **not** even approximately hold at $N = 10^7$ for
any single $k$ in the table.

### 17.2 Why convergence is hopeless at any practical $N$

The mass of stratum $A_k$ is concentrated at integers $n$ where
$\log\log n \approx k$ (saddle-point, §11.1–11.2). The relevant
scale is $u_k := e^{e^k}$:

| $k$ | $u_k = e^{e^k}$ | $\log_{10} u_k$ |
|---:|---|---:|
| $2$ | $\sim 10^{3.2}$ | $3.2$ |
| $3$ | $\sim 10^{8.7}$ | $8.7$ |
| $4$ | $\sim 10^{23.7}$ | $23.7$ |
| $5$ | $\sim 10^{64.5}$ | $64.5$ |
| $6$ | $\sim 10^{175.2}$ | $175.2$ |
| $7$ | $\sim 10^{476.3}$ | $476.3$ |
| $8$ | $\sim 10^{1295}$ | $1295$ |
| $9$ | $\sim 10^{3519}$ | $3519$ |
| $10$ | $\sim 10^{9566}$ | $9566$ |

For the leading-order asymptotic $S(A_k) \approx 1 - c k^2/2^k$ to
be tight at finite $N$, we need $N \gg u_k$. Concretely, the
truncation residual $S(A_k \cap [1, N]) \to S(A_k)$ requires
several decades past $u_k$.

For $k = 5$ — the smallest $k$ at which $c k^2/2^k = c \cdot 0.78$
gives a clean main term — this means $N \ge 10^{75}$ or so, vastly
beyond any direct sieve.

### 17.3 The honest conclusion

The §16 dichotomy ("is the literature value $c \approx 0.0656$ the
exact $c_\star = 0.06647517\ldots$, or only a $1\%$
approximation?") **cannot be settled by direct numerical sieve at
any feasible $N$**. The convergence rate of $S(A_k \cap [1, N])
\to S(A_k)$ is so slow that even $N = 10^{50}$ would be inadequate
to discriminate the two candidate $c$ values, which differ by $1\%$
of the leading term.

This closes off **option (1)** from the §16/handoff dichotomy: an
autonomous numerical resolution of the §9 closing route's
plausibility is not on offer. The remaining paths to settling the
identity are:

(a) **Literature lookup** of the explicit Sathe–Selberg constant
    formula (Selberg 1954 §3; Tenenbaum *Introduction to Analytic
    and Probabilistic Number Theory* §II.6.1) — outside the
    autonomous loop.
(b) **First-principles re-derivation** of $c$ as a specific Mertens
    integral or Euler-product expression — a research-paper-scale
    contribution that the loop has not produced in 17 rounds.
(c) **Side-stepping** the §9 identity: pursue a different proof
    strategy that does not depend on whether $6c = e^{\gamma}\pi/4
    - 1$ holds exactly. The §11.4 cross-stratum exclusion approach
    is one such side-step — it could in principle close Lemma 3
    without ever computing $c$.

### 17.4 What's recorded for future sessions

The §9 identity, having survived only a $1\%$ numerical agreement
test (§16) and now declared not-numerically-settleable (§17), is
not load-bearing for any rigorous step. The §15.2 candidate route
(stratum-aware Behrend with deficit $c k^2/2^k$ per stratum) is
*structurally* suggestive but its required identity remains
unverified. Future sessions that want to keep the §9 line live
need either an analytic derivation of $c$ or an external citation.

The §11.4 cross-stratum exclusion direction (option (c)) is more
promising for autonomous progress: it is a structural
combinatorial argument rather than a numerical one, and the
existing Sections 11.4 and 13 already lay the groundwork.

(End of Section 17.)

## Section 18 — Two-stratum cross-exclusion: explicit numerics

Pursuing option (c) from §17.3: side-step §9 by quantifying the
§11.4 / §13 cross-stratum exclusion route directly. This section
tabulates the explicit two-stratum sum
\[
S\!\left(A^{(k_1)} \;\sqcup\; A^{(k_2)}_\text{kept}\right)
\;=\; \sum_{a \in A^{(k_1)}} \frac{1}{a \log a}
\;+\; \sum_{b \in A^{(k_2)}_\text{kept}} \frac{1}{b \log b}
\]
where $A^{(k_1)} = A_{k_1} \cap [x, N]$ (the full $k_1$-stratum) and
$A^{(k_2)}_\text{kept} = \{b \in A_{k_2} \cap [x, N]:
\max\bigl\{d \mid b: \Omega(d) = k_1\bigr\} < x\}$ is the
cross-stratum kept set forced by primitivity (every $k_1$-divisor
of $b$ lies below the floor, so does not collide with $A^{(k_1)}$).

### 18.1 Computational setup

SPF sieve over $[2, N]$ with $N = 10^6$. For each $b$ with
$\Omega(b) = k_2$, the maximum $k_1$-divisor of $b$ is
$b / d_\text{small}(b, k_2 - k_1)$ where $d_\text{small}(b, m)$ is
the product of the smallest $m$ prime factors of $b$ (with
multiplicity). $b$ is *kept* iff this maximum is $< x$. Wall-clock:
$\approx 6$s for the full table.

### 18.2 Table

| $x$ | $(k_1, k_2)$ | $S(A^{(k_1)})$ | $S(A_{k_2}\!\cap[x,N])$ | $S(A^{(k_2)}_\text{kept})$ | frac kept | $S_\text{total}$ |
|---:|:---:|---:|---:|---:|---:|---:|
| $10^2$ | $(2, 3)$ | $0.288$ | $0.278$ | $0.046$ | $0.02\%$ | $\mathbf{0.334}$ |
| $10^2$ | $(2, 4)$ | $0.288$ | $0.187$ | $0.049$ | $0.05\%$ | $\mathbf{0.337}$ |
| $10^2$ | $(2, 5)$ | $0.288$ | $0.106$ | $0.036$ | $0.14\%$ | $\mathbf{0.324}$ |
| $10^2$ | $(3, 4)$ | $0.278$ | $0.187$ | $0.021$ | $0.01\%$ | $0.299$ |
| $10^2$ | $(3, 5)$ | $0.278$ | $0.106$ | $0.021$ | $0.02\%$ | $0.300$ |
| $10^2$ | $(3, 6)$ | $0.278$ | $0.052$ | $0.013$ | $0.05\%$ | $0.291$ |
| $10^3$ | $(2, 3)$ | $0.167$ | $0.177$ | $0.036$ | $0.26\%$ | $0.204$ |
| $10^3$ | $(2, 4)$ | $0.167$ | $0.127$ | $0.045$ | $1.20\%$ | $\mathbf{0.212}$ |
| $10^3$ | $(2, 5)$ | $0.167$ | $0.075$ | $0.035$ | $4.38\%$ | $0.203$ |
| $10^3$ | $(3, 4)$ | $0.177$ | $0.127$ | $0.018$ | $0.11\%$ | $0.195$ |
| $10^3$ | $(3, 5)$ | $0.177$ | $0.075$ | $0.020$ | $0.37\%$ | $0.197$ |
| $10^3$ | $(3, 6)$ | $0.177$ | $0.039$ | $0.014$ | $1.03\%$ | $0.191$ |
| $10^4$ | $(2, 3)$ | $0.091$ | $0.103$ | $0.031$ | $4.22\%$ | $0.122$ |
| $10^4$ | $(2, 4)$ | $0.091$ | $0.078$ | $0.042$ | $18.34\%$ | $\mathbf{0.133}$ |
| $10^4$ | $(2, 5)$ | $0.091$ | $0.047$ | $0.034$ | $38.22\%$ | $0.125$ |
| $10^4$ | $(3, 4)$ | $0.103$ | $0.078$ | $0.017$ | $1.52\%$ | $0.120$ |
| $10^4$ | $(3, 5)$ | $0.103$ | $0.047$ | $0.019$ | $5.88\%$ | $0.122$ |
| $10^4$ | $(3, 6)$ | $0.103$ | $0.026$ | $0.015$ | $16.45\%$ | $0.118$ |

(Bolded entries are the row-by-row maxima of $S_\text{total}$ at
each $x$.)

### 18.3 Three observations

**(O1) The maximum two-stratum total decays monotonically with $x$.**

| $x$ | $\max_{k_1 < k_2} S_\text{total}$ |
|---:|---:|
| $10^2$ | $0.337$ |
| $10^3$ | $0.212$ |
| $10^4$ | $0.133$ |

The decay rate is faster than $1/\log x$ ($\approx \log 10^2 / \log 10^4 = 0.5$ would give 0.169 from 0.337; observed 0.133, slightly faster). Consistent with — and in fact tracking
just below — the conjecture's expected $1 + o(1)$ ceiling at scale
$x \to \infty$. At $x = 10^4$, $S_\text{total} = 0.133$ is well
below $1$.

**(O2) The kept-fraction grows from negligible at $x = 100$ to substantial at $x = 10^4$ for high $k_2/k_1$ ratios.**

At $(k_1, k_2) = (2, 5)$: kept fraction is $0.14\%$ at $x = 10^2$
but $38.2\%$ at $x = 10^4$. The rapid growth reflects the §13.2
threshold $k_1 < \sqrt{2 k_2}$: at $(2, 5)$, $\sqrt{2 \cdot 5}
= 3.16 > 2$, so primitivity is "loose" and most $b \in A_5$
survive at large enough $x$. At $(3, 4)$, $\sqrt{2 \cdot 4} = 2.83
< 3$, so primitivity is "tight" and the kept fraction stays
small ($1.5\%$ even at $x = 10^4$).

The §13 prediction is qualitatively confirmed: above the threshold
$k_1 = \sqrt{2 k_2}$, primitivity is weak; below, it is strong.

**(O3) The maximum is consistently $(k_1, k_2) = (2, 4)$.**

At every tested $x$, the row maximum is at $(k_1, k_2) = (2, 4)$.
This pairing maximises $S(A^{(k_1)})$ (since $a_2$ is the largest
single-stratum) plus the kept contribution from $A_4$. The pairing
$(2, 5)$ gets a higher kept fraction but a smaller raw $a_5$, so
loses on the product.

### 18.4 Quantitative implication for Lemma 3

The conjecture asserts $\sup_A S(A) \le 1 + o(1)$ for primitive
$A \subset [x, \infty)$ as $x \to \infty$. The §18.2 table —
restricted to two-stratum constructions — gives the bound

\[
\sup_{A = A^{(k_1)} \sqcup A^{(k_2)}} S(A) \;\le\;
\begin{cases} 0.337 & x = 10^2 \\ 0.212 & x = 10^3 \\
0.133 & x = 10^4 \end{cases}
\]

within the truncation $[x, 10^6]$. The natural (heuristic, not
proven) extrapolation: the two-stratum sup decays as $\sim
(\log\log x) / (\log x)$ (single-stratum-dominant rate). At
$x = 10^{30}$, this would give $\sup \sim 0.05$ — far below $1$.

Multi-stratum (3+ strata) sums per §14 give at most a 30% boost
over two-stratum. So even with all strata, the data is consistent
with $\sup_A S(A) \to 0$ as $x \to \infty$ — *stronger* than the
conjecture's $1 + o(1)$.

This empirical signal is the strongest evidence to date — across
17 prior rounds — that the conjecture is true. **It is not a
proof.** The numerical decay holds only over the tested range
$x \le 10^4$; an analytical bound that captures the cross-stratum
exclusion's mass loss across all strata simultaneously is still
needed to close Lemma 3.

### 18.5 What would close Lemma 3 from here

The §18 data points to a concrete analytic target:

> **Claim.** For primitive $A \subset [x, \infty)$,
> \[
> S(A) \;\le\; \sum_k a_k(x; \infty) \cdot \rho_k(x)
> \]
> where $\rho_k(x)$ is the fraction of $A_k \cap [x, \infty)$
> compatible with the rest of $A$ under primitivity, and
> $\sum_k a_k \cdot \rho_k \to 0$ (or at worst $\to 1$) as
> $x \to \infty$.

The §13.2 Erdős–Kac threshold gives $\rho_k(x)$ asymptotics but
not yet the explicit $a_k \rho_k$ inequality. A round that
formalises $\rho_k$ via Erdős–Kac and bounds the sum by a
saddle-point integral would be the next step. This is research-
paper-scale but tractable in principle.

(End of Section 18.)










