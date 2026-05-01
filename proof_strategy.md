# Proof attempt — `primitive_set_erdos`

This is the agent-editable proof draft for the Track 2 loop. Its content
is hashed for round-dedup; pure whitespace / comment edits do not count
as a real round. Lemmas live in `proof_lemmas/`.

## Section 1 — Setup

### 1.1 Statement

Fix $x \ge 2$. A set $A \subseteq \mathbb{N}$ is *primitive* if no
distinct elements of $A$ stand in a divisor relation: $a, b \in A$ and
$a \ne b$ imply $a \nmid b$. Define
\[
S(A) \;=\; \sum_{a \in A} \frac{1}{a \log a}.
\]

**Conjecture (target).** For any primitive $A \subset [x, \infty)$,
\[
S(A) \;\le\; 1 + o(1) \qquad \text{as } x \to \infty,
\]
where the $o(1)$ depends only on $x$.

The set $\mathcal{P}$ of primes from $2$ is primitive and
$S(\mathcal{P}) \approx 1.6366$, but $\mathcal{P} \not\subset [x,
\infty)$ for $x > 2$. The conjecture concerns the *truncated* family
$\mathcal{F}(x) = \{A \text{ primitive} : A \subset [x, \infty)\}$,
where the small-element contributions of $\mathcal{P}$ have been
excluded.

### 1.2 Given facts (citations only — no rederivation in this draft)

The harness ships three facts in `proofs/primitive_set_erdos.json`. Each
sign reading below is restated explicitly because misreading the sign
of F2 is the canonical failure mode.

**F1 (Erdős–Zhang upper bound).** For any primitive $A \subseteq
\mathbb{N}$,
\[
S(A) \;<\; e^{\gamma} \tfrac{\pi}{4} \;+\; o(1) \;\approx\; 1.399 +
o(1).
\]
Sign reading: this is an *upper* bound (strict inequality, fixed $A$,
$o(1)$ as the truncation point grows). The constant $1.399$ is
positive; the bound is consistent with the conjecture's tighter $1$, it
just doesn't attain it. Citing F1 to show $S(A) > 1$ inverts the
inequality.

**F2 ($\Omega = k$ stratum, unsigned correction).** Let
$A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$, the integers with exactly
$k$ prime factors counted with multiplicity. Then
\[
S(A_k) \;\ge\; 1 \;+\; O\!\bigl(k^{-1/2 + o(1)}\bigr).
\]
Sign reading: the $O(\cdot)$ term is *unsigned* — it could be positive,
negative, or zero, with absolute value bounded by $k^{-1/2 + o(1)}$.
The bound reads "$S(A_k)$ is at least $1$ minus something controlled in
absolute value by $k^{-1/2+o(1)}$", **not** "$S(A_k)$ is at least $1$
plus a positive quantity." Inferring $S(A_k) > 1$ from F2 alone is a
sign error.

**F3 ($\Omega = k$ stratum, sharpened to one-sided).** For the same
$A_k$,
\[
S(A_k) \;=\; 1 \;-\; (c + o(1)) \frac{k^2}{2^k}, \qquad
c \approx 0.0656 > 0.
\]
Sign reading: the leading correction is *negative* (since $c > 0$), so
$S(A_k) < 1$ for every $k \ge 1$, and $S(A_k) \uparrow 1$ from below as
$k \to \infty$. F3 sharpens F2: the unsigned $O(\cdot)$ in F2 is in fact
dominated by $-c k^2/2^k + o(k^2/2^k)$, lying strictly below $1$ for
every finite $k$.

The pair (F2, F3) is consistent. F2 says "$S(A_k)$ is within
$k^{-1/2+o(1)}$ of $1$"; F3 says "in fact it is exactly
$\Theta(k^2/2^k)$ below $1$." A direct counterexample reading would
require the $O(\cdot)$ in F2 to be positive, which F3 rules out for the
canonical extremal family $A_k$.

### 1.3 Witness contract

A claim against the target bound can be admitted into the loop only by
exhibiting a primitive $A^\star \subset [x_\star, \infty)$ together
with a rigorously verified lower bound on $S(A^\star)$ exceeding $1$.
The harness implements this as a `<!-- WITNESS -->` block in this file:

```
<!-- WITNESS
{
  "x_floor": <int>,
  "elements": [<int>, ...],
  "claimed_sum_lower_bound": <float>
}
WITNESS -->
```

`library.primitive_set_witness.verify_witness` checks:

1. each $a$ in `elements` is an integer with $a \ge x_\text{floor}$;
2. the elements are pairwise non-divisible;
3. it computes a rigorous lower bound on
   $\sum_{a \in \text{elements}} 1/(a \log a)$ via stdlib `decimal`
   arithmetic with a ULP-bumped `math.log`, accurate to roughly $50$
   decimal digits;
4. it accepts (`is_valid = True`) iff the rigorous lower bound exceeds
   `witness_threshold = 1.0`.

No `WITNESS` block ⇒ `witness_valid = 0`, and any narrative chain that
ends in a counterexample claim without a verified witness is forced to
`verdict_hint = blocked` by the resolution-string defense-in-depth in
`proof_prepare._compute_verdict_hint`.

### 1.4 The o(1) caveat

The conjecture's bound is $1 + o(1)$ as $x_\star \to \infty$. A finite
witness at some $x_\star$ that produces $S(A^\star) > 1$ is
*suggestive* but not conclusive: the implicit $o(1)$ at that $x_\star$
may itself be $\ge S(A^\star) - 1$. A counterexample resolution at
finite $x_\star$ needs both

- (a) a witness with rigorous lower bound exceeding $1$, **and**
- (b) an analytical estimate that the implicit $o(1)$ at $x_\star$ is
  small enough to leave room (i.e. $o(1) < S(A^\star) - 1 - \epsilon$
  for some explicit $\epsilon > 0$).

The harness verifier handles (a). (b) is left to the proof body and a
human reviewer.

### 1.5 What is to be proved

To establish the conjecture, the loop must produce one of:

- a **proof body** demonstrating, for every primitive $A \subset [x,
  \infty)$, that $S(A) \le 1 + o(1)$. F1 already implies this with the
  weaker bound $1.399 + o(1)$; the conjecture asks to sharpen the
  constant to $1$.
- a **partial-result body** isolating an explicit subclass of primitive
  sets for which the bound holds, plus a clear statement of the
  remaining gap. The loop admits this as a `keep_progress` round once
  three consecutive rounds stabilise on the same content hash with
  clean verdict and no live open qids.
- (the loop also admits) a **counterexample witness** as above. Given
  F1 and F3, a witness exceeding $1.399$ would falsify F1, and any
  witness exceeding $1$ requires the analytical (b) above.

(End of Section 1. Sections 2+ are populated by subsequent rounds;
see `proof_open_questions.jsonl` for the worklist.)
