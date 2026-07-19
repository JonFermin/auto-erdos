---
id: stratum_bound
status: proved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

> Concluded `primitive_set_erdos` attempt (claim proved in the literature,
> May 2026, arXiv:2605.00301); retained as audit trail, not load-bearing for
> any active chain. Per the falsify-critic contract, one-line sandbox
> re-derivations are not expected for this file; deterministic re-checks, if
> any, live in its CHECK blocks.

# Lemma 1: Stratum bound

**Statement.** Let $A \subseteq [x, \infty)$ be a primitive set and let
$B_k = A \cap \{n \geq x : \Omega(n) = k\}$ for $k \geq 1$. Then
$$\sum_{b \in B_k} \frac{1}{b \log b} \;\leq\; S_k(x) := \sum_{\substack{n \geq x \\ \Omega(n) = k}} \frac{1}{n \log n}.$$

**Proof.** $B_k \subseteq \{n \geq x : \Omega(n) = k\}$, so summing $1/(b \log b)$
over the smaller set is bounded by the sum over the full set. $\square$

**Remark.** The cross-stratum constraint (no $a \in B_j$ divides $b \in B_k$ for
$j \neq k$) is automatic: if $a \mid b$ and $a \neq b$, then $b = a \cdot m$ for
some $m \geq 2$, hence $\Omega(b) \geq \Omega(a) + 1$. So elements in different
strata cannot divide each other — the only active constraint is within each
stratum $B_k$ (no two elements of $B_k$ divide each other).

**Within-stratum constraint.** The bound $S_k(x)$ does NOT use the within-stratum
primitivity of $B_k$. It is a loose bound. Lemma 3 (prime extremality) uses a
sharper argument to bound the TOTAL across strata.
