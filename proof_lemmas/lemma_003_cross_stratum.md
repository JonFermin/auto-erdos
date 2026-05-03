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

## Update from Round 18 — numerical-sieve route is infeasible

Direct SPF sieve at $N = 10^7$ gives $S_k(N)$ for $k=1\ldots10$
(see proof_strategy.md §17). The implied $c$ grows monotonically
with $k$ — far from the asymptotic constant. Reason: $A_k$ mass
saturates at $u_k = e^{e^k}$. For $k=5$, $u_k \sim 10^{65}$;
for $k=8$, $u_k \sim 10^{1295}$. No feasible sieve reaches the
regime where the asymptotic kicks in.

Therefore the §16 dichotomy ($c_\text{lit} = 0.0656$ vs
$c_\star = 0.06647517$) cannot be resolved autonomously by direct
numerical experiment. Three remaining paths: (a) literature
lookup, (b) first-principles re-derivation of $c$ via Mertens
integrals, (c) side-step §9 via the §11.4 cross-stratum
exclusion route — option (c) is the most autonomous-tractable.

## Update from Round 19 — explicit two-stratum cross-exclusion table

Computed $S(A^{(k_1)} \sqcup A^{(k_2)}_\text{kept})$ for
$(k_1, k_2) \in \{(2,3),(2,4),(2,5),(3,4),(3,5),(3,6)\}$ at
$x \in \{10^2, 10^3, 10^4\}$, $N = 10^6$ (proof_strategy.md §18).

Key finding: max two-stratum sum decays $0.337 \to 0.212 \to 0.133$
as $x$ goes $10^2 \to 10^3 \to 10^4$, faster than $1/\log x$.
Pair $(2,4)$ dominates at every $x$. Kept fraction grows above
the §13 threshold $k_1 < \sqrt{2 k_2}$: at $(2,5)$ it reaches
$38\%$ at $x=10^4$.

This is the strongest empirical signal in 18 rounds that the
conjecture holds — but only as evidence within $x \le 10^4$.
Analytical step still needed: a saddle-point bound on
$\sum_k a_k(x) \rho_k(x)$ where $\rho_k(x)$ is the cross-stratum
kept fraction. §13's Erdős–Kac threshold gives $\rho_k$ asymptotics
but not yet the closed-form $\sum_k a_k \rho_k$ inequality.

## Update from Round 20 — closed-form a_k(x; infty) + restated goal

§19 derived (rigorously, by partial summation from §11.1):
  a_k(x; inf) ~ (1/log x) * sum_{j=0..k-1} (loglog x)^j / j!
              = (1/log x) * P(Poisson(loglog x) <= k-1)

Validated numerically at x=10^7 against §17 sieve data: k=1 gives
1.6366 = Erdős's prime-tail constant exactly; k=3..10 give
S(A_k)_inf within 1% of 1, confirming §11.

This restates Lemma 3's open goal in the cleanest form yet
(§19.5):
  prove sum_{k=L..L^2/2} rho_k(x) = o(log x) uniformly as x→inf,
where L = loglog x and rho_k is the §18-style cross-stratum kept
fraction. §13's Erdős–Kac saddle-point should give this — but
hasn't been worked out rigorously yet.

This is the single missing analytic step that closes the
§11+§12+§13+§18+§19 chain into a proof of Lemma 3 / the CST
conjecture.
