---
id: cross_stratum_control
status: abandoned
depends_on: [stratum_sub_bound, large_floor_vanish]
discharged_by_round: null
introduced_at_round: 1
---

# Lemma: cross-stratum control (the open core)

**Statement** (conjectured; not proved): For any primitive set $A \subset
[x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1) \quad (x \to \infty).$$

This is equivalent to the main conjecture. It is stated as a lemma to
isolate the part that the stratification approach cannot handle.

---

## Why the per-stratum approach fails

From `lemma_stratum_sub_bound` and `lemma_large_floor_vanish`, we have:

$$\sum_{a \in A} \frac{1}{a \log a} = \sum_{k=1}^\infty S_k(A,x)$$

where $S_k(A,x) \leq T_k(x) \leq 1 - ck^2/2^k < 1$ for each $k$.

Summing: $\sum_{k=1}^\infty (1-ck^2/2^k) = \infty$ since the terms $\to 1$.
The per-stratum bounds are individually useful but globally vacuous.

## The critical stratum regime

Set $k^* = \lfloor \log_2 x \rfloor$. For strata $k \approx k^*$:
- The smallest $k$-almost prime is $2^k \approx x$, so elements in $[x, \infty)$
  are not restricted away from the full $k$-stratum.
- The per-stratum bound is $T_{k^*}(x) \approx T_{k^*}(2) = 1 - ck^{*2}/2^{k^*}
  \approx 1 - c(\log_2 x)^2/x$, close to 1.
- Summing over $k \in [k^* - C, k^* + C]$ (a window of width $2C$) gives
  $\approx 2C \cdot (1 - c(\log_2 x)^2/x)$, which diverges as $C \to \infty$.

Any proof of the conjecture must show that a primitive set $A \subset [x, \infty)$
cannot use "full weight" from many strata near $k^*$ simultaneously.

## What primitivity means for this regime

Let $A^{(k)} = \{a \in A : \Omega(a) = k\}$. For two elements $a \in A^{(j)}$
and $b \in A^{(k)}$ with $j < k$, the primitivity condition $a \nmid b$ says
$b$ is NOT a multiple of $a$. The "antichain" structure forbids clustering.

The challenge: elements in stratum $j$ rule out specific multiples in stratum
$k$, but the density of $k$-almost primes is much higher than $j$-almost primes,
so the ruling-out is local and does not globally bound $S_k(A,x)$ below
$T_k(2) - \epsilon$.

## Approaches that were investigated and WHY they fail

1. **Dyadic interval counting (FAILS — gives O(log x), not O(1))**:
   
   Partition $[x, \infty)$ into dyadic intervals $I_j = [x2^j, x2^{j+1})$
   for $j = 0, 1, 2, \ldots$ In each interval, ALL elements form a primitive
   set (since if $a, b \in [N, 2N)$ with $a < b$ and $a|b$, then $b \geq 2a > 2N$,
   a contradiction). So the per-interval contribution is bounded by:
   $$\sum_{a \in A \cap I_j} \frac{1}{a \log a}
     \leq \sum_{n \in I_j} \frac{1}{n \log n}
     \approx \ln\!\left(1 + \frac{\log 2}{\log x + j \log 2}\right)
     \approx \frac{\log 2}{\log x + j \log 2}.$$
   Summing over all $j$:
   $$\sum_{a \in A} \frac{1}{a \log a}
     \leq \sum_{j=0}^\infty \frac{\log 2}{\log x + j \log 2}
     = \sum_{j=0}^\infty \frac{1}{\log_2 x + j}$$
   which is a DIVERGENT harmonic tail. The per-interval bound does not give a
   convergent global sum; the global primitivity constraint (cross-interval
   divisibility) must be used but the dyadic decomposition does not encode it.

2. **Mertens / Abel summation**: Standard Mertens-type estimates give
   $\sum_{n \leq x, \Omega(n)=k} 1/n \sim (\log\log x)^{k-1}/((k-1)! \log x)$.
   For $k = k^* = \lfloor \log_2 x \rfloor$, this is
   $\sim (\log_2 x \cdot \log 2)^{k^*-1} / ((k^*-1)! \log x)$, which is a
   non-trivial quantity. Without the primitivity constraint, summing
   $1/(n \log n)$ over $n \leq N$ in stratum $k$ gives $\sim 1 - ck^2/2^k$
   (by F3). Using primitivity to sharpen this requires a sieve-type argument.

3. **Generating function approach**: $F_A(s) = \sum_{a \in A} a^{-s}$ for
   a primitive set $A$ satisfies the "sub-multiplicativity" property via
   Rankin's trick: $F_A(s) \leq F_P(s) = \sum_{p \text{ prime}} p^{-s}$ for
   $s > 1$ (by the Erdős argument). But extracting the constant at $s=1$
   (the $1/(a \log a)$ sum) from the behavior of $F_A(s)$ near $s=1$
   requires a Tauberian theorem and control over the $o(1)$ correction.

## Current obstacle

No approach above closes the conjecture. The gap is: bounding
$\sum_{k \sim \log_2 x} S_k(A, x)$ uniformly over primitive sets $A \subset
[x, \infty)$ by something that, combined with the low-stratum $o(1)$, gives a
total bound of $1 + o(1)$.

This may require new ideas beyond F1–F3.

---

**Abandoned 2026-07-18 (session s_0718-205004-c44a).** The parent claim
`primitive_set_erdos` (Erdős #1196) was proved in the literature in May
2026 (arXiv:2605.00301) and the spec was reclassified as a rediscovery
benchmark in the 2026-07-11 audit. This attempt is concluded; the lemma
is retained as audit trail. Nothing here is wrong — it is simply moot as
research (the o(1) gap it chased is closed by the published proof).
