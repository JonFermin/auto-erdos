---
id: 2adic_stratum
status: partial
depends_on: [chain_decomposition]
discharged_by_round: null
introduced_at_round: 10
---

# Lemma 3: 2-Adic Stratum Decomposition

## Key Observation (proved)

**Within a fixed 2-adic stratum, odd parts are pairwise non-divisible.**

Let $A \subset [x, \infty)$ be primitive. Write $a = 2^{e(a)} m(a)$ ($m(a)$ odd).
For fixed $e \geq 0$ define $M_e = \{m(a) : a \in A,\; e(a) = e,\; m(a) \geq x\}$.

**Claim:** $M_e$ is pairwise non-divisible.

**Proof:** If $m_1, m_2 \in M_e$ with $m_1 \mid m_2$, then $a_1 = 2^e m_1$
divides $a_2 = 2^e m_2$, contradicting primitivity of $A$. $\square$

This corrects Lemma 2's error: $M = \bigcup_e M_e$ is only distinct (not
pairwise non-div), but each stratum $M_e$ separately is primitive.

## Structural Consequence

$$S_{\text{large}}(A, x) = \sum_{e \geq 0} \sum_{m \in M_e} \frac{1}{2^e m \log(2^e m)}
\leq \sum_{e \geq 0} \frac{1}{2^e} \sum_{m \in M_e} \frac{1}{m \log m}.$$

Each $M_e$ is a primitive set of odd integers in $[x,\infty)$, so:

$$\boxed{S_{\text{large}}(A,x) \leq 2\, f_{\text{odd}}(x)},$$

where $f_{\text{odd}}(x) = \sup\bigl\{\sum_{b \in B} 1/(b \log b) :
B \subset [x,\infty) \text{ primitive, all } b \text{ odd}\bigr\}$.

Combined with Lemma 2:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{1}{2\log x} + 2\, f_{\text{odd}}(x).$$

## Why the Recursion Diverges

Applying the same 3-adic decomposition to odd primitive sets, then 5-adic, etc.,
yields a product factor $\prod_p p/(p-1) = \zeta(1) = \infty$. The inter-stratum
primitivity constraints (which tie the $M_e$'s together in $A$) are discarded
when each stratum is bounded independently, so no finite bound emerges.

## What This Rules Out

1. Layer-by-layer Lemma 1 on dyadic layers: $\sum_k \log 2/\log(2^k x)$ diverges.
2. Naive odd-part reduction (Lemma 2 original): $M$ not pairwise non-div.
3. Iterated prime-stratum recursion: product $\prod_p p/(p-1) = \infty$.
4. Chain-length bound via $\max e(a)$: $\max e(a)$ unbounded for infinite $A$.

## What Remains Open

Bounding $f_{\text{odd}}(x)$ independently requires a Selberg/Turán-type argument
or direct use of the Euler product structure of $\sum 1/(a \log a)$; neither
follows from F1–F3 alone. The actual Erdős–Zhang proof (1993) uses Turán's
power-sum method, which is outside the given ledger.

*Status: PARTIAL — the reduction $S_{\text{large}} \leq 2 f_{\text{odd}}$ is proved;
closing the recursion is open.*
