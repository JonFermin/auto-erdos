---
id: lift_screen_window
status: proved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma: no theta/dumbbell/$K_4$ voltage lift in the witness window is an Erdős–Gyárfás witness

**Statement** (finite, machine-checked computational fact). Every graph in
the following three families contains a simple cycle of length $4$, $8$,
or $16$:

1. **Theta lifts** $\Theta_m(0, a_2, a_3)$: vertices $(x, j)$,
   $x \in \{0,1\}$, $j \in \mathbb{Z}_m$; edges $(0,j) \sim (1, j + a_t)$
   for each voltage $a_t \in \{0, a_2, a_3\}$; $m \in [15, 32]$,
   $0 < a_2 < a_3 < m$ (voltages pairwise distinct so the lift is
   simple); 4,596 lifts.
2. **Dumbbell lifts = I-graphs** $I(m,a,b)$, $m \in [15,32]$, simple and
   cubic: 1,248 lifts. (Cleared at ALL sizes, not just the window, by
   Lemma `igraph_c4_or_c8`.)
3. **$K_4$ lifts**: base $K_4$ with spanning-tree edges
   $(0,1),(0,2),(0,3)$ at voltage $0$ and co-tree edges
   $(1,2),(1,3),(2,3)$ at voltages $a,b,c \in \mathbb{Z}_m$;
   $m \in [8, 16]$; all $m^3$ assignments per $m$; 17,712 lifts.

In total 23,556 lifts were screened with the same per-length exhaustive
DFS the witness verifier uses (`library.erdos_gyarfas_witness`,
node-expansion budget 80M per length, lengths $4, 8, 16, 32, 64$ in
increasing order with short-circuit). Outcome:

- every graph produced a power-of-2 cycle at length $\le 16$
  (first-hit histogram: theta 864/2,526/1,206 at 4/8/16; I-graph
  248/1,000 at 4/8; $K_4$ 3,758/6,994/6,960 at 4/8/16);
- zero survivors. Budget exhaustion was tracked per (graph, length) pair
  and recorded as "inconclusive", never as a pass; the inconclusive
  count was zero, so every search that ran is an exhaustive certificate
  for its (graph, length) pair. The CHECK block below re-derives the
  claim on a deterministic slice with a complete, budget-free DFS, so
  the slice cannot silently miss a cycle.

Hence no member of these families within the $\le 64$-vertex witness cap
is an Erdős–Gyárfás witness, and the Q8 counterexample arm over these
families is closed.

**Why these were the right families.** The witness box (F1+F2+F3 of the
spec) demands 30–64 vertices and near-cubic regularity; $\mathbb{Z}_m$
lifts of the three smallest cubic multigraph bases tile that box with
highly structured, girth-biased candidates while keeping the search
exhaustive per instance.

**Scope caution.** This lemma certifies a finite window only. It says
nothing about theta or $K_4$ lifts with more than 64 vertices (see
Section 4 of `proof_strategy.md` for the large-$m$ theta observation),
and nothing about cubic graphs outside these lift families.

**Re-derivation note.** The lemma's content is an exhaustive fixed-length
cycle search over tens of thousands of graphs; it cannot be re-derived by
a one-line sandbox expression (graph construction plus DFS exceed the
math-and-basic-builtins budget). The deterministic CHECK block below IS
the re-derivation path: it re-screens a slice (all simple theta lifts for
$m \in \{19, 31\}$ and all $K_4$ lifts for $m = 13$ — 2,785 graphs) with
a self-contained complete DFS and fails loudly on any survivor.

<!-- CHECK
# Falsification probe: re-screen a deterministic slice of the window with
# a self-contained stdlib search. Slice = all simple theta lifts for
# m in {19, 31} (prime moduli — the ones with the largest C16 tails) and
# all K4 lifts for m = 13 (prime). The lemma claims every one of these
# contains a C4, C8, or C16; a single survivor falsifies it.
import sys
sys.setrecursionlimit(100)

def has_cycle_len(adj, L):
    n = len(adj)
    def dfs(s, v, depth, used):
        if depth == L:
            return s in adj[v]
        for w in adj[v]:
            if w > s and not (used >> w) & 1:
                if dfs(s, w, depth + 1, used | (1 << w)):
                    return True
        return False
    return any(dfs(s, s, 1, 1 << s) for s in range(n))

def theta_adj(m, a2, a3):
    adj = [set() for _ in range(2 * m)]
    for j in range(m):
        for a in (0, a2, a3):
            u, v = j, m + (j + a) % m
            adj[u].add(v); adj[v].add(u)
    return [sorted(s) for s in adj]

def k4_adj(m, a, b, c):
    adj = [set() for _ in range(4 * m)]
    for j in range(m):
        for (x, y, g) in ((0,1,0),(0,2,0),(0,3,0),(1,2,a),(1,3,b),(2,3,c)):
            u, v = x * m + j, y * m + (j + g) % m
            adj[u].add(v); adj[v].add(u)
    return [sorted(s) for s in adj]

def dies_by_16(adj):
    return has_cycle_len(adj, 4) or has_cycle_len(adj, 8) or has_cycle_len(adj, 16)

for m in (19, 31):
    for a2 in range(1, m):
        for a3 in range(a2 + 1, m):
            adj = theta_adj(m, a2, a3)
            assert all(len(x) == 3 for x in adj), (m, a2, a3)
            assert dies_by_16(adj), f"theta({m},{a2},{a3}) survives C4/C8/C16 — lemma falsified"

m = 13
for a in range(m):
    for b in range(m):
        for c in range(m):
            adj = k4_adj(m, a, b, c)
            if any(len(x) != 3 for x in adj):
                continue
            assert dies_by_16(adj), f"K4 lift m=13 ({a},{b},{c}) survives C4/C8/C16 — lemma falsified"
CHECK -->
