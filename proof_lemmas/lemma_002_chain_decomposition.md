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

Moreover, odd parts are distinct: if $m(a) = m(b)$ for $a \neq b$, then $a$ and $b$
are in the same chain $\{m, 2m, 4m, \ldots\}$, so one divides the other —
contradicting primitivity.

**Key constraint (not full non-divisibility):** If $m(a) \mid m(b)$ and $e(a) \leq e(b)$,
then $a = 2^{e(a)} m(a)$ divides $2^{e(b)} m(b) = a$, so $a \mid b$ — contradicting
primitivity. Hence: if $m(a) \mid m(b)$ for distinct $a, b \in A$, then
necessarily $e(a) > e(b)$ (the 2-adic valuation DECREASES in the divisibility direction).

**Note on non-divisibility:** The odd parts are NOT necessarily pairwise non-divisible.
Example: $A = \{6, 15\}$ is primitive ($6 \nmid 15$, $15 \nmid 6$), yet
$m(6) = 3 \mid 15 = m(15)$. The key constraint is that any divisibility chain
$m(a_1) \mid m(a_2) \mid \cdots$ in the odd parts must correspond to a DECREASING
sequence of 2-adic valuations $e(a_1) > e(a_2) > \cdots$ in $A$.

**Step 2: Small-chain contribution.**

For $a \in A$ with $m(a) < x$: since $a \geq x$, we need $2^{e(a)} m(a) \geq x$,
so $e(a) \geq \lceil \log_2(x/m(a)) \rceil$. In particular $a \geq x$, so:
$$\frac{1}{a \log a} \leq \frac{1}{x \log x}.$$

The odd parts $\{m(a) : a \in A, m(a) < x\}$ are distinct odd integers in
$[1, x)$. There are at most $\lfloor x/2 \rfloor < x/2$ odd integers in $[1, x)$,
so $|\{m(a) : m(a) < x\}| \leq x/2$.

Therefore:
$$S_{\mathrm{small}}(A, x) \leq \frac{x/2}{x \log x} = \frac{1}{2 \log x}. \quad \square$$

## Reduction for the large-chain part (corrected)

For $a \in A$ with $m(a) \geq x$: since $a = 2^{e(a)} m(a) \geq m(a) \geq x$,
we have $1/(a \log a) \leq 1/(m(a) \log m(a))$.

The set $M = \{m(a) : a \in A, m(a) \geq x\}$ is a set of **distinct** odd integers
in $[x, \infty)$ (distinctness proved above). Thus:
$$S_{\mathrm{large}}(A, x) \leq \sum_{m \in M} \frac{1}{m \log m}.$$

**Important limitation:** $M$ is merely distinct, not pairwise non-divisible.
A bound on $\sum_{m \in M} 1/(m \log m)$ over all distinct odd $M \subset [x, \infty)$
is $\sum_{n \geq x, n \text{ odd}} 1/(n \log n)$, which diverges. So the large-chain
reduction does NOT give a useful bound without further constraints.

**Additional structure:** By the key constraint, any divisibility chain in $M$ has
strictly decreasing 2-adic valuations in $A$. Since $e(a) \geq 0$ for all $a$,
divisibility chains in $M$ have length at most $\max_{a \in A} e(a) + 1$. But
$\max e(a)$ is unbounded for general $A$, so this does not bound the sum.

This reveals that the large-chain bound requires a fundamentally different approach.

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
