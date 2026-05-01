---
id: truncated_low_strata
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 1 (truncated low-strata). For fixed $k \ge 1$,
\[
S(A_k \cap [x, \infty)) \;=\; \sum_{\substack{a \ge x \\ \Omega(a) = k}}
\frac{1}{a \log a}
\;=\; O\!\left( \frac{(\log\log x)^{k-1}}{\log x} \right) \;\to\; 0
\]
as $x \to \infty$.

## Sketch

By Landau's theorem,
$\pi_k(y) := |A_k \cap [1, y]| \sim \frac{y (\log\log y)^{k-1}}{(k-1)! \log y}$
as $y \to \infty$. Thus
\[
S(A_k \cap [x, y]) \;=\; \int_x^y \frac{1}{u \log u} \, d\pi_k(u),
\]
and partial summation against $1/(u \log u)$ gives
\[
S(A_k \cap [x, \infty))
\;=\; \frac{(\log\log x)^{k-1}}{(k-1)! \log x} \cdot \frac{1}{\log x}
\;+\; \text{lower-order}
\;=\; O\!\left( \frac{(\log\log x)^{k-1}}{(\log x)^2} \right).
\]

(Sharper than the bound stated above. The looser $(\log\log x)^{k-1}/\log x$
suffices for our application.)

## Current obstacle

The argument as written cites Landau's theorem with a uniform constant in $k$.
A clean writeup needs the constant to be uniform on a range $k \le K(x)$
where $K(x) \to \infty$ slowly with $x$ — otherwise summing over $k$ in
Lemma 2 picks up an $x$-dependent error in the implicit constant. The
Hardy–Ramanujan formula $|A_k \cap [1, y]| = \frac{y}{\log y} \cdot
\frac{(\log\log y + B)^{k-1}}{(k-1)!} (1 + O_k(1/\log\log y))$ does this
uniformly for $k \le (\log\log y)^2$ (Pomerance–Sárközy 1988); citing
that gives a uniform-in-$k$ Lemma 1 on an explicit range of $k$.

Next move: tighten the proof to use the Hardy–Ramanujan / Sathe form
and state the explicit uniform-in-$k$ range.
