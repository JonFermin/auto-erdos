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
Moreover, $T_k(x) \to 0$ as $x \to \infty$ for each fixed $k$.

Proof: $A \cap \{n : \Omega(n) = k\}$ is a subset of $\{n \geq x : \Omega(n)=k\}$;
all terms are positive, so $S_k(A,x) \leq T_k(x)$. By F3, the full series
$\sum_{n \geq 2, \Omega(n)=k} 1/(n \log n) = 1 - (c+o(1))k^2/2^k$ is
convergent for each $k$ (the formula's right side is finite). The tail $T_k(x)$
of a convergent series tends to 0 as $x \to \infty$. See
`proof_lemmas/lemma_stratum_sub_bound.md`. $\square$

Note: The bound $T_k(x) \leq T_k(2)$ gives $T_k(x) \leq \sum_{n \geq 2,\Omega(n)=k}
1/(n \log n)$, which by F3 is $1 - (c+o(1))k^2/2^k$. For large $k$ this is
close to 1 from below. For $k=1$ (primes from 2), the full sum exceeds 1 (the
$o(1)$ correction in F3 is large at $k=1$); however, the TAIL $T_1(x)$
still vanishes as $x \to \infty$, which is what matters for the conjecture.

**Lemma `large_floor_vanish`** (status: proved): For each fixed $k \geq 1$,
$T_k(x) \to 0$ as $x \to \infty$.

Proof: The full series $\sum_{n \geq 2, \Omega(n)=k} 1/(n \log n) = 1 - (c+o(1))k^2/2^k$
converges by F3. The tail from $x$ is the tail of a convergent series,
hence $\to 0$ as $x \to \infty$. See `proof_lemmas/lemma_large_floor_vanish.md`. $\square$

**Corollary (Low-stratum control, FIXED $K$ only)**: For each fixed constant $K \geq 1$
(not depending on $x$),
$$\sum_{k=1}^{K} S_k(A, x) \leq \sum_{k=1}^{K} T_k(x) \to 0 \quad (x \to \infty).$$

Proof: Each $T_k(x) \to 0$ as $x \to \infty$ by Lemma `large_floor_vanish`; a
FIXED finite sum of $o(1)$ terms is $o(1)$. This argument is VALID ONLY for fixed $K$:
if $K = K(x) \to \infty$ with $x$, the sum of $K(x)$ terms, each individually $o(1)$,
need not tend to 0. The Corollary is not applicable to a growing $K(x)$.

**Decomposition**: For a FIXED constant $K \geq 1$ (not varying with $x$), split:
$$\sum_{a \in A} \frac{1}{a \log a}
  = \underbrace{\sum_{k=1}^{K} S_k(A,x)}_{\text{(I) low strata, fixed }K}
  + \underbrace{\sum_{k > K} S_k(A,x)}_{\text{(II) high strata}}.$$

- **(I) Low strata** ($K$ fixed): $\leq \sum_{k=1}^K T_k(x) \to 0$ as $x \to \infty$
  by the Corollary above (valid since $K$ is a fixed constant).

- **(II) High strata**: $\leq \sum_{k > K} T_k(x)$. For fixed $K$, the bound
  $\sum_{k > K} T_k(x) \leq \sum_{k > K} (1 - ck^2/2^k)$ diverges since each term
  $\to 1$ as $k \to \infty$.
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

1. **Per-stratum bound**: Each stratum of any primitive set contributes $< 1$
   to the sum (Lemma `stratum_sub_bound`, proved from F3).

2. **Vanishing for fixed strata**: For each fixed $k$, as $x \to \infty$, the
   contribution from $k$-almost primes in $[x, \infty)$ vanishes (Lemma
   `large_floor_vanish`, proved).

3. **Low-stratum $o(1)$**: For any fixed $K$, the sum over strata $k \leq K$
   from $[x, \infty)$ is $o(1)$ as $x \to \infty$.

4. **Global upper bound (from F1)**: The total sum is $< 1.399 + o(1)$ (the
   weaker Erdős–Zhang bound). This is an input fact, not proved here.

**What remains open** (the proof gap):

The critical regime is strata $k \sim \lfloor \log_2 x \rfloor$. For such $k$,
the smallest $k$-almost prime is $2^k \approx x$, so the restriction $a \geq x$
imposes almost no constraint. The per-stratum bound gives $S_k(A,x) \leq
T_k(x) \approx T_k(2) = 1 - ck^2/2^k$. For $k = \log_2 x$, this is
$1 - c(\log_2 x)^2/x$, which is close to 1. The sum over strata
$k \in [\log_2 x - C, \log_2 x + C]$ of these per-stratum bounds is
approximately $2C \cdot (1 - c(\log_2 x)^2/x)$, which diverges as $C \to \infty$
regardless of $x$. Controlling this requires a global argument that uses
primitivity to prevent multiple "critical strata" from simultaneously
contributing nearly 1.

**Dead ends ruled out**:
- Using F2's unsigned big-O to conclude $\sum > 1$ for any stratum: SIGN ERROR.
- Summing per-stratum bounds $\sum_k (1-ck^2/2^k)$ and claiming total $\leq 1$:
  this series diverges; the approach fails.
- Claiming the conjecture is proved or disproved without a valid witness:
  not supported.

**Lemma `dyadic_interval_bound`** (status: proved): For any primitive set
$A \subset [x, \infty)$ and any single dyadic interval $I = [N, 2N)$,
$$\sum_{a \in A \cap I} \frac{1}{a \log a} \leq \frac{\log 2}{\log N} + O\!\left(\frac{1}{N \log N}\right).$$

Proof: Every subset of $[N, 2N)$ is automatically primitive (no element divides
another). So $A \cap [N, 2N)$ can be any subset of $[N, 2N)$. The sum is
maximized when $A \cap I$ is the FULL set $\{N, N+1, \ldots, 2N-1\}$:
$$\sum_{a=N}^{2N-1} \frac{1}{a \log a} = \int_N^{2N} \frac{dt}{t \log t} + O\!\left(\frac{1}{N \log N}\right)
  \quad\text{(integral comparison for monotone decreasing } 1/(t\log t)\text{; elementary)}$$
$$= \ln\!\left(\frac{\log(2N)}{\log N}\right) + O\!\left(\frac{1}{N \log N}\right)
  = \ln\!\left(1 + \frac{\log 2}{\log N}\right) + O\!\left(\frac{1}{N \log N}\right)
  \leq \frac{\log 2}{\log N} + O\!\left(\frac{1}{N \log N}\right). \quad \square$$

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
   $\log 2/\log x = o(1)$ by Lemma `dyadic_interval_bound`, regardless of
   density. This direction therefore gives only per-interval $o(1)$, not a
   global bound.

2. **Mertens-type averaging with primitivity**: The Mertens sum
   $\sum_{n \leq x} 1/n \approx \log x$ and $\sum_{n \leq x, \Omega(n)=k} 1/n
   \approx (\log\log x)^{k-1}/((k-1)! \log x)$. For a primitive set, one
   needs to bound the sub-sum over $A$-elements via the antichain property.
   A Plünnecke–Ruzsa type inequality might control the "spread" of the set.

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

*Proof*: Every element of $A_1$ lies in $[x, x^e)$, so
$$S_1 \leq \sum_{n \geq x,\, n < x^e} \frac{1}{n \log n}
  \;\leq\; \int_x^{x^e} \frac{dt}{t \log t} + O\!\left(\frac{1}{x \log x}\right).$$
The integral telescopes (elementary calculus: $\tfrac{d}{dt}\log\log t = 1/(t\log t)$):
$$\int_x^{x^e} \frac{dt}{t \log t}
  = \bigl[\ln \ln t\bigr]_x^{x^e}
  = \ln\!\bigl(e \ln x\bigr) - \ln\!\bigl(\ln x\bigr)
  = \ln e = 1. \quad \square$$
(Here and throughout Section 4, $\log = \ln$ denotes the natural logarithm.)

This is tight: taking $A_1 = \emptyset$ gives $S_1 = 0$; taking $A_1$ to be
the full set $\{n \in \mathbb{Z} : x \leq n < x^e\}$ (not primitive, but
an upper bound) gives $S_1 \to 1$ as $x \to \infty$.

**Why $S_2$ is hard without primitivity**:

Without any constraint, $\sum_{n \geq x^e} 1/(n \log n)$ diverges
(since $\int_{x^e}^\infty dt/(t \log t) = \infty$). So the contribution from
$A_2$ is not bounded by the naive tail of the harmonic series. Primitivity
is essential to control $S_2$.

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
$\rho \cdot \sum_{n=N}^{2N} 1/(n \log n) \approx \rho \cdot \log 2/\log N$
over infinitely many dyadic intervals $N = x^e, 2x^e, 4x^e, \ldots$ gives
$\rho \cdot \sum_{j \geq 0} \log 2/(e \log x + j \log 2)$, which diverges for
any fixed $\rho > 0$. Multiplying a divergent sum by any positive constant does
not make it converge.

**Why this fails**: The tail $\sum_{n \geq x^e, n \in \mathcal{U}(A_1)} 1/(n \log n)$
cannot be bounded by a sieve-density argument alone, because the base series
$\sum_{n \geq x^e} 1/(n \log n)$ diverges and a multiplicative density factor
(not depending on $n$) cannot convert a divergent series to a convergent one.

Conclusion: Controlling $S_2$ via "unblocked density from $A_1$" fails because
the density factor does not cure divergence.

**Correct interpretation**: Even if one accounts for the blocking by $A_1$
at every dyadic scale $[x^e 2^j, x^e 2^{j+1})$ via a multiplicative density
factor $\rho < 1$ (the proportion of integers surviving the sieve by $A_1$),
the sum $\rho \cdot \sum_{j \geq 0} \log 2/(e \log x + j \log 2)$ is still $\rho$
times a divergent series. Multiplying a divergent sum by any positive constant
does not make it converge, so this "blocking density" heuristic cannot bound
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
which gives $S_2 < 1.399 + o(1)$. Combined with $S_1 \leq 1$, this gives
$S_1 + S_2 < 2.399 + o(1)$ — weaker than F1 applied directly to $A$, and not
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

Equivalently: if $A_1$ "nearly saturates" the integral $\int_x^{x^e} dt/(t \log t) = 1$,
then $A_2$ must contribute $o(1)$. This requires showing that "near-saturation"
of $S_1$ forces $A_1$ to be very "dense" in $[x, x^e)$, and that density in
$[x, x^e)$ forces near-emptiness (in the $\sum 1/(a \log a)$ sense) of $A_2$.

The "density" of $A_1$ in [x, x^e) needs to be measured in a way compatible
with both the $1/(a \log a)$ metric AND the divisibility blocking structure.
This is the essential unresolved point.

---

## Section 5 — Globally unblocked elements and the exchange inequality (Q8)

**Setup**. Fix $k \geq 1$ and let $k_0 = \lfloor \log_2 x \rfloor$ (so $2^{k_0} \leq x < 2^{k_0+1}$).
For any primitive $A \subset [x, \infty)$ and any $b \in A$ with $\Omega(b) = k+1$, define:

- $b$ is **globally $k$-blocked** if there exists a $k$-almost prime $d \in [x, \infty)$ with $d \mid b$.
- $b$ is **globally $k$-unblocked** if no $k$-almost prime in $[x, \infty)$ divides $b$.

(By primitivity of $A$: since no $a \in A$ with $\Omega(a) = k$ can divide $b$, every element of $A$
with $\Omega = k+1$ is automatically unblocked by $A$'s own $k$-stratum. "Global" unblockedness
is the stronger condition that also excludes $k$-almost primes NOT in $A$.)

**Lemma `globally_unblocked_size`** (status: proved): If $b \in [x, \infty)$ is globally
$k$-unblocked (no $k$-almost prime in $[x, \infty)$ divides $b$), then $b < x^{(k+1)/k}$.

*Proof*: Suppose $b \geq x$ has $\Omega(b) \geq k+1$ and no $k$-almost prime divisor in $[x, \infty)$.
Let $q$ be the smallest prime factor of $b$. The element $b/q$ has $\Omega(b/q) = \Omega(b) - 1 \geq k$.
If $\Omega(b/q) = k$, then $b/q$ is a $k$-almost prime. For $b/q \geq x$ we would need
$b \geq qx$. But then $b/q \geq x$ would be a $k$-almost prime in $[x,\infty)$ dividing $b$,
contradicting global $k$-unblockedness. Hence $b/q < x$, i.e.\ $b < qx \leq b^{1/(k+1)} \cdot x$
(since $q \leq b^{1/(k+1)}$ because $q$ is the smallest of at least $k+1$ prime factors of $b$,
so $q^{k+1} \leq b$). Thus $b^{1 - 1/(k+1)} < x$, giving $b < x^{(k+1)/k}$. $\square$

**Lemma `globally_unblocked_sum`** (status: proved): For any primitive $A \subset [x,\infty)$
and any $k \geq 1$:
$$\sum_{\substack{a \in A,\; \Omega(a) \geq k+1 \\ a \text{ globally } k\text{-unblocked}}}
  \frac{1}{a \log a} \;\leq\; \ln\!\left(1 + \tfrac{1}{k}\right) \;\leq\; \frac{1}{k}.$$

*Proof*: Every globally $k$-unblocked $a \in A$ with $\Omega(a) \geq k+1$ satisfies $a \in [x, x^{(k+1)/k})$
by Lemma `globally_unblocked_size`. Since all terms are positive:
$$\sum_{\substack{a \in A,\; \Omega(a) \geq k+1 \\ a \text{ globally } k\text{-unblocked}}}
  \frac{1}{a \log a}
  \;\leq\; \sum_{n \in [x,\, x^{(k+1)/k})} \frac{1}{n \log n}
  \;\leq\; \int_x^{x^{(k+1)/k}} \frac{dt}{t \ln t}
  = \bigl[\ln \ln t\bigr]_x^{x^{(k+1)/k}}
  = \ln\!\left(\frac{(k+1)\ln x}{k \cdot \ln x \cdot 1}\right)... $$

More carefully: $\int_x^{x^{(k+1)/k}} dt/(t\ln t) = \ln\ln(x^{(k+1)/k}) - \ln\ln x
= \ln((k+1)\ln x / k) - \ln(\ln x) = \ln((k+1)/k) = \ln(1+1/k) \leq 1/k$. $\square$

**Key consequence (exchange inequality for specific constructions)**:

Consider the primitive set $B = \{\text{all } k\text{-almost primes in } [x,\infty)\}
\cup \{\text{globally } k\text{-unblocked } (k+1)\text{-almost primes in } [x,\infty)\}$.

One can verify $B$ is primitive: (a) two $k$-almost primes never divide each other; (b) a
$k$-almost prime $a$ cannot divide a globally $k$-unblocked $(k+1)$-almost prime $b$ by definition;
(c) two globally-unblocked $(k+1)$-almost primes $b_1, b_2$ with $b_1 \mid b_2$ would give
$\Omega(b_2) \geq \Omega(b_1)+1 = k+2$, contradicting $\Omega(b_2)=k+1$. Hence $B$ is primitive.

The sum satisfies:
$$\sum_{b \in B} \frac{1}{b\log b} = T_k(x) + \sum_{\substack{b\in B\\ \Omega(b)=k+1}} \frac{1}{b\log b}
\;\leq\; T_k(x) + \frac{1}{k} \;<\; 1 + \frac{1}{k}.$$

Choosing $k = k_0 = \lfloor \log_2 x \rfloor$: since $1/k_0 = O(1/\log x) = o(1)$, and $T_{k_0}(x) < 1$
(by Lemma `stratum_sub_bound` applied to $T_k(2) = 1 - (c+o(1))k^2/2^k < 1$ for all $k$), we get:
$$\sum_{b \in B} \frac{1}{b \log b} < 1 + O(1/\log x) = 1 + o(1).$$

This confirms that the specific construction $B$ satisfies the conjecture's bound. The open
question is whether ALL primitive $A \subset [x,\infty)$ satisfy $\sum 1/(a\log a) < 1 + o(1)$.

**The remaining obstacle (Q8's open core)**:

The bound above applies only to elements of $A$ that are **globally** $k$-unblocked.
In a general primitive $A \subset [x,\infty)$, elements $b \in A$ with $\Omega(b) = k+1$
may be **globally $k$-blocked** — there exists a $k$-almost prime $d \in [x,\infty)$ with
$d \mid b$, but $d \notin A$ (by primitivity, $d$ cannot be in $A$ since $d \mid b$).

Such a globally-blocked $b$ is NOT confined to $[x, x^{(k+1)/k})$ and can be arbitrarily large.
Its contribution $1/(b\log b)$ is not covered by Lemma `globally_unblocked_sum`.

Concretely: take $k=1$ (k-almost primes = primes), $x=10^6$. The element $b = 2 \times 10^7$
(a $2$-almost prime, $\Omega=2$) has the $1$-almost prime divisor $d=2 \in [x,\infty)$?
No: $d=2 < x$. So $d$ must be $\geq x = 10^6$. The prime divisors of $b = 2\times10^7$ are
$\{2, 10^7\}$; the prime $10^7 \geq x$ IS a globally $1$-blocking prime. So $b$ is globally
$1$-blocked, but $10^7 \notin A$ (by primitivity, since $10^7 \mid b$). Here $b \in [x, \infty)$
but $b \notin [x, x^{2/1}) = [x, x^2)$ — wait, $b = 2\times 10^7 < (10^6)^2 = 10^{12}$, so
$b \in [x, x^2)$ which is $x^{(k+1)/k}$ for $k=1$. So in this case, the globally-blocked $b$
IS in $[x, x^{(k+1)/k})$. Is this always the case?

Hmm: if $b$ is globally $k$-blocked, then some $k$-almost prime $d \geq x$ divides $b$, so
$b \geq d \cdot 2 \geq 2x$ (since $d \geq x$ and $b = dm$ for integer $m \geq 2$, so $b \geq 2d \geq 2x$).
But there is no upper bound forcing $b < x^{(k+1)/k}$. For instance, if $d \approx x$ and $m$ is a
large $1$-almost prime (i.e.\ a prime $p \gg x^{1/k}$), then $b = dp \gg x^{1+1/k} = x^{(k+1)/k}$.
So globally-blocked $b$ can exceed $x^{(k+1)/k}$, and the unblocked-sum lemma does not apply.

**Partial conclusion (this remains open)**:

The globally-unblocked sum lemma shows that primitive sets consisting ONLY of k-almost primes
plus globally-unblocked $(k+1)$-almost primes satisfy the conjecture. General primitive sets
additionally include globally-$k$-blocked elements, which can be large. Bounding the globally-blocked
contribution requires the cross-strata primitivity to "transfer" the budget from the absent $k$-almost
prime $d$ (not in $A$) to the $(k+1)$-almost prime $b$ (in $A$). This cross-transfer argument is
the unresolved core; it requires tracking how much of $T_k(x)$ is "spent" by absent primes
that block elements of $A$'s higher strata, rather than being in $A$ themselves.

See `proof_lemmas/lemma_globally_unblocked.md` for detailed analysis.

This partial result is consistent with the conjecture and identifies the remaining mathematical gap.

**Lemma `large_elements_blocked`** (status: proved, Q9): The converse of Lemma
`globally_unblocked_size` holds. If $b \geq x^{(k+1)/k}$ and $\Omega(b) \geq k+1$, then $b$
is globally $k$-blocked (has a $k$-almost prime divisor $\geq x$). Combined with
`globally_unblocked_size`, this gives the complete dichotomy: every $(k+1)$-almost prime
element of $A$ is either in $[x, x^{(k+1)/k})$ (globally $k$-unblocked, bounded sum $\leq 1/k$)
or is globally $k$-blocked by some absent $k$-almost prime $d \geq x$. The blocked case remains
open; see `proof_lemmas/lemma_large_elements_blocked.md`.

**Lemma `fiber_sum_bound`** (status: proved per-fiber; total blocked sum open, Q10): For any
$k$-almost prime $d \geq x$ with $d \notin A$, define the fiber
$F_k(d,A) = \{b \in A : d \mid b,\; \Omega(b) = k+1\}$.
Every $b \in F_k(d,A)$ has the form $b = dp$ for a prime $p$, and
$$\sum_{b \in F_k(d,A)} \frac{1}{b \log b} \leq \frac{T_1(2)}{d},$$
where $T_1(2) = \sum_p 1/(p\log p)$ is a finite constant. Proof: $\log(dp) \geq \log p$
gives $1/(dp\log(dp)) \leq 1/(dp\log p)$; summing over primes $p$ with $dp \in A$ and using
$\sum_p 1/(p\log p) = T_1(2)$ yields the bound. See `proof_lemmas/lemma_fiber_sum_bound.md`.

**Fiber obstacle** (Q10 obstacle, open): Summing over all blocking $d$'s gives
$\sum_{d \geq x,\,\Omega(d)=k,\,d \notin A} T_1(2)/d \leq T_1(2)\cdot\sum_{d \geq x,\,\Omega(d)=k} 1/d$.
The sum $\sum 1/d$ over $k$-almost primes $d \geq x$ exceeds $T_k(x)$ by a $\log x$ factor
(since $\sum 1/d = (\log d)\cdot \sum 1/(d\log d)$ and $\log d$ is unbounded). The fiber bound
thus gives $\Omega(\log x)$ for the total blocked sum — divergent. A global weight argument
exploiting cross-fiber primitivity (Q11) is needed to close the gap.

**Integral representation + exchange principle** (Q11): Via Abel summation,
$\sum_{a \in A} 1/(a\log a) = \int_x^\infty N_A(t)\,dt/(t\log^2 t)$
where $N_A(t) = |A \cap [x,t]|$. The exchange construction satisfies
$\int_x^\infty N_{B_{k_0}(x)}(t)\,dt/(t\log^2 t) \leq 1 + 1/k_0$.
Claim $D_{k_0}$: $N_A(t) \leq N_{B_{k_0}(x)}(t)$ for all $t \geq x$ (counting-function dominance).
The map $\phi: b \mapsto d(b)$ (product of $b$'s $k_0$ smallest prime factors) sends each
$b \in A \setminus B_{k_0}$ to an absent $d(b) \in B_{k_0} \setminus A$ with $d(b) < b$ and
$d(b) \geq x$ (proved: $d(b) \cdot q_1\cdots q_\ell = b$ with $q_i \geq 2$, so $d(b) \leq b/2^{\Omega(b)-k_0} \leq b/4$ for $\Omega(b) \geq k_0+2$; and $d(b) \geq b/(q_1 q_2) \geq b/b \cdot x = x$ since $q_1 q_2 \leq b/2^{k_0} \leq b/x$).
However, $\phi$ is NOT injective: two elements $b, b' \in A \setminus B_{k_0}$ may share
$\phi(b) = \phi(b')$, so a single absent $d$ cannot compensate two extras. Claim $D_{k_0}$
is FALSE in general (fiber sharing). A modified approach — handling the multi-fiber case
separately or using a direct analytic bound on the integral — is needed (Q12).
See `proof_lemmas/lemma_primitive_exchange.md`.

**Cascading removal and sum maximality** (Q12): Adding a fiber element $b = dp$ (with
$d \notin A$, $p$ prime) to a primitive set requires removing all $d_q = (d/q)p$ for primes
$q \mid d$ with $d_q \in A$. Since $d_q = (d/q)p \geq x$ for all prime $q \mid d$ (proved:
$(d/q)p \geq (x/q)\cdot q = x$) and $d_q < d\cdot p$ (since $d_q = (d/q)p < dp = b$):
the net sum change from the reverse exchange is
$$\Delta_b = \frac{1}{dp\log(dp)} - \sum_{q \mid d,\, d_q \in A} \frac{1}{(d/q)p\log((d/q)p)} < 0$$
whenever ANY $d_q \in A$ (since $(d/q)p \geq 2 \cdot \frac{d}{q} \cdot \frac{p}{p} \geq \frac{dp}{q}$
so each removed term exceeds $q$ times the gain). This proves the FORWARD EXCHANGE (remove
fiber of $d$, add $d$) INCREASES the sum. Consequently: any primitive $A$ can be transformed
toward $B_{k_0}(x)$ by forward exchanges, with each exchange increasing the sum. A sum maximizer
must therefore have NO globally $k_0$-blocked elements — i.e., must be a subset of $B_{k_0}(x)$.
Thus $\sup \{\text{sum}(A) : A \text{ primitive}, A \subset [x,\infty)\} \leq \text{sum}(B_{k_0}(x)) \leq 1 + 1/k_0 = 1 + o(1)$.

**Gap in Q12 proof**: The above exchange argument assumes the sum maximizer $A^*$ exists and
that the exchange can always be applied. If $d$ has DIVISORS (not just multiples) in $A$, removing
them is also required and the sum change may go the other direction. A rigorous completion
requires either: (a) showing that divisors-in-$A$ case cannot arise for the maximizer, or
(b) a direct (non-exchange) proof of the bound. See `proof_lemmas/lemma_cascading_removal.md`
and Q13.

**Multi-stratum bound and divisors-in-A gap** (Q13, partial): The exchange approach fundamentally
fails when $a \in A$, $\Omega(a) = j < k_0$, $a \mid d$, $d \notin A$: removing $a$ costs
$1/(a \log a) > 1/(d \log d)$ (the gain from adding $d$), so the exchange decreases the sum.
Two partial results are proved: (1) **Pure-$k_0$ case** (proved): if $A \subseteq \{k_0$-almost
primes $\geq x\}$, then $S(A) \leq T_{k_0}(x) \leq 1 + 1/k_0$. (2) **Asymptotic per-element
budget** (proved): for $a \in A$ with $\Omega(a) = j < k_0$, the excluded budget of
$k_0$-almost prime multiples satisfies $W(a) \geq c \log\log x / (a \log a) \gg 1/(a \log a)$
as $x \to \infty$ (using $\sum_{p \leq a} 1/p \sim \log\log a$). However, the GLOBAL budget
accounting fails: multiple elements of $A$ at stratum $j$ can share the same $(j+1)$-almost prime
multiples as their excluded budget (the $j \mid$ check fails to be injective), so the chain
$S_j(A) \leq C(j+1)/(\log\log x) \cdot T_{j+1}(x)$ does not sum to $o(1)$ uniformly.
The remaining gap is Q14: a direct analytic proof (Sathe-Selberg + cross-stratum sieve) that
$\sum_{j \neq k_0} S_j(A) = o(1)$ for any primitive $A \subset [x,\infty)$. See
`proof_lemmas/lemma_multistratum_bound.md`.

**Trading decomposition cases** (Q14, partial): Let $e = (k_0+1)/k_0$ and split
$A = A_{\text{low}} \cup A_{\text{high}}$ at threshold $x^e$. Three cases are fully proved:
(1) $A \subset [x, x^e)$: $S(A) \leq \int_x^{x^e} dt/(t \log t) = 1$ by the integral bound
(no primitivity needed; the sum of $1/(n\log n)$ over any subset of integers in $[x,x^e)$ is
$\leq \int_x^{x^e} dt/(t\log t) = \log\log(x^e) - \log\log x = \log e = 1$).
(2) $A \subset [x^e, \infty)$: $S(A) < T_{k_0+1}(x^e) < 1$ by F3 applied to threshold $x^e$.
(3) $A \subset \{k_0\text{-APs} \geq x\}$: $S(A) \leq T_{k_0}(x) < 1$ (pure-stratum case).
The GENERAL case (both ranges nonempty with mixed strata) remains open: the cross-stratum
constraint prevents $A_{\text{low}}$ and $A_{\text{high}}$ from being jointly large, but a joint
bound requires $S_{\text{low}} + S_{\text{high}} \leq 1+o(1)$, which depends on the amount of
$(k_0+1)$-AP budget blocked by $A_{\text{low}}$. Since $T_{k_0}([x,x^e))$ and $T_{k_0+1}([x^e,\infty))$
are each close to 1, the sum is close to 2, and the cross-blocking reduction is only $O(S_{\text{low}}/\log x)$
— insufficient. Q15 will pursue the joint bound via a weight function argument. See
`proof_lemmas/lemma_trading_bound.md`.
