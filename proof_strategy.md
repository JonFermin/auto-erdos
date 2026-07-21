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
- The active proof-direction arm is **Q9** (DFS depth-chain discharging:
  back-edge depth-gaps forbidden in $\{3,7,15,31,\dots\}$, min degree 3
  forcing DFS leaves to carry $\ge 2$ back edges). Ideation losers
  (Hashimoto trace compression, dyadic-window cycle-spectrum sieve,
  minimal-counterexample stability stack) must not be re-proposed without
  new input; the notes channel records why each died.
- Minimal open statement: the conjecture itself, with the search space for
  a hypothetical counterexample narrowed by F1–F3 and, from this session,
  by the I-graph clearance (all sizes) and the theta/$K_4$ window screen.

## Section 6 — Q9: DFS chain-locality approach (in progress)

**Goal**: prove that every connected graph $G$ with $\delta(G) \ge 3$
contains a cycle of length $2^k$ for some $k \ge 2$.

**DFS tree setup.** Fix an arbitrary DFS spanning tree $T$ of $G$. Every
non-tree edge $(u,v)$ is a back edge (undirected DFS has no cross edges),
connecting a descendant to an ancestor. The associated *fundamental cycle*
$C_{uv}$ uses the tree path from $u$ up to $v$ plus the back edge; its
length is $\mathrm{depth}(u) - \mathrm{depth}(v) + 1$.

**Pairwise chain-locality lemma** (Lemma `dfs_chain_locality`, status:
open). For any $G$ with $\delta(G) \ge 3$ and any DFS tree $T$:

1. Some fundamental cycle of $T$ has length $2^k$, OR
2. The symmetric difference $C_{e_1} \triangle C_{e_2}$ of some two
   fundamental cycles is a simple cycle of length $2^k$.

*Computational evidence* (round 2, 2026-07-21): every connected min-degree-3
labeled graph on $n = 4,5,6$ vertices passes for ALL DFS trees (1,885
graphs exhaustively; sorted and reversed adjacency tested per root). The
Petersen graph ($n = 10$, girth 5) also passes. No counterexample in 1,887
graphs.

**Why (1) failing forces two back edges at every DFS leaf.** If (1) fails,
no back edge $(u,v)$ has depth-gap $2^k - 1$. Every DFS leaf $\ell$ has
$\mathrm{outdeg}_T(\ell) = 0$, so all $\deg_G(\ell) \ge 3$ incident edges
are back edges (going to ancestors). In particular every leaf carries $\ge
3$ back edges. (Non-leaf vertices with $\mathrm{outdeg}_T \ge 1$ carry
$\ge 0$ back edges; they are not the immediate target of the argument.)

**Spine-pair characterization (Round 4 update).** The sym-diff $C_{e_1} \triangle
C_{e_2}$ is a simple cycle iff all four endpoints lie on a common DFS spine AND the
two depth intervals overlap.  The unified length formula (wlog $d_{u_1} \ge d_{u_2}$):
$$|C_{e_1} \triangle C_{e_2}| = |d_{u_1} - d_{u_2}| + |d_{v_1} - d_{v_2}| + 2.$$
Two sub-cases: *nested* ($d_{v_1} \le d_{v_2}$, gap-difference $\delta_1-\delta_2$
equals the sum) and *crossing* ($d_{v_1} > d_{v_2}$, depth intervals partially overlap
in the middle; gap-difference $\delta_1-\delta_2 = (d_{u_1}-d_{u_2})-(d_{v_1}-d_{v_2})$
can be 0 even though the sym-diff has length $> 2$).  Condition (2) requires
$|d_{u_1}-d_{u_2}| + |d_{v_1}-d_{v_2}| = 2^k-2$ for some $k \ge 2$.

**Diagnostic (n=4..6), refined.** 1,174 A-fail DFS-tree instances; every satisfying
pair is a $C_4$ ($k=2$, sum $=2$).  Of these: 800 are nested ($|\delta_1-\delta_2|=2$)
and 374 are crossing ($|d_{u_1}-d_{u_2}|=|d_{v_1}-d_{v_2}|=1$, same gap
$\delta_1=\delta_2$, adjacent spine vertices).  Gap sets in A-fail trees: $\{2,4\}$,
$\{2,4,5\}$, $\{2,5\}$.

**Key mechanism for crossing pairs.** If DFS leaf $\ell$ has a back edge of gap $g$,
and its parent $p=\mathrm{par}(\ell)$ also has a back edge of the SAME gap $g$, then
the pair $\{e_\ell, e_p\}$ is a crossing pair with $A=B=1$ and sym-diff a $C_4$,
regardless of any other gaps.  The min-degree constraint forces $p$ to carry $\ge 1$
back edge (it uses 2 of its $\ge 3$ edges on tree edges to $\ell$ and $\mathrm{par}(p)$).

**Round 5 finding: pairwise claim is FALSE; 3-locality holds (empirically).** A sample
of 600 connected 3-regular graphs ($n \in \{10,12,14\}$) was tested over all canonical
DFS trees (2 root-orderings × $n$ roots).  In 7 (graph, DFS-tree) pairs, condition (A)
fails AND no pairwise sym-diff (condition B2) is a simple power-of-2 cycle — though the
graph contains a $C_8$.  The failure mode: the relevant back edges lie on different DFS
spines, so every pairwise sym-diff of the "right" edge-count decomposes into two disjoint
cycles rather than one.  In EVERY such failing case, a **triple** sym-diff of fundamental
cycles IS a simple $C_8$.  Distribution over 1,706 A-fail DFS trees in the sample:
1,699 resolved by B2 (pairwise), 7 by B3 (triple), 0 needing quadruple or larger.

**Round 6 finding: depth-separation + odd-overlap bridge.** Inspection of all 6
pairwise-failing DFS trees from the $n \le 14$ sample yields a uniform pattern:

(a) **Depth-separation**: the two components $D_0, D_1$ of the non-simple pairwise
    sym-diff have vertex-depths that don't interleave — one component occupies a
    strictly deeper depth band than the other.  All 6 cases confirm this.

(b) **Odd-overlap bridge**: in every case a back edge $e_k$ exists such that $C_{e_k}$
    shares an ODD number of edges with each of $D_0$ and $D_1$.  Such a bridge makes
    $(D_0 \cup D_1) \triangle C_{e_k}$ a connected simple cycle.  The bridge's spine
    path spans both depth bands (passing through vertices of both $D_0$ and $D_1$).

**Revised proof target (Round 7).** Prove that depth-separation is forced by the
non-simple pairwise sym-diff condition (ruling out nesting, leaving only separation
or depth-interleaving), and that min-degree-3 forces an odd-overlap bridge whenever
depth-separation holds.  The border-vertex argument: the DFS tree must have some edge
crossing between the two depth bands; a back edge from a deep vertex through this
border always achieves odd overlap if it spans far enough (forbidden-gap condition
restricts short "safe" back edges, pushing them into the crossing regime).
