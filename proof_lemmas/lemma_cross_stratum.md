---
id: cross_stratum
status: open
depends_on: [within_stratum]
discharged_by_round: null
introduced_at_round: 7
---

# Lemma: cross-stratum interaction bound

**Statement**: Let $A \subset [x, \infty)$ be a primitive set. Partition
$A = \bigsqcup_{k \geq 1} A_k$ where $A_k = \{a \in A : \Omega(a) = k\}$.
Then $\sum_{k \geq 1} S_k(A) \leq 1 + o(1)$ as $x \to \infty$.

This is equivalent to the Erdős primitive-set conjecture.

**What the stratification reveals**: By `lemma_within_stratum`, primitivity
is vacuous within each $A_k$. The cross-stratum condition says: for
$a \in A_j$ and $b \in A_k$ with $j < k$, if $a | b$ then $b \notin A$.
This creates "holes" in higher strata: any multiple of a prime $p \in A_1$
with $\Omega \geq 2$ is excluded from $A$.

**Role of F1**: F1 (Erdős-Zhang, $\approx 1.399$) gives the global upper
bound on the sum over any primitive set. This is the best unconditional
bound from the ledger; it is above 1, so F1 alone does not prove the
conjecture.

**Role of F3**: F3 identifies the extremal family (primes in a short
interval) as approaching 1 from below. The correction $-(c+o(1))k^2/2^k$
is negative and decays rapidly, suggesting higher strata contribute
negligibly in the extremal family. If this pattern holds for all primitive
sets — not just the extremal family — it would yield the conjecture.
Establishing this uniformity is precisely the hard part.

**Role of F2**: F2's stratum lower bound $\Omega(k^{-1/2+o(1)})$ is
unsigned. It cannot be used to establish that the total exceeds or is
bounded by any specific constant.

**Key obstacle**: To prove $\sum S_k(A) \leq 1 + o(1)$ for all primitive
$A \subset [x, \infty)$, one needs to show that inter-stratum exclusions
force sufficient sparsity in every stratum simultaneously. This is a global
condition on the full primitive set, not decomposable stratum by stratum.
The Maier–Tenenbaum approach (which underlies F1 and similar results) uses
multiplicative structure and sieve theory; the exact $o(1)$ improvement
to reach the conjectured bound of $1$ rather than $1.399$ is not known
to follow from F1/F2/F3 alone.

**Next directions** (for future sessions):
1. Check whether F3's rapid-decay correction term can be used to bound
   higher-stratum contributions uniformly (not just for the extremal family).
2. Explore whether any sieve-type argument using only PNT-level inputs
   (foundational, not requiring a new ledger entry) can close the gap
   from F1's bound of $1.399$ to the conjectured $1$.
3. Continue the witness search at larger $x_\text{floor}$ values to
   confirm the conjecture computationally.
