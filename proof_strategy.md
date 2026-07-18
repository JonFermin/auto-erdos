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

- **F3** (Asymptotic for large $k$): For
  $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
  $$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
  \quad c \approx 0.0656 > 0.$$
  The $o(1)$ is as $k \to \infty$. For large $k$ the correction is negative
  and $k^2/2^k \to 0$, so the sum approaches 1 from BELOW (anti-trap 2). For
  small $k$ (e.g.\ $k=1$, the primes starting from 2), the full-stratum sum
  may exceed 1 because the $o(1)$ correction is not small at $k=1$.

**Anti-traps** (do not trigger):

1. F2 sign confusion: unsigned big-O does not imply sum > 1 for any stratum.
2. F3 from-above misread: for large $k$, the sum approaches 1 from BELOW
   (correction is negative). Do NOT conclude sum $> 1$ from F3.
3. Open-claim-asserted-resolved-without-witness: the conjecture is open.

**Conceptual calibration** (not a proof): The conjecture concerns
$A \subset [x, \infty)$ for LARGE $x$; only elements $a \geq x$ contribute.
By Lemma `large_floor_vanish`, for each fixed $k$ the stratum tail
$T_k(x) \to 0$ as $x \to \infty$. This applies in particular to $k=1$
(the prime stratum): $T_1(x) = \sum_{p \geq x} 1/(p \log p) \to 0$.
For small $k$ (e.g.\ $k=1$), the full-stratum sum $\sum_{n:\Omega(n)=k} 1/(n\log n)$
is finite (by F3, which proves convergence) but may exceed 1 due to F3's
asymptotic scope (the formula is for large $k$). The TAIL vanishing is all
that is needed for the conjecture's $o(1)$ bound.

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

Note: We also have $T_k(x) \leq T_k(2) := \sum_{n:\,\Omega(n)=k} 1/(n \log n)$
(removing the lower-bound constraint). By F3, as $k \to \infty$ the full sum
$T_k(2)$ approaches $1$ from below. For each fixed $k$, $T_k(x) \to 0$ as
$x \to \infty$ (Lemma `large_floor_vanish` below).

**Lemma `large_floor_vanish`** (status: proved): For each fixed $k \geq 1$,
$T_k(x) \to 0$ as $x \to \infty$.

Proof: For $k=1$ (primes): $T_1(x) \leq \int_x^\infty dt/(t(\log t)^2) = 1/\log x \to 0$
by Mertens' theorem (which gives $\sum_{p\geq x} 1/p \leq 2/\log x$, hence
$T_1(x) \leq (2/\log x) \cdot \max_{p\geq x} 1/\log p \to 0$). For fixed $k\geq 2$:
apply Mertens' theorem inductively — each $n$ with $\Omega(n)=k$ factors as $n=pm$
with $p$ prime and $\Omega(m)=k-1$, giving $T_k(x) \leq \sum_{p} (1/p) \cdot T_{k-1}(x/p)
\to 0$ by induction. See `proof_lemmas/lemma_large_floor_vanish.md`. $\square$

**Corollary (Low-stratum control, FIXED $K$ only)**: For each fixed constant $K \geq 1$
(not depending on $x$),
$$\sum_{k=1}^{K} S_k(A, x) \leq \sum_{k=1}^{K} T_k(x) \to 0 \quad (x \to \infty).$$

Proof: See `proof_lemmas/lemma_low_stratum_vanish.md`. $\square$

**Warning**: This Corollary is VALID ONLY for fixed $K$: if $K = K(x) \to \infty$
with $x$, the sum of $K(x)$ terms, each individually $o(1)$, need not tend to $0$.
The Corollary is not applicable to a growing $K(x)$.

**Decomposition**: For a FIXED constant $K \geq 1$ (not varying with $x$), split:
$$\sum_{a \in A} \frac{1}{a \log a}
  = \underbrace{\sum_{k=1}^{K} S_k(A,x)}_{\text{(I) low strata, fixed }K}
  + \underbrace{\sum_{k > K} S_k(A,x)}_{\text{(II) high strata}}.$$

- **(I) Low strata** ($K$ fixed): $\leq \sum_{k=1}^K T_k(x) \to 0$ as $x \to \infty$
  by the Corollary above (valid since $K$ is a fixed constant).

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
   $T_k(x)$ to the sum, where $T_k(x) \to 0$ for fixed $k$ (Lemma `stratum_sub_bound`
   plus Lemma `large_floor_vanish`, proved).

2. **Vanishing for fixed strata**: For each fixed $k$, as $x \to \infty$, the
   contribution from $k$-almost primes in $[x, \infty)$ vanishes (Lemma
   `large_floor_vanish`, proved).

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
per-stratum sum is close to $1$ because the positive correction in F3 involves
$k^{*2}/2^{k^*} \approx (\log_2 x)^2/x$, which is negligible for large $x$.
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

**Lemma `dyadic_interval_bound`** (status: proved): For any primitive set
$A \subset [x, \infty)$ and any single dyadic interval $I = [N, 2N)$,
$$\sum_{a \in A \cap I} \frac{1}{a \log a} \leq \frac{1}{\log N}.$$

Proof: For each $a \in A \cap [N, 2N)$, we have $a \geq N$, so
$\frac{1}{a\log a} \leq \frac{1}{N\log N}$. The interval $[N, 2N)$ contains
exactly $N$ integers, so $|A \cap [N, 2N)| \leq N$, giving
$\sum_{a \in A \cap [N,2N)} \frac{1}{a\log a} \leq N \cdot \frac{1}{N\log N} = \frac{1}{\log N}$.
See `proof_lemmas/lemma_dyadic_interval_bound.md`. $\square$


Note: This per-interval bound is tight but its sum over dyadic intervals
$[x, 2x), [2x, 4x), \ldots$ diverges (a harmonic-type series). The
cross-interval primitivity constraint is essential to obtain a finite global
bound. See `proof_lemmas/lemma_cross_stratum_control.md` for why this fails.

**Suggested directions for future work**:

1. **Sieve / antichain density (DOES NOT APPLY at dyadic scale)**: By
   Lemma `dyadic_interval_bound`, every subset of $[N, 2N)$ is automatically
   primitive (no divisor-multiple pair can exist within a factor-of-2 window).
   So a primitive set in $[x, 2x]$ can have up to $\approx x$ elements — the
   full interval is primitive. The density within a single dyadic interval is
   NOT restricted to $O(x/\log x)$; that bound applies to multi-scale settings
   (e.g. $|A \cap [x, x^2]|$ with the cross-scale primitivity biting). For a
   single interval, the per-interval contribution is at most
   $1/\log N = o(1)$ by Lemma `dyadic_interval_bound`, regardless of
   density. This direction therefore gives only per-interval $o(1)$, not a
   global bound.

2. **Averaging with primitivity**: For a primitive set, one needs to bound
   the sub-sum over $A$-elements via the antichain property.
   Averaging arguments relate the sum to density estimates for k-almost
   primes, but without exploiting the cross-interval primitivity constraint
   these do not close the problem.

3. **Generating function / Dirichlet series**: For a primitive set $A$, the
   function $F_A(s) = \sum_{a \in A} a^{-s}$ satisfies $F_A(s) \cdot
   \zeta(s)^{-1}$ constraints from primitivity. Analyzing the residue at
   $s=1$ might give an improved bound.

The results above constitute the partial progress committed in this document.
The conjecture remains open; Section 4 continues the exploration.

---

## Section 4 — Trading decomposition (Q7)

**Setup**: Fix $e = 2.718\ldots$ (Euler's number). For any primitive set
$A \subset [x, \infty)$, split at the "pivot" $x^e$:
$$A_1 := A \cap [x,\, x^e), \qquad A_2 := A \cap [x^e, \infty).$$

Let $S_1 := \sum_{a \in A_1} \frac{1}{a \log a}$ and
$S_2 := \sum_{a \in A_2} \frac{1}{a \log a}$.

**Lemma (`S1_bound`)**: $S_1 \leq 1 + O(1/\log x)$.

*Proof*: Since each $a \in A_1 \subset [x, x^e)$, we have
$S_1 \leq \sum_{x \leq n < x^e} \frac{1}{n\log n}$.
The function $t \mapsto 1/(t\log t)$ is decreasing for $t > 1$, so each term satisfies
$\frac{1}{n\log n} \leq \int_{n-1}^{n} \frac{dt}{t\log t}$, giving
$S_1 \leq \int_{x-1}^{x^e} \frac{dt}{t\log t} = \bigl[\log\log t\bigr]_{x-1}^{x^e}
= \log(e\log x) - \log\log(x-1) = 1 + O(1/\log x)$,
where $\log(e\log x) = 1 + \log\log x$ and $\log\log(x-1) = \log\log x + O(1/(x\log x))$.
See `proof_lemmas/lemma_s1_bound.md`. $\square$
(Here and throughout Section 4, $\log = \ln$ denotes the natural logarithm.)

This is tight: taking $A_1 = \emptyset$ gives $S_1 = 0$; taking $A_1$ to be
the full set $\{n \in \mathbb{Z} : x \leq n < x^e\}$ (not primitive, but
an upper bound) gives $S_1 \to 1$ as $x \to \infty$.

**Why $S_2$ is hard without primitivity**:

Without any constraint, $\sum_{n \geq x^e} 1/(n \log n)$ is unbounded
(the series has no finite upper bound as more terms are included). So the
contribution from $A_2$ is not controlled by the size of the interval
$[x^e, \infty)$ alone. Primitivity is essential to control $S_2$.

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
with $f(t) = o(1)$ as $t \to 1^-$ such that $S_2 \leq f(S_1)$ for all
primitive $A$ and all $x$ large; this would give $S_1 + S_2 \leq S_1 + f(S_1)
\leq 1 + o(1)$. No such $f$ is currently known.

*Why sieve-density arguments fail* (heuristic exploration):

A natural approach is to estimate how many integers in $[x^e, \infty)$ avoid
divisibility by $A_1$. Even if only a small fraction $\rho \ll 1$ of integers in
each interval $[N, 2N)$ escape blocking by $A_1$, the sum
$\rho \cdot \sum_{n=N}^{2N-1} 1/(n \log n) \leq \rho/\log N$
over infinitely many dyadic intervals $N = x^e, 2x^e, 4x^e, \ldots$ gives
$\rho \cdot \sum_{j \geq 0} 1/(e \log x + j \log 2)$, which is unbounded for
any fixed $\rho > 0$ (the harmonic-type partial sums grow without bound).
Multiplying a divergent series by any positive constant does not make it
converge.

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
which gives $S_2 < e^\gamma \pi/4 + o(1)$ by F1 (F1 applies to any primitive set,
including $A_2 \subset [x^e, \infty)$; the $o(1)$ is as $x\to\infty$ since $x^e\to\infty$).
Combined with $S_1 \leq 1$, this gives
$S_1 + S_2 < 1 + e^\gamma \pi/4 + o(1)$ — weaker than F1 applied directly to $A$, and not
a proof of the conjecture. No recursive application closes the gap.

**Dead end confirmed**: The trading decomposition at $x^e$ does NOT give
$S_1 + S_2 \leq 1 + o(1)$ without additional input. The approach correctly
bounds $S_1 \leq 1$ (tight) but cannot control $S_2 \leq o(1)$ without
genuinely using the cross-structure of primitivity between $A_1$ and $A_2$.

See `proof_lemmas/lemma_trading_decomposition.md` for the precise gap statement.

**What IS needed (updated obstacle)**:

To prove the conjecture, one needs to show that for a primitive set
$A \subset [x, \infty)$:

$$S_2 \leq o(1) \quad \text{whenever } S_1 \approx 1.$$

Equivalently: if $S_1 \approx 1$, i.e., $A_1$ "nearly saturates" its maximal
possible contribution of 1, then $A_2$ must contribute $o(1)$. This requires
showing that "near-saturation"
of $S_1$ forces $A_1$ to be very "dense" in $[x, x^e)$, and that density in
$[x, x^e)$ forces near-emptiness (in the $\sum 1/(a \log a)$ sense) of $A_2$.

The "density" of $A_1$ in [x, x^e) needs to be measured in a way compatible
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

The essential question: does there exist a function $f(S_1) \to 0$ as
$S_1 \to 1$ such that for any primitive $A_2 \subset \mathcal{S}(A_1)$,
$S_2 \leq f(S_1)$? A YES answer with $S_1 + S_2 \leq 1 + o(1)$ would
close the conjecture; the existence of such $f$ is not known.

### 5.4 Current status and next steps

What is proved (combining Sections 2–4):
- $S_1 \leq 1$ (Lemma `S1_bound`, exact)
- $S_2 < e^\gamma \pi/4 + o(1)$ (from F1, which applies to any primitive set $A_2 \subset [x^e,\infty)$; $o(1)$ as $x\to\infty$)
- The combined bound $S_1 + S_2 < 1 + e^\gamma \pi/4 + o(1)$ (weaker than F1 directly)

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

**Lemma `low_stratum_vanish`**: Fix any integer $K \geq 1$. For any primitive
set $A \subset [x, \infty)$ whose elements all satisfy $\Omega(a) \leq K$,
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_{k=1}^{K} T_k(x) \to 0
\quad\text{as } x \to \infty.$$

*Proof*: See `proof_lemmas/lemma_low_stratum_vanish.md`. $\square$

**Consequence**: The conjecture holds easily (with $o(1)$ bound) whenever $A$
is supported on strata of bounded Omega-number. The hard case requires elements
with $\Omega(a) \to \infty$ as $x \to \infty$.

### 6.2 The critical Omega-regime

The smallest integer with $\Omega(n) = k$ is $2^k$ (any $n$ with $\Omega(n)=k$ has $k$
prime factors each $\geq 2$, so $n \geq 2^k$, with equality at $n = 2^k$).
For $A \subset [x, \infty)$
to have any element with $\Omega(a) = k$, we need $2^k \leq a$ for some
$a \geq x$, which requires $k$ can take any value (since there are arbitrarily
large $k$-almost primes). However, for the element to be "inexpensive"
(small $1/(a\log a)$), we want $a$ small — and the smallest $k$-almost prime
$\geq x$ has $a \approx x$ when $k \approx \log_2 x$.

Precisely: the strata $k$ for which $T_k(x)$ is not negligible are those
where $k$ is large enough that $k$-almost primes $\geq x$ are plentiful,
i.e., $k \gtrsim \log_2 x$. By the low-stratum lemma, any $A$ avoiding
strata $k > \log_2 x - C$ (for any fixed $C$) satisfies $S = o(1)$.

The critical range is $k \in [k^* - C, k^* + C]$ for $k^* = \lfloor \log_2 x
\rfloor$ and any fixed $C$. An element $a \geq x$ with $\Omega(a) = k$ in
this range satisfies $2^k \approx x$, meaning $a$ is an integer just above $x$
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
where by F3 each $T_\ell(2) = \sum_{n:\Omega(n)=\ell} \frac{1}{n\log n} < 1$.
For $j$ or $k$ small (say $j = 1$, $k = 2$), the two per-stratum bounds
could sum to exceed $1$, showing the naive two-stratum bound is insufficient.

Cross-stratum primitivity constrains $A^{(k)}$: for each $a \in A^{(j)}$ and
$b \in A^{(k)}$, $a \nmid b$. So $A^{(k)}$ is contained in the sieved set
$$\mathcal{S}_k(A^{(j)}) := \{n \geq x : \Omega(n) = k,\; a \nmid n \;
\forall a \in A^{(j)}\}.$$

A quantitative bound on $\sum_{n \in \mathcal{S}_k(A^{(j)})} 1/(n\log n)$
in terms of $S_j$ (the weight of $A^{(j)}$) would close the two-stratum case.
Such a bound would likely follow from a Selberg-type sieve applied to
$k$-almost primes sieved by the divisors in $A^{(j)}$, but this remains open.

### 6.5 Gap summary and updated strategy

What the analysis achieves (combining all sections):
- **Sections 2–3**: Per-stratum bounds; each $S_k < 1$; summing diverges.
- **Section 4**: Trading decomposition; $S_1 \leq 1$ exact.
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

*Case 1 ($k$ fixed as $x\to\infty$)*: By Mertens' theorem and induction on $k$
(as in Lemma `large_floor_vanish`), $T_k(x) \to 0$ as $x\to\infty$.
Hence $S \leq T_k(x) \to 0$, giving $S = o(1) < 1 + o(1)$.

*Case 2 ($k = k(x) \to \infty$)*: By F3, for all large enough $k$,
$T_k(2) = 1 - (c + o(1))k^2/2^k < 1$.
Hence $S \leq T_k(x) \leq T_k(2) < 1 < 1 + o(1)$.

Combined: In both cases $S < 1 + o(1)$ as $x\to\infty$. $\square$

See `proof_lemmas/lemma_single_stratum_bound.md` for the complete argument.

**Consequence**: The conjecture holds for single-stratum primitive sets.
The remaining open case is when $A$ spans two or more $\Omega$-strata; in
that case, cross-stratum primitivity must prevent simultaneous near-1
contributions from multiple strata.
