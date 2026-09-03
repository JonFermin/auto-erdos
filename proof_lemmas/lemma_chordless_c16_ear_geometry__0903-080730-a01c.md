---
id: chordless_c16_ear_geometry
status: proved
depends_on: []
discharged_by_round: 65
introduced_at_round: 65
---

# Lemma `chordless_c16_ear_geometry` (proved — the spoke/ear structure of a chordless $C_{16}$)

**Setting.** $G$ cubic, $\{C_4, C_8\}$-free, $C$ a chordless
$16$-cycle in $G$, $n = |V(G)|$. Call the unique off-$C$ edge at each
$C$-vertex its *spoke* (it exists and leaves $C$ because $C$ is
chordless and $G$ is cubic), and call a vertex $u \notin C$ with
$s \ge 2$ spoke-endpoints an *$s$-ear apex*. Arc distances $d$
between spoke feet are taken in min-form, $1 \le d \le 8$.

**Claim.**

(a) $C$ has exactly $16$ spokes, all ending in $V \setminus C$.

(b) *(2-ear exclusions)* If $u$ is a $2$-ear apex with feet $x, y$ at
arc distance $d$, then the two *ear cycles* — short arc $+\ xuy$ and
long arc $+\ xuy$, of lengths $d + 2$ and $18 - d$ — are simple
cycles of $G$, so $d \in \{1, 3, 4, 5, 7, 8\}$; if $G$ has girth
$\ge 5$ then $d \in \{3, 4, 5, 7, 8\}$. A $d = 1$ apex is a triangle
sharing exactly one edge with $C$; a $d = 3$ apex certifies a
$C_{15}$ in $G$; a $d=1$ apex certifies a $C_{17}$.

(c) *(distinct feet)* Two distinct ear apexes have distinct feet
pairs (equal pairs $\{x,y\}$ give the $4$-cycle $x u y v$).

(d) *(3-ear exclusions)* If $u$ is a $3$-ear apex, its feet cut $C$
into arcs of lengths $(a, b, c)$, $a + b + c = 16$, with
$a, b, c \notin \{2, 6, 10, 14\}$ (each pair of spokes makes cycles
of lengths $g + 2$ and $18 - g$ for $g \in \{a, b, c\}$ and for the
pairwise sums $16 - g$, which give the same exclusion set).

(e) *(pigeonhole, $n \le 31$)* If $n \le 31$ then some outside
vertex is an $s$-ear apex with $s \ge 2$: $16$ spokes land in
$n - 16 \le 15$ outside vertices.

(f) *($n = 32$ dichotomy)* If $n = 32$ and no outside vertex is a
multi-spoke apex, then: the spokes form a perfect matching
$C \to V \setminus C$; every $C$-to-outside edge is a spoke, so the
outside graph $G[V \setminus C]$ is $2$-regular — a disjoint union
of cycles, each of length $\ge 3$ and $\ne 4, 8$; and every outside
edge $uv$ with feet $x, y$ at arc distance $d$ satisfies
$d \notin \{1, 5\}$ (lengths $d+3 \in \{4,8\}$), while $d = 3$
produces a **second $16$-cycle** on
$(C \setminus \{p, q\}) \cup \{u, v\}$, where $p, q$ are the two
interior vertices of the short arc (long arc, $13$ edges, $+$ the
path $x\,u\,v\,y$, $3$ edges).

**Proof.**

(a) Chordless means no $C$-vertex has its third edge inside $C$
except the two cycle edges; the third edge cannot end on $C$ (that
would be a chord), so it leaves $C$. $\square$

(b) The two arcs of $C$ between $x$ and $y$ have lengths $d$ and
$16 - d$; appending the path $x\,u\,y$ ($2$ edges, interior vertex
$u \notin C$) to either arc closes a simple cycle — lengths $d + 2$
and $18 - d$. Class exclusions: $d + 2 \in \{4, 8\}$ iff
$d \in \{2, 6\}$; $18 - d \in \{4, 8\}$ iff $d \in \{14, 10\}$,
which are $\{2, 6\}$ in min-form. Hence
$d \in \{1, 3, 4, 5, 7, 8\}$. $d = 1$ gives the $3$-cycle
$x u y$ with $xy \in C$ (its other two edges meet at $u \notin C$,
so exactly one shared edge), excluded at girth $\ge 5$; the long ear
cycle has length $17$. $d = 3$ gives ear cycles $C_5$ and
$C_{15}$. $\square$

(c) If apexes $u \ne v$ share the feet pair $\{x, y\}$ then
$x u y v x$ is a $4$-cycle ($u, v \notin C$ are nonadjacent to
themselves; all four vertices distinct). $\square$

(d) Each pair of the three spokes is a $2$-ear configuration whose
feet arc-distances (in the two directions) are $g$ and $16 - g$ with
$g \in \{a, b, c, a{+}b, b{+}c, a{+}c\}$; the pairwise sums are
$16 - c, 16 - a, 16 - b$, so the exclusion
$g \notin \{2, 6, 10, 14\}$ for the singletons already covers the
sums (the set $\{2, 6, 10, 14\}$ is invariant under
$g \mapsto 16 - g$). $\square$

(e) Immediate pigeonhole. $\square$

(f) With no multi-spoke apex the $16$ spokes have $16$ distinct
outside endpoints and $|V \setminus C| = 16$, so the spoke map is a
perfect matching. Any edge from $C$ to the outside is the third edge
of its $C$-endpoint, i.e. a spoke. Each outside vertex then has
exactly one spoke and two outside-neighbors: $G[V \setminus C]$ is
$2$-regular, and its cycles are cycles of $G$, so $\{4,8\}$-free.
For an outside edge $uv$: feet $x \ne y$ (matching), arcs $d$ and
$16 - d$, path $x\,u\,v\,y$ has $3$ edges and interior vertices
$u, v \notin C$, giving simple cycles of lengths $d + 3$ and
$19 - d$. Exclusions: $d + 3 \in \{4, 8\}$ iff $d \in \{1, 5\}$
($19 - d \ge 11$ for $d \le 8$, and $19 - d = 8$ iff $d = 11$, which
is $5$ in min-form). At $d = 3$ the long-side cycle has length
$19 - 3 = 16$: a $16$-cycle whose vertex set is
$C \setminus \{p, q\}$ plus $u, v$. $\square$

**Empirical cross-check (R65 probe, all four in-hand members).**
Chordless $C_{16}$ counts $32/112/10/15$ (pin $n{=}28$, G5 $n{=}30$,
TRI $n{=}30$, $T(\text{Petersen})$ $n{=}30$) — every one has a
multi-spoke apex (consistent with (e), and far above the pigeonhole
minimum: min $\#$multi-spoke apexes per chordless $C_{16}$ is $2$ at
$n = 30$, observed $\ge 5$ on pin, $\ge 2$ on G5, $\ge 7$ on
TRI/TP). Observed $2$-ear distances: pin
$\{3{:}58, 4{:}68, 5{:}24, 7{:}24, 8{:}6\}$, G5
$\{3{:}99, 4{:}132, 5{:}89, 7{:}72, 8{:}59\}$ — exactly the
girth-$5$ allowed set; TRI $\{1{:}62\}$, TP $\{1{:}120\}$ — the
triangle regime sits entirely on $d = 1$. Observed $3$-ear arc
triples: $(3,4,9), (4,5,7), (4,4,8), (3,5,8), (1,7,8)$ — all obey
(d). TP's chordless $C_{16}$s all have profile $(2^8)$: eight
$d{=}1$ apexes (the eight off-cycle truncation-triangle vertices),
zero singleton spokes.

**Why this matters for `share1_supply_18`.** The supply falsifier
must have EVERY $C_{16}$ chordless (`c16_chord_equiv`). This lemma
pins what such a graph must look like around each of its $C_{16}$s:
at $n \le 31$ an ear exists and its distance menu is
$\{1,3,4,5,7,8\}$ ($\{3,4,5,7,8\}$ at girth $5$); each $d = 3$ ear
manufactures a $C_{15}$, and a triangle ear on a $C_{15}$ (rather
than on $C_{16}$) would already be a $(3,15)$ share-$1$ pair — i.e.
a chorded $C_{16}$. At $n = 32$ either the ear machinery applies or
the graph decomposes as $C_{16}$ + perfect spoke matching + outside
cycle union with the $d \notin \{1,5\}$ feet law, and every $d = 3$
outside edge spawns another $C_{16}$ (which the falsifier must also
keep chordless — a strong closure pressure for the tight end).

<!-- CHECK
# CHECK 1 — parts (b)/(c)/(d)/(e) against ALL chordless C16s of the
# four in-hand class members: ear distances in the allowed set (and
# girth-5 subset on g5 members), 3-ear gaps avoid {2,6,10,14}, feet
# pairs pairwise distinct, and every chordless C16 at n<=31 has a
# multi-spoke apex. Also re-pins the chordless counts 32/112/10/15.
import itertools
from collections import deque, Counter

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def cycles16(adj, n):
    out = []
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        out.append(tuple(path))
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                if len(path) + dist[w] > 16:
                    continue
                stack.append((w, mask | (1 << w), path + [w]))
    return out

E28 = [(0,11),(0,19),(0,27),(1,17),(1,19),(1,21),(2,9),(2,13),(2,14),
       (3,22),(3,24),(3,25),(4,5),(4,7),(4,26),(5,14),(5,18),(6,7),(6,8),
       (6,20),(7,13),(8,14),(8,25),(9,17),(9,24),(10,16),(10,21),(10,27),
       (11,15),(11,16),(12,19),(12,23),(12,26),(13,18),(15,22),(15,26),
       (16,25),(17,23),(18,23),(20,21),(20,24),(22,27)]
pin = [[] for _ in range(28)]
for u, v in E28: pin[u].append(v); pin[v].append(u)
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

ALLOWED = {1, 3, 4, 5, 7, 8}
G5ALLOWED = {3, 4, 5, 7, 8}
chordless_counts = {}
ear_hist = {}
for name, adj, n, g5 in [("pin", pin, 28, True), ("G5", G5, 30, True),
                         ("TRI", TRI, 30, False), ("TP", TP, 30, False)]:
    ncl = 0
    hist = Counter()
    for path in cycles16(adj, n):
        onC = set(path); idx = {v: i for i, v in enumerate(path)}
        chord = False; feet = {}
        for i, v in enumerate(path):
            for w in adj[v]:
                if w in onC:
                    if abs(i - idx[w]) not in (1, 15): chord = True
                else:
                    feet.setdefault(w, []).append(i)
        if chord: continue
        ncl += 1
        assert sum(len(ps) for ps in feet.values()) == 16      # (a)
        multi = {w: ps for w, ps in feet.items() if len(ps) >= 2}
        assert multi, (name, path)                              # (e) n<=31
        pairs_seen = set()
        for w, ps in multi.items():
            for i, j in itertools.combinations(sorted(ps), 2):
                d = min(j - i, 16 - (j - i))
                assert d in ALLOWED, (name, d)                  # (b)
                if not g5 or d != 1: pass
                if g5: assert d in G5ALLOWED, (name, d)
            if len(ps) == 2:
                i, j = sorted(ps)
                d = min(j - i, 16 - (j - i))
                hist[d] += 1
                fp = frozenset((path[i], path[j]))
                assert fp not in pairs_seen                     # (c)
                pairs_seen.add(fp)
            elif len(ps) == 3:
                i, j, k = sorted(ps)
                gaps = (j - i, k - j, 16 - k + i)
                assert sum(gaps) == 16
                for g in gaps:
                    assert g not in {2, 6, 10, 14}, (name, gaps)  # (d)
    chordless_counts[name] = ncl
    ear_hist[name] = dict(hist)
assert chordless_counts == {"pin": 32, "G5": 112, "TRI": 10, "TP": 15}
assert ear_hist["pin"] == {3: 58, 4: 68, 5: 24, 7: 24, 8: 6}
assert ear_hist["G5"] == {3: 99, 4: 132, 5: 89, 7: 72, 8: 59}
assert ear_hist["TRI"] == {1: 62}
assert ear_hist["TP"] == {1: 120}
CHECK -->

<!-- CHECK
# CHECK 2 — constructive soundness of the ear cycles: for every 2-ear
# on every chordless C16 of TP and pin, both predicted cycles
# (lengths d+2 and 18-d) are verified to be simple cycles of the
# graph edge-by-edge, and for d=1 the triangle shares EXACTLY one
# edge with C; for d=3 the long ear cycle is a C15.
import itertools
from collections import deque

def bfs_dist(adj, n, s):
    d = [n+1]*n; d[s] = 0; q = deque([s])
    while q:
        v = q.popleft()
        for w in adj[v]:
            if d[w] > d[v] + 1:
                d[w] = d[v] + 1; q.append(w)
    return d

def cycles16(adj, n):
    out = []
    for s in range(n):
        dist = bfs_dist(adj, n, s)
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        out.append(tuple(path))
                    continue
                if w < s or (mask >> w) & 1:
                    continue
                if len(path) + dist[w] > 16:
                    continue
                stack.append((w, mask | (1 << w), path + [w]))
    return out

def is_cycle(adj, verts):
    k = len(verts)
    if len(set(verts)) != k: return False
    return all(verts[(i+1) % k] in adj[verts[i]] for i in range(k))

E28 = [(0,11),(0,19),(0,27),(1,17),(1,19),(1,21),(2,9),(2,13),(2,14),
       (3,22),(3,24),(3,25),(4,5),(4,7),(4,26),(5,14),(5,18),(6,7),(6,8),
       (6,20),(7,13),(8,14),(8,25),(9,17),(9,24),(10,16),(10,21),(10,27),
       (11,15),(11,16),(12,19),(12,23),(12,26),(13,18),(15,22),(15,26),
       (16,25),(17,23),(18,23),(20,21),(20,24),(22,27)]
pin = [[] for _ in range(28)]
for u, v in E28: pin[u].append(v); pin[v].append(u)
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

n_ears = 0
for name, adj, n in [("pin", pin, 28), ("TP", TP, 30)]:
    for path in cycles16(adj, n):
        onC = set(path); idx = {v: i for i, v in enumerate(path)}
        chord = False; feet = {}
        for i, v in enumerate(path):
            for w in adj[v]:
                if w in onC:
                    if abs(i - idx[w]) not in (1, 15): chord = True
                else:
                    feet.setdefault(w, []).append(i)
        if chord: continue
        for u, ps in feet.items():
            if len(ps) != 2: continue
            i, j = sorted(ps)
            d = min(j - i, 16 - (j - i))
            # short arc from the closer direction
            if j - i <= 16 - (j - i):
                short = list(path[i:j+1])
                long_ = list(path[j:]) + list(path[:i+1])
            else:
                short = list(path[j:]) + list(path[:i+1])
                long_ = list(path[i:j+1])
            cyc_short = short + [u]
            cyc_long = long_ + [u]
            assert is_cycle(adj, cyc_short) and len(cyc_short) == d + 2
            assert is_cycle(adj, cyc_long) and len(cyc_long) == 18 - d
            if d == 1:
                tri_edges = {frozenset(e) for e in
                             [(cyc_short[0], cyc_short[1]),
                              (cyc_short[1], cyc_short[2]),
                              (cyc_short[2], cyc_short[0])]}
                c_edges = {frozenset((path[k], path[(k+1) % 16]))
                           for k in range(16)}
                assert len(tri_edges & c_edges) == 1
            if d == 3:
                assert len(cyc_long) == 15
            n_ears += 1
assert n_ears == 58 + 68 + 24 + 24 + 6 + 120   # pin hist + TP hist
CHECK -->
