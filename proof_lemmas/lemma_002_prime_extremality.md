---
id: prime_extremality
status: open
depends_on: [stratum_bound]
discharged_by_round: null
introduced_at_round: 1
---

# Lemma 2: Prime extremality (the hard lemma)

**Statement.** For any primitive set $A \subseteq [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p}.$$

**Significance.** This is the core of the Erdős primitive set conjecture. Combined
with Lemma 2 (prime sum asymptotics), it gives the full conjecture: the sum over any
primitive $A \subseteq [x, \infty)$ is bounded by $(1+o(1))/\log x \to 0$.

**Known proof.** Lichtman–Pomerance (2021), "A proof of the Erdős primitive set
conjecture." Their argument:

1. **Smallest-prime-factor partition.** For each prime $p \geq x$, let
   $A_p = \{a \in A : p(a) = p\}$ where $p(a)$ denotes the smallest prime factor
   of $a$. Then $\{A_p\}_{p \geq x \text{ prime}}$ is a partition of $A$.

2. **Per-prime bound.** Lichtman–Pomerance show:
   $$\sum_{a \in A_p} \frac{1}{a \log a} \;\leq\; \frac{1}{p \log p}.$$
   This is the non-trivial step. Heuristically: $A_p$ consists of integers of the
   form $p \cdot m$ with $\gcd(m, \text{smaller primes}) > 1$ impossible (since $p(a)=p$),
   so $m$ is $p$-smooth-free. The key tool is a comparison inequality for Dirichlet
   series associated to primitive sets restricted to "integers with smallest prime factor $p$."

3. **Summation.** Summing over all $p \geq x$:
   $$\sum_{a \in A} \frac{1}{a \log a} = \sum_{p \geq x} \sum_{a \in A_p} \frac{1}{a \log a}
   \leq \sum_{p \geq x} \frac{1}{p \log p}.$$

**Current obstacle.** Step 2 requires a Beurling-style multiplicative comparison
that is not formalized here. The inequality $\sum_{a \in A_p} 1/(a \log a) \leq 1/(p \log p)$
relies on the structure of "primitive sets with fixed smallest prime factor," which
requires the Dirichlet series comparison developed in Lichtman–Pomerance §3.

This lemma is **not proved in this proof attempt**. Establishing it rigorously
is beyond the scope of the Track 2 loop. This is the reason the proof is a
partial result: the conjecture is likely true (and proved in the literature), but
the proof of Lemma 2 is a genuine hard step this agent cannot close.
