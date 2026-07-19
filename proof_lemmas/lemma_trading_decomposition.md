---
id: trading_decomposition
status: abandoned
depends_on: [stratum_sub_bound, large_floor_vanish, dyadic_interval_bound]
discharged_by_round: null
introduced_at_round: 3
---

# Lemma: Trading decomposition at $x^e$

**Goal**: Prove $\sum_{a \in A} 1/(a \log a) \leq 1 + o(1)$ for
primitive $A \subset [x, \infty)$ by splitting at $x^e$ into
$A_1 = A \cap [x, x^e)$ and $A_2 = A \cap [x^e, \infty)$.

---

## Part 1 (proved): $S_1 \leq 1 + O(1/x \log x)$

**Proof**:
$$S_1 = \sum_{a \in A_1} \frac{1}{a \log a}
  \leq \sum_{n=x}^{\lfloor x^e \rfloor - 1} \frac{1}{n \log n}
  \leq \int_x^{x^e} \frac{dt}{t \log t} + \frac{1}{x \log x}.$$

The integral is exactly:
$$\int_x^{x^e} \frac{dt}{t \log t} = \log \log(x^e) - \log \log x
  = \log(e \log x) - \log \log x = \log e = 1.$$

So $S_1 \leq 1 + O(1/(x \log x))$. The bound is TIGHT: it cannot be
improved to $1 - \epsilon$ without using primitivity, because the full
(non-primitive) set $\{n : x \leq n < x^e\}$ achieves $S_1 \to 1$.

**Optimality note**: The pivot $x^e$ is forced by the computation above.
The integral $\int_x^{x^M} dt/(t \log t) = \log M$, which equals 1 at $M = e$.
Any other pivot $M \neq e$ gives a bound $\neq 1$.

---

## Part 2 (open): $S_2 = o(1)$ (needed to close)

**What we need**: For the trading decomposition to prove the conjecture,
we need $S_2 \leq o(1)$ (so that $S_1 + S_2 \leq 1 + o(1)$).

**Why naive bounds fail**:

1. Without any constraint: $\sum_{n \geq x^e} 1/(n \log n) = \infty$ (divergent
   harmonic-type series). Primitivity is essential.

2. With only the "not divisible by $A_1$" constraint:
   The "unblocked" density is $\prod_{a \in A_1}(1 - 1/a) \approx e^{-C}$
   (where $C = \sum_{a \in A_1} 1/a$). But $e^{-C} \cdot \sum_{n \geq x^e} 1/(n \log n)$
   still diverges. The blocking density does not give a finite bound.

3. Recursive application of the conjecture: $S_2 \leq 1 + o(1)$ (by conjecture
   for parameter $x^e$). Combined with $S_1 \leq 1$: gives $\leq 2 + o(1)$,
   worse than F1.

**The essential constraint not used**: $A_2$ is not just any primitive set in
$[x^e, \infty)$. It is additionally constrained to avoid all multiples of
elements of $A_1$. Furthermore, $A_1 \cup A_2$ together must be primitive —
there are NO cross-divisibilities in either direction.

The missing bound: Translate the cross-divisibility constraint into a
quantitative estimate on $S_2$ in terms of $S_1$.

---

## Potential routes to Part 2

### Route A: Near-saturation implies density

**Claim** (unproved): If $S_1 \geq 1 - \delta$ for some $\delta > 0$, then
$A_1$ is "dense" enough in $[x, x^e)$ to block nearly all elements of
$[x^e, \infty)$ in the $1/(n \log n)$ sense, forcing $S_2 = O(\delta)$.

**Obstacle**: Density of $A_1$ in $[x, x^e)$ (in the $1/(n \log n)$ metric)
does not imply density in the blocking sense (multiples in $[x^e, \infty)$).
An $A_1$ achieving $S_1 \approx 1$ could consist of very few large elements
near $x^e$ (where $1/(a \log a)$ is small) which block very few multiples
in $[x^e, \infty)$.

### Route B: Maximal primitive sets

**Claim** (unproved): The maximal primitive sets in $[x, \infty)$
(by inclusion, not by sum) have a special structure that prevents
$S_1 + S_2 > 1 + o(1)$.

**Obstacle**: Maximal primitive sets can have varied structure; it's not
clear their maximality imposes a useful sum constraint.

### Route C: Induction on the pivot

**Claim** (unproved): The bound $S_1 + S_2 \leq 1 + o(1)$ can be proved
by iterating the pivot construction: split at $x^e$, then $x^{e^2}$, etc.

**Obstacle**: Each level of the recursion applies the same bound, giving
$S \leq k$ after $k$ levels, not $\leq 1$.

---

## What a proof would look like

A proof of Part 2 (and hence of the full conjecture) would need a function
$f: \mathbb{R}_{\geq 0} \to \mathbb{R}_{\geq 0}$ with:

1. $f(t) = o(1)$ as $t \to 1^-$ (or $f(1) = 0$).
2. $S_2 \leq f(S_1)$ for ALL primitive sets $A \subset [x, \infty)$.
3. $S_1 + f(S_1) \leq 1 + o(1)$ as $x \to \infty$.

Properties 1 and 3 together would give the conjecture. Property 2 is the
key estimate that must come from the cross-structure of primitivity.

Such a function $f$ is not currently known or proved.

---

## Status

**Status**: open. Part 1 is proved (a trivial bound from the integral).
Part 2 is open and is the essential gap. The trading decomposition is a
clean reformulation of the conjecture but does not constitute progress
beyond what was already known.

The approach is recorded as a "dead end" in the sense that it does not
yield a proof without new ideas for Part 2.

---

**Abandoned 2026-07-18 (session s_0718-205004-c44a).** The parent claim
`primitive_set_erdos` (Erdős #1196) was proved in the literature in May
2026 (arXiv:2605.00301) and the spec was reclassified as a rediscovery
benchmark in the 2026-07-11 audit. This attempt is concluded; the lemma
is retained as audit trail. Nothing here is wrong — it is simply moot as
research (the o(1) gap it chased is closed by the published proof).
