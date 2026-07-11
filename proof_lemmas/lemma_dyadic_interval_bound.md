---
id: dyadic_interval_bound
status: proved
depends_on: []
discharged_by_round: 2
introduced_at_round: 2
---

# Lemma: per-dyadic-interval sum bound

**Statement**: For any primitive set $A \subset [x, \infty)$ and any interval
$I = [N, 2N)$ with $N \geq 2$,
$$\sum_{a \in A \cap I} \frac{1}{a \log a}
  \leq \frac{\log 2}{\log N} + O\!\left(\frac{1}{\log^2 N}\right).$$

**Proof**:

**Step 1 (any subset of $[N, 2N)$ is primitive)**: If $a, b \in [N, 2N)$ with
$a < b$ and $a | b$, then $b \geq 2a \geq 2N$, contradicting $b < 2N$. Hence
no element of $[N, 2N)$ divides any other distinct element of $[N, 2N)$.

Therefore $A \cap I$ is a subset of $[N, 2N)$ with no additional primitivity
constraint: EVERY subset of $[N, 2N)$ is automatically primitive.

**Step 2 (bound by the full-interval sum)**: Since every term $1/(a \log a) > 0$,
the sum over any subset is maximized when the subset is all of $[N, 2N) \cap \mathbb{Z}$:
$$\sum_{a \in A \cap I} \frac{1}{a \log a}
  \leq \sum_{n=N}^{\lfloor 2N \rfloor - 1} \frac{1}{n \log n}.$$

**Step 3 (estimate the full-interval sum)**: By the Euler–Maclaurin formula,
$$\sum_{n=N}^{2N-1} \frac{1}{n \log n} = \int_N^{2N} \frac{dt}{t \log t} + O\!\left(\frac{1}{N \log N}\right).$$

Evaluating the integral (with $u = \log t$, $du = dt/t$):
$$\int_N^{2N} \frac{dt}{t \log t} = \int_{\log N}^{\log(2N)} \frac{du}{u}
  = \ln\!\left(\frac{\log(2N)}{\log N}\right)
  = \ln\!\left(1 + \frac{\log 2}{\log N}\right)
  = \frac{\log 2}{\log N} - \frac{(\log 2)^2}{2(\log N)^2} + O\!\left(\frac{1}{\log^3 N}\right).$$

Therefore:
$$\sum_{a \in A \cap [N, 2N)} \frac{1}{a \log a}
  \leq \frac{\log 2}{\log N} + O\!\left(\frac{1}{\log^2 N}\right). \quad \square$$

---

## Why this does not close the conjecture

The bound above does NOT use the cross-interval primitivity constraint. Summing
over all dyadic intervals $[x \cdot 2^j, x \cdot 2^{j+1})$ for $j = 0, 1, 2, \ldots$:

$$\sum_{j=0}^\infty \left(\frac{\log 2}{\log(x \cdot 2^j)} + O\!\left(\frac{1}{\log^2(x \cdot 2^j)}\right)\right)
  = \sum_{j=0}^\infty \frac{\log 2}{\log x + j \log 2} + O\!\left(\frac{1}{\log^2 x}\right)
  = \sum_{j=0}^\infty \frac{1}{\log_2 x + j} + O\!\left(\frac{1}{\log^2 x}\right).$$

The series $\sum_{j=0}^\infty 1/(\log_2 x + j)$ diverges (harmonic tail). So
the dyadic-interval bound gives a divergent total without using cross-interval
primitivity.

In particular, this lemma shows the per-dyadic bound is tight: taking $A$ to be
the full set $\{N, N+1, \ldots, 2N-1\}$ (which is primitive) achieves the bound.
Any improvement must exploit GLOBAL primitivity — the fact that elements across
different intervals $I_j$ interact (a small element in $I_0$ blocks multiples in
$I_1, I_2, \ldots$).
