---
id: total_bound
status: open
depends_on: [primes_stratum, higher_strata_tails, cross_stratum]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 4: Total Sum Bound (Combines All Strata)

**Statement**: Let $A \subseteq [x, \infty)$ be primitive. Then
$$\sum_{a \in A} \frac{1}{a \ln a} < 1 + o(1) \quad \text{as } x \to \infty.$$

**Proof sketch** (conditional on Lemmas 2 and 3):

Decompose: $\sum_{a \in A} 1/(a \ln a) = \Sigma_1 + \sum_{k \geq 2} \Sigma_k$
where $\Sigma_k = \sum_{a \in A, \Omega(a)=k} 1/(a \ln a)$.

By Lemma 1: $\Sigma_1 \leq \sum_{p \geq x} 1/(p \ln p) \approx 1/\ln x \to 0$.
By Lemma 2: each $\Sigma_k \leq T_k(x) \to 0$ as $x \to \infty$.
By Lemma 3 (the hard part): the cross-stratum coupling gives a tighter bound when
$\Sigma_1 > 0$, preventing the total from approaching 1.

**The gap**: Lemmas 1 and 2 together give $\sum_a 1/(a \ln a) \leq \sum_{k \geq 1} T_k(x)$.
But $\sum_{k \geq 1} T_k(x) = \sum_{n \geq x} 1/(n \ln n) = \infty$, so this bound is
useless. The cross-stratum exclusion from Lemma 3 is ESSENTIAL — without it, the bound
cannot be closed.

**What's needed**: A quantitative version of Lemma 3 showing that
$$\sum_{k \geq 1} \Sigma_k < 1 + o(1).$$

The only known approach (in the given facts) is F1 (Zhang's theorem), which gives
$\sum_k \Sigma_k < 1.399 + o(1)$. Tightening to $1 + o(1)$ is the open conjecture.

**Current status: OPEN.** This is the conjecture itself, restated. Without a proof of
Lemma 3, this lemma cannot be discharged.
