---
id: convergence_barrier
status: open
depends_on: [single_stratum_bound, two_stratum, cross_stratum]
discharged_by_round: null
introduced_at_round: 10
---

# Lemma: barrier to closing the multi-stratum gap

This file documents why F1/F2/F3 alone appear insufficient to prove the
Erdős conjecture, and what additional facts would suffice.

## What we have

From the current proof attempt (using only F1/F2/F3):

1. **Single-stratum case** (proved via F3): for any primitive $A$ within
   one $\Omega$-stratum, $\sum_{a \in A} 1/(a \log a) < 1$.

2. **Global ceiling** (F1): for any primitive $A$,
   $\sum_{a \in A} 1/(a \log a) < 1.399 + o(1)$.

3. **F2 is unsigned**: F2 cannot establish any particular sum $> 1$.

## The multi-stratum gap

For a primitive set $A$ drawing from multiple strata, the sum
$\sum_k S_k(A)$ involves contributions from strata $k = 1, 2, 3, \ldots$
The naive stratum-by-stratum bound from F3 gives $\sum_k(1 - \delta_k)$
where $\delta_k = (c+o(1))k^2/2^k > 0$. This series diverges (the $\sum_k 1$
part alone diverges). The inter-stratum constraint must supply the missing mass.

## What would suffice (four sufficient conditions)

**Sufficiency 1 — Restricted stratum bound**: If there exists a function
$R(k, A_1)$ such that for a primitive $A$ with prime part $A_1$:
$$\sum_{n:\,\Omega(n)=k,\; \forall a \in A_1: a \nmid n} \frac{1}{n \log n}
\leq R(k, A_1)$$
and if $\sum_k R(k, A_1) + S_1(A) \leq 1$, the conjecture would follow.
This requires a "restricted F3" formula for the $k$-stratum sum with
divisibility exclusions — a variant of F3 not in the current ledger.

**Sufficiency 2 — Finite effective strata**: If for any primitive
$A \subset [x, \infty)$, the contribution from strata $k > K(x)$ is $o(1)$
as $x \to \infty$ for some explicit $K(x)$, and if the sum over strata
$k \leq K(x)$ is $\leq 1 + o(1)$, the conjecture would follow. This requires
counting estimates for $\Omega$-strata in $[x, \infty)$, not in the ledger.

**Sufficiency 3 — Conservation law**: If there is a function $g$ on the
integers such that $\sum_{a \in A} g(a) = 1$ for any maximal primitive set
$A$, and if $1/(a \log a) \leq g(a)$ for all $a$, the conjecture would
follow. No such $g$ is derivable from F1/F2/F3.

**Sufficiency 4 — Two-stratum induction**: If the two-stratum conjecture
($S_j(A) + S_k(A) \leq 1$ for any two-stratum primitive $A$) were proved
for all $j < k$, an inductive argument on the number of strata might extend
to the general case. However, the two-stratum case appears as hard as the
full conjecture within F1/F2/F3.

## Conclusion

None of conditions 1–4 can be established from F1/F2/F3 alone:
- Sufficiency 1 needs a restricted variant of F3 (not in ledger).
- Sufficiency 2 requires counting estimates for $\Omega$-strata (not in ledger).
- Sufficiency 3 requires a conservation law not derivable from F1/F2/F3.
- Sufficiency 4 reduces to the two-stratum sub-problem (equally open, Q7).

The barrier is therefore: the given-facts ledger (F1/F2/F3) is insufficient
to close the conjecture without additional analytic number theory inputs.
The partial result (single-stratum case) is the best achievable here.
