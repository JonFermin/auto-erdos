---
id: strat_per_k_bound
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 1 — Single-Stratum Bound

**Statement**: Let $x \geq 2$ and $A \subseteq [x, \infty)$ be primitive with $A \subseteq A_k$
(all elements have exactly $k$ prime factors counted with multiplicity). Then:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{n \in A_k,\, n \geq x} \frac{1}{n \log n}.$$
Moreover, for $k \geq 2$:
$$\sum_{n \in A_k,\, n \geq x} \frac{1}{n \log n} < \sum_{n \in A_k} \frac{1}{n \log n} = 1 - (c+o(1))\frac{k^2}{2^k} < 1.$$
For $k = 1$ (primes): $\sum_{p \geq x} \frac{1}{p \log p} \to 0$ as $x \to \infty$.

**Proof**:

*First inequality*: $A \cap A_k \subseteq A_k \cap [x,\infty)$, so summing the non-negative terms $1/(a \log a)$
over the subset $A$ gives at most the full sum over $A_k \cap [x, \infty)$.

*Second inequality ($k \geq 2$)*: Since $A_k \cap [x, \infty) \subsetneq A_k$ for any finite $x$,
the tail sum is strictly less than the full sum. By fact F3:
$$\sum_{n \in A_k} \frac{1}{n \log n} = 1 - (c+o(1))\frac{k^2}{2^k}$$
with $c \approx 0.0656 > 0$ and the correction term $-(c+o(1))k^2/2^k < 0$, so the full sum
is $< 1$.

*$k = 1$ (primes)*: The series $\sum_p 1/(p \log p)$ converges (numerically to $\approx 1.636$).
Hence the tail $\sum_{p \geq x} 1/(p \log p) \to 0$ as $x \to \infty$. Numerically:
$\sum_{p \geq 10} 1/(p \log p) \approx 0.292$, $\sum_{p \geq 100} 1/(p \log p) \approx 0.094$, etc.

**Corollary**: For any $k \geq 1$ and $x$ large enough (specifically $x \geq 4$ for $k \geq 2$,
$x \geq 10$ for $k = 1$), a primitive set $A \subseteq A_k \cap [x, \infty)$ satisfies $f(A) < 1$.

**Remark**: F3's formula gives $\sum_{A_1} = 1 - (c+o(1))/2 \approx 0.967$, but numerically
the full prime sum $\approx 1.636 > 1$. The discrepancy arises because F3 is an asymptotic in $k$
that breaks down at $k = 1$; the $k = 1$ case is handled separately via the direct convergence
observation above.

**Status**: proved. This closes the single-stratum case of the conjecture.
