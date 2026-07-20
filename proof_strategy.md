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

## Section 5 — Current open state (after Q8)

- **Q8 is resolved**: no witness exists in the screened families — the
  I-graph/GP/dumbbell arm is cleared at all sizes by Lemma
  `igraph_c4_or_c8`, and the theta/$K_4$ arm is cleared throughout the
  witness window by Lemma `lift_screen_window`. The counterexample hunt,
  if resumed, must move outside these lift families (girth-biased random
  cubic graphs, cages, snark-like families) or to the large-$m$
  theta-lift question above.
- Ideation losers (Hashimoto trace compression, dyadic-window
  cycle-spectrum sieve, minimal-counterexample stability stack) must not be
  re-proposed without new input; the notes channel records why each died.
- Minimal open statement: the conjecture itself, with the search space for
  a hypothetical counterexample narrowed by F1–F3 and, from this session,
  by the I-graph clearance (all sizes) and the theta/$K_4$ window screen.

## Section 6 — Q9: DFS depth-chain discharging (in progress)

**Strategy.** A DFS tree $T$ of a min-degree-3 graph $G$ decomposes all
edges into tree edges and back edges. A back edge from $v$ to ancestor $w$
has depth-gap $d = \mathrm{dep}(v) - \mathrm{dep}(w) \ge 2$, yielding a
fundamental cycle of length $d+1$.

Key observation: in a DFS of a cubic graph, every DFS leaf carries exactly
two back edges (degree 3 minus one parent tree-edge). If their gaps are
$d_1 < d_2$:
- $d_i + 1 \in \{4,8,16,\ldots\}$ iff $d_i \in \{3,7,15,\ldots\}$:
  fundamental cycle witnesses the conjecture.
- $(d_2 - d_1) + 2 \in \{4,8,16,\ldots\}$ iff $d_2 - d_1 \in \{2,6,14,\ldots\}$:
  nested symmetric difference of the two fundamental cycles is a
  power-of-2 simple cycle.

**Lemma `dfs_chain_locality`** (status: open, see
`proof_lemmas/lemma_dfs_chain_locality.md`): for every connected
min-degree-3 graph on $\le 12$ vertices, SOME DFS ordering has at least
one vertex whose back-edge profile triggers the above detection. Two CHECK
blocks in the lemma file provide computational support:
- CHECK 1 (passed): all 27 cubic graphs on $n \le 10$ have C4/C8 and SOME
  DFS ordering detects via gap/gap-diff analysis.
- CHECK 2 (passed): adversarial DFS sampling (3000 random orderings) on the
  Petersen graph (unique girth-5 cubic graph on $n \le 10$) finds no ordering
  that avoids detection.

**Key structural finding: girth constrains valid gap-differences.** For a
graph of girth $g$, any nested symmetric difference of two fundamental cycles
from the same DFS vertex is a simple cycle of length $d_2-d_1+2 \ge g$.
Therefore $d_2-d_1 \ge g-2$.

- **Girth 4 graphs**: C4 detected immediately as a fundamental cycle (gap 3).
- **Girth 5 graphs** (like the Petersen graph, $n=10$): pairwise diff must
  be $\ge 3$; the first detecting diff is 6, requiring $d_2 \ge d_1+6 \ge 10$.
  For $n \le 10$, $d_2 \le 9$, so **pairwise detection is impossible** for
  girth-5 graphs on $n \le 10$. Detection must come from a gap-7 back edge
  (C8 as fundamental cycle). The CHECK 2 adversarial sampling (3000 tries)
  finds gap-7 in every DFS ordering tried on the Petersen graph.

**CHECK 3 kill (2026-07-20): universal claim falsified; existential claim stands.**
Adversarial DFS sampling (5000 orderings per graph) on all 27 cubic graphs on
$n \le 10$ found non-detecting orderings for 14 graphs (girth 3 and 4). The
universal claim ("any DFS tree detects") is FALSE. The Petersen graph (girth 5)
is the sole case with no adversarial ordering found.

The EXISTENTIAL claim (SOME DFS tree detects for every cubic graph on $\le 10$
vertices) is supported by CHECK 1 + the failure of the adversarial search to
kill the Petersen graph.

**Redirected proof strategy for Q9:**
- Abandon "any DFS tree detects"; pursue "CANONICAL DFS always detects."
- A candidate canonical rule: DFS from the vertex of minimum eccentricity
  (center of the graph), breaking ties by maximum degree, exploring neighbors
  in depth-increasing order. Under this rule, girth-constraint forces short
  cycles to appear as fundamental cycles and long-path DFS ensures high-gap
  back edges for girth-5 graphs.
- Key sub-claim to verify: the depth-maximizing DFS always places the
  graph's shortest power-of-2 cycle as a fundamental cycle (or pairwise
  sym-diff). CHECK for this canonical rule on all 27 cubic graphs is the
  next logical step.
