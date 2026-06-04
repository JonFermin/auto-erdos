---
id: cross_stratum_primitivity
status: open
depends_on: [stratum_tail_bound]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 2 — Cross-stratum primitivity exclusion

**Statement.** Let $A \subseteq [x, \infty)$ be a primitive set. Partition $A = \bigcup_{k \geq 1} A^{(k)}$ where $A^{(k)} = \{a \in A : \Omega(a) = k\}$. For any prime $p \in A^{(1)}$, all composites in $A$ with $p$ as a factor are excluded. More precisely:

If $p \in A^{(1)}$, then $A \cap \{p \cdot m : m \geq 2,\, m \text{ integer}\} = \emptyset$.

**Proof.** Immediate from primitivity: if $p \in A$ and $p | b$ for some $b \in A$ with $b \neq p$, then $p$ divides $b$, violating the "no element divides another" condition. $\square$

**Consequence (exclusion count).** Each prime $p \in A^{(1)}$ excludes all multiples $\{2p, 3p, 4p, \ldots\} \cap [x, \infty)$ from $A$. The "cost" in potential sum is:
$$\sum_{m \geq 2,\, pm \geq x} \frac{1}{pm \log(pm)}$$
which is roughly $\frac{1}{p \log p} \sum_{m=2}^\infty \frac{1}{m \log m}$ — a divergent sum! This means the gain from including prime $p$ (which is $1/(p \log p)$) is "offset" by excluding the entire arithmetic progression $p \cdot \{2, 3, \ldots\}$.

**Current obstacle.** To use this exclusion quantitatively, we need to show that NO alternative choice of composites (avoiding divisibility by $p$) can compensate for the lost elements. Specifically, we want to show that for any primitive $A' \subseteq [x, \infty)$ with $p \notin A'$ (so that $p$ and all its multiples are available for replacement by other composites), we have:
$$\sum_{a \in A'} \frac{1}{a \log a} \leq \sum_{a \in A} \frac{1}{a \log a}.$$
This "local exchange" argument would show that the all-primes set is optimal — which is Lemma 3. The difficulty is that composites with small factors can be dense near $x$, potentially beating the prime density $1/\log x$ in a specific interval.

**Next steps:**
1. Try a Plünnecke/Ruzsa-style inequality bounding the sum density of the complement.
2. Look for a comparison with the Zhang proof (which uses the $1/\log n$ weight in a sieve argument).
3. Alternatively, prove a weaker "stratum dominance" lemma: the sum over $A^{(1)}$ (primes in $A$) $\geq$ sum over $A^{(k)}$ for any $k > 1$, when measured in the same $[x, 2x]$ interval.
