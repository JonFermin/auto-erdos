---
id: single_interval
status: proved
depends_on: []
discharged_by_round: 5
introduced_at_round: 5
---

# Lemma single_interval: Sum over one dyadic interval vanishes

**Statement.** For any set $A \subseteq [x, 2x)$ (integer $x \geq 2$),
$$\sum_{a \in A} \frac{1}{a \log a} < \frac{\log 2}{\log x}.$$
In particular, this bound tends to $0$ as $x \to \infty$.

**Remark.** Every subset $A$ of $[x, 2x)$ is automatically a primitive set: for $a, b \in [x, 2x)$ with $a < b$, the ratio $b/a \in (1, 2)$ is not a positive integer, so $a \nmid b$. Hence the lemma applies in particular to any primitive sub-set of a single dyadic interval.

**Proof.** All terms are positive, so $\sum_{a \in A} 1/(a \log a) \leq \sum_{a=x}^{2x-1} 1/(a \log a)$.

The function $t \mapsto 1/(t \log t)$ is strictly decreasing for $t \geq 3$ (its derivative is negative), so by comparison with the integral:
$$\sum_{a=x}^{2x-1} \frac{1}{a \log a} < \int_{x}^{2x} \frac{dt}{t \log t} = \Big[\log \log t\Big]_{t=x}^{t=2x} = \log\!\left(\frac{\log 2x}{\log x}\right).$$

Since $\log 2x = \log 2 + \log x$:
$$\log\!\left(\frac{\log 2x}{\log x}\right) = \log\!\left(1 + \frac{\log 2}{\log x}\right) < \frac{\log 2}{\log x},$$
using the standard inequality $\log(1 + u) < u$ for $u > 0$.

Therefore $\sum_{a \in A} 1/(a \log a) < \log 2 / \log x$. $\square$

**No ledger fact needed.** The proof uses: (a) positivity and monotone-decrease of $1/(t \log t)$, (b) the antiderivative $\int dt/(t \log t) = \log \log t$, and (c) $\log(1+u) < u$. None of F1, F2, F3 are used.

**Corollary.** For the "fat antichain" $A = \{x, x+1, \ldots, 2x-1\}$:
$$\sum_{a=x}^{2x-1} \frac{1}{a \log a} < \frac{\log 2}{\log x} \to 0 \quad \text{as } x \to \infty.$$

**Role in the proof.** This is the SINGLE-BLOCK CASE of Lemma f1_gap: when $A$ fits entirely within one dyadic interval $[x, 2x)$, the sum is $o(1)$. The full conjecture (Lemma f1_gap) covers $A$ spanning arbitrarily many dyadic intervals; the cross-block case is what remains open.
