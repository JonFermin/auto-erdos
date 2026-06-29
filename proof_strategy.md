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

## Section 2: Numerical Evidence (Q2 — pending)

Target: verify F3 numerically for $k = 1, 2, 3, 4$.

## Section 3: Prime-sum Check (Q3 — pending)

Target: compute the truncated prime sum and confirm consistency with F1.

## Section 4: Proof Structure (Q5 — pending)

Target: omega-stratification lemma outline.
