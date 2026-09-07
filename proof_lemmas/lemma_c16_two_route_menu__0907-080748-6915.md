---
id: c16_two_route_menu
status: open
depends_on: [c16_two_routes, c16_dist3_le30, chordless_c16_ear_geometry]
discharged_by_round: null
introduced_at_round: 77
---

# Lemma `c16_two_route_menu` (open — the exchange's route-length menu; conjecture + dual-attack probes)

**Statement (conjecture).** Let $G$ be a connected cubic
$\{C_4, C_8\}$-free graph on $24 \le n \le 30$ vertices, $C$ a chordless
$16$-cycle, $v$ a $0$-spoke outside vertex of $C$. For a chorded
$16$-cycle $C'$ with $v \in V(C')$ and $E(C') \cap E(C) \ne \emptyset$,
write its *branch segment* for the maximal subpath of $C'$ through $v$
with all interior vertices off $C$; its two halves at $v$ are the
exchange's two routes, of lengths $(c_1, c_2)$, $c_1 \le c_2$. Then
some witness $C'$ has

$$(c_1, c_2) \in \{(2,2),\ (2,3)\} \quad \text{if } \mathrm{dist}(v, C) = 2,$$
$$(c_1, c_2) = (3,3) \quad \text{if } \mathrm{dist}(v, C) = 3,$$

i.e. BOTH routes have length $\le 3$ and the branch segment has length
$c_1 + c_2 \le 6$. Separately (not necessarily the same witness): some
witness has at most $2$ maximal shared arcs.

**Optimality of the menu (proved inline).**

1. Each route has length $\ge 2$ ($v$ is $0$-spoke), and
   $c_1 \ge \mathrm{dist}(v, C)$; so at dist-$3$ vertices (which exist
   at $n = 30$ — the $39$ fallback pairs below; impossible at
   $n \le 28$ where corpus distance is uniformly $2$) the $(3,3)$ row
   is the best possible, and the menu is per-pair optimal.
2. A branch segment of length $4$ cannot come from a SINGLE-arc
   witness: there the complementary cycle (segment + replaced arc,
   both of length $L$) has length $2L = 8$ — a $C_8$. So every
   $(2,2)$-witness is composite ($m \ge 2$ shared arcs), which is
   exactly what the corpus minimizers do (the dominant shape is
   segment $4$ + one length-$2$ ear + two arcs totalling $10$).
3. General segment exclusion (the R74-corrected ear arithmetic): a
   branch segment of length $L$ between feet at arc distance $d$
   rides with cycles of lengths $d + L$ and $16 - d + L$;
   $\{d + L, 16 - d + L\} \cap \{4, 8\} = \emptyset$ in the class.
   For $L = 4$ this forbids exactly $d = 4$; for $L = 5$, $d = 3$;
   for $L = 6$, $d = 2$ (and $d + L = 16$ IS a witness when the
   segment closes against the long arc).

**Dual-attack record (probe BEFORE proof effort, standing policy).**
Deterministic corpus, $2{,}440$ pairs total, zero violations:

- CHECK 1: $n = 24$ (a locally-searched member, hardcoded — the first
  deterministic $n = 24$ class member in this program, $3$ pairs),
  $n = 26$ ($14$ pairs), twelve $n = 28$ zero-free representatives +
  the R57 pin ($745$ pairs): every pair has a routes-$\le 3$ witness,
  an $m \le 2$ witness, and (dist is uniformly $2$ here) a
  $\{(2,2),(2,3)\}$ witness.
- CHECK 2: T(Petersen) + the ten R71 slice members ($n = 30$,
  $1{,}678$ pairs): same, with exactly $39$ pairs — precisely the
  dist-$3$ pairs — falling to the $(3,3)$ row, each with a $(3,3)$
  witness present.

Walk-level evidence (nondeterministic, documented in Sections 113–114):
$\sim 1.5$M pairs across $n = 24 \dots 32$ never produced a pair
whose every witness needs a route $> 4$; the $n = 32$ envelope is
dist $\le 4$ / routes observed up to $(4, \cdot)$ — the $n = 32$ menu
is NOT part of this conjecture (the branch-distance bound is $4$
there, sharp).

**Why this is the right next rung.** `c16_two_routes` (R76) gives the
two disjoint routes unconditionally; `c16_dist3_le30` bounds the
SHORTER one by $3$. What is missing for the arc-exchange program is
exactly the second route's length and the landing arithmetic: with
both routes $\le 3$ the exchange menu at a $0$-spoke vertex is a
FINITE list of local shapes (segment length $4$, $5$ or $6$; feet
arc-distances constrained by the exclusion table above and
`chordless_c16_ear_geometry`), so the conjecture reduces the
$k \ge 1$ branch to a bounded local statement. Proof targets, in
order: (a) dist-$2$ case — both routes lie in $B(v, 2)$-ish
territory; the two feet are spoke-hosts of $T$-vertices adjacent to
$v$'s neighbourhood, and the $|T| \ge 6$ / $|Z| \le n - 22$ pressure
plus the $d \ne 4$ ($L = 4$) exclusion must force a landing arc pair;
(b) dist-$3$ case at $n = 30$ — re-run the `c16_dist3_le30` plug
forcing one level up: the dist-$3$ geometry is rigid enough that the
$(3,3)$ segment through the forced $B(v,2)$ shape may be enumerable.
A falsifier — a class member + pair whose every witness routes
$> 3$ — would be equally informative: it would locate the exchange's
true range and re-open the composite (`share1_c16_compose`) route.

<!-- CHECK
# CHECK A draft - menu on n=24 (hardcoded member), n=26, twelve n=28 reps,
# R57 pin: every (chordless C16, 0-spoke v) pair has (i) a witness whose
# branch segment through v splits as routes (c1,c2) with both <= 3, and
# (ii) a witness with at most 2 shared arcs; moreover a witness with routes
# in {(2,2),(2,3)} exists (no dist-3 vertices at n <= 28).
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
def menu_pair(adj, vsC, esC, chd, v):
    # returns (found routes<=3 each, found m<=2, found routes in {(2,2),(2,3)})
    fr = fm = fs = False
    for vs2, es2, p2 in chd:
        if v not in vs2 or not (esC & es2): continue
        k = len(p2)
        sh = [frozenset((p2[i], p2[(i+1) % k])) in esC for i in range(k)]
        m = sum(1 for i in range(k) if sh[i] and not sh[i-1])
        pv = p2.index(v)
        i = pv; c1 = 0
        while p2[i] not in vsC: i = (i-1) % k; c1 += 1
        j = pv; c2 = 0
        while p2[j] not in vsC: j = (j+1) % k; c2 += 1
        lo, hi = min(c1, c2), max(c1, c2)
        if hi <= 3: fr = True
        if m <= 2: fm = True
        if (lo, hi) in ((2, 2), (2, 3)): fs = True
        if fr and fm and fs: break
    return fr, fm, fs
graphs = [ADJ24, to_adj(FLAT26, 26)] + [to_adj(f, 28) for f in REPS28]
gp = [[] for _ in range(28)]
for a, b in PIN28: gp[a].append(b); gp[b].append(a)
graphs.append(gp)
tot = 0
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
        interior = [u for u in range(n) if u not in vsC
                    and not any(t in vsC for t in adj[u])]
        for v in interior:
            tot += 1
            fr, fm, fs = menu_pair(adj, vsC, esC, chd, v)
            assert fr, ("routes>3", n, sorted(vsC), v)
            assert fm, ("m>2", n, sorted(vsC), v)
            assert fs, ("no short-route witness", n, sorted(vsC), v)
assert tot == 3 + 14 + 745, tot
print("CHECK A ok:", tot, "pairs")
CHECK -->

<!-- CHECK
# CHECK B draft - menu at n=30 (T(Petersen) + 10 slice members): every pair
# has a witness with routes <= 3 each AND a witness with m <= 2; a witness
# with routes in {(2,2),(2,3)} exists unless dist(v,C) = 3, in which case a
# (3,3) witness exists. Enumerators identical to arc_exchange CHECKs 1-2.
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
tot = d3 = 0
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
        interior = [u for u in range(n) if u not in vsC
                    and not any(t in vsC for t in adj[u])]
        for v in interior:
            tot += 1
            fr = fm = fs = f33 = False
            for vs2, es2, p2 in chd:
                if v not in vs2 or not (esC & es2): continue
                k = len(p2)
                sh = [frozenset((p2[i], p2[(i+1) % k])) in esC for i in range(k)]
                m = sum(1 for i in range(k) if sh[i] and not sh[i-1])
                pv = p2.index(v)
                i = pv; c1 = 0
                while p2[i] not in vsC: i = (i-1) % k; c1 += 1
                j = pv; c2 = 0
                while p2[j] not in vsC: j = (j+1) % k; c2 += 1
                lo, hi = min(c1, c2), max(c1, c2)
                if hi <= 3: fr = True
                if m <= 2: fm = True
                if (lo, hi) in ((2, 2), (2, 3)): fs = True
                if (lo, hi) == (3, 3): f33 = True
                if fr and fm and fs: break
            assert fr, ("routes>3", sorted(vsC), v)
            assert fm, ("m>2", sorted(vsC), v)
            if not fs:
                d3 += 1
                assert dist_to(adj, v, vsC) == 3 and f33, ("fallback", sorted(vsC), v)
assert tot == 1678, tot
assert d3 == 39, d3
print("CHECK B ok:", tot, "pairs;", d3, "(3,3)-fallback pairs")
CHECK -->
