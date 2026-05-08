---
id: primes_extremal
status: open
depends_on: [single_stratum_bound, inter_stratum]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 3: Primes are the extremal primitive set (the main open lemma)

**Statement.** For any $x \geq 2$ and any primitive $A \subset [x, \infty)$:
$$S(A) := \sum_{a \in A} \frac{1}{a \log a} \leq \sum_{p \geq x} \frac{1}{p \log p} + o(1),$$
where the $o(1)$ term tends to $0$ as $x \to \infty$.

**Difficulty.** HARD — this is essentially the full Erdős primitive-set
conjecture in the $[x, \infty)$ form.

**What's known.**

- Erdős-Zhang (F1): $S(A) < e^\gamma \pi/4 + o(1) \approx 1.399 + o(1)$ for
  any primitive $A \subseteq \mathbb{N}$. This is a WEAKER bound than what
  Lemma 3 claims.

- The prime tail sum $\sum_{p \geq x} 1/(p \log p) \to 0$ as $x \to \infty$
  (established numerically in Section 3; formal proof via PNT + partial summation
  is routine). So Lemma 3, if true, would imply $S(A) < 1$ for all large enough
  $x$, and hence $S(A) < 1 + o(1)$.

**The exchange argument.**

A standard approach: consider any primitive $A$. Suppose $A$ contains a
composite $a = pq$ with $p < q$ primes. Then $p \notin A$ (primitivity).
We can try to "swap" $a$ for $p$:

- Remove $a$ from $A$: lose $\frac{1}{pq \log(pq)}$.
- Add $p$ to $A$ (if $p \geq x$): gain $\frac{1}{p \log p}$.
- But we must also remove any $b \in A$ with $p | b$.

The gain from adding $p$ is $1/(p \log p)$. The loss from removing $a = pq$ is
$1/(pq \log(pq))$. Since $pq > p$, the gain exceeds the loss for this single
swap (ignoring the removal of other multiples of $p$). This suggests the
primes should be preferred.

However, removing all multiples of $p$ from $A$ might cost more than the gain
from adding $p$. The net trade-off requires careful accounting.

**Key estimate needed.**

Show: for $p \geq x$ (large),
$$\frac{1}{p \log p} \geq \sum_{\substack{a \in A \\ p \mid a}} \frac{1}{a \log a}.$$

This is plausible for large $x$ since:
1. Elements of $A$ divisible by $p$ have $a \geq px$ (since $a = p \cdot m$ with $m \geq x/p$... wait, actually $a \geq x$ and $p | a$, so $a \geq p$. But $a \geq x$ is the constraint, not $a \geq px$).
2. Still: $\sum_{a \geq x, p|a} 1/(a \log a) = \sum_{m \geq \lceil x/p \rceil} 1/(pm \log(pm))$. For $m \geq 2$, $pm \geq 2p$, and $1/(pm \log(pm)) \leq 1/(pm \log p) < 1/(p^2 \log p)$. The sum over all multiples is $\sim 1/(p^2 \log p)$ (geometric), which is $o(1/(p \log p))$. ✓

So for large $p$: the gain from adding $p$ exceeds the loss from removing
all its multiples. The problem is the SMALL primes (near $x$).

**Current obstacle.** Making the exchange argument uniform in $p$ and summing
over all swaps requires careful analysis. The argument breaks for primes
$p \approx x^{1/2}$ where the multiples $pm$ can be very close to $x$. The
key technical gap is controlling the near-threshold regime.

**Alternative approach: Analytic / multiplicative number theory.**

The Zhang 1993 proof uses a clever estimate involving $\sum_p 1/(p \log^2 p)$.
A more refined version (e.g., using the Erdős-Kac theorem or the Omega
distribution of prime factors) might yield the full Lemma 3. This is the
main open problem.
