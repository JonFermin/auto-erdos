---
id: cross_stratum
status: open
depends_on: [primes_stratum, higher_strata_tails]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 3: Cross-Stratum Coupling (The Hard Lemma)

**Statement**: The global primitivity constraint on $A$ creates anti-correlations between
strata: if $A^{(1)} = A \cap \{\text{primes}\}$ is large (many primes $\geq x$), then
$A^{(k)} = A \cap A_k$ for $k \geq 2$ must avoid all multiples of primes in $A^{(1)}$.

More precisely: Let $A \subseteq [x, \infty)$ be primitive. For each prime $p \in A^{(1)}$
and each $k \geq 2$, the set $A^{(k)}$ contains no multiple of $p$.

**Consequence (informal)**: A large primes contribution forces the higher strata to
"avoid" multiples of those primes. In the extreme case where $A^{(1)} = $ all primes $\geq
x$, the set $A^{(\geq 2)} = \emptyset$ since every integer $\geq x$ with $\Omega \geq 2$
has a prime factor $\geq x$ (for $x$ prime) or below $x$ (for small prime factors).

Wait — that's NOT correct. If $x = 100$ and $p = 101$ (a prime in $A^{(1)}$), then
$202 = 2 \times 101 \in A_2$ is a multiple of $p$, so $202 \notin A$. But $4 = 2^2 \in
A_2$ with $\Omega(4) = 2$ could still be in $A^{(2)}$ (since $4 < x = 100$, it's not
in $[x, \infty)$). For elements $\geq x$: $n = 2 \times 101 = 202$ is excluded if
$101 \in A^{(1)}$.

**The key interaction**: If $A^{(1)}$ contains many primes, then $A^{(2)}$ is restricted
to $k$-almost-primes $n \geq x$ whose prime factors are NOT in $A^{(1)}$.

**Formalizing the trade-off**: Let $P_1 = \{p \in A^{(1)}\}$ be the set of primes chosen.
The sum contribution is:
$$\Sigma_1 = \sum_{p \in P_1} \frac{1}{p \ln p}$$
and the contribution from $A^{(2)}$ is constrained to numbers avoiding all $P_1$-factors:
$$\Sigma_{\geq 2} \leq \sum_{\substack{n \geq x, \Omega(n) \geq 2 \\ p \nmid n \; \forall p \in P_1}} \frac{1}{n \ln n}.$$

The total $\Sigma_1 + \Sigma_{\geq 2}$ must be bounded by $1 + o(1)$. The challenge is
showing that increasing $P_1$ (larger $\Sigma_1$) forces a decrease in $\Sigma_{\geq 2}$
fast enough to keep the total below $1 + o(1)$.

**Known cases**:
- If $P_1 = $ all primes $\geq x$: $\Sigma_1 \approx 1/\ln x$ and $\Sigma_{\geq 2} = 0$
  (all multiples of primes $\geq x$ are excluded from $[x,\infty)$... wait, not exactly:
  $n = p \cdot q \geq x$ for small $q$ and large $p \geq x$ would be excluded if
  $p \in P_1$, but for $n \geq x$ with both prime factors $< x$, it's not excluded).
- If $P_1 = \emptyset$: $\Sigma_1 = 0$ and $\Sigma_{\geq 2}$ can be maximized; but by
  Lemma 2, even $\sum_k T_k(x)$ might be large.

**Current status: OPEN.** This is the central difficulty of the conjecture. The coupling
between strata is non-trivial and not handled by existing techniques in the given facts
(F1, F2, F3). A full proof likely requires a new analytical tool.

**What a proof might look like**:

Approach A (Sieve-theoretic): Model the restriction using multiplicative sieves. The sum
$\sum_{n \geq x, \Omega(n) \geq 2, p \nmid n \; \forall p \in P_1} 1/(n \ln n)$ can be
estimated by a sieve that removes multiples of primes in $P_1$. By inclusion-exclusion or
the Turán sieve, this sum decreases as $|P_1|$ grows.

Approach B (Dirichlet series / analytic): Consider the generating Dirichlet series
$F_A(s) = \sum_{a \in A} a^{-s}$ for a primitive set. Erdős used the identity
$\zeta(s) = \prod_{a \in A} (1 - a^{-s})^{-1} \cdot G(s)$ for some "error" $G$ related
to the complement, but this is not straightforward.

Approach C (Probabilistic): Model $A$ as a random primitive set and show the expected
total sum is $< 1 + o(1)$ with high probability. Conditioning on the primes chosen forces
a reduction in the composite terms.

None of these approaches is complete with the given facts. This lemma is the main obstacle
to a full proof.
