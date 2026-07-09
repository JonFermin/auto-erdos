---
id: cross_stratum_interaction
status: open
depends_on: [stratification_setup, single_stratum_f3_bound]
discharged_by_round: null
introduced_at_round: 1
---

# Lemma `cross_stratum_interaction`

**Statement (conjectured)**: For any primitive $A \subseteq [x, \infty)$:
$$f(A) = \sum_{k \geq 1} f(A_k) < 1 + o(1) \quad \text{as } x \to \infty.$$

**Status**: open. This is the main conjecture reformulated. Proving this
lemma proves the conjecture.

## What is known

- F1: $f(A) < 1.399 + o(1)$ (black-box upper bound, does not close to 1).
- Lemma `single_stratum_f3_bound`: $f(A_k) < 1$ for each $k$ individually.
- Lemma `stratification_setup`: for $j < k$, no element of $A_j$ divides
  any element of $A_k$.

## The proof gap

To close the gap from 1.399 to 1, we need a quantitative estimate: given that
elements of lower strata block (as divisors) elements of higher strata, how
much does this exclusion reduce the total sum?

Formally: if $f(A_{j_0}) \approx 1 - \epsilon$ for some stratum $j_0$, the
exclusion principle forces $A_k$ to avoid all multiples of elements in $A_{j_0}$
for $k > j_0$. If this exclusion reduces $\sum_{k \neq j_0} f(A_k)$ by at
least $1 - o(1) - \epsilon$, the conjecture would follow. This reduction
estimate is not in the given-facts ledger (F1, F2, F3).

## Current obstacle

No elementary combination of F1, F2, F3 yields $f(A) < 1 + o(1)$:
- F1 gives 1.399, not 1; the technique behind F1 is not in the ledger.
- F2's $O$-term is unsigned; supplying positivity would require additional input.
- F3 bounds strata individually; their sum is not bounded by F3 alone.

This lemma requires either a new fact in the ledger or a fundamentally different
argument exploiting the large-$x$ regime of $A \subseteq [x, \infty)$.

**Suggested future work**:
- Add a fact quantifying the cross-stratum density reduction (outside current
  ledger; requires curator approval to add to `proofs/primitive_set_erdos.json`).
- Attempt a direct sieve bound for $A \subseteq [x, \infty)$ showing
  $f(A) < (1 + C/\log x)$ for some explicit constant $C$.
