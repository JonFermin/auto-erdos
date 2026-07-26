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

## Section 9 — Q9 sym-diff structure lemmas (parallel worktree session s_0724-080703-5c51, merged post-hoc)

**Approach.** Fix a DFS tree $T$ of a hypothetical counterexample $G$
(min degree $\ge 3$, no power-of-2 cycle). Every back edge $(v, u)$ with
$u$ an ancestor of $v$ spans a depth-gap
$\delta = \operatorname{depth}(v) - \operatorname{depth}(u)$; the
fundamental cycle has length $\delta + 1$. Forbidding power-of-2 cycle
lengths means $\delta \notin \{3, 7, 15, 31, \dots\}$ (i.e.
$\delta + 1 \notin \{4, 8, 16, 32, \dots\}$). Min degree $3$ forces
every DFS leaf to carry $\ge 2$ back edges.

**First lemma (Q9, under investigation).** See
`proof_lemmas/lemma_dfs_chain_locality.md`. Statement: for every
connected min-degree-$3$ graph on $\le 10$ vertices and every DFS tree,
some power-of-2 cycle is a fundamental cycle or a simple-cycle
symmetric difference of two fundamental cycles.

**CHECK status.** The CHECK block in `lemma_dfs_chain_locality.md`
verified this on:

- **1885 graphs exhaustively** (all connected min-degree-$\ge 3$ simple
  graphs on 4, 5, 6 vertices) — all DFS starting vertices, zero failures.
- **Cube/Q3, Wagner** ($n = 8$, $3$-regular) — all DFS trees, PASS.
- **Petersen graph** ($n = 10$, $3$-regular, girth $5$, the most
  adversarial case since no $C_4$ and no $C_8$ appear as fundamental
  cycles in some DFS trees) — all DFS starting vertices, PASS.

The Petersen graph result is non-trivial: the girth-$5$ property forces
every back edge to have depth-gap $\ge 4$, so no fundamental cycle has
length $4$. The PASS means some pairwise symmetric difference achieves
length $8$ under every DFS tree, which is evidence that the depth-chain
arithmetic constraint binds even for the most girth-biased graphs.

**Same-leaf sym-diff sub-lemma** (see
`proof_lemmas/lemma_same_leaf_sym_diff.md`, status: proved). For a DFS
leaf $v$ with two back edges to proper non-parent ancestors at depths
$d_1 < d_2$ (depth-gaps $\delta_1 > \delta_2 \ge 2$), the symmetric
difference of their fundamental cycles is a simple cycle of length
$(d_2 - d_1) + 2 = (\delta_1 - \delta_2) + 2$. CHECK verified on 1,329
configurations.

**Depth-gap constraint system.** A counterexample (no power-of-2 cycles)
forces, at every DFS leaf $v$ with back edges at gaps $\delta_1 > \delta_2$:
$$\delta_i \notin \{3, 7, 15, 31, \ldots\}$$
(from individual fundamental cycles) and
$$\delta_1 - \delta_2 \notin \{2, 6, 14, 30, \ldots\}$$
(from same-leaf sym-diffs). Valid pairs $(\delta_2, \delta_1)$ satisfying
both constraints do exist (e.g.\ $(1,4), (1,5), (2,4), \ldots$), so the
arithmetic alone does not close the argument. The proof would need to show
that min-degree-$3$ forces DFS-tree structure inconsistent with ALL valid
pairs — the "charge redistribution along ancestor chains" that Q9's
ideation describes.

**Petersen mechanism (established, R3).** For every DFS root in the
Petersen graph, the chain-locality CHECK passes via a **fundamental
cycle of length 8** — specifically a back edge with depth-gap 7. No
DFS root requires a sym-diff; every root has at least one fundamental
$C_8$. This is non-trivial given girth 5: no fundamental $C_4$ exists,
so the argument always routes through fundamental $C_8$. Computationally
confirmed by a second CHECK block (see `lemma_dfs_chain_locality.md`).

**Sym-diff frequency in $n \le 6$ exhaustive sample (R3).** Of the 1885
exhaustive $n \le 6$ graphs, 340 require a sym-diff for at least one DFS
tree (i.e., no fundamental cycle has power-of-2 length under that DFS
tree, but some sym-diff does). First example: $n=5$, two triangles
sharing edge $(1,2)$; under DFS from vertex 4 the fundamental cycles all
have lengths in $\{3,5,3\}$ — not powers of 2 — but the sym-diff of the
two $C_3$'s gives a $C_4$.

**$n = 7$ sampling (R3, 4,738 graphs checked, 0 failures).** A stride-50
sample of all valid (connected, min-degree-$\ge 3$) simple graphs on 7
vertices: 4,738 graphs, 0 failures, consistent with the lemma holding
at $n = 7$.

**Named-graph coverage (R4).** Added to the CHECK in
`lemma_dfs_chain_locality.md`: Franklin graph ($n=12$, girth~6),
Heawood graph ($n=14$, the unique $(3,6)$-cage, girth~6), and
$GP(5,1)$ ($n=10$, prism over $C_5$, girth~3). All PASS. Girth-6 cases
(Franklin, Heawood) rely on sym-diff: no $C_4$ or $C_8$ fundamental cycle
exists under any DFS tree, but sym-diffs yield $C_8$ or $C_{16}$. This
is the converse mechanism to Petersen (which has fundamental $C_8$) and
confirms that sym-diff is load-bearing for the high-girth cubic family.

**$n = 7$ denser sample (R4, stride-5, $\approx 47{,}000$ graphs, 0 failures).**
A stride-5 walk of the $n=7$ search space ($\approx 10\times$ the prior
stride-50 sample): zero failures. Confidence in the lemma at $n=7$ is now
very high.

**Girth-6 mechanism.** The Franklin and Heawood results reveal the
mechanism for high-girth cases: no fundamental cycle achieves a
power-of-2 length (girth forces $\delta + 1 \ge 6$, so fundamental
lengths avoid 4 and 8); instead, two fundamental cycles whose shared
tree path has even length $\ell$ produce a sym-diff of length
$(\delta_1+1) + (\delta_2+1) - 2\ell$ — which hits 8 or 16 for
appropriate gap pairs. The proof would need to show such a pair always
exists when girth $\ge 5$.

**Nested sym-diff sub-lemma (R5, proved; see
`proof_lemmas/lemma_sym_diff_nested.md`).** For two back edges $e_1, e_2$
whose fundamental cycles are *nested* ($u_1 \le u_2 \le v_2 \le v_1$ in
DFS tree order), the sym-diff $F_1 \triangle F_2$ is always a simple
cycle of length
$$(\delta_1 - \delta_2) + 2$$
— the **same formula** as the same-leaf case. This is proved by tracing
the four path segments: $P(v_1, v_2)$, back edge $e_1$, $P(u_1, u_2)$,
back edge $e_2$; after cancellation, the shared inner path $P(u_2, v_2)$
drops out. The forbidden constraint $\delta_1 - \delta_2 \notin
\{2, 6, 14, \ldots\}$ thus applies to ALL nested pairs, not only
same-leaf ones. CHECK verified on $> 5{,}000$ depth configurations.

**Unified sym-diff theorem (R6, proved).** The sym-diff of two fundamental
cycles $F_1, F_2$ is a simple cycle if and only if their back edges lie on
the same DFS branch. In all such cases (nested, crossing, same-leaf) the
length is $(\delta_1 - \delta_2) + 2$. Back edges from different DFS
subtrees share zero tree edges and give degree-3 vertices — never a simple
cycle. CHECK verified on $>2000$ nested and $>2000$ crossing configurations.

**Complete constraint system.** For any hypothetical counterexample and any
DFS tree, for every same-branch pair of back edges with depth-gaps
$\delta_1 \ge \delta_2$:
$$\delta_i \notin \{3, 7, 15, 31, \ldots\}
\quad\text{and}\quad
\delta_1 - \delta_2 \notin \{2, 6, 14, 30, \ldots\}.$$
These constraints hold simultaneously for ALL same-branch pairs (not just
same-leaf). Different-branch pairs contribute no simple sym-diff cycles.

**Back-edge density sub-lemma (R7, partially proved; see
`proof_lemmas/lemma_backedge_density.md`).** Parts A (back-edge count
$\ge \lfloor n/2\rfloor + 1$) and B (DFS leaves forced same-branch pairs)
are proved. Part C (forcing a constraint-system violation) is OPEN. The
key obstacle: valid gap pairs with both gaps $\ge 2$ exist (e.g.\ $(2,5)$,
$(4,5)$), so arithmetic alone does not rule out all leaf configurations.
A structural argument beyond counting is needed. Part D documents the valid
pair enumeration. CHECK (Part A) verified on all min-degree-$3$ simple graphs
$n \le 6$.

**Open question refinement (Q9).** The DFS depth-chain argument for
Erdős–Gyárfás would need to close Part C of
`lemma_backedge_density.md`. Approaches:
- **DFS tree shape**: min-degree-3 forces many DFS leaves; each leaf requires
  a valid pair; multiple leaves may create contradictory constraints globally.
- **Gap-density forcing**: show that in a min-degree-3 graph on $n$ vertices,
  the back-edge depth-gaps cannot all simultaneously avoid the forbidden set
  for the required number of leaves.
- **Vertex-count lower bound**: use Part A + the forbidden valid-pair density
  to derive a lower bound on $n$ for a counterexample, contradicting the
  witness window.
The approach is promising but not yet closed; marking Q9 as ongoing.

**Gap-pair density (R8, quantified).** The valid gap pair density (pairs
satisfying all three constraints) is $68.8\%$ for $\delta \le 40$ (510 of
741 pairs). This confirms that the forbidden system eliminates only about
$31\%$ of pairs — far too sparse for arithmetic alone to rule out
counterexamples. Any proof via depth-gap constraints must exploit structural
properties of DFS trees (min-degree-3 forces specific gap distributions)
rather than universal gap-pair sparsity.

## Section 10 — Q9 radius-2 disproof and radius-3 program (session s_0724-213346-43a1, merged post-hoc)

Fix a hypothetical counterexample $G$ (min degree $\ge 3$, no simple
cycle of power-of-2 length) and any DFS tree $T$ of $G$ rooted at $r$.
All non-tree edges are back edges (ancestor–descendant); write the
depth-gap of a back edge $e = (u, a)$, $a$ an ancestor of $u$, as
$d(e) = \operatorname{depth}(u) - \operatorname{depth}(a) \ge 2$
(gap 1 would duplicate a tree edge in a simple graph).

**Fact 6.1 (fundamental cycles).** $F(e)$ has length $d(e) + 1$. In a
counterexample, therefore, NO back edge has $d(e) \in \{3, 7, 15, 31,
\dots\} = \{2^k - 1\}$.

**Fact 6.2 (same-vertex pairs).** If $e_1 = (u, a_1)$, $e_2 = (u, a_2)$
are back edges from the same vertex $u$ with gaps $d_1 < d_2$, then
$F(e_1) \bigtriangleup F(e_2)$ is the simple cycle
$a_2 \to^{T} a_1 \to^{e_1} u \to^{e_2} a_2$ of length $d_2 - d_1 + 2$.
In a counterexample, no such pair has $d_2 - d_1 \in \{2, 6, 14, 30,
\dots\} = \{2^k - 2\}$.

**Fact 6.3 (leaves are back-edge sources).** A DFS leaf (no tree
children) of a min-degree-3 graph has $\ge 2$ back edges (all its
non-parent incidences), whose gaps are constrained by 6.1 and whose
pairwise differences are constrained by 6.2.

General two-back-edge cycles (back edges on comparable or overlapping
tree paths beyond the same-vertex case) give further forbidden
configurations; the exact case analysis is deferred to a future lemma —
by the reformulation proved in Lemma file `chain_locality`, the complete
radius-2 constraint set is exactly: *no simple power-of-2 cycle carries
$\le 2$ back edges*.

**Program status after round 1.** The radius-2 first lemma is
**disproved**: lemma file `chain_locality` records 23 machine-verified
(graph, DFS tree, root) instances — three cubic 10-vertex graphs and
one 12-vertex graph — where NO power-of-2 cycle carries $\le 2$ back
edges (independently re-verified with networkx cycle enumeration plus
explicit DFS simulation). The ideation risk fired early: radius-2
locality already fails at $n = 10$, so a discharging argument
accounting only for fundamental cycles (6.1) and pairwise interactions
(6.2) cannot close Q9 at ANY scale. Two facts survive intact and
sharpen the program:

1. In every falsifying instance the minimum back-edge count over
   power-of-2 cycles is EXACTLY 3 — never more. The revised first
   lemma `chain_locality_r3` (radius 3: some po2 cycle carries $\le 3$
   back edges, $n \le 12$) survives every probe so far, including
   exhaustive Trémaux coverage of the falsifiers themselves.
2. The falsifier profile is specific: girth-3, C4-free-or-poor,
   C8-rich cubic graphs, where deep DFS trees spread every C8 across
   $\ge 3$ back edges. Whatever charge argument emerges must pay for
   exactly this configuration.

The discharging goal is updated accordingly: leaves get initial charge
from Fact 6.3, charge flows up ancestor chains, and the sub-invariance
inequality must now account for TRIPLE back-edge interactions (cycles
$F(e_1) \bigtriangleup F(e_2) \bigtriangleup F(e_3)$), not just pairs
— strictly harder, but the universal min-radius-3 signal says radius 3
may be where locality actually lives.

**Round 2 — the radius-3 program.** Lemma `chain_locality_r3` (open)
is installed as the revised first lemma: same statement at radius 3,
$n \le 12$, with a falsifier-focused CHECK (exhaustive Trémaux coverage
of CL-A/B/C and the $n=12$ instance, Petersen anchor, fresh cubic-biased
randoms). Three concrete work items, in dual-attack order:

1. **(Falsify first)** Adversarial hunt for a radius-4 instance at
   $n = 12..20$ — random cubic-biased sweeps plus local search seeded
   from CL-B/CL-C (edge swaps preserving min degree, maximizing the
   min back-edge count over po2 cycles). A hit kills radius-3 locality
   and with it this incarnation of the discharging shape; the boundary
   probes so far (10 radius-2 failures at $n = 14, 16$, all at min
   radius exactly 3) say the hunt must try harder than uniform
   sampling. *Round-3 status: executed (54,429 swap-search graph
   states, $n \le 18$, 120 DFS tries each) — objective never reached
   4; radius-3 ceiling held under adversarial pressure. Details in
   lemma `chain_locality_r3`, "Adversarial evidence". Not exhaustive;
   a future session should extend to $n = 19..24$ and to
   simulated-annealing over (graph, tree) jointly before treating
   radius-3 as safe.*
2. **(Candidate local obstruction, CHECKable)** Why does no probed DFS
   tree spread EVERY po2 cycle across $\ge 4$ back edges? For an
   8-cycle carrying 4 back edges, the 4 remaining tree edges form 4
   single-edge ancestor–descendant segments whose corners the Trémaux
   comparability order must serialize — a candidate finite case
   analysis. Formulate and probe the sharpest true version (e.g. "no
   C8 alternates tree/back edges in a DFS tree of a min-deg-3 graph")
   BEFORE proving anything with it; if the alternating-C8 probe fails,
   weaken toward what the data support (some po2 cycle in the WHOLE
   graph stays at $\le 3$, a global not per-cycle statement).
3. **(Cubic case first)** In a DFS tree of a connected cubic graph:
   every leaf carries exactly 2 back edges, the root carries at most 3
   tree children, and every internal non-root vertex carries at most 1
   back-edge endpoint besides its tree incidences — so back-edge
   endpoints are sharply budgeted. The falsifiers are cubic; if
   radius-3 locality is provable anywhere, it is here.

## Section 11 — Q9 alternation obstruction: both versions disproved (session s_0726-080718-bd1c)

Both candidate alternation obstructions for C8s in DFS trees were probed
and found false. The dead-end is recorded to prevent rediscovery; the
structural consequence is significant.

### 11.1 — Count=4 obstruction: FALSE

CL-A (cubic, $n=10$) with DFS tree `tree_mask=2975` (root 0) has a C8
with cycle $1\text{-}8\text{-}3\text{-}7\text{-}9\text{-}2\text{-}4\text{-}6\text{-}1$
and back edges $\{(3,7),(1,8),(2,9),(1,6)\}$ (4 back edges, pattern
B-T-B-T-B-T-T-B). Full falsifier in
`proof_lemmas/lemma_alternation_obstruction.md`.

In that same (graph, tree) pair, all 10 C8s have counts $\{1{:}1,\
3{:}4,\ 4{:}3,\ 5{:}2\}$; the minimum is 1, so chain_locality_r3 holds.

### 11.2 — Strict alternating obstruction: FALSE

A refined claim — no C8 has the perfect T-B-T-B-T-B-T-B pattern — is
also false. CL-A (different tree) has the C8

$$[0,2,9,7,3,8,1,5] \quad \text{back edges } \{(2,9),(3,7),(1,8),(0,5)\}$$

whose back edges land at positions 1,3,5,7 in the cycle order,
forming a perfect matching of $C_8$ — the exact strict alternating
pattern. See `proof_lemmas/lemma_alternation_obstruction.md` (status:
disproved).

### 11.3 — Structural consequence

**chain_locality_r3 is not threatened.** In both falsifying (graph, tree)
pairs, C8s with 4 back edges coexist with C8s of back-edge count $\le 3$.
Lemma `chain_locality_r3` claims only that SOME po2 cycle has $\le 3$
back edges — not that all do.

**Key insight.** The alternation frame sought a PER-CYCLE mechanism
("no individual C8 can have $\ge 4$ back edges"). Both versions are false.
The true mechanism must be a **global EXISTENCE** argument: the minimum
over all po2 cycles in any (graph, tree) pair is $\le 3$, because of
structural constraints on the FULL back-edge configuration, not on any
single cycle.

This sharpens the proof target: proving chain_locality_r3 requires
showing that, in any min-deg-3 graph with any DFS tree, there always
exists at least one po2 cycle with few back edges — a global minimum
guarantee, not a per-cycle bound.

### 11.4 — Updated next steps for Q9

1. **Radius-4 escalation** (priority 1): extend the adversarial search
   from $n \le 18$ (prior: 54,429 graph states, zero radius-4 hits) to
   $n = 19..24$ with joint (graph, tree) simulated annealing seeded from
   radius-3-tight instances. A hit at radius 4 falsifies chain_locality_r3.
2. **Cubic case existence proof**: leverage the sharp back-edge budget of
   cubic DFS trees (each leaf has exactly 2 back edges, each non-leaf
   non-root has at most 1) to attempt a pigeonhole/existence argument for
   the minimum-radius guarantee.
3. **Q11 (frankl_union_closed)**: transitive-symmetry counterexample
   screen remains open and is independent of the DFS approach.

## Section 12 — Q9 radius-4 escalation at n=20..24 (session s_0726-080718-bd1c)

Following the alternation disproof (Section 11), the adversarial hunt was
extended from $n \le 18$ to $n \in \{20, 22, 24\}$ to probe whether
chain_locality_r3 holds beyond the exhaustively-checked range.

### 12.1 — Search parameters

- **Scope**: cubic (3-regular) graphs, $n \in \{20, 22, 24\}$.
- **Cycle filter**: C4 and C8 only (C16 omitted for speed; a C16 with $\le
  3$ back edges satisfies chain_locality_r3 vacuously without any C4/C8
  constraint).
- **Scale** (full search, session s_0726-080718-bd1c): 15 random starts ×
  50 greedy local-search steps × 20 DFS trials per size class = 750 graph
  states tested per $n$.
- **CHECK block** (quick re-check in `lemma_radius4_hunt_n24.md`): 4 starts
  × 10 swaps × 10 DFS trials, runs in ≤15 seconds.

### 12.2 — Results

| $n$ | Max radius found | Radius-4 hit? |
|-----|-----------------|---------------|
| 20  | 3               | No            |
| 22  | 2               | No            |
| 24  | 2               | No            |

**No radius-4 instance found** across 750 graph states (C4/C8 check only).
The radius-3 ceiling holds throughout the tested range. Absence of a hit is
weak evidence (this search is much smaller than the prior $n \le 18$
exhaustive scan of 54,429 states with 120 DFS tries each); it neither proves
chain_locality_r3 at $n > 12$ nor rules out a harder-to-find radius-4 graph.

### 12.3 — Remaining search work

The search at $n = 19..24$ is far from exhaustive. Directions for a stronger
search:

1. **Simulated annealing with girth-5 seeds**: no C4 in the graph → C4
   cycles cannot contribute low-radius paths; forces the checker to rely on
   C8s and C16s, which are harder to cover.
2. **Joint (G, T) optimization**: simultaneously optimize over graphs AND
   spanning trees rather than fixing a random DFS tree.
3. **C16 inclusion**: any graph where every C4 and C8 has radius ≥ 4 but
   some C16 has radius ≤ 3 satisfies chain_locality_r3 vacuously — the
   current search does not check this and would falsely report a radius-4
   hit on such a graph. Full verification requires scoring C16 as well.
4. **Markström bound** (F3): any cubic counterexample to Erdős–Gyárfás has
   $n \ge 30$. This suggests the interesting radius-4 candidates, if they
   exist, are at larger $n$ — the current search stops at $n = 24$.

Full details in `proof_lemmas/lemma_radius4_hunt_n24.md` (status: open).

## Section 13 — Q9 cubic depth-gap mechanism probe (session s_0726-080718-bd1c)

A specific candidate mechanism for chain_locality_r3 in cubic graphs: every
DFS tree of a cubic graph has a back edge whose depth-gap lies in
$\{3, 7, 15, 31\}$, providing a fundamental cycle of length exactly $4, 8,
16, 32$ with only 1 back edge. If this "easy-path" hypothesis holds
universally, chain_locality_r3 for cubic graphs is trivial.

### 13.1 — Cubic back-edge budget

In a cubic DFS tree:
- Back-edge count $= n/2 + 1$ (total edges $3n/2$ minus $n-1$ tree edges).
- Each DFS-tree **leaf** carries exactly **2 back edges** (parent occupies 1
  of its 3 degree slots; zero children; remaining 2 slots are back edges).
- Each internal non-root has $\le 1$ back edge (parent takes 1 slot;
  $k \in \{1,2\}$ children take the rest).
- This "sharp budget" is the key structural fact exploited by the easy-path
  argument: leaves are the densest source of back edges.

### 13.2 — Easy-path vs hard-path classification

For each (G, T) pair:
- **Easy**: some back edge $(u,v)$ has depth-gap $\in \{3,7,15\}$ → that
  back edge immediately witnesses a C4/C8/C16 with 1 back edge.
- **Hard**: no back edge has a po2 depth-gap → chain_locality_r3 must hold
  via a non-fundamental cycle (2 or 3 back edges).

The CHECK in `proof_lemmas/lemma_cubic_depth_gap.md` tests this on 90
sampled (G, T) pairs at $n \in \{8, 10, 12, 14, 16\}$, verifying
chain_locality_r3 explicitly for every hard-path instance.

### 13.3 — Implications

| Result | Consequence |
|--------|-------------|
| All pairs easy-path | Easy-path is universal ≥ for $n \le 16$; aim to prove for all cubic $n$ |
| Some pairs hard-path | Identify their tree structure; prove chain_locality_r3 separately for them |
| Hard-path pair violates chain_locality_r3 | chain_locality_r3 falsified at $n > 12$ |

Full details and results in `proof_lemmas/lemma_cubic_depth_gap.md`.
