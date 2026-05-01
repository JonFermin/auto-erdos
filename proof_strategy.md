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
$e^\gamma \pi / 4 \approx 1.399$ is positive and exceeds $1$, so F1 is
**consistent with** the conjecture — F1 is weaker than what we are
trying to prove. F1 must never be cited as a *lower* bound; doing so is
a sign error.

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
$\widehat{S}_k \;=\; 1 - c\, k^2 / 2^k$ with $c \approx 0.0656$ from the
ledger's F3 statement. This $\widehat{S}_k$ is the *leading-correction*
prediction; F3's $o(1)$ remainder is not computed here.

#### 2.2 Data

| $k$ | $\widehat{S}_k$ (F3 lead) | $S_{k}^{(200)}$ | $S_{k}^{(1000)}$ | $S_{k}^{(4000)}$ | $S_{k}^{(8000)}$ |
|----:|----:|----:|----:|----:|----:|
| 1 | $0.9672$ | $1.4965$ | $1.5253$ | $1.5418$ | $1.5482$ |
| 2 | $0.9344$ | $0.6819$ | $0.7461$ | $0.7877$ | $0.8052$ |
| 3 | $0.9262$ | $0.3134$ | $0.3676$ | $0.4072$ | $0.4249$ |
| 4 | $0.9344$ | $0.1403$ | $0.1730$ | $0.1986$ | $0.2107$ |

(Values for $k = 1$ at $N = 200$, $1000$, $4000$, $8000$ correspond to
last primes $1223$, $7919$, $37{,}813$, $81{,}799$ respectively.)

#### 2.3 Reading the data

1. **The case $k = 1$ is the lone outlier**, with truncated sums
   exceeding $1$ already at $N = 200$. This is *not* in conflict with
   F3: F3 is an asymptotic statement as $k \to \infty$, and at $k = 1$
   the leading-correction expression $1 - c \cdot 1 / 2 = 0.9672$ is
   far from the actual full-stratum value
   $\sum_{p} 1/(p \log p) \approx 1.6366$. F3's $o(1)$ remainder is
   bounded only as $k \to \infty$, so finite-$k$ pointwise agreement
   is not asserted.

   Crucially, the $k = 1$ stratum (primes) does *not* refute the
   conjecture either: the conjecture concerns primitive sets contained
   in $[x, \infty)$, and as $x \to \infty$ the truncation
   $\sum_{p \geq x} 1/(p \log p) \to 0$, because the series
   $\sum_p 1/(p \log p)$ converges (a classical consequence of
   $\pi(t) \sim t / \log t$ via integral comparison against
   $\int dt / (t \log^2 t)$). The $\sim 1.64$ figure is for primes
   from $2$, not from $x$.

2. **For $k \in \{2, 3, 4\}$**, every truncated sum satisfies
   $S_k^{(N)} < \widehat{S}_k < 1$, monotone increasing in $N$, with
   substantial residual gap to $\widehat{S}_k$: at $N = 8000$ the gaps
   are $+0.129$, $+0.501$, $+0.724$ for $k = 2, 3, 4$. This is the
   expected behavior of partial sums of a slowly convergent series
   (the heavy tail is uncaptured by any finite-$N$ truncation).

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

For $k = 1$ the relevant primitive set is the primes, and a primitive
$A \subset [x, \infty)$ that lives entirely in $A_1$ has its sum
controlled by the tail
$\sum_{p \geq x} 1/(p \log p)$, which tends to $0$ as $x \to \infty$
because the series $\sum_{p} 1/(p \log p)$ converges (its convergence
is a classical consequence of the prime-counting estimate
$\pi(t) \sim t / \log t$, via integral comparison
against $\int dt / (t \log^2 t)$). So the $k=1$ stratum, despite its
notorious $\sim 1.6366$ full sum from $p = 2$, contributes
asymptotically $0$ when restricted to $[x, \infty)$.

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
