---
id: s1_bound
status: proved
depends_on: []
discharged_by_round: 8
introduced_at_round: 8
---

# Lemma: S1 ≤ 1 + o(1)

**Statement**: For any primitive set $A \subset [x, \infty)$ with
$A_1 := A \cap [x, x^e)$, the partial sum
$$S_1 := \sum_{a \in A_1} \frac{1}{a \log a} \leq 1 + o(1) \quad (x \to \infty).$$

**Proof**:

**Step 1**: Since each $a \in A_1 \subset [x, x^e)$,
$$S_1 \leq \sum_{n=\lfloor x \rfloor}^{\lceil x^e \rceil - 1} \frac{1}{n\log n}.$$

**Step 2 (integral comparison)**: The function $f(t) = 1/(t\log t)$ is positive and
strictly decreasing for $t > e^0 = 1$ (its derivative is
$f'(t) = -(1 + \log t)/(t\log t)^2 < 0$ for $t > 1$). For any integer $n \geq 2$,
since $f$ is decreasing,
$$\frac{1}{n\log n} = f(n) \leq \int_{n-1}^{n} f(t)\,dt = \int_{n-1}^{n} \frac{dt}{t\log t}.$$
Summing from $n = \lceil x \rceil$ to $n = \lceil x^e \rceil - 1$:
$$\sum_{n=\lceil x \rceil}^{\lceil x^e \rceil - 1} \frac{1}{n\log n}
  \leq \int_{\lceil x \rceil - 1}^{\lceil x^e \rceil} \frac{dt}{t\log t}
  \leq \int_{x-1}^{x^e + 1} \frac{dt}{t\log t}.$$

**Step 3 (antiderivative)**: For $t > 1$, $\frac{d}{dt}\log\log t = \frac{1}{t\log t}$
(chain rule: $\frac{d}{dt}\log u = 1/u$ with $u = \log t$ and $\frac{d}{dt}\log t = 1/t$).
Therefore:
$$\int_{x-1}^{x^e+1} \frac{dt}{t\log t} = \bigl[\log\log t\bigr]_{x-1}^{x^e+1}
= \log\log(x^e+1) - \log\log(x-1).$$

**Step 4 (asymptotic)**: $\log\log(x^e+1) = \log(1 + \log x) = \log(e\log x) + o(1) = 1 + \log\log x + o(1)$ as $x \to \infty$. Likewise $\log\log(x-1) = \log\log x + o(1)$ as $x \to \infty$.
Therefore:
$$S_1 \leq \int_{x-1}^{x^e+1} \frac{dt}{t\log t} = (1 + \log\log x + o(1)) - (\log\log x + o(1)) = 1 + o(1). \quad \square$$

**Tightness**: Taking $A_1 = \{n \in \mathbb{Z} : x \leq n < x^e\}$ (which is automatically
primitive since no element of $[x, x^e)$ divides another element of $[x, x^e)$) gives
$S_1 = \sum_{x \leq n < x^e} 1/(n\log n) \to 1$ as $x \to \infty$ (same integral estimate).
