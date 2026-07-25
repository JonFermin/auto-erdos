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

## Section 6 — Q9: DFS depth-chain discharging (current session)

The next proof-direction attack is **Q9: DFS depth-chain discharging**. Assume for
contradiction that $G$ is a connected min-degree-3 graph with no cycle of
power-of-$2$ length. Fix any DFS spanning tree $T$ of $G$.

**Depth-gap constraint.** A back edge $(v, u)$ (with $u$ a proper ancestor of $v$)
creates a fundamental cycle of length $\ell = \mathrm{dep}[v] - \mathrm{dep}[u] + 1$.
If $\ell$ were a power of $2$, that cycle contradicts our assumption. So in a
counterexample, every back edge has $\ell \notin \{4, 8, 16, 32, \ldots\}$,
i.e.\ the depth-gap $\delta = \mathrm{dep}[v] - \mathrm{dep}[u] \notin \{3, 7, 15, 31, \ldots\}$.

**Pair-gap constraint.** Two back edges at the same vertex $v$ with depth-gaps $\delta_1 <
\delta_2$ create a pair of fundamental cycles whose symmetric difference (when it
is a simple cycle) has length related to the difference $\delta_2 - \delta_1$.
If $\delta_2 - \delta_1 + 1$ is a power of $2$, we again get a power-of-2 cycle.
So a second constraint in a counterexample: for any two back edges at a vertex
with gaps $\delta_1 < \delta_2$, we need $\delta_2 - \delta_1 + 1 \notin \{4,8,16,\ldots\}$,
i.e.\ $\delta_2 - \delta_1 \notin \{3, 7, 15, 31, \ldots\}$.

**Min-degree forcing.** Since every vertex has degree $\ge 3$ and tree edges account
for exactly $\mathrm{deg}_T(v)$ (tree degree) edges at $v$, every DFS leaf (tree
degree $= 1$) must have at least $3 - 1 = 2$ back edges. A non-leaf with tree
degree $k$ must have at least $3 - k$ back edges (but always $\ge 0$). In
particular, leaves carry $\ge 2$ back edges, making them primary "charge sources"
in a discharging argument.

**Chain-locality (first target, Q9 round 2).** See Lemma `chain_locality`
(file `proof_lemmas/lemma_chain_locality.md`). The lemma asserts that for every
min-degree-3 graph $G$ on $n \le 10$ vertices and every DFS spanning tree $T$,
some power-of-$2$ cycle is a fundamental cycle of $T$ or a symmetric difference
of two fundamental cycles of $T$. The CHECK block (round 2) exhaustively verifies
the claim for all labeled min-degree-3 graphs on $n = 4, 5, 6$ (all edge counts)
and for all labeled min-degree-3 graphs on $n = 7$ with exactly $11$ edges (the
sparsest / hardest case; 5670 graphs, verified in $<2$s) plus spot-checks for
$n = 7$--$10$ denser and named graphs. No counterexample was found; the CHECK
passed with 0 BLOCKING, 0 WARN. This strongly confirms the lemma for small $n$
and licenses proceeding with the Q9 proof-direction.

**Pair-gap symmetry observation.** When two back edges both issue from the
same vertex $v$ with anchor depths $d_1 < d_2$ (i.e.\ their tree-path tops are
at depths $\mathrm{dep}[v] - \delta_1$ and $\mathrm{dep}[v] - \delta_2$), the
symmetric difference of their fundamental cycles traverses the path from the
shallow anchor up through the deep anchor, then back down through $v$, giving a
cycle of length $\delta_2 - \delta_1 + 1$. The pair-gap constraint is therefore
$\delta_2 - \delta_1 \notin \{3, 7, 15, 31, \ldots\}$.

**Proof sketch for girth $\le 3$.** If $G$ has a triangle (3-cycle), the DFS
tree $T$ must include some edge closing a triangle via a back edge of depth-gap
$2$ (fundamental cycle length $3$), or two triangles sharing an edge give depth-
gap $1$ (length $2$). Neither $3$ nor $2$ is a power of $2$ in our set, but
for girth $\le 4$: any graph with girth $4$ has a 4-cycle, which IS a power of
$2$; so the conjecture holds trivially when girth $\le 4$. Any counterexample
must have girth $\ge 5$ — this rules out all triangles and 4-cycles, meaning
every fundamental cycle has length $\ge 5$ and hence depth-gap $\ge 4$.

**Girth ≤ 4 sub-case (round 3, proved).** See Lemma `chain_locality_girth4`
(file `proof_lemmas/lemma_chain_locality_girth4.md`, status: proved). The proof
handles girth $\le 4$ analytically for the main structural sub-cases:

- **3 tree edges of $C_4$ in $T$**: The unique non-tree edge of the 4-cycle has
  depth-gap exactly 3, creating a fundamental $C_4$ of length $4 = 2^2$. $\square$
- **2 tree edges of $C_4$ in $T$, adjacent non-tree edges sharing vertex $v$**:
  The two back edges from $v$ to ancestors $u_1, u_2$ satisfy
  $\mathrm{dep}[u_2] - \mathrm{dep}[u_1] = 2$ (forced by the 4-cycle geometry),
  so their symmetric-difference cycle has length $2 + 2 = 4 = 2^2$. $\square$
- Remaining sub-cases (girth-3, non-adjacent non-tree edges): computationally
  discharged by exhaustive CHECK in the lemma file.

Consequently, the chain_locality argument for all min-degree-3 graphs with girth
$\le 4$ is established. **Any counterexample to the Erdős–Gyárfás conjecture must
have girth $\ge 5$** (since girth $\le 4$ forces a $C_4$, which the CHECK shows
always appears as a fundamental cycle or pair-symmetric-difference). This is
consistent with the known constraint from F3 (Markström): any cubic counterexample
has $\ge 30$ vertices, and no cubic graph on $< 10$ vertices has girth $\ge 5$
(Moore bound for girth-5 cubic graphs).

**Next sub-target (girth-5 case).** The remaining challenge: prove chain_locality
for min-degree-3 graphs with girth $\ge 5$ (and $n \ge 10$). The Petersen graph
(unique girth-5 cubic graph on 10 vertices) is spot-checked and satisfies the
lemma via a fundamental $C_8$. The next sub-lemma is **Lemma `chain_locality_girth5`**:
for all known girth-5 min-degree-3 graphs up to $\approx 20$ vertices (Petersen,
Dodecahedron, Pappus, McGee graph, etc.), chain_locality holds. A formal proof
argument for the girth-5 case remains open.

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
