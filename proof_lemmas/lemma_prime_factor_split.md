---
id: prime_factor_split
status: open
depends_on: [prime_tail_vanish, large_floor_vanish]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma: prime-factor split (Q12 gap statement)

**Statement (goal)**: For any primitive set $A \subset [x, \infty)$, writing
$A = A_{\mathrm{sm}} \cup A_{\mathrm{lg}}$ (partition by whether $p_{\min}(a) < x$ or $\geq x$),
show:
$$\sum_{a \in A} \frac{1}{a \ln a}
  = \sum_{a \in A_{\mathrm{sm}}} \frac{1}{a \ln a}
  + \sum_{a \in A_{\mathrm{lg}}} \frac{1}{a \ln a}
  \leq 1 + o(1).$$

**Status**: OPEN. This is equivalent to the original conjecture, rephrased using
the prime-factor split. The decomposition identifies which component is hard.

**What Section 5 establishes**:

1. **Structural non-divisibility**: No $a \in A_{\mathrm{sm}}$ divides any $b \in A_{\mathrm{lg}}$
   (Section 5, pure logic). Only the direction $b \nmid a$ ($b \in A_{\mathrm{lg}}$,
   $a \in A_{\mathrm{sm}}$) is enforced by primitivity.

2. **Prime stratum of $A_{\mathrm{lg}}$** (Lemma `prime_tail_vanish`):
   $$\sum_{\substack{a \in A_{\mathrm{lg}} \\ \Omega(a)=1}} \frac{1}{a \ln a}
     \leq T_1(x) \to 0.$$

3. **Each fixed $\Omega$-stratum of $A_{\mathrm{lg}}$** (Lemma `large_floor_vanish`):
   For each fixed $k \geq 2$, elements of $A_{\mathrm{lg}}$ with $\Omega(a) = k$
   satisfy $a \geq x^k$, giving:
   $$\sum_{\substack{a \in A_{\mathrm{lg}} \\ \Omega(a)=k}} \frac{1}{a \ln a}
     \leq T_k(x^k) \to 0.$$

**The gap**:

To conclude $\sum_{a \in A_{\mathrm{lg}}} 1/(a \ln a) = o(1)$ by summing over all $k$,
one needs $\sum_{k \geq 1} T_k(x^k) \to 0$. The obstacles are:

- Each $T_k(x^k) \to 0$ for fixed $k$, but the strata active near $k \sim \log_2 x$
  have $T_k(x^k)$ potentially close to $T_k(2) = 1 - (c+o(1))k^2/2^k \to 1$
  (by F3 with large $k$).
- $\sum_k T_k(2)$ diverges (a sum of terms approaching 1 from below).
- F1 applied to $A_{\mathrm{lg}}$ gives $\sum_{a \in A_{\mathrm{lg}}} 1/(a \ln a) < e^\gamma \pi/4 + o(1)$,
  a nontrivial bound but not $\leq 1 + o(1)$.

**Subproblem**: Even if $\sum_{a \in A_{\mathrm{lg}}} 1/(a \ln a) = o(1)$ could be proved,
one would still need $\sum_{a \in A_{\mathrm{sm}}} 1/(a \ln a) \leq 1 + o(1)$ for
primitive $A_{\mathrm{sm}} \subset [x,\infty)$ with $p_{\min}(a) < x$. That is an
independent open problem of the same difficulty.

**Current obstacle**: A global argument using the primitivity of $A_{\mathrm{lg}}$ as a whole
is needed to control the sum of the $k$-stratum contributions across all $k$.
The per-stratum approach (via Lemma `large_floor_vanish`) is insufficient.
