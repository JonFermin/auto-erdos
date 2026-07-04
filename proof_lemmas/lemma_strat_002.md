---
id: strat_002
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 2
---

# Lemma strat_002: F3 asymptotics and the k=1 anomaly

## Statement

For $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$, the full weight
$f_k = \sum_{a \in A_k} 1/(a \log a)$ satisfies:

(a) **For $k \geq 2$** (numerical evidence): $f_k < 1$. Specifically,
    $f_2 \approx 0.81$, $f_3 \approx 0.44$, $f_4 \approx 0.21$
    (truncated sums to 50,000; full sums likely modestly larger but
    still $< 1$ for $k \geq 2$).

(b) **For $k = 1$ (primes)**: $f_1 = \sum_p 1/(p \log p) \approx 1.6366$.
    This is the **maximum** weight over all primitive sets (conjectured by
    Erdős; proven by Lichtman–Pomerance 2019 — but this citation is not
    in the given-facts ledger so cannot be used here).

(c) **F3's formula**: $f_k = 1 - (c + o(1)) k^2 / 2^k$ with $c \approx
    0.0656$. This is given as fact F3. Numerically, it matches well for
    large $k$ but is far off for $k = 1$ (F3 predicts $\approx 0.967$;
    actual $\approx 1.637$). The $o(1)$ correction at $k=1$ is $\approx
    0.670$, not small.

## Current obstacle

F3 as a *uniform* bound for all $k \geq 1$ cannot be used to show
$f_k < 1$ for every $k$, since $f_1 \approx 1.637 > 1$.

Two possible resolutions:
1. F3 is a large-$k$ asymptotic. For small $k$ (especially $k=1$), a
   separate argument is needed. For the proof, we might treat $k=1$
   separately: any prime $p \geq x$ contributes $1/(p \log p)$, and the
   sum over primes in $[x, \infty)$ is $\sim 1/\log x \to 0$.
2. F3 involves a different normalization (e.g., tail sums over $[x, \infty)$
   normalized by $\log x$), in which case $k=1$ IS less than 1 in the
   normalized sense.

## Status note

This lemma is **open** pending resolution of the F3 interpretation. The
central goal of the proof shifts to: rather than bounding each $f_k$
uniformly below 1, show that a primitive set can use at most a vanishing
fraction of each stratum's weight.
