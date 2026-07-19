---
id: prime_sum_numerics
status: verified_numerically
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

> Concluded `primitive_set_erdos` attempt (claim proved in the literature,
> May 2026, arXiv:2605.00301); retained as audit trail, not load-bearing for
> any active chain. Per the falsify-critic contract, one-line sandbox
> re-derivations are not expected for this file; deterministic re-checks, if
> any, live in its CHECK blocks.

# Lemma 2 (renamed: Prime sum — numerical verification)

**Claim (numerically verified).** $P(x) := \sum_{p \geq x, p \text{ prime}} 1/(p \log p)$
satisfies $P(x) < 1$ for all $x \geq 3$, and $P(x) \to 0$ as $x \to \infty$.

**Numerical evidence (from Section 3):**

| $x$ | $P(x) \approx$ | Below 1? |
|-----|----------------|----------|
| 2 | 1.637 | No |
| 3 | 0.916 | **Yes** |
| 100 | 0.217 | Yes |
| 1000 | 0.145 | Yes |

At $x = 3$: $P(3) \approx 0.916 < 1$, so any primitive set of primes from $x \geq 3$
automatically satisfies the conjecture's $< 1$ threshold IF Lemma 3 (prime extremality) holds.

**Note.** The asymptotic $P(x) \sim 1/\log x$ is a standard result from analytic
number theory (prime number theorem + partial summation) used here only as informal
motivation. The formal claim is just the numerical observation $P(x) < 1$ for $x \geq 3$.

**Consequence.** If Lemma 3 (prime extremality) holds, then for $x \geq 3$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq P(x) < 1 \leq 1 + o(1)$$
for any primitive $A \subseteq [x, \infty)$. The conjecture would follow.
