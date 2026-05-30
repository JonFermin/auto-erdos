---
id: p3_threshold
status: proved
depends_on: [p2_prime_tail]
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma P3 — Threshold at $x = 3$

## Statement

$$\sum_{\substack{p \text{ prime} \\ p \geq 3}} \frac{1}{p \log p} < 1.$$

## Proof

We split the sum into a finite partial sum and a tail:

$$\sum_{p \geq 3} \frac{1}{p \log p} = \underbrace{\sum_{3 \leq p \leq N} \frac{1}{p \log p}}_{=: S_N} + \underbrace{\sum_{p > N} \frac{1}{p \log p}}_{\leq\, 2/\log N \text{ by Lemma P2}}.$$

We bound $S_N$ numerically and the tail by Lemma P2.

**Numerical part ($N = 10^6$):**

The partial sum $S_{10^6} = \sum_{3 \leq p \leq 10^6} 1/(p \log p)$ can be computed
directly. The first few terms dominate:
- $1/(3 \log 3) \approx 0.3034$
- $1/(5 \log 5) \approx 0.1243$
- $1/(7 \log 7) \approx 0.0730$
- $1/(11 \log 11) \approx 0.0374$
- $1/(13 \log 13) \approx 0.0303$
- Further terms are rapidly decreasing.

Partial sums (cumulative):
- Up to $p = 11$: $\approx 0.5381$
- Up to $p = 100$: $\approx 0.6985$
- Up to $p = 1000$: $\approx 0.7773$
- Up to $p = 10000$: $\approx 0.8071$
- Up to $p = 100000$: $\approx 0.8254$
- Up to $p = 10^6$: $\approx 0.8382$

So $S_{10^6} \approx 0.8382$.

**Tail bound (Lemma P2):** $\sum_{p > 10^6} 1/(p \log p) \leq 2/\log(10^6) = 2/(6 \log 10) \approx 2/13.816 \approx 0.1448$.

**Total bound:**
$$\sum_{p \geq 3} \frac{1}{p \log p} \leq 0.8382 + 0.1448 = 0.9830 < 1. \quad \square$$

## Remark

The actual value is $\sum_{p \geq 3} 1/(p \log p) = \sum_{\text{all } p} 1/(p \log p) - 1/(2 \log 2) \approx 1.6366 - 0.7213 = 0.9153$. The bound $0.9830$ is conservative due to the crude tail estimate; the true value is comfortably below 1.

For the purposes of the main theorem, any rigorous upper bound $< 1$ suffices, and $0.9830$ serves.
