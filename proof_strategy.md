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

**Formal proof progress (Lemma `chain_locality_sketch`).**
The formal proof sketch closes the cases $n \le 8$:
- $n \le 8$, $\delta \ge 3$: girth $\le 4$ (proved — no 3-regular girth-5 graph has
  $n \le 9$, and the Petersen graph is the unique cubic girth-5 graph with $n=10$);
  hence some fundamental cycle has length 4 directly.
- $n = 10$ cubic, girth 5 (Petersen graph): all 30 tested spanning trees yield
  a triple sym-diff of pow-2 length; the Petersen graph has only odd-length cycles,
  so pairwise sym-diffs are always even, and the triple case is needed for some trees.
- Remaining gap: $n \in \{9, 10\}$ non-cubic min-degree-3 graphs with $\delta \ge 4$
  (these are denser and expected to trivially contain $C_4$ or $C_8$).

**Next steps for Q9.**
1. Close the remaining case ($n \in \{9,10\}$, $\delta \ge 4$ min-degree-3 graphs)
   by verifying exhaustively that they all contain a direct pow-2 cycle or short
   sym-diff. These graphs have higher $\delta$ and hence more cycles, making the
   case easier than the cubic case.
2. Attempt a formal proof of the cubic full-window case (`chain_locality_full_window`):
   for cubic $G$ on $n \le 64$, the cycle space dimension is $\ell = n/2+1 \in [7,33]$;
   show that no multiset of fundamental-cycle lengths avoids all pow-2 values
   at triple order. A SAT/ILP encoding over $(n, \ell, \text{length multiset})$
   is the recommended route.
3. Redirect Q9 to the theta-lift voltage-relation obstruction:
   NOTE — computational check shows many $(m, a_2, a_3)$ pairs with $m \le 60$
   have NO short pow-2 relation, so the simple voltage argument does NOT prove the
   conjecture for all theta lifts. The theta-lift route requires a more subtle
   argument (e.g., voltage sequences that realize a non-simple sym-diff, not just
   linear relations). Deprioritize this direction.
