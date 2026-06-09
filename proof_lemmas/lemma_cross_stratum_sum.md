---
id: cross_stratum_sum
status: open
depends_on: [stratum_bound]
discharged_by_round: null
introduced_at_round: 4
---

# Lemma cross_stratum_sum: Total sum across all strata

**Statement.** For any primitive set $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k \geq 1} \sum_{a \in A \cap A_k} \frac{1}{a \log a} < 1 + o(1)$$
as $x \to \infty$.

**Current obstacle.** The per-stratum bound (Lemma stratum_bound) gives each term $< 1$. But summing infinitely many quantities each $< 1$ can diverge. We need to show the SUM over $k$ is small.

**Approach 1: Heavy-stratum / light-stratum split.** For large $k$ ($k \geq K$ for some $K$), each stratum sum is $\leq 1 - c k^2/2^k$ (by F3), so $\sum_{k \geq K} (\text{stratum}_k \text{ bound}) \leq \sum_{k \geq K} 1 = \infty$. This is too crude.

**Approach 2: Primitive set constraint limits cross-stratum density.** A primitive set $A$ satisfies: if $a \in A$ and $a | b$, then $b \notin A$. In particular, for $a \in A \cap A_k$, all multiples of $a$ (which lie in strata $A_{k+j}$ for $j \geq 1$) are excluded from $A$. This "blocks" contributions to higher strata.

The key question: does the primitivity constraint, combined with F3, force $\sum_{k \geq 1} \sum_{a \in A \cap A_k} 1/(a \log a) < 1 + o(1)$?

**Approach 3: Beurling / sieve method.** Erdős's original 1935 proof uses a sieve-like argument. The proof idea is that each "prime factor" of elements in $A$ contributes a controlled amount. Zhang's 1993 improvement (giving the 1.399 bound) uses a more refined sieve. The tighter 1 + o(1) bound would require a new sieve or analytic argument.

**Key partial result available.** By F1 (Zhang 1993), the bound $< 1.399 + o(1)$ is known. The gap from 1.399 to 1 is what needs closing. If the proof can show $< 1 + \varepsilon$ for any fixed $\varepsilon > 0$ once $x$ is large enough, that is the conjecture.

**Open obstacle.** No current proof approach closes this gap. The stratification reduces the problem to: "the maximum over primitive $A$ of $\sum_k (\text{fraction of stratum}_k \text{ captured by } A) \times (\text{stratum}_k \text{ sum})$." This maximum is achieved (in the limit) by the prime set $A_1$ restricted to large $x$, which by our numerics has sum $\to 0 < 1$. But the analytic bound for arbitrary primitive sets is the hard part.
