---
id: primes_are_extremal
status: open
depends_on: [stratum_bound, cross_stratum_constraint]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma: Primes achieve the maximum sum among primitive sets

**Statement.** For any $x \geq 2$ and any primitive set $A \subset [x, \infty)$,

$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p \text{ prime}, p \geq x} \frac{1}{p \log p}.$$

**Current status: OPEN.** This is essentially the Erdős conjecture itself
(the Lichtman–Pomerance 2021 paper proves this for all $x$).

**Approach attempt.** We outline the sieve-based strategy:

1. *Multiplicative weight function.* Define $w : \mathbb{N} \to \mathbb{R}_{>0}$
   by $w(n) = 1/(n \log n)$. The conjecture is that $\sum_{a \in A} w(a)$
   is maximized by $A = P_x := \{p \text{ prime} : p \geq x\}$.

2. *Fundamental lemma.* For any $n \geq 2$,
   $$\sum_{d \mid n, d > 1} \frac{1}{d \log d} \geq \frac{1}{\log n}.$$
   *Sketch:* For $n = p$ prime, the only divisor $> 1$ is $n$ itself, giving
   $1/(p \log p)$. We need this to be $\geq 1/\log n = 1/\log p$, i.e.,
   $1/(p \log p) \geq 1/\log p$, which gives $1/p \geq 1$. FALSE for $p \geq 2$.
   This approach fails immediately — the fundamental lemma as stated is false.

3. *Revised approach.* The actual proof likely uses a different inequality.
   One candidate: for any primitive set $A$,
   $$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{a \in A} \frac{\log\log a}{\log a} \cdot \frac{1}{a}$$
   but this requires knowing that $\log \log a / \log a \cdot (1/a)$ is maximized
   at primes, which is not obviously true.

**Current obstacle.** The fundamental combinatorial inequality that makes
primes extremal is not yet clear. The Lichtman–Pomerance proof uses a
Rankin-type bound, which may be worth transcribing in a future session.

See: Lichtman, J.D. and Pomerance, C. (2021), "Primitive sets with large
counting functions," *Publ. Math. Debrecen*, for the proof.
