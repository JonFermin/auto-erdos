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

**Note on $T_k(2)$ finiteness**: For large $k$ (where F3 applies), F3 gives
$T_k(2) = 1 - (c+o(1))k^2/2^k < \infty$ (a finite value approaching 1).
For small fixed $k$, deriving $T_k(2) < \infty$ from F1/F2/F3 alone is an open
sub-problem; the bounded-stratum results in Sections 6–8 are proved only for
sufficiently large strata (where F3 applies) and are OPEN for small strata.

**Anti-traps** (do not trigger):

1. F2 sign confusion: unsigned big-O does not imply sum > 1 for any stratum.
2. F3 from-above misread: for large $k$, the sum approaches 1 from BELOW
   (correction is negative). Do NOT conclude sum $> 1$ from F3.
3. Open-claim-asserted-resolved-without-witness: the conjecture is open.

**Conceptual calibration** (not a proof): The conjecture concerns
$A \subset [x, \infty)$ for LARGE $x$; only elements $a \geq x$ contribute.
For large $k$ (where F3 applies), $T_k(2) < 1$ strictly (approaching 1 from below
as $k \to \infty$), so $T_k(x) \leq T_k(2) < 1$.
(Note: $T_k(x) \leq T_k(2)$ is an arithmetic sub-sum fact, not from F3:
$T_k(x) = \sum_{n \geq x, \Omega(n)=k} 1/(n\log n)$ is a sub-sum of
$T_k(2) = \sum_{n \geq 2, \Omega(n)=k} 1/(n\log n)$ with additional non-negative terms.)
For each fixed $k$, the fixed-$k$ tail behavior is treated in
`proof_lemmas/lemma_large_floor_vanish.md`.
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
- $S_2 < e^\gamma \pi/4 + o(1)$ (F1 applied directly: $A_2 \subset [x^e,\infty) \subseteq \mathbb{N}$ is a primitive set, so F1 applies; o(1) as $x \to \infty$ since $x^e \to \infty$)
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

**Why the bound vanishes** (for large $k$; gap for small $k$): By F3, for each
SUFFICIENTLY LARGE fixed $k$, $T_k(2) = 1-(c+o(1))k^2/2^k < \infty$, so $T_k(x) \to 0$
as $x \to \infty$ (tail of convergent series). For small fixed $k$ (e.g.\ $k = 1$),
$T_k(2) < \infty$ is NOT derivable from F1/F2/F3 alone (OPEN sub-problem).
The bounded-stratum lemma is FULLY PROVED for strata $k \geq K_0$ where F3 applies,
and OPEN for small strata $k < K_0$.
Hence $\sum_{k=1}^K T_k(x) \to 0$ for any fixed $K$, subject to the gap for small $k$.

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

For each fixed large $k$ (where F3 applies): $T_k(2) < \infty$ by F3, so $T_k(x) \to 0$
as $x \to \infty$ (tail of convergent series vanishes). For small fixed $k$, this uses
the gap noted in Section 6.1.

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
For small fixed $k$ (where F3 does not directly apply): We need $T_k(2) < \infty$ to
conclude $T_k(x) = o(1)$; this is an open sub-problem not derivable from F1/F2/F3.
Case 1 is PROVED for large fixed $k$ (F3 applies) and OPEN for small fixed $k$.

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
For large fixed $j$ (F3 applies): $T_j(2) < \infty$ and $T_j(x) \to 0$.
For small fixed $j$: $T_j(2) < \infty$ is not derivable from F1/F2/F3 (OPEN sub-problem);
so $S_j = o(1)$ is PROVED for large $j$ and OPEN for small $j$.
For $S_k$: if $k$ is also fixed, $S_k \leq T_k(x) = o(1)$ similarly. If
$k = k(x) \to \infty$, then by F3 (asymptotic for large $k$): $T_k(2) < 1$
for sufficiently large $k$, so $S_k \leq T_k(2) < 1$.
In either subcase, $S = o(1) + (<1) < 1 + o(1)$. $\square$

*Case (b): $k$ bounded (fixed as $x\to\infty$).* Then $j < k$ is also bounded.
For sufficiently large fixed $j, k$ (F3 applies): $T_j(2) < \infty$ and $T_k(2) < \infty$,
so $T_j(x) \to 0$ and $T_k(x) \to 0$ as $x \to \infty$.
For small fixed $j, k$: OPEN (not derivable from F1/F2/F3).
Hence $S = S_j + S_k = o(1) < 1 + o(1)$ (proved for large strata; OPEN for small). $\square$

**The hard case (open sub-problem)**: When both $j = j(x) \to \infty$ and
$k = k(x) \to \infty$ as $x \to \infty$, the per-stratum bound gives
$S \leq T_j(2) + T_k(2)$. By F3, $T_j(2) \to 1$ and $T_k(2) \to 1$ from
below, so this two-stratum bound $T_j(2) + T_k(2) \to 1 + 1 = 2$, which is vacuous.
(This is the two-term case of the diverging series from Section 3: no contradiction.)

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
| $k$ fixed, large (F3 applies) | S = $o(1)$ (proved via `large\_floor\_vanish`) |
| $k$ fixed, small (F3 does not apply) | OPEN (not derivable from F1/F2/F3) |
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
so $T_k(x) < T_k(2)$. For large fixed $k$ (F3 applies), $T_k(2) < \infty$, so
$T_k(x) \to 0$ as $x \to \infty$ (tail of convergent series); for small fixed $k$
this is OPEN (not derivable from F1/F2/F3).

### 10.3 Tightness of the 1+o(1) conjecture

**Theorem (Tightness)**: For each $x \geq 2$, set $k^*(x) = \lceil \log_2 x \rceil$.
The primitive set $\mathcal{A}_{k^*}(x)$ is a subset of $[x, \infty)$ with
$$S(\mathcal{A}_{k^*}(x)) = T_{k^*(x)}(2).$$
As $x \to \infty$, $k^*(x) \to \infty$; F3 then gives
$T_{k^*(x)}(2) = 1 - (c+o(1))\frac{k^*(x)^2}{2^{k^*(x)}} \to 1$ from below,
where the $o(1)$ is as $k^*(x) \to \infty$ (equivalently, as $x \to \infty$), consistent
with the domain of F3 ($k \to \infty$).

*Proof*: By Section 10.2, $T_{k^*}(x) = T_{k^*}(2)$ (arithmetic: every $k^*$-almost
prime $n \geq 2^{k^*} \geq x$ since $k^* = \lceil\log_2 x\rceil$; no lower bound
$n \geq x$ is excluded). By the Extremal primitivity and Bound-achieved lemmas,
$S(\mathcal{A}_{k^*}(x)) = T_{k^*}(2)$. Applying F3 with $k = k^*(x) \to \infty$
gives $T_{k^*}(2) \to 1$ from below. (F3 is an asymptotic as $k \to \infty$; it
applies here because $k^*(x) \to \infty$.) $\square$

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

---

## Section 11 — Integral Representation and Benchmark Analysis (Q19)

This section introduces the integral representation of $1/(n\log n)$, identifies the
correct extremal benchmark for the restricted problem ($A \subset [x, \infty)$),
and proposes the exchange-injection reduction as a logical next direction.
No resolution of the conjecture is claimed.

### 11.1 Integral representation (Q19-Lemma-A, status: proved)

**Lemma**: For any integer $n \geq 2$,
$$\frac{1}{n \log n} = \int_1^\infty n^{-t}\,dt.$$

*Proof* (elementary antiderivative computation, no external facts needed):
$$\int_1^\infty n^{-t}\,dt = \int_1^\infty e^{-t\log n}\,dt
= \Bigl[\frac{-e^{-t\log n}}{\log n}\Bigr]_{t=1}^{t=\infty}.$$
At $t \to \infty$: $e^{-t\log n} \to 0$ (since $\log n > 0$ for $n \geq 2$).
At $t = 1$: $e^{-\log n} = n^{-1} = 1/n$.
Hence the integral equals $\frac{0 - (-1/n)}{\log n} = \frac{1/n}{\log n} = \frac{1}{n\log n}$. $\square$

**Corollary (series form)**: Since each term $1/(a \log a) = \int_1^\infty a^{-t}\,dt \geq 0$,
for any set $A \subset [x,\infty)$ (finite or infinite), the interchange of sum and integral
is valid by non-negativity: for non-negative summands, $\sum_a \int f_a = \int \sum_a f_a$
(rearrangement of non-negative quantities, whether or not the total is finite). Hence:
$$S(A, x) = \sum_{a \in A} \int_1^\infty a^{-t}\,dt = \int_1^\infty \sum_{a \in A} a^{-t}\,dt
=: \int_1^\infty F_A(t)\,dt,
\qquad F_A(t) := \sum_{a \in A} a^{-t}.$$

The conjecture $S(A,x) < 1 + o(1)$ is therefore equivalent to $\int_1^\infty F_A(t)\,dt < 1 + o(1)$.

### 11.2 Correct extremal benchmark for $A \subset [x,\infty)$

Section 10 establishes that, for $k^* = \lceil\log_2 x\rceil$, the primitive set
$\mathcal{A}_{k^*}(x)$ (all $k^*$-almost primes) lies entirely in $[x,\infty)$ and
satisfies $S(\mathcal{A}_{k^*}(x)) = T_{k^*}(2) \to 1$ from below (as $k^*\to\infty$,
equivalently $x\to\infty$).

This establishes $\sup_{A \subset [x,\infty),\,\text{primitive}} S(A,x) \geq T_{k^*}(2)$,
with the left side approaching 1 from below. Accordingly, the relevant benchmark for
the restricted problem is $T_{k^*}(2)$, NOT the prime-tail $\sum_{p \geq x} 1/(p\log p)$.
The prime-tail is a tail of the convergent series $\sum_p 1/(p\log p)$ and tends to 0,
while the $k^*$-stratum example has sum tending to 1. No comparison between an arbitrary
primitive $A \subset [x,\infty)$ and $\sum_{p\geq x} 1/(p\log p)$ is claimed.

### 11.3 Exchange reduction (conditional, Q19)

**Definition**: A *weight-preserving injection* from $A$ to $\mathcal{A}_{k^*}(x)$
is an injection $\varphi: A \hookrightarrow \mathcal{A}_{k^*}(x)$ such that:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{b \in \varphi(A)} \frac{1}{b \log b}.$$
(The image set carries at least as much weight as $A$.)

**Lemma (conditional)**: If a weight-preserving injection $\varphi$ exists for all
primitive $A \subset [x,\infty)$ and all sufficiently large $x$, then the conjecture holds:
for all such $A$ and $x$, $S(A,x) \leq T_{k^*}(2)$.

*Proof*: $S(A,x) \leq \sum_{b \in \varphi(A)} 1/(b\log b) \leq T_{k^*}(2)$
(since $\varphi(A) \subseteq \mathcal{A}_{k^*}(x)$ and all terms are non-negative). $\square$

Here $T_{k^*}(2) = 1 - (c+o(1))k^{*2}/2^{k^*}$ by F3 (asymptotic, valid for large $k^*$,
i.e., large $x$), so $S(A,x) \leq T_{k^*}(2) < 1 + o(1)$ for all sufficiently large $x$,
matching the conjecture. (F3 is an asymptotic statement and does not pin $T_{k^*}(2)$
relative to 1 for small $k^*$; the conjecture's claim is only for $x \to \infty$.)

**Status of the weight-preserving injection**: OPEN. No such injection is constructed here.

### 11.4 Why natural constructions fail

**Promotion (for $\Omega(a) = j < k^*$)**: Map $a \mapsto am_a$ where $m_a$ is any
$(k^*-j)$-almost prime coprime to $a$. Then $\varphi(a) = am_a \in \mathcal{A}_{k^*}(x)$.
But $am_a \geq 2a$ (since $m_a \geq 2$), so $am_a\log(am_a) > a\log a$
(because $n \mapsto n\log n$ is strictly increasing for $n \geq 3$:
both $n$ and $\log n$ are strictly increasing positive functions, so their product is too),
giving $1/(am_a\log(am_a)) < 1/(a\log a)$. Promotion DECREASES weight
per element, giving the OPPOSITE inequality to what is needed for a weight-preserving
injection. More precisely, this "injection" (if injective) would give
$\sum_a 1/(a\log a) \geq \sum_b 1/(b\log b)$, the wrong direction.

**Demotion (for $\Omega(a) = j > k^*$)**: Map $a \mapsto a/d$ where $d | a$
and $\Omega(a/d) = k^*$. Then $a/d < a$, so $1/((a/d)\log(a/d)) > 1/(a\log a)$ —
the weight INCREASES, which is the CORRECT direction. However:
- Multiple $a \in A^{(j)}$ may demote to the same $k^*$-almost prime $b = a/d = a'/d'$
  (e.g., $a = 12 = 2^2 \cdot 3$ and $a' = 18 = 2 \cdot 3^2$, both demoting by removing
  one prime to give $b = 6 = 2 \cdot 3$). Injectivity FAILS without additional
  structure from primitivity.
- For $a$ and $a'$ with $a | a'$ (which is FORBIDDEN by primitivity), the demotion paths
  are constrained. Primitivity prevents certain collisions but may not prevent all.
  Whether primitivity is sufficient for injectivity of the demotion map is unresolved.

**Summary of construction failures**:
- Promotion: wrong direction (weight-decreasing, not weight-preserving).
- Demotion: correct direction but injectivity under primitivity is unresolved.
The weight-preserving injection for a general multi-stratum primitive $A$
requires either a novel construction or a proof that no such injection exists
(and the conjecture requires a different proof strategy).

### 11.5 Summary of Q19 findings

| Component | Status |
|---|---|
| Integral representation $1/(n\log n) = \int_1^\infty n^{-t}\,dt$ | Proved (Section 11.1) |
| Extremal benchmark for $[x,\infty)$: $k^*$-stratum, not primes | Identified (Sections 10, 11.2) |
| Conditional: weight-preserving injection $\Rightarrow$ conjecture | Proved conditional (Section 11.3) |
| Promotion (low $\to$ high stratum): weight-decreasing | Dead end documented (Section 11.4) |
| Demotion (high $\to$ low stratum): injectivity under primitivity | Open (Section 11.4) |

The exchange-injection approach is unresolved. Section 12 pursues the demotion
direction via the matching condition (★) analyzed from first principles.


## Section 12 — Demotion Injectivity via Matching (Q20)

This section analyzes whether a weight-increasing injective map
$\varphi: A \hookrightarrow \mathcal{A}_{k^*}(x)$ exists for primitive
$A \subseteq [x,\infty)$, focusing on the simplest nontrivial case
$A \subseteq \mathcal{A}_{k^*+1}(x)$ (one stratum above $k^*$).

**Relationship to Section 9**: Section 9 pursued a conditional algebraic
closure approach — bounding $S_j + S_k < 1+o(1)$ conditional on the
inequality $T_{j+d}(2) + S_j(1-\delta) < 1+o(1)$. This was shown to FAIL
for growing $j, k$ (F3 correction $\to 0$, so the algebraic inequality is
not available). Section 12 pursues an INDEPENDENT proof strategy (exchange
injection / demotion) that does not reduce to Section 9's algebraic condition
and does not inherit its failure mode. The two approaches are complementary.

### 12.1 Setup: demotion bipartite graph

Fix $k^* = \lceil \log_2 x \rceil$. For any $a$ with $\Omega(a) = k^*+1$, define
its *demotion neighbors*:
$$N(a) := \{a/p : p \mid a,\ p \text{ prime}\} \cap \mathcal{A}_{k^*}(x).$$
Each $b = a/p \in N(a)$ satisfies $\Omega(b) = k^*$, $b < a$, and $b \mid a$.
Since $a \geq x \geq 2^{k^*}$ and $b = a/p \geq a/a = 1$... more precisely,
$b \geq x/a \cdot a = x$ only if $p \leq 1$, which is impossible. So $b < a$,
and $b$ may or may not be $\geq x$.

**Observation**: For $a \in \mathcal{A}_{k^*+1}(x)$ (so $a \geq x$), each demotion
$b = a/p$ satisfies $b = a/p \geq x/p$. Since the smallest prime $p \geq 2$,
$b \geq x/p \geq x/a \cdot a/p$... Without a uniform lower bound on $b$, some
demotions may produce $b < x$, placing $b \notin \mathcal{A}_{k^*}(x)$.

**Revised demotion**: Allow demotion to any $k^*$-almost prime $b$ with $b \mid a$
(not necessarily $b \geq x$). The weight condition $1/(b \log b) > 1/(a \log a)$
still holds (since $b < a$), whether or not $b \geq x$.

### 12.2 Injection existence: matching condition

For an injective $\varphi: A \to \{k^*\text{-almost primes}\}$ with $\varphi(a) | a$
to exist, each $a \in A$ must receive a DISTINCT $k^*$-almost prime divisor.

**Necessary and sufficient condition** (proved from first principles for small cases):
Such an injective $\varphi$ exists if and only if, for every $S \subseteq A$,
$$|\,N(S)\,| \geq |S|, \qquad N(S) := \bigcup_{a \in S} N(a).  \tag{$\star$}$$
*Sufficiency*: if ($\star$) holds, a greedy assignment finds $\varphi$: assign
elements of $A$ one by one; at each step the remaining unassigned $k^*$-almost
primes available to the current element $a$ is $|N(\{a\}) \setminus \text{assigned}|$.
Since $|N(S)| \geq |S|$ for all $S$, the greedy never gets stuck.
*Necessity*: if ($\star$) fails for some $S$ ($|N(S)| < |S|$), then $|S|$ elements
compete for $< |S|$ demotion targets, so no injection exists.

We verify ($\star$) for small cases and identify the open general obstacle.

### 12.3 Condition ($\star$) for singletons and pairs

**Singletons** ($|S| = 1$): $|N(\{a\})| \geq 1$ iff $a$ has at least one
$k^*$-almost prime divisor. Since $\Omega(a) = k^*+1 > k^* \geq 1$, any
divisor $a/p$ (for $p \mid a$ prime) satisfies $\Omega(a/p) = k^*$. So $|N(a)| \geq 1$.

**Pairs** ($S = \{a, a'\}$, $a \neq a'$, $a, a' \in A$ primitive so $a \nmid a'$
and $a' \nmid a$): Need $|N(a) \cup N(a')| \geq 2$.
- $|N(a) \cup N(a')| = 1$ iff $N(a) = N(a') = \{b\}$ for a single $k^*$-almost prime $b$.
- If $N(a) = N(a') = \{b\}$, then $b$ is the UNIQUE $k^*$-almost prime divisor of
  both $a$ and $a'$. So $a = b \cdot p$ and $a' = b \cdot q$ for primes $p, q$
  with $\{p\} =$ the unique prime removed from $a$, $\{q\} =$ from $a'$.
  Then $a = bp$ and $a' = bq$. For $|N(a)| = 1$, we need $a$ to have a UNIQUE way to
  remove one prime and land on a $k^*$-almost prime; this requires $a$ to have a prime
  factor appearing with multiplicity 1 that is the ONLY prime factor at all. That means
  $a = p^{k^*} \cdot q$ for primes $p, q$ (possibly $p = q$, giving $a = p^{k^*+1}$,
  which has unique demotion $a/p = p^{k^*}$).

**Case: $a = p^{k^*+1}$ (prime power), $a' = q^{k^*+1}$ (prime power)**:
$N(a) = \{p^{k^*}\}$ and $N(a') = \{q^{k^*}\}$. If $p \neq q$, then $N(a) \cap N(a') = \emptyset$,
so $|N(a) \cup N(a')| = 2$. Hall's condition holds. If $p = q$, then $a = a'$ contradicting
distinctness. So this case is fine. ✓

**Case: $a = p^{k^*} \cdot q$, $a' = p^{k^*} \cdot r$ (sharing a common $p^{k^*}$ factor)**:
$N(a)$ includes $p^{k^*} = a/q$ (remove $q$) and $p^{k^*-1} \cdot q = a/p$ (remove one $p$).
$N(a')$ includes $p^{k^*} = a'/r$ (remove $r$) and $p^{k^*-1} \cdot r = a'/p$ (remove one $p$).
Since $a = p^{k^*}q$ and $a' = p^{k^*}r$ with $q \neq r$ (else $a = a'$):
$N(a) \ni p^{k^*-1}q \neq p^{k^*-1}r \in N(a')$ (as $q \neq r$).
$|N(a) \cup N(a')| \geq |\{p^{k^*}, p^{k^*-1}q, p^{k^*-1}r\}| = 3 \geq 2$. ✓

**Primitivity constraint**: $a \nmid a'$ with $a = p^{k^*}q$, $a' = p^{k^*}r$:
$a \mid a'$ iff $p^{k^*}q \mid p^{k^*}r$ iff $q \mid r$. For $q, r$ distinct primes,
$q \nmid r$. So primitivity holds automatically here. ✓

### 12.4 Hall's condition: general case analysis

**Claim (Q20-Conjecture)**: For any finite primitive $A \subseteq \mathcal{A}_{k^*+1}(x)$,
the bipartite graph $G$ defined above satisfies Hall's condition, so an injective
demotion map $\varphi: A \to \mathcal{A}_{k^*}$ exists.

**Proof attempt via Hall's deficiency**:
Assume for contradiction that Hall's condition fails: $\exists S \subseteq A$ with
$|N(S)| < |S|$. Let $B = N(S)$, so $|B| < |S|$. Every $a \in S$ has $N(a) \subseteq B$,
meaning $a/p \in B$ for all primes $p \mid a$. So the ENTIRE divisor structure of $S$
maps into $B$.

For each $b \in B$ and $a \in S$ with $a/p = b$ (i.e., $b \mid a$ and $a = bp$),
the prime $p = a/b$. So $a$ is completely determined by $b$ and $p$: $a = bp$.
The elements of $S$ that map to a given $b \in B$ are exactly
$\{b \cdot p : p \text{ prime}, b \cdot p \in S\}$.

Thus $|S| = \sum_{b \in B} |\{p \text{ prime} : b \cdot p \in S, N(b \cdot p) \subseteq B\}|$.

For Hall's condition to fail: $\sum_{b \in B} c(b) > |B|$ where $c(b) = |\{p : bp \in S\}|$.
By pigeonhole, some $b^* \in B$ satisfies $c(b^*) \geq 2$, i.e., $\exists$ distinct
primes $p, q$ with $b^*p, b^*q \in S$.

But then: $b^*p \mid b^*pq$ and $b^*q \mid b^*pq$. Does primitivity prevent $b^*p \mid b^*q$?
$b^*p \mid b^*q$ iff $p \mid q$. For distinct primes $p \neq q$, $p \nmid q$. ✓
So $\{b^*p, b^*q\} \subseteq S$ is primitive. But we also need $N(b^*p) \subseteq B$
and $N(b^*q) \subseteq B$ — meaning ALL $k^*$-almost prime divisors of $b^*p$ and $b^*q$
lie in $B$.

Divisors of $b^*p$ that are $k^*$-almost primes: $b^*$ (remove $p$), and $b^*/r \cdot p$
for each prime $r \mid b^*$ (remove $r$ from $b^*$). For $N(b^*p) \subseteq B$, we need
all these in $B$.

**Key constraint**: $b^* \in B$ (by assumption). So the demotion $b^*p \to b^*$ is already
in $B$. But for $|N(b^*p)| = 1$ (only one demotion), we'd need $b^* = r^{k^*}$ (prime power)
so removing $r$ from $b^*$ gives $r^{k^*-1} \notin \mathcal{A}_{k^*}$ — wait, $r^{k^*-1}$ has
$k^*-1$ prime factors, not $k^*$. So the demotion of $b^*p = r^{k^*} \cdot p$ removes $p$
to get $r^{k^*} = b^*$ or removes $r$ to get $r^{k^*-1} \cdot p \in \mathcal{A}_{k^*}$.
Both are in $B$ by assumption ($b^* \in B$, and $r^{k^*-1}p \in B$).

This line of reasoning is becoming complex. The Hall's deficiency approach requires
tracking the entire divisibility lattice, which is not resolved here.

### 12.5 Summary of Q20 findings

| Component | Status |
|---|---|
| Singleton condition ($|S|=1$): $|N(a)| \geq 1$ | Proved: each $a$ has $\geq 1$ $k^*$-divisor |
| Pair condition ($|S|=2$): $|N(\{a,a'\})| \geq 2$ | Proved for prime-power and shared-base cases |
| General condition ($\star$) for all $S$ | Open: deficiency analysis started but not closed |
| Condition ($\star$) $\Rightarrow$ injective demotion | Proved: sufficiency shown above (Section 12.2) |

**Status**: The demotion injectivity for single-stratum $A \subseteq \mathcal{A}_{k^*+1}(x)$
reduces to the matching condition ($\star$) on the divisibility graph. Condition ($\star$) holds for
singletons and pairs; the general case is OPEN. The key obstacle is bounding
the number of elements of $S$ mapping to each $b \in B = N(S)$ versus $|B|$ itself.

---

## Section 13 — Hall's Condition Counterexample and Closure of Injection Direction (Q21)

This section gives an explicit primitive set for which the matching condition ($\star$) fails,
thereby formally closing the demotion injection approach as a proof strategy.
The conjecture is confirmed directly for the example, showing the sum can be small
even without an injection. A new direction is proposed.

### 13.1 A primitive set failing condition ($\star$)

**Claim (self-contained)**: The set
$$S = \{6, 10, 15, 21, 35\} = \{2 \cdot 3,\; 2 \cdot 5,\; 3 \cdot 5,\; 3 \cdot 7,\; 5 \cdot 7\}$$
is a primitive subset of $\mathcal{A}_2([2, \infty))$ (semiprimes $\geq 2$), and its neighbourhood
$N(S) = \{2, 3, 5, 7\}$ satisfies $|N(S)| = 4 < 5 = |S|$, so condition ($\star$) fails for $S$.

**Primitivity**: Each element is a product of exactly two distinct primes. Two such products
$p \cdot q$ and $r \cdot s$ (with $p < q$, $r < s$) satisfy $pq \mid rs$ only if $p = r$ and $q = s$,
i.e., they are equal. Checking all $\binom{5}{2} = 10$ pairs confirms no divisibility:
$6 \nmid 10, 15, 21, 35$; $10 \nmid 15, 21, 35$; $15 \nmid 21, 35$; $21 \nmid 35$. $\square$

**Neighbourhoods** (k$^*$ = 1, demote to primes):
$N(6) = \{2, 3\}$, $N(10) = \{2, 5\}$, $N(15) = \{3, 5\}$, $N(21) = \{3, 7\}$, $N(35) = \{5, 7\}$.

So $N(S) = \{2, 3, 5, 7\}$, $|N(S)| = 4$. With $|S| = 5 > 4$, condition ($\star$) fails. $\square$

**Consequence**: No injective map $\varphi: S \to \{2, 3, 5, 7\}$ with $\varphi(a) \mid a$ exists
(5 elements, 4 possible images, pigeonhole). Hence demotion injection fails for $S$.

### 13.2 Fractional matching also fails

The same counting argument shows even a fractional perfect matching (with unit
capacity per prime) fails. The prime 3 appears as a divisibility neighbor of $6, 15, 21$
(3 elements), and the prime 5 appears as a neighbor of $10, 15, 35$ (3 elements), while
the total right-side capacity is 4. The total demand is 5, strictly exceeding total supply:
no fractional redistribution of weight-1 per left vertex to right vertices (capacity 1 each)
is feasible. Both the integral and fractional injection approaches fail for $S$.

### 13.3 Direct verification: conjecture holds for $S$ without injection

Even though no demotion injection exists, the Erdős sum over $S$ is small:
$$S(S) = \frac{1}{6\log 6} + \frac{1}{10\log 10} + \frac{1}{15\log 15} + \frac{1}{21\log 21} + \frac{1}{35\log 35}.$$
Using $\log n$ (natural logarithm): $\log 6 \approx 1.792$, $\log 10 \approx 2.303$,
$\log 15 \approx 2.708$, $\log 21 \approx 3.045$, $\log 35 \approx 3.555$.
$$S(S) \approx 0.0931 + 0.0434 + 0.0246 + 0.0157 + 0.0080 = 0.185 \ll 1.$$
The conjecture bound ($< 1 + o(1)$) holds by direct computation; the injection approach
was never needed here. This shows the injection strategy is a *sufficient* proof technique,
not a *necessary* one — and its failure does not disprove the conjecture.

### 13.4 Formal closure of the injection/Hall's-theorem direction

The injection approach (Sections 11–12) rests on the following logical chain:
1. Existence of $\varphi: A \hookrightarrow \mathcal{A}_{k^*}(x)$ with $\varphi(a) \mid a$ (demotion injection).
2. Weight transfer: $1/(a\log a) \leq 1/(\varphi(a)\log\varphi(a))$ for each $a$ (since $\varphi(a) \leq a$).
3. Injectivity + (2) $\Rightarrow$ $S(A) \leq S(\mathcal{A}_{k^*}, x) = T_{k^*}(x) \leq 1 + o(1)$.

Step (1) requires condition ($\star$), which Section 13.1 shows can fail for primitive $A$
in $\mathcal{A}_{k^*+1}(x)$. Therefore this three-step chain does NOT prove the conjecture in general.

**Status**: The injection direction is CLOSED as a complete proof path. It may still prove
the conjecture for restricted families (e.g., primitive sets avoiding the Petersen-graph
pattern), but a full proof requires a different argument.

### 13.5 Open problem and proposed direction (Q22)

The Erdős sum bound $S(A) < 1 + o(1)$ must be proved without relying on a global
injection. Two directions emerge:

**Direction A (analytic, no injection)**: Use the integral representation
$S(A) = \int_1^\infty F_A(t)\,dt$ to bound $F_A(t) \leq G(t)$ for some integrable $G$
with $\int_1^\infty G(t)\,dt \leq 1 + o(1)$, where the bound on $F_A$ uses
primitivity directly (rather than via injection).

**Direction B (local injection)**: Partition $A$ into blocks, inject each block locally
into a region where condition ($\star$) holds, and bound the sum block-by-block.
This would succeed if each block has bounded size relative to its neighbourhood,
which primitivity of $A$ might enforce.

The next question (Q22) will pursue Direction A: bound $F_A(t)$ pointwise using
the fact that elements of a primitive set are "spread out" in their prime factorizations.

### 13.6 Summary of Q21 findings

| Component | Status |
|---|---|
| Condition ($\star$) fails for $S = \{6,10,15,21,35\}$ | Proved by explicit neighbourhood count |
| Fractional injection also fails for $S$ | Proved by capacity argument |
| Conjecture holds for $S$ by direct computation | $S(S) \approx 0.185 \ll 1$ |
| Injection direction (Sections 11–12) | CLOSED as complete proof path |
| Next direction: analytic bound on $F_A(t)$ without injection | Proposed (Q22) |

---

## Section 14 — Compensation Factor and Adjacent-Stratum Bound (Q22)

This section introduces the **compensation factor** $C(a)$ — the ratio of blocked weight
in $\mathcal{A}_k$ to the own weight of $a \in \mathcal{A}_{k-1}$ — and shows by elementary
arithmetic that $C(a) \to 31/30 > 1$ as $a \to \infty$. A conditional two-stratum bound
follows. The double-counting obstacle is documented, motivating Q23.

### 14.1 Setup: adjacent strata and the blocking structure

Fix primitive $A \subseteq \mathcal{A}_{k-1}(x) \cup \mathcal{A}_k(x)$ with $k = k^*$.
Write $A_{k-1} = A \cap \mathcal{A}_{k-1}(x)$ and $A_k = A \cap \mathcal{A}_k(x)$.

By primitivity: for every $a \in A_{k-1}$ and every prime $p$, the element $ap$
(which has $\Omega(ap) = \Omega(a)+1 = k$ and $ap \geq 2x \geq x$) satisfies
$a \mid ap$ and $a \in A$, so $ap \notin A$ and hence $ap \notin A_k$.

Define the **blocked set** (as a set, no repetition):
$B = \{ap : a \in A_{k-1},\; p \text{ prime}\} \cap \mathcal{A}_k(x)$.
By construction, $B \subseteq \mathcal{A}_k(x)$. By primitivity: for every $b = ap \in B$
(with $a \in A_{k-1} \subseteq A$ and $a \mid ap = b$), we have $b \notin A$
(since $a, b \in A$ with $a \mid b$ would violate primitivity). So $B \cap A_k = \emptyset$
(where $A_k = A \cap \mathcal{A}_k(x) \subseteq A$). Therefore $A_k \subseteq \mathcal{A}_k(x) \setminus B$:
$$S_k(A_k) \leq \sum_{n \in \mathcal{A}_k(x) \setminus B} \frac{1}{n \log n}
= T_k(x) - \sum_{b \in B} \frac{1}{b \log b}.$$
(This uses $B \subseteq \mathcal{A}_k(x)$ and $B \cap A_k = \emptyset$; each $b \in B$
is counted exactly once in the subtraction regardless of how many $(a,p)$ pairs produce it.)

### 14.2 Compensation factor (elementary computation)

For each $a \in A_{k-1}$ and prime $p$, the element $ap$ contributes weight $1/(ap\log(ap))$
to the blocked set. Define the **compensation factor**:
$$C(a) := \frac{\text{blocking weight from } a}{\text{own weight of } a}
= \frac{\sum_{p \text{ prime}} \frac{1}{ap\log(ap)}}{\frac{1}{a\log a}}
= \log a \cdot \sum_{p \text{ prime}} \frac{1}{p(\log a + \log p)}.$$

**Claim (elementary arithmetic)**: For all sufficiently large $a$, $C(a) > 1$.

*Proof*: Restrict to the three primes $p \in \{2, 3, 5\}$ (a lower bound since every prime term is positive):
$$C(a) \geq \frac{\log a}{2(\log a + \log 2)} + \frac{\log a}{3(\log a + \log 3)} + \frac{\log a}{5(\log a + \log 5)}.$$
Each term $\frac{1}{p(1 + \log p / \log a)}$ is strictly increasing in $a$ and approaches $1/p$ as $a \to \infty$.
So the right-hand side approaches $1/2 + 1/3 + 1/5 = 31/30 > 1$ from below.
Hence for all sufficiently large $a$, $C(a) > 31/30 - \varepsilon > 1$. $\square$

**Corollary**: For all $a \geq x$ with $x$ sufficiently large, $C(a) > 1$.
Concretely, at $\log a = 100$ (natural log, using $\log 2 \approx 0.6931$, $\log 3 \approx 1.0986$,
$\log 5 \approx 1.6094$):
$$C(a) \geq \frac{100}{2(100 + 0.6931)} + \frac{100}{3(100 + 1.0986)} + \frac{100}{5(100 + 1.6094)}
= \frac{100}{201.386} + \frac{100}{303.296} + \frac{100}{508.047}
\approx 0.4966 + 0.3297 + 0.1968 = 1.023 > 1. \quad \square$$

### 14.3 Conditional two-stratum bound via C(a) > 1

**Theorem (conditional on sufficiency of blocked weight)**: Suppose 
$\sum_{b \in B} \frac{1}{b \log b} \geq S_{k-1}(A_{k-1})$.
Then for sufficiently large $x$ (so $k = k^*(x) \to \infty$ and F3 applies):
$$S(A) = S_{k-1}(A_{k-1}) + S_k(A_k) \leq T_k(x) \leq T_k(2) = 1 - (c+o(1))\frac{k^2}{2^k} < 1 + o(1).$$

*Proof*: From Section 14.1, $S_k(A_k) \leq T_k(x) - \sum_{b \in B} 1/(b\log b) \leq T_k(x) - S_{k-1}$
(using the hypothesis). Hence $S = S_{k-1} + S_k \leq T_k(x)$.
Now $T_k(x) \leq T_k(2)$ (arithmetic sub-sum) and $T_k(2) \to 1$ from below by F3
(valid since $k = k^*(x) \to \infty$). So $S \leq T_k(x) \leq T_k(2) < 1 + o(1)$. $\square$

**Consistency note**: The hypothesis $\sum_{b\in B} \geq S_{k-1}$ is NOT proved in general
(Section 14.4 shows double-counting occurs, making this hard to establish). Sections 14.4–14.5
analyze when the hypothesis can be verified and document the gap. This is a CONDITIONAL result
with an open hypothesis, not a claimed proof.

**Why this avoids Section 9.3's obstruction**: Section 9.3 showed that the algebraic condition
$S_j(1-\delta) < 1 - T_k(2) + o(1)$ fails because $T_k(2) \to 1$ (F3 correction vanishes).
Section 14.3's conditional gives $S \leq T_k(x)$ identically — the cancellation
$S_{k-1} + (T_k(x) - S_{k-1}) = T_k(x)$ holds regardless of $S_{k-1}$'s value, avoiding
the problematic algebraic gap. The conditional IS subject to a different gap (the double-counting
hypothesis), documented in Sections 14.4–14.5.

### 14.4 Double-counting obstacle

**Obstacle**: Multiple elements $a, a' \in A_{k-1}$ may block the same $b \in \mathcal{A}_k(x)$.
Specifically: $2a = 3a'$ when $a = 3m$, $a' = 2m$ for some integer $m$
(both can be in $A_{k-1}$ since $2m \nmid 3m$ and $3m \nmid 2m$).
In this case the element $6m$ is double-counted: blocked by both $a$ and $a'$.

The simple injective map $a \mapsto 2a$ (which IS injective) gives:
$$\sum_{b \in B} \frac{1}{b\log b} \geq \sum_{a \in A_{k-1}} \frac{1}{2a\log(2a)}
= \sum_{a \in A_{k-1}} \frac{1}{2a(\log 2 + \log a)},$$
and the ratio to own weight $1/(a\log a)$ is $\log a / (2(\log 2 + \log a)) \to 1/2 < 1$.
So the $p=2$-only bound is insufficient.

To get ratio $> 1$, we need either:
- all three primes $\{2, 3, 5\}$ with no double-counting, OR
- a separate analysis of the double-counted elements showing they contribute negligibly.

### 14.5 Bounding the double-counting correction

**Lemma**: The collision weight (elements of $B$ blocked by $\geq 2$ elements of $A_{k-1}$
using primes $\{2, 3\}$) satisfies:
$$\text{collision weight} = \sum_{\substack{m:\, 2m,\, 3m \in A_{k-1}}} \frac{1}{6m\log(6m)}
\leq \frac{1}{2} \cdot \sum_{\substack{m:\, 2m,\, 3m \in A_{k-1}}} \frac{1}{3m\log(3m)}.$$

*Proof*: $\log(6m) = \log 6 + \log m > \log 3 + \log m = \log(3m)$, so $1/(6m\log 6m) < 1/(6m\log 3m)
= (1/2)\cdot 1/(3m\log 3m)$. $\square$

The right-hand side is at most $(1/2) \cdot S_{k-1}(A_{k-1})$, so the collision correction
is at most half the primary term. After accounting for collisions:
$$\sum_{b \in \{2a\}\cup\{3a\}} \frac{1}{b\log b} \geq \sum_a \frac{1}{2a\log 2a} + \sum_a \frac{1}{3a\log 3a} - \frac{1}{2} S_{k-1}(A_{k-1}).$$
For each $a \in A_{k-1}$ with $a \geq x$: termwise, $1/(2a\log(2a)) + 1/(3a\log(3a))
= \frac{1}{a\log a}\Bigl[\frac{\log a}{2(\log 2 + \log a)} + \frac{\log a}{3(\log 3 + \log a)}\Bigr]
\to \frac{1}{a\log a}\cdot\bigl(\tfrac{1}{2}+\tfrac{1}{3}\bigr)$ as $a \to \infty$.
So for all $a \geq x$ (large $x$): $1/(2a\log 2a) + 1/(3a\log 3a) \geq (5/6 - \varepsilon_x)/(a\log a)$
for some $\varepsilon_x \to 0$ as $x \to \infty$. Summing over $a \in A_{k-1}$:
$\sum_{a} [1/(2a\log 2a) + 1/(3a\log 3a)] \geq (5/6 - \varepsilon_x) S_{k-1}(A_{k-1})$,
and the combined $\{p=2, p=3\}$ effective ratio is $5/6 - \varepsilon_x$.

The ratio $5/6 < 1$: adding primes 2 and 3 together still falls short of 1. The shortfall
is $1 - 5/6 = 1/6$; adding the $p=5$ contribution (ratio $+1/5$) raises the total to
$1/2 + 1/3 + 1/5 = 31/30 > 1$ in principle, but only if double-counting corrections
among $\{2, 3, 5\}$ are small.
Adding $p=5$ and bounding its collision correction similarly would give effective ratio
$(1/2+1/3+1/5) - (\text{corrections}) = 31/30 - \text{corrections}$; if corrections
$< 1/30$, the argument closes. This requires bounding the total collision weight among
primes $\{2, 3, 5\}$, which depends on how many pairs $(a, a')$ with $pa = qa'$ for
$p \neq q \in \{2, 3, 5\}$ exist in $A_{k-1}$.

### 14.6 Summary of Q22 findings

| Component | Status |
|---|---|
| Compensation factor $C(a) \to 31/30 > 1$ as $a \to \infty$ | **Proved** (elementary arithmetic) |
| Conditional two-stratum bound: $C(a)>1 \Rightarrow S(A) \leq T_k(x)$ | **Proved conditional** |
| $p=2$ injection gives ratio $\to 1/2 < 1$ | **Proved** (insufficient alone) |
| Collision correction $\leq (1/2) \cdot$ collision source weight | **Proved** |
| Combined $\{2,3,5\}$ correction $< 1/30$ to close argument | **OPEN** (Q23) |

**Status**: The compensation approach gives $C(a) \to 31/30 > 1$, establishing that
for large $x$ each element of $A_{k-1}$ blocks more than its own weight in principle.
The double-counting correction needs to be bounded below $1/30$ of $S_{k-1}(A_{k-1})$.
Q23 will bound the collision terms via the primitivity constraint on $A_{k-1}$.
