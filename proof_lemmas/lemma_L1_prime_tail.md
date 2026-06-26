---
id: L1_prime_tail
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 5
---

# Lemma L1 — Prime Tail Upper Bound

## Statement

For all sufficiently large $x$ (specifically, for $x \geq 3$):
$$\sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p} < 1.$$

## Motivation

L1 is used as a stepping stone toward L2: if the prime stratum (k=1)
contributes less than 1 when restricted to $[x,\infty)$, it supports
the intuition that all primitive sets in $[x,\infty)$ also contribute less
than 1 (L2's claim).

L1 is also numerically supported by Section 2.2 of proof\_strategy.md:
the truncated prime sum from $x=3$ to $200{,}000$ is $0.8334 < 1$.

## Proof Attempt

**Route 1 (via F1):**
The set $\{p \text{ prime} : p \geq x\}$ is a primitive set in $[x,\infty)$.
By F1, any primitive set has sum $< e^\gamma \pi/4 + o(1) \approx 1.399$.
This gives $\sum_{p \geq x} 1/(p \log p) < 1.399$, which is an upper bound
but NOT the desired bound of $1$.

*Obstacle*: F1's bound is $\approx 1.399$, not $< 1$. Route 1 does not
close L1.

**Route 2 (via convergence of the full prime series):**
The series $\sum_{p} 1/(p \log p)$ converges (this follows from
$\sum_p 1/p^s$ having abscissa of convergence $1$, combined with the
Mertens-type estimate $\sum_{p \leq N} 1/p \sim \log \log N$).
Let $S = \sum_{p} 1/(p \log p)$.  Then:
$$\sum_{p \geq x} \frac{1}{p \log p} = S - \sum_{p < x} \frac{1}{p \log p}
\xrightarrow{x \to \infty} 0.$$

In particular, for $x$ large enough, $\sum_{p \geq x} 1/(p \log p) < 1$.

*Obstacle (ledger)*: The statement "the series $\sum_p 1/(p \log p)$
converges" and the Mertens estimate $\sum_{p \leq N} 1/p \sim \log \log N$
are external facts NOT in the ledger $\{F1, F2, F3\}$.  If cited as
"known," the ledger critic will flag this as BLOCKING.  Any proof of L1
via Route 2 requires adding a convergence lemma (or a Mertens-type estimate)
to the facts ledger, or proving it from scratch within the framework.

## Current Obstacle

L1 requires either:
(a) A tighter version of F1 that decays as $x \to \infty$ (e.g.,
    $\sum_{p \geq x} 1/(p \log p) < f(x)$ for some $f(x) \to 0$), or
(b) An analytic number theory estimate (Mertens, PNT) establishing
    convergence of $\sum_p 1/(p \log p)$.

Neither (a) nor (b) is in the current ledger.  Closing L1 requires a
new fact to be added to the ledger, or an entirely different approach.

## Next Move

Request that the facts ledger be augmented with either:
- The Mertens estimate: $\sum_{p \leq N} 1/p = \log \log N + M + O(1/\log N)$
  where $M \approx 0.2615$ is the Meissel–Mertens constant.
- Or a direct statement: $\sum_{p} 1/(p \log p)$ converges to a
  constant $S < 2$, and $\sum_{p \geq x} 1/(p \log p) = O(1/\log x)$.

If such a fact is added, Route 2 closes L1 immediately.
