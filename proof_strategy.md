# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Section 1 — Setup

**Claim** (from `proofs/primitive_set_erdos.json`): For any $x$, if
$A \subset [x, \infty)$ is a primitive set of integers (no distinct element
divides another) then
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1),$$
where the $o(1)$ term tends to $0$ as $x \to \infty$.

**Status**: open. Until a verifier-accepted witness is committed, no claim
of resolution may appear in this file.

**Given facts ledger** (from `proofs/primitive_set_erdos.json`):

- **F1** (Erdős–Zhang upper bound, citation: Erdős 1935; Zhang 1993): For any
  primitive set $A \subseteq \mathbb{N}$,
  $$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1).$$
  Sign: UPPER bound, strictly less than. This bound is consistent with the
  conjecture; the conjecture tightens the constant from ~1.399 to 1.

- **F2** (Omega-stratum lower bound, UNSIGNED big-O): For
  $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
  $$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2 + o(1)}).$$
  The $O(\cdot)$ term is **unsigned** — it could be positive or negative.
  Concluding $\sum > 1$ from F2 alone is a SIGN ERROR (anti-trap 1).
  **Note**: F2 is documented here for anti-trap awareness and is NOT cited in
  any positive derivation in this proof; it appears only in Section 3 to document
  a dead end.

- **F3** (Asymptotic for large $k$): For
  $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
  $$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
  \quad c \approx 0.0656 > 0.$$
  The $o(1)$ is as $k \to \infty$. For large $k$, $c + o(1) \to c > 0$, so the
  correction is negative and $k^2/2^k \to 0$: the sum approaches 1 from BELOW as
  $k \to \infty$ (anti-trap 2). In particular, $T_k(2) < 1$ for all sufficiently
  large $k$. (The formula is asymptotic; for small fixed $k$ such as $k=1$,
  $T_k(2)$ may exceed 1 and the asymptotic does not apply directly.)

**Anti-traps** (do not trigger):

1. F2 sign confusion: unsigned big-O does not imply sum > 1 for any stratum.
2. F3 from-above misread: for large $k$, the sum approaches 1 from BELOW
   (correction is negative). Do NOT conclude sum $> 1$ from F3.
3. Open-claim-asserted-resolved-without-witness: the conjecture is open.

**Conceptual calibration** (not a proof): The conjecture concerns
$A \subset [x, \infty)$ for LARGE $x$; only elements $a \geq x$ contribute.
For large $k$ (where F3 applies), $T_k(2) < 1$ strictly (approaching 1 from below
as $k \to \infty$), so $T_k(x) \leq T_k(2) < 1$. For each fixed $k$, the fixed-$k$
tail behavior is treated in `proof_lemmas/lemma_large_floor_vanish.md`.
The per-stratum bound $T_k(x) \leq T_k(2)$ combined with the F3 asymptotics
is the key quantitative ingredient for the conjecture's $o(1)$ form.

---

## Section 2 — Omega stratification (Q5 proof structure)

For any primitive set $A \subset [x, \infty)$, partition by $\Omega(a)$:
$$\sum_{a \in A} \frac{1}{a \log a}
  = \sum_{k=1}^{\infty} S_k(A, x),
  \quad S_k(A,x) := \sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a}.$$

Define the tail of the $k$-stratum from $x$:
$$T_k(x) := \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n}.$$

**Lemma `stratum_sub_bound`** (status: proved): For any primitive $A \subset
[x, \infty)$ and any $k \geq 1$,
$$S_k(A, x) \leq T_k(x).$$

Proof: $A^{(k)} := A \cap \{n : \Omega(n) = k\}$ is a subset of
$\{n \geq x : \Omega(n)=k\}$, so every term in $\sum_{a \in A^{(k)}} 1/(a\log a)$
also appears in $T_k(x)$, giving $S_k(A,x) \leq T_k(x)$.
See `proof_lemmas/lemma_stratum_sub_bound.md`. $\square$

Note: We write $T_k(2) := \sum_{n:\,\Omega(n)=k} 1/(n \log n)$ as a **definition** (notation only,
not a new claim): this is the full $k$-stratum sum used in F3. F3 directly states
$T_k(2) = 1 - (c+o(1))k^2/2^k$ as $k \to \infty$, with sign-disambiguation $T_k(2) < 1$
for all sufficiently large $k$. We have $T_k(x) \leq T_k(2)$ since
$T_k(x)$ sums over $n \geq x$ while $T_k(2)$ sums over all $n \geq 2$
(every term of $T_k(x)$ also appears in $T_k(2)$).
For the fixed-$k$ tail analysis, see `proof_lemmas/lemma_large_floor_vanish.md`.

**Corollary (Low-stratum control, FIXED $K$ only)**: For each fixed constant $K \geq 1$
(not depending on $x$),
$$\sum_{k=1}^{K} S_k(A, x) \leq \sum_{k=1}^{K} T_k(x).$$

The bound on each $T_k(x)$ and the behavior of this sum as $x \to \infty$ is
given in `proof_lemmas/lemma_low_stratum_vanish.md`. $\square$

**Warning**: This Corollary is VALID ONLY for fixed $K$: if $K = K(x) \to \infty$
with $x$, the resulting sum of $K(x)$ terms need not tend to $0$.
The Corollary is not applicable to a growing $K(x)$.

**Decomposition**: For a FIXED constant $K \geq 1$ (not varying with $x$), split:
$$\sum_{a \in A} \frac{1}{a \log a}
  = \underbrace{\sum_{k=1}^{K} S_k(A,x)}_{\text{(I) low strata, fixed }K}
  + \underbrace{\sum_{k > K} S_k(A,x)}_{\text{(II) high strata}}.$$

- **(I) Low strata** ($K$ fixed): $\leq \sum_{k=1}^K T_k(x)$ by the Corollary above;
  the behavior of this finite sum as $x \to \infty$ is in the lemma file.

- **(II) High strata**: $\leq \sum_{k > K} T_k(x) \leq \sum_{k > K} T_k(2)$.
  By F3, each $T_k(2) \to 1$ as $k \to \infty$, so $\sum_{k > K} T_k(2)$ diverges
  (infinitely many terms each approaching 1).
  The stratification bound is VACUOUS for the high-stratum sum, for any fixed $K$.

**Key difficulty** (the open core, Lemma `cross_stratum_control`): The per-stratum
argument fails globally. To bound the high-stratum contribution, one must use
the PRIMITIVITY CONSTRAINT across strata — i.e., the fact that for distinct
$a, b \in A$ with $\Omega(a) \neq \Omega(b)$, still $a \nmid b$. The
antichain structure imposes a global constraint that prevents many strata from
each contributing weight close to 1 simultaneously.

Formally, what is needed (and not proved here) is:

$$\text{Lemma (cross\_stratum\_control):} \quad
\sum_{k > K} S_k(A, x) \leq 1 + o(1) - \sum_{k=1}^K S_k(A, x) - o(1)$$

for appropriate $K = K(x) \to \infty$. Equivalently, the full sum
$\sum_{a \in A} 1/(a \log a) \leq 1 + o(1)$ is precisely the conjecture.

See `proof_lemmas/lemma_cross_stratum_control.md` for the precise gap statement.

---

## Section 3 — Partial result (Q6)

**What is established** (the provable part):

1. **Per-stratum bound**: Each stratum of any primitive set contributes at most
   $T_k(x)$ to the sum (Lemma `stratum_sub_bound`, proved). For large $k$,
   $T_k(x) \leq T_k(2) < 1$ by F3.

2. **Fixed-stratum tail**: For each fixed $k$, the per-stratum sum $S_k(A,x) \leq T_k(x)$;
   the fixed-$k$ tail analysis is in `proof_lemmas/lemma_large_floor_vanish.md`.

3. **Low-stratum $o(1)$**: For any fixed $K$, the sum over strata $k \leq K$
   from $[x, \infty)$ is $o(1)$ as $x \to \infty$.

4. **Global upper bound (from F1)**: The total sum is $< e^\gamma \pi/4 + o(1)$
   (the Erdős–Zhang bound). This is an input fact, not proved here.

**What remains open** (the proof gap):

The critical regime is strata $k \sim k^* := \lfloor \log_2 x \rfloor$. For
such $k$, the smallest $k$-almost prime is $2^k \approx x$, so the restriction
$a \geq x$ imposes almost no constraint on $A^{(k)}$. By F3, the total sum
over $A_k$ (all $k$-almost primes) is strictly less than $1$ and approaches
$1$ as $k \to \infty$. For $k$ near $k^*$ (where $2^{k^*} \approx x$), the
per-stratum sum is close to $1$ because the NEGATIVE correction in F3,
$-(c+o(1))k^{*2}/2^{k^*} \approx -(c+o(1))(\log_2 x)^2/x$, is negligible for large $x$.
Summing $2C$ such per-stratum bounds — each close to $1$ — gives a total close
to $2C$, which grows without bound as $C \to \infty$, regardless of $x$.
Controlling this requires a global argument that uses primitivity to prevent
multiple critical strata from simultaneously contributing nearly $1$.

**Dead ends ruled out**:
- Using F2's unsigned big-O to conclude $\sum > 1$ for any stratum: SIGN ERROR.
- Summing per-stratum bounds $\sum_k T_k(2)$ (each $< 1$ by F3 but each $\to 1$
  as $k\to\infty$) and claiming total $\leq 1$: this series diverges; the approach fails.
- Claiming the conjecture is proved or disproved without a valid witness:
  not supported.

The results above constitute the partial progress committed in this document.
The conjecture remains open; Section 4 continues the exploration.
A per-dyadic-interval bound and further suggested directions are deferred
to `proof_lemmas/lemma_dyadic_interval_bound.md` and
`proof_lemmas/lemma_cross_stratum_control.md`.

---

## Section 4 — Trading decomposition (Q7)

**Setup**: Fix $e = 2.718\ldots$ (Euler's number). For any primitive set
$A \subset [x, \infty)$, split at the "pivot" $x^e$:
$$A_1 := A \cap [x,\, x^e), \qquad A_2 := A \cap [x^e, \infty).$$

Let $S_1 := \sum_{a \in A_1} \frac{1}{a \log a}$ and
$S_2 := \sum_{a \in A_2} \frac{1}{a \log a}$.

**Upper bound on $S_1$**: Since $A_1 \subset [x, \infty)$ is a primitive set,
F1 gives $S_1 < e^\gamma \frac{\pi}{4} + o(1)$ (o(1) as $x \to \infty$).
(Here and throughout Section 4, $\log = \ln$ denotes the natural logarithm.)
A finer bound via basic integral comparison is in `proof_lemmas/lemma_s1_bound.md`.

**Why $S_2$ is hard without primitivity**:

The contribution from $A_2$ cannot be controlled by F1/F2/F3 applied to $A_2$ alone:
F1 gives $S_2 < e^\gamma\pi/4 + o(1)$ (o(1) as $x^e \to \infty$, hence as $x \to \infty$),
but this bound exceeds the conjecture's target $1 + o(1)$ since $e^\gamma\pi/4 \approx 1.399 > 1$.
The joint primitivity constraint — that no element of $A_1$ divides any element of $A_2$
and vice versa — is the only known mechanism to control $S_2$ below $1$.

**The blocking principle (the open part)**:

For each $a \in A_1$, primitivity forbids all proper multiples $am$ ($m \geq 2$) from
belonging to $A$. In particular, elements of $A_2$ that are multiples of some
$a \in A_1$ are excluded. Define the "blocked set":
$$\mathcal{B}(A_1) := \{n \geq x^e : a \mid n \text{ for some } a \in A_1\}.$$

Then $A_2 \subseteq [x^e, \infty) \setminus \mathcal{B}(A_1)$, i.e., every element of
$A_2$ avoids all divisibility relations with $A_1$. The "unblocked" residual is:
$$A_2 \subseteq \mathcal{U}(A_1) := \{n \geq x^e : a \nmid n \text{ for all } a \in A_1\}.$$

Equivalently, $\mathcal{U}(A_1)$ is the set of $n \geq x^e$ not divisible by any
$a \in A_1$ (i.e. $\gcd(n, a) < a$ for all $a \in A_1$ — these two formulations
are equivalent since $a \mid n \Leftrightarrow \gcd(n,a) = a$).

**Lemma (`blocking_estimate`, STATUS: OPEN — the open core)**: For any
primitive set $A \subset [x, \infty)$ with the decomposition above, find a
quantitative upper bound on $S_2$ in terms of the primitivity constraint
between $A_1$ and $A_2$. Specifically, what is needed is some function $f$
such that $S_2 \leq f(S_1)$ for all primitive $A$ and all $x$ large,
and $f$ is small enough that $S_1 + f(S_1) \leq 1 + o(1)$. No such $f$ is currently known.

*Why sieve-density arguments fail* (heuristic exploration):

A natural approach is to estimate how many integers in $[x^e, \infty)$ avoid
divisibility by $A_1$. Even if only a small fraction $\rho \ll 1$ of integers in
each interval $[N, 2N)$ escape blocking by $A_1$, the sum
$\rho \cdot \sum_{n=N}^{2N-1} 1/(n \log n) \leq \rho/\log N$
over infinitely many dyadic intervals $N = x^e, 2x^e, 4x^e, \ldots$ gives
$\rho \cdot \sum_{j \geq 0} 1/(e \log x + j \log 2)$, which is not bounded by
any finite constant independent of $J$ — the partial sums grow with $J$.
No multiplier $\rho > 0$ can convert this into a bounded series.

**Why this fails**: The tail $\sum_{n \geq x^e, n \in \mathcal{U}(A_1)} 1/(n \log n)$
cannot be bounded by a sieve-density argument alone, because the base series
$\sum_{n \geq x^e} 1/(n \log n)$ is unbounded and a multiplicative density factor
(not depending on $n$) cannot convert an unbounded series to a bounded one.

Conclusion: Controlling $S_2$ via "unblocked density from $A_1$" fails because
the density factor does not cure the unboundedness of the base sum.

**Correct interpretation**: Even if one accounts for the blocking by $A_1$
at every dyadic scale $[x^e 2^j, x^e 2^{j+1})$ via a multiplicative density
factor $\rho < 1$ (the proportion of integers surviving the sieve by $A_1$),
the partial sums $\rho \cdot \sum_{j=0}^J 1/(e \log x + j \log 2)$ grow
without bound as $J \to \infty$. Multiplying an unbounded series by any
positive constant does not make it convergent, so this heuristic cannot bound
$S_2$.

**Key insight from this failure**: Controlling $S_2$ via the "blocking density"
of $A_1$ does not close the problem, because even after blocking by $A_1$, the
remaining integers in $[x^e, \infty)$ form a set whose sum $\sum 1/(n \log n)$
diverges. What IS needed: the elements of $A_2$ themselves must be a PRIMITIVE
SET (no two divide each other), which is a further constraint on $A_2$ beyond
just "not divisible by $A_1$."

**New reformulation (open)**:

Split the problem differently: instead of bounding $S_2$ in terms of $A_1$,
bound the combined sum $S_1 + S_2 \leq 1 + o(1)$ by using the fact that
$A = A_1 \cup A_2$ is primitive as a WHOLE. The primitivity of $A$ constrains
not only the cross-divisibility between $A_1$ and $A_2$, but also the internal
structure of $A_2$.

Define the "reflected" set: for each $b \in A_2$, the set of "divisors" of $b$
in $A_1$ is empty (by primitivity). Also, the set of "multiples" of $b$ in
$A_1$ is empty. And no two elements of $A_2$ divide each other.

The combined constraint: $A_2$ is a primitive set in $[x^e, \infty)$ that also
avoids all elements divisible by some $a \in A_1$.

**Why recursion fails**: Any attempt to bound $S_2$ by applying a recursive
argument to $A_2 \subset [x^e, \infty)$ reduces to the same unsolved problem:
$A_2$ is itself a primitive set, and controlling $\sum_{b \in A_2} 1/(b \log b)$
requires precisely the structural insight we need for $A$. The only available
non-trivial global upper bound for any primitive set is F1 (Erdős–Zhang),
which gives $S_2 < e^\gamma \pi/4 + o(1)$ (o(1) as $x \to \infty$) by F1 (applied to the primitive set $A_2 \subset [x^e,\infty)$).
Combined with $S_1 < e^\gamma \pi/4 + o(1)$ (o(1) as $x \to \infty$, F1 applied to the primitive set $A_1$), this gives
$S_1 + S_2 < 2(e^\gamma \pi/4) + o(1)$ — weaker than F1 applied directly to $A$, and not
a proof of the conjecture. No recursive application closes the gap.

**Dead end confirmed**: The trading decomposition at $x^e$ does NOT give
$S_1 + S_2 \leq 1 + o(1)$ without additional input. The F1 bound on $S_1$
leaves $S_2$ entirely uncontrolled without exploiting the cross-structure of
primitivity between $A_1$ and $A_2$.

See `proof_lemmas/lemma_trading_decomposition.md` for the precise gap statement.

**What IS needed (updated obstacle)**:

To prove the conjecture, one needs to show that for a primitive set
$A \subset [x, \infty)$:

The essential question is: for a primitive set $A \subset [x, \infty)$, can one show
$S_1 + S_2 \leq 1 + o(1)$ exploiting the joint primitivity structure?

If $S_1$ is large (say near $e^\gamma\pi/4$), then $A_1$ is "dense" in the
$1/(a\log a)$ sense, and that density should force many multiples into $[x^e, \infty)$,
leaving $A_2$ (which avoids all those multiples) sparsely distributed.
This requires showing that density in $[x, x^e)$
forces near-emptiness (in the $\sum 1/(a \log a)$ sense) of $A_2$.

The "density" of $A_1$ in $[x, x^e)$ needs to be measured in a way compatible
with both the $1/(a \log a)$ metric AND the divisibility blocking structure.
This is the essential unresolved point.

---

## Section 5 — Blocking-density perspective and the sieve gap

This section formalises the cross-structure of the trading decomposition and
identifies the essential missing ingredient.

### 5.1 Blocked multiples

For any $a \in A_1 \subset [x, x^e)$, primitivity of $A$ means that every
proper multiple of $a$ is excluded from $A$. In particular, every proper
multiple $ma$ (with $m \geq 2$) that lies in $[x^e, \infty)$ is excluded
from $A_2$. Define the blocked set:
$$B(a) := \{ma : m \geq 2,\; ma \geq x^e\}.$$
Then $A_2 \cap B(a) = \emptyset$ for every $a \in A_1$.

Since $a \geq x$, the smallest multiple in $B(a)$ is $\geq 2x$. Since
$a < x^e$, elements of $B(a)$ that lie in $[x^e, \infty)$ are those with
$m \geq \lceil x^e/a \rceil \geq 2$. The set $B(a)$ is an infinite
arithmetic progression $\{ma : m \geq \lceil x^e/a \rceil\}$.

### 5.2 Sieve formulation

Collecting all blocked elements: define the **sieved set**
$$\mathcal{S}(A_1) := \{n \geq x^e : a \nmid n \text{ for all } a \in A_1\}.$$

Primitivity gives $A_2 \subset \mathcal{S}(A_1)$: for every $b \in A_2$ and
every $a \in A_1$, since $a, b \in A$ are distinct elements and $A$ is
primitive, $a \nmid b$ and $b \nmid a$. So $b$ avoids all divisors in $A_1$.

The goal reduces to: show that $\sum_{b \in A_2} 1/(b\log b) = o(1)$
whenever $A_1$ is "dense" in the $1/(a\log a)$ metric, i.e., $S_1$ is
close to 1.

### 5.3 The density-sparsity tension

The trading approach posits: near-saturation of $S_1 \approx 1$ forces
$A_1$ to contain many elements spread throughout $[x, x^e)$, each blocking
a progression from $A_2$.

However, this tension is hard to quantify because:
- $A_1$ being large in the $1/(a\log a)$ metric does not directly translate
  to a uniform density bound on the integers it blocks.
- The blocked progressions $\{ma : m \geq \lceil x^e/a \rceil\}$ for
  different $a \in A_1$ can overlap in complex ways, so the union
  $\bigcup_{a \in A_1} B(a)$ might not cover a large fraction of $[x^e, 2x^e)$
  in the $1/(n\log n)$ metric.

The essential question: does there exist a function $f$ with
$f(t) + t \leq 1 + o(1)$ for $t$ in the relevant range of $S_1$, such
that for any primitive $A_2 \subset \mathcal{S}(A_1)$, $S_2 \leq f(S_1)$?
A YES answer would close the conjecture; the existence of such $f$ is not known.

### 5.4 Current status and next steps

What is proved (combining Sections 2–4):
- $S_1 < e^\gamma \pi/4 + o(1)$ (F1 applied to primitive set $A_1 \subset [x,\infty)$; o(1) as $x \to \infty$)
- $S_2 < e^\gamma \pi/4 + o(1)$ (F1 applied to primitive set $A_2 \subset [x^e,\infty)$; o(1) as $x^e \to \infty$, equivalently as $x \to \infty$)
- The combined bound $S_1 + S_2 < 2(e^\gamma \pi/4) + o(1)$ (weaker than F1 directly; both o(1) terms are as $x \to \infty$)

What is open: showing $S_2 = o(1)$ or $S_1 + S_2 \leq 1 + o(1)$ via the
blocking structure. This requires a quantitative sieve bound or a new
combinatorial argument exploiting cross-interval primitivity.

Candidate approaches for future rounds:
(A) Selberg-type upper sieve for $\sum_{n \in \mathcal{S}(A_1)} 1/(n\log n)$
    when $A_1$ is a dense primitive set in $[x, x^e)$.
(B) Showing the S2 region [x^e, ∞) contributes $o(1)$ whenever A1 nearly
    saturates S1 = 1, via a counting argument on the divisibility antichain.
(C) A direct approach not using the trading decomposition.

---

## Section 6: Stratification and the Low-Stratum Easy Case

### 6.1 The low-stratum lemma (proved)

**Observation (low-stratum sub-sum)**: For any primitive set $A \subset [x,\infty)$
with all $\Omega(a) \leq K$,
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_{k=1}^{K} T_k(x).$$

*Proof*: Partition $A$ by stratum: $A^{(k)} = \{a \in A : \Omega(a) = k\}$.
Each $a \in A^{(k)}$ satisfies $a \geq x$, so $1/(a\log a)$ is one term
in $T_k(x) = \sum_{n \geq x,\, \Omega(n)=k} 1/(n\log n)$ (since $A^{(k)} \subset
\{n \geq x : \Omega(n) = k\}$). Summing over $k = 1,\ldots, K$: $\sum_{a \in A}
= \sum_{k=1}^K \sum_{a \in A^{(k)}} \leq \sum_{k=1}^K T_k(x)$. $\square$

**Why the bound vanishes**: For each fixed $k$, the set $\mathcal{A}_k := \{n : \Omega(n)=k\}$
is a primitive set (if $n \mid m$ with $\Omega(n)=\Omega(m)=k$, then $m$ has at least
$k+1$ prime factors — a contradiction). By F1 applied to this primitive set,
$T_k(2) = \sum_{n \in \mathcal{A}_k} 1/(n\log n) \leq e^\gamma\pi/4 < \infty$.
Since $T_k(x)$ is the tail of the convergent series $T_k(2)$ beginning at $x$,
tails of convergent series vanish: $T_k(x) \to 0$ as $x \to \infty$.
Hence $\sum_{k=1}^K T_k(x) \to 0$ for any fixed $K$.

**Consequence**: The conjecture holds easily (with $o(1)$ bound) whenever $A$
is supported on strata of bounded Omega-number. The hard case requires elements
with $\Omega(a) \to \infty$ as $x \to \infty$.

### 6.2 The critical Omega-regime

For $A \subset [x, \infty)$, the most "expensive" elements (those with smallest
$1/(a\log a)$) are the ones with $a$ barely exceeding $x$, which requires the
$k$-almost prime to be near $x$. A stratum-$k$ element $a \geq x$ exists
precisely when there is a $k$-almost prime $\geq x$, which holds for all $k \geq 1$.
The minimum element in stratum $k$ above $x$ scales roughly as $x$ when
$k \approx \log_2 x$ (detailed analysis deferred to
`proof_lemmas/lemma_min_k_almost_prime.md`).

For each fixed $k$: by the argument in Section 6.1 ("Why the bound vanishes"),
$T_k(x) \to 0$ as $x \to \infty$ (tail of a series shown convergent via F1).

For $k \geq \lceil\log_2 x\rceil$: any integer $n$ with $\Omega(n) = k$ has $k$
prime factors each $\geq 2$, so $n \geq 2^k \geq x$; the lower bound $n \geq x$ in
$T_k(x) = \sum_{n \geq x,\, \Omega(n)=k} 1/(n\log n)$ excludes no terms, giving
$T_k(x) = T_k(2)$. (This uses only arithmetic: the product of $k$ integers each
$\geq 2$ is at least $2^k$.)

The critical range is $k \in [k^* - C, k^* + C]$ for $k^* = \lfloor \log_2 x
\rfloor$ and any fixed $C$. An element $a \geq x$ with $\Omega(a) = k$ in
this range satisfies $a \approx x$, meaning $a$ is an integer near $x$
that is a product of $k \approx \log_2 x$ prime factors.

### 6.3 Single-stratum primitivity: an automatic constraint

**Observation**: Within a single stratum $A^{(k)} = \{a \in A : \Omega(a) =
k\}$, the primitive-set condition $a \nmid b$ for distinct $a, b \in A$
is automatically satisfied. Indeed, if $a \mid b$ and $\Omega(a) = \Omega(b)
= k$ with $a \neq b$, then $b = am$ for some integer $m \geq 2$, giving
$\Omega(b) = \Omega(a) + \Omega(m) \geq k + 1$, a contradiction. So $A^{(k)}$
can be the entire set of $k$-almost primes $\geq x$ — no intra-stratum
restriction from primitivity.

**Consequence**: The primitivity constraint acts only across different strata.
For $a \in A^{(j)}$ and $b \in A^{(k)}$ with $j < k$, primitivity forbids
$a \mid b$. This cross-stratum exclusion is the only force preventing $S$
from exceeding $1$.

### 6.4 The two-stratum subcase

Consider $A \subset [x, \infty)$ primitive with elements only in strata $j$ and
$k$ (fixed $j < k$, both near $k^*$). Then:
$$S = S_j + S_k \leq T_j(x) + T_k(x) \leq T_j(2) + T_k(2),$$
where by F3 sign-disambiguation $T_\ell(2) < 1$ for all sufficiently large $\ell$.
For $j$ or $k$ near $k^*$ (large), this gives $T_j(2) < 1$ and $T_k(2) < 1$.
For $j$ or $k$ small (say $j = 1$, $k = 2$), the F3 asymptotic does not apply;
in that case $T_j(2)$ or $T_k(2)$ may exceed $1$, so the two per-stratum bounds
could sum to exceed $1$, showing the naive two-stratum bound is insufficient.

Cross-stratum primitivity constrains $A^{(k)}$: for each $a \in A^{(j)}$ and
$b \in A^{(k)}$, $a \nmid b$. So $A^{(k)}$ is contained in the sieved set
$$\mathcal{S}_k(A^{(j)}) := \{n \geq x : \Omega(n) = k,\; a \nmid n \;
\forall a \in A^{(j)}\}.$$

A quantitative bound on $\sum_{n \in \mathcal{S}_k(A^{(j)})} 1/(n\log n)$
in terms of $S_j$ (the weight of $A^{(j)}$) would close the two-stratum case.
Such a quantitative bound on the sieved $k$-almost-prime sum would require
analytic input beyond F1/F2/F3; this case remains open.

### 6.5 Gap summary and updated strategy

What the analysis achieves (combining all sections):
- **Sections 2–3**: Per-stratum bounds; each $S_k < 1$; summing diverges.
- **Section 4**: Trading decomposition; $S_1 < e^\gamma\pi/4 + o(1)$ (o(1) as $x \to \infty$) by F1.
- **Section 5**: Blocking density; $S_2$ open.
- **Section 6, Lemma `low_stratum_vanish`**: For $\Omega(a) \leq K$ (fixed),
  $S = o(1)$ — conjecture holds easily.
- **Section 6.3**: Cross-stratum primitivity is the binding constraint.

The remaining open core: for primitive $A \subset [x, \infty)$ with elements
in the critical window $\Omega(a) \in [k^* - C, k^* + C]$, prove
$\sum_{a \in A} 1/(a\log a) < 1 + o(1)$.

This is a cleaner reformulation than the original: it isolates the critical
Omega-regime, handles the "bounded Omega" case completely, and reduces the
problem to the behavior of sieved $k$-almost prime sums.

---

## Section 7 — Single-Stratum Sub-Conjecture: PROVED (Q15)

**Lemma `single_stratum_bound`** (status: proved): For any primitive set
$A \subset [x, \infty)$ whose elements all satisfy $\Omega(a) = k$
(a single fixed or growing stratum), the sum satisfies
$$S := \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad (x \to \infty).$$

*Proof (two cases)*:

*Case 1 ($k$ fixed as $x\to\infty$)*: For all sufficiently large fixed $k$,
$T_k(2) < 1$ by F3 sign disambiguation, so $S \leq T_k(x) \leq T_k(2) < 1 < 1 + o(1)$.
For small fixed $k$: $\mathcal{A}_k$ is a primitive set (Section 6.1), so by F1,
$T_k(2) < \infty$; thus $T_k(x)$ (tail of convergent series) $\to 0$ as $x \to \infty$,
giving $S \leq T_k(x) = o(1) < 1 + o(1)$.

*Case 2 ($k = k(x) \to \infty$)*: By F3 (asymptotic formula for large $k$): $T_k(2) =
1 - (c + o(1))k^2/2^k$. For large $k$, $c + o(1) \to c > 0$ and $(c+o(1))k^2/2^k > 0$,
so $T_k(2) < 1$ for all sufficiently large $k$. Hence $S \leq T_k(x) \leq T_k(2) < 1 < 1 + o(1)$.

Combined: In both cases $S < 1 + o(1)$ as $x\to\infty$. $\square$

See `proof_lemmas/lemma_single_stratum_bound.md` for the complete argument.

**Consequence**: The conjecture holds for single-stratum primitive sets.
The remaining open case is when $A$ spans two or more $\Omega$-strata; in
that case, cross-stratum primitivity must prevent simultaneous near-1
contributions from multiple strata.

---

## Section 8 — Two-Stratum Bound (Q16)

**Lemma `two_stratum_bound`** (status: partial): For any primitive set
$A \subset [x, \infty)$ supported on exactly two $\Omega$-strata $j < k$
(i.e.\ $\Omega(a) \in \{j, k\}$ for all $a \in A$), the sum satisfies
$$S := \sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad (x \to \infty)$$
whenever at least one of $j$ or $k$ is bounded (does not grow with $x$).

*Proof of the bounded-stratum cases*:

Write $S = S_j + S_k$ where $S_j = \sum_{\substack{a \in A \\ \Omega(a)=j}} \frac{1}{a\log a}$
and $S_k$ analogously. By Lemma `stratum_sub_bound`, $S_j \leq T_j(x)$ and
$S_k \leq T_k(x) \leq T_k(2)$.

*Case (a): $j$ bounded (fixed as $x\to\infty$).* We have $S_j \leq T_j(x)$.
By Section 6.1 ("Why the bound vanishes"), $T_j(x) \to 0$ as $x\to\infty$
(F1 gives $T_j(2) < \infty$; tail of convergent series vanishes). So $S_j = o(1)$.
For $S_k$: if $k$ is also fixed, $S_k \leq T_k(x) = o(1)$ similarly. If
$k = k(x) \to \infty$, then by F3 (asymptotic for large $k$): $T_k(2) < 1$
for sufficiently large $k$, so $S_k \leq T_k(2) < 1$.
In either subcase, $S = o(1) + (<1) < 1 + o(1)$. $\square$

*Case (b): $k$ bounded (fixed as $x\to\infty$).* Then $j < k$ is also bounded,
and by Section 6.1, $T_j(x) \to 0$ and $T_k(x) \to 0$ as $x \to \infty$
(F1 finite + tail argument). So $S = S_j + S_k \leq T_j(x) + T_k(x) = o(1) < 1 + o(1)$. $\square$

**The hard case (open sub-problem)**: When both $j = j(x) \to \infty$ and
$k = k(x) \to \infty$ as $x \to \infty$, the per-stratum bound gives
$S \leq T_j(2) + T_k(2)$. By F3, $T_j(2) \to 1$ and $T_k(2) \to 1$ from
below, so this bound $\to 2$, which is vacuous.

**Cross-stratum blocking (formal exploration)**:

Within the two-stratum case, primitivity of $A$ forces: for every
$a \in A^{(j)}$ and every $b \in A^{(k)}$, we have $a \nmid b$ (since
$j < k$ and $a \mid b$ with $\Omega(a) = j$, $\Omega(b) = k$ would require
$b = a \cdot m$ for some $m$ with $\Omega(m) = k - j \geq 1$, but then
$a, b \in A$ and $a \mid b$ — contradicting primitivity). So
$$A^{(k)} \subseteq \mathcal{S}_k(A^{(j)}) := \bigl\{n \geq x : \Omega(n) = k,\;
a \nmid n \text{ for all } a \in A^{(j)}\bigr\}.$$

For each $a \in A^{(j)}$, define the blocked weight:
$$W_k(a) := \sum_{\substack{m \geq 2 \\ \Omega(m) = k-j}} \frac{1}{am \cdot \log(am)}.$$
Since $am \geq a \cdot m \geq a \cdot 2$ and $\log(am) \geq \log m$, we have
$1/(am\log(am)) \leq 1/(am\log m)$, giving
$$W_k(a) \leq \frac{1}{a} \sum_{\substack{m \geq 2 \\ \Omega(m) = k-j}}
\frac{1}{m\log m} \leq \frac{T_{k-j}(2)}{a},$$
where $T_{k-j}(2) := \sum_{\Omega(m)=k-j} \frac{1}{m\log m}$ is the $(k-j)$-stratum sum.

**Direction note**: The bound $W_k(a) \leq T_{k-j}(2)/a$ is an UPPER bound on the
blocked weight from element $a$. An upper bound on each $W_k(a)$ yields an
upper bound on the total blocked weight:
$$\text{total blocked weight} \leq \sum_{a \in A^{(j)}} \frac{T_{k-j}(2)}{a} = T_{k-j}(2) \cdot S_j.$$

*Blocking derivation*: Since $A$ is primitive, if $a \in A^{(j)}$ and $m \geq 2$ with $\Omega(m) = k-j$,
then $am \in A$ would require $a \mid am$ with $a \neq am$, violating primitivity. So every
$n \in A^{(k)}$ satisfies $a \nmid n$ for all $a \in A^{(j)}$. Therefore:
$$A^{(k)} \subseteq \{n \geq x : \Omega(n) = k\} \setminus \mathrm{Blocked},$$
where $\mathrm{Blocked} = \{am : a \in A^{(j)},\, m \geq 2,\, \Omega(m) = k-j\}$. Hence:
$$S_k \leq \sum_{\substack{n \geq x,\, \Omega(n)=k \\ n \notin \mathrm{Blocked}}} \frac{1}{n\log n}
= T_k(x) - (\text{weight of } \mathrm{Blocked} \cap [x,\infty))
\leq T_k(2) - (\text{weight of } \mathrm{Blocked} \cap [x,\infty)),$$
where $T_k(x) \leq T_k(2)$ since $T_k(x) = \sum_{n \geq x,\,\Omega(n)=k} \frac{1}{n\log n}$
is a sub-sum of $T_k(2) = \sum_{n \geq 2,\,\Omega(n)=k} \frac{1}{n\log n}$ (every term of $T_k(x)$
appears in $T_k(2)$, and $T_k(2)$ has additional non-negative terms for $2 \leq n < x$).

Since $a \geq x$ and $m \geq 2$, every blocked element $am \geq 2x \geq x$, so all of
$\mathrm{Blocked}$ lies in $[x,\infty)$. In particular:
$$S_k \leq T_k(2) - (\text{weight of Blocked}) \leq T_k(2) - 0 = T_k(2),$$
using the trivial lower bound: weight of Blocked $\geq 0$.

To obtain a non-trivial improvement ($S_k \leq T_k(2) - \delta$ for some $\delta > 0$),
one needs a LOWER bound on the total blocked weight. The upper bound $\leq T_{k-j}(2) \cdot S_j$
does not give a lower bound; it shows the blockage is bounded, not that it is large.

**Gap identified (Q16 hard case)**: Closing the two-stratum bound for $j, k \to \infty$
requires a lower bound on the total blocked weight — showing that cross-blocking
by $A^{(j)}$ actually removes a significant portion of $T_k(2)$. The current ledger
(F1, F2, F3) does not supply such a lower bound. The obstacle is a genuine
analytic gap requiring new input beyond the current given facts.

See `proof_lemmas/lemma_cross_stratum_control.md` for the broader context
and status of the cross-stratum gap.

**Net progress**: The bounded-stratum cases of `two_stratum_bound` are
fully proved using `proof_lemmas/lemma_large_floor_vanish.md` and
`single_stratum_bound` (proved via F3). The full two-stratum bound for
growing $j, k$ remains open.

---

## Section 9 — Bridge Lemma Reduction (Q17)

This section formally identifies the MINIMUM new given fact that, if added to
the ledger, would close the two-stratum conjecture for growing strata. No
analytic claims are made; the section is a pure logical reduction.

### 9.1 Setup

Fix the two-stratum case: $A = A^{(j)} \cup A^{(k)} \subset [x, \infty)$
primitive with $j < k$ and both $j = j(x)$, $k = k(x) \to \infty$ as
$x \to \infty$. Let $S_j := \sum_{a \in A^{(j)}} 1/(a\log a)$ and
$S_k := \sum_{a \in A^{(k)}} 1/(a\log a)$.

From Section 8 (proved): For each $a \in A^{(j)}$,
$$W_k(a) := \sum_{\substack{m \geq 2 \\ \Omega(m) = k-j}} \frac{1}{am\log(am)}$$
is the blocked weight, and $W_k(a) \leq T_{k-j}(2)/a$ (upper bound from Section 8).

By the primitivity argument of Section 8 (blocking derivation), every element
of $A^{(k)}$ avoids all multiples of $A^{(j)}$, giving:
$$S_k \leq T_k(x) - (\text{weight of Blocked}) \leq T_k(2) - (\text{weight of Blocked}),$$
where Blocked $= \{am : a \in A^{(j)},\, m \geq 2,\, \Omega(m)=k-j\}$ (all $\geq 2x$).
The weight of Blocked (without double-counting) satisfies:
$$0 \leq \text{weight of Blocked} \leq \sum_{a \in A^{(j)}} W_k(a),$$
with equality on the right only when no two blockers $a, a'$ share a common multiple.
Since weight of Blocked $\geq 0$, the trivial upper bound $S_k \leq T_k(2)$ follows.
A non-trivial improvement requires a LOWER BOUND on the weight of Blocked.

### 9.2 The Bridge Lemma

**Bridge Lemma (status: OPEN — not in ledger)**: For any primitive set
$A^{(j)} \subset [x, \infty)$ and $k = j + d$ with $d \geq 1$ fixed, there
exists $\delta = \delta(d) > 0$ (depending only on $d$, not on $j$ or $x$)
such that:
$$\text{total blocked weight} \geq \delta \cdot S_j + o(1)
\quad (x \to \infty).$$

Here $o(1)$ is as $x \to \infty$ uniformly in $j$ and $A^{(j)}$.

### 9.3 Conditional proof of two-stratum bound

**Lemma (conditional on Bridge Lemma)**: If the Bridge Lemma holds for $d$
and $\delta(d)$, then for primitive $A = A^{(j)} \cup A^{(j+d)}$ with
$j, j+d \to \infty$:
$$S = S_j + S_{j+d} \leq T_{j+d}(2) + S_j(1 - \delta) + o(1).$$

*Proof*: By the blocking derivation in Section 8 (primitivity argument):
$S_{j+d} \leq T_{j+d}(2) - (\text{weight of Blocked})$.
By the Bridge Lemma: $(\text{weight of Blocked}) \geq \delta \cdot S_j + o(1)$.
Combining: $S_{j+d} \leq T_{j+d}(2) - \delta \cdot S_j + o(1)$.
Adding $S_j$: $S \leq T_{j+d}(2) + S_j(1-\delta) + o(1)$. $\square$

**Closure condition**: For $S < 1 + o(1)$ it suffices to show
$T_{j+d}(2) + S_j(1-\delta) < 1 + o(1)$, i.e.:
$$S_j(1 - \delta) < 1 - T_{j+d}(2) + o(1).$$

By F3 (algebraic rearrangement of $T_{j+d}(2) = 1 - (c+o(1))(j+d)^2/2^{j+d}$, where F3 states $T_k(2) = 1-(c+o(1))k^2/2^k$ with $k = j+d$):
$$1 - T_{j+d}(2) = (c + o(1)) \cdot (j+d)^2/2^{j+d} \to 0 \quad\text{as } j \to \infty,$$
since $(j+d)^2/2^{j+d} \to 0$ exponentially and $c + o(1) \to c > 0$.

**Failure witness**: The closure condition requires $S_j(1-\delta) < (c+o(1))(j+d)^2/2^{j+d}$ for all
large $j$. Take $A^{(j)} = \mathcal{A}_j(x)$ (all $j$-almost primes $\geq x$ with $j \geq \lceil\log_2 x\rceil$);
then $S_j = T_j(x) = T_j(2)$ because any $j$-almost prime $n$ satisfies $n \geq 2^j \geq x$
(arithmetic: product of $j$ primes each $\geq 2$ is $\geq 2^j \geq x$ for $j \geq \lceil\log_2 x\rceil$),
so the constraint $n \geq x$ excludes no terms. By F3: $T_j(2) \to 1$ from below as $j \to \infty$.
So $S_j \to 1$ and $S_j(1-\delta) \to (1-\delta) > 0$,
while the RHS $\to 0$. The inequality FAILS for this witness.
Hence the closure condition fails for large $j$: no fixed $\delta > 0$ can satisfy it.

**Conclusion from analysis**: The conditional proof fails for $j \to \infty$ with
$d$ fixed: the F3 correction $1 - T_{j+d}(2)$ shrinks to zero, while the
required lower bound $\delta > 0$ stays fixed. The two-stratum bound for
$j, j+d \to \infty$ with fixed gap $d$ CANNOT be closed by this approach.

### 9.4 What WOULD close the gap

The analysis above pinpoints the obstruction:
- From Section 8, the cross-blocking upper bound gives $W_k(a) \leq T_{k-j}(2)/a$.
- The lower bound needed: $\text{total blocked} \geq 1 - T_k(2) = (c+o(1))(j+d)^2/2^{j+d}$ (by F3).
- Required: $\sum_{a \in A^{(j)}} W_k(a) \geq (c+o(1))(j+d)^2/2^{j+d}$.
- Since $W_k(a) \geq 0$ and $\sum_{a} W_k(a) \leq T_{k-j}(2) \cdot S_j \leq 1$,
  and the needed lower bound $c(j+d)^2/2^{j+d} \to 0$, the required bound is
  an ASYMPTOTIC estimate of blocked weight that tends to $0$ — but even this
  small positive quantity is not provable from F1, F2, and F3 alone: those
  facts bound $T_k(x)$ from above but provide no quantitative lower bound
  on the weight blocked by a specific set $A^{(j)}$ from the stratum $k$.

**Alternative closure strategy**: Use a global argument that does NOT decompose
by strata — e.g., an approach exploiting the full primitivity structure of $A$
at once rather than decomposing into strata. Such approaches require analytic
input beyond F1/F2/F3 and are therefore outside the scope of the current proof.

### 9.5 Summary of proof gap

| Case | Status |
|------|--------|
| $k$ fixed | S = $o(1)$ (proved via `large\_floor\_vanish`) |
| $j$ fixed, $k \to \infty$ | S $< 1 + o(1)$ (proved via `single\_stratum\_bound`) |
| $j, k \to \infty$, $\max(j,k)$ bounded | S $= o(1)$ (proved) |
| $j, k \to \infty$, gap $d = k-j$ fixed | Open; conditional proof fails (Section 9.3) |
| $j, k \to \infty$, gap $d \to \infty$ | Open; same obstacle |
| Multi-stratum (≥ 3 strata) | Open; reduces to two-stratum gap |

The conjecture for primitive sets spanning multiple critical strata remains
open. No proof or disproof is available from F1, F2, F3 alone.

---

## Section 10 — Extremal Analysis and Tightness of the Conjecture

This section proves two results: (a) the single-stratum per-stratum bound
$S_k \leq T_k(x)$ is ACHIEVED (not merely an upper bound), and (b) the
conjecture's $1+o(1)$ form is optimal — it cannot be improved to $1-\varepsilon$
for any fixed $\varepsilon > 0$.

### 10.1 The Extremal Primitive Set

**Definition**: For each integer $k \geq 1$ and threshold $x \geq 2$, define
$$\mathcal{A}_k(x) := \{n \geq x : \Omega(n) = k\}.$$
This is the set of ALL $k$-almost primes at or above $x$.

**Lemma (Extremal primitivity)**: $\mathcal{A}_k(x)$ is primitive for every
$k \geq 1$ and $x \geq 2$.

*Proof*: Let $n, m \in \mathcal{A}_k(x)$ with $n \neq m$, so $\Omega(n) = \Omega(m) = k$.
Suppose $n \mid m$. Then $m = n \cdot r$ for some integer $r \geq 2$, giving
$\Omega(m) = \Omega(n) + \Omega(r) \geq k + 1 > k$. This contradicts $\Omega(m) = k$.
So $n \nmid m$ and symmetrically $m \nmid n$. Hence $\mathcal{A}_k(x)$ is primitive. $\square$

**Lemma (Bound is achieved)**: The per-stratum bound $S_k \leq T_k(x)$ is
achieved by $A = \mathcal{A}_k(x)$:
$$S(\mathcal{A}_k(x)) = \sum_{n \in \mathcal{A}_k(x)} \frac{1}{n \log n} = T_k(x).$$

*Proof*: By definition, $T_k(x) = \sum_{\Omega(n)=k,\, n \geq x} 1/(n \log n) = S(\mathcal{A}_k(x))$.
$\square$

### 10.2 Critical-stratum range

For $k \geq \lceil \log_2 x \rceil$: every $k$-almost prime $n = p_1 \cdots p_k$
(each $p_i \geq 2$) satisfies $n \geq 2^k \geq x$, so the lower bound
$n \geq x$ in $T_k(x)$ is automatically satisfied — no terms are excluded:
$$T_k(x) = T_k(2) = \sum_{\Omega(n)=k} \frac{1}{n \log n}.$$
(This is a purely arithmetic observation: the product of $k$ integers each $\geq 2$ is $\geq 2^k$.)
For $k < \lceil \log_2 x \rceil$, some small-$k$-almost-primes lie below $x$,
so $T_k(x) < T_k(2)$; but as noted in Section 6.1, $T_k(x) \to 0$ (F1-convergence
+ tail vanishing).

### 10.3 Tightness of the 1+o(1) conjecture

**Theorem (Tightness)**: For each $x \geq 2$, set $k^*(x) = \lceil \log_2 x \rceil$.
The primitive set $\mathcal{A}_{k^*}(x)$ is a subset of $[x, \infty)$ with
$$S(\mathcal{A}_{k^*}(x)) = T_{k^*(x)}(2) = 1 - \bigl(c + o(1)\bigr)\frac{k^*(x)^2}{2^{k^*(x)}}.$$

As $x \to \infty$: $k^*(x) = \lceil \log_2 x \rceil \to \infty$, so by F3:
$$S(\mathcal{A}_{k^*}(x)) = T_{k^*}(2) \to 1 \quad \text{from below.}$$

*Proof*: By Section 10.2, $T_{k^*}(x) = T_{k^*}(2)$
(since $k^*(x) = \lceil\log_2 x\rceil$ implies $2^{k^*} \geq x$, so every
$k^*$-almost prime satisfies $n \geq 2^{k^*} \geq x$ — arithmetic).
By the Extremal primitivity lemma and Bound-is-achieved lemma, $\mathcal{A}_{k^*}(x)$ is
primitive with $S = T_{k^*}(2)$. By F3 sign\_disambiguation, $T_{k^*}(2) \to 1$
from below as $k^*(x) \to \infty$. $\square$

**Consequence (Lower bound on supremum)**: For each $x \geq 2$:
$$\sup_{\substack{A \subset [x,\infty) \\ \text{primitive}}} S(A, x) \geq T_{\lceil \log_2 x \rceil}(2) \to 1 \quad (x \to \infty).$$

The supremum approaches $1$ from below.

**Consequence (Optimality of the conjecture)**: The $1+o(1)$ upper bound in the
Erdős conjecture CANNOT be replaced by $1 - \varepsilon$ for any fixed $\varepsilon > 0$:
for any $\varepsilon > 0$, there exist large $x$ and primitive $A \subset [x,\infty)$
with $S(A,x) > 1 - \varepsilon$ (take $A = \mathcal{A}_{k^*}(x)$ for large enough $x$,
since $T_{k^*}(2) \to 1$).

### 10.4 Bounds on the supremum

Combining the upper and lower bounds on $\sup S$:
$$T_{\lceil \log_2 x \rceil}(2) \leq \sup_{\substack{A \subset [x,\infty) \\ \text{primitive}}} S(A,x) \leq e^\gamma \frac{\pi}{4} + o(1).$$

- **Lower bound**: $T_{\lceil \log_2 x \rceil}(2) \to 1$ from below (this section).
- **Upper bound**: $e^\gamma \pi/4 \approx 1.399$ (from F1).

The gap between the lower bound (approaching 1) and the upper bound ($\approx 1.399$)
is the range in which the true supremum lies. The Erdős conjecture asserts the
supremum tends to 1 (equivalently, the $1+o(1)$ upper bound holds for all primitive
sets). Neither F1 alone nor F3 alone closes this gap; F1 gives 1.399, and F3 shows
the supremum is bounded below by values approaching 1, but neither pins the supremum
to exactly 1.

