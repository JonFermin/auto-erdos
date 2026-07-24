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

## Section 5 — Q8 resolution summary

**Q8 is resolved**: no witness exists in the screened families — the
I-graph/GP/dumbbell arm is cleared at all sizes by Lemma
`igraph_c4_or_c8`, and the theta/$K_4$ arm is cleared throughout the
witness window by Lemma `lift_screen_window`. The counterexample hunt,
if resumed, must move outside these lift families (girth-biased random
cubic graphs, cages, snark-like families) or to the large-$m$
theta-lift question above. Ideation losers (Hashimoto trace compression,
dyadic-window cycle-spectrum sieve, minimal-counterexample stability
stack) must not be re-proposed without new input.

## Section 6 — Q9: DFS depth-chain discharging

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

**Next steps for Q9.** (1) Exhaustive $n=7$ (236,926 graphs) in a
dedicated offline run — the stride-5 coverage is very strong evidence but
not a proof. (2) Prove the girth-6 sym-diff mechanism: show that for every
cubic girth-$\ge 5$ graph there exist two back edges in some DFS tree whose
gap-difference or sum lands on a power-of-2 minus 2. (3) Bridge to
min-degree-3 (not just cubic): extend the DFS leaf argument to
non-regular graphs.
