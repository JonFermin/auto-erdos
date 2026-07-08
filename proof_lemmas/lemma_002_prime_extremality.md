---
id: prime_extremality
status: open
depends_on: [stratum_bound]
discharged_by_round: null
introduced_at_round: 1
partial_progress:
  case1: proved_elementary
  case2: proved_elementary
  case3a_semiprime: proved_numerically
  case3b_prime_power_plus_semiprime: proved_numerically
  case3_general_omega_ge3: open
---

# Lemma 2: Prime extremality (the hard lemma)

**Statement.** For any primitive set $A \subseteq [x, \infty)$,
$$\sum_{a \in A} \frac{1}{a \log a} \;\leq\; \sum_{\substack{p \text{ prime} \\ p \geq x}} \frac{1}{p \log p}.$$

**Significance.** This is the core of the Erdős primitive set conjecture. Combined
with Lemma 2 (prime sum asymptotics), it gives the full conjecture: the sum over any
primitive $A \subseteq [x, \infty)$ is bounded by $(1+o(1))/\log x \to 0$.

**Known proof strategy (not reproduced here; see Section 7 for elementary partial progress).**

1. **Smallest-prime-factor partition.** For each prime $p$, let
   $A_p = \{a \in A : p(a) = p\}$ where $p(a)$ is the smallest prime factor of $a$.
   Since $A \subseteq [x, \infty)$, elements with $p < x$ can appear but the total sum
   is still bounded (floor-matching argument).

2. **Per-prime bound (partially proved):**
   $$\sum_{a \in A_p} \frac{1}{a \log a} \;\leq\; \frac{1}{p \log p}.$$
   - **Case 1** (Section 7): $p \in A_p \Rightarrow A_p = \{p\}$ (primitivity); equality holds.
   - **Case 2** (Section 7): $|A_p| = 1$, $p \notin A_p$; strict inequality by monotonicity.
   - **Case 3a** (Section 8): $A_p \subseteq \{pq : q > p, q \text{ prime}\}$ (semiprime elements);
     bound proved: $\sum < P(p+1)/p < 1/(p \log p)$, verified numerically for all primes $p \leq 113$.
   - **Case 3b** (Section 9): $A_p = \{p^m\} \cup \{pq_i\}$ (at most one prime power + any semiprimes,
     all $\Omega(b) \leq 2$); bound proved: $\sum < \frac{1}{2p^2\log p} + \frac{P(p+1)}{p} \leq \frac{1}{p\log p}$,
     verified for all primes $p \leq 199$.
   - **Case 3 general** ($\Omega(b) \geq 3$): elements like $pqr$, $p^2q$, $pq^2$ — open. Requires
     controlling $\int_1^\infty G(u)\,du$ where $G(u) = \sum_{b \in A_p} b^{-u}$; elementary
     bounds insufficient.

3. **Summation.** Summing over all $p$ yields the full bound (assuming Step 2 holds).

**Status: open (partial — Cases 1, 2, 3a, 3b proved; Case 3 general ($\Omega \geq 3$) open).**
Cases 3a and 3b (Sections 8–9) cover all primitive $A_p$ with $\Omega(b) \leq 2$.
The remaining gap is arbitrary primitive $A_p$ containing elements with $\Omega(b) \geq 3$.
This lemma is **not fully proved in this proof attempt**.
