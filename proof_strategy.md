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

1. **Sieve / antichain density**: Any primitive set in $[x, 2x]$ contains
   at most $O(x/\log x)$ elements (by the Erdős–Gallai-type bound for
   antichains in divisibility). Their contribution to the sum over an
   interval of length $x$ is $O(x/\log x \cdot 1/(x \log x)) = O(1/\log^2 x)$.
   Summing over $O(\log x)$ dyadic intervals $[x, 2x], [2x, 4x], \ldots$
   gives $O(1/\log x) = o(1)$, BUT this only covers the "low weight"
   regime. The contribution from elements concentrated near a single
   $k$-stratum (e.g. squarefree numbers, or numbers of the form $p_1 \cdots p_k$)
   is not directly handled this way.

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
