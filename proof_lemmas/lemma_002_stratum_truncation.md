---
id: lemma_002_stratum_truncation
status: proved
depends_on: [lemma_001_omega_k_is_primitive]
discharged_by_round: 5
introduced_at_round: 5
---

# Lemma 2 — Stratum truncation respects the F3 bound

**Statement.** Let $A_k = \{ n \in \mathbb{Z}_{\geq 2} : \Omega(n) = k \}$
and let $S_k = \sum_{a \in A_k} 1/(a \log a)$. By F3,
$S_k = 1 - (c + o(1)) k^2 / 2^k$ as $k \to \infty$, with $c$ as
in F3 (positive). Then for every $x \geq 2$, the truncated stratum
$A_k \cap [x, \infty)$ is again a primitive set, and
$$
\sum_{a \in A_k \cap [x, \infty)} \frac{1}{a \log a}
\;\leq\; S_k.
$$
In particular there exists $k_0 \geq 1$ such that for every
$k \geq k_0$ and every $x \geq 2$,
$$
\sum_{a \in A_k \cap [x, \infty)} \frac{1}{a \log a}
\;\leq\; S_k \;\leq\; 1 - \tfrac{c}{2}\,\frac{k^2}{2^k} \;<\; 1.
$$
The quantitative form $S_k \leq 1 - (c/2)\, k^2 / 2^k$ for
$k \geq k_0$ is what is actually used in §3.3 of
`proof_strategy.md`; the weaker form $S_k < 1$ stated in earlier
drafts is an immediate consequence ($c, k^2, 2^{-k} > 0$).

**Proof.**
*Primitivity.* By Lemma `lemma_001_omega_k_is_primitive`, $A_k$ is a
primitive set. Any subset of a primitive set is again primitive, so
$A_k \cap [x, \infty)$ is primitive.

*The truncation inequality.* Each summand $1/(a \log a)$ with
$a \in A_k$ satisfies $a \geq 2$, so $\log a > 0$ and the summand is
positive. The truncation $A_k \cap [x, \infty) \subseteq A_k$ removes
finitely many positive terms (those with $a < x$) from the convergent
series defining $S_k$. Hence
$$
\sum_{a \in A_k \cap [x, \infty)} \frac{1}{a \log a}
\;=\; S_k - \sum_{a \in A_k \cap [2, x)} \frac{1}{a \log a}
\;\leq\; S_k.
$$
(Convergence of the series $\sum_{a \in A_k} 1/(a \log a)$ — needed
to make the partial sum $\sum_{a \in A_k \cap [2,x)}$ well-defined as
a part of $S_k$ — is established below.)

*Existence of $k_0$ and the quantitative bound.* By F3 there is a
function $\varepsilon \colon \mathbb{N} \to \mathbb{R}_{\geq 0}$
with $\varepsilon(k) \to 0$ as $k \to \infty$ such that
$$
\bigl| S_k \;-\; \bigl(1 - c\, k^2 / 2^k\bigr) \bigr|
\;\leq\; \varepsilon(k) \cdot k^2 / 2^k.
$$
Define $k_0$ as the smallest positive integer such that
$\varepsilon(k_0) \leq c/2$ (such $k_0$ exists since
$\varepsilon \to 0$ and $c > 0$ is a fixed positive constant from
the F3 ledger; the value of $k_0$ depends on the effective form
of $\varepsilon$, which the F1/F2/F3 ledger does not pin down
beyond its asymptotic decay, so we do not assign a numerical
value to $k_0$ inside the strict ledger-only writeup). Then for
all $k \geq k_0$,
$$
S_k
\;\leq\; \bigl(1 - c\, k^2 / 2^k\bigr) + \varepsilon(k)\, k^2/2^k
\;\leq\; 1 - c\, k^2 / 2^k + \tfrac{c}{2}\, k^2 / 2^k
\;=\; 1 - \tfrac{c}{2}\, k^2 / 2^k
\;<\; 1.
$$
Combining with the truncation inequality above gives the
displayed quantitative bound. $\square$

**Remark on $S_k$ convergence.** F3's exact-asymptotic statement
implicitly assumes $S_k$ exists (is finite); convergence of
$\sum_{a \in A_k} 1/(a \log a)$ for each fixed $k$ follows from
density estimates of integers with exactly $k$ prime factors
(Landau, 1900): the count of $n \leq t$ with $\Omega(n) = k$ is
$\sim t (\log\log t)^{k-1} / ((k-1)! \log t)$, so by partial summation
$\sum_{a \in A_k, a \leq t} 1/(a \log a)$ converges as $t \to \infty$.
This convergence is what permits the truncation-equals-difference
identity used above.
