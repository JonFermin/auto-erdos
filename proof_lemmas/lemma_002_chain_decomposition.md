---
id: chain_decomposition
status: partial
depends_on: [dense_antichain]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 2: Chain Decomposition — Partial Result

## Statement

For any primitive set $A \subset [x, \infty)$ with $x \geq 2$, write each
$a \in A$ as $a = 2^{e(a)} m(a)$ where $m(a)$ is the odd part of $a$.
Define:
$$S_{\mathrm{small}}(A, x) = \sum_{\substack{a \in A \\ m(a) < x}} \frac{1}{a \log a}, \qquad
S_{\mathrm{large}}(A, x) = \sum_{\substack{a \in A \\ m(a) \geq x}} \frac{1}{a \log a}.$$

**Proved partial result:**
$$S_{\mathrm{small}}(A, x) \leq \frac{1}{2 \log x}.$$

**Open part:** $S_{\mathrm{large}}(A, x)$ is bounded by a primitive set of odd
numbers in $[x, \infty)$, reducing to the same conjecture type for odd inputs.

## Proof of the partial result

**Step 1: Chain structure.**

The integers partition into chains: for each odd $m \geq 1$, the chain of $m$
is $\{m, 2m, 4m, 8m, \ldots\}$. Since distinct elements of the same chain are in
a divisibility relation, a primitive set $A$ contains at most one element from
each chain. Thus the odd parts $\{m(a) : a \in A\}$ are distinct.

Moreover, if $m(a) \mid m(b)$ for $a, b \in A$ with $a \neq b$: write $m(b) = j \cdot m(a)$
for integer $j \geq 1$. If $e(a) \leq e(b)$, then $a = 2^{e(a)} m(a)$ divides
$2^{e(b)} m(b) = 2^{e(b)-e(a)} \cdot 2^{e(a)} \cdot j m(a)$, so $a \mid b$ — contradicting
primitivity. Symmetrically if $e(b) < e(a)$ and $m(b) \mid m(a)$, then $b \mid a$.
So the odd parts $\{m(a) : a \in A\}$ are pairwise non-divisible (this justification
is used in the large-chain reduction; the small-chain bound only needs distinctness).

**Step 2: Small-chain contribution.**

For $a \in A$ with $m(a) < x$: since $a \geq x$, we need $2^{e(a)} m(a) \geq x$,
so $e(a) \geq \lceil \log_2(x/m(a)) \rceil$. In particular $a \geq x$, so:
$$\frac{1}{a \log a} \leq \frac{1}{x \log x}.$$

The odd parts $\{m(a) : a \in A, m(a) < x\}$ are distinct odd integers in
$[1, x)$. There are at most $\lfloor x/2 \rfloor < x/2$ odd integers in $[1, x)$,
so $|\{m(a) : m(a) < x\}| \leq x/2$.

Therefore:
$$S_{\mathrm{small}}(A, x) \leq \frac{x/2}{x \log x} = \frac{1}{2 \log x}. \quad \square$$

## Reduction for the large-chain part

For $a \in A$ with $m(a) \geq x$: since $a = 2^{e(a)} m(a) \geq m(a) \geq x$,
we have $1/(a \log a) \leq 1/(m(a) \log m(a))$.

The set $B = \{m(a) : a \in A, m(a) \geq x\}$ is a primitive set of odd numbers
in $[x, \infty)$ (pairwise non-divisible, shown in Step 1). Thus:
$$S_{\mathrm{large}}(A, x) \leq \sum_{m \in B} \frac{1}{m \log m}.$$

This reduces Lemma 2 (for general integers) to the same conjecture for odd integers.

## Combining

$$\sum_{a \in A} \frac{1}{a \log a} \leq \frac{1}{2 \log x} + \sum_{m \in B} \frac{1}{m \log m}$$

where $B$ is a primitive set of odd integers in $[x, \infty)$.

## Current obstacle (why this does not close the conjecture)

Applying the same decomposition to $B$ (primitive odd integers in $[x, \infty)$):
- Odd integers' chains are defined by $\{m, 3m, 9m, \ldots\}$ (3-adic chains) or
  by $\{m, pm, p^2m, \ldots\}$ for some prime $p$.
- The argument recurses, but each step introduces a factor slightly smaller than $1/\log x$.
- Summing the geometric recursion: if $f_{\mathrm{odd}}(x)$ denotes the supremum over
  primitive odd sets in $[x, \infty)$, then the decomposition gives
  $f_{\mathrm{odd}}(x) \leq 1/(2\log x) + f_{\mathrm{odd}}(x + \Delta)$ for some $\Delta > 0$,
  which again leads to a divergent sum unless $f_{\mathrm{odd}}$ decays sufficiently fast.

The quantitative cross-layer primitivity constraint (elements from different layers
cannot be in a divisibility relation) is the key to closing this recursion, but
its exploitation requires techniques beyond those available from the given ledger facts.

## Consequence

The partial result $S_{\mathrm{small}} \leq 1/(2\log x)$ shows that the
"spread-out small elements" cannot contribute significantly to the sum.
The open part is entirely from elements with large odd part ($m(a) \geq x$),
i.e., elements that are themselves odd or have only small powers of 2 as their
2-adic component relative to $x$.
