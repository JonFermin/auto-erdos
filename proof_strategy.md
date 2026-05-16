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

1. **Numerical verification of F3** (Section 2): Confirm the sum over $A_k$
   for $k = 1, 2, 3, 4$ is strictly less than 1, with explicit values. Confirm
   the prime sum ($A_1$ restricted to $[2, \infty)$) and the finite-vs-asymptotic
   distinction.

2. **Witness search** (Section 3): Computationally test whether a primitive
   $A \subseteq [x_{\rm floor}, \infty)$ with rigorous sum $> 1.0$ exists for
   $x_{\rm floor} \in \{100, 1000, 10000\}$.

3. **Stratification sketch** (Section 4): Outline the Omega-stratification
   argument, assign lemmas, and characterize which steps are supported by
   F1/F3 and which remain open.

4. **Partial result** (Section 5): State what has been ruled out and what
   remains open under current knowledge.

*(Sections 2–5 are populated in subsequent rounds.)*
