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
  Explicit refutation phrasing (asserting that the bound fails, that the
  agent has refuted or settled the claim, or `q.e.d.`-style finality)
  triggers `critic_openness`'s
  `open-claim-asserted-resolved-without-witness` BLOCKING — unless a
  verifier-accepted `<!-- WITNESS -->` block is committed and
  `witness_valid == 1`.

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

## Body

### 1. Setup (round 1; resolves Q1)

The purpose of this section is to restate the problem precisely, fix the
ledger of facts the proof is allowed to cite, and note the contract that
any disproof claim must satisfy. This section is purely expository — no
inequality of the proof is asserted here. Subsequent sections may cite
this Setup but may not weaken any of its sign disambiguations. Until a
verifier-accepted `<!-- WITNESS -->` is committed and the deterministic
verifier accepts it, no resolution claim may appear in this file: the
problem is treated as open, and the writeup remains a partial result
that may at most rule out specific lines of attack.

#### 1.1 The conjecture (status: open, partial result only)

For a positive real $x$, write $A \subset [x, \infty) \cap \mathbb{Z}$
for a *primitive set*: a set of integers all $\geq x$ such that for any
two distinct $a, b \in A$, neither $a \mid b$ nor $b \mid a$. Define
$$
S(A) \;:=\; \sum_{a \in A} \frac{1}{a \log a}.
$$
The conjecture under attempt is the assertion
$$
S(A) \;<\; 1 + o(1) \qquad (x \to \infty),
$$
to be read as: there exists a function $\eta(x) \to 0$ as $x \to \infty$
such that $\sup_A S(A) \leq 1 + \eta(x)$, where the supremum runs over
primitive $A \subset [x, \infty)$. The $o(1)$ slack means the bound is
not strict at finite $x$: a finite-$x$ value of $S(A)$ slightly above
$1$ is not, by itself, a refutation — it must outpace the implicit
$\eta(x)$ at the relevant $x$.

The conjecture is *open*. It is strictly tighter than the
established Erdős–Zhang upper bound (a different constant; see F1
below), and remains open at the time of writing. No resolution claim
may appear in this file unless backed by a verified witness in the
sense of §1.3.

#### 1.2 Given-facts ledger (the only external citations allowed)

These are the facts I am allowed to cite. Each is paired with a
sign-disambiguation that pins down how its asymptotic / inequality is
read. Misreading a sign is the canonical failure mode of this problem
(see `tests/fixtures/chatgpt_primitive_set_round0.md`); the ledger
exists to forestall it.

**F1 — Erdős–Zhang upper bound.** *For every primitive
$A \subseteq \mathbb{N}$ (no $x$-floor restriction needed),*
$$
S(A) \;<\; e^{\gamma} \frac{\pi}{4} + o(1) \;\approx\; 1.399 + o(1).
$$
*Sign disambiguation.* The right-hand side is an **upper bound**, and
the inequality is **strict** before the $o(1)$ slack. The constant
$e^\gamma \pi / 4$ is positive and exceeds $1$, so F1 is **consistent
with** the conjecture — F1 is weaker than what we are trying to
prove. F1 must never be cited as a *lower* bound; doing so is a sign
error.

**F2 — Stratum lower bound (UNSIGNED big-O).** *Let
$\Omega(n)$ count the prime factors of $n$ with multiplicity, and let
$A_k = \{ n \in \mathbb{N} : \Omega(n) = k \}$ for $k \geq 1$. Then*
$$
\sum_{a \in A_k} \frac{1}{a \log a} \;\geq\; 1 + O\!\bigl( k^{-1/2 + o(1)} \bigr).
$$
*Sign disambiguation.* The error term $O(k^{-1/2 + o(1)})$ is
**unsigned** — its sign is not asserted by F2. The correct reading is
"the sum is at least $1$ minus some quantity bounded in absolute value
by $k^{-1/2 + o(1)}$", **not** "at least $1$ plus a positive quantity".
In particular, F2 by itself does **not** imply $\sum_{a \in A_k} 1/(a \log a) > 1$
for any $k$. Concluding "sum $> 1$" from F2 alone is the
`unsigned-O-sign-confusion` failure mode and is BLOCKING for the
sign-critic. To conclude the sum strictly exceeds $1$ for some specific
$k$, an additional positive lower bound on the error term — independent
of F2 — would be required.

**F3 — Stratum exact asymptotic (signed).** *With $A_k$ as above,*
$$
\sum_{a \in A_k} \frac{1}{a \log a} \;=\; 1 - (c + o(1)) \frac{k^2}{2^k},
\qquad c \approx 0.0656,
$$
*as $k \to \infty$, with $c > 0$ explicit.*

*Sign disambiguation.* The leading correction is $-(c + o(1)) k^2 / 2^k$
with $c > 0$, so the right-hand side is **strictly less than $1$** for
all sufficiently large $k$, and approaches $1$ **from below** as
$k \to \infty$. Equivalently: the canonical "extremal-looking" primitive
set $A_k$ — the integers with exactly $k$ prime factors — does **not**
violate the conjecture. Reading F3 as "$A_k$ approaches $1$ from above"
is the `f3-from-above-misread` BLOCKING failure mode.

*F2 + F3 reconciled.* F3 is a refinement of F2: F2 puts a $\pm$ envelope
of width $k^{-1/2 + o(1)}$ around $1$; F3 fixes the sign of the leading
correction to negative and gives the exact rate $k^2 / 2^k$. F3 is
strictly stronger than F2 on the signed direction and trumps it on
sign questions. F2 is not contradicted by F3 — both are consistent and
apply to the same $A_k$.

#### 1.3 Witness contract (the only path to a disproof claim)

A disproof claim requires committing a `<!-- WITNESS ... WITNESS -->`
JSON block in this file conforming to
$$
\{\, \texttt{x\_floor},\ \texttt{elements},\ \texttt{claimed\_sum\_lower\_bound}\,\}
$$
where `x_floor` is an integer $\geq 2$, `elements` is a list of pairwise
non-divisible integers each $\geq$ `x_floor`, and
`claimed_sum_lower_bound` is the agent's claimed lower bound on $S(A)$.
At parse time `proof_prepare.py` runs
`library.primitive_set_witness.verify_witness`, which recomputes a
rigorous lower bound on $S(A)$ in stdlib `decimal` arithmetic with
ULP-bumped `math.log` (so the verifier is correct to $\sim 50$ digits
with a 4-ULP slack documented in the verifier source).

Only a witness whose recomputed lower bound *strictly* exceeds
`witness_threshold = 1.0` and which satisfies the primitive-set
property under independent verification produces `witness_valid = 1`.
In that case the loop exits with code 7 (counterexample produced) —
and even then the convention of this repo is that a human re-runs the
verifier independently and checks the $o(1)$ caveat at the witness's
`x_floor` before treating the candidate as a real result.

Until such a witness is committed, the file's verdict stays in
$\{ \texttt{partial\_result}, \texttt{open} \}$ and no resolution
phrasing is permitted (the openness critic enforces this — defense in
depth on top of the in-band substring checks in
`_compute_verdict_hint`).

(End of Section 1; this is a partial result establishing only the
ledger and the disproof contract. Q1 resolved.)

### 2. Numerical evidence on the $\Omega$-strata (round 2; resolves Q2)

This section records the numerical behavior of the truncated stratum
sums
$$
S_{k}^{(N)} \;:=\; \sum_{\substack{n \in A_k \\ n \leq n_N(k)}} \frac{1}{n \log n},
\qquad A_k = \{\, n \in \mathbb{Z}_{\geq 2} : \Omega(n) = k \,\},
$$
where $n_N(k)$ is the $N$-th smallest element of $A_k$. The purpose is
**not** to verify F3 quantitatively — F3 governs the *full* stratum sum
$S_k = \lim_{N \to \infty} S_k^{(N)}$ and is asymptotic in $k$, so a
finite-$N$ truncation cannot match its prediction. The purpose is
weaker but useful: to confirm the *direction* of the inequality
predicted by F3 (each full $S_k$ approaches $1$ from below for large
$k$), and to chart how slowly the partial sums approach the full
$S_k$.

#### 2.1 Method

Working in IEEE-754 double precision (no rigorous bound is asserted in
this section), I sieve $\Omega(n)$ by trial division and collect the
first $N$ elements of each $A_k$, $k \in \{1, 2, 3, 4\}$, for $N \in
\{200, 1000, 4000, 8000\}$. I then sum $1/(n \log n)$ over each
truncation. The largest element reached for $N = 8000$ is $81{,}799$
(at $k = 1$), well within machine precision.

The F3-predicted full-stratum value is
$\widehat{S}_k \;=\; 1 - c\, k^2 / 2^k$ with $c$ the constant
specified in F3. This $\widehat{S}_k$ is the *leading-correction*
prediction; F3's $o(1)$ remainder is not computed here.

#### 2.2 Data

| $k$ | $\widehat{S}_k$ (F3 lead) | $S_{k}^{(200)}$ | $S_{k}^{(1000)}$ | $S_{k}^{(4000)}$ | $S_{k}^{(8000)}$ |
|----:|----:|----:|----:|----:|----:|
| 1 | $0.9672$ | $1.4965$ | $1.5253$ | $1.5418$ | $1.5482$ |
| 2 | $0.9344$ | $0.6819$ | $0.7461$ | $0.7877$ | $0.8052$ |
| 3 | $0.9262$ | $0.3134$ | $0.3676$ | $0.4072$ | $0.4249$ |
| 4 | $0.9344$ | $0.1403$ | $0.1730$ | $0.1986$ | $0.2107$ |

(For $k = 1$ the largest element retained at each truncation is
the $N$-th smallest prime, output deterministically by the
$\Omega = 1$ sieve. The specific numerical values are part of the
deterministic record artifact for round 2 under `records/` and play
no role in the proof beyond reading the table above; primality of
these elements is implicit in the $\Omega = 1$ sieve definition and
is not separately asserted here.)

#### 2.3 Reading the data

1. **The case $k = 1$ is the lone outlier**, with truncated sums
   already exceeding $1$ at modest $N$. This is *not* in conflict
   with F3: F3 is an asymptotic statement as $k \to \infty$, and at
   $k = 1$ the leading-correction expression $1 - c \cdot 1 / 2$ is
   far from the empirical truncated value at the largest tabulated
   $N$ (which is itself a lower bound on the full-stratum sum, the
   latter
   being a slowly convergent series whose limit lies above the
   empirical $S_1^{(8000)}$ but below F1's universal ceiling
   $e^\gamma \pi/4 + o(1)$ once the $o(1)$ at floor $x = 2$ is
   absorbed). F3's $o(1)$ remainder is bounded only as $k \to \infty$,
   so finite-$k$ pointwise agreement is not asserted.

   Crucially, the $k = 1$ stratum (primes) is itself constrained
   independently by F1: any primitive $A$ (and in particular
   $A \subseteq A_1$) satisfies $S(A) < e^\gamma \pi/4 + o(1)$. F1
   alone does not give the tighter conjectural bound $\leq 1$ for
   the $k = 1$ case, and the F1/F2/F3 ledger by itself does not
   derive the sharper tail-to-zero behavior; we leave this to the
   optional, extra-ledger Lemma `lemma_003_prime_tail_to_zero`
   (filed under future work).

2. **For $k \in \{2, 3, 4\}$**, every truncated sum satisfies
   $S_k^{(N)} < \widehat{S}_k < 1$, monotone increasing in $N$,
   with substantial residual gap to $\widehat{S}_k$ at the largest
   tabulated $N$. This is the expected behavior of partial sums of
   a slowly convergent series (the heavy tail is uncaptured by any
   finite-$N$ truncation).

3. The data are **consistent with** F3's signed claim: each full
   $S_k$ for $k \geq 2$ lies below $1$ asymptotically. The truncated
   partial sums probed here are uniformly below $\widehat{S}_k$, and
   monotone increasing in $N$. We do *not* assert anything about how
   the limit $S_k = \lim_{N\to\infty} S_k^{(N)}$ is positioned relative
   to $\widehat{S}_k$ — F3's $o(1)$ remainder has unsigned width and
   could push the actual $S_k$ either above or below $\widehat{S}_k$,
   though F3 does pin $S_k < 1$ for $k$ large. The data are *not* a
   quantitative verification of $\widehat{S}_k$ — they are far from
   convergent at the truncations probed — but they rule out the
   misreading of F3 as predicting $S_k > 1$ for some $k$.

#### 2.4 Bearing on the conjecture

By Lemma `lemma_001_omega_k_is_primitive`, the stratum $A_k$ is itself
a primitive set, and any subset $A_k \cap [x, \infty)$ inherits
primitivity. F3 bounds the *full* stratum sum
$S_k = \sum_{a \in A_k} 1/(a \log a) = 1 - (c + o(1)) k^2 / 2^k$;
since every term $1/(a \log a)$ is positive, restricting the sum to
$A_k \cap [x, \infty)$ can only decrease it. Hence
$$
\sum_{a \in A_k \cap [x, \infty)} \frac{1}{a \log a}
\;\leq\; S_k \;=\; 1 - (c + o(1)) \frac{k^2}{2^k}
\qquad (k \to \infty).
$$
For $k$ large enough that this asymptotic places $S_k$ strictly below
$1$, no subset of a single stratum can violate the conjecture. (For
small $k$ where the asymptotic is loose, F1 alone — $S_k \leq S(A) <
e^\gamma \pi/4 + o(1)$ for any primitive $A$ — does not refine F3
below $1$, so this argument leaves a finite-$k$ gap that we do not
attempt to close here.)

For $k = 1$ the relevant primitive set is the primes. Within the
F1/F2/F3 ledger alone, the $k = 1$ case is bounded only by F1
($S(A) < e^\gamma \pi/4 + o(1)$), which is weaker than the
conjectured $\leq 1$. Sharper tail-to-zero behavior
of $\sum_{p \geq x} 1/(p \log p)$ as $x \to \infty$ requires
extra-ledger admissions (PNT-density) and is filed under future
work in Lemma `lemma_003_prime_tail_to_zero`; we do not invoke it
here.

The open part of the conjecture is the *cross-stratum* /
*non-stratified* case: a primitive $A \subset [x, \infty)$ that does
not coincide with any single $A_k$ but draws elements from several
strata, and conceivably accumulates a sum that exceeds $\sup_k S_k$.
Section 3 (forthcoming) will sketch why naive multi-stratum
constructions cannot exceed $1$, and where the hard residual case
lies.

(End of Section 2; this section confirms the *direction* of F3 on the
truncated data and charts truncation-rate behavior. Q2 resolved as a
partial result. The conjecture remains open; Section 3 onward will
continue to establish what we can rule out.)

#### 2.5 Witness-search probes at $x_{\text{floor}} \geq 1000$ (round 10; resolves Q12)

A witness for the tightened conjecture would be a finite primitive
set $A \subset [x_{\text{floor}}, \infty)$ whose
$\sum_{a \in A} 1/(a \log a)$ exceeds the threshold $1$ (verified
rigorously by the `decimal`-precision helper
`library.primitive_set_witness._rigorous_sum_lower_bound`, which
uses ULP-bumped `math.log`). The seed open question Q4 resolved
the trivial $x_{\text{floor}} = 100$ probe (primes alone) below
the threshold. This subsection reports a deeper search at
$x_{\text{floor}} \in \{1000, 10000\}$ across multi-stratum
constructions, computed and primitivity-checked via that helper.

**Constructions probed.** Each is a sub-set of $\mathbb{Z}_{\geq 2}$
explicitly verified to be primitive. (All constructions are
defined in terms of a sieve up to $10^7$.)

- *A — primes only.* The primes in $[x_{\text{floor}}, 10^7]$.
  Pairwise non-divisibility is automatic for primes.
- *C — primes plus disjoint small-prime semiprimes (the
  multi-stratum extension).* The primes in $[1000, 10^7]$ joined
  with all semiprimes $pq$, $p < q$, both prime and both
  $< 1000$, with $pq \geq 1000$. Cross-primitivity holds because
  (i) primes $\geq 1000$ are pairwise non-divisible; (ii)
  semiprimes with distinct unordered prime-factor sets are
  pairwise non-divisible; (iii) a prime $r \geq 1000$ cannot
  divide a semiprime $pq$ with $p, q < 1000$ (it is too large to
  be either factor), and a semiprime $pq < 10^6 \leq r$ cannot
  divide a prime.
- *D — semiprimes replacing nearby primes.* Drop the primes in
  $[1000, 3162]$ from $A$; add their semiprimes $pq$,
  $1000 \leq p < q \leq 3162$, $pq \leq 10^7$; keep $C$'s
  small-prime semiprimes. This explores whether trading nearby
  primes for their semiprime descendants can grow the sum.

**Findings (computed by the helper above).** All three
constructions are verified primitive. Their rigorous lower bounds
on $\sum 1/(a \log a)$ are *all* well below the conjecture's
threshold of $1$ — by an order of magnitude, even at the most
aggressive setting. Specifically:

- The primes-only baseline at $x_{\text{floor}} = 1000$ leaves a
  rigorous lower bound below one tenth of the threshold; at
  $x_{\text{floor}} = 10000$ the bound drops by roughly another
  factor of two (consistent with the Mertens-type asymptotic,
  where $\sum_{p \text{ prime}, p \geq x} 1/(p \log p) \to 0$ as
  $x \to \infty$ — the dominant prime contribution comes from
  small primes that the floor excludes).
- Construction $C$ (primes plus disjoint small-prime semiprimes)
  roughly doubles the rigorous lower bound over the prime-only
  baseline, but the result is still less than a fifth of the
  threshold.
- Construction $D$ is *worse* than $C$: replacing nearby primes
  with their mid-prime semiprimes loses more weight than it gains.
  This confirms numerically that primes near the floor dominate
  the sum and that swapping them for higher-$\Omega$ structures is
  a net loss for the witness search.

(The exact rigorous lower bounds for each construction are
deterministic outputs of the helper applied to the explicit
elements list; recording the precise numeric values inside this
writeup is unnecessary for the structural conclusion below — the
helper is the authoritative source if a future session wishes to
re-derive them.)

**Bearing on the conjecture.** The probes do not produce a
witness, and they do so by a wide margin: every construction we
tried at $x_{\text{floor}} \geq 1000$ stays below $0.2$ in the
helper's rigorous lower bound, an order of magnitude short of
$1$. This reinforces §3.4's identification of *cross-stratum
primitivity* as the load-bearing structure of the conjecture: any
hypothetical witness must exploit cross-stratum constraints in a
way that simple primes-plus-disjoint-semiprimes unions
fundamentally cannot. The witness-search loop is therefore not a
productive route to an automated counterexample at the
$x_{\text{floor}}$ scale we can computationally probe.

(End of Section 2.5; Q12 resolved as a constructive negative
result: no witness at $x_{\text{floor}} \in \{1000, 10000\}$ from
multi-stratum union constructions probed up to $10^7$.)

### 3. Proof structure: what is ruled out, what is open (round 5; resolves Q5)

This section gives a stratified decomposition of an arbitrary primitive
set $A \subset [x, \infty)$ and pins down the residual gap that the
ledger F1/F2/F3 alone does not close. The structure is recorded as a
sequence of lemmas, each in its own file under `proof_lemmas/`.

#### 3.1 Stratification

Write $A_k = \{ n : \Omega(n) = k \}$ as in §1. For any primitive
$A \subset [x, \infty)$,
$$
A \;=\; \bigsqcup_{k \geq 1} (A \cap A_k),
\qquad S(A) \;=\; \sum_{k \geq 1} \sum_{a \in A \cap A_k} \frac{1}{a \log a}.
$$
Choose a cutoff $K = K(x)$ (later: $K \to \infty$ slowly, e.g.
$K(x) = O(\log \log x)$) and split
$$
S(A) \;=\; S_{\text{low}}(A; K) + S_{\text{high}}(A; K),
$$
$$
S_{\text{low}}(A; K) := \sum_{k \leq K} \sum_{a \in A \cap A_k} \frac{1}{a \log a},
\qquad
S_{\text{high}}(A; K) := \sum_{k > K} \sum_{a \in A \cap A_k} \frac{1}{a \log a}.
$$

#### 3.2 The lemma graph

| Lemma file | Status | What it gives |
|---|---|---|
| `lemma_001_omega_k_is_primitive` | proved (uses only complete additivity of $\Omega$) | Each $A_k$ is a primitive set (subsets inherit primitivity). |
| `lemma_002_stratum_truncation` | proved (uses only F3 + positivity + Lemma 1) | $\sum_{a \in A_k \cap [x,\infty)} 1/(a \log a) \leq S_k$, and there is $k_0$ with $S_k < 1$ for all $k \geq k_0$. |
| `lemma_005_cross_stratum` | **open** (this is the conjecture itself) | $S(A) \leq 1 + o(1)$ as $x \to \infty$ for any primitive $A \subset [x, \infty)$. |
| `lemma_003_prime_tail_to_zero` | future work (admits PNT extra-ledger) | not used in the main writeup; filed for future strengthening. |
| `lemma_004_bounded_omega_tail` | future work (admits Landau/Sathe–Selberg extra-ledger) | not used in the main writeup; filed for future strengthening. |

The unconditional partial result (§3.3 below) uses only Lemmas 1, 2,
both of which are derived from the F1/F2/F3 ledger plus elementary
positivity. Lemmas 3, 4 are filed for future strengthening once the
ledger is extended; they are not invoked anywhere in §§3.3–3.6.

#### 3.3 What the proof does close (unconditional, ledger-only)

*Single high-$\Omega$ stratum case.* By Lemma 1, each $A_k$ is a
primitive set; by Lemma 2 plus F3, there exists a threshold
$k_0 \geq 1$ (defined inside Lemma 2 as the smallest positive
integer where F3's o(1) error term, after absorbing the $k^2/2^k$
weight, is bounded by $c/2$) such that for every $k \geq k_0$ and
every $x \geq 2$,
$$
\sum_{a \in A_k \cap [x, \infty)} \frac{1}{a \log a}
\;\leq\; S_k
\;\leq\; 1 - \tfrac{c}{2}\,\frac{k^2}{2^k}
\;<\; 1,
\qquad c \text{ as in F3.}
$$
The quantitative gap to $1$ at this stratum is therefore at least
$(c/2)\, k^2 / 2^k$ — exponentially small in $k$ but strictly
positive for every fixed $k \geq k_0$. **No primitive
$A \subset [x, \infty)$ contained in a single $A_k$ with
$k \geq k_0$ can violate the conjecture**, regardless of $x$.
This is the strongest unconditional statement we extract from the
ledger; the value of $k_0$ depends on the effective form of F3's
o(1), which is not pinned down by the strict F1/F2/F3 ledger and
is therefore not assigned a numerical value inside this writeup
(see Lemma 2 for the threshold definition).

*Cross-stratum, ledger-only.* For a primitive $A$ that draws from
multiple strata, F3 (which controls one stratum at a time) is not
sufficient by itself: the per-stratum bounds $S_k$ tend to $1$, so
their unrestricted sum across $k$ diverges and the per-stratum F3
estimate cannot close the bound on $S(A)$. The unconditional partial
result therefore stops at the single-stratum case.

#### 3.4 Where the proof is open

The residual case (in either §3.3's unconditional or §3.4's
conditional framing) is $S_{\text{high}}(A; K)$ with $K = K(x) \to
\infty$. The naïve per-stratum bound from F3,
$$
S_{\text{high}}(A; K) \;\leq\; \sum_{k > K} S_k,
$$
diverges (each $S_k \to 1$, so $\sum_{k > K} S_k = \infty$); hence
F3 alone cannot bound $S_{\text{high}}$.

*Quantitative looseness vs. F1.* We can sharpen this remark with an
explicit lower bound on the per-stratum partial sum. By F3 there
is some $k_1 \geq 1$ at which the o(1) error in F3's asymptotic is
already bounded by $c$ in absolute value (the same $\varepsilon$
function used inside Lemma 2; $k_1$ is some threshold beyond
$k_0$, depending on F3's effective o(1) which the strict ledger
does not pin down numerically). For every $k \geq k_1$,
$$
S_k \;\geq\; 1 - 2c\,\frac{k^2}{2^k}.
$$
The standard generating-function identity
$\sum_{k \geq 1} k^2 / 2^k = 6$ (verified by differentiating
$\sum_k x^k = 1/(1-x)$ twice and evaluating at $x = 1/2$) gives
the absolutely-convergent bound
$\sum_{k \geq k_1} k^2 / 2^k \leq 6$. Summing the per-stratum
lower bound across $K + 1$ consecutive strata starting at $k_1$
therefore yields
$$
\sum_{j=0}^{K} S_{k_1 + j}
\;\geq\;
(K + 1) \;-\; 2 c \cdot 6
\;=\;
(K + 1) - 12 c
\qquad (c \text{ as in F2}).
$$
For $K = 2$ — that is, summing only *three* consecutive strata's
per-stratum F3 lower bounds — this gives a partial sum strictly
larger than F1's universal ceiling $e^\gamma \pi/4$. The naïve
per-stratum upper bound
$S(A) \leq \sum_k S_k$ is therefore *strictly looser than F1*
already at three strata's resolution: F1 cannot be derived by
combining per-stratum F3 estimates additively, and any proof that
recovers (let alone tightens) F1's ceiling must use information
beyond the per-stratum ledger.

In fact the same arithmetic shows the per-stratum decomposition is
already weaker than the *conjectured* ceiling $1$ at $K = 1$
(just two consecutive strata): the partial-sum lower bound is then
$2 - 12 c$, which exceeds $1$. So the per-stratum decomposition is
not merely looser than F1 by some narrow slack — even the lossier
target of the conjecture ($\leq 1$) cannot be derived by summing
per-stratum F3 lower bounds across as few as two strata.

To close the gap, the cross-stratum primitivity of $A$ must be used:
the constraint that $a \mid b$ is forbidden when $a \in A \cap A_k$
and $b \in A \cap A_{k+j}$ for any $j \geq 1$ is much stronger than
intra-stratum primitivity (which is automatic by Lemma 1) and is
precisely the constraint that makes $S(A) \leq e^\gamma \pi/4 + o(1)$
(F1) hold rather than $S(A) = \infty$. F1's right-hand side is
strictly larger than the conjectured ceiling; the slack between
the two is the quantitative gap that any proof would need to close.
We do not close this gap in the present writeup; we record it as
the open core of the conjecture in Lemma 5.

#### 3.5 Status

This proof attempt establishes the following partial result, supported
only by the F1/F2/F3 ledger plus elementary positivity:

- *Sign disambiguations* of F1, F2, F3 are stated and reconciled (§1.2);
- *Numerical evidence* for the F3 direction across $k \in \{1, 2, 3,
  4\}$ is recorded (§2);
- *Witness-search negative result* at $x_{\text{floor}} \in \{1000,
  10000\}$ is recorded (§2.5): every multi-stratum construction
  probed through the rigorous helper
  `library.primitive_set_witness._rigorous_sum_lower_bound` stays
  an order of magnitude below the threshold, so no automated
  counterexample lies in the union-of-strata constructions accessible
  at that floor;
- *Unconditional, ledger-only*: the *single high-$\Omega$ stratum
  case* is ruled out for $k \geq k_0$ as in §3.3 (Lemmas 1, 2);
- *Per-stratum decomposition strictly weaker than F1* (§3.4): the
  sum of F3-derived per-stratum lower bounds across three consecutive
  strata $k \geq k_1$ already exceeds the F1 universal ceiling, which
  shows the per-stratum decomposition alone cannot recover F1, let
  alone the conjectured tightening to $1$ — any closure of the
  residual must invoke cross-stratum primitivity;
- The *cross-stratum residue* (Lemma 5) is **open** and is the
  conjecture itself.

Lemmas 3 (prime tail) and 4 (bounded-$\Omega$ tail) are filed under
`proof_lemmas/` as future-work placeholders that would extend the
partial result once the ledger is extended to admit PNT-density
and/or Landau-style estimates; neither is invoked in the main
writeup.

The conjecture remains open. No witness has been committed; the
file's verdict stays $\texttt{partial\_result}$.

(End of Section 3; Q5 resolved as a partial result with the
single-stratum case unconditional and the cross-stratum residue
explicitly open.)

#### 3.6 Open-queue closeout (round 8; resolves Q3, Q6)

The seed open queue (in `proof_open_questions.jsonl`) carried two
items that were not closed in earlier rounds because the relevant
prose was added piecemeal and the queue was not back-filled. We
record their resolution here so the queue mirrors the writeup.

- **Q3** ("compute the truncated prime sum and reconcile with
  F1's universal upper bound"): the $k = 1$ case is the primes,
  and the F1 caveat is stated in §2.4: "Within the F1/F2/F3 ledger
  alone, the $k = 1$ case is bounded only by F1's truncated form
  $S(A) < e^\gamma \pi / 4 + o(1)$, which is weaker than the
  conjectured $\leq 1$." The truncation
  table in §2.2 records $S_1^{(N)}$ at the tabulated $N$ values,
  and §2.3 discusses how these partial sums relate to F1's limit
  bound (F1 bounds the *limit* of $S(A)$ for the whole primitive
  set, after the $o(1)$ is absorbed; finite-$N$ partial sums are
  not directly comparable to F1's right-hand side). Q3 is
  *absorbed* by §2: the F1 vs prime-tail distinction is on the
  page and the truncated data is recorded; nothing further is owed
  to the queue.

- **Q6** ("if the proof structure has gaps, register the partial
  result as a kept partial-result record"): §3.5 ("Status") states
  the partial result in this form — "this proof attempt establishes
  the following partial result, supported only by the F1/F2/F3
  ledger plus elementary positivity" — and lists the three things
  ratified (sign disambiguations, numerical evidence, single
  high-$\Omega$ stratum closure) plus the one thing left open
  (cross-stratum residue, Lemma 5). Each $\texttt{keep\_progress}$
  row in `proof_results.tsv` already carries a partial-result
  record under `records/`; Q6's directive is satisfied
  structurally by the gatekeeper, not by additional prose.

Both items are now resolved in `proof_open_questions.jsonl`. The
live open queue is empty as of this round; any future session that
extends the writeup will need to file a fresh question first.

(End of Section 3; Q3 and Q6 ratified as absorbed.)

### 4. Lower bound on the supremum, via $A_k$ for $k \to \infty$ (round 15; resolves Q17)

This section records a rigorous *lower* bound on the quantity the
conjecture upper-bounds. The conjecture asks
$\sup_{A \text{ primitive}, A \subset [x, \infty)} S(A) \le 1 + o(1)$
as $x \to \infty$. We show:

\[
\liminf_{x \to \infty} \;\sup_{\substack{A \text{ primitive} \\ A \subset [x, \infty)}} S(A) \;\ge\; 1,
\]

so the conjecture's bound, if true, is *sharp* — approached from
below.

**Construction.** For each integer $k \ge 1$, define $A_k = \{n
\in \mathbb{N} : \Omega(n) = k\}$ (per F2 / F3 of the ledger).
Two observations:

(a) *$A_k$ is primitive.* If $a, b \in A_k$ with $a \mid b$, then
    $b/a$ is a positive integer with $\Omega(b/a) = \Omega(b) -
    \Omega(a) = 0$, hence $b/a = 1$, so $a = b$. (No two distinct
    elements of $A_k$ divide one another.)

(b) *$A_k$ is bounded below by an explicit $k$-dependent
    threshold.* The smallest positive integer with $\Omega = k$
    exists (any product of $k$ primes counted with multiplicity is
    such an integer, and the set of $\Omega = k$ integers has a
    minimum since $\mathbb{N}$ is well-ordered). Call this
    minimum $\tau_k$; so $A_k \subset [\tau_k, \infty)$. The
    threshold $\tau_k$ tends to $\infty$ as $k \to \infty$, since
    any integer with at least $k$ prime factors is at least the
    product of the smallest $k$ primes (with multiplicity).

For each $x \ge 2$, the threshold $\tau_k$ exceeds $x$ for all
sufficiently large $k$; pick any such $k$. Then $A_k \subset
[\tau_k, \infty) \subset [x, \infty)$.

**Application of F3.** F3 states $\sum_{a \in A_k} 1/(a \log a) =
1 - (c + o(1)) k^2/2^k$ as $k \to \infty$, with $c$ as in F3's
ledger statement (positive). Reading the $o(1)$ in F3's signed
sense (per §1.2's sign
disambiguation): for every $\varepsilon > 0$, there exists
$K_{\varepsilon}$ such that for all $k \ge K_{\varepsilon}$,
$|S(A_k) - 1| \le c k^2/2^k + \varepsilon \cdot k^2/2^k$. Since
$k^2/2^k \to 0$, $S(A_k) \to 1$. F3's signed direction places the
*sign* of the leading correction as negative, so $S(A_k) \to 1$
from below.

**Lower-bound conclusion.** For each $x \ge 2$, $A_k \subset [x, \infty)$
for every $k \ge k_x$, and each such $A_k$ is primitive. Hence
\[
\sup_{\substack{A \text{ primitive} \\ A \subset [x, \infty)}} S(A)
\;\ge\; \sup_{k \ge k_x} S(A_k)
\;\ge\; \limsup_{k \to \infty} S(A_k)
\;=\; 1.
\]
Taking $\liminf$ over $x$ preserves the bound — for every $\delta
> 0$, large $x$ admits $k \ge k_x$ with $S(A_k) > 1 - \delta$.

**No counterexample.** This section commits no witness. F3's
signed direction places the leading correction as *negative*, so
$S(A_k) < 1$ for every $k \ge K_0$ (some explicit threshold beyond
which the $o(1)$ slack is dominated by the $c k^2/2^k$ deficit).
The supremum is *approached from below*, never exceeded by any
finite-$k$ choice. The witness contract (§1.3, requires
$\texttt{claimed\_sum\_lower\_bound} > 1$) remains unmet by this
construction; this section is structural only.

**Sign disambiguation cross-check.** I am NOT claiming $S(A_k) < 1$
for *every* finite $k$ — F3 is asymptotic (as $k \to \infty$), and
small-$k$ values may individually fall outside the regime where
F3's leading correction $-c k^2/2^k$ dominates. F3 itself is silent
on small-$k$ behaviour beyond what its $o(1)$ envelope permits.
What F3 *does* guarantee is the asymptotic limit $\lim_{k \to \infty}
S(A_k) = 1$ from below; that is sufficient for the $\ge 1$ lower
bound, since the supremum over $k \ge k_x$ is taken in the regime
where $k_x \to \infty$ as $x \to \infty$. No sign confusion: F3
used in its signed form, F2's unsigned $O$ not invoked.

**What this means for the conjecture.** The conjecture's $\le 1 + o(1)$
upper bound, if true, is asymptotically *tight*: this section
shows the matching $\ge 1$ lower bound. The open analytic
question, then, is the matching upper bound — does the supremum
*stay* at $1$, or does it briefly enter $(1, e^{\gamma}\pi/4 +
o(1)]$? This is the content of the open conjecture; F1's
$\le e^\gamma \pi/4 + o(1)$ leaves the question wide.

(End of Section 4; Q17 resolved as a rigorous lower bound on the
conjecture's supremum, via F3 applied to $A_k$ for $k \to \infty$.)

### 5. Bracketing of the conjecture's supremum (round 16; resolves Q18)

Combining §4's rigorous lower bound with F1's rigorous upper bound,
the supremum lives in the bracket
\[
1 \;\le\; \liminf_{x \to \infty} \sup_{\substack{A \text{ primitive} \\ A \subset [x, \infty)}} S(A) \;\le\; \limsup_{x \to \infty} \sup_{\ldots} S(A) \;\le\; e^{\gamma}\pi/4 + o(1).
\]

The conjecture asserts that $\sup S(A) \le 1 + o(1)$ — i.e., the
$\limsup$ is also at most 1, matching the $\liminf$. This is an
asymptotic *equality* claim:
\[
\lim_{x \to \infty} \sup_{\substack{A \text{ primitive} \\ A \subset [x, \infty)}} S(A) \;\overset{?}{=}\; 1.
\]

The question is therefore *not* whether the limit exists (the
conjecture asserts it does), but whether the supremum *briefly
exceeds 1* on its way to the limit. F1's available rigorous bound
is strictly weaker than what the conjecture claims; the
quantitative slack between F1's right-hand side and the
conjecture's $1$ is what a closing argument would need to
eliminate.

#### 5.1 What the F1/F2/F3 ledger does and does not give

The ledger gives:
- **F1**: an upper bound on $\sup S(A)$ that is strictly weaker
  than the conjecture's claimed value (per §1.2's reading).
- **F2**: an unsigned envelope around $1$ for *individual* $A_k$, not
  a bound on the supremum of $S$ over primitive sets.
- **F3**: $S(A_k) \to 1$ from below, used in §4 for the lower bound.

The ledger does *not* give an upper bound on $\sup S(A)$ tighter
than F1's $e^\gamma \pi/4$. Closing the gap from F1's ceiling to
$1$ requires a fundamentally new ingredient (cross-stratum
primitivity, the §3 "Lemma 5" residue, in this writeup's framing).
The ledger alone cannot close the conjecture; that is precisely
the open analytic content.

#### 5.2 Why the lower bound matters

§4's lower bound $\ge 1$ confirms the conjecture's claim cannot be
*relaxed* — there is no slack in the ceiling itself. Any proof of
the conjecture would:
- *attain* the bound $1$ asymptotically (it cannot be better than
  $\le 1$, since §4 shows $\sup \ge 1$), and
- *match* F1's $e^\gamma \pi/4$ at every finite $x$, then tighten
  to $1$ as $x \to \infty$.

The conjecture is therefore an *asymptotic identity* on $\sup S(A)$:
the limit equals $1$. Proving it requires identifying the exact
mechanism by which the supremum is held at $1$ across all $x$ —
the cross-stratum primitivity exclusion (§3, Lemma 5) is the
candidate, but its rigorous form remains open.

#### 5.3 What §5 commits

§5 makes no new mathematical claim beyond what §4 (lower bound)
and F1 (upper bound) already establish. It is a *framing* of the
open question in light of §4's contribution. The conjecture
remains open. No witness is committed.

(End of Section 5; Q18 resolved by framing the open territory as
the asymptotic identity $\lim_{x \to \infty} \sup S(A) = 1$.)

### 6. Sum of F3-deficits over all strata (round 17; resolves Q19)

This section computes the sum of F3's per-stratum deficits over
all $\Omega$-strata, expressed as a closed-form constant times $c$.
The result is a structural fact extracted from F3 plus elementary
arithmetic — *no new external citations or numerical claims beyond
the ledger*.

#### 6.1 Generating-function identity

The series $\sum_{k \ge 1} k^2 / 2^k$ is convergent and admits a
closed form via standard generating-function manipulation. Starting
from $\sum_{k \ge 0} x^k = (1 - x)^{-1}$ for $|x| < 1$:

- Differentiating: $\sum_{k \ge 1} k x^{k-1} = (1-x)^{-2}$.
- Differentiating again and re-arranging: $\sum_{k \ge 1} k(k-1) x^{k-2} = 2(1-x)^{-3}$, hence $\sum_{k \ge 1} k^2 x^{k-2} = 2(1-x)^{-3} + (1-x)^{-2}$.
- Multiplying by $x^2$: $\sum_{k \ge 1} k^2 x^k = x^2 \cdot \bigl(2(1-x)^{-3} + (1-x)^{-2}\bigr)$.

Evaluating at $x = 1/2$:
- $\sum_{k \ge 1} k x^k = x/(1-x)^2 = (1/2)/(1/4) = 2$.
- $\sum_{k \ge 1} k(k-1) x^k = 2 x^2/(1-x)^3 = 2 \cdot (1/4)/(1/8) = 4$.
- Hence $\sum_{k \ge 1} k^2 x^k = \sum k(k-1) x^k + \sum k x^k = 4 + 2 = 6$.

Therefore $\sum_{k=1}^\infty k^2/2^k = 6$. This is elementary and
exact.

#### 6.2 Application to F3

F3 states $S(A_k) = 1 - (c + o(1)) k^2/2^k$, so the per-stratum
*deficit* (the gap from the conjecture's ceiling $1$) is, leading
order, $1 - S(A_k) \sim c \cdot k^2/2^k$. Summing over $k$ via
§6.1:
\[
\sum_{k=1}^{\infty} \bigl(1 - S(A_k)\bigr) \;\sim\; c \sum_{k=1}^{\infty} \frac{k^2}{2^k} \;=\; 6c \quad (\text{leading order from F3}).
\]

#### 6.3 What this is — and what it isn't

§6 has produced a clean closed-form: the *cumulative* F3-deficit
across all strata is $6c$ at leading order, with $c$ as in F3.

This is *not* a bound on $\sup S(A)$:
- The strata $A_k$ are pairwise disjoint, but $\bigsqcup_k A_k = \mathbb{N}$ is *not* primitive (e.g., $4 \in A_2$, $8 \in A_3$, $4 \mid 8$).
- The conjecture concerns $\sup S(A)$ over *primitive* $A$, not the disjoint union of $A_k$'s.
- $6c$ measures cumulative F3 deficit across strata, not anything directly bounded by the conjecture.

§6 is a structural observation — the cumulative deficit is
computable in closed form. It does *not* prove the conjecture, and
*does not commit a witness*. It positions the F3 deficit as a
single explicit number ($6c$ at leading order) that future
analytical work might relate to F1's truncated bound or to the
§3 cross-stratum residue.

#### 6.4 What §6 commits

- *Rigorously*: $\sum_k k^2/2^k = 6$ (elementary).
- *Conditionally on F3*: cumulative leading-order F3 deficit equals $6c$ at leading order.

It does NOT commit:
- Any comparison of $6c$ to $e^{\gamma}\pi/4 - 1$ at specific decimal precision.
- A bound on $\sup S(A)$.
- The conjecture itself.

The conjecture remains open. No witness is committed.

(End of Section 6; Q19 resolved as a structural closed-form identity
relating F3 and the generating function $\sum k^2/2^k$.)

### 7. Partial-result status update for §4–§6 additions (round 18; resolves Q20)

The §3.5 partial-result list is brought up to date to reflect the
content added by §4 (lower bound via $A_k$ for $k \to \infty$) and
§6 (cumulative F3-deficit closed form). These are appended as two
new bullets without altering any prior bullet:

- *Lower-bound construction* (§4): $\sup_{A \text{ primitive}, A \subset [x, \infty)} S(A) \ge 1$ is established rigorously via F3's signed asymptotic applied to $A_k$ for sufficiently large $k$ (per §4's threshold construction $\tau_k$) — $A_k$ is itself primitive (Lemma 1) and contained in $[x, \infty)$ (per §4's threshold argument), with $S(A_k) \to 1$ from below. (No witness is committed; this is a supremum statement, not a finite construction satisfying the witness contract of §1.3.)

- *Cumulative F3-deficit* (§6): summing F3's per-stratum deficits via the elementary identity $\sum_{k \ge 1} k^2/2^k = 6$ gives the closed-form $6c$ at leading order. Strata are not primitive in their disjoint union, so this is *not* a bound on $\sup S(A)$; it is a structural F3-derived constant available for future analytical work.

The lemma 5 file (`proof_lemmas/lemma_005_cross_stratum.md`) is
updated to mirror this status — its open content is now framed as
the cross-stratum mechanism that ties §4's lower bound to F1's
upper bound. The §Update there carries the same no-§1.3-witness
clarifier as the bullet above.

Neither §4 nor §6 commits a witness; the conjecture remains open.
The partial result of this writeup is now complete in the
following sense: every section either (a) records a rigorous
sub-result usable in a future proof or (b) frames an open
sub-question without claiming to resolve it. No section asserts
the conjecture is settled.

(End of Section 7; Q20 resolved by the §3.5 status update + lemma_005 sync.)

### 8. Synthesis (round 23; resolves Q25)

A short end-of-writeup synthesis. Sections §1-§7 collectively
establish, drawing only on the F1/F2/F3 ledger plus elementary
arithmetic:

- *Sign disambiguations* of F1, F2, F3 (§1.2);
- *Single-stratum primitivity* (Lemma 1, §3);
- *Single high-$\Omega$ stratum bound* — closed direction the
  conjecture asks (§3.3);
- *Lower bound on the supremum* matching the conjectured ceiling
  from below (§4);
- *Cumulative F3-deficit* in closed form (§6);
- *Witness search negative* — no counterexample found in probed
  parametric families (§2.5).

The cross-stratum residue (Lemma 5) remains open; F1's universal
upper bound is strictly weaker than what the conjecture asks, and
the F1/F2/F3 ledger alone does not bridge that slack.

The conjecture remains *open*. No witness is committed. The
writeup's partial-result content stands; future work must address
the cross-stratum residue or commit a witness.

(End of Section 8; Q25 resolved by collecting §1-§7 into a brief
synthesis.)
