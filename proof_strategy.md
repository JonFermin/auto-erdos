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
- **Q9 is in progress** (DFS depth-chain discharging; see Section 6).
- Minimal open statement: the conjecture itself, with the search space for
  a hypothetical counterexample narrowed by F1–F3 and, from Q8, by the
  I-graph clearance (all sizes) and the theta/$K_4$ window screen.

## Section 6 — DFS depth-chain discharging (Q9)

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

**Chain-locality lemma (computationally established; formal proof open).**
For $n \le 10$, Lemma `chain_locality` shows that the first three
levels of the $\mathbb{F}_2$ cycle space always see a power-of-2 cycle:
some fundamental cycle, or pairwise, or triple symmetric difference of
fundamental cycles forms a simple $C_{2^k}$. The pairwise version fails
for some 3-regular 10-vertex graphs (discovered computationally this
session); the triple version holds for all 13,940 tested $(G, T)$ pairs.

**Extended chain-locality for cubic graphs (Lemma `chain_locality_extended`).**
The triple-sym-diff sufficiency extends to cubic (3-regular) graphs through
$n = 24$. Across 350 cubic graphs and 6,650 $(G, T)$ pairs (12 vertices
through 24 vertices, seed-42 random 3-regular graphs), zero triple
failures were found. Pairwise failures
occur at $n = 10$ and $n = 14$ but are always rescued by some triple.
This is consistent with Markström's bound: any cubic counterexample has
$n \ge 30$, so the chain-locality obstruction (triple sym-diffs always
produce a pow-2 cycle) rules out the cubic counterexample region up to at
least $n = 24$. The first untested cubic sizes are $n \ge 26$.

**Consequence for Q9.** The chain-locality lemmas show that the DFS
approach cannot rule out power-of-2 cycles for cubic $G$ with $n \le 24$
purely via back-edge forbidden sets; those graphs already have detectable
pow-2 cycles in their cycle-space span (within triple order). For the
discharging argument to work for $n \ge 25$, the depth-gap constraints
must force a contradiction through a *global* invariant (ancestor-chain
charge absorption) rather than local cycle detection. The gap between
the chain-locality coverage ($n \le 24$) and Markström's lower bound
($n \ge 30$) for cubic counterexamples — a window of $n \in [25,29]$
— is the next target for extending the computational check.

**Next steps for Q9.**
1. Extend the chain-locality check to cubic $n \in [26, 32]$ to close
   the gap with Markström's bound; if zero triple failures persist through
   $n = 32$, the triple sym-diff obstruction covers the full cubic witness
   window (vertex cap 64 means a cubic counterexample has $n \le 64$).
2. Formalize the triple chain-locality lemma for $n \le 10$ (all
   min-degree-3 graphs, not just cubic) — the formal proof is still open.
3. OR redirect Q9 to the theta-lift voltage-relation obstruction (noted
   in Section 4): prove that for all $(m, a_2, a_3)$, some pow-2-length
   relation $\alpha a_2 + \beta a_3 \equiv 0 \pmod{m}$ with
   $|\alpha|,|\beta| \le m/2$ is unavoidable.
