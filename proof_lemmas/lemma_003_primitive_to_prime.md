---
id: primitive_to_prime
status: open
depends_on: [prime_tail_decay]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 3 (Hard): Primitive sets are bounded by the prime-tail sum

**Target statement.** For any primitive set $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p \geq x} \frac{1}{p \log p} + o(1) \quad \text{as } x \to \infty.$$

If true, this combined with Lemma 2 would prove the Erdős conjecture: since
$\sum_{p \geq x} 1/(p \log p) \to 0 < 1$, we get
$\sum_{a \in A} 1/(a \log a) < 1 + o(1)$.

**Why this is hard (and why a naive bound fails).**

The inequality does NOT follow from monotonicity alone. For a primitive set $A
\subset [x, \infty)$ that includes composite numbers, the composite elements
can contribute to the sum independently of the primes. For example, at $x=3$
the set $\{3, 4\}$ is primitive and gives $\sum = 0.483 > 0.427 = 1/(3\log 3)
+ 1/(5 \log 5)$ (the primes $3, 5$). So primitive sets CAN exceed the "same
number of primes" bound.

**Comparison with the Erdős-Zhang proof technique:**

Zhang (1993) proved F1 using the following key lemma (paraphrased):

*For a primitive set $A$, assign to each $a \in A$ its "smallest prime
factor" $\text{spf}(a) = p$. For each prime $p$, the elements of $A$
with $\text{spf} = p$ form a primitive subset of $\{n : p | n, n/p \text{ has no prime factor} < p\}$. By recursion / Euler product arguments, the total contribution can be bounded by $\sum_p 1/(p \log p) \cdot C$ for some constant $C$.*

This gives the F1 bound ($\approx 1.399$), but not the tighter bound of 1.

**What the $1 + o(1)$ bound requires beyond F1:**

For the bound to approach 1 as $x \to \infty$, one needs to show that
elements of $A$ with large smallest-prime-factor (i.e., near-prime elements in
$[x, \infty)$) have collectively small sum. Equivalently: the "weight" of $A$
attributable to primes $p \geq x$ must be $< 1 + o(1)$.

The key obstacle: elements of $A$ that are products of two or more large primes
(e.g., $a = p \cdot q$ with $p, q \geq \sqrt{x}$) contribute independently and
are hard to relate to a single prime's "slot" in the bound.

**Approaches to try:**

1. **Exploit primitivity more strongly.** If $a, b \in A$ with $a | b$, that's
   a contradiction. This means $A$ is an antichain in the divisibility poset.
   Dilworth's theorem says the maximum antichain equals the minimum chain cover.
   But this is in terms of cardinality, not weighted sum.

2. **Omega-k stratification + union bound.** Write
   $A = \bigcup_k (A \cap A_k)$ and sum the bounds. The challenge: bounds for
   each stratum separately overcounts (elements in different strata can
   "compete" for the same prime slot).

3. **Greedy algorithm argument.** The greedy primitive set (Lemma 1's Section
   §2.3) shows that at $x=3$, the greedy achieves sum $\approx 1.003$, barely
   above 1. For $x \geq 5$, the greedy stays below 1. This suggests the
   conjecture IS true for $x \geq 5$ (no primitive set in $[5, \infty)$ exceeds
   1), but a proof is lacking.

4. **Lichtman-Pomerance (2022) technique.** The actual proof uses harmonic
   analysis and multiplicative number theory (Euler product expansions,
   Mertens-type estimates). This requires tools beyond the given-facts ledger.

**Current obstacle**: Cannot prove this without citing a major result like
Lichtman-Pomerance. The given-facts ledger (F1, F2, F3) does not include the
key comparison lemma. This lemma remains **open**.

**Partial result**: Numerically, for $x_{\text{floor}} \geq 5$, greedy
construction gives sum $< 1$ (§2.3). The conjecture appears true for $x \geq
5$ by numerical evidence, but no proof is available within the current facts ledger.
