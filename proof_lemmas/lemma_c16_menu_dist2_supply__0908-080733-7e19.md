---
id: c16_menu_dist2_supply
status: proved
depends_on: []
discharged_by_round: 78
introduced_at_round: 78
---

# Lemma `c16_menu_dist2_supply` (proved — the dist-2 supply dichotomy: T-neighbour count decides the menu row)

**Setting.** $G$ connected cubic $\{C_4, C_8\}$-free, $C$ a chordless
$16$-cycle, $v$ a $0$-spoke outside vertex with
$\mathrm{dist}(v, C) = 2$. Call $u \in N(v)$ a *T-neighbour* of $v$ if
$u$ has a neighbour on $C$ (all of $N(v)$ is off $C$ since $v$ is
$0$-spoke), and write $\mathrm{feet}(u) = N(u) \cap V(C)$ and
$\tau(v)$ for the number of T-neighbours. $\mathrm{dist}(v,C) = 2$
gives $\tau(v) \ge 1$. Route/branch-segment conventions as in
`c16_two_route_menu`; arc distances in min-form $1 \le d \le 8$.

**Claim.**

(a) *(disjoint feet)* Distinct T-neighbours $u_1 \ne u_2$ of $v$ have
$\mathrm{feet}(u_1) \cap \mathrm{feet}(u_2) = \emptyset$: a common
foot $f$ closes the $4$-cycle $v\,u_1\,f\,u_2$.

(b) *(automatic $d \ne 4$)* For any $u_1 \ne u_2$ and any
$f_1 \in \mathrm{feet}(u_1)$, $f_2 \in \mathrm{feet}(u_2)$ (distinct
by (a)), the arc distance of $\{f_1, f_2\}$ is $\ne 4$: the branch
path $f_1 u_1 v u_2 f_2$ has length $4$ and its five vertices are
distinct and meet $C$ only in $\{f_1, f_2\}$, so a $4$-arc between
the feet would close a simple $C_8$. (The long side: a $12$-gap is
the $4$-gap in min-form; $20 - g \in \{4, 8\}$ needs $g \ge 12$,
same exclusion.) Hence EVERY cross-pair of feet is a legal
$(2,2)$-landing pair: distinct, at arc distance
$d \in \{1,2,3,5,6,7,8\}$.

(c) *(necessity)* A $(2,2)$-witness for $(C, v)$ exists only if
$\tau(v) \ge 2$: its two routes share only $v$, so they leave $v$
through distinct neighbours, and a length-$2$ route $v\,a\,f$ forces
$a$ to be a T-neighbour.

(d) *($(2,3)$ floor at $\tau = 1$)* If $\tau(v) = 1$, with unique
T-neighbour $u$, then every witness has longer route $\ge 3$, so the
menu row $(2,3)$ is per-pair optimal there; a shorter route of
length $2$ (which exists in any $(2,3)$-witness) necessarily runs
through $u$.

(e) *(single-arc $(2,3)$ arithmetic)* A single-arc ($m = 1$) witness
with routes $(2,3)$ has branch segment of length $5$ and its unique
shared arc of length $11$, so its feet are at min-distance exactly
$5$; the complementary cycle (segment + $5$-arc) is a legal
$C_{10}$. Conversely $L = 5$ forbids feet distance $3$
($5 + 3 = 8$).

(f) *(supply dichotomy — realized menu, CHECK-backed)* On the whole
deterministic corpus ($762$ dist-$2$ pairs at $n \le 28$, $1{,}639$
at $n = 30$; every $n \le 28$ pair is dist-$2$):
$\tau \in \{1, 2, 3\}$ with counts $\{1{:}30, 2{:}268, 3{:}464\}$
($n \le 28$) and $\{1{:}163, 2{:}561, 3{:}915\}$ ($n = 30$); a
$(2,2)$-witness exists **iff** $\tau \ge 2$ (all $2{,}208$
$\tau \ge 2$ pairs have one; none of the $193$ $\tau = 1$ pairs
does — consistent with (c)); every $\tau = 1$ pair has a
$(2,3)$-witness AND nonzero length-$3$ second-route supply (some
$v\,x\,y\,f_2$ with $x \in N(v) \setminus \{u\}$, $y \notin C$ a
T-vertex, $f_2 \notin \mathrm{feet}(u)$); and every single-arc
$(2,3)$ minimizer lands at feet distance $5$ per (e).

**Consequence (the R78 reduction).** By (a)–(b), at $\tau(v) \ge 2$
the $(2,2)$-landing SUPPLY is unconditional — every choice of feet
through two distinct T-neighbours is legal. The dist-$2$ row of
`c16_two_route_menu` is therefore equivalent to two pure CLOSURE
statements:

- **(A)** $\tau \ge 2$: some legal landing pair completes to a
  chorded $16$-cycle witness (observed minimal shapes: $m = 2$ with
  second off-$C$ segment of length $2..7$ — $2{,}192$ pairs — or
  $m = 3$ with two length-$2$/$3$ ears — $16$ pairs).
- **(B)** $\tau = 1$: some $(2,3)$ completion exists (observed:
  single-arc at feet distance $5$ — $77$ of $193$ — else composite,
  $m \in \{2, 3\}$).

Neither closure statement needs any supply hypothesis beyond
$\tau(v)$; the *shape* of the completion is what remains open, and
the corpus shape histograms above (recorded R78) bound what a
closure proof must produce. The second-route supply fact in (f) is
the $\tau = 1$ analogue of (b) and is what statement (B)'s
enumeration should consume.

**Proof.**

(a) $v, u_1, u_2 \notin C$, $f \in C$: the four vertices are
pairwise distinct ($u_1 \ne u_2$ given; $u_i \ne v$; $f$ differs
from all three), and $v u_1, u_1 f, f u_2, u_2 v \in E(G)$ — a
$C_4$, excluded. $\square$

(b) The path $P = f_1 u_1 v u_2 f_2$: $u_1 \ne u_2$, feet distinct
by (a), $u_i, v \notin C \ni f_1, f_2$, so $|V(P)| = 5$ and
$V(P) \cap V(C) = \{f_1, f_2\}$. An arc of length $4$ between $f_1$
and $f_2$ has $3$ interior vertices, all on $C$, hence disjoint
from $\{u_1, v, u_2\}$ and from the feet; arc $+$ $P$ is a simple
closed walk on $8$ distinct vertices — a $C_8$, excluded. A gap of
$g$ on one side is $16 - g$ on the other, so $g \ne 4$ and
$g \ne 12$, i.e. min-form $d \ne 4$. No other value is excluded by
the segment alone: $d + 4 \in \{4, 8\}$ iff $d \in \{0, 4\}$ and
$20 - d \in \{4, 8\}$ iff $d \ge 12$. $\square$

(c) Routes of a witness share only $v$ (they are the two halves of
the branch segment at $v$), so their first edges $v a$, $v b$ have
$a \ne b$. A route of length $2$ is $v\,a\,f$ with $f \in C$, so
$a$ is a T-neighbour; two length-$2$ routes give two distinct
T-neighbours. $\square$

(d) By (c) applied to the shorter route: if both routes had length
$2$ we would need $\tau \ge 2$; with $\tau = 1$ at most one route
has length $2$, and routes have length $\ge 2$ ($v$ is $0$-spoke),
so the longer route is $\ge 3$. The route floor $c_1 \ge
\mathrm{dist}(v, C) = 2$ makes $(2,3)$ optimal. A length-$2$ route
$v\,a\,f$ forces $a = u$. $\square$

(e) With $m = 1$ the witness is branch segment ($L$ edges) $+$ one
shared arc ($16 - L$ edges); routes $(2,3)$ give $L = 5$, arc
$= 11$, feet gap $11$, min-form $5$. The complementary cycle uses
the other arc: $5 + 5 = 10 \notin \{4, 8\}$ — consistent. If the
feet were at distance $3$, segment $+$ short arc $= 5 + 3 = 8$, a
$C_8$ — the exclusion-table row for $L = 5$. $\square$

(f) Deterministic CHECKs below (n $\le 28$ / $n = 30$ split for the
CHECK budget), enumerating all chordless/chorded $16$-cycles exactly
as in `c16_two_route_menu` CHECKs 1–2. $\square$

**What this rung does for the program.** It moves the menu's
dist-$2$ row from "conjecture with CHECKs" to "two closure
statements with proved, unconditional supply", and it pins the
$\tau = 1$ stratum ($193$ corpus pairs, $8\%$) as the only place
the $(2,3)$ row is NEEDED at dist-$2$ — everywhere else $(2,2)$ is
both possible and per-pair optimal. Closure statement (A) is the
next enumeration target (R79+): the completion lives in
$G - \{v, u_1, u_2\}$'s interaction with the $\le 14$-vertex
outside, and the blob-kill/plug-forcing style applies to the
second off-$C$ segment.

<!-- CHECK
# CHECK 1 - supply dichotomy at n<=28 (n24 hardcoded member, n26, twelve n28
# reps, R57 pin; every pair is dist-2 there): (a) distinct T-neighbours of v
# have disjoint feet; (b) all cross feet pairs at arc distance != 4;
# (c)+(f) a (2,2) witness exists iff tau >= 2; tau=1 implies a (2,3) witness
# and >=1 length-3 second route; single-arc (2,3) minimizers land at feet
# distance 5; tau histogram {1:30, 2:268, 3:464} on 762 pairs.
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
def routes_of(vsC, p2, v):
    k = len(p2); pv = p2.index(v)
    i = pv; c1 = 0
    while p2[i] not in vsC: i = (i-1) % k; c1 += 1
    f1 = p2[i]
    j = pv; c2 = 0
    while p2[j] not in vsC: j = (j+1) % k; c2 += 1
    f2 = p2[j]
    return (min(c1, c2), max(c1, c2)), f1, f2
graphs = [ADJ24, to_adj(FLAT26, 26)] + [to_adj(f, 28) for f in REPS28]
gp = [[] for _ in range(28)]
for a, b in PIN28: gp[a].append(b); gp[b].append(a)
graphs.append(gp)
tot = 0; hist = {1: 0, 2: 0, 3: 0}
for adj in graphs:
    n = len(adj)
    cs = all_c16(adj)
    chl, chd = [], []
    for vs, es, path in cs:
        ch = False
        for x in path:
            for y in adj[x]:
                if y in vs and frozenset((x, y)) not in es: ch = True
        (chd if ch else chl).append((vs, es, path))
    for vsC, esC, pathC in chl:
        pos = {x: i for i, x in enumerate(pathC)}
        interior = [u for u in range(n) if u not in vsC
                    and not any(t in vsC for t in adj[u])]
        for v in interior:
            tot += 1
            tn = [(u, [f for f in adj[u] if f in vsC]) for u in adj[v]]
            tn = [(u, F) for u, F in tn if F]
            tau = len(tn); hist[tau] += 1
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    assert not (set(tn[a][1]) & set(tn[b][1])), ("(a)", v)
                    for f1 in tn[a][1]:
                        for f2 in tn[b][1]:
                            g = (pos[f2]-pos[f1]) % 16
                            assert min(g, 16-g) != 4, ("(b)", v)
            has22 = has23 = False; sa_ok = True
            for vs2, es2, p2 in chd:
                if v not in vs2 or not (esC & es2): continue
                r, f1w, f2w = routes_of(vsC, p2, v)
                if r == (2, 2): has22 = True
                if r == (2, 3):
                    has23 = True
                    k = len(p2)
                    sh = [frozenset((p2[i], p2[(i+1) % k])) in esC for i in range(k)]
                    m = sum(1 for i in range(k) if sh[i] and not sh[i-1])
                    if m == 1:
                        g = (pos[f2w]-pos[f1w]) % 16
                        if min(g, 16-g) != 5: sa_ok = False
            assert has22 == (tau >= 2), ("(c)+(f)", v, tau, has22)
            assert sa_ok, ("(e)", v)
            if tau == 1:
                u, F1 = tn[0]
                r3 = 0
                for x in adj[v]:
                    if x == u: continue
                    for y in adj[x]:
                        if y == v or y in vsC: continue
                        r3 += sum(1 for f in adj[y] if f in vsC and f not in F1)
                assert has23 and r3 >= 1, ("(f) tau=1", v, has23, r3)
assert tot == 762, tot
assert hist == {1: 30, 2: 268, 3: 464}, hist
print("CHECK 1 ok:", tot, "pairs;", hist)
CHECK -->

<!-- CHECK
# CHECK 2 - same dichotomy at n=30 (T(Petersen) + the 10 slice members),
# restricted to the 1,639 dist-2 pairs: tau histogram {1:163, 2:561, 3:915};
# (2,2) iff tau >= 2; tau=1 implies (2,3) + length-3 supply; disjoint feet;
# cross feet distance != 4; single-arc (2,3) minimizers at feet distance 5.
from collections import deque
from itertools import combinations
def t_pet():
    padj = {v: set() for v in range(10)}
    for i in range(5):
        for a, b in ((i, (i+1) % 5), (i, i+5), (5+i, 5+(i+2) % 5)):
            padj[a].add(b); padj[b].add(a)
    verts = [(v, u) for v in sorted(padj) for u in sorted(padj[v])]
    idx = {p: i for i, p in enumerate(verts)}
    g = [set() for _ in verts]
    for v in sorted(padj):
        for a, b in combinations([idx[(v, u)] for u in sorted(padj[v])], 2):
            g[a].add(b); g[b].add(a)
        for u in padj[v]:
            if v < u:
                g[idx[(v, u)]].add(idx[(u, v)]); g[idx[(u, v)]].add(idx[(v, u)])
    return [sorted(s) for s in g]
def slice10():
    MD = [[min(abs(a-b) % 16, 16-abs(a-b) % 16) for b in range(16)] for a in range(16)]
    def exm(m):
        return frozenset(x for x in (4-m, 8-m) if 1 <= x <= 8)
    hosts = [0, 0]+list(range(1, 13))+[13, 13]
    excl = []; adj1 = []
    for si in range(16):
        e = []; nr = []
        for sj in range(si):
            t = abs(hosts[si]-hosts[sj]); ex = exm(t+2)
            if ex: e.append((sj, ex))
            if t == 1: nr.append((sj, frozenset((hosts[si], hosts[sj]))))
        excl.append(e); adj1.append(nr)
    def build(feet):
        adj = [[] for _ in range(30)]
        def add(a, b): adj[a].append(b); adj[b].append(a)
        for i in range(16): add(i, (i+1) % 16)
        for si in range(16): add(16+hosts[si], feet[si])
        for h in range(13): add(16+h, 17+h)
        return adj
    def has_c4(adj):
        n = len(adj); bits = [0]*n
        for v in range(n):
            for w in adj[v]: bits[v] |= 1 << w
        for u in range(n):
            for v in range(u+1, n):
                c = bits[u] & bits[v] & ~(1 << u) & ~(1 << v)
                if c and (c & (c-1)): return True
        return False
    def has_c8(adj):
        n = len(adj)
        for s in range(n):
            stack = [(u, (1 << s) | (1 << u), 2) for u in adj[s] if u > s]
            while stack:
                v, mask, ln = stack.pop()
                for w in adj[v]:
                    if w == s:
                        if ln == 8: return True
                        continue
                    if w < s or (mask >> w) & 1: continue
                    if ln >= 8: continue
                    stack.append((w, mask | (1 << w), ln+1))
        return False
    members = []
    feet = [-1]*16; used = [False]*16
    for i, p in enumerate((0, 1, 3)):
        feet[i] = p; used[p] = True
    exc = []
    def rec(g):
        if g == 16:
            adj = build(feet)
            if not has_c4(adj) and not has_c8(adj): members.append(adj)
            return
        if g in (1, 15):
            cands = [p for p in range(feet[g-1]+1, 16) if not used[p]]
        else:
            cands = [p for p in range(16) if not used[p]]
        for p in cands:
            ok = True
            for (gj, e) in excl[g]:
                if MD[p][feet[gj]] in e: ok = False; break
            pushed = 0
            if ok:
                for (gj, hp) in adj1[g]:
                    a, b = p, feet[gj]
                    for (c, dd, hp2) in exc:
                        if hp & hp2: continue
                        if len({a, b, c, dd}) == 4 and ((MD[a][c] == 1 and MD[b][dd] == 1)
                                or (MD[a][dd] == 1 and MD[b][c] == 1)):
                            ok = False; break
                    if not ok: break
                    exc.append((a, b, hp)); pushed += 1
            if ok:
                feet[g] = p; used[p] = True
                rec(g+1)
                used[p] = False; feet[g] = -1
            for _ in range(pushed): exc.pop()
    rec(3)
    assert len(members) == 10, len(members)
    return members
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
tot = 0; hist = {1: 0, 2: 0, 3: 0}
for adj in [t_pet()] + slice10():
    n = 30
    cs = all_c16(adj)
    chl, chd = [], []
    for vs, es, path in cs:
        ch = False
        for x in path:
            for y in adj[x]:
                if y in vs and frozenset((x, y)) not in es: ch = True
        (chd if ch else chl).append((vs, es, path))
    for vsC, esC, pathC in chl:
        pos = {x: i for i, x in enumerate(pathC)}
        interior = [u for u in range(n) if u not in vsC
                    and not any(t in vsC for t in adj[u])]
        for v in interior:
            if dist_to(adj, v, vsC) != 2: continue
            tot += 1
            tn = [(u, [f for f in adj[u] if f in vsC]) for u in adj[v]]
            tn = [(u, F) for u, F in tn if F]
            tau = len(tn); hist[tau] += 1
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    assert not (set(tn[a][1]) & set(tn[b][1])), ("(a)", v)
                    for f1 in tn[a][1]:
                        for f2 in tn[b][1]:
                            g = (pos[f2]-pos[f1]) % 16
                            assert min(g, 16-g) != 4, ("(b)", v)
            has22 = has23 = False; sa_ok = True
            for vs2, es2, p2 in chd:
                if v not in vs2 or not (esC & es2): continue
                k = len(p2); pv = p2.index(v)
                i = pv; c1 = 0
                while p2[i] not in vsC: i = (i-1) % k; c1 += 1
                f1w = p2[i]
                j = pv; c2 = 0
                while p2[j] not in vsC: j = (j+1) % k; c2 += 1
                f2w = p2[j]
                r = (min(c1, c2), max(c1, c2))
                if r == (2, 2): has22 = True
                if r == (2, 3):
                    has23 = True
                    sh = [frozenset((p2[i2], p2[(i2+1) % k])) in esC for i2 in range(k)]
                    m = sum(1 for i2 in range(k) if sh[i2] and not sh[i2-1])
                    if m == 1:
                        g = (pos[f2w]-pos[f1w]) % 16
                        if min(g, 16-g) != 5: sa_ok = False
            assert has22 == (tau >= 2), ("(c)+(f)", v, tau, has22)
            assert sa_ok, ("(e)", v)
            if tau == 1:
                u, F1 = tn[0]
                r3 = 0
                for x in adj[v]:
                    if x == u: continue
                    for y in adj[x]:
                        if y == v or y in vsC: continue
                        r3 += sum(1 for f in adj[y] if f in vsC and f not in F1)
                assert has23 and r3 >= 1, ("(f) tau=1", v, has23, r3)
assert tot == 1639, tot
assert hist == {1: 163, 2: 561, 3: 915}, hist
print("CHECK 2 ok:", tot, "pairs;", hist)
CHECK -->
