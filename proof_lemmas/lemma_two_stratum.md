---
id: two_stratum
status: open
depends_on: [single_stratum_bound, cross_stratum]
discharged_by_round: null
introduced_at_round: 9
---

# Lemma: two-stratum primitive sets satisfy the conjecture

**Claim**: Let $1 \leq j < k$ and let $A = A_j \cup A_k$ be a primitive set
with all elements in stratum $j$ or $k$. Then
$$S_j(A) + S_k(A) = \sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1).$$

**Known bounds from F3**: By `lemma_single_stratum_bound`:
- $S_j(A) \leq 1 - (c+o(1))j^2/2^j =: 1 - \delta_j$ where $\delta_j > 0$.
- $S_k(A) \leq 1 - (c+o(1))k^2/2^k =: 1 - \delta_k$ where $\delta_k > 0$.

Summing: $S_j(A) + S_k(A) \leq 2 - \delta_j - \delta_k$. This is at most
$2 - \delta_j - \delta_k < 2$. For the conjecture we need $\leq 1$, so the
separate bounds are insufficient by a factor of $\approx 1$.

**Inter-stratum exclusion.** By primitivity: for every $a \in A_j$ and
$b \in A_k$, we need $a \nmid b$. This means the elements of $A_k$ avoid
all multiples of elements of $A_j$ in the $k$-th stratum.

**Excluded mass from $A_k$**. The elements excluded from $A_k$ by a single
$a \in A_j$ (with $\Omega(a) = j$) are $\{b: \Omega(b)=k, a|b\}$. Writing
$b = a \cdot m$ with $\Omega(m) = k - j$, the excluded sum is:
$$E_{j,k}(a) = \sum_{m:\,\Omega(m)=k-j} \frac{1}{a m \log(am)}.$$

If $E_{j,k}(a)$ can be related to $S_j$ in a useful way, we might be able
to show that the "gain" from $A_j$ (adding $S_j(A)$ to the total) is at
most offset by the "loss" in $A_k$ (the excluded mass $E_{j,k}$), keeping
the combined sum $\leq 1$.

**Obstacle**: To bound $E_{j,k}(a)$ below (from the contribution side),
we need estimates on the density of $k-j$-stratum elements — essentially
another application of F3. But $E_{j,k}(a) = \sum_{m:\Omega(m)=k-j} 1/(am \log(am))$
involves a Dirichlet convolution that doesn't directly simplify to F3's
formula (because $\log(am) \neq \log a + \log m$ in the needed way).

**Scale of the gap**: Even for $(j,k) = (1,2)$ (primes and semiprimes), the
naive sum of F3 bounds gives $S_1 + S_2 \leq (1 - \delta_1) + (1 - \delta_2)$
with $\delta_j = (c+o(1))j^2/2^j$. Since $\delta_j$ is small (decaying rapidly
in $j$, with $\delta_j \ll 1$ for all $j$), the naive bound is close to 2,
not 1. The inter-stratum exclusion must supply the missing unit of "mass."

The exclusion argument must supply the missing $\approx 0.9$. This seems
plausible given the strong constraint (all multiples of each prime in $A_1$
are excluded from $A_2$), but making it rigorous requires quantitative
estimates not available in F1/F2/F3 alone.

**Current obstacle**: The exclusion bound $E_{j,k}(a)$ requires estimating
a Dirichlet convolution involving the $(k-j)$-stratum sum. This in turn
depends on F3-style asymptotic formulas for the stratum sum with a restricted
set of divisors — a variant of F3 that is not stated in the ledger.

**Next moves**: Explore whether the $(j,k) = (1,2)$ case (prime + semiprime
stratum) can be handled using only F1/F2/F3, or whether the two-stratum
conjecture is itself as hard as the full conjecture.
