---
id: prime_stratum_obstacle
status: open
depends_on: [stratification]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma 3 — The prime stratum ($k=1$) is the main obstacle

**Statement.** (Informal) For a primitive set $A \subset [x, \infty)$,
the $k=1$ contribution $\sum_{a \in A_1} 1/(a \ln a)$ (sum over prime
elements of $A$) can be large.  Specifically, if $A$ contains all primes
$\geq x$, the sum is $\sum_{p \geq x} 1/(p \ln p)$, which decreases to 0
as $x \to \infty$ but is large for small $x$.

**Numerical evidence** (from Section 2 of the proof draft):
- For $x = 2$: $\sum_{p \geq 2} 1/(p \ln p) > 1.55$ (partial sum to $N=200\,000$,
  still increasing).
- No witness found for $x_\text{floor} \geq 100$ using any tested primitive set.

**The obstacle.** The primitive condition prevents $A_1$ from being large:
if $p \in A_1$ (a prime), then no multiple of $p$ can be in $A$ (since $p | kp$
for $k \geq 2$).  This removes elements $2p, 3p, 4p, \ldots$ from
$A_{k}$ for all $k \geq 2$.  The interaction between the prime stratum and
the higher strata is exactly the **cross-stratum interaction** (Lemma 4).

**Why this stratum is hard:** The $k=1$ case (primes) is where the sum $S_1
= \sum_p 1/(p \ln p)$ is largest (apparently exceeding 1 for the full prime
set from 2).  Bounding the contribution from $A_1$ requires knowing which
primes are "used" by $A$ and then cascading the no-multiples constraint
into higher strata.

**Partial result.** For $x_\text{floor} \geq 3$: numerical evidence (Section 3)
shows no tested primitive set achieves sum $> 1$.  If the analytical bound
$\sum_{p \geq x} 1/(p \ln p) < 1/\ln x$ (a PNT-level estimate not currently
in the ledger) holds, then for $x \geq 3$ the primes-only strategy gives
sum $< 1/\ln 3 \approx 0.91 < 1$, so the prime contribution is not enough
to exceed 1 by itself.

**Current obstacle.** This lemma is open because:
1. The bound $\sum_{p \geq x} 1/(p \ln p) < 1/\ln x$ requires a PNT-level
   estimate not in the given-facts ledger.
2. Even if the prime contribution is bounded, we need to show that the
   cross-stratum interaction (Lemma 4) doesn't push the total over 1.
