---
id: lemma_004_bounded_omega_tail
status: conditional
depends_on: [lemma_001_omega_k_is_primitive, lemma_002_stratum_truncation, lemma_003_prime_tail_to_zero]
discharged_by_round: null
introduced_at_round: 5
---

> **Conditional.** The proof sketch below admits Landau's
> density estimate $|A_k \cap [2, t]| \sim t (\log\log t)^{k-1} /
> ((k-1)! \log t)$ — sharpened by Sathe–Selberg — as an
> extra-ledger fact. As with Lemma 3, this lemma is not unconditional
> under the F1/F2/F3 ledger; the main writeup invokes it only inside
> a clearly-flagged conditional subsection.

# Lemma 4 — Tail of bounded-$\Omega$ stratum sums

**Statement (target).** For every fixed $K \geq 1$,
$$
\sum_{k=1}^{K} \sum_{a \in A_k \cap [x, \infty)} \frac{1}{a \log a}
\;\longrightarrow\; 0 \qquad (x \to \infty).
$$

**Status.** *Open.* The case $k = 1$ is Lemma
`lemma_003_prime_tail_to_zero`. The cases $k \in \{2, \ldots, K\}$
require an analogous tail-to-zero estimate for sums of the form
$\sum_{a \in A_k,\ a \geq x} 1/(a \log a)$.

**Current state of attack.**

- For each $k \geq 1$ the convergence of $\sum_{a \in A_k} 1/(a \log a)$
  (used in Lemma `lemma_002_stratum_truncation`) follows from Landau's
  density $|A_k \cap [2, t]| \sim t (\log \log t)^{k-1} / ((k-1)! \log t)$.
  By partial summation, the tail $\sum_{a \in A_k,\ a \geq x}
  1/(a \log a)$ tends to $0$ as $x \to \infty$ for each fixed $k$.
- The constant in the convergence rate (the analogue of $L$ in Lemma 3)
  is $S_k$ from F3, which is bounded above by $1$ for $k$ large.
- Summing over $k \in \{1, \ldots, K\}$ is summing finitely many
  individually tail-to-zero quantities; each tends to $0$ at its own
  rate, but the union-rate is the slowest of $K$ rates and still
  $\to 0$.

**Obstacle.** Landau's asymptotic for $|A_k \cap [2, t]|$ is
extra-ledger and is the first place this proof would need to admit a
substantial classical fact beyond the F1/F2/F3 ledger. A defensive
strategy is to cite Landau (or Sathe–Selberg, which sharpens it) as a
foundational extra-ledger admission, in the same spirit as Lemma 3
admits the PNT density. Weaker fall-back bounds based on the
elementary observation that $A_k$ is sparse in a $k$-dependent way
are too loose to support partial summation.

**Next move.**
1. Promote a Landau-style admission to a named "extra-ledger fact"
   block at the top of `proof_strategy.md`, so the ledger critic has
   an explicit place to find the citation rather than treating each
   use as an unsupported drift.
2. Once admitted, the lemma falls out by partial summation per stratum.
3. Restrict $K$ to a function of $x$ (e.g. $K = K(x) \to \infty$
   slowly enough that the $k$-uniform tail rate is summable) — this is
   the bridge to Lemma 5 (open).
