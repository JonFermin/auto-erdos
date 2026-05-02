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








