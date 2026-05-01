---
id: cross_stratum_primitivity
status: open
depends_on: []
discharged_by_round: null
introduced_at_round: 5
---

# Lemma 3 (cross-stratum primitivity exploitation). For every $\varepsilon > 0$ there exists $x_0 = x_0(\varepsilon)$ such that, for every primitive $A \subset [x_0, \infty)$,
\[
S(A) \;=\; \sum_{a \in A} \frac{1}{a \log a} \;\le\; 1 + \varepsilon.
\]

## Status: hard. This lemma IS the conjecture.

This is the load-bearing lemma. Per-stratum bounds (Lemmas 1, 2) only
yield $\sum_k S(A^{(k)}) \le \sum_k S(A_k)$, where the right-hand side
is a *divergent* series (each $S(A_k) \to 1$, summed over all $k$).
A per-stratum bound therefore cannot prove the conjecture; the
primitivity constraint must be exploited *across* strata.

## Why it's hard

If $a \in A^{(k)}$ (i.e. $\Omega(a) = k$), primitivity forbids any
multiple $b = a \cdot p$ ($p$ prime) from lying in $A^{(k+1)}$, any
$b = a \cdot p_1 p_2$ from $A^{(k+2)}$, etc. So inclusion at low $k$
*excludes* mass at higher $k$.

The Erdős–Zhang proof of $S(A) \le e^\gamma \pi/4 \approx 1.399 +
o(1)$ (F1) uses a "log-Mertens" weighting — replace $1/(a \log a)$ by
$1/a \int_a^{\infty} du/(u (\log u)^2)$ or similar — to exploit
primitivity uniformly across strata. The bound $1.399$ is the natural
ceiling of *that* argument; sharpening to $1$ requires a different
(unknown) technique.

## What is known

- Erdős's original conjecture (1935): $S(A) \le S(\mathcal{P}) \approx
  1.6366$ for all primitive $A$. Refuted? Refined? Status here treats
  the *truncated* version $S(A \cap [x, \infty)) \le 1 + o(1)$ as
  open.
- Erdős–Zhang (1993): $S(A) < e^{\gamma} \pi/4 + o(1) \approx 1.399$.
- Lichtman (~2020): $S(A) < S(\mathcal{P}) - \delta$ for an explicit
  $\delta > 0$ — but still well above $1$.
- The conjecture target $1 + o(1)$ is consistent with the
  $A_k$-only data (Section 2's F3 asymptotic) and with the witness
  search (Section 4) but lacks a proof technique.

## Current obstacle

I do not see a clean route. The standard Erdős–Zhang weighting
saturates at $e^{\gamma} \pi/4$. A new ingredient is needed — perhaps
a stratum-specific weighting that exploits the F3 deficit
$c k^2/2^k$, perhaps a different decomposition. Without a new idea,
this lemma stays open and the proof body is a partial result.

## Next move

Either:

(a) Find a stratum-aware weighting that converts the $A_k$-only deficit
of F3 into a global deficit for arbitrary primitive $A$. This would
look roughly like: weight each $a \in A^{(k)}$ by $w_k(a) = (1 - c
k^2/2^k) \cdot 1/(a \log a)$, then bound $\sum_k \sum_{a \in A^{(k)}}
w_k(a)$ from primitivity. The factor $(1 - c k^2/2^k)$ is unhelpful
for small $k$ (where $A^{(k)}$ is sparse anyway) but is the right
deficit for large $k$. Rough check: this rescaling could buy back
the gap from $1.399$ to $1$ if the unweighted bound on
$\sum_k \sum_{a \in A^{(k)}} 1/(a \log a)$ is split correctly.

(b) Concede: this is a famous open problem; the loop produces a
*partial result* (Sections 1–4 + Lemma 1 + Lemma 2 + the statement of
Lemma 3 as the gap) and the convergence rule fires.
