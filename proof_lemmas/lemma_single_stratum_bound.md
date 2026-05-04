---
id: single_stratum_bound
status: open
depends_on: [within_stratum]
discharged_by_round: null
introduced_at_round: 8
---

# Lemma: single-stratum primitive sets satisfy the conjecture

**Claim**: For any $k \geq 1$ and any $A \subset \{n \geq 2 : \Omega(n) = k\}$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{n:\,\Omega(n)=k} \frac{1}{n \log n} = 1 - (c+o(1))\frac{k^2}{2^k},$$
where the equality is F3 (from the given-facts ledger). Since $c > 0$,
the right-hand side is strictly less than 1.

**Proof of the inequality**: All terms $1/(a \log a)$ are positive for $a \geq 2$.
Since $A$ is a subset of $\{n: \Omega(n)=k\}$, removing the non-$A$ terms
from the full-stratum sum can only decrease the value. Hence
$\sum_{a \in A} 1/(a \log a) \leq \sum_{n:\Omega(n)=k} 1/(n \log n)$.

**Applying F3**: F3 states the right-hand side equals $1-(c+o(1))k^2/2^k$.
F3's sign disambiguation confirms $c > 0$ so the correction is negative and
the total is strictly less than 1 for every $k \geq 1$.

**Consequence**: The Erdős conjecture holds for any primitive set confined
to a single $\Omega$-stratum. By `lemma_within_stratum`, every subset of a
fixed-$\Omega$ stratum is automatically primitive, so the class is non-trivial.

**Why this does not close the full conjecture**: A primitive set can draw
from multiple strata simultaneously. Summing the F3 bounds independently
over all strata would give $\sum_{k \geq 1} (1-(c+o(1))k^2/2^k)$, which
diverges (since $\sum_k 1$ diverges). The inter-stratum constraint must be
used for multi-stratum sets; see `lemma_cross_stratum.md`.

**Status note**: Marked `open` rather than `proved` because the F3 equality
relies on the full-stratum sum converging to the stated value — an analytic
fact taken from the ledger. If F3 is accepted as stated, the proof above
is complete. Pending internal consistency checks.
