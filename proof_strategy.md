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
  a hypothetical counterexample narrowed by F1–F3 and, from this session,
  by the I-graph clearance (all sizes) and the theta/$K_4$ window screen.

## Section 6 — Q9: DFS depth-chain discharging (in progress)

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
