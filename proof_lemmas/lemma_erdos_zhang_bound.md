---
id: erdos_zhang_bound
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 3
---

# Lemma: Erdős-Zhang bound and its limitations

**Statement** (F1, proved): For any primitive $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} < e^{\gamma} \frac{\pi}{4} + o(1) \approx 1.399 + o(1)$$
where the $o(1)$ holds as $\min(A) \to \infty$.

This is a PROVED result (Erdős 1935 + Zhang 1993), not an open conjecture.

**Clarification of the $o(1)$ for large sets**: For $A = \{2, 3, 5, 7, ...\}$
(all primes), the sum is $\approx 1.637 > 1.399$. This is NOT a contradiction
because $\min(A) = 2$ makes the $o(1)$ large. F1 only claims sum $< 1.399 + C/\log(\min A)$
for some constant $C$; for $\min A = 2$, this is $< 1.399 + C/0.693$, which can
accommodate 1.637 if $C$ is moderate.

F1 says: for fixed $\epsilon > 0$, if $\min(A)$ is large enough (depending on $\epsilon$),
then $\sum < 1.399 + \epsilon$. Asymptotics only.

**Proof sketch** (Erdős 1935, rough):
For each prime $p$, group $A$ into $A_p := \{a \in A : p$ is the smallest prime
factor of $a\}$. The $A_p$ partition $A$. For each $p$, show
$\sum_{a \in A_p} 1/(a \log a) \leq 1/(p \log p) + \text{error}$
(roughly: $A_p$ elements are all divisible by $p$ and pairwise non-divisible,
so $A_p / p$ is a primitive set of integers each $> 1$; recurse). Summing over
$p$ and using $\sum_p 1/(p \log p) \approx 1.637$ gives F1.

**Key gap between F1 and the conjecture**: The conjecture asserts the bound is
$1 + o(1)$, not $1.399 + o(1)$. The gap from 1.399 to 1 is the content of the
open problem. Heuristically, the tighter bound should hold because:

1. For large $x$, primitive sets in $[x, \infty)$ are "sparse" — they can
   only use a small fraction of each interval $[x, 2x]$, $[2x, 4x]$, etc.
2. The sum over ALL integers $\geq x$ (not just a primitive subset) is
   $\sum_{n \geq x} 1/(n \log n) = \int_x^\infty dt/(t \log t) = 1/\log x \to 0$.
   A primitive set is a sparse antichain within these integers.

**Current obstacle**: The Erdős proof method gives ~1.399 because the recursion
loses a constant factor. To get the tight bound 1, one likely needs to use
the "stratum structure" (via $\Omega$) more carefully, not just the smallest prime
factor. See `lemma_cross_stratum.md` for an attempt at this approach.
