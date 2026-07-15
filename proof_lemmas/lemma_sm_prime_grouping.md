---
id: sm_quotient_primitive
status: proved
depends_on: []
discharged_by_round: 4
introduced_at_round: 4
---

# Lemma: A_sm quotient sets are primitive

**Statement**: For a primitive set $A \subset [x, \infty)$ and any prime
$p < x$, define $A(p) := \{a \in A : p_{\min}(a) = p\}$ and
$B(p) := \{a/p : a \in A(p)\}$. Then $B(p)$ is a primitive set with
all elements $\geq \lceil x/p \rceil$ and all prime factors $\geq p$.

**Proof**:

*Primitivity*: Suppose $b, b' \in B(p)$ are distinct with $b \mid b'$.
Then $a = pb$ and $a' = pb'$ are distinct elements of $A(p) \subseteq A$
with $pb \mid pb'$, i.e., $a \mid a'$. This contradicts primitivity of $A$.
Symmetrically $b' \nmid b$. So $B(p)$ is primitive. $\square$

*Lower bound*: Each $a \in A(p)$ satisfies $a \geq x$ (since $A \subset
[x,\infty)$), so $b = a/p \geq x/p$.

*Small-prime-free*: Suppose $q \mid b$ for a prime $q < p$. Then $q \mid pb = a$,
so $p_{\min}(a) \leq q < p$, contradicting $p_{\min}(a) = p$.
Hence $p_{\min}(b) \geq p$ for all $b \in B(p)$.

**Consequence (per-p F1 bound)**:

Since $B(p)$ is primitive, F1 gives $\sum_{b \in B(p)} 1/(b \ln b) < e^\gamma\pi/4$.
Since $\ln(pb) \geq \ln b$ for $p \geq 1$:
$$\sum_{a \in A(p)} \frac{1}{a \ln a} = \sum_{b \in B(p)} \frac{1}{pb\ln(pb)}
\leq \frac{1}{p} \sum_{b \in B(p)} \frac{1}{b \ln b} < \frac{e^\gamma\pi/4}{p}.$$

**Why this doesn't close the A_sm bound**: Summing over all primes $p < x$
gives $\sum_{a \in A_{\mathrm{sm}}} 1/(a\ln a) < e^\gamma\pi/4 \cdot \sum_{p<x} 1/p$,
but $\sum_{p<x} 1/p \to \infty$ as $x \to \infty$. The cross-$p$
primitivity constraints (for $a \in A(p)$, $a' \in A(q)$, $p \neq q$:
$a \nmid a'$ and $a' \nmid a$) are not used by this per-$p$ bound
and are essential for a non-divergent estimate.

**Gap**: A global argument using the full primitivity of
$A_{\mathrm{sm}} = \bigsqcup_p A(p)$ across all $p$-classes is needed.
