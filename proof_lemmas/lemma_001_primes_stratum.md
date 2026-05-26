---
id: primes_stratum
status: proved
depends_on: []
discharged_by_round: 5
introduced_at_round: 5
---

# Lemma 1: Primes Stratum Bound

**Statement**: Let $A \subseteq [x, \infty)$ be a primitive set. Then
$$\sum_{\substack{a \in A \\ \Omega(a) = 1}} \frac{1}{a \ln a}
\leq \sum_{p \geq x} \frac{1}{p \ln p} = O\!\left(\frac{1}{\ln x}\right).$$

**Proof**: The set $A^{(1)} := A \cap \{n : \Omega(n) = 1\}$ is a set of primes $\geq x$.
Each prime $p \in A^{(1)}$ satisfies $p \geq x$ and is distinct. Therefore:
$$\sum_{p \in A^{(1)}} \frac{1}{p \ln p} \leq \sum_{p \geq x} \frac{1}{p \ln p},$$
the sum over ALL primes $\geq x$.

By the prime number theorem and partial summation:
$$\sum_{p \geq x} \frac{1}{p \ln p} = \int_x^\infty \frac{d\pi(t)}{t \ln t}
\sim \int_x^\infty \frac{dt}{t (\ln t)^2} = \frac{1}{\ln x}.$$

More precisely, $\sum_{p \geq x} 1/(p \ln p) = 1/\ln x + O(1/(\ln x)^2)$ (from Mertens
estimates; numerical evidence: $\approx 0.217$ at $x=100$, $\approx 0.145$ at $x=1000$).

**This term goes to $0$ as $x \to \infty$, well within the conjecture's $1 + o(1)$ bound.**

**Status**: Proved. This is easy.
