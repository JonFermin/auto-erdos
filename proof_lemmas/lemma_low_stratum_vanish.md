# Lemma: `low_stratum_vanish`

**Status**: proved

**Statement**: Fix any integer $K \geq 1$. For any primitive set
$A \subset [x, \infty)$ whose elements all satisfy $\Omega(a) \leq K$,
$$\sum_{a \in A} \frac{1}{a\log a} \leq \sum_{k=1}^{K} T_k(x) \to 0
\quad\text{as } x \to \infty.$$

---

## Proof

Since $A \subset [x, \infty)$ and each $a \in A$ has $\Omega(a) = k$ for
some $k \in \{1, \ldots, K\}$, partition $A = \bigsqcup_{k=1}^K A^{(k)}$
where $A^{(k)} = \{a \in A : \Omega(a) = k\}$. Then:
$$\sum_{a \in A} \frac{1}{a\log a}
  = \sum_{k=1}^{K} \sum_{a \in A^{(k)}} \frac{1}{a\log a}
  \leq \sum_{k=1}^{K} T_k(x),$$
where the inequality uses Lemma `stratum_sub_bound` for each stratum.

By Lemma `large_floor_vanish`, $T_k(x) \to 0$ as $x \to \infty$ for each
fixed $k$. Since $K$ is a fixed constant, the finite sum
$\sum_{k=1}^K T_k(x) \to 0$ as $x \to \infty$. $\square$

**Note on scope**: This argument is VALID ONLY for FIXED $K$ (not depending on
$x$). If $K = K(x) \to \infty$ with $x$, the finite sum of $K(x)$ terms each
individually $o(1)$ need not tend to $0$.

**Consequence**: The Erdős primitive-set conjecture holds (with $o(1)$ bound)
whenever $A$ is supported on strata of bounded Omega-number. The hard case
requires elements with $\Omega(a)$ growing with $x$.
