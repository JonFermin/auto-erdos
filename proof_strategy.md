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

- **F3** (Exact asymptotic, sum from BELOW 1): For
  $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$,
  $$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k},
  \quad c \approx 0.0656 > 0.$$
  The correction is **negative**: the sum is strictly less than 1 and
  approaches 1 from BELOW as $k \to \infty$ (anti-trap 2).

**Anti-traps** (do not trigger):

1. F2 sign confusion: unsigned big-O does not imply sum > 1 for any stratum.
2. F3 from-above misread: correction is negative; every full stratum sums to
   strictly less than 1.
3. Open-claim-asserted-resolved-without-witness: the conjecture is open.

**Numerical calibration** (not a proof): Computation confirms
$\sum_{p \leq 10^5} 1/(p \log p) \approx 1.550$ and the tail adds $\approx 0.087$,
giving total $\approx 1.637$ for the prime set starting at 2. Removing $p=2$
(so $A = \{3, 5, 7, \ldots\}$) gives partial sum $\approx 0.915 < 1$.
This suggests the conjecture is consistent: for $x \geq 3$, even the
"extremal-looking" set of primes gives sum $< 1$.

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
$$S_k(A, x) \leq T_k(x) \leq T_k(2) = 1 - (c + o(1)) \frac{k^2}{2^k} < 1.$$

Proof: $A \cap \{n : \Omega(n) = k\}$ is a subset of $\{n \geq x : \Omega(n)=k\}$;
all terms are positive; the right-hand bound is F3. See
`proof_lemmas/lemma_stratum_sub_bound.md`. $\square$

**Lemma `large_floor_vanish`** (status: proved): For each fixed $k \geq 1$,
$T_k(x) \to 0$ as $x \to \infty$.

Proof: The full series $\sum_{n \geq 2, \Omega(n)=k} 1/(n \log n) = 1 - (c+o(1))k^2/2^k$
converges by F3. The tail from $x$ is the tail of a convergent series,
hence $\to 0$ as $x \to \infty$. See `proof_lemmas/lemma_large_floor_vanish.md`. $\square$

**Corollary (Low-stratum control)**: For any fixed $K \geq 1$,
$$\sum_{k=1}^{K} S_k(A, x) \leq \sum_{k=1}^{K} T_k(x) \to 0 \quad (x \to \infty).$$

The "low-stratum" contribution (strata $k \leq K$ for any fixed $K$) is $o(1)$.

**Decomposition**: Fix $K = K(x)$ (to be chosen). Split:
$$\sum_{a \in A} \frac{1}{a \log a}
  = \underbrace{\sum_{k=1}^{K} S_k(A,x)}_{\text{(I) low strata}}
  + \underbrace{\sum_{k > K} S_k(A,x)}_{\text{(II) high strata}}.$$

- **(I) Low strata**: $\leq \sum_{k=1}^K T_k(x)$. By the Corollary, this is
  $o(1)$ as $x \to \infty$ for any fixed $K$.

- **(II) High strata**: $\leq \sum_{k > K} T_k(x) \leq \sum_{k > K} (1 - ck^2/2^k)$.
  The naive bound $\sum_{k>K}(1-ck^2/2^k)$ diverges since each term $\to 1$.
  The stratification bound is VACUOUS for the high-stratum sum.

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
$$\sum_{a \in A \cap I} \frac{1}{a \log a} \leq \frac{\log 2}{\log N} + O\!\left(\frac{1}{\log^2 N}\right).$$

Proof: Every subset of $[N, 2N)$ is automatically primitive (no element divides
another). So $A \cap [N, 2N)$ can be any subset of $[N, 2N)$. The sum is
maximized when $A \cap I$ is the FULL set $\{N, N+1, \ldots, 2N-1\}$:
$$\sum_{a=N}^{2N-1} \frac{1}{a \log a} = \int_N^{2N} \frac{dt}{t \log t} + O\!\left(\frac{1}{N \log N}\right)
  = \ln\!\left(\frac{\log(2N)}{\log N}\right) + O\!\left(\frac{1}{N \log N}\right)
  = \ln\!\left(1 + \frac{\log 2}{\log N}\right) + O\!\left(\frac{1}{N \log N}\right)
  = \frac{\log 2}{\log N} + O\!\left(\frac{1}{\log^2 N}\right). \quad \square$$

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

This session closes with the above partial result as the committed artifact.
The conjecture remains open.

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
The integral telescopes:
$$\int_x^{x^e} \frac{dt}{t \log t}
  = \bigl[\log \log t\bigr]_x^{x^e}
  = \log(e \log x) - \log(\log x)
  = \log e = 1. \quad \square$$

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

**Lemma (`blocking_estimate`, STATUS: OPEN)**: For any finite or locally finite
set $A_1 \subset [x, x^e)$, the sum
$$S_2 \leq \sum_{n \in \mathcal{U}(A_1),\, n \geq x^e} \frac{1}{n \log n}$$
is bounded in terms of $S_1 := \sum_{a \in A_1} 1/(a \log a)$, and
$$S_1 + S_2 \leq 1 + o(1) \quad (x \to \infty).$$

*Attempted bound via inclusion-exclusion*: By the multiplicative sieve,
$$\sum_{n \in \mathcal{U}(A_1),\, n \geq x^e} \frac{1}{n \log n}
  \;\approx\; \sum_{n \geq x^e} \frac{1}{n \log n}
  \cdot \prod_{a \in A_1} \!\left(1 - \frac{1}{a}\right).$$
This uses the heuristic that divisibility by distinct $a \in A_1$ is
"approximately independent." The product
$$\prod_{a \in A_1}\!\left(1-\frac{1}{a}\right)
  \approx \exp\!\left(-\sum_{a \in A_1} \frac{1}{a}\right).$$

For elements $a \in [x, x^e)$: $\sum_{a \in A_1} 1/a \geq (\min_{a \in A_1} \log a) \cdot S_1
\geq (\log x) \cdot S_1$. So:
$$\prod_{a \in A_1}\!\left(1-\frac{1}{a}\right) \lesssim e^{-(\log x) S_1} = x^{-S_1}.$$

But $\sum_{n \geq x^e} 1/(n \log n)$ diverges, so the product estimate alone does
not control $S_2$.

*Why this fails*: The heuristic independence assumption breaks down. For
large $n \geq x^e$, the event $a \mid n$ for different $a \in A_1$ is NOT
independent; elements of $A_1$ that are themselves divisible by a common factor
create correlations. A rigorous sieve bound requires either a square-root
cancellation argument or a combinatorial bound on the "unblocked density."

**Refined obstacle**: The key quantity is
$$D(A_1, N) := \#\{n \in [N, 2N) : a \nmid n \text{ for all } a \in A_1\}$$
for $N \geq x^e$. By a sieve of Eratosthenes type:
$$D(A_1, N) = N \cdot \prod_{a \in A_1, a \leq N}\!\left(1 - \frac{1}{a}\right) + \text{error}.$$
The main term: $N \cdot e^{-\sum_{a \leq N} 1/a}$ where the sum is over $a \in A_1$.
Contribution to $S_2$ from $[N, 2N)$:
$$\leq D(A_1, N) \cdot \frac{1}{N \log N} \leq \frac{1}{\log N} \cdot e^{-\sum_{a \in A_1,\, a \leq N} 1/a}.$$

Summing over dyadic intervals $N = x^e, 2x^e, 4x^e, \ldots$:
$$S_2 \lesssim \sum_{j=0}^\infty \frac{1}{\log(x^e 2^j)} \cdot e^{-C_j},
  \quad C_j = \sum_{a \in A_1,\, a \leq x^e 2^j} \frac{1}{a}.$$

For fixed $A_1 \subset [x, x^e)$: $C_j = \sum_{a \in A_1} 1/a$ for all $j$ (since
$A_1 \subset [x, x^e) \subset [x, x^e 2^j)$ for all $j \geq 0$). So:
$$S_2 \lesssim e^{-C} \cdot \sum_{j=0}^\infty \frac{1}{e \log x + j \log 2},
  \quad C = \sum_{a \in A_1} \frac{1}{a}.$$

The sum $\sum_{j=0}^\infty 1/(e \log x + j \log 2)$ diverges. So even with
the sieve factor $e^{-C}$, the bound on $S_2$ is $\infty$ (since $C$ is fixed
and the sum diverges). This again fails.

**Correct interpretation**: The sieve estimate above assumes $A_1$ blocks
$n$ independently at each dyadic scale. In reality, at scale $j$ (interval
$[x^e 2^j, x^e 2^{j+1})$), the blocking by $A_1$ applies to ALL elements of that
interval. The "blocking density" is:
$$\frac{D(A_1, N)}{N} \approx \prod_{a \in A_1}\!\left(1-\frac{1}{a}\right) \sim e^{-C},
\quad N \text{ large}.$$
So the contribution per dyadic interval is:
$$\frac{\log 2}{\log N} \cdot e^{-C}.$$

Summing over all $j \geq 0$: this gives $e^{-C} \cdot \sum_{j=0}^\infty \log 2/(e \log x + j \log 2)$
which STILL diverges. The sieve density factor $e^{-C}$ does not make the
sum converge.

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

**NOTE (circular, not a proof)**: One might attempt to bound $S_2$ by applying
the same conjecture to $A_2$ with parameter $x^e$. That would give
$S_2 \leq 1 + o(1)$ and hence $S_1 + S_2 \leq 2 + o(1)$ — which is WORSE
than F1's bound of 1.399 and does not prove the conjecture. Circular
application of the conjecture is NOT a valid proof step; it is included here
only to document that the recursive route fails.

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
