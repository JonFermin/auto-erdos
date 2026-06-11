---
id: f1_gap
status: open
depends_on: [cross_stratum_sum]
discharged_by_round: null
introduced_at_round: 4
---

# Lemma f1_gap: Closing the gap from F1 (1.399) to the conjectured bound (1)

**Statement.** For any primitive set $A \subset [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} < 1 + o(1)$$
where $o(1) \to 0$ as $x \to \infty$.

---

## What F1 gives and the gap to close

By F1 (Zhang 1993), for ANY primitive $A \subseteq \mathbb{N}$:
$$\sum_{a \in A} \frac{1}{a \log a} < 1.399 + o(1).$$

The improvement from $1.399$ to $1$ is the open gap. The restriction $A \subset [x, \infty)$ should help because large $x$ forces each term $1/(a \log a) \leq 1/(x \log x) \to 0$; the question is whether this "small-term" effect can be parlayed into a global bound.

---

## Partial result: Dyadic decomposition upper bound (OPEN — gap in argument)

Partition $A$ by dyadic intervals: $A = \bigsqcup_{j \geq 0} A^{(j)}$ where $A^{(j)} = A \cap [2^j x, 2^{j+1} x)$.

For elements in dyadic block $j$:
$$\sum_{a \in A^{(j)}} \frac{1}{a \log a} \leq \frac{|A^{(j)}|}{2^j x \cdot \log(2^j x)}.$$

Since every subset of $[N, 2N)$ is a primitive set (no element in $[N, 2N)$ divides another, because $b/a \in (1, 2)$ for $N \leq a < b < 2N$, which is never an integer), the primitivity constraint does NOT restrict $|A^{(j)}|$ within a single dyadic block. We only have $|A^{(j)}| \leq 2^j x$.

Substituting: the contribution from block $j$ is at most
$$\frac{2^j x}{2^j x \cdot \log(2^j x)} = \frac{1}{\log(2^j x)} = \frac{1}{\log x + j \log 2}.$$

Summing over $j \geq 0$:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{j \geq 0} \frac{1}{\log x + j \log 2}.$$

This sum DIVERGES (it is a harmonic-type series). So the dyadic decomposition with the trivial antichain bound is too crude.

**The failure mode.** The triviality that every subset of $[N, 2N)$ is primitive means the antichain constraint contributes nothing within a single dyadic interval. The primitivity must be used ACROSS dyadic intervals to limit the total density.

---

## Approach: Cross-interval primitivity constraint

When $a \in A^{(j)}$ and $b \in A^{(j')}$ with $j' > j$, primitivity requires $a \nmid b$. This cross-interval constraint means: fixing $a \in A^{(j)}$, the elements $b = 2a, 3a, \ldots$ are excluded from $A$. How many elements does this eliminate?

For $a \in [2^j x, 2^{j+1} x)$ and $b \in [2^{j'} x, 2^{j'+1} x)$ with $b = ma$ (integer $m \geq 2$):
- $m \approx 2^{j'-j}$, so multiples $ma$ with $m \in [2^{j'-j}, 2^{j'-j+1})$ land in block $j'$.
- There are $\sim 2^j x$ elements in $A^{(j)}$, each excluding $\sim 1$ multiple per block $j' > j$.

The total number of "exclusions" from all $a \in A^{(j)}$ in block $j'$ is at most $|A^{(j)}|$ (since each $a$ excludes at most one multiple in $[2^{j'} x, 2^{j'+1} x)$ per specific multiple $m$). This argument limits $|A^{(j')}|$ based on $|A^{(j)}|$, but turning this into a quantitative bound on the sum requires a recursive estimate — which is exactly the sieve approach used by Erdős and Zhang.

---

## Empirical evidence from witness search (Q4)

Witness search via `library.primitive_set_witness.verify_witness` on several candidate types shows the sum is well below 1 for $x \geq 100$:

| Candidate | $x_\text{floor}$ | Sum (rigorous lower bound) |
|---|---|---|
| 50 primes in $[1000, 2000]$ | 1000 | $\approx 0.0061$ |
| 100 primes in $[10000, 20000]$ | 10000 | $\approx 0.0010$ |
| All 100 integers in $[101, 201)$ | 101 | $\approx 0.1396$ |
| All 1000 integers in $[1001, 2001)$ | 1001 | $\approx 0.0956$ |

The "fat antichain" rows (all integers in a dyadic interval) are the most adversarial: they maximize density within a dyadic block. Yet their sum is $\ll 1$ for $x \geq 100$. This strongly suggests the conjecture holds, though numerical evidence does not constitute a proof.

**Monotonicity of the fat antichain sum.** For $A = \{N, N+1, \ldots, 2N-1\}$:
$$\sum_{a=N}^{2N-1} \frac{1}{a \log a} < \int_{N}^{2N} \frac{dt}{t \log t} = \log\!\left(\frac{\log 2N}{\log N}\right) = \log\!\left(1 + \frac{\log 2}{\log N}\right) \approx \frac{\log 2}{\log N} \to 0.$$
This integral bound uses only basic calculus (no ledger fact needed). It proves that the fat antichain sum is $O(1/\log N)$, consistent with $o(1)$ as $N \to \infty$.

**Observation.** The fat antichain is NOT a primitive set over all of $[x, \infty)$ — it only covers one dyadic block. When concatenating fat antichains from multiple blocks, cross-block primitivity constraints kick in and restrict which elements can coexist. Whether the multi-block cross-constraint keeps the total $< 1 + o(1)$ is the open question.

---

## Alternative approach: Smooth-rough decomposition

Split $A = A_{\mathrm{rough}} \cup A_{\mathrm{smooth}}$ where:
- $A_{\mathrm{rough}}$: elements whose smallest prime factor $p(a) \geq y(x)$ for some threshold $y(x)$.
- $A_{\mathrm{smooth}}$: elements with $p(a) < y(x)$.

For $A_{\mathrm{smooth}}$: each element $a$ has a small prime factor $\leq y(x)$; bounding the contribution of $A_{\mathrm{smooth}}$ requires controlling how many "smooth-above" elements from $[x, \infty)$ can coexist in a primitive set.

For $A_{\mathrm{rough}}$: elements are "$y$-rough", so their smallest prime factor is $\geq y$. For large $y$, rough elements are sparse in $[x, \infty)$, suggesting their contribution is $o(1)$.

Whether this decomposition closes the gap from $1.399$ to $1 + o(1)$ is an open question. Both parts are bounded by F1 (giving 1.399 total), and tightening requires new analytic estimates outside the current given-facts ledger.

---

## Status summary

| Sub-claim | Status | Follows from |
|-----------|--------|--------------|
| Sum < 1.399 for any primitive $A \subset [x, \infty)$ | **Proved** | F1 |
| Dyadic decomposition gives finite bound | **Partial** — bound diverges without cross-interval constraint | — |
| Cross-interval primitivity limits total density | **Plausible** — requires sieve/product argument | Qualitative, not proved |
| Sum < $1 + o(1)$ via smooth-number decomposition | **Open** — approach outlined but not closed | Requires new estimate |
| Full lemma f1_gap: sum < $1 + o(1)$ | **Open** | The conjecture itself |
