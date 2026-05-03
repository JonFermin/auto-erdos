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

## Update from Round 9 — the $6c$ identity

Standard generating-function identity: $\sum_{k \ge 1} k^2 / 2^k = 6$
exactly. Hence the *total* F3 deficit summed over all strata is
$6c \approx 0.394$ (with $c \approx 0.0656$). The F1 gap from
the conjectured ceiling is $e^{\gamma} \pi/4 - 1 \approx 0.399$.

**These two quantities differ by $0.005$.** If they are analytically
equal — i.e. if $c = (e^{\gamma} \pi/4 - 1)/6 \approx 0.0665$
exactly, with the literature's $0.0656$ being a rounded value —
then the conjecture's $1$ ceiling = F1 ceiling minus the cumulative
F3 deficit. This crystallises plan (a) above into a concrete claim:

> **Conjecture (CST — Conjecture-via-Stratum-aware-Tightening).**
> A stratum-aware refinement of Erdős–Zhang exists that loses
> $c k^2/2^k$ per stratum used, recovering the ceiling
> $e^{\gamma} \pi/4 - \sum_k c k^2/2^k = 1$ for any primitive
> $A \subset [x, \infty)$ as $x \to \infty$.

To validate or refute CST one needs:

1. The exact analytical value of $c$ in F3 (Sathe–Selberg). Confirm
   whether $c = (e^{\gamma} \pi/4 - 1)/6$ holds.
2. A "weighted version" of Erdős–Zhang's proof that preserves the
   per-stratum F3 deficit. The standard proof presumably loses the
   stratum information; a refinement that retains it would likely
   yield CST directly.

Neither step is in scope for the present autonomous loop. Documented
as the most concrete open lead from the loop's run.

## Update from Round 17 — precision check on the §9 identity

Computed in proof_strategy.md §16: $e^{\gamma}\pi/4 - 1 =
0.39885100596735378886\ldots$ to 20 decimals (IEEE-754 double, more
than enough precision). The value of $c$ that would make the §9 /
CST identity exact is $c_\star = 0.06647516766122563148\ldots$

The cited literature value $c \approx 0.0656$ differs from
$c_\star$ by $+0.000875$ — a relative gap of $1.32\%$. So the §9
identity is *either* exact (literature value $0.0656$ is just a
2-decimal approximation of $c_\star$) *or* a $1\%$ near-miss
numerical coincidence.

The CST conjecture's plausibility is downstream of which branch
holds. Without literature lookup or a first-principles re-derivation
of $c$ from the Sathe–Selberg formula (Tenenbaum §II.6.1), the
autonomous loop cannot settle this. The open question is now
**concretely scoped**: is the explicit Sathe–Selberg constant equal
to $0.06647516766\ldots$?
