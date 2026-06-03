---
id: functional_ineq_bound
status: open
depends_on: [spf_reduction]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 3 — Functional inequality bound (open)

**Statement** (to be proved): Let $M(x) = \sup_{A \subset [x, \infty), A \text{ primitive}} \sum_{a \in A} 1/(a \log a)$. Then $M(x) \leq 1 + o(1)$ as $x \to \infty$.

**Equivalent formulation**: Show that the functional inequality from Lemma 2,
$$M(x) \leq \sum_{p} \frac{1}{p} \cdot M(x/p), \tag{$\star$}$$
forces $M(x) \to 1$ as $x \to \infty$.

## Boundary conditions

- $M(x) = 0$ for $x > x_\infty$ (empty primitive set). In practice $M(x) \to 0$ is not claimed;
  we expect $M(x) \to 1$ from above.
- Primes in $[x, \infty)$ give $f_\mathrm{primes}(x) = \sum_{p \geq x} 1/(p \log p) \approx 1/\log x \to 0$.
  So the primes are NOT the extremal primitive set for large $x$.
- The extremal sets appear to be $A_k$ (all integers with $\Omega = k$) for large $k$.
  Each $A_k$ is a subset of $[2^k, \infty)$ and has sum $1 - c k^2/2^k \to 1$ from below.

## Attempted approach: trial solution $M(x) = C/\log x$

Plug into ($\star$):
$$\frac{C}{\log x} \leq \sum_p \frac{1}{p} \cdot \frac{C}{\log(x/p)} = C \sum_p \frac{1}{p(\log x - \log p)}.$$

For this to be consistent, we need $\sum_p 1/(p(\log x - \log p)) \leq 1/\log x$, i.e.,
$\sum_p (\log x) / (p(\log x - \log p)) \leq 1$. The LHS diverges as $p \to x$ (the term
$\log x / (p(\log x - \log p))$ blows up for $p$ near $x$). So $M(x) = C/\log x$ does not
satisfy ($\star$) with a consistent constant — the ansatz fails.

## Attempted approach: $M(x) = 1 + h(x)$ with $h(x) \to 0$

The conjecture claims $M(x) \leq 1 + h(x)$ with $h(x) \to 0$. Plugging into ($\star$):
$$1 + h(x) \leq \sum_p \frac{1}{p}(1 + h(x/p)) = \sum_p \frac{1}{p} + \sum_p \frac{h(x/p)}{p}.$$

The term $\sum_p 1/p$ diverges, so this approach fails unless we restrict the sum to $p \leq x$
(since for $p > x$, $A_p$ is empty in $[x, \infty)$). Restrict to $p \leq x$:
$$M(x) \leq \sum_{p \leq x} \frac{M(x/p)}{p}.$$

Still, $\sum_{p \leq x} 1/p = \log\log x + M_{\text{Meissel}} + O(1/\log x)$ diverges, so the approach
$M(x) = 1 + h(x)$ with $h(x) \to 0$ plugged directly doesn't close.

## What is needed

A sharper analysis must exploit that the $B_p$ sets in Lemma 2 are NOT independent — they
are "fibers" of the same primitive set $A$, so their elements are constrained to be
pairwise non-divisible across fibers as well. The inequality ($\star$) treats them as
independent, losing information. A tighter version of Lemma 2 that captures the
cross-fiber constraint is needed. This appears to be the main gap in the Erdős proof program.

## Current status

Open. The functional inequality ($\star$) is correctly derived but not sufficient on its own.
The next step would be to find a refined version of ($\star$) that accounts for cross-fiber
primitivity, or to use a completely different approach (e.g., a direct sieve bound).

**This is the genuine mathematical obstacle**: the Erdős conjecture has been open since 1988
(Erdős posed it; Lichtman and Pomerance proved F1 ≈ 1.399 in 2021; the bound 1 remains open).
The agent cannot prove Lemma 3 without a genuinely new idea.
