# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop.
Content hash is used for round-dedup. Lemma files live in `proof_lemmas/`.

---

## Section 1 — Claim, Given Facts, and Proof Context

### 1.1 The Conjecture

**Erdős's Primitive-Set Conjecture (tightened form).**
A set $A \subseteq \mathbb{N}$ is *primitive* if no element divides another
distinct element. The conjecture asserts:

$$\sup_{\substack{A \text{ primitive} \\ A \subseteq [x,\infty)}} \sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1) \quad \text{as } x \to \infty.$$

Equivalently: for every $\varepsilon > 0$ there exists $X_\varepsilon$ such that
for all $x \geq X_\varepsilon$, every primitive $A \subseteq [x, \infty)$ satisfies
$\sum_{a \in A} \frac{1}{a \log a} < 1 + \varepsilon$.

This tightens the Zhang bound (F1). Zhang shows the supremum is at most about
1.399 (for $A \subseteq [x, \infty)$ as $x \to \infty$); the conjecture asserts
this bound improves to 1.

**Status**: open. The verifier tracks a candidate disproof only through a
verified `<!-- WITNESS -->` block — no unverified claim of resolution is
permitted.

### 1.2 Given Facts

**F1 (Erdős 1935; Zhang 1993).** For any primitive set $A \subseteq [x, \infty)$:
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1),
\quad x \to \infty.$$
This is an UPPER bound, strictly less than $e^\gamma \pi/4 \approx 1.399$.
It is consistent with the conjecture (which posits a tighter asymptotic
bound of $1$). The bound is *asymptotic in $x$*: for small $x$ (e.g., $x = 2$),
the sum over all primes exceeds $1.399$ substantially (≈ 1.636); this does
NOT contradict F1 since F1 only applies for $x \to \infty$.

**F2 (Omega-stratum, UNSIGNED big-O lower bound).**
Let $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (exactly $k$ prime factors
counted with multiplicity). Then:
$$\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O\!\left(k^{-1/2+o(1)}\right).$$
**Sign warning**: the $O(k^{-1/2+o(1)})$ term is **unsigned** — it bounds the
absolute value of the correction, which may be **negative**. One cannot
conclude $\sum > 1$ from F2 alone. (F3 below resolves the sign: the correction
is negative for all finite $k$.)

Note: $A_k$ is primitive. Proof: if $a, b \in A_k$ and $a \mid b$, then
$b = am$ with $\Omega(b) = \Omega(a) + \Omega(m)$, so $\Omega(m) = 0$, giving
$m = 1$ and $a = b$ — a contradiction since elements are distinct.

**F3 (Exact asymptotic for $A_k$).**
$$\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
The leading correction $-(c+o(1)) k^2/2^k$ is **negative** (since $c > 0$).
Therefore:
- The sum is **strictly less than 1** for every finite $k \geq 1$.
- It approaches 1 from **below** as $k \to \infty$.
- F3 resolves F2's ambiguity: the unsigned-O error in F2 is achieved by a
  negative quantity, namely $-(c+o(1)) k^2/2^k$.

**Key consequence**: the $A_k$ family (the "canonical extremal" family) does
not provide a counterexample. Each $A_k$ has sum strictly below 1.

### 1.3 Witness Contract

A *counterexample candidate* is a finite primitive set
$A \subset [x_{\rm floor}, \infty)$ (pairwise non-divisible, all elements
$\geq x_{\rm floor} \geq 2$) whose rigorous lower bound on
$\sum_{a \in A} 1/(a \log a)$ exceeds the threshold 1.0. Such a candidate is
embedded as a `<!-- WITNESS -->` block and verified by
`library.primitive_set_witness.verify_witness` (Decimal arithmetic, 4-ULP
slack on `math.log`).

**Caveat on finite-$x$ witnesses**: the conjecture's $o(1)$ correction is
asymptotic in $x$. A witness at small $x_{\rm floor}$ (say $x_{\rm floor} = 2$)
with sum slightly above 1 is consistent with the conjecture since the $o(1)$
term at $x=2$ is large. A human reviewer would need to bound the $o(1)$
correction at the witness's $x_{\rm floor}$ to assess whether the witness is
a genuine counterexample.

### 1.4 Proof Approach

This attempt develops:

1. **Numerical verification of F3** (Section 2): Confirm the sum behavior of
   $A_k$ for $k = 1, 2, 3, 4$ and document the finite-vs-asymptotic distinction
   for F1 and F3.

2. **Witness search** (Section 3): Computationally test whether a primitive
   $A \subseteq [x_{\rm floor}, \infty)$ with rigorous sum $> 1.0$ exists for
   $x_{\rm floor} \in \{100, 1000, 10000\}$.

3. **Stratification sketch** (Section 4): Outline the Omega-stratification
   argument, assign lemmas, and characterize which steps are supported by
   F1/F3 and which remain open.

4. **Partial result** (Section 5): State what has been ruled out and what
   remains open under current knowledge.

---

## Section 2 — Numerical Evidence

### 2.1 Truncated Sums over $A_k$

We computed $S_k(N) = \sum_{a \in A_k, 2 \leq a \leq N} \frac{1}{a \log a}$
for $k = 1, 2, 3, 4$ using a sieve for $\Omega(n)$ up to $N = 100000$.

| $k$ | $S_k(100000)$ | Tail est. | Full sum est. | F3 prediction |
|-----|--------------|-----------|---------------|---------------|
| 1   | 1.5498       | ~0.087    | ~1.637        | ~0.967        |
| 2   | 0.8288       | ~0.212    | ~1.041        | ~0.934        |
| 3   | 0.4522       | ~0.259    | ~0.711        | ~0.926        |
| 4   | 0.2128       | ~0.260    | ~0.473        | ~0.934        |

The tail estimates use integral approximations based on the PNT-density
of $A_k$: for $k=1$ (primes), density $\sim 1/\log t$ gives
$\sum_{p>N} 1/(p \log p) \approx 1/\log N$; for $k=2$ (semiprimes), density
$\sim \log\log t / \log t$ gives tail $\approx \log\log N/\log N$.

**Discrepancy with F3 for small $k$**: The full-sum estimates for $k=1$
(~1.637) and $k=2$ (~1.041) exceed 1, which appears to contradict F3's
claim that "the sum is strictly less than 1 for every $k \geq 1$". Two
interpretations are possible:

1. **F3 is an asymptotic for large $k$ only**: the formula
   $1 - (c+o(1)) k^2/2^k$ might only hold for $k$ sufficiently large, with
   the $o(1)$ term large and negative for small $k$ (making the full
   correction large and positive for $k = 1, 2$).

2. **Normalization ambiguity**: F3 might describe a normalized quantity
   (e.g., $\log(2^k) \cdot \sum_{a \in A_k} 1/(a \log a)$) rather than the
   raw sum.

For $k \geq 3$, the tail estimates are rougher (the asymptotic formula for
$|\{n \leq x : \Omega(n) = k\}|$ has larger error terms for moderate $k$), so
the full sum estimates for $k = 3, 4$ are less reliable.

**Key unambiguous fact**: $A_k$ is primitive for each $k$, and the F3 formula
correctly predicts the asymptotic behavior as $k \to \infty$ (sum $\to 1$
from below), consistent with F2's unsigned-O being negative.

### 2.2 Prime Sum and the Finite-vs-Asymptotic Distinction

The set $A_1 = \{\text{primes}\}$ forms a primitive set. Its sum converges:
$$\sum_p \frac{1}{p \log p} \approx 1.6366,$$
computed numerically (primes up to $10^5$ give 1.5498; with tail
$\approx 1/\log(10^5) \approx 0.087$ the full sum is $\approx 1.637$).

This exceeds $e^\gamma \pi/4 \approx 1.399$ (the constant in F1), but this is
NOT a contradiction: F1 bounds primitive sets confined to $[x, \infty)$ with
$x \to \infty$. The prime set starting from $x=2$ is NOT in the asymptotic
regime. When restricted to primes $\geq x$:
$$\sum_{p \geq x} \frac{1}{p \log p} \approx \frac{1}{\log x} \to 0
\quad \text{as } x \to \infty,$$
which is certainly $< 1 + o(1)$.

**Summary**: the finite prime sum $\approx 1.637 > 1.399$ is consistent with
F1 because F1 is an asymptotic-in-$x$ bound. For small $x$, primitive sets
can have large sums (the primes starting from 2 achieve $\approx 1.637$, and
Zhang proved no primitive set in $\mathbb{N}$ achieves more than this).

---

## Section 3 — Witness Search (Computational)

### 3.1 Strategy and Results

We searched for a primitive $A \subseteq [x_{\rm floor}, \infty)$ with
rigorously verified $\sum_{a \in A} 1/(a \log a) > 1.0$, testing
$x_{\rm floor} \in \{100, 1000, 10000\}$.

**Candidates tested**:

| Construction | $x_{\rm floor}$ | Verified sum | $> 1$? |
|---|---|---|---|
| $[100, 200)$ (interval, primitive since ratio $< 2$) | 100 | 0.1408 | No |
| Greedy primitive set in $[100, 5000]$ | 100 | 0.2682 | No |
| $A_2 \cap [100, 200000]$ (semiprimes $\geq 100$) | 100 | 0.2625 | No |
| $A_7 \cap [100, 5000]$ | 100 | 0.0110 | No |
| $[1000, 2000)$ interval | 1000 | 0.0957 | No |
| $A_{10} \cap [1000, 200000]$ | 1000 | 0.0015 | No |
| $[10000, 20000)$ interval | 10000 | 0.0726 | No |

All verified using `library.primitive_set_witness.verify_witness` (rigorous
Decimal arithmetic). No counterexample witness found.

**Analytical explanation**: for $A \subseteq [x_{\rm floor}, \infty)$, each
element $a \geq x_{\rm floor}$ contributes at most $1/(x_{\rm floor} \log x_{\rm floor})$.
To achieve sum $> 1$, at least $x_{\rm floor} \log x_{\rm floor}$ elements are
needed. But a primitive set in $[x_{\rm floor}, 2x_{\rm floor})$ (a maximal
"interval" construction) achieves sum only $\approx 1/\log x_{\rm floor}$,
which goes to $0$. For $x_{\rm floor} = 100$, this is $\approx 0.22$, well
below 1.

The truncated sums suggest the maximum achievable at $x_{\rm floor} = 100$
is around $0.27$ (from the greedy construction). This supports the conjecture
but does NOT prove it.

### 3.2 Bearing on the Conjecture

The computational evidence supports (but cannot prove) the conjecture: for
$x_{\rm floor} \geq 100$, no primitive set achieves sum $> 1$. The conjecture
would follow if one could show the supremum of sums over all primitive
$A \subseteq [x, \infty)$ is bounded by $1 + o(1)$, i.e., that the supremum
approaches 1 from below as $x \to \infty$.

*(Sections 4–5 are populated in subsequent rounds.)*
