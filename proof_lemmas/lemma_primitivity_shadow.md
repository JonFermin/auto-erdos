---
id: primitivity_shadow
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma 2: Primitivity Shadow Bound

## Statement

Let $A \subset [x, \infty)$ be a primitive set and $k \geq 1$. Define
$$S_k = \sum_{\substack{a \in A \\ \Omega(a) = k}} \frac{1}{a \log a}.$$

**Qualitative form** (proved): For each $a \in A$ with $\Omega(a) = j$, no
multiple $am$ (for $m \geq 2$) belongs to $A$. In particular, the set
$\{am : m \geq 1, \, \Omega(am) = j+1\} = \{ap : p \text{ prime}\}$ is
entirely excluded from $A$.

**Quantitative form** (open): There exists a function $\psi(x) \to 0$ such that
$$\sum_{k \geq 1} S_k < 1 + \psi(x).$$
The goal is to prove $\psi(x) = o(1)$ (i.e., $\psi(x) \to 0$ as $x \to \infty$).

## Qualitative Proof

**Proof of qualitative form**: Direct from primitivity. If $a \in A$ and
$am \in A$ for some $m \geq 2$, then $a | am$ and $a \neq am$, violating
primitivity. So $A \cap \{am : m \geq 2\}$ is empty for each $a \in A$. $\square$

**Corollary (within-stratum non-divisibility)**: For any two distinct
$a, b \in A$ with $\Omega(a) = \Omega(b) = k$, $a \nmid b$ and $b \nmid a$.
*Proof*: if $a | b$ with $a \neq b$, then $b = am$ for $m \geq 2$, contradicting
primitivity. $\square$

## Quantitative Analysis (open)

### The Key Comparison

For each $a \in A_j^A$ (stratum $j$ contribution to $A$), consider what is
"blocked" in stratum $j+1$: the set $\{ap : p \text{ prime}\} \cap [x, \infty)$.
Each blocked element $ap$ would contribute $1/(ap \log ap)$ to the sum.

**Comparison inequality** (to be proved): Is it true that
$$\frac{1}{a \log a} \geq \sum_{p \text{ prime}} \frac{1}{ap \log(ap)}?$$

The right-hand side is $\frac{1}{a} \sum_p \frac{1}{p \log(ap)}$. Since
$\log(ap) \leq \log a + \log p \leq 2 \max(\log a, \log p)$, a lower bound
requires knowing the relative sizes of $a$ and $p$. For $a \geq x$ large,
if $p < a$, then $\log(ap) \approx \log a + \log p < 2\log a$, giving
$\sum_p 1/(ap \log(ap)) > \sum_p 1/(2ap \log a) = \frac{1}{2a \log a} \sum_p \frac{1}{p}$,
which diverges — showing the naive comparison fails.

### What the Comparison Should Measure

The correct comparison is not per-element but global. The idea (following the
spirit of Zhang's 1993 proof of F1) is to use a weight function $w$ such that:
$$\sum_{a \in A} \frac{1}{a \log a} \leq \sum_{a \in A} w(a) \cdot (\text{prime density at scale } a)$$

where the right-hand side telescopes using primitive structure.

Zhang's approach uses: for each $a \in A$ with largest prime factor $P^+(a) = p$,
bound $1/(a \log a)$ in terms of $1/(p \log p)$, and use the fact that each
prime $p$ can appear as $P^+$ of at most one element of $A$ (this follows from
primitivity in a subtle way).

### Current Status

The qualitative statement is proved. The quantitative bound requires:
1. A precise "largest prime factor" decomposition of $A$ (Zhang's key step).
2. A Mertens-type estimate bounding $\sum_{p \geq x} 1/(p \log p)$.
3. A telescoping argument showing the cross-stratum total is bounded by the prime tail.

**Obstacle**: Steps 2 and 3 require facts about prime distribution not in the
given-facts ledger (F1, F2, F3). F1 itself may be the source of the bound, but
the argument needs to go through F1 cleanly without invoking unlicensed theorems.

### Next Move

Attempt to use F1 directly as the bounding mechanism: since F1 gives
$\sum_{a \in A} 1/(a \log a) < e^\gamma\pi/4 + o(1)$ for any primitive
$A \subset [x, \infty)$, the cross-stratum total is already bounded. The
conjecture strengthens this to $< 1 + o(1)$, and the strengthening must come
from a structural argument about how primitivity at large $x$ limits the sum.

The quantitative shadow bound may emerge by considering only those strata $k$
with $k \leq K(x)$ for some $K(x) \to \infty$ (the "relevant" strata), and
showing strata $k > K(x)$ contribute negligibly by F3.
