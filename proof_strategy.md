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

**Standing assumption**: Throughout this document, $x \geq 2$. All assertions
involving $T_k(x)$, inclusions $\{n \geq x\} \subseteq \{n \geq 2\}$, and
similar rely only on $x \geq 2$.

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
  small $k$ (e.g.\ $k=1$, the primes), F3's asymptotic is stated for $k \to \infty$
  and makes no claim about the value at $k=1$; the total is bounded above by
  F1 (less than $e^\gamma\pi/4$) and F2's $O(\cdot)$ is UNSIGNED so the
  direction relative to 1 at $k=1$ is not determined by the ledger.

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
is finite: $A_k$ is primitive (no $k$-almost prime divides another), so the series $\sum_{a\in A_k} 1/(a\ln a)$ is finite — as proved in Lemma `stratum_sub_bound` by applying F1 to finite subsets and taking limits.
F3's asymptotic formula holds for $k\to\infty$ and its accuracy at small $k$
(including $k=1$) is not established by the ledger. The TAIL vanishing is all
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
all terms are positive, so $S_k(A,x) \leq T_k(x)$. The full series
$\sum_{n \geq 2, \Omega(n)=k} 1/(n \log n)$ converges for each $k$: the set
$A_k := \{n \geq 2 : \Omega(n) = k\}$ is itself a primitive set, because if
$a \mid b$ with $a \neq b$ and $\Omega(a) = \Omega(b) = k$ then $b/a \geq 2$
gives $\Omega(b) \geq \Omega(a) + \Omega(2) = k+1 > k$, contradiction. Moreover $A_k \subset [2^k, \infty)$: each $n \in A_k$ has exactly $k$ prime factors (with multiplicity) each $\geq 2$; any product of $k$ factors each $\geq 2$ is $\geq 2^k$ (by monotonicity of multiplication), so $n \geq 2^k$.
Convergence of the series: any finite subset $S \subseteq A_k$ is a primitive set;
by F1, $\sum_{a \in S} 1/(a \ln a)$ is bounded above (by F1's upper bound, which is finite).
Since all terms $1/(n\ln n) > 0$, the partial sums form a bounded increasing sequence;
hence the series $\sum_{n:\Omega(n)=k} 1/(n\ln n)$ converges.
Since the partial sums $\sum_{\Omega(n)=k,\, 2\leq n \leq M} 1/(n\ln n)$ increase to a finite limit
$L_k$ as $M \to \infty$, the remainder $T_k(x) = L_k - \sum_{\Omega(n)=k,\, 2\leq n < x} 1/(n\ln n)
\to 0$ as $x \to \infty$. See
`proof_lemmas/lemma_stratum_sub_bound.md`. $\square$

Note: The bound $T_k(x) \leq T_k(2)$ gives $T_k(x) \leq \sum_{n \geq 2,\Omega(n)=k}
1/(n \log n)$, which is finite (the series converges by Lemma `stratum_sub_bound`). For large $k$, F3 shows this full-stratum sum
approaches 1 from below (by F3, the correction term $-(c+o(1))k^2/2^k$ is negative and tends to $0$ as $k \to \infty$). For $k=1$ (primes),
F3's formula is stated for $k \to \infty$ and does not determine the value at $k=1$;
from F1, the full prime sum is bounded above by $e^\gamma\pi/4$, but whether it
exceeds or falls below 1 is not established by the ledger. The TAIL $T_1(x)$
still vanishes as $x \to \infty$, which is what matters for the conjecture.

**Lemma `large_floor_vanish`** (status: proved): For each fixed $k \geq 1$,
$T_k(x) \to 0$ as $x \to \infty$.

Proof: Lemma `stratum_sub_bound` shows the full series $\sum_{n \geq 2, \Omega(n)=k} 1/(n \log n)$
converges (using F1 applied to finite subsets). Since all terms are positive, the partial
sums form a bounded increasing sequence, so $T_k(x) \to 0$ as $x \to \infty$ (tail of a
convergent positive series). See `proof_lemmas/lemma_large_floor_vanish.md`. $\square$

**Corollary (Low-stratum control, FIXED $K$ only)**: For each fixed constant $K \geq 1$
(not depending on $x$),
$$\sum_{k=1}^{K} S_k(A, x) \leq \sum_{k=1}^{K} T_k(x) = o(1) \quad (x \to \infty,\; K \text{ fixed}).$$

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

- **(II) High strata**: $\leq \sum_{k > K} T_k(x) \leq \sum_{k > K} T_k(2) < \infty$?
  No: $T_k(2) = \sum_{n \geq 2,\, \Omega(n)=k} 1/(n\log n)$. The smallest $n$
  with $\Omega(n)=k$ is $2^k \geq 2$, so $T_k(2)$ equals the full stratum sum
  $\sum_{\Omega(n)=k} 1/(n\log n)$; by F3 (for $k \to \infty$), this equals
  $1 - (c+o(1))k^2/2^k \to 1$ as $k \to \infty$ (since $k^2/2^k \to 0$ as $k \to \infty$). The terms $T_k(2)$ do not
  tend to 0, so $\sum_{k > K} T_k(2)$ diverges by the divergence test.
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

1. **Per-stratum bound**: Each stratum of any primitive set contributes $\leq T_k(x)$,
   a finite bound by F1 (Lemma `stratum_sub_bound`, proved from F1).

2. **Vanishing for fixed strata**: For each fixed $k$, as $x \to \infty$, the
   contribution from $k$-almost primes in $[x, \infty)$ vanishes (Lemma
   `large_floor_vanish`, proved).

3. **Low-stratum $o(1)$**: For any fixed $K$, the sum over strata $k \leq K$
   from $[x, \infty)$ is $o(1)$ as $x \to \infty$.

4. **Global upper bound (from F1)**: The total sum is $< 1.399 + o(1)$ (the
   weaker Erdős–Zhang bound). This is an input fact, not proved here.

**What remains open** (the proof gap):

The critical regime is strata near $k = \lfloor \log_2 x \rfloor$. For such $k$,
the smallest $k$-almost prime is $2^k$ and we have $2^k \leq x < 2^{k+1}$,
so the restriction $a \geq x$ is nearly vacuous. The per-stratum bound gives
$S_k(A,x) \leq T_k(x) \leq T_k(2)$ (since $x \geq 2$ implies $\{n \geq x : \Omega(n)=k\} \subseteq \{n \geq 2 : \Omega(n)=k\}$, so $T_k(x)$ is a partial sub-sum of $T_k(2)$ with non-negative terms, giving $T_k(x) \leq T_k(2)$). As $x \to \infty$, $k = \lfloor\log_2 x\rfloor \to \infty$, so F3's asymptotic formula applies: $T_k(2) = 1 - (c+o(1))k^2/2^k$. Since
$k = \lfloor\log_2 x\rfloor$ satisfies $2^k \leq x$ (by definition of floor),
hence $1/2^k \geq 1/x$, so $k^2/2^k \geq k^2/x$; since $k = \lfloor\log_2 x\rfloor \geq (\log_2 x) - 1$, we get
$k^2/x \geq (\lfloor\log_2 x\rfloor)^2/x$, giving
$T_k(2) \leq 1 - (c+o(1))(\lfloor\log_2 x\rfloor)^2/x$, which tends to 1
from below as $x \to \infty$ (correction of order $(\log x)^2/x \to 0$).
For any fixed $C$, the sum over strata $k \in [\lfloor\log_2 x\rfloor - C,
\lfloor\log_2 x\rfloor + C]$ of these per-stratum bounds is at most
$(2C+1) \cdot (1 - (c+o(1))(\lfloor\log_2 x\rfloor)^2/x)$ (since the range $[\lfloor\log_2 x\rfloor - C, \lfloor\log_2 x\rfloor + C]$ contains exactly $2C+1$ integer values of $k$). As $x \to \infty$, the correction
$(c+o(1))(\lfloor\log_2 x\rfloor)^2/x \to 0$ (since $(\log_2 x)^2/x \to 0$), so
each individual $T_{k'}(2)$ for $k'$ in the window satisfies $T_{k'}(2) \to 1$ as $x \to \infty$ (since $k' \approx \log_2 x \to \infty$ and the F3 correction $k'^2/2^{k'} \to 0$). For each fixed $C$, the sum of $2C+1$ such terms tends to $2C+1$. As $C$ grows (a separate limit from $x \to \infty$), $2C+1 \to \infty$.
Controlling this requires a global argument that uses
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

Proof: Every subset of $[N, 2N)$ is automatically primitive: if $a, b \in [N, 2N)$
and $a \mid b$ with $a \neq b$, then $b \geq 2a \geq 2N$, contradicting $b < 2N$.
So $A \cap [N, 2N)$ can be any subset of $[N, 2N)$. Since all terms $1/(a\log a)$
are positive, the sum $\sum_{a \in A\cap I} 1/(a\log a)$ is non-decreasing as
$A \cap I$ increases, so it is maximized when $A \cap I$ is the FULL set
$\{N, N+1, \ldots, 2N-1\}$:
Since $f(t) = 1/(t \log t)$ is strictly decreasing for $t \geq 2$, for each integer $n \geq N+1$:
$f(n) \leq \int_{n-1}^n f(t)\,dt$ (since $f$ decreases on $[n-1,n]$). Summing from $n = N+1$ to $2N-1$:
$\sum_{n=N+1}^{2N-1} f(n) \leq \int_N^{2N-1} f(t)\,dt \leq \int_N^{2N} f(t)\,dt$.
Adding $f(N) = 1/(N\log N)$:
$$\sum_{a=N}^{2N-1} \frac{1}{a \log a} \leq \frac{1}{N\log N} + \int_N^{2N} \frac{dt}{t \log t},$$
so:
$$\sum_{a=N}^{2N-1} \frac{1}{a \log a} \leq \int_N^{2N} \frac{dt}{t \log t} + \frac{1}{N \log N}$$
The integral evaluates using the antiderivative: by the chain rule, $\frac{d}{dt}(\ln\ln t) = \frac{1}{\ln t}\cdot\frac{1}{t} = \frac{1}{t\ln t}$ (for $t > 1$), so
$\int_N^{2N} \frac{dt}{t\ln t} = \bigl[\ln\ln t\bigr]_N^{2N} = \ln\ln(2N) - \ln\ln N = \ln\!\bigl(\frac{\ln(2N)}{\ln N}\bigr) = \ln\!\bigl(\frac{\log(2N)}{\log N}\bigr)$, giving:
$$= \ln\!\left(\frac{\log(2N)}{\log N}\right) + O\!\left(\frac{1}{N \log N}\right)
  = \ln\!\left(1 + \frac{\log 2}{\log N}\right) + O\!\left(\frac{1}{N \log N}\right)
  \leq \frac{\log 2}{\log N} + O\!\left(\frac{1}{N \log N}\right), \quad \square$$
where the last step uses $\ln(1 + u) \leq u$ for $u \geq 0$: since $e^u \geq 1 + u$ for all $u$ (this follows by comparing derivatives: $e^0 = 1 + 0 = 1$ and $\frac{d}{du} e^u = e^u \geq 1 = \frac{d}{du}(1+u)$ for $u \geq 0$), taking logarithms gives $u \geq \ln(1+u)$.

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

2. **Mertens-type averaging with primitivity**: Heuristically,
   $\sum_{n \leq x, \Omega(n)=k} 1/n$ grows like a power of $\log\log x$
   divided by $\log x$ for fixed $k$ (a well-known count heuristic).
   For a primitive set, one
   needs to bound the sub-sum over $A$-elements via the antichain property.
   A sumset-type inequality might control the "spread" of the primitive set.

3. **Generating function / Dirichlet series**: For a primitive set $A$, the
   function $F_A(s) = \sum_{a \in A} a^{-s}$ satisfies $F_A(s) \cdot
   \zeta(s)^{-1}$ constraints from primitivity. Analyzing the residue at
   $s=1$ might give an improved bound.

The results above constitute the partial progress committed in this document.
The conjecture remains open; Section 4 continues the exploration.

---

## Section 4 — Trading decomposition (Q7)

**Setup**: For any primitive set $A \subset [x, \infty)$, split at the
pivot $x^e$ (where $e \approx 2.718$ denotes Euler's number, the base of the natural logarithm):
$$A_1 := A \cap [x,\, x^e), \qquad A_2 := A \cap [x^e, \infty).$$

Let $S_1 := \sum_{a \in A_1} \frac{1}{a \log a}$ and
$S_2 := \sum_{a \in A_2} \frac{1}{a \log a}$.

**Lemma (`S1_bound`)**: $S_1 \leq 1 + o(1)$ as $x \to \infty$.

*Proof*: Every element of $A_1$ lies in $[x, x^e) \cap \mathbb{Z}$, so
$A_1 \subseteq \{x, x+1, \ldots, \lfloor x^e \rfloor\}$; since all terms $1/(n \ln n)$
are positive, summing over a subset is $\leq$ summing over the full range:
$$S_1 \leq \sum_{n=x}^{\lfloor x^e \rfloor} \frac{1}{n \ln n}.$$
Since $f(t) = 1/(t \ln t)$ is strictly decreasing for $t \geq 2$: for any $n \geq x+1$ and $t \in [n-1,n]$, $t \leq n$ gives $f(n) \leq f(t)$. Integrating over $[n-1,n]$ (length 1): $f(n) = \int_{n-1}^n f(n)\,dt \leq \int_{n-1}^n f(t)\,dt$. Therefore:
$$\sum_{n=x}^{\lfloor x^e \rfloor} f(n)
  = f(x) + \sum_{n=x+1}^{\lfloor x^e \rfloor} f(n)
  \leq f(x) + \sum_{n=x+1}^{\lfloor x^e \rfloor} \int_{n-1}^n f(t)\,dt
  = f(x) + \int_x^{\lfloor x^e \rfloor} f(t)\,dt
  \leq \frac{1}{x \ln x} + \int_x^{x^e} f(t)\,dt.$$
(Since $f \geq 0$, extending the upper limit from $\lfloor x^e\rfloor \leq x^e$ only adds non-negative terms.)
By the chain rule, $\frac{d}{dt}(\ln \ln t) = \frac{1}{\ln t} \cdot \frac{1}{t} = \frac{1}{t \ln t}$,
so $\ln \ln t$ is an antiderivative of $\frac{1}{t \ln t}$. Therefore:
$$\int_x^{x^e} \frac{dt}{t \ln t}
  = \bigl[\ln \ln t\bigr]_x^{x^e}
  = \ln\!\bigl(\ln(x^e)\bigr) - \ln\!\bigl(\ln x\bigr)
  = \ln(e\ln x) - \ln(\ln x)
  = \ln e + \ln(\ln x) - \ln(\ln x) = \ln e,$$
using $\ln(x^e) = e\ln x$ and $\ln(e\ln x) = \ln e + \ln(\ln x)$ (product rule $\ln(ab) = \ln a + \ln b$).
By the identity $\ln(e^t) = t$ applied at $t = 1$: $\ln e = \ln(e^1) = 1$.
So $S_1 \leq 1 + \frac{1}{x \ln x} \to 1$ as $x \to \infty$. $\square$

(Here and throughout Section 4, $\log = \ln$ denotes the natural logarithm.)

The upper bound $S_1 \leq 1 + 1/(x\ln x)$ is meaningful (its right side is $1 + o(1)$),
and the bound $\sum_{n=x}^{\lfloor x^e\rfloor} 1/(n\ln n) \to 1$ shows the sum over
ALL integers in $[x, x^e)$ (not necessarily forming a primitive set) approaches 1.
This sum serves as an upper bound on $S_1$ regardless of the primitivity structure of $A_1$.

**Why $S_2$ is hard without primitivity**:

Without any constraint, $\sum_{n \geq x^e} 1/(n \log n)$ diverges. Since $f(t) = 1/(t\ln t)$ is decreasing, for $t \in [n, n+1]$ we have $f(n) \geq f(t)$, so $f(n) = \int_n^{n+1} f(n)\,dt \geq \int_n^{n+1} f(t)\,dt$. Summing from $n = N$ to $M$: $\sum_{n=N}^M f(n) \geq \int_N^{M+1} f(t)\,dt = [\ln\ln t]_N^{M+1} = \ln\ln(M+1) - \ln\ln N$ (using the antiderivative from the $S_1$ proof above). Since $\ln\ln(M+1) \to \infty$, the series diverges. Primitivity is essential to control $S_2$.

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
with $f(t) \to 0$ as $t \to 1^-$ (i.e., $f$ is a function vanishing as its argument approaches 1 from below) such that $S_2 \leq f(S_1)$ for all
primitive $A$ and all $x$ large; this would give $S_1 + S_2 \leq S_1 + f(S_1)
\leq 1 + o(1)$. No such $f$ is currently known.

*Why sieve-density arguments fail* (heuristic exploration):

A natural approach is to estimate how many integers in $[x^e, \infty)$ avoid
divisibility by $A_1$. Suppose a fraction $\rho > 0$ (bounded below, uniformly
in $j$) of integers in each interval $[N, 2N)$ escape blocking by $A_1$; the sum
$\rho \cdot \sum_{n=N}^{2N} 1/(n \log n) \leq \rho \cdot (\log 2/\log N + O(1/(N\log N)))$
over infinitely many dyadic intervals $N = x^e 2^j$ gives
$\rho \cdot \sum_{j \geq 0} \frac{\log 2}{e \log x + j \log 2}$, which diverges for
any fixed $\rho > 0$ (compare with $\sum_{j \geq 1} 1/j = \infty$, the harmonic series,
since $\log 2 / (e\log x + j \log 2) \geq c/j$ for $j$ large). (Note: if $\rho_j \to 0$ fast enough as $j \to \infty$,
the series could converge — but no such decay of $\rho_j$ is available from
the blocking structure alone without additional primitivity input.)
Multiplying a divergent series by a uniformly positive constant does not make
it converge.

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

## Section 5 — Prime-factor split (Q12)

**Definition**: For any primitive set $A \subset [x, \infty)$, define:
$$A_{\mathrm{sm}} := \{a \in A : p_{\min}(a) < x\},
\qquad
A_{\mathrm{lg}} := \{a \in A : p_{\min}(a) \geq x\},$$
where $p_{\min}(a)$ denotes the smallest prime factor of $a$. Every element of
$A_{\mathrm{lg}}$ has ALL prime factors $\geq x$.

**Structural non-divisibility** (no external citation): For any $a \in A_{\mathrm{sm}}$
and $b \in A_{\mathrm{lg}}$, we have $a \nmid b$.

*Proof*: Let $p = p_{\min}(a) < x$. Since $p \mid a$, if $a \mid b$ then by transitivity of divisibility ($p \mid a$ and $a \mid b$ imply $p \mid b$; explicitly: $b = a \cdot m$ for some integer $m$, and $a = p \cdot k$ for some integer $k$, so $b = pk m$ and $p \mid b$) we get $p \mid b$.
But every prime factor of $b \in A_{\mathrm{lg}}$ is $\geq x > p$, so $p \nmid b$ (as $p < x \leq$ every prime factor of $b$). Contradiction. $\square$

**Consequence**: The only cross-divisibility excluded by primitivity of $A$ is
$b \nmid a$ for $b \in A_{\mathrm{lg}}$, $a \in A_{\mathrm{sm}}$. The reverse direction
($a \nmid b$ for $a \in A_{\mathrm{sm}}$, $b \in A_{\mathrm{lg}}$) holds structurally, regardless
of primitivity.

**Lemma `prime_tail_vanish`** (status: proved; see `proof_lemmas/lemma_prime_tail_vanish.md`):
$$\sum_{\substack{p \geq x \\ p \text{ prime}}} \frac{1}{p \ln p} \;\to\; 0
  \quad \text{as } x \to \infty.$$
*Proof sketch*: The primes form a primitive set (if $p \mid q$ with $p, q$ prime then $p = q$,
so no distinct prime divides another). For any finite $X$, the finite set $\{p \leq X : p \text{ prime}\}
\subseteq \mathbb{N}$ is primitive, so **F1** gives $\sum_{p \leq X} 1/(p \ln p) < e^\gamma\pi/4$.
Since this bound holds for all $X$ and the partial sums $\sum_{p \leq X} 1/(p \ln p)$ are monotone
non-decreasing in $X$ and bounded above, the series $\sum_{p} 1/(p \ln p)$ converges to a finite limit.
Its tail from $x$ then tends to $0$ as $x \to \infty$. $\square$

**Contribution of $A_{\mathrm{lg}}$ by stratum**:

Every $a \in A_{\mathrm{lg}}$ with $\Omega(a) = k$ has all $k$ prime factors (counted with multiplicity) $\geq x$,
so $a = p_1 p_2 \cdots p_k$ with each $p_i \geq x$, giving $a \geq x^k$.

- **$\Omega(a) = 1$ (primes $\geq x$)**:
  $$\sum_{\substack{a \in A_{\mathrm{lg}} \\ \Omega(a)=1}} \frac{1}{a \ln a}
    \;\leq\; T_1(x) \;\to\; 0,$$
  by Lemma `prime_tail_vanish`.

- **$\Omega(a) = k \geq 2$ (each fixed $k$)**: The $\Omega = k$ stratum of $A_{\mathrm{lg}}$
  lies inside $\{n \geq x^k : \Omega(n) = k\}$:
  $$\sum_{\substack{a \in A_{\mathrm{lg}} \\ \Omega(a)=k}} \frac{1}{a \ln a}
    \;\leq\; T_k(x^k) \;\to\; 0 \quad (x \to \infty),$$
  by Lemma `large_floor_vanish` at threshold $x^k$ (valid since $x^k \to \infty$).

**Obstacle (summing over all $k$)**: The per-stratum bounds $T_k(x^k) \to 0$ hold
for each FIXED $k$ as $x \to \infty$. However, the number of non-negligible strata
grows with $x$ (roughly $k \sim \log_2 x$ strata are "active"). By **F3**,
$T_k(2) = 1 - (c+o(1))k^2/2^k$, so $\sum_{k \geq 1} T_k(2)$ diverges. A naive
sum of the per-stratum bounds over all $k$ is therefore not finite. A global argument
exploiting the primitivity of $A_{\mathrm{lg}}$ as a whole is required.

By **F1** applied to the primitive set $A_{\mathrm{lg}} \subseteq [x,\infty)$:
$$\sum_{a \in A_{\mathrm{lg}}} \frac{1}{a \ln a} < e^{\gamma}\frac{\pi}{4},$$
which gives a finite upper bound (${\approx}1.399 > 1$) but not the sharper $\leq 1$ needed for the conjecture. The full stratum sum $T_k(2) = \sum_{n \geq 2,\, \Omega(n)=k} 1/(n \ln n)$ (note:
the smallest $n$ with $\Omega(n) = k$ is $2^k \geq 2$, so the sum from $2$ equals the
full stratum sum) tends to 1 as $k \to \infty$ (since $k^2/2^k \to 0$ elementarily,
so F3's correction term $-ck^2/2^k \to 0^-$ as $k \to \infty$, meaning the sum approaches 1 from below). Hence $\sum_k T_k(2)$ diverges by
the divergence test (terms $\to 1 \neq 0$); but this does not bound $\sum_{a \in A_\mathrm{lg}} 1/(a\ln a)$
since $A_\mathrm{lg}$ intersects each stratum sparsely.

**Reduction remark**: If one could prove $\sum_{a \in A_{\mathrm{lg}}} 1/(a \ln a) = o(1)$,
the conjecture would reduce to showing $\sum_{a \in A_{\mathrm{sm}}} 1/(a \ln a) \leq 1 + o(1)$
for any primitive $A_{\mathrm{sm}} \subset [x,\infty)$ with $p_{\min}(a) < x$ for all $a$.
That sub-problem is also open.

See `proof_lemmas/lemma_prime_factor_split.md` for the precise gap statement.

---

## Section 6 — A_sm decomposition by smallest prime factor (Q12, continued)

**Setup**: Recall $A_{\mathrm{sm}} = \{a \in A : p_{\min}(a) < x\}$. For each prime
$p < x$, define the $p$-class:
$$A(p) := \{a \in A : p_{\min}(a) = p\}.$$

Then $A_{\mathrm{sm}} = \bigsqcup_{p < x,\, p \text{ prime}} A(p)$ (disjoint union).

**Lemma (`sm_quotient_primitive`, status: proved)**: For each prime $p < x$,
the quotient set $B(p) := \{a/p : a \in A(p)\}$ is a primitive set.

*Proof*: Suppose $b, b' \in B(p)$ are distinct with $b \mid b'$. Set
$a = pb$, $a' = pb' \in A(p) \subseteq A$. Then $a \mid a'$ (since $b \mid b'$
and $p \mid p$). But $A$ is primitive, so no distinct $a, a' \in A$ satisfies
$a \mid a'$. Contradiction. Similarly $b' \nmid b$. $\square$

**Properties of $B(p)$**: Each $b \in B(p)$ satisfies:
1. $b = a/p \geq x/p$ and $b$ is a positive integer. We claim $b \geq 2$:
   if $b = 1$ then $a = p < x$ (since $p < x$), contradicting $a \in A \subset [x,\infty)$.
   So $b \geq 2$ for ALL primes $p < x$, regardless of whether $p \leq x/2$ or not.
2. $p_{\min}(b) \geq p$: if some prime $q < p$ divides $b$, then $q \mid pb = a$,
   giving $p_{\min}(a) \leq q < p$, contradicting $p_{\min}(a) = p$.

So $B(p) \subset \{n \geq 2 : p_{\min}(n) \geq p\}$ is a primitive set.

**Per-$p$ contribution bound**: The contribution of $A(p)$ satisfies:
$$\sum_{a \in A(p)} \frac{1}{a \ln a}
  = \sum_{b \in B(p)} \frac{1}{pb \cdot \ln(pb)}.$$
Since $b \geq 2$ and $p \geq 2$, both $b$ and $pb$ are $\geq 2$, so $\ln b > 0$.
Since $p \geq 2 > 1$, we have $\ln p > 0$ (logarithm is increasing and $\ln 1 = 0$), so
$\ln(pb) = \ln p + \ln b > \ln b > 0$. In particular $\ln(pb) \geq \ln b$
and $1/\ln(pb) \leq 1/\ln b$, giving:
$$\frac{1}{pb \cdot \ln(pb)} \leq \frac{1}{pb \cdot \ln b}
  = \frac{1}{p} \cdot \frac{1}{b \ln b}.$$
Summing over $B(p)$ and applying **F1** to the primitive set $B(p) \subseteq \{n \geq 2\}$:
$$\sum_{a \in A(p)} \frac{1}{a \ln a} \leq \frac{1}{p} \sum_{b \in B(p)} \frac{1}{b \ln b} < \frac{e^{\gamma}\pi/4}{p}.$$

**Why summing over $p$ fails**: Summing over all primes $p < x$:
$$\sum_{a \in A_{\mathrm{sm}}} \frac{1}{a \ln a}
  < e^{\gamma}\frac{\pi}{4} \cdot \sum_{\substack{p < x \\ p \text{ prime}}} \frac{1}{p}.$$
This upper bound does NOT tend to $0$ as $x \to \infty$: for all $x > 2$,
the prime $p = 2 < x$ contributes $1/p = 1/2$ to the sum (since $2 < x$ whenever $x > 2$), so
$\sum_{p<x} 1/p \geq 1/2$, giving $e^\gamma\pi/4 \cdot \sum_{p<x} 1/p \geq e^\gamma\pi/8 > 0$.
The bound is bounded below by a positive constant for all $x > 2$, so it
cannot show $\sum_{a \in A_{\mathrm{sm}}} 1/(a\ln a) = o(1)$.

**Why per-$p$ bounds fail globally**: Each $B(p)$ is controlled by F1
independently, but the $B(p)$ are NOT independent — they derive from a single
primitive set $A$, and cross-$p$ constraints prevent the $A(p)$ from being
simultaneously large across many primes $p < x$.

Specifically: for $a \in A(p)$ and $a' \in A(q)$ with primes $p \neq q < x$,
primitivity forces $a \nmid a'$ and $a' \nmid a$. These cross-$p$ constraints
are not used by the per-$p$ F1 bound.

**Reformulation of the A_sm obstacle**: To bound $\sum_{a \in A_{\mathrm{sm}}} 1/(a\ln a)$,
one needs an argument that uses the full primitivity of $A_{\mathrm{sm}}$ as a whole
(across all $p$-classes simultaneously), not just the internal primitivity of
each $A(p)$.

**Structural observation**: The map $a \mapsto (p_{\min}(a), a/p_{\min}(a))$
sends $A_{\mathrm{sm}}$ injectively into $\bigcup_{p<x} \{p\} \times B(p)$. The
cross-$p$ primitivity of $A_{\mathrm{sm}}$ translates to: for $p \neq q$ and
$b \in B(p)$, $b' \in B(q)$, neither $pb \mid qb'$ nor $qb' \mid pb$. These
constraints link the quotient sets $B(p)$ across different primes.

See `proof_lemmas/lemma_sm_prime_grouping.md` for the precise formulation.

---

## Section 7 — Directional cross-$p$ structural constraint (Q12, continued)

**Setup**: For distinct primes $p < q$, both $< x$, any $a \in A(p)$ writes as
$a = pb$ with $p_{\min}(b) \geq p$, and any $a' \in A(q)$ writes as $a' = qb'$
with $p_{\min}(b') \geq q$.

**Lemma (`sm_directional_no_div`, status: proved; see `proof_lemmas/lemma_sm_directional_constraint.md`)**:
For any $a \in A(p)$ and $a' \in A(q)$ with distinct primes $p < q < x$,
$a \nmid a'$ — automatically, without using primitivity of $A$.

*Proof*: Suppose $pb \mid qb'$. Then $p \mid qb'$. Since $p$ is prime:
either $p \mid q$ or $p \mid b'$.
But $p < q$ with $q$ prime implies $p \nmid q$ (distinct primes).
And $p < q \leq p_{\min}(b')$ implies $p$ is not a prime factor of $b'$, so $p \nmid b'$.
Both cases fail: contradiction. $\square$

**Directional asymmetry**: The cross-$p$ non-divisibility is directional:
- **Upward** ($a \in A(p)$ vs.\ $a' \in A(q)$, $p < q$): $a \nmid a'$ holds
  **structurally** (Lemma above, no primitivity needed).
- **Downward** ($a' \in A(q)$ vs.\ $a \in A(p)$, $p < q$): $a' \nmid a$ is excluded
  by **primitivity** of $A$ (not structural — the lemma does NOT apply in this direction).

**Consequence**: Primitivity of $A$ is needed to rule out only the downward cross-$p$
direction. The upward direction is free.

**What downward divisibility would force**: Suppose $a' = qb' \in A(q)$ divided
$a = pb \in A(p)$ with $p < q$ (hypothetically — primitivity forbids this):
Then $qb' \mid pb$. Since $q \mid qb'$ and $qb' \mid pb$, we have $q \mid pb$.
Since $q$ is prime and $\gcd(q, p) = 1$ (distinct primes), from $q \mid pb$ we get $q \mid b$ by Euclid's lemma. (Derivation: Bézout gives $qs + pt = 1$ for some integers $s, t$; multiply by $b$: $qsb + ptb = b$; then $q \mid qsb$ and $q \mid pb$ so $q \mid t(pb) = ptb$; hence $q \mid b$.)
Also $p < q \leq p_{\min}(b')$ means $p$ is strictly less than every prime factor of $b'$, so $p \nmid b'$, giving $\gcd(p, b') = 1$; and $p \nmid q$ (distinct primes), so $\gcd(p, q) = 1$. Since $p$ is prime and $\gcd(p, q) = \gcd(p, b') = 1$, we have $\gcd(p, qb') = 1$ (as $p$ divides neither $q$ nor $b'$, hence not their product).
Now $qb' \mid pb$ and $\gcd(qb', p) = 1$: by the coprime-divisibility lemma (if $\gcd(m,n)=1$ and $m \mid nk$ then $m \mid k$, proved via Bézout: $ms + nt = 1 \Rightarrow msk + ntk = k$, so $m \mid k$), with $m = qb'$, $n = p$, $k = b$: since $\gcd(qb', p) = 1$ and $qb' \mid pb$, we get $qb' \mid b$. Since $b' \geq 2$ (as shown in
Section 6 for $B(q)$, because $b'=1$ would require $a' = q < x$, contradicting $a' \geq x$):
$$qb' \geq 2q \geq 4 \quad (q \geq 2,\; b' \geq 2),$$
so $b \geq qb' \geq 2q$. Thus downward divisibility forces $b$ to be a multiple of $qb'$,
a quantity $\geq 2q \geq 4$; this places strong lower bounds on elements of $B(p)$ that could
participate in such a divisibility relation.

**Cross-set constraint reformulated**: Primitivity of $A$ (in the downward cross-$p$ direction)
requires: for all primes $p < q < x$ and all $b' \in B(q)$, no element of $B(p)$ is divisible
by $qb'$. That is, $B(p) \cap qb' \mathbb{Z} = \emptyset$ is required for each $b' \in B(q)$.
(Note: the constraint is $qb' \nmid b$ for all $b \in B(p)$, which is equivalent, given $\gcd(p, qb') = 1$,
to $qb' \nmid b$, i.e.\ no $b \in B(p)$ is a multiple of $qb'$.)

**Why this helps**: The upward structural constraint (Lemma `sm_directional_no_div`)
removes half of the cross-$p$ primitivity conditions automatically. What remains is
a one-directional constraint: for $p < q$, no multiple of $qb'$ (with $b' \in B(q)$)
can appear in $B(p)$. This is a genuine sieve-type condition on $B(p)$ imposed by
$B(q)$, for every $q > p$.

**Open direction**: If the sets $\{qb' : b' \in B(q), q > p\}$ are "dense" enough in
the integers, they sieve out most of $B(p)$, forcing $\sum_{b \in B(p)} 1/(pb \ln(pb))$
to be small. Whether this sieve density is controllable — and whether summing over
all $p$ then gives $\sum_{a \in A_{\mathrm{sm}}} 1/(a \ln a) = o(1)$ or $\leq 1 + o(1)$ —
remains the central open problem for the $A_{\mathrm{sm}}$ component.

See `proof_lemmas/lemma_sm_directional_constraint.md` for the precise statement.
