---
id: c16_dip_decomposition
status: proved
depends_on: [c16_menu_dist2_supply, chordless_c16_ear_geometry]
discharged_by_round: 82
introduced_at_round: 82
---

# Lemma `c16_dip_decomposition` (proved — the completion calculus at a dist-2 landing; chordedness is FREE at $d = 1$)

**Setting.** $G$ a connected cubic $\{C_4, C_8\}$-free graph on
$24 \le n \le 30$ vertices, $C$ a chordless $16$-cycle, $v$ a
$0$-spoke outside vertex at $\mathrm{dist}(v, C) = 2$ with
$\tau(v) \ge 2$, and $(f_1, u_1, v, u_2, f_2)$ a legal landing
(distinct T-neighbours $u_1 \ne u_2$ of $v$, feet
$f_1 \in \mathrm{feet}(u_1)$, $f_2 \in \mathrm{feet}(u_2)$; by
`c16_menu_dist2_supply` (a)–(b) all such landings have $f_1 \ne f_2$
and $d := \mathrm{dist}_C(f_1, f_2) \ne 4$). Let $P$ be ANY
$f_2 \to f_1$ path of length $12$ in $G - \{u_1, v, u_2\}$, and let
$C' := f_1 u_1 v u_2 f_2 \cdot P$ be the resulting closed $16$-walk.

**Statement (proved).**

(a) **Cycle for free.** $C'$ is always a $16$-cycle on $16$ distinct
vertices: the interior of $P$ avoids $u_1, v, u_2$ (they are deleted),
avoids $f_2$ and $f_1$ (path endpoints of a simple path), and the
branch path has no other vertices.

(b) **Arc decomposition.** Every edge of $P$ with both endpoints on
$C$ is an edge of $C$ (chordlessness of $C$), so $P \cap C$ is a
disjoint union of subarcs of $C$ and $P$ alternates
$\mathrm{arc}_0 \cdot \mathrm{seg}_1 \cdot \mathrm{arc}_1 \cdots
\mathrm{seg}_k \cdot \mathrm{arc}_k$ with arcs possibly single
vertices (zero edges) and segments entirely off $C$.

(c) **Arc-sharing is automatic.** The branch path's edges
($f_1 u_1$, $u_1 v$, $v u_2$, $u_2 f_2$ — spokes and outside edges)
are never $C$-edges, so
$E(C') \cap E(C) = \{C\text{-edges used by } P\}$. And $P$ MUST use
$C$-edges — its first and last edges are $C$-edges: a chordless
$16$-cycle in a cubic graph gives every $C$-vertex exactly ONE
off-$C$ neighbour (its spoke), and the spokes of $f_2$ and $f_1$
are precisely $u_2$ and $u_1$ — both deleted. So $P$ can only leave
$f_2$ (and only enter $f_1$) along $C$; $\mathrm{arc}_0$ and
$\mathrm{arc}_k$ of (b) each have length $\ge 1$, and EVERY
completion path yields an arc-sharing $C'$, at every $d$ and every
$n$. The `noshare` validity test is vacuous.

(d) **No pure arc.** $P$ cannot lie entirely on $C$: that requires
$12 \in \{d, 16 - d\}$, i.e. $d = 4$, which legality excludes. So
every completion has $k \ge 1$ off-$C$ segments — re-deriving the
single-arc exclusion of `c16_two_route_menu` (optimality 2) in this
calculus.

(e) **Chordedness is free at $d = 1$.** If $d = 1$ and $C'$ is
arc-sharing, then $C'$ is automatically chorded: $f_1 f_2$ is an
edge of $G$ (a $C$-edge, $d = 1$), both endpoints lie on $C'$, and
it is NOT an edge of $C'$ — the $C'$-neighbours of $f_1$ are $u_1$
and the penultimate vertex of $P$, which is not $f_2$ because
$|P| = 12 > 1$. Hence $f_1 f_2$ is a chord of $C'$.

**Corollary (the $d = 1$ reduction).** At a legal landing with
$d = 1$, a completion witness exists iff $G - \{u_1, v, u_2\}$
contains ANY $f_2 \to f_1$ path of length $12$: every validity
condition — distinct vertices, arc-sharing, chordedness — is
automatic by (a), (c), (e). The negation of
`c16_landing_universal` at $d = 1$ is therefore a bare
path-existence statement about the deleted graph — the cleanest
possible blob-kill target. (The same start/end-on-$C$ rigidity
holds for the $\tau = 1$ branch paths of Section 121: there the
deleted route end $y$ is $f_2$'s spoke.)

(f) **Single-dip arithmetic.** If $k = 1$ and both arcs of (b) run
along the long ($16 - d$)-arc, with the segment of length $s$
attached at long-arc positions $a < b$ (measured from $f_2$), then
$|P| = (16 - d) - (b - a) + s$, so $|P| = 12$ iff
$b - a = s + 4 - d$. (For the $\tau = 1$ row, branch length $5$,
completion length $11$, the same computation gives $b - a = s + 5 - d$
— at $d = 1$ this is the $b - a = s + 4$ criterion whose failure
Section 121 mined in the two R80 counterexamples.)

**Corpus census (probe record, R82).** Exhaustive over all
$\tau \ge 2$ landings of the deterministic corpus: at $d = 1$, ALL
$18{,}325$ length-$12$ paths are valid witnesses (zero failures of
any kind — as (a)+(c)+(e) predict); at $d \ge 2$, of $216{,}832$ length-$12$ paths
$196{,}128$ are valid and $20{,}704$ fail ($5{,}027$ at $n \le 28$,
$15{,}677$ at $n = 30$), ALL by chordlessness alone — `not16` and
`noshare` never occur anywhere.
So chordedness at $d \ge 2$ ($\sim 9.5\%$ of paths) is the ONLY
nontrivial validity condition left in the dist-2 closure question.

<!-- CHECK
# CHECK 1 - decomposition consequences on the n<=28 subcorpus (n24, n26,
# REPS28[0..5], PIN28): for EVERY tau>=2 landing and EVERY f2->f1 path of
# length 12 avoiding {u1,v,u2}: the closed walk has 16 distinct vertices
# (a); its first and last edges are C-edges and it shares an arc (c); and
# at d=1 it is chorded (e) - the only failure mode anywhere is
# chordlessness at d>=2. ~5s.
from collections import deque
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
def all_c16(adj):
    n = len(adj); out = []
    for s in range(n):
        d = [n+1]*n; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        es = frozenset(frozenset(e) for e in zip(path, path[1:]+path[:1]))
                        out.append((frozenset(path), es, tuple(path)))
                    continue
                if w < s or (mask >> w) & 1: continue
                if len(path) + d[w] > 16: continue
                stack.append((w, mask | (1 << w), path+[w]))
    return out
def dist_to(adj, v, S):
    d = {v: 0}; q = deque([v])
    while q:
        u = q.popleft()
        if u in S: return d[u]
        for w in adj[u]:
            if w not in d: d[w] = d[u]+1; q.append(w)
    return 99
def arc_dist(pathC, a, b):
    g = abs(pathC.index(a) - pathC.index(b)) % 16
    return min(g, 16 - g)
graphs = [ADJ24, to_adj(FLAT26, 26)] + [to_adj(f, 28) for f in REPS28]
gp = [[] for _ in range(28)]
for a, b in PIN28: gp[a].append(b); gp[b].append(a)
graphs.append(gp)
n_ok = n_nochord = 0
for adj in graphs:
    n = len(adj)
    cs = all_c16(adj)
    chl = []
    for vs, es, path in cs:
        ch = False
        for a in path:
            for b in adj[a]:
                if b in vs and frozenset((a, b)) not in es: ch = True
        if not ch: chl.append((vs, es, path))
    for vsC, esC, pathC in chl:
        interior = [w for w in range(n) if w not in vsC
                    and not any(t in vsC for t in adj[w])]
        for v in interior:
            if dist_to(adj, v, vsC) != 2: continue
            tn = [(w, [f for f in adj[w] if f in vsC]) for w in adj[v]]
            tn = [(w, F) for w, F in tn if F]
            if len(tn) < 2: continue
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    u1, F1 = tn[a]; u2, F2 = tn[b]
                    for f1 in F1:
                        for f2 in F2:
                            d = arc_dist(pathC, f1, f2)
                            seg = [f1, u1, v, u2, f2]
                            banned = {u1, v, u2}
                            stack = [(f2, [f2], False)]
                            while stack:
                                cur, path, usedC = stack.pop()
                                for w in adj[cur]:
                                    e_onC = frozenset((cur, w)) in esC
                                    if w == f1:
                                        if len(path) == 12:
                                            uc = usedC or e_onC
                                            assert uc, ("C-edge-free path", n, v, f1, f2)
                                            assert frozenset((path[0], path[1])) in esC, \
                                                ("first edge off C", n, v, f1, f2)
                                            assert e_onC, ("last edge off C", n, v, f1, f2)
                                            cyc = seg + path[1:]
                                            assert len(set(cyc)) == 16, ("not16", n, v)
                                            es2 = set(frozenset((cyc[i], cyc[(i+1) % 16]))
                                                      for i in range(16))
                                            assert esC & es2, ("noshare", n, v)
                                            s2 = set(cyc)
                                            ch = False
                                            for aa in cyc:
                                                for bb in adj[aa]:
                                                    if bb in s2 and frozenset((aa, bb)) not in es2:
                                                        ch = True
                                            if d == 1:
                                                assert ch, ("nochord at d=1", n, v, f1, f2)
                                            if ch: n_ok += 1
                                            else: n_nochord += 1
                                        continue
                                    if w in banned or w in path or w == f2: continue
                                    if len(path) >= 12: continue
                                    stack.append((w, path + [w], usedC or e_onC))
assert n_ok == 50125, n_ok
assert n_nochord == 3063, n_nochord
print("CHECK 1 ok:", n_ok, "valid paths;", n_nochord, "chordless-only failures (all d>=2)")
CHECK -->
