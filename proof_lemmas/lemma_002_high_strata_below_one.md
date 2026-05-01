---
id: high_strata_below_one
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 2 (high-stratum bound). There exist $K_0 \in \mathbb{N}$ and $\delta > 0$ such that for every $k \ge K_0$,
\[
S(A_k) \;\le\; 1 - \delta \cdot \frac{k^2}{2^k}.
\]

## Sketch

Direct restatement of the F3 asymptotic
$S(A_k) = 1 - (c + o(1)) k^2/2^k$ as $k \to \infty$, with $c \approx
0.0656 > 0$. Pick $K_0$ large enough that $|o(1)| \le c/2$, set
$\delta = c/2$, and the bound follows.

Crucially this gives $S(A_k) < 1$ for **every** $k \ge K_0$, with an
explicit decay rate.

## Current obstacle

F3 is cited as a black-box asymptotic. To make this lemma a stand-alone
proved object, we'd reproduce the F3 derivation (Sathe–Selberg) — this
is non-trivial and likely beyond the loop's scope. For the proof body
we treat F3 as a *given* (it's listed in `proofs/primitive_set_erdos.json`
ledger) and cite it.

For low $k$ the bound is non-trivial: e.g. $k = 1$ gives
$S(A_1) = \sum_p 1/(p \log p) \approx 1.6366 > 1$. So the bound
$S(A_k) \le 1 - \delta k^2/2^k$ is *false* at $k = 1$. We need
$K_0 \ge $ some explicit threshold; from the convergence pattern in
Section 2's table we'd guess $K_0 \approx 5$ or so, but no rigorous
threshold is established here.

Next move: locate an explicit $K_0$ in the literature (Cohen 1998?
Lichtman 2020?) or compute $S(A_k)$ directly via the Selberg formula
for a few $k$ to bracket $K_0$.
