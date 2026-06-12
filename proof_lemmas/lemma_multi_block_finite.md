---
lemma_id: lemma_multi_block_finite
status: proved
proved_in_session: s_0612-080410-fd09
depends_on: lemma_single_interval
---

# Lemma multi_block_finite

## Statement

For any set $A \subseteq [x, 2^N x)$ and any integer $N \geq 1$:
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{N \log 2}{\log x}.$$

As $x \to \infty$ with $N$ fixed, the right-hand side tends to $0$.

## Proof

By integral comparison: $1/(t \log t)$ is decreasing for $t \geq 3$, so
$$\sum_{a \in A} \frac{1}{a \log a} \leq \int_x^{2^N x} \frac{dt}{t \log t} = \log\log(2^N x) - \log\log x = \log\!\left(1 + \frac{N\log 2}{\log x}\right) < \frac{N\log 2}{\log x}.$$

The last step uses $\log(1+u) < u$ for $u > 0$. $\square$

## Special cases

- $N=1$: Lemma single\_interval ($A \subseteq [x,2x)$, sum $< \log 2/\log x$).
- $N=2$: two-block case in proof\_strategy.md Section 5.

## Corollary

For any $M > 1$ and $A \subseteq [x, Mx)$: with $N = \lceil \log_2 M \rceil$, sum $< \lceil\log_2 M\rceil \log 2 / \log x \to 0$.

## Limitation

For $A \subseteq [x, \infty)$ spanning infinitely many blocks, the naive sum of per-block bounds diverges. The infinite-extent case requires the primitive constraint.
