---
id: total_bound
status: open
depends_on: [stratum_tail_bound, cross_stratum_blocking]
discharged_by_round: null
introduced_at_round: 2
---

# Lemma: Total bound assembly (L3)

## Statement

**Target**: For all primitive $A \subset [x, \infty)$,
$$f(A) = \sum_{a \in A} \frac{1}{a \log a} \leq 1 + o(1) \quad \text{as } x \to \infty.$$

This is the Erdős primitive-set conjecture itself.

## What we've established

- **Naïve stratification fails** (Lemma `stratum_tail_bound`): $\sum_k T_k(x)$ diverges,
  so we cannot bound $f(A) \leq \sum_k T_k(x) \leq 1 + o(1)$.

- **F1 gives a weaker bound**: Any primitive $A$ satisfies $f(A) \leq 1.399 + o(1)$
  (Zhang 1993, F1 from the ledger).  This is below 2 but above 1.

- **Numerically, the bound seems true for $x \geq 4$**: No primitive set $A \subset [x, \infty)$
  with $x \geq 4$ and $f(A) > 1$ was found by exhaustive search.

## Known partial results (from literature, NOT in ledger — citation only for context)

The state of the art is approximately $f(A) \leq 1 + O(1/\log \log x)$ (Lichtman,
~2022), improving F1.  The full conjecture ($\leq 1 + o(1)$) is open.

*Note*: This citation is NOT in the given-facts ledger.  We cannot use it as a formal
proof step; it is contextual background only.

## The core difficulty

The gap between F1 ($\approx 1.399$) and the conjectured bound ($1$) reflects
a genuine mathematical difficulty.  The key step is ruling out "dense" primitive
sets that include many elements near $x$ with similar sizes.

The "Cramér-style" heuristic: near $x$, integers have about $\log x$ prime factors
(by the Omega mean value theorem $\mathbb{E}[\Omega(n)] \sim \log \log n$).  A primitive
set $A \subset [x, 2x)$ can contain at most $\sim x/\log x$ elements (by Dilworth),
and each contributes $\sim 1/(x \log x)$.  The total is $\sim 1/\log x \to 0$, which
is far below 1 — consistent with the conjecture.

But the conjecture allows $A$ to span all of $[x, \infty)$, not just $[x, 2x)$.
Summing the contributions across doublings:

$$f(A) \leq \sum_{j=0}^\infty f(A \cap [2^j x, 2^{j+1} x)) \leq \sum_{j=0}^\infty C / \log(2^j x)
= C \sum_{j=0}^\infty \frac{1}{j \log 2 + \log x} \approx C \int_0^\infty \frac{dj}{j \log 2 + \log x}$$

which diverges!  So the dyadic-decomposition argument also fails.

The key missing insight: elements in $A \cap [2^j x, 2^{j+1} x)$ and
$A \cap [2^{j'} x, 2^{j'+1} x)$ for $j < j'$ may have divisibility relations
(the $2^j x$-range element might divide the $2^{j'} x$-range element), imposing
further restrictions that are not captured by the per-dyadic-block bound.

## Status

This lemma is **open**.  The proof of $f(A) \leq 1 + o(1)$ requires a technique
beyond simple stratification or dyadic decomposition.  The genuine difficulty
matches the literature's statement that the conjecture is open.

This session will document the above as a partial result (Q6).
