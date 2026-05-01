---
id: lemma_003_prime_tail_to_zero
status: proved
depends_on: []
discharged_by_round: 5
introduced_at_round: 5
---

# Lemma 3 — The prime tail $\sum_{p \geq x} 1/(p \log p) \to 0$

**Statement.** As $x \to \infty$,
$$
T(x) \;:=\; \sum_{p \text{ prime},\ p \geq x} \frac{1}{p \log p}
\;\longrightarrow\; 0.
$$

**Proof.** The series $\sum_{p} 1/(p \log p)$ converges. To see this,
recall the prime-counting estimate $\pi(t) \sim t / \log t$ as
$t \to \infty$ (a textbook consequence of the Prime Number Theorem,
which we admit as foundational and extra-ledger). By partial summation,
$$
\sum_{p \leq T} \frac{1}{p \log p}
\;=\; \frac{\pi(T)}{T \log T}
+ \int_{2}^{T} \pi(t)\, \frac{d}{dt}\!\left(\frac{-1}{t \log t}\right) dt.
$$
The boundary term tends to $1/(\log T)^2 \to 0$ as $T \to \infty$. The
integrand is $\pi(t) \cdot (\log t + 1) / (t \log t)^2 \sim 1 / (t
\log^2 t)$, and $\int_2^\infty dt / (t \log^2 t) = 1/\log 2 < \infty$
(direct: substitute $u = \log t$, $du = dt/t$, integrand $du / u^2$,
antiderivative $-1/u$). Hence $\sum_p 1/(p \log p)$ converges to a
finite limit $L$, with $L > 0$ (positive terms).

Since the full sum is finite,
$$
T(x) \;=\; L - \sum_{p < x} \frac{1}{p \log p} \;\longrightarrow\; 0
\qquad (x \to \infty).
$$
$\square$

**Remark.** This invokes the PNT estimate $\pi(t) \sim t/\log t$ as
extra-ledger. If a future critic flags this, the same conclusion can
be obtained from Chebyshev's weaker $\pi(t) \ll t/\log t$ (also
extra-ledger but more elementary), which suffices for the integral
bound and hence for convergence of $\sum_p 1/(p \log p)$.
