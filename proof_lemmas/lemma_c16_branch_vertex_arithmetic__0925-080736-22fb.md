---
id: c16_branch_vertex_arithmetic
status: proved
depends_on: [chordless_c16_ear_geometry, c16_dip_decomposition]
discharged_by_round: 95
introduced_at_round: 95
---

# Lemma `c16_branch_vertex_arithmetic` (Q85 branch-vertex program, layer 0)

**Setting.** $G$ cubic, $\{C_4, C_8\}$-free, $C$ a chordless $C_{16}$ in
$G$, $n = |V(G)|$ (even), $H := G - V(C)$ the outside graph, and for an
outside vertex $v$ let $s(v)$ be its spoke count (edges to $C$). The
**branch-vertex set** is $Z := \{v \in V(H) : s(v) = 0\}$, $k := |Z|$,
$t := |V(H)| - k$ the touched count. For a component $K$ of $H$ write
$q(K) = |V(K)|$, $e(K) = |E(K)|$, $\mu(K) = e(K) - q(K) + 1$ (cyclomatic
number), and $c(H)$, $\mu(H)$ for the component count and total
cyclomatic number of $H$.

**Statement.**

- **(B0)** (restatement; `c16_dip_decomposition` (c)) Every vertex of
  $C$ has exactly one spoke; hence the $16$ spoke feet are pairwise
  distinct, and $\sum_{v \in V(H)} s(v) = 16$.
- **(B1) (absorption law)** $Z$ is exactly the set of degree-$3$
  vertices of $H$. Every component $K$ of $H$ absorbs exactly
  $$\sum_{v \in K} s(v) \;=\; q(K) + 2 - 2\mu(K)$$
  spokes. Consequently $\mu(K) \le (q(K)+2)/2$ for every component, and
  summing over components,
  $$c(H) - \mu(H) \;=\; \frac{32 - n}{2},$$
  so $H$ has at least $(32-n)/2$ tree components ($\ge 4$ at $n = 24$,
  $\ge 2$ at $n = 28$, $\ge 1$ at $n = 30$). A tree component absorbs
  $q+2$ spokes; a component absorbs $0$ spokes iff $\mu = (q+2)/2$.
- **(B2) (branch-vertex cap)** $t \ge 6$ and $k \le n - 22$
  ($k \le 2$ at $n=24$, $\le 4$ at $26$, $\le 6$ at $28$, $\le 8$ at
  $30$, $\le 10$ at $32$).
- **(B3) (the $L$-menu)** Let $P$ be a path of length $L \ge 2$ between
  distinct $C$-vertices $f_1 \ne f_2$ whose interior lies in $H$, and
  let $d \in [1, 8]$ be the arc distance of $(f_1, f_2)$ on $C$. Then
  $$d \;\notin\; \{\,4 - L,\; 8 - L\,\}.$$
  Instances: $L{=}2$: $d \notin \{2,6\}$ (the
  `chordless_c16_ear_geometry` (b) 2-ear menu re-derived); $L{=}3$:
  $d \notin \{1,5\}$; $L{=}4$: $d \ne 4$; $L{=}5$: $d \ne 3$; $L{=}6$:
  $d \ne 2$; $L{=}7$: $d \ne 1$; $L \ge 8$: no exclusion — the menu is
  EXHAUSTED at $L = 8$: only the short-arc cycle can be a $C_4$/$C_8$,
  and its length $d + L$ exceeds $8$ from there on. Moreover
  $L = 16 - d$ (short-arc side) or $L = d$ (long-arc side) makes the
  path-plus-arc cycle a SECOND $C_{16}$ sharing an arc with $C$ (the
  arc-exchange creation event — not an exclusion).
- **(B4) (branch-layer instantiations)** (i) For any $H$-edge $uw$ with
  both ends touched and any feet $f_u, f_v$ of $u, w$: the feet arc
  distance avoids $\{1, 5\}$ — the outside-edge feet law of
  `chordless_c16_ear_geometry` (f), previously proved only in the
  $n = 32$ matching corner, holds for EVERY chordless $C_{16}$ at every
  $24 \le n \le 32$. (ii) For any outside vertex $v$ and touched
  $u, w \in N_H(v)$, $u \ne w$: the feet are distinct and their arc
  distance is $\ne 4$ (the dist-2 menu through $v$; the case $v \in Z$
  is the branch-vertex contact geometry).
- **(B5) ($n = 24$ classification)** At $n = 24$: $\mu(H) \le 1$,
  $k \le 1$ (strictly sharper than (B2)'s cap $2$), and if $k = 1$
  then $H$ is one of exactly three profiles:
  $$\{K_{1,3},\, K_2,\, 2K_1\}, \qquad
    \{S(2,1,1),\, 3K_1\}, \qquad
    \{C_3{+}\text{pendant},\, 4K_1\},$$
  where $S(2,1,1)$ is the 5-vertex spider with legs $2,1,1$ and
  $C_3{+}\text{pendant}$ is the triangle with one pendant edge. If
  $k = 0$, $H$ is a $4$-component forest on $8$ vertices with no
  degree-$3$ vertex, or $\{C_3, K_2, 3K_1\}$.

**Refuted radius-1 hypothesis (documented, NOT part of the claim).**
"Every $0$-spoke vertex has a touched $H$-neighbor" is FALSE. On the
in-hand corpus it fails $40/1199$ times: e.g. every chordless $C_{16}$
of $T(\text{Petersen})$ whose two unvisited triangles are joined by an
edge has both bridge endpoints at $H$-distance $2$ from the touched
set ($H[Z]$ there is two triangles plus a bridge, size-$6$ connected).
Branch-vertex analysis must therefore work at component level, not
radius $1$: $H[Z]$ components of size up to $7$ occur (TRI, $n = 30$,
$k = 7$ — one below the B2 cap $8$).

## Proof

**(B0)** $C$ chordless and $G$ cubic: each $x \in V(C)$ has two
$C$-edges and one third edge which is not a chord, hence a spoke — one
per $C$-vertex, and distinct $C$-vertices are distinct feet. There are
$16$ $C$-vertices, so $16$ spokes in total, each counted at its outside
end by $s(v)$. $\square$

**(B1)** Every outside vertex has $G$-degree $3$, split as
$\deg_H(v) + s(v) = 3$; so $s(v) = 0$ iff $\deg_H(v) = 3$, giving
$Z = \deg_3(H)$. For a component $K$:
$\sum_{v \in K} s(v) = 3q(K) - \sum_{v \in K} \deg_H(v)
= 3q(K) - 2e(K) = 3q(K) - 2(q(K) + \mu(K) - 1) = q(K) + 2 - 2\mu(K)$.
Absorption is nonnegative, so $\mu(K) \le (q(K)+2)/2$, with equality
iff $K$ absorbs $0$. Summing over the $c(H)$ components and using
(B0): $16 = (n - 16) + 2c(H) - 2\mu(H)$, i.e.
$c(H) - \mu(H) = (32-n)/2$. Each non-tree component has $\mu \ge 1$,
so $\#\{\text{tree components}\} \ge c(H) - \mu(H) = (32-n)/2$. A tree
has $\mu = 0$, absorbing $q + 2$. $\square$

**(B2)** Each touched vertex has $s(v) \le 3$, and by (B0) the $t$
touched vertices absorb all $16$ spokes: $3t \ge 16$, so $t \ge 6$
(integrality), and $k = (n - 16) - t \le n - 22$. $\square$

**(B3)** The two $f_1$–$f_2$ arcs of $C$ have lengths $d$ and $16 - d$.
$P$'s interior lies in $H$, so it is disjoint from both arcs; its
endpoints are the arcs' shared endpoints. Hence arc $\cup$ $P$ is a
simple cycle, of length $d + L$ resp. $(16 - d) + L$. The long-arc
cycle has length $(16 - d) + L \ge 8 + 2 = 10$, never a $C_4$ or
$C_8$; the short-arc cycle gives $d + L \notin \{4, 8\}$, i.e.
$d \ne 4 - L$ and $d \ne 8 - L$. If $d + L = 16$ (resp.
$(16 - d) + L = 16$, i.e. $L = d$), the corresponding cycle is a
$16$-cycle sharing the other arc with $C$ — a creation, not an
exclusion. $\square$

**(B4)(i)** Take $P = f_u, u, w, f_w$, $L = 3$: interior $\{u, w\}
\subset V(H)$, feet distinct by (B0) (two spokes at one $C$-vertex are
impossible). (B3) at $L = 3$ gives $d \notin \{1, 5\}$.
**(ii)** Take $P = f_u, u, v, w, f_w$, $L = 4$: interior
$\{u, v, w\} \subset V(H)$ has three distinct vertices ($u \ne w$
given, $v$ adjacent to both), feet distinct by (B0). (B3) at $L = 4$
gives $d \ne 4$. $\square$

**(B5)** At $n = 24$, $H$ has $8$ vertices and, by (B1),
$c(H) - \mu(H) = 4$.

*Step 1 ($\mu(H) \le 1$).* Suppose some component has $\mu \ge 2$.
A connected graph with $\mu \ge 2$ and maximum degree $\le 3$
contains either a theta subgraph $\theta(a,b,c)$ ($a \le b \le c$:
three internally disjoint paths of those lengths between two
branch vertices, order $a+b+c-1$) or two vertex-disjoint cycles
(order $\ge 3+3 = 6$; two cycles through a common vertex would
need degree $4$). In the theta case the three cycles have lengths
$a{+}b, a{+}c, b{+}c$, none equal to $4$ or $8$ in our class, and
simplicity forces $a+b \ge 3$; every triple of order $< 6$ —
$(1,2,2), (1,2,3), (1,3,3), (2,2,2)$ — contains a $C_4$, so the
theta has order $\ge 6$ (realized by $(1,2,4)$). Either way the
$\mu \ge 2$ component has $q \ge 6$, and by (B1)
$c(H) = \mu(H) + 4 \ge 6$, needing $\ge 6 + 5 \cdot 1 = 11 > 8$
vertices. Contradiction.

*Step 2 (profiles).* If $\mu(H) = 1$: $c(H) = 5$, so the unicyclic
component has $q \le 8 - 4 = 4$; its cycle has length
$\le q \le 4$ and $\ne 4$, hence a triangle, and the component is
$C_3$ ($q{=}3$, forcing the remaining profile $\{K_2, 3K_1\}$ by
$\sum q = 8$) or $C_3{+}$pendant ($q{=}4$, remaining $\{4K_1\}$).
In the first case every $H$-degree is $\le 2$, so $k = 0$; in the
second exactly the pendant-bearing triangle vertex has $H$-degree
$3$, so $k = 1$. If $\mu(H) = 0$: $H$ is a forest of exactly $4$
trees on $8$ vertices, so every tree has $q \le 5$. A subcubic tree
with two degree-$3$ vertices has $\ge 6$ vertices, so each tree
carries at most one; a tree with a degree-$3$ vertex has $q \ge 4$,
and two such trees would put $\ge 8$ vertices in $2$ of the $4$
components, leaving the other two empty — impossible. Hence
$k \le 1$. Suppose $k = 1$ and the branch-carrying tree has $q$
vertices, $q \in \{4, 5\}$. At $q = 4$ the only subcubic tree on
$4$ vertices with a degree-$3$ vertex is $K_{1,3}$, and the
remaining $4$ vertices split into $3$ nonempty trees, necessarily
sizes $(2,1,1)$: profile $\{K_{1,3}, K_2, 2K_1\}$. At $q = 5$ the
trees on $5$ vertices are $P_5$, $K_{1,4}$ (degree $4$, excluded
in a subcubic $H$), and the spider $S(2,1,1)$; only the spider has
a degree-$3$ vertex, and the remaining $3$ vertices split as
$(1,1,1)$: profile $\{S(2,1,1), 3K_1\}$. $\square$

## Probe record (falsification-first, session s_0925-080736-22fb)

Census over the $18$ in-hand members recoverable from committed CHECK
blocks (adj24; n26; pin + n28r0–r11 at $n{=}28$; g5, tri, tp at
$n{=}30$): $546$ chordless $C_{16}$s. Identities (B0)/(B1)/(B2) hold
with $0$ failures; the $L$-menu holds with $0$ violations over $4{,}534$
dist-2 instances and $29$ adjacent-pair instances, and exhaustively over
all feet-paths of length $\le 9$ (CHECK B — which also FALSIFIED the
draft's over-claimed $L \ge 9$ exclusion $d \ne L-8$ before commit:
pin realizes $(L, d) = (9, 1)$; the corrected menu stops at $L = 7$).
$k$-histogram
$\{0{:}25, 1{:}141, 2{:}188, 3{:}137, 4{:}27, 5{:}7, 6{:}19, 7{:}2\}$ —
$k = 0$ is RARE ($5\%$): the zero-free completion's hypothesis is the
exception, the branch-vertex regime the rule. The radius-1 hypothesis
fails exactly $40$ times (all in tp/tri geometry). (B5) in-hand: all
$3$ chordless $C_{16}$s of adj24 have $k = 1$ with profile
$\{K_{1,3}, K_2, 2K_1\}$ — one of the three classified shapes
realized, two still hypothetical (their feet-menu feasibility is the
natural next target).

<!-- CHECK
# CHECK A — (B0)/(B1)/(B2) identities + radius-1 refutation datum on the
# 18 in-hand members; expected chordless counts pin/g5/tri/tp = 32/112/10/15.
from collections import deque
from itertools import combinations
def to_adj(flat, n):
    nums = [int(x) for x in flat.split(",")]
    adj = [[] for _ in range(n)]
    for a, b in zip(nums[::2], nums[1::2]):
        adj[a].append(b); adj[b].append(a)
    return adj
REPS28 = [
"0,1,0,15,0,16,1,2,1,16,2,3,2,20,3,4,3,22,4,5,4,17,5,6,5,24,6,7,6,21,7,8,7,25,8,9,8,19,9,10,9,27,10,11,10,18,11,12,11,26,12,13,12,23,13,14,13,27,14,15,14,18,15,19,16,17,17,18,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,16,2,3,2,18,3,4,3,23,4,5,4,17,5,6,5,21,6,7,6,25,7,8,7,22,8,9,8,20,9,10,9,20,10,11,10,19,11,12,11,19,12,13,12,26,13,14,13,24,14,15,14,27,15,27,16,17,17,18,18,19,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,16,2,3,2,18,3,4,3,27,4,5,4,17,5,6,5,22,6,7,6,25,7,8,7,27,8,9,8,24,9,10,9,18,10,11,10,26,11,12,11,20,12,13,12,23,13,14,13,17,14,15,14,21,15,19,16,17,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,21,2,3,2,17,3,4,3,18,4,5,4,16,5,6,5,24,6,7,6,26,7,8,7,17,8,9,8,18,9,10,9,27,10,11,10,27,11,12,11,19,12,13,12,25,13,14,13,22,14,15,14,20,15,23,16,17,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,16,2,3,2,21,3,4,3,17,4,5,4,23,5,6,5,25,6,7,6,18,7,8,7,18,8,9,8,26,9,10,9,19,10,11,10,19,11,12,11,22,12,13,12,20,13,14,13,24,14,15,14,27,15,27,16,17,17,18,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,26,2,3,2,18,3,4,3,23,4,5,4,16,5,6,5,21,6,7,6,17,7,8,7,19,8,9,8,19,9,10,9,18,10,11,10,27,11,12,11,20,12,13,12,22,13,14,13,25,14,15,14,27,15,24,16,17,17,18,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,22,2,3,2,19,3,4,3,19,4,5,4,16,5,6,5,18,6,7,6,20,7,8,7,26,8,9,8,17,9,10,9,25,10,11,10,27,11,12,11,27,12,13,12,24,13,14,13,21,14,15,14,18,15,23,16,17,17,18,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,16,2,3,2,19,3,4,3,17,4,5,4,23,5,6,5,25,6,7,6,22,7,8,7,22,8,9,8,21,9,10,9,21,10,11,10,18,11,12,11,26,12,13,12,20,13,14,13,24,14,15,14,27,15,27,16,17,17,18,18,19,19,20,20,21,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,16,2,3,2,19,3,4,3,21,4,5,4,17,5,6,5,23,6,7,6,20,7,8,7,19,8,9,8,27,9,10,9,27,10,11,10,18,11,12,11,25,12,13,12,22,13,14,13,20,14,15,14,24,15,26,16,17,17,18,18,19,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,26,2,3,2,22,3,4,3,25,4,5,4,16,5,6,5,19,6,7,6,21,7,8,7,17,8,9,8,23,9,10,9,20,10,11,10,24,11,12,11,27,12,13,12,19,13,14,13,20,14,15,14,27,15,18,16,17,17,18,18,19,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,26,2,3,2,22,3,4,3,25,4,5,4,16,5,6,5,19,6,7,6,21,7,8,7,17,8,9,8,23,9,10,9,18,10,11,10,21,11,12,11,20,12,13,12,24,13,14,13,27,14,15,14,27,15,20,16,17,17,18,18,19,19,20,21,22,22,23,23,24,24,25,25,26,26,27",
"0,1,0,15,0,16,1,2,1,16,2,3,2,17,3,4,3,20,4,5,4,16,5,6,5,23,6,7,6,21,7,8,7,25,8,9,8,22,9,10,9,19,10,11,10,17,11,12,11,26,12,13,12,18,13,14,13,24,14,15,14,27,15,27,17,18,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27",
]
PIN28 = [(0,11),(0,19),(0,27),(1,17),(1,19),(1,21),(2,9),(2,13),(2,14),
(3,22),(3,24),(3,25),(4,5),(4,7),(4,26),(5,14),(5,18),(6,7),(6,8),(6,20),
(7,13),(8,14),(8,25),(9,17),(9,24),(10,16),(10,21),(10,27),(11,15),(11,16),
(12,19),(12,23),(12,26),(13,18),(15,22),(15,26),(16,25),(17,23),(18,23),
(20,21),(20,24),(22,27)]
FLAT26 = "0,1,0,15,0,16,1,2,1,16,2,3,2,17,3,4,3,17,4,5,4,16,5,6,5,18,6,7,6,18,7,8,7,23,8,9,8,20,9,10,9,24,10,11,10,17,11,12,11,21,12,13,12,19,13,14,13,22,14,15,14,22,15,25,18,19,19,20,20,21,21,22,23,24,23,25,24,25"
ADJ24 = [[8,16,21],[7,15,23],[4,16,18],[10,12,15],[2,13,18],[19,20,21],
[11,14,18],[1,10,23],[0,17,21],[13,15,22],[3,7,12],[6,14,23],[3,10,17],
[4,9,22],[6,11,20],[1,3,9],[0,2,22],[8,12,19],[2,4,6],[5,17,20],[5,14,19],
[0,5,8],[9,13,16],[1,7,11]]
G5 = [[8,28,9],[11,14,2],[9,15,1],[20,29,17],[14,21,16],[8,27,6],
      [9,22,5],[10,12,19],[5,25,0],[6,2,0],[7,16,26],[1,24,13],
      [21,7,13],[11,12,18],[4,22,1],[24,2,25],[10,29,4],[3,24,19],
      [23,13,19],[7,17,18],[3,25,26],[12,4,27],[14,6,28],[26,18,27],
      [11,15,17],[8,20,15],[23,10,20],[5,21,23],[22,29,0],[3,16,28]]
TRI = [[11,16,21],[29,18,13],[9,8,10],[21,12,9],[12,7,20],[26,8,22],
       [27,11,22],[4,20,26],[5,2,22],[2,3,10],[29,2,9],[0,27,6],
       [4,3,21],[17,29,1],[15,24,28],[14,16,25],[15,25,0],[13,23,19],
       [24,25,1],[23,17,27],[7,4,23],[3,12,0],[6,5,8],[19,17,20],
       [18,14,28],[18,16,15],[5,28,7],[11,6,19],[26,14,24],[1,13,10]]
def t_pet():
    EP = [(i,(i+1)%5) for i in range(5)] + [(i,i+5) for i in range(5)] \
         + [(5+i,5+(i+2)%5) for i in range(5)]
    adjH = [[] for _ in range(10)]
    for a, b in EP: adjH[a].append(b); adjH[b].append(a)
    TP = [[] for _ in range(30)]
    pos = {}
    for v in range(10):
        for i, w in enumerate(sorted(adjH[v])):
            pos[(v, w)] = 3*v + i
    def add(a, b): TP[a].append(b); TP[b].append(a)
    for v in range(10):
        t = [3*v, 3*v+1, 3*v+2]
        add(t[0], t[1]); add(t[1], t[2]); add(t[0], t[2])
        for w in sorted(adjH[v]):
            if v < w: add(pos[(v, w)], pos[(w, v)])
    return TP
def from_edges(E, n):
    adj = [[] for _ in range(n)]
    for u, v in E: adj[u].append(v); adj[v].append(u)
    return adj
GRAPHS = {"adj24": ADJ24, "n26": to_adj(FLAT26, 26), "pin": from_edges(PIN28, 28)}
for i, f in enumerate(REPS28):
    GRAPHS["n28r%d" % i] = to_adj(f, 28)
GRAPHS["g5"] = G5; GRAPHS["tri"] = TRI; GRAPHS["tp"] = t_pet()
def all_c16(adj, n):
    out = []
    dist = []
    for s in range(n):
        d = [n+1]*n; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        dist.append(d)
    for s in range(n):
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        out.append(tuple(path))
                    continue
                if w < s or (mask >> w) & 1: continue
                if len(path) + dist[s][w] > 16: continue
                stack.append((w, mask | (1 << w), path + [w]))
    return out
def is_chordless(adj, cyc):
    cs = set(cyc); pos = {v: i for i, v in enumerate(cyc)}
    for v in cyc:
        for w in adj[v]:
            if w in cs and abs(pos[v]-pos[w]) not in (1, 15):
                return False
    return True
k_hist = {}
radius1_fail = 0
expected_chordless = {"pin": 32, "g5": 112, "tri": 10, "tp": 15}
for name, adj in sorted(GRAPHS.items()):
    n = len(adj)
    assert all(len(a) == 3 for a in adj), name
    chordless = [c for c in all_c16(adj, n) if is_chordless(adj, c)]
    if name in expected_chordless:
        assert len(chordless) == expected_chordless[name], (name, len(chordless))
    for cyc in chordless:
        cs = set(cyc)
        outside = [v for v in range(n) if v not in cs]
        spokes = {v: [w for w in adj[v] if w in cs] for v in outside}
        # B0: exactly one spoke per C-vertex
        feet = [f for v in outside for f in spokes[v]]
        assert len(feet) == 16 and len(set(feet)) == 16, (name, "B0")
        hadj = {v: [w for w in adj[v] if w not in cs] for v in outside}
        Z = [v for v in outside if not spokes[v]]
        assert set(Z) == {v for v in outside if len(hadj[v]) == 3}, (name, "B1 Z")
        k = len(Z); k_hist[k] = k_hist.get(k, 0) + 1
        assert k <= n - 22, (name, "B2")
        seen = set(); c_cnt = 0; mu_tot = 0
        for v in outside:
            if v in seen: continue
            comp = []; qq = deque([v]); seen.add(v)
            while qq:
                x = qq.popleft(); comp.append(x)
                for w in hadj[x]:
                    if w not in seen: seen.add(w); qq.append(w)
            qn = len(comp); en = sum(len(hadj[x]) for x in comp)//2
            mu = en - qn + 1
            assert sum(len(spokes[x]) for x in comp) == qn + 2 - 2*mu, (name, "B1 absorb")
            c_cnt += 1; mu_tot += mu
        assert 2*(c_cnt - mu_tot) == 32 - n, (name, "B1 global")
        for v in Z:
            if not any(spokes[w] for w in hadj[v]):
                radius1_fail += 1
assert k_hist == {0: 25, 1: 141, 2: 188, 3: 137, 4: 27, 5: 7, 6: 19, 7: 2}, k_hist
assert radius1_fail == 40, radius1_fail  # the refutation datum is REAL
print("CHECK A ok:", sum(k_hist.values()), "chordless C16s; radius-1 fails", radius1_fail)
CHECK -->

<!-- CHECK
# CHECK B — the L-menu (B3) exhaustively for all feet-paths of length
# L <= 9 on four members spanning both regimes (pin, n26, tp, tri).
from collections import deque
def to_adj(flat, n):
    nums = [int(x) for x in flat.split(",")]
    adj = [[] for _ in range(n)]
    for a, b in zip(nums[::2], nums[1::2]):
        adj[a].append(b); adj[b].append(a)
    return adj
PIN28 = [(0,11),(0,19),(0,27),(1,17),(1,19),(1,21),(2,9),(2,13),(2,14),
(3,22),(3,24),(3,25),(4,5),(4,7),(4,26),(5,14),(5,18),(6,7),(6,8),(6,20),
(7,13),(8,14),(8,25),(9,17),(9,24),(10,16),(10,21),(10,27),(11,15),(11,16),
(12,19),(12,23),(12,26),(13,18),(15,22),(15,26),(16,25),(17,23),(18,23),
(20,21),(20,24),(22,27)]
FLAT26 = "0,1,0,15,0,16,1,2,1,16,2,3,2,17,3,4,3,17,4,5,4,16,5,6,5,18,6,7,6,18,7,8,7,23,8,9,8,20,9,10,9,24,10,11,10,17,11,12,11,21,12,13,12,19,13,14,13,22,14,15,14,22,15,25,18,19,19,20,20,21,21,22,23,24,23,25,24,25"
TRI = [[11,16,21],[29,18,13],[9,8,10],[21,12,9],[12,7,20],[26,8,22],
       [27,11,22],[4,20,26],[5,2,22],[2,3,10],[29,2,9],[0,27,6],
       [4,3,21],[17,29,1],[15,24,28],[14,16,25],[15,25,0],[13,23,19],
       [24,25,1],[23,17,27],[7,4,23],[3,12,0],[6,5,8],[19,17,20],
       [18,14,28],[18,16,15],[5,28,7],[11,6,19],[26,14,24],[1,13,10]]
def t_pet():
    EP = [(i,(i+1)%5) for i in range(5)] + [(i,i+5) for i in range(5)] \
         + [(5+i,5+(i+2)%5) for i in range(5)]
    adjH = [[] for _ in range(10)]
    for a, b in EP: adjH[a].append(b); adjH[b].append(a)
    TP = [[] for _ in range(30)]
    pos = {}
    for v in range(10):
        for i, w in enumerate(sorted(adjH[v])):
            pos[(v, w)] = 3*v + i
    def add(a, b): TP[a].append(b); TP[b].append(a)
    for v in range(10):
        t = [3*v, 3*v+1, 3*v+2]
        add(t[0], t[1]); add(t[1], t[2]); add(t[0], t[2])
        for w in sorted(adjH[v]):
            if v < w: add(pos[(v, w)], pos[(w, v)])
    return TP
def from_edges(E, n):
    adj = [[] for _ in range(n)]
    for u, v in E: adj[u].append(v); adj[v].append(u)
    return adj
GRAPHS = {"pin": from_edges(PIN28, 28), "n26": to_adj(FLAT26, 26),
          "tp": t_pet(), "tri": TRI}
def all_c16(adj, n):
    out = []
    dist = []
    for s in range(n):
        d = [n+1]*n; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        dist.append(d)
    for s in range(n):
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        out.append(tuple(path))
                    continue
                if w < s or (mask >> w) & 1: continue
                if len(path) + dist[s][w] > 16: continue
                stack.append((w, mask | (1 << w), path + [w]))
    return out
def is_chordless(adj, cyc):
    cs = set(cyc); pos = {v: i for i, v in enumerate(cyc)}
    for v in cyc:
        for w in adj[v]:
            if w in cs and abs(pos[v]-pos[w]) not in (1, 15):
                return False
    return True
MAXL = 9
tested = 0
for name, adj in sorted(GRAPHS.items()):
    n = len(adj)
    for cyc in all_c16(adj, n):
        if not is_chordless(adj, cyc): continue
        cs = set(cyc); pos = {v: i for i, v in enumerate(cyc)}
        outside = [v for v in range(n) if v not in cs]
        spokes = {v: [w for w in adj[v] if w in cs] for v in outside}
        hadj = {v: [w for w in adj[v] if w not in cs] for v in outside}
        # enumerate simple H-paths u ... w (length <= MAXL-2) between
        # touched u, w; each (feet, H-path) pair is one L-menu instance
        for u in outside:
            if not spokes[u]: continue
            stack = [(u, frozenset([u]), 0)]
            while stack:
                x, used, ln = stack.pop()
                if spokes[x] and (ln > 0 or x == u):
                    for fu in spokes[u]:
                        for fw in spokes[x]:
                            if fu == fw:
                                assert x == u and ln == 0, (name, "B0")
                                continue
                            L = ln + 2
                            dd = abs(pos[fu]-pos[fw]) % 16
                            d = min(dd, 16-dd)
                            assert d not in (4-L, 8-L), (name, L, d)
                            tested += 1
                if ln < MAXL - 2:
                    for w in hadj[x]:
                        if w not in used:
                            stack.append((w, used | frozenset([w]), ln+1))
print("CHECK B ok:", tested, "L-menu instances, zero violations")
CHECK -->

<!-- CHECK
# CHECK C — (B5) on adj24: every chordless C16 at n=24 has k <= 1, mu(H) <= 1,
# and each k=1 profile is one of the three classified shapes.
from collections import deque
ADJ24 = [[8,16,21],[7,15,23],[4,16,18],[10,12,15],[2,13,18],[19,20,21],
[11,14,18],[1,10,23],[0,17,21],[13,15,22],[3,7,12],[6,14,23],[3,10,17],
[4,9,22],[6,11,20],[1,3,9],[0,2,22],[8,12,19],[2,4,6],[5,17,20],[5,14,19],
[0,5,8],[9,13,16],[1,7,11]]
n = 24; adj = ADJ24
def all_c16(adj, n):
    out = []; dist = []
    for s in range(n):
        d = [n+1]*n; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        dist.append(d)
    for s in range(n):
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        out.append(tuple(path))
                    continue
                if w < s or (mask >> w) & 1: continue
                if len(path) + dist[s][w] > 16: continue
                stack.append((w, mask | (1 << w), path + [w]))
    return out
def is_chordless(adj, cyc):
    cs = set(cyc); pos = {v: i for i, v in enumerate(cyc)}
    for v in cyc:
        for w in adj[v]:
            if w in cs and abs(pos[v]-pos[w]) not in (1, 15):
                return False
    return True
# the three classified k=1 profiles as (q, mu, sorted H-degree seq) multisets
STAR    = sorted([(4,0,(1,1,1,3)), (2,0,(1,1)), (1,0,(0,)), (1,0,(0,))])
SPIDER  = sorted([(5,0,(1,1,1,2,3)), (1,0,(0,)), (1,0,(0,)), (1,0,(0,))])
TRIPEND = sorted([(4,1,(1,2,2,3)), (1,0,(0,)), (1,0,(0,)), (1,0,(0,)), (1,0,(0,))])
count = 0; realized = set()
for cyc in all_c16(adj, n):
    if not is_chordless(adj, cyc): continue
    count += 1
    cs = set(cyc)
    outside = [v for v in range(n) if v not in cs]
    hadj = {v: [w for w in adj[v] if w not in cs] for v in outside}
    k = sum(1 for v in outside if len(hadj[v]) == 3)
    assert k <= 1, (cyc, k)
    seen = set(); prof = []; mu_tot = 0
    for v in outside:
        if v in seen: continue
        comp = []; q = deque([v]); seen.add(v)
        while q:
            x = q.popleft(); comp.append(x)
            for w in hadj[x]:
                if w not in seen: seen.add(w); q.append(w)
        qn = len(comp); en = sum(len(hadj[x]) for x in comp)//2
        mu = en - qn + 1; mu_tot += mu
        prof.append((qn, mu, tuple(sorted(len(hadj[x]) for x in comp))))
    assert mu_tot <= 1, (cyc, mu_tot)
    if k == 1:
        p = sorted(prof)
        assert p in (STAR, SPIDER, TRIPEND), p
        realized.add(("STAR", "SPIDER", "TRIPEND")[(STAR, SPIDER, TRIPEND).index(p)])
assert count == 3, count
assert realized == {"STAR"}, realized
print("CHECK C ok: adj24 has 3 chordless C16s, all k=1, all profile K13+K2+2K1")
CHECK -->
