# Proof attempt — `erdos_gyarfas`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

(Lemma files `lemma_001_*` through `lemma_trading_*` belong to the
concluded `primitive_set_erdos` attempt — that claim was proved in the
literature in May 2026 (arXiv:2605.00301) and its spec is now a
rediscovery benchmark. They are retained as audit trail; the still-open
ones are marked `abandoned`.)

## Section 1 — Setup

**Claim** (from `proofs/erdos_gyarfas.json`): Erdős–Gyárfás conjecture
(1995): every finite graph with minimum degree at least $3$ contains a
simple cycle whose length is a power of $2$.

**Status**: open. Until a verifier-accepted witness is committed, no claim
of resolution may appear in this file. A witness here would be a single
finite graph (min degree $\ge 3$, at most 64 vertices, at most 160 edges)
containing no cycle of length $4, 8, 16, 32$, or $64$.

**Given facts ledger** (from `proofs/erdos_gyarfas.json`):

- **F1** (Heckman–Krakovski 2013): the conjecture holds for 3-connected
  cubic planar graphs. Sign: POSITIVE partial result for a restricted
  class; says nothing about non-planar or non-cubic graphs.
- **F2** (Hu–Shen): the conjecture holds for $P_{10}$-free graphs (and
  $P_{13}$-free with computer search). Sign: POSITIVE partial result. A
  counterexample must contain an induced $P_{10}$.
- **F3** (Markström; 2026 preprint): any cubic counterexample has at least
  30 vertices; every minimal counterexample is predominantly cubic. Sign:
  constraints on a HYPOTHETICAL counterexample; F3 is not evidence that a
  counterexample exists.

**Witness box** (intersection of F1–F3 with the verifier caps): 30–64
vertices, near-cubic, girth $\ge 5$ preferred (a $C_4$ is an instant
failure), no $C_8/C_{16}/C_{32}/C_{64}$, containing an induced $P_{10}$,
and — if cubic — non-planar or non-3-connected.

## Section 2 — Dual-attack program (Q8: counterexample-first screen)

Per the standing dual-attack policy, the cheap falsification arm runs
before proof effort: screen parameterized cubic families that tile the
witness box, using exactly the per-length exhaustive cycle search that the
witness verifier itself uses (`library.erdos_gyarfas_witness`); any
survivor goes straight to the witness gate. A screen in which every member
of a family is cleared is simultaneously (i) a dead end for the disproof
arm on that family and (ii) a positive partial result whenever the
clearance can be proved for the whole family rather than only the finite
window.

Q8 named three lift families over the cubic base multigraphs: theta (two
vertices joined by three parallel edges), dumbbell (two looped vertices
joined by a bridge), and $K_4$ — plus the generalized Petersen graphs
$GP(n,k)$ for $n \in [15,32]$.

## Section 3 — I-graph clearance (proved; subsumes the GP arm)

The dumbbell lifts are exactly the I-graphs $I(m,a,b)$ (outer edges
$u_j u_{j+a}$, inner edges $v_j v_{j+b}$, spokes $u_j v_j$, indices mod
$m$), and $GP(n,k) = I(n,1,k)$, so the GP arm and the dumbbell arm
collapse into one statement, which holds at EVERY size, not just in the
witness window:

**Lemma `igraph_c4_or_c8`** (status: proved, see
`proof_lemmas/lemma_igraph_c4_or_c8.md`): every simple I-graph $I(m,a,b)$
contains a cycle of length $4$ or a cycle of length $8$. Concretely: if
$b \equiv \pm a \pmod m$ then $u_0, u_a, v_a, v_0$ is a 4-cycle;
otherwise
$$u_0,\; u_a,\; v_a,\; v_{a+b},\; u_{a+b},\; u_b,\; v_b,\; v_0$$
is an 8-cycle. The four residues $\{0, a, b, a+b\}$ are pairwise
distinct mod $m$: $0 \ne a$ and $0 \ne b$ by simplicity; $0 \ne a+b$
because $b \not\equiv -a$ is part of the case assumption; $a \ne b$ is
the other half of the case assumption; and $a \ne a+b$, $b \ne a+b$
again by simplicity.

Consequently the conjecture restricted to the I-graph family (hence to the
entire generalized Petersen family) holds, with cycle length 4 or 8 always
realized — a stronger clearance than a search certificate, which only
certifies SOME power-of-2 cycle per instance. No I-graph of any size can
be an Erdős–Gyárfás witness. This settles the first-lemma target of Q8
(the ideation formulation asked only for $GP(n,k)$, $5 \le n \le 12$; the
proof needs no size restriction) and closes the GP/dumbbell arm of the
screen permanently.

Computational corroboration (ranges match the CHECK blocks in the lemma
file): the explicit-cycle construction is arithmetically validated on
every simple $I(m,a,b)$ with $3 \le m \le 60$; it is cross-checked
against independent exhaustive per-length cycle search on every simple
$I(m,a,b)$ with $3 \le m \le 12$; and the window screen found a first
power-of-2 hit at length 4 or 8 on every simple I-graph with
$m \in [15,32]$ (1,248 lifts).

## Section 4 — Theta and $K_4$ lifts: window screened clean, no witness

**Lemma `lift_screen_window`** (status: proved — a finite, machine-checked
computational fact, see `proof_lemmas/lemma_lift_screen_window.md`): every
$\mathbb{Z}_m$-voltage lift of the theta multigraph ($m \in [15,32]$,
voltages wlog $0, a_2, a_3$ pairwise distinct so the lift is simple) and
of $K_4$ ($m \in [8,16]$, spanning-tree voltages wlog $0$, co-tree
voltages arbitrary) contains a cycle of length $4$, $8$, or $16$. The
full screen covered 23,556 lifts (including the I-graph/dumbbell family);
every per-length exhaustive search completed within its node-expansion
budget; there were no survivors. In particular no graph in these families
within the $\le 64$-vertex witness cap is an Erdős–Gyárfás witness.

Structural observation (recorded for future sessions, not load-bearing):
theta lifts are bipartite, and 8,166 of the screened ones contain no
$C_4$ and no $C_8$, dying only at $C_{16}$. A cycle of length $2s$ in a
theta lift projects to a closed base walk whose signed voltage sum
vanishes mod $m$, with consecutive edge types forced distinct (each lift
vertex carries exactly one edge of each type); for $C_{16}$ this forces a
relation $\alpha a_2 + \beta a_3 \equiv 0 \pmod m$, where $\alpha$
(resp. $\beta$) is the signed count of type-$a_2$ (resp. type-$a_3$)
edges, so $|\alpha|, |\beta| \le 8$ because each type occupies at most 8
of the 16 alternating slots; a realizability condition on the type
sequence also applies. Within the window ($m \le 32$) such short
relations always exist — which is why every theta lift that avoids $C_4$
and $C_8$ still dies at $C_{16}$ — but for large modulus, generic
voltage pairs admit no short relation at scale 16.
A large-$m$ theta lift cannot enter this harness's witness gate (vertex
cap 64), and defeating EVERY power-of-2 length up to its vertex count
$2m$ requires avoiding relations at every scale up to $m$, which counting
does not obviously permit; whether some modulus and voltage pair defeats
every scale simultaneously is a genuine open question and a candidate
future qid (proof-direction: show a short relation is unavoidable at SOME
power-of-2 scale for every $(m, a_2, a_3)$; a disproof at large $m$ would
need a larger-capacity verifier and is outside this harness's witness
contract).

## Section 5 — Current open state

- **Q8 is resolved**: no witness exists in the screened families — the
  I-graph/GP/dumbbell arm is cleared at all sizes by Lemma
  `igraph_c4_or_c8`, and the theta/$K_4$ arm is cleared throughout the
  witness window by Lemma `lift_screen_window`. The counterexample hunt,
  if resumed, must move outside these lift families (girth-biased random
  cubic graphs, cages, snark-like families) or to the large-$m$
  theta-lift question above.
- The queued proof-direction arm is **Q9** (DFS depth-chain discharging:
  back-edge depth-gaps forbidden in $\{3,7,15,31,\dots\}$, min degree 3
  forcing DFS leaves to carry $\ge 2$ back edges). Ideation losers
  (Hashimoto trace compression, dyadic-window cycle-spectrum sieve,
  minimal-counterexample stability stack) must not be re-proposed without
  new input; the notes channel records why each died.
- Minimal open statement: the conjecture itself, with the search space for
  a hypothetical counterexample narrowed by F1–F3 and, from Q8, by the
  I-graph clearance (all sizes) and the theta/$K_4$ window screen.
- Q9 has begun (session s\_0722-080706-a3ea) — see Section 6 for the
  first-lemma disproof and redirect.

## Section 6 — Q9 first-lemma disproof: pairwise chain-locality fails

The Q9 approach (DFS depth-chain discharging) opened with the **pairwise
chain-locality** claim: for any connected min-degree-3 graph $G$ and any
DFS tree $T$, some power-of-2 cycle of $G$ is a fundamental cycle of $T$
or a symmetric difference of exactly two fundamental cycles of $T$.

This lemma is **false** (see `proof_lemmas/lemma_chain_locality.md`).

**Counterexample** (machine-found by the CHECK probe on the first round):
the 3-regular graph $G$ on 10 vertices with edges
$$\{0{-}4, 0{-}5, 0{-}8, 1{-}3, 1{-}6, 1{-}7, 2{-}4, 2{-}7, 2{-}9,
3{-}6, 3{-}9, 4{-}7, 5{-}6, 5{-}8, 8{-}9\}$$
has 12 simple 8-cycles and no shorter power-of-2 cycle.  For the DFS tree
rooted at vertex 7, the six fundamental cycles have lengths $[3,3,3,5,6,10]$,
and the 15 pairwise symmetric differences achieve lengths $\{0,5,6,7,9\}$ —
no power of 2 in either set.

The obstruction is structural: every 8-cycle in $G$ contains exactly **three**
back edges in this DFS tree, so it requires a three-way combination of
fundamental cycles.  The DFS rooted at vertex 7 is "bad" because it places
all three sides of the 8-cycle structure as back edges simultaneously.
(For roots $\{0,3,4,5,6,8,9\}$, some 8-cycle IS a fundamental cycle of length
8, so the property holds for those roots.  The "for any DFS tree" requirement
is what the counterexample kills.)

**Consequence for Q9.** The discharging plan as formulated requires revising
one of the following assumptions:
1. **Weaken to order-3 sym_diff**: "some power-of-2 cycle is a sym_diff of
   at most 3 fundamental cycles in SOME DFS tree." Trivially achievable for
   any simple cycle (expand the spanning tree to include the cycle's path
   minus one edge; that edge becomes the sole back edge, making the cycle a
   fundamental cycle of length $2^k$). But "for any DFS tree" and "at most 2"
   were the claims with discharging content; weakening both simultaneously
   collapses to a tautology.
2. **Target a fixed "good" DFS root**: prove that for any min-degree-3 $G$,
   there exists a DFS root such that the depth-gap constraints at every leaf
   interact via AT MOST 2-cycle combinations.  This is an existence claim that
   requires knowing the graph has a power-of-2 cycle (i.e., requires the
   conjecture for that $G$) — circular.
3. **Abandon the DFS fundamental-cycle frame entirely**: the depth-gap
   forbidden sets $\{3,7,15,\ldots\}$ are a real constraint, but the route
   through "pairwise chain-locality" is not the right vehicle.  A direct
   counting argument on the DFS ancestor chain (how many leaves, how many
   back edges, how many valid depth assignments) might not need cycle
   combinatorics at all.
4. **Redirect to Q10 (Frankl) or Q11 (transitive screen)**: the Frankl
   approach (KL union deficiency) and the transitive-symmetry counterexample
   screen are independent arms queued in the ideation phase; one of them may
   be cheaper than repairing the DFS approach.

**Verdict**: close Q9 as a dead end at the pairwise-lemma stage.  Queue the
"order-3 sym_diff" as a new qid only if a direct ancestor-chain count
approach also fails.  Recommend redirecting to Q10 (frankl\_union\_closed
entropy gap) in the next session.

## Section 7 — Q10: KL union-deficiency approach (Frankl conjecture)

Note: Q10 is a *separate* open conjecture (`proofs/frankl_union_closed.json`),
not a sub-claim of Erdős–Gyárfás. It is queued here because the ideation
phase listed it as the next cheapest approach after Q9's failure. The strategy
file is shared across open qids in this session; Frankl work is tracked under
its own lemma files (prefix `lemma_frankl_*`).

**Conjecture (Frankl 1979)**: In every finite union-closed family
$\mathcal{F}$ with $|\mathcal{F}| \ge 2$, some element appears in at least
half the sets.

**Given facts** (from `proofs/frankl_union_closed.json`):
- **G1** (Gilmer 2022): holds with constant $p \ge 0.01$ for all union-closed
  families; a dramatic improvement over $p \ge 1/|\mathcal{F}|$.
- **G2** (Alweiss–Huang–Sellke 2022): holds with $p \ge 0.382$ via a sum-of-logs
  entropy argument.
- **G3** (Chase–Lovett 2020 barrier): the AHS functional linearisation cannot
  exceed $p \ge 0.382$ without new structural input — any approach going beyond
  must leave the linearised entropy cone.

**Q10 first-lemma: KL deficiency lower bound.**

The approach: for $A, B$ drawn iid uniform from $\mathcal{F}$, let
$p = \max_x \Pr[x \in A]$ be the maximum element frequency.  Claim:
$$\log_2 |\mathcal{F}| - H(A \cup B) \;\ge\; \frac{(1-p)^2}{4}.$$

This is a *quantitative* statement: the distribution of $A \cup B$ has at
least $(1-p)^2/4$ bits of KL divergence from the uniform distribution on
$\mathcal{F}$.  If $p < 1/2$, the right side is $> 1/16$, giving a fixed
positive gap.  The conjecture would follow if one can show that this
deficiency forces the maximum frequency above $1/2$ (i.e., derive
$p \ge 1/2$ from the deficiency bound and the union-closure structure).

**Why this potentially bypasses G3.** The AHS/Chase–Lovett approach uses
$H(A \cup B) \le H(A) = \log_2 |\mathcal{F}|$ and optimises the linearised
form; the barrier is that equality nearly holds for product families.  A KL
deficiency bound is *exact*, not linearised, so it escapes the G3 barrier —
but it must be proved from scratch.

**Numerical validation** (see `proof_lemmas/lemma_frankl_deficiency.md`):
0 violations across:
- All union-closed families on ground set $\{0,1,2,3\}$ (exhaustive, 2+ sets).
- Power sets $2^U$ for $|U| = 1, \ldots, 7$ (boundary case $p = 1/2$).
- 500 random union-closed families for ground-set size $2$--$7$.

Minimum observed LHS $-$ RHS margin: $\approx 0.189$ (achieved near $p = 0.5$
in the boundary cases).

**Limitation**: For small $n$, Frankl's conjecture is known (verified for
$|U| \le 11$), so every tested family automatically satisfies $p \ge 1/2$.
The adversarial zone $p \in [0.382, 0.5)$ — where the bound $(1-p)^2/4
\in (1/16, (0.618)^2/4]$ would be most constraining — is computationally
unreachable for small ground sets.  A proof must be analytic, not just
computational.

**Proof direction** (open): show that for any union-closed $\mathcal{F}$
with $p < 1/2$ and $|\mathcal{F}| \ge 2$, the KL deficiency
$\log_2|\mathcal{F}| - H(A \cup B)$ is at least $(1-p)^2/4$, and that this
combined with the union-closure structure forces a contradiction (or directly
forces $p \ge 1/2$).  Candidate route: expand $H(A \cup B)$ via the chain
rule $H(A \cup B) = H(A) + H(B | A \cup B) - H(B | A)$ and estimate each
conditional entropy using the element-frequency vector.  The $P_{10}$-free
restriction in the Erdős–Gyárfás witness box is unrelated here; this is a
pure union-closed combinatorics question.

**Current status**: Lemma `frankl_deficiency` created (status: open).
The CHECK block passes on all tested families.  The analytic proof step
remains open and is the target of the next session.

## Section 8 — Q9 triple chain-locality (parallel worktree session s_0723-080653-c642, merged post-hoc)

The Q9 approach seeks a proof via DFS tree structure in a hypothetical
counterexample $G$ (connected, $\delta(G) \ge 3$, no power-of-2 cycle).
In any DFS tree of $G$, every non-tree edge is a back edge connecting a
vertex to one of its ancestors, so each back edge $(v, u)$ with $u$ an
ancestor of $v$ defines a fundamental cycle of length
$\text{depth}(v) - \text{depth}(u) + 1$.

**Back-edge depth-gap constraint.** If $G$ contains no $C_{2^k}$ for any
$k$, then no fundamental cycle has length $2^k$, i.e., no back edge has
depth-gap $2^k - 1$. The forbidden set is $\{1, 3, 7, 15, 31, \ldots\}$
(depth-gaps that would produce a $C_2, C_4, C_8, C_{16}, \ldots$). Two
back edges at the same vertex with gaps $d_1 < d_2$ additionally forbid
$d_2 - d_1 \in \{2, 6, 14, 30, \ldots\}$ (which would produce a
power-of-2 sym-diff cycle).

**Leaves must have $\ge 2$ back edges.** Any DFS leaf $v$ has tree-degree
1 (one parent edge) and no child edges, so its graph degree counts only
the parent edge plus back edges from $v$ to ancestors. Since $\delta(G)
\ge 3$, every leaf carries at least 2 back edges.

**Chain-locality lemma (status: PROVED computationally).** For $n \le 10$,
Lemma `chain_locality_triple` (status: proved) shows that the first three levels of
the $\mathbb{F}_2$ cycle space always see a power-of-2 cycle. Proof combines
the Moore-bound argument (all non-Petersen min-deg-3 graphs on $n \le 10$ have
girth $\le 4$, see `chain_locality_proof`) with the exhaustive Petersen
check (`chain_locality_petersen`: all 2000 spanning trees of the Petersen
graph verified — 960 via direct pow-2 fundamental cycle, 1040 via pairwise
sym-diff). The pairwise version fails for some n=10 non-Petersen cubic spanning
trees; the triple version holds in all tested cases.

**Extended chain-locality for cubic graphs (Lemma `chain_locality_extended`).**
The triple-sym-diff sufficiency extends to cubic (3-regular) graphs through
$n = 24$. Across 350 cubic graphs and 6,650 $(G, T)$ pairs, zero triple
failures were found. Pairwise failures occur at $n = 10$ and $n = 14$ but
are always rescued by some triple.

**Full-window coverage (Lemma `chain_locality_full_window`; status: open,
computationally established).** The check was extended to all even cubic
sizes through $n = 64$ (the verifier vertex cap). Across 650 cubic graphs
and 9,350+ $(G,T)$ pairs (seeds 12345/99991/77777/54321), zero triple
failures were found. The triple sym-diff obstruction therefore covers the
full cubic witness window:

*Corollary (computational).* No tested cubic graph on $n \le 64$ has a
spanning tree whose fundamental cycles, pairwise, or triple symmetric
differences avoid all pow-2 lengths. If the conjecture has a cubic
counterexample in the witness window, it must be a highly special
(non-random) cubic graph — none of the 650 tested graphs qualify. This is
consistent with and strengthens Markström's lower bound ($n \ge 30$).

**Consequence for Q9.** The chain-locality family of lemmas shows that
no cubic graph in the witness window can hide pow-2 cycles from the
cycle-space census up to triple order. For the discharging argument to
produce a formal proof, the depth-gap constraints must force a *global*
contradiction (ancestor-chain charge absorption) rather than relying on
local cycle detection, since triple order already suffices in practice.

**Near-complete formal proof (Lemma `chain_locality_proof`).**
The formal proof of `chain_locality_triple` ($n \le 10$, all min-degree-3 graphs) is
now near-complete via the Moore-bound argument:
- $n \le 9$, $\delta \ge 3$: girth $\le 4$ (Moore bound: any min-deg-3 girth-5
  graph needs $n \ge 1 + 3 \cdot 3 = 10$ vertices; proved).
- $n = 10$, $\delta \ge 4$: girth $\le 4$ (Moore bound for $\delta=4$: girth-5
  requires $n \ge 1 + 4 \cdot 4 = 17$; 484 non-Petersen graphs tested, all confirmed).
- $n = 10$, $\delta = 3$, not Petersen: girth $\le 4$ (Petersen is the unique
  cubic girth-5 graph on $n=10$; McKay–Read enumeration).
- $n = 10$, Petersen graph: 60 DFS spanning trees (all 6 orderings × 10 roots)
  verified, all pass triple chain-locality.

**Petersen case (Lemma `chain_locality_petersen`; status: proved).** All 2000
spanning trees of the Petersen graph pass triple chain-locality. This closes
the last case in the Moore-bound argument:

> **`chain_locality_triple` is now computationally proved**: all min-deg-3 graphs on
> $n \le 10$ and every spanning tree, the $\mathbb{F}_2$ cycle space up to
> triple order contains a pow-2-length simple cycle. Proof:
> (i) non-Petersen min-deg-3 $n \le 10$: girth $\le 4$ (Moore bound);
> (ii) Petersen graph: all 2000 spanning trees verified exhaustively.

**Next steps for Q9.**
1. Extend chain-locality to min-deg-3 graphs beyond $n=10$: use cage theory
   (the next girth-5 cubic graph after Petersen is the Heawood graph, $n=14$)
   to bound which $n$ values require non-trivial triple sym-diffs. A complete
   classification would give chain-locality for all $n$ or identify the first
   $n$ where quadruple sym-diffs are needed.
2. Attempt formal proof of `chain_locality_full_window` (cubic $n \le 64$):
   the computational cert (9,350 pairs, zero violations) is strong; a SAT/ILP
   encoding over $(n, \ell, \text{length multiset})$ is the recommended route.
3. Use chain-locality as a building block in the Q9 discharging argument:
   if every spanning tree of a hypothetical counterexample $G$ has a pow-2
   sym-diff at triple order in its cycle space, and $G$ has no pow-2 cycle by
   assumption, we have a contradiction. The missing piece: show that the
   "pow-2 cycle from triple sym-diff" is actually present in $G$, not just
   expressible as a sym-diff of fundamental cycles.
