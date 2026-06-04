---
id: stratum_tail_bound
status: proved
depends_on: []
discharged_by_round: 3
introduced_at_round: 3
---

# Lemma 1 — Single-stratum tail bound

**Statement.** For any fixed $k \geq 1$ and any primitive set $A \subseteq [x, \infty)$:
$$\sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a} \leq T_k(x) := \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n}.$$
Moreover, $T_k(x) \to 0$ as $x \to \infty$ for each fixed $k$.

**Proof.** The first inequality is immediate: the terms $1/(a \log a)$ are positive, and $A \cap \{n : \Omega(n)=k\} \subseteq \{n \geq x : \Omega(n)=k\}$, so the sum over the smaller set is at most the sum over the larger set.

For the second claim, let $A_k(x) = \{n \geq x : \Omega(n) = k\}$. By the Sathe–Selberg theorem, the number of elements of $A_k(x)$ up to $y$ is
$$\#\{x \leq n \leq y : \Omega(n) = k\} \sim \frac{y}{\log y} \cdot \frac{(\log \log y)^{k-1}}{(k-1)!}.$$
By partial summation (Abel's theorem), letting $f(n) = 1/(n \log n)$:
$$T_k(x) = \sum_{n \geq x, \Omega(n)=k} \frac{1}{n \log n} \leq \int_x^\infty \frac{d(\pi_k(t))}{t \log t}$$
where $\pi_k(t) = \#\{n \leq t : \Omega(n)=k\}$. By integration by parts and the Sathe–Selberg asymptotics, this integral is $O\!\left(\frac{(\log \log x)^{k-1}}{(k-1)! \cdot \log x}\right) \to 0$ as $x \to \infty$. $\square$

**Numerical verification** (from §2.1 of the main proof): The table confirms $T_k(x) < 1$ for all $k = 1, 2, 3, 4$ and all $x_{\text{floor}} \geq 3$.

**Role in the proof.** This lemma handles each stratum individually. The hard step (not covered here) is bounding the TOTAL over all strata simultaneously — see the proof outline (Section 4) and Lemma 3.
