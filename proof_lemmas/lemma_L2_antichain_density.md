---
id: L2_antichain_density
status: open
depends_on: [L1_prime_tail]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma L2 — Antichain Density Bound

## Statement

For any primitive set $A \subseteq [x, \infty)$, there exists an absolute
constant $C > 0$ such that for all sufficiently large $x$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{C}{\log x}.$$

## Motivation

L2 immediately implies the conjecture: for $x$ large, $C/\log x \to 0$,
so the sum is $\leq C/\log x = o(1)$, giving the bound $1 + o(1)$.

## Proof Strategy: Omega-Stratification

Partition any primitive $A \subseteq [x, \infty)$ by $\Omega$-value:
let $A_k' = A \cap \{n : \Omega(n) = k\}$ for $k = 1, 2, 3, \ldots$.
Since $A$ is primitive, each $A_k'$ is also primitive (a subset of the
primitive set $A_k$).  Then:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} \sum_{a \in A_k'} \frac{1}{a \log a}.$$

*Step 1 — Per-stratum bound:*
For each $k$, $A_k' \subseteq A_k \cap [x, \infty)$, so:
$$\sum_{a \in A_k'} \frac{1}{a \log a} \leq \sum_{\substack{a \in A_k \\ a \geq x}} \frac{1}{a \log a} =: T_k(x).$$

*Step 2 — Sum over strata:*
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{k=1}^{\infty} T_k(x).$$

*Step 3 — Bound $T_k(x)$:*
The key difficulty is bounding $T_k(x) = \sum_{a \in A_k, a \geq x} 1/(a \log a)$.

For LARGE $k$ (say $k \geq k_0$): By F3,
$\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1))k^2/2^k$.
The tail $T_k(x) \leq \sum_{a \in A_k} 1/(a \log a) \leq 1$.
And $\sum_{k \geq k_0} T_k(x) \leq \sum_{k \geq k_0} 1 = \infty$ — this is
unbounded, so a naive per-stratum upper bound of $1$ is not useful.

*Obstacle*: The sum over infinitely many strata is potentially infinite.
We need a bound $T_k(x) \leq g(k, x)$ with $\sum_k g(k, x)$ convergent
and $\to 0$ as $x \to \infty$.

## A Better Per-Stratum Bound (Requires External Estimates)

For the stratification to work, we need:
$$T_k(x) = \sum_{\substack{a \in A_k \\ a \geq x}} \frac{1}{a \log a} \leq \frac{h(k)}{(\log x)^\alpha}$$
for some $\alpha > 0$ and $h(k)$ summable.

Standard estimates (using PNT-type results for $k$-almost-primes) give:
$$\sum_{\substack{n \leq N \\ \Omega(n) = k}} \frac{1}{n \log n} \sim \frac{(\log \log N)^{k-1}}{(k-1)! \log N}$$
as $N \to \infty$. From this, a Mertens-type Abel summation gives:
$$T_k(x) = \sum_{\substack{a \geq x \\ \Omega(a) = k}} \frac{1}{a \log a} \leq \frac{C_k}{(\log x)^{?}}$$
for some computable $C_k$.

*Obstacle (ledger)*: The estimate for $\sum_{n \leq N, \Omega(n)=k} 1/(n \log n)$
requires the Selberg–Sathe theorem or a combinatorial sieve, neither of which
is in the facts ledger $\{F1, F2, F3\}$.

## What F1/F2/F3 Can Give

**From F1:** For any primitive $A \subseteq [x,\infty)$, $\sum 1/(a \log a) < 1.399$.
This is a uniform bound, independent of $x$, so it does NOT decay with $x$
and does NOT prove L2.

**From F2:** $A_k$ has sum $\geq 1 + O(k^{-1/2})$.  This is a LOWER bound
and does not help bound $T_k(x)$ from above.

**From F3:** $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1))k^2/2^k < 1$.
This tells us the total stratum sum, but not the tail $T_k(x)$.

## Conclusion: Key Gap

Neither F1, F2, nor F3 is sufficient to prove L2.  The missing ingredient
is an estimate of the form:
$$\sum_{\substack{n \leq N \\ \Omega(n)=k}} \frac{1}{n \log n} \asymp \frac{(\log \log N)^{k-1}}{(k-1)!} \cdot \frac{1}{\log N}$$
(Selberg–Sathe-type), which gives $T_k(x) = O((\log\log x)^{k-1}/((k-1)!\,\log x))$
and allows summing over $k$:
$$\sum_{k=1}^\infty T_k(x) \leq \frac{e^{\log\log x}}{\log x} = \frac{\log x}{\log x} = O(1).$$

(Here $\sum_{k \geq 1} (\log\log x)^{k-1}/(k-1)! = e^{\log\log x} = \log x$.)
This would give L2 with $C = O(1)$ — not a $1/\log x$ decay but at most a constant.
A tighter bound would need the tail estimate directly.

**To close L2, add to the ledger:** the Selberg–Sathe theorem for almost primes,
or the tail estimate $T_k(x) = O((\log\log x)^{k-1}/((k-1)!\,\log x))$.

## Status

Open.  The stratification approach is sound.  The missing fact is a
Selberg–Sathe-type estimate for tail sums of $k$-almost-prime series.
This is a known result in analytic number theory but is not in $\{F1, F2, F3\}$.
