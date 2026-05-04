---
id: lemma_005_cross_stratum
status: open
depends_on: [lemma_001_omega_k_is_primitive, lemma_002_stratum_truncation, lemma_004_bounded_omega_tail]
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 5 — The cross-stratum residue (the open core)

**Statement (target).** For every primitive $A \subset [x, \infty)$,
$$
S(A) \;=\; \sum_{a \in A} \frac{1}{a \log a} \;\leq\; 1 + o(1)
\qquad (x \to \infty).
$$

**Status.** *Open.* This is the conjecture itself, restated. The
purpose of this lemma file is to record the proof structure that
*would* derive this from Lemmas 1–4 plus an additional cross-stratum
estimate, and to identify the residual gap.

**Decomposition.** Stratify $A$ by $\Omega$:
$$
A \;=\; \bigsqcup_{k = 1}^{\infty} (A \cap A_k),
\qquad S(A) \;=\; \sum_{k=1}^{\infty} \sum_{a \in A \cap A_k}
\frac{1}{a \log a}.
$$
(Lemma 1 gives that each $A_k$ is primitive, but the disjoint union
$\bigsqcup_k (A \cap A_k)$ inherits primitivity from $A$, not from
each $A_k$ individually — primitivity in $A$ is the input.)

Choose a cutoff $K = K(x) \to \infty$ as $x \to \infty$, and split
$$
S(A) \;=\; \underbrace{\sum_{k \leq K} \sum_{a \in A \cap A_k}
\frac{1}{a \log a}}_{=: \, S_{\text{low}}(A; K)}
\;+\; \underbrace{\sum_{k > K} \sum_{a \in A \cap A_k}
\frac{1}{a \log a}}_{=: \, S_{\text{high}}(A; K)}.
$$

**Bounding $S_{\text{low}}$ (the proved direction).** By Lemma 4 (open
modulo a Landau/Sathe–Selberg admission),
$$
S_{\text{low}}(A; K) \;\leq\; \sum_{k=1}^{K} \sum_{a \in A_k \cap [x, \infty)}
\frac{1}{a \log a} \;\longrightarrow\; 0 \qquad (x \to \infty),
$$
provided $K = K(x)$ does not grow too fast. The crude rate from
Landau is enough to handle, e.g., $K(x) = O(\log \log x)$.

**Bounding $S_{\text{high}}$ (the open direction).** By Lemma 2,
each individual stratum $A_k \cap [x, \infty)$ has
$\sum 1/(a \log a) \leq S_k = 1 - (c+o(1)) k^2/2^k$ for $k \geq k_0$.
The naïve sum
$$
S_{\text{high}}(A; K) \;\leq\; \sum_{k > K} S_k
$$
is **not finite**: $\sum_{k > K} S_k \approx \sum_{k > K} 1$ diverges.
So the per-stratum bound from F3 cannot be summed naïvely across
strata to give the conjecture.

A quantitative form of this looseness is recorded in §3.4 of
`proof_strategy.md`. By F3 there is some $k_1$ at which the o(1)
error is bounded by $c$ in absolute value, giving
$S_k \geq 1 - 2c\,k^2/2^k$ for every $k \geq k_1$. Using
$\sum_{k \geq 1} k^2/2^k = 6$, the partial sum across just two
consecutive strata starting at $k_1$ already exceeds the
conjectured ceiling $1$, and across three strata it exceeds F1's
universal ceiling $e^\gamma \pi/4 \approx 1.399$ — so the
per-stratum decomposition alone is strictly weaker than both
targets, and any closure of this lemma must invoke cross-stratum
primitivity in a non-trivial way.

**The residual gap (open).** What we need is *not* an upper bound
on each stratum's contribution to a generic primitive set; it is an
upper bound on the *combined* contribution of a primitive set across
all $k > K$. The key constraint we have not yet used is that $A$ is
primitive *as a set in $[x, \infty)$* — i.e. for $a \in A \cap A_k$
and $a' \in A \cap A_{k'}$ with $k \neq k'$, we still need
$a \nmid a'$ and $a' \nmid a$. This is a much stronger constraint
than primitivity within each stratum; it is what makes the bound
$\leq 1$ (rather than $\leq \sum_k S_k = \infty$) plausible at all.

The Erdős–Zhang upper bound F1 ($S(A) \leq e^\gamma \pi/4 + o(1)$)
**uses** this cross-stratum primitivity in a non-trivial way; that
proof's slack between $e^\gamma \pi/4 \approx 1.399$ and the
conjectured $1$ is precisely the residual gap that Lemma 5 would
have to close.

**What we have ruled out (partial result).**

- *Single-stratum counterexamples* are ruled out by Lemma 2 for
  $k \geq k_0$; for $k < k_0$ they would need a primitive subset of
  $A_k$ with sum $> 1$, which does not exist (full $S_k < 1$ for
  $k \geq k_0$, and small-$k$ $A_k \cap [x, \infty)$ has a tail going
  to $0$ by Lemma 4 once admitted).
- *Bounded-$\Omega$ counterexamples* (i.e. $A \subseteq \bigcup_{k
  \leq K} A_k$ for some fixed $K$) are ruled out as $x \to \infty$ by
  Lemma 4.
- A small numerical probe at $x_\text{floor} = 100$ found no
  counterexample using all primes in $[100, 10^5]$ (sum $\approx
  0.13$), nor any naïve union of primes plus low-$\Omega$ composites
  at that floor (such unions either fail primitivity or stay below
  $1$). A deeper search at $x_\text{floor} \in \{1000, 10000\}$
  through the rigorous helper
  `library.primitive_set_witness._rigorous_sum_lower_bound` extends
  the negative result: across primes-only baselines and primes-plus-
  disjoint-small-prime-semiprime unions (constructions $A$, $C$, $D$
  of §2.5), every probed primitive set yields a rigorous lower bound
  on $\sum 1/(a \log a)$ that is an order of magnitude below the
  threshold $1$.

**Where the proof is open.** A primitive $A \subset [x, \infty)$
that draws elements from arbitrarily-many strata, none of them
dominant, may in principle have $S(A) > 1$ for finite $x$. F1
established $S(A) < e^\gamma \pi/4 + o(1)$; the conjecture asserts
the tighter $S(A) < 1 + o(1)$. The gap is the residue not closed by
Lemmas 1–4. We do not close it here.

## Update — connection to §4 and §6 (round 18 v2)

Strategy file Sections 4 and 6 add structure to the cross-stratum
residue:

**§4**: applying F3 to $A_k$ for $k \to \infty$ shows
$\sup_{A \text{ primitive}, A \subset [x, \infty)} S(A) \ge 1$ in the
limit. The witness is $A_k$ for $k$ large; it is primitive (Lemma 1)
and contained in $[x, \infty)$ (smallest element $2^k$). So the
single-stratum case alone matches the conjecture's ceiling from
below.

**§6**: summing F3's per-stratum deficits via the elementary identity
$\sum k^2/2^k = 6$ gives the closed-form $6c$ at leading order. Strata
are not primitive in their disjoint union, so this is not a bound on
$\sup S(A)$, but it is a clean F3-derived constant available for
future analytical work.

**Effect on Lemma 5's framing**: the residue's open content is the
cross-stratum mechanism that ties §4's lower bound to F1's upper
bound. The lemma is *not* about achieving 1 (single strata already
do that asymptotically), but about preventing *excess* above 1 via
cross-stratum primitivity exclusion. We have not closed it; the
residue remains open.
