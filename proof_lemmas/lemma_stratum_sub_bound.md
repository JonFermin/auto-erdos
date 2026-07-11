---
id: stratum_sub_bound
status: proved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma: per-stratum sub-sum bound

**Statement**: For any primitive set $A \subset [x, \infty)$ and any $k \geq 1$,
$$\sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a}
  \leq T_k(x)
  \leq T_k(2)
  = 1 - (c + o(1)) \frac{k^2}{2^k}
  < 1.$$

**Proof**:

Let $A_k^{\geq x} := \{n \in \mathbb{N} : n \geq x,\ \Omega(n) = k\}$, the
full set of $k$-almost primes that are at least $x$. Define
$$T_k(x) := \sum_{n \in A_k^{\geq x}} \frac{1}{n \log n}.$$

Since $A \cap \{n : \Omega(n) = k\} \subseteq A_k^{\geq x}$ (because every
element of $A$ is at least $x$, by hypothesis), and since all terms
$1/(n \log n) > 0$, we have:
$$\sum_{\substack{a \in A \\ \Omega(a)=k}} \frac{1}{a \log a}
  \leq \sum_{n \in A_k^{\geq x}} \frac{1}{n \log n} = T_k(x).$$

Since $A_k^{\geq x} \subseteq A_k^{\geq 2} = \{n \geq 2 : \Omega(n) = k\}$,
the same argument gives $T_k(x) \leq T_k(2)$.

By **F3**, $T_k(2) = \sum_{n \geq 2, \Omega(n)=k} 1/(n \log n)
= 1 - (c+o(1))k^2/2^k$ with $c \approx 0.0656 > 0$. Since $c > 0$ and
$k^2/2^k > 0$, this is strictly less than 1. $\square$

**Notes**:
- This lemma does NOT use primitivity of $A$ — only that $A \subseteq [x, \infty)$
  and the elements have $\Omega$-value $k$.
- The upper bound $T_k(2)$ is the full $k$-stratum sum (Fact F3). The actual
  $T_k(x)$ is typically much smaller for small $k$ and large $x$.
- The lemma does NOT say the sum over ALL strata is $< 1$; it bounds each
  stratum separately. Summing over all $k$ gives a divergent series.
