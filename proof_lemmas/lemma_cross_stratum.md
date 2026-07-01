---
id: cross_stratum
status: open
depends_on: [primitivity_shadow]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 3: Cross-Stratum Total < 1 + o(1)

## Statement

Let $A \subset [x, \infty)$ be a primitive set. Then
$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^{\infty} S_k < 1 + o(1)
\quad \text{as } x \to \infty.$$

**Note**: This is exactly the Erdős primitive-set conjecture (restricted to
$A \subset [x, \infty)$). Proving this lemma IS proving the conjecture. The
known result (F1) gives the weaker bound $< e^\gamma\pi/4 + o(1) \approx 1.399 + o(1)$.

## Reduction to a Prime Comparison

**Claim (informal)**: For any primitive $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p \geq x, \, p \text{ prime}} \frac{1}{p \log p}.$$
If this inequality holds, then the left side is bounded by the prime tail
$\sum_{p \geq x} 1/(p \log p)$, which (by general principles) tends to 0 as
$x \to \infty$ — establishing the conjecture with the stronger bound $o(1) < 1 + o(1)$.

**Status**: This comparison is the "primes are extremal" conjecture, which is
STRICTLY STRONGER than the bound we want. Even if the prime tail comparison
fails, the conjecture $< 1 + o(1)$ could still hold.

## What F1, F2, F3 Give

### Using F1 alone

F1 immediately gives $\sum_{a \in A} 1/(a \log a) < e^\gamma\pi/4 + o(1)$. This
is a proved bound, but weaker than the conjectured $1 + o(1)$.

### Using F3 and stratification

By Lemma 1 (Case 2), $S_k \leq$ (full $A_k$ sum) $= 1 - (c+o(1))k^2/2^k$ for large $k$.

However, summing over all $k$ gives:
$$\sum_{k \geq K} S_k \leq \sum_{k \geq K} \left(1 - (c+o(1))\frac{k^2}{2^k}\right)$$

This series DIVERGES as $K \to \infty$ (each term is $< 1$ but approaches 1, and
there are infinitely many). F3 alone does NOT bound the cross-stratum total.

**Conclusion**: F3 bounds each stratum individually but cannot be summed across
infinitely many strata to get a finite bound. Primitivity must provide the
"cancellation" that prevents many strata from each contributing near-1
simultaneously.

### The Primitivity Constraint (Lemma 2)

From Lemma 2 (shadow bound): if $a \in A_j^A$, then no element of $A_j$
that is a multiple of $a$ can be in $A$. This creates dependencies between
strata: elements in stratum $j$ "block" elements in strata $j+1, j+2, \ldots$

**Key question**: Does the blocking from Lemma 2 prevent $\sum_k S_k$ from
approaching 1 from multiple strata simultaneously?

**Partial answer**: For elements $a \in A$ with large $\Omega(a) = k$, the
element $a$ has $\Omega$-order $k$ meaning it has $k$ prime factors (with
multiplicity). If $a \geq x$, then $a$ is "efficient" (large number with many
prime factors only if those factors are small). The "shadow" in stratum $k+1$
includes $a \cdot p$ for all primes $p$ — a large set of elements. The sum
blocked from stratum $k+1$ by $a$ is $\sum_p 1/(ap \log(ap))$, which for
$p \leq a$ is $\sim \frac{1}{a} \sum_{p \leq a} \frac{1}{p \log(ap)}$.

This analysis requires detailed prime distribution estimates beyond F1/F2/F3.

## Partial Bound: Bounding Contributions from Small and Large Strata

**Regime 1 — fixed $k$, $x \to \infty$** (from Lemma 1, Case 1):
For any fixed $K$, $\sum_{k=1}^K S_k \to 0$ as $x \to \infty$, since
each term $\leq \#(A_k^A) \cdot 1/(x \log x)$ and $\#(A_k^A)$ is finite.

**Regime 2 — large $k$ (say $k > K(x)$ for $K(x) \to \infty$)**:
For strata with $k > K(x)$: elements $a \in A_k \cap [x, \infty)$ satisfy
$\Omega(a) > K(x)$. If $K(x) = c \log\log x$, then such $a$ have unusually
many prime factors. By F3, the FULL $A_k$ sum (all $a$ with $\Omega(a)=k$) is
$1 - (c+o(1))k^2/2^k$, but only the $[x,\infty)$ restriction contributes to $S_k$.
The $[x,\infty)$ restriction makes $S_k \to 0$ for each fixed $k$.

**Regime 3 — intermediate $k$** (the hard case): $k \sim \log\log x$ or
$k \sim \log x$. Elements with $\Omega(a) \sim \log\log x$ and $a \geq x$:
these are numbers $\geq x$ with $\sim \log\log x$ prime factors (near the
typical number of prime factors for integers of size $x$, by Hardy-Ramanujan).
The density of such numbers in $[x, \infty)$ and how they interact via
primitivity is the unresolved core of the problem.

## Next Steps

1. **Try to bound the intermediate regime** using F3: for $k \sim \log\log x$,
   $1 - (c+o(1))k^2/2^k \approx 1 - c(\log\log x)^2 / x^{\log 2}$, which is
   close to 1 for large $x$. F3 doesn't help here without additional structure.

2. **Try a weight function approach**: define weights $w_a$ such that
   $\sum_{a \in A} 1/(a \log a) \leq \sum_{a \in A} w_a$ and the right side
   is bounded via a sieve or inclusion-exclusion argument using F1.

3. **Try to exploit the $o(1)$ in the conjecture's bound more carefully**:
   the $o(1)$ means for any $\varepsilon > 0$, sum $< 1 + \varepsilon$ for
   large enough $x$. Maybe the bound degrades gracefully and can be established
   for a specific $\varepsilon$ sequence.

**Status: open.** The cross-stratum bound is the conjecture itself. Partial
progress: each stratum is bounded separately (Lemma 1), but no cross-stratum
argument has been found using only F1/F2/F3.
