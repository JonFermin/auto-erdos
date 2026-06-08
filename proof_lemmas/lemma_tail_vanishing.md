---
id: tail_vanishing
status: open
depends_on: [F3_omega_k_exact_below_one]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma: Tail vanishing for each stratum (Q10)

**Statement:** For each fixed $k \geq 1$,
$$\sum_{\substack{a \in A_k \\ a \geq x}} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

## Attempted proof from F3

By F3, $\sum_{a \in A_k} \frac{1}{a \log a} = 1 - (c + o(1)) \frac{k^2}{2^k} < 1$.
This is a finite positive number. Therefore the series
$\sum_{a \in A_k} \frac{1}{a \log a}$ converges (its partial sums have a finite limit).
By the basic real-analysis fact that the tails of a convergent series tend to 0,
$$\sum_{a \in A_k,\, a \geq x} \frac{1}{a \log a} \to 0 \quad \text{as } x \to \infty.$$

The "tails of a convergent series → 0" step is a standard result (no named theorem
beyond basic analysis is invoked) that "no honest reader could dispute."

**Potential critic objection (ledger):** F3 asserts a finite value for the full sum,
which implies convergence; but F3 does not explicitly state "the series converges"
or "tails → 0." Whether the critic accepts this one-step real-analysis inference is
the key question.

## Why this matters

If the tail-vanishing lemma is accepted, then for any primitive
$A \subseteq [x, \infty)$ and any fixed $k$:
$$\sum_{a \in A \cap A_k} \frac{1}{a \log a} \leq \sum_{a \in A_k,\, a \geq x} \frac{1}{a \log a} \to 0.$$

Each individual stratum's contribution to the primitive set vanishes as $x \to \infty$.

## The remaining gap (Q11)

Even if every per-stratum contribution → 0, summing over ALL strata $k$ is not
directly possible. For the total to → 0, we would need:
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} \underbrace{\sum_{a \in A \cap A_k} \frac{1}{a \log a}}_{\to\, 0 \text{ for each fixed } k} \to 0.$$

This interchange of limit and sum requires uniform convergence (or dominated
convergence) across $k$, which is a non-trivial claim. Specifically:
- For large $k$, $\sum_{a \in A_k} 1/(a \log a) \approx 1$ (by F3).
- The "tail" $\sum_{a \in A_k \cap [x, \infty)} 1/(a \log a)$ for large $k$ may
  not be much smaller than 1, because for $k > \log_2 x$ all elements of $A_k$
  automatically satisfy $a \geq 2^k \geq x$, so the restriction adds no extra savings.

Quantitatively: for $k = \lceil \log_2 x \rceil$, $A_k$ consists of numbers with $k$
prime factors, all of which are $\geq 2^k \approx x$. The full $A_k$ sum (by F3) is
$1 - (c+o(1))k^2/2^k \approx 1 - c(\log x)^2/x$, which approaches 1. So even as
$x \to \infty$, the stratum $k = \lceil \log_2 x \rceil$ contributes nearly 1 to the
full stratum sum — the large-$k$ strata are NOT small.

**Current obstacle for Q11:** The tail-vanishing per stratum does not extend to
a uniform bound across all $k$, because large-$k$ strata have nearly-full contribution
even for large $x$. Closing this gap (getting $\sum_{k} [\text{stratum } k \text{ contribution}] \to 0$)
requires either a uniform rate on the per-stratum tails (not available from F3 alone)
or a direct use of primitivity to limit which $k$ can contribute simultaneously.

**Status:** open — tail-vanishing per stratum may be provable from F3; the multi-stratum
summation remains the obstacle.
