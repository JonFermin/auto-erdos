---
id: inter_stratum
status: open
depends_on: [single_stratum_bound]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 2: Inter-stratum interaction under primitivity

**Statement (conjectured).** For any primitive $A \subset [x, \infty)$:
$$\sum_{k \geq 1} S(A_k) \leq \sup_{\text{primitive } B \subset [x, \infty)} S(B)$$
where $A_k = A \cap \{n : \Omega(n) = k\}$ and the supremum is the maximum
over all primitive sets in $[x, \infty)$.

This is a tautology, so the real content is: can we BOUND the supremum?

**The hard sub-problem.** Fix $x$ large. Among all primitive sets $A \subset [x, \infty)$,
which one maximizes $S(A)$?

Erdős conjectured (and partially proved) that the answer is the SET OF PRIMES
$\geq x$. The Erdős–Zhang theorem (F1) gives $S(A) < 1.399 + o(1)$, but not
the sharp "primes maximize" claim.

**Why primitivity creates inter-stratum constraints.**

If $a \in A_1$ (prime $p \geq x$) and $b \in A_2$ (semiprime $pq \geq x$ with
$p | b$), then $a | b$, so we CANNOT have both $a$ and $b$ in $A$ (primitivity).

This constraint is favorable for the proof: including a prime $p$ forces us to
exclude all multiples of $p$ in $A$. The "excluded multiples" have large
contributions to the sum (if they were included), so the loss from excluding
them is bounded.

**Key inequality to prove.** For a prime $p \geq x$:
$$\frac{1}{p \log p} \geq \sum_{\substack{n \geq x \\ p | n \\ \Omega(n) > 1}} \frac{1}{n \log n}$$

If this holds, then including $p$ in $A$ is "worth more" than excluding $p$
and including all its multiples. This would prove the primes are optimal.

**Status.** This inequality likely FAILS for small $p$ (the prime 2 is worth
$1/(2 \ln 2) \approx 0.721$, but the multiples of 2 in $[x, \infty)$ also
contribute significantly). But for large enough $x$, the multiples of $p$
in $[x, 2x]$ are sparse and their contribution is $O(1/(x \log^2 x))$, which
is much less than $1/(p \log p)$.

**Current obstacle.** The precise comparison between $1/(p \log p)$ and the
sum over multiples of $p$ in $[x, \infty)$ requires a careful estimate of
$\sum_{n: p|n, n \geq x} 1/(n \log n) = \sum_{m \geq x/p} 1/(pm \log(pm))$.
This is a well-studied type of sum but making the inequality explicit is work.
