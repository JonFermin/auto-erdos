---
id: prime_tail_vanish
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma: prime tail vanishes

**Statement**: For any $x \geq 2$,
$$T_1(x) := \sum_{\substack{p \geq x \\ p \text{ prime}}} \frac{1}{p \ln p} \;\to\; 0
  \quad \text{as } x \to \infty.$$

**Proof**:

The set $\mathbb{P}$ of all primes is a primitive set: no prime divides another
distinct prime (if $p \mid q$ with $p,q$ prime and $p \neq q$, then $p \leq q/p < q$
contradicts minimality of $q$; actually $p \mid q$ prime forces $p = q$). By **F1**
(Erdős–Zhang), applied to the primitive set $A = \mathbb{P}$:
$$\sum_{p \in \mathbb{P}} \frac{1}{p \ln p} < e^{\gamma} \frac{\pi}{4}.$$

In particular, the series $\sum_{p} 1/(p \ln p)$ converges absolutely. The tail
$$T_1(x) = \sum_{p \geq x,\, p \text{ prime}} \frac{1}{p \ln p}$$
is the tail of a convergent series of non-negative terms, hence $T_1(x) \to 0$
as $x \to \infty$. $\square$

**Notes**:
- This lemma uses only **F1** and the fact that the primes form a primitive set.
- It is used in Section 5 to bound the $\Omega = 1$ stratum of $A_{\mathrm{lg}}$.
- The result $T_1(x) \to 0$ is consistent with both F2 and F3: F2 gives a lower
  bound on the FULL prime sum $\sum_{p \text{ prime}} 1/(p \ln p)$ (with unsigned
  big-O), not a lower bound on $T_1(x)$.
