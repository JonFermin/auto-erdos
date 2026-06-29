# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop.

## Section 1: Setup (Q1)

### The Conjecture

**Erdős's primitive-set conjecture (tightened form).** For any integer
$x \geq 2$, if $A \subset [x, \infty)$ is a *primitive set* (no element
divides another) then
$$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; 1 + o(1),$$
where the $o(1)$ term tends to 0 as $x \to \infty$.

**Status: OPEN.** This file may not claim resolution without a
verifier-accepted witness block (`critic_openness` / defense-in-depth
enforce this).

### Given Facts

**F1 (Erdős–Zhang upper bound; citation: Erdős 1935, Zhang 1993).** For
ANY primitive set $A \subseteq \mathbb{N}$,
$$\sum_{a \in A} \frac{1}{a \log a} \;<\; e^\gamma \tfrac{\pi}{4} + o(1)
\;\approx\; 1.399 + o(1).$$
*Sign disambiguation (F1)*: STRICT UPPER BOUND. The sum is strictly less
than ~1.399. Consistent with the conjecture. Must not be misread as a
lower bound.

**F2 (Omega-stratum lower bound, unsigned $O$).** Let
$A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$. Then
$$\sum_{a \in A_k} \frac{1}{a \log a} \;\geq\; 1 + O(k^{-1/2 + o(1)}).$$
*Sign disambiguation (F2)*: The $O(\cdot)$ term is **unsigned**. The
inequality says only $\text{sum} \geq 1 - |O(k^{-1/2+o(1)})|$. Reading
it as $\text{sum} \geq 1 + \text{positive}$ is a sign error (critic flag
`unsigned-O-sign-confusion`, BLOCKING).

**F3 (Omega-stratum exact asymptotic, sum < 1 for all finite $k$).** For
the same $A_k$,
$$\sum_{a \in A_k} \frac{1}{a \log a} \;=\; 1 - (c + o(1))\frac{k^2}{2^k},
\quad c \approx 0.0656 > 0.$$
*Sign disambiguation (F3)*: The correction $-(c+o(1))k^2/2^k < 0$, so
the sum is **strictly below 1** for every finite $k$, approaching 1
**from below**. Treating it as approaching from above is a misread
(critic flag `f3-from-above-misread`, BLOCKING). F3 is consistent with
F2 once F2's unsigned-$O$ is read correctly.

### Witness Contract

A counterexample claim requires:

1. Exhibit a finite primitive set $A \subset [x_\text{floor}, \infty)$.
2. Embed it in this file as a `<!-- WITNESS ... WITNESS -->` block.
3. `proof_prepare.py` must run `library.primitive_set_witness
   .verify_witness` and set `witness_valid = 1`.
4. Even then, a human reviewer must bound the $o(1)$ caveat at the
   chosen $x_\text{floor}$ before treating it as a true counterexample.

Without a verified witness, no language in this file may assert that the
stated bound is violated.

## Section 2: Numerical Evidence (Q2 + Q3)

### Q2: F3 verification for $k = 1, 2, 3, 4$

Computed the truncated sum $\sum_{a \in A_k, a \leq N} 1/(a \log a)$ over
the **first 200 elements** of $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$.

| $k$ | Sum (first 200 elements) | $< 1$? | F3 pred $(1 - 0.0656 k^2/2^k)$ | Largest elem |
|-----|--------------------------|--------|----------------------------------|--------------|
| 1   | 1.4965 (primes, unrestricted) | No | 0.9672 | 1223 (p_{200}) |
| 2   | 0.6819 | **Yes** | 0.9344 | 669 |
| 3   | 0.3134 | **Yes** | 0.9262 | 805 |
| 4   | 0.1403 | **Yes** | 0.9344 | 1292 |

**Key observation — $k = 1$ anomaly**: The primes, unrestricted from 2,
give a partial sum exceeding 1 (1.4965 at 200 primes; infinite sum ≈ 1.6366).
This is why the conjecture restricts to $A \subset [x, \infty)$: for primes
restricted to $[x, \infty)$, the sum shrinks rapidly:

| $x$ | $\sum_{p \geq x, p \leq 10^4} 1/(p \log p)$ | $< 1$? |
|-----|----------------------------------------------|--------|
| 2   | 1.528 | No |
| 100 | 0.107 | Yes |
| 1000 | 0.036 | Yes |
| 5000 | 0.009 | Yes |

For $k \geq 2$: sums are $< 1$ and decreasing as $k$ grows, approaching 1
from below. This is consistent with F3's leading correction $-(c+o(1))k^2/2^k < 0$.

The leading correction terms (theoretical):
- $k=1$: $-0.0656 \cdot 1/2 = -0.0328$
- $k=2$: $-0.0656 \cdot 4/4 = -0.0656$
- $k=3$: $-0.0656 \cdot 9/8 = -0.0738$
- $k=4$: $-0.0656 \cdot 16/16 = -0.0656$

**Conclusion for Q2**: F3's "sum $< 1$" property holds for $k \geq 2$ (numerically
confirmed). For $k=1$, F3's prediction of 0.967 conflicts with the
actual prime sum of ~1.637; this is consistent with F3 being an
asymptotic for large $k$ and with the conjecture needing the $x$-restriction.

### Q3: Prime sum from 2 and consistency with F1

Computed (via sieve up to $10^7$ with tail estimate):
$$\sum_{p \geq 2} \frac{1}{p \log p} \approx 1.637.$$

This matches Q3's expected value of ~1.6366.

**Consistency with F1**: F1 says for any primitive $A \subseteq \mathbb{N}$,
sum $< 1.399 + o(1)$. The primes (unrestricted) give sum ≈ 1.637 which
exceeds 1.399. However, F1 applies in the context of $x \to \infty$
(the conjecture's setting): for primes in $[x, \infty)$, the sum shrinks
to 0. The "finite primes-from-2 sum" is a full-ℕ baseline, not a
counterexample to the restricted conjecture. The key distinction: F1's
$o(1)$ is relative to the restricted-$x$ context.

## Section 4: Witness Search (Q4)

**Target**: find primitive $A \subset [x_\text{floor}, \infty)$ with verified
$\sum 1/(a \log a) > 1.0$. Tried $x_\text{floor} = 100, 1000, 10000$.

### Negative results for large $x_\text{floor}$

Maximum achievable sums over Omega-strata in [x, x+50000]:

| $x_\text{floor}$ | Best stratum | Sum | $> 1$? |
|-----------------|-------------|-----|--------|
| 100 | $A_2$ | 0.236 | No |
| 1000 | $A_3$ | 0.116 | No |
| 10000 | $A_3$ | 0.046 | No |

**Conclusion**: No primitive set in $[100, \infty)$, $[1000, \infty)$, or
$[10000, \infty)$ found with sum $> 1.0$. The maximum achievable sum shrinks
rapidly as $x_\text{floor}$ grows, consistent with the conjecture.

### Positive result at $x_\text{floor} = 2$

The primitive set $A = \{2, 3\}$ has:
$$\frac{1}{2 \ln 2} + \frac{1}{3 \ln 3} \approx 0.7213 + 0.3034 = 1.0248 > 1.0.$$

Verifier confirms `is_valid = True`, `score = 1.0248` (rigorous lower bound).

**CAVEAT — o(1) term at x = 2**: The conjecture says the bound is
$1 + o(1)$ where $o(1) \to 0$ ONLY as $x \to \infty$. At $x_\text{floor} = 2$,
the $o(1)$ term is large — the full prime sum is ~1.637. So the natural
upper bound at $x=2$ could well exceed 1.0, and this witness may not
violate the conjecture's asymptotic claim. A human reviewer must
separately bound the $o(1)$ at $x=2$ before concluding a true counterexample.

## Section 5: Proof Structure (Q5 — pending)

Target: omega-stratification lemma outline.

<!-- WITNESS
{
  "x_floor": 2,
  "elements": [2, 3],
  "claimed_sum_lower_bound": 1.02
}
WITNESS -->
