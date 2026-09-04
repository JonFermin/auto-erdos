---
id: c16_n28_zero_free_closed
status: proved
depends_on: [chordless_c16_ear_geometry, c16_chord_equiv]
discharged_by_round: 69
introduced_at_round: 69
---

# Lemma `c16_n28_zero_free_closed` (proved — the $n = 28$ zero-free corner is exhausted: every member has a chorded $C_{16}$, and twelve NEW class members appear)

**Setting.** $G$ cubic $\{C_4, C_8\}$-free on $28$ vertices, $C$ a
chordless $16$-cycle. The $16$ spokes land on the $12$ outside
vertices; the profile is *zero-free* if every outside vertex receives
at least one spoke. Excess $16 - 12 = 4$ with spoke counts $\le 3$
forces exactly three profiles:
$(3, 3, 1^{10})$, $(3, 2, 2, 1^9)$, $(2^4, 1^8)$.

**Claim.** Every cubic $\{C_4, C_8\}$-free graph on $28$ vertices
containing a chordless $C_{16}$ with a zero-free spoke profile
contains a chorded $C_{16}$. Consequently a supply falsifier (all
$C_{16}$s chordless, per `c16_chord_equiv`) at $n = 28$ must realize
every chordless $C_{16}$ with at least one $0$-spoke outside vertex.
Moreover the corner contains exactly **12 isomorphism classes** of
class members — all previously unknown (the R57 pin is not among
them: none of its $32$ chordless $C_{16}$s is zero-free).

**Proof (exhaustive enumeration, edge-determined).**

*Step 1 — the graph is determined by the configuration.* An outside
vertex with $s$ spokes has outside degree $3 - s$: a $3$-apex is
isolated in the outside graph, a $2$-apex is an endpoint of an
outside path, and a $1$-spoke vertex is interior to a path or lies
on an outside cycle. Outside edge count:
$(3 \cdot 12 - 16)/2 = 10$, so
$16 + 16 + 10 = 42 = 3 \cdot 28 / 2$ — all edges are accounted for.
Per profile the outside graph is:
$(3,3,1^{10})$ — two isolated apexes plus disjoint cycles
partitioning $10$ (parts $\ge 3$, $\ne 4, 8$: $\{10\}, \{7,3\},
\{5,5\}$); $(3,2,2,1^9)$ — one isolated apex, ONE path joining the
two $2$-apexes with $j$ interior vertices, cycles on the remaining
$9 - j$ ($j \in \{0,1,2,3,4,6,9\}$); $(2^4,1^8)$ — two disjoint
paths pairing the four $2$-apexes plus cycles on the rest.

*Step 2 — canonicalization (provably complete).* Rotation of $C$ is
fixed by an anchor: each profile has a unit KIND present in every
configuration (a $3$-apex for the first two profiles, a $2$-apex for
the third), and some rotation moves one of that unit's feet to $0$ —
so enumerating configurations in which the anchored unit carries
foot $0$ is complete. Within units: apex and path-endpoint feet
ascending; a non-anchored path is read from the endpoint with the
smaller minimum foot; each cycle is written from its OWN minimal
foot with equal-length cycles ordered by increasing start (the R68
own-min rule). Reflections and cycle directions are enumerated
redundantly (harmless).

*Step 3 — pruning is necessary-only; the filter is exact.* During
the feet DFS, two feet $x, y$ on the same outside unit whose hosts
are $t$ outside-edges apart close cycles of lengths
$d + t + 2$ and $(16 - d) + t + 2$ ($d = $ min-arc of $x, y$; both
values for cycle units via the two host paths), pruned when a length
lands in $\{4, 8\}$; additionally the $3{+}1{+}3{+}1$ double-ear
$C_8$ (two host-disjoint $3$-edge excursions whose feet pairs sit at
arc distance $1$ twice) is pruned across units. Every surviving
configuration is BUILT as a graph and tested exactly: $C_4$ by
common-neighbor bitsets, $C_8$ by exhaustive depth-$8$ search — no
reliance on the pruning. The DFS framework reproduces the audited
R67 apex-$(0,1,8)$ slice bit-for-bit ($252$ configurations, the same
$4$ members, all chorded) before being pointed at $n = 28$.

*Step 4 — result.*

| profile | configs | members (labeled) | all-chordless |
|---|---|---|---|
| $(3,3,1^{10})$ | 71,304 | 0 | 0 |
| $(3,2,2,1^9)$ | 128,310 | 6 | 0 |
| $(2^4,1^8)$ | 162,680 | 208 | 0 |
| total | **362,294** | **214** | **0** |

Every one of the $214$ class-member configurations contains a
chorded $C_{16}$ (full $C_{16}$ enumeration per graph). The $214$
labeled members collapse to **12 isomorphism classes** (exact
`is_isomorphic` verification; the labeled multiplicities $32/16/6$
are the anchor/reflection/direction redundancy). All members have
their $3$-apex-free outside structure concentrated in pure-path
configurations: NO member has an outside cycle, and profile
$(3,3,1^{10})$ is EMPTY. $\square$

**The twelve new class members** (censuses $c_3 \ldots c_9$, $c_{16}$,
share-1 sum-18 supply = chorded-$C_{16}$ incidences):

| class | labeled | girth | $c_3..c_9$ | $c_{16}$ | supply |
|---|---|---|---|---|---|
| 0 | 32 | 3 | 1,0,4,12,10,0,33 | 579 | 997 |
| 1 | 32 | 3 | 4,0,6,8,6,0,8 | 392 | 888 |
| 2 | 16 | 3 | 1,0,3,12,13,0,31 | 574 | 1019 |
| 3 | 16 | 3 | 1,0,5,11,11,0,27 | 565 | 995 |
| 4 | 16 | 3 | 4,0,4,8,5,0,18 | 400 | 872 |
| 5 | 16 | 3 | 1,0,4,12,11,0,30 | 564 | 990 |
| 6 | 16 | 3 | 2,0,4,12,10,0,28 | 471 | 889 |
| 7 | 16 | 3 | 4,0,4,10,6,0,10 | 379 | 838 |
| 8 | 16 | 3 | 2,0,2,11,11,0,28 | 541 | 983 |
| 9 | 16 | **5** | 0,0,4,12,8,0,44 | 731 | **1330** |
| 10 | 16 | 3 | 1,0,2,12,14,0,34 | 588 | 1049 |
| 11 | 6 | 3 | 2,0,5,11,7,0,22 | 536 | 1040 |

Class 9 is a **second girth-5 class member at $n = 28$** (the R57
pin was the only known one) and carries the LARGEST supply seen on
any known member ($1330$; the pin has $1061$). Class 11 is the sole
$(3,2,2,1^9)$-profile member. Every supply is $\ge 838$, comfortably
above the in-class floor $562$ — the floor conjecture's margin
survives another corner. Edge lists for all twelve representatives
are embedded in CHECK 2 below.

**Program consequence.** Combined with `c16_matching_corner_closed`
($n = 32$ matching branch) and `c16_three_apex_corner_closed`
($n = 30$ three-apex corner), the zero-free chordless-$C_{16}$
profiles are now closed at $n = 28$ entirely, at $n = 30$ for
$(3, 1^{13})$, and at $n = 32$ for the matching branch. A supply
falsifier's every chordless $C_{16}$ must now have a $0$-spoke
(branch) outside vertex, except at $n = 30$ profile $(2,2,1^{12})$
(still open, feet-map space large) and $n \in \{24, 26\}$ (excess
$8, 6$: many-apex profiles, smaller spaces — next targets). The
$n = 24$ and $n = 26$ zero-free corners are the natural next
exhaustions with this (validated) unit framework.

<!-- CHECK
# CHECK 1 — re-derive one sub-slice of the (3,2,2,1^9) enumeration:
# anchored 3-apex fixed at feet (0,1,4), path j=9 (the only member-carrying
# structure of profile B). Claim: exactly 407 configurations survive the
# pruning, exactly ONE is a class member, and it contains a chorded C16.
from collections import deque
MD = [[min(abs(a-b)%16, 16-abs(a-b)%16) for b in range(16)] for a in range(16)]
def exm(m):
    return frozenset(x for x in (4-m, 8-m) if 1 <= x <= 8)
# path unit: hosts per slot [0,0,1..9,10,10]; slot exclusions vs earlier slots
hosts = [0,0]+list(range(1,10))+[10,10]
excl = []
adj1 = []
for si in range(13):
    e = []; nr = []
    for sj in range(si):
        t = abs(hosts[si]-hosts[sj])
        ex = exm(t+2)
        if ex: e.append((sj, ex))
        if t == 1: nr.append((sj, frozenset((hosts[si], hosts[sj]))))
    excl.append(e); adj1.append(nr)
APEX = (0,1,4)
def build(feet):
    adj = [[] for _ in range(28)]
    def add(a,b): adj[a].append(b); adj[b].append(a)
    for i in range(16): add(i, (i+1)%16)
    for f in APEX: add(16, f)
    for si in range(13): add(17+hosts[si], feet[si])
    for h in range(10): add(17+h, 18+h)
    return adj
def has_c4(adj):
    bits = [0]*28
    for v in range(28):
        for w in adj[v]: bits[v] |= 1 << w
    for u in range(28):
        for v in range(u+1, 28):
            c = bits[u] & bits[v] & ~(1<<u) & ~(1<<v)
            if c and (c & (c-1)): return True
    return False
def has_c8(adj):
    for s in range(28):
        d = [29]*28; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            if d[v] >= 8: continue
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        stack = [(u, (1<<s)|(1<<u), 1) for u in adj[s] if u > s]
        while stack:
            v, mask, depth = stack.pop()
            for w in adj[v]:
                if w == s:
                    if depth+1 == 8: return True
                    continue
                if w < s or (mask>>w)&1: continue
                nd = depth+1
                if nd + d[w] > 8: continue
                if nd < 8: stack.append((w, mask|(1<<w), nd))
    return False
def chorded16(adj):
    for s in range(28):
        d = [29]*28; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        stack = [(u, (1<<s)|(1<<u), [s,u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        onC = set(path); idx = {x:i for i,x in enumerate(path)}
                        for i,x in enumerate(path):
                            for y in adj[x]:
                                if y in onC and abs(i-idx[y]) not in (1,15):
                                    return True
                    continue
                if w < s or (mask>>w)&1: continue
                if len(path)+d[w] > 16: continue
                stack.append((w, mask|(1<<w), path+[w]))
    return False
cnt = 0; members = []
feet = [-1]*13; used = [False]*16
for p in APEX: used[p] = True
exc = []
def rec(g):
    global cnt
    if g == 13:
        cnt += 1
        adj = build(feet)
        if not has_c4(adj) and not has_c8(adj):
            members.append((tuple(feet), chorded16(adj)))
        return
    si = g
    if si == 1 or si == 12:
        cands = [p for p in range(feet[si-1]+1, 16) if not used[p]]
    elif si == 11:
        cands = [p for p in range(feet[0]+1, 16) if not used[p]]
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
                    if len({a,b,c,dd}) == 4 and ((MD[a][c]==1 and MD[b][dd]==1)
                            or (MD[a][dd]==1 and MD[b][c]==1)):
                        ok = False; break
                if not ok: break
                exc.append((a, b, hp)); pushed += 1
        if ok:
            feet[g] = p; used[p] = True
            rec(g+1)
            used[p] = False; feet[g] = -1
        for _ in range(pushed): exc.pop()
rec(0)
assert cnt == 407, cnt
assert len(members) == 1 and members[0][1], members
assert members[0][0] == (2,10,12,9,3,6,8,5,13,7,11,14,15), members
CHECK -->

<!-- CHECK
# CHECK 2 — audit the twelve claimed class representatives (cubic,
# C4-free, C8-free, chorded C16 present) and the negative control:
# the R57 pin (the only previously-known n=28 member) has NO zero-free
# chordless C16, so its absence from the enumeration is consistent.
from collections import deque
REPS = [
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
PIN = [(0,11),(0,19),(0,27),(1,17),(1,19),(1,21),(2,9),(2,13),(2,14),
(3,22),(3,24),(3,25),(4,5),(4,7),(4,26),(5,14),(5,18),(6,7),(6,8),(6,20),
(7,13),(8,14),(8,25),(9,17),(9,24),(10,16),(10,21),(10,27),(11,15),(11,16),
(12,19),(12,23),(12,26),(13,18),(15,22),(15,26),(16,25),(17,23),(18,23),
(20,21),(20,24),(22,27)]
def to_adj(pairs, n=28):
    adj = [[] for _ in range(n)]
    for u, v in pairs:
        adj[u].append(v); adj[v].append(u)
    return adj
def has_c4(adj, n):
    bits = [0]*n
    for v in range(n):
        for w in adj[v]: bits[v] |= 1 << w
    for u in range(n):
        for v in range(u+1, n):
            c = bits[u] & bits[v] & ~(1<<u) & ~(1<<v)
            if c and (c & (c-1)): return True
    return False
def has_c8(adj, n):
    for s in range(n):
        d = [n+1]*n; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            if d[v] >= 8: continue
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        stack = [(u, (1<<s)|(1<<u), 1) for u in adj[s] if u > s]
        while stack:
            v, mask, depth = stack.pop()
            for w in adj[v]:
                if w == s:
                    if depth+1 == 8: return True
                    continue
                if w < s or (mask>>w)&1: continue
                nd = depth+1
                if nd + d[w] > 8: continue
                if nd < 8: stack.append((w, mask|(1<<w), nd))
    return False
def c16_scan(adj, n):
    """yield (path, chorded) over all 16-cycles"""
    for s in range(n):
        d = [n+1]*n; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[w] > d[v]+1: d[w] = d[v]+1; q.append(w)
        stack = [(u, (1<<s)|(1<<u), [s,u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        onC = set(path); idx = {x:i for i,x in enumerate(path)}
                        ch = False
                        for i,x in enumerate(path):
                            for y in adj[x]:
                                if y in onC and abs(i-idx[y]) not in (1,15):
                                    ch = True
                        yield path, ch
                    continue
                if w < s or (mask>>w)&1: continue
                if len(path)+d[w] > 16: continue
                stack.append((w, mask|(1<<w), path+[w]))
for k, flat in enumerate(REPS):
    xs = [int(t) for t in flat.split(",")]
    pairs = list(zip(xs[0::2], xs[1::2]))
    adj = to_adj(pairs)
    assert all(len(set(a)) == 3 and v not in a for v, a in enumerate(adj)), k
    assert not has_c4(adj, 28), k
    assert not has_c8(adj, 28), k
    chorded = False
    for path, ch in c16_scan(adj, 28):
        if ch:
            chorded = True
            break
    assert chorded, k
# negative control: pin has no zero-free chordless C16
adj = to_adj(PIN)
assert not has_c4(adj, 28) and not has_c8(adj, 28)
for path, ch in c16_scan(adj, 28):
    if ch: continue
    onC = set(path)
    touched = {w for x in path for w in adj[x] if w not in onC}
    assert len(touched) < 12, path
CHECK -->
