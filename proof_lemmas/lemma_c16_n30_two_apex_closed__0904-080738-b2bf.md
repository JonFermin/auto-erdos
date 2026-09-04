---
id: c16_n30_two_apex_closed
status: proved
depends_on: [chordless_c16_ear_geometry, c16_n28_zero_free_closed, c16_n2426_zero_free_closed]
discharged_by_round: 71
introduced_at_round: 71
---

# Lemma `c16_n30_two_apex_closed` (proved — the last zero-free corner falls: every $n = 30$ two-apex configuration is chorded, and the ZERO-FREE PROGRAM IS COMPLETE)

**Setting.** $G$ cubic $\{C_4, C_8\}$-free on $30$ vertices, $C$ a
chordless $16$-cycle with spoke profile $(2, 2, 1^{12})$ — the one
zero-free profile left open by R66–R70. Outside: two $2$-apexes
(endpoints of one outside path with $j$ interior vertices) and
twelve $1$-spoke vertices ($j$ on the path, $12 - j$ on outside
cycles); $13$ outside edges; the graph is edge-determined
($16 + 16 + 13 = 45 = 3 \cdot 30/2$).

**Claim.**

(a) The corner is EXHAUSTED: $43{,}936$ configurations across all
$22$ structures ($j \in \{0,1,2,3,4,5,6,7,9,12\}$ with cycle
partitions of $12 - j$), of which $1{,}976$ are class members —
and **every one contains a chorded $C_{16}$**; zero all-chordless.

(b) The members collapse to **104 isomorphism classes**. Two are
rediscoveries — the R61 G5 snapshot and the R67 three-apex-corner
member, both recovered by an INDEPENDENT enumeration (a strong
end-to-end validation) — and **102 are new class members**
($82$ girth-$3$, $20$ girth-$5$; the classes split $83/21$ by girth
with one rediscovery in each), lifting the known corpus from $5$
members (pre-session) to $120$.

(c) **Zero-free completion.** Combined with
`c16_matching_corner_closed` ($n{=}32$, R66/R68),
`c16_three_apex_corner_closed` ($n{=}30$ $(3,1^{13})$, R67/R68),
`c16_n28_zero_free_closed` (R69), and
`c16_n2426_zero_free_closed` (R70): in ANY cubic
$\{C_4, C_8\}$-free graph on $24 \le n \le 32$ vertices, EVERY
chordless $C_{16}$ whose spokes cover all outside vertices coexists
with a chorded $C_{16}$ in the same graph. Hence a supply falsifier
(all $C_{16}$s chordless, `c16_chord_equiv`) must have, for every
one of its chordless $C_{16}$s, at least one $0$-spoke outside
vertex — an outside vertex untouched by the cycle's spokes. The
falsifier analysis is now entirely a *branch-vertex* analysis.

**Proof.** The validated unit-DFS framework (R69; anchored
$2$-apex carrying foot $0$, own-min cycle canonicalization,
necessary-only pruning, exact $C_4$/$C_8$ re-test of every
survivor, full $C_{16}$ enumeration on every member). Ran together
with the $(3, 1^{13})$ profile as a built-in cross-check: that
profile reproduced EXACTLY $15{,}066$ configurations and EXACTLY
the $24$ labeled members of `c16_three_apex_corner_closed`, all in
partition $(10, 3)$ — the R67/R68 numbers to the digit, from a
different code path. The two-apex profile's $1{,}976$ members were
each built and exactly re-verified; iso-classification by exact
`is_isomorphic` within short-cycle-census buckets. Members appear
in $15$ of the $22$ structures; the full-path structure
($j = 12$, no outside cycles) carries by far the most ($592$
labeled members of $1{,}976$), echoing the R69 observation that
member outside-structure is path-heavy. $\square$

**Validation anchors.** Rediscovering BOTH the G5 snapshot (found
by SA in R61, census $c_{16} = 728$, supply $1079$) and the R67
corner graph (found by a different exhaustion over a different
profile) from the $(2,2,1^{12})$ enumeration means three
independent search processes agree on these graphs — the framework,
the R67 DFS, and R61's simulated annealing.

**Program consequence.** The Q84 chorded-$C_{16}$ question is now:
*why must a class member all of whose $C_{16}$s are chordless give
every chordless $C_{16}$ a $0$-spoke outside vertex — and can the
branch-vertex geometry (`chordless_c16_ear_geometry` + spoke
counting: at $n \le 30$ a $0$-spoke vertex forces a multi-spoke
apex elsewhere) be closed against girth/$C_8$ exclusions?* The
zero-free side needs no further rounds. Next targets: (i) local
structure of a $0$-spoke outside vertex adjacent to the $C_{16}$'s
spoke ends (its three edges all go to other outside vertices —
branch trees); (ii) counting: $16$ spokes on $\le n - 17$ touched
outside vertices forces apex multiplicity $\ge 2$ somewhere at
$n \le 32$ (pigeonhole), re-entering the ear-geometry menu.

<!-- CHECK
# CHECK 1 — spot re-derivation: structure j=12 (full outside path),
# anchored endpoint pair prefix (0,1,3). Claim: exactly 184
# configurations survive pruning, exactly 10 are class members, and
# every member contains a chorded C16.
from collections import deque
MD = [[min(abs(a-b)%16, 16-abs(a-b)%16) for b in range(16)] for a in range(16)]
def exm(m):
    return frozenset(x for x in (4-m, 8-m) if 1 <= x <= 8)
hosts = [0,0]+list(range(1,13))+[13,13]
excl = []; adj1 = []
for si in range(16):
    e = []; nr = []
    for sj in range(si):
        t = abs(hosts[si]-hosts[sj])
        ex = exm(t+2)
        if ex: e.append((sj, ex))
        if t == 1: nr.append((sj, frozenset((hosts[si], hosts[sj]))))
    excl.append(e); adj1.append(nr)
def build(feet):
    adj = [[] for _ in range(30)]
    def add(a,b): adj[a].append(b); adj[b].append(a)
    for i in range(16): add(i, (i+1)%16)
    for si in range(16): add(16+hosts[si], feet[si])
    for h in range(13): add(16+h, 17+h)
    return adj
def has_c4(adj, n=30):
    bits = [0]*n
    for v in range(n):
        for w in adj[v]: bits[v] |= 1 << w
    for u in range(n):
        for v in range(u+1, n):
            c = bits[u] & bits[v] & ~(1<<u) & ~(1<<v)
            if c and (c & (c-1)): return True
    return False
def has_c8(adj, n=30):
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
def chorded16(adj, n=30):
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
feet = [-1]*16; used = [False]*16
for i, p in enumerate((0,1,3)):
    feet[i] = p; used[p] = True
exc = []
def rec(g):
    global cnt
    if g == 16:
        cnt += 1
        adj = build(feet)
        if not has_c4(adj) and not has_c8(adj):
            members.append((tuple(feet), chorded16(adj)))
        return
    si = g
    if si in (1, 15):
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
rec(3)
assert cnt == 184, cnt
assert len(members) == 10, len(members)
assert all(c for _, c in members)
CHECK -->

<!-- CHECK
# CHECK 2 — rediscovery audit: the R67 three-apex member and the R61 G5
# snapshot each (i) are cubic class members, (ii) contain a chordless C16
# with zero-free two-apex profile (2,2,1^12) — i.e. they BELONG in this
# corner — and (iii) contain a chorded C16, as the lemma asserts of every
# corner member.
from collections import deque
def r67_adj():
    adj = [[] for _ in range(30)]
    def add(a,b): adj[a].append(b); adj[b].append(a)
    for i in range(16): add(i, (i+1)%16)
    for f in (0,1,8): add(16, f)
    base = 17
    for cyc in [(2,4,11,9,5,7,10,14,12,15),(3,6,13)]:
        L = len(cyc)
        for i in range(L):
            add(base+i, base+(i+1)%L); add(base+i, cyc[i])
        base += L
    return adj
G5 = [[8, 28, 9], [11, 14, 2], [9, 15, 1], [20, 29, 17], [14, 21, 16],
      [8, 27, 6], [9, 22, 5], [10, 12, 19], [5, 25, 0], [6, 2, 0],
      [7, 16, 26], [1, 24, 13], [21, 7, 13], [11, 12, 18], [4, 22, 1],
      [24, 2, 25], [10, 29, 4], [3, 24, 19], [23, 13, 19], [7, 17, 18],
      [3, 25, 26], [12, 4, 27], [14, 6, 28], [26, 18, 27], [11, 15, 17],
      [8, 20, 15], [23, 10, 20], [5, 21, 23], [22, 29, 0], [3, 16, 28]]
def audit(adj):
    n = 30
    assert all(len(set(a)) == 3 and v not in a for v, a in enumerate(adj))
    bits = [0]*n
    for v in range(n):
        for w in adj[v]: bits[v] |= 1 << w
    for u in range(n):
        for v in range(u+1, n):
            c = bits[u] & bits[v] & ~(1<<u) & ~(1<<v)
            assert not (c and (c & (c-1))), "C4"
    found_zero_free_two_apex = False
    found_chorded = False
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
                    L = len(path)
                    if L == 8:
                        raise AssertionError("C8")
                    if L == 16 and path[1] < path[-1]:
                        onC = set(path); idx = {x:i for i,x in enumerate(path)}
                        ch = False
                        for i, x in enumerate(path):
                            for y in adj[x]:
                                if y in onC and abs(i-idx[y]) not in (1,15):
                                    ch = True
                        if ch:
                            found_chorded = True
                        else:
                            spokes = [w2 for x in path for w2 in adj[x]
                                      if w2 not in onC]
                            touched = set(spokes)
                            if len(touched) == 14:
                                from collections import Counter
                                prof = sorted(Counter(spokes).values(),
                                              reverse=True)
                                if prof[:2] == [2, 2]:
                                    found_zero_free_two_apex = True
                    continue
                if w < s or (mask>>w)&1: continue
                if len(path)+d[w] > 16: continue
                stack.append((w, mask|(1<<w), path+[w]))
    assert found_zero_free_two_apex and found_chorded
audit(r67_adj())
audit(G5)
CHECK -->
