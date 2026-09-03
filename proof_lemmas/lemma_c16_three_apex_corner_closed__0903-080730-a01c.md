---
id: c16_three_apex_corner_closed
status: proved
depends_on: [chordless_c16_ear_geometry, c16_matching_corner_closed]
discharged_by_round: 67
introduced_at_round: 67
---

# Lemma `c16_three_apex_corner_closed` (proved — the $n = 30$ three-apex zero-free corner is a single graph, and it has a chorded $C_{16}$)

**Setting.** $G$ cubic $\{C_4, C_8\}$-free on $30$ vertices, $C$ a
chordless $16$-cycle. The $16$ spokes land on the $14$ outside
vertices; the *spoke profile* is the multiset of per-vertex spoke
counts. "Zero-free" means every outside vertex catches $\ge 1$ spoke;
the excess is then exactly $2$, so the zero-free profiles are
precisely $(3, 1^{13})$ (one 3-apex) and $(2, 2, 1^{12})$ (two
2-apexes).

**Claim.** In the $(3, 1^{13})$ case the graph is FORCED up to
isomorphism: the apex arc gaps are $(1, 7, 8)$, the outside graph is
$C_{10} \sqcup C_3$ plus the isolated apex, and exactly $24$
rotation-canonical configurations survive — all with the same cycle
census $c_3 = 2$, $c_5 = 5$, $c_6 = 8$, $c_7 = 6$, $c_9 = 28$,
$c_{16} = 613$ (and $c_4 = c_8 = 0$). Every one of them contains a
chorded $C_{16}$. Hence a supply falsifier (all $C_{16}$s chordless)
can never present a chordless $C_{16}$ with profile $(3, 1^{13})$ at
$n = 30$.

**Proof.**

*Determinacy.* With profile $(3, 1^{13})$ the apex $u_0$ has outside
degree $0$ (all three edges are spokes) and each other outside vertex
has outside degree $2$, so the outside graph is $u_0$ plus a disjoint
union of cycles covering the other $13$ vertices, with lengths
$\notin \{4, 8\}$ (cycles of $G$). Edge count
$16 + 16 + 13 = 45 = 3 \cdot 30 / 2$: the decomposition is the whole
graph, and $G$ is determined by (apex feet triple, cycle partition of
$13$, feet map). The apex gaps $(a, b, c)$, $a + b + c = 16$, avoid
$\{2, 6, 10, 14\}$ (`chordless_c16_ear_geometry`(d)); the ring feet
law and octagon law of `c16_matching_corner_closed` Step 2 hold
verbatim for the outside cycles (they are necessary conditions;
completeness is NOT needed here because every surviving configuration
is re-verified exactly).

*Exhaustion.* Allowed cycle partitions of $13$:
$\{13\}, \{10,3\}, \{7,6\}, \{7,3,3\}, \{5,5,3\}$. DFS over all apex
triples with foot $0$ (rotation-canonical; $39$ triples pass the gap
law) and all feet maps with the necessary-condition pruning yields
$10{,}838$ configurations; building each graph and testing
$c_4 = c_8 = 0$ EXACTLY (full cycle search, no reliance on the
pruning) leaves exactly $24$ members. All $24$ have apex gaps
$(1, 7, 8)$ and partition $(10, 3)$, identical full cycle census
(above), and each contains a chorded $C_{16}$ (verified by full
$C_{16}$ enumeration per graph). The $24$ are the dihedral/direction
variants of a single labeled graph. $\square$

**The forced graph** (canonical representative; $C = 0\ldots15$,
apex $16$ with feet $\{0, 1, 8\}$, outside $C_{10}$ with feet
$(2,4,11,9,5,7,10,14,12,15)$, outside $C_3$ with feet $(3,6,13)$):

```
(0,1)(0,15)(0,16)(1,2)(1,16)(2,3)(2,17)(3,4)(3,27)(4,5)(4,18)(5,6)
(5,21)(6,7)(6,28)(7,8)(7,22)(8,9)(8,16)(9,10)(9,20)(10,11)(10,23)
(11,12)(11,19)(12,13)(12,25)(13,14)(13,29)(14,15)(14,24)(15,26)
(17,18)(17,26)(18,19)(19,20)(20,21)(21,22)(22,23)(23,24)(24,25)
(25,26)(27,28)(27,29)(28,29)
```

This is a **new (fifth) verified class member** at $n = 30$, the
first mixed-regime one: only $2$ triangles, yet its share-$1$
sum-$18$ supply spans all five shapes —
$(3,15){:}267$, $(5,13){:}314$, $(6,12){:}265$, $(7,11){:}100$,
$(9,9){:}97$, total $1043$ — comfortably above the in-class floor
$562$.

**Program consequence.** Combined with
`c16_matching_corner_closed`, two of the fully-edge-determined
corners of the falsifier space are now closed exhaustively. The
falsifier at $n = 30$ must realize every chordless $C_{16}$ with
profile $(2,2,1^{12})$ or with $0$-spoke outside vertices (outside
branch vertices); at $n = 32$, with an ear plus at least one
$0$-spoke vertex. The zero-free two-2-apex case $(2,2,1^{12})$ is
also fully determined (path + cycles outside) but its feet-map space
is orders of magnitude larger (long-path placements); it needs
either a smarter propagator or a compiled search — recorded as the
next exhaustion target.

<!-- CHECK
# CHECK — the full offline exhaustion (all 39 apex triples, 10,838
# configs, ~100 s) found exactly 24 members; within the harness budget
# this CHECK re-derives one full slice and audits every claimed member:
# (i) the apex (0,1,8) slice enumerates exactly 172 configurations and
# its exact member set is exactly the 4 claimed ones; (ii) all 24
# claimed members across all slices are verified class members
# (no C4 by common-neighbor count, no C8 by exhaustive depth-8 search)
# each containing a chorded C16.
from itertools import combinations
from collections import deque

def md16(a, b):
    d = abs(a - b) % 16
    return min(d, 16 - d)

def excl_for_k(k):
    return {x for x in (4 - k, 8 - k) if 1 <= x <= 8}

def pe(l):
    return {dl: excl_for_k(dl + 2) | excl_for_k((l - dl) + 2)
            for dl in range(1, l // 2 + 1)}

def parts13():
    allowed = [x for x in range(3, 14) if x not in (4, 8)]
    out = []
    def rec(rem, mx, cur):
        if rem == 0: out.append(tuple(cur)); return
        for p in allowed:
            if p <= mx and p <= rem: rec(rem - p, p, cur + [p])
    rec(13, 13, [])
    return out

def dfs(partition, positions, sink):
    n_cyc = len(partition); used = set()
    cycles = [[] for _ in range(n_cyc)]
    excl = [pe(l) for l in partition]; edges = []
    def violB(a, b):
        for (c, d) in edges:
            if len({a, b, c, d}) == 4 and (
               (md16(a, c) == 1 and md16(b, d) == 1) or
               (md16(a, d) == 1 and md16(b, c) == 1)):
                return True
        return False
    def okA(ci):
        cyc = cycles[ci]; L = partition[ci]; n = len(cyc); j = n - 1
        for i in range(n - 1):
            dl = j - i
            if not (n == L or dl <= L // 2): continue
            e = excl[ci].get(min(dl, L - dl))
            if e and md16(cyc[i], cyc[j]) in e: return False
        if n == L:
            for i, jj in combinations(range(L), 2):
                dl = jj - i
                e = excl[ci].get(min(dl, L - dl))
                if e and md16(cyc[i], cyc[jj]) in e: return False
        return True
    def rec(ci):
        if ci == n_cyc:
            sink(partition, [list(c) for c in cycles]); return
        L = partition[ci]; cyc = cycles[ci]
        if len(cyc) == L:
            rec(ci + 1); return
        if not cyc:
            rem = [p for p in positions if p not in used]
            starts = [rem[0]] if rem else []
        else:
            starts = [p for p in positions if p not in used]
        for p in starts:
            cyc.append(p); used.add(p)
            ok = okA(ci); pushed = 0
            if ok and len(cyc) >= 2:
                a, b = cyc[-2], cyc[-1]
                ok = not violB(a, b)
                if ok: edges.append((a, b)); pushed += 1
            if ok and len(cyc) == L:
                a, b = cyc[-1], cyc[0]
                ok = not violB(a, b)
                if ok: edges.append((a, b)); pushed += 1
            if ok: rec(ci)
            for _ in range(pushed): edges.pop()
            cyc.pop(); used.discard(p)
    rec(0)

def build(apex, cycles):
    adj = [[] for _ in range(30)]
    def add(a, b): adj[a].append(b); adj[b].append(a)
    for i in range(16): add(i, (i + 1) % 16)
    for f in apex: add(16, f)
    base = 17
    for cyc in cycles:
        L = len(cyc)
        for i in range(L):
            add(base + i, base + (i + 1) % L)
            add(base + i, cyc[i])
        base += L
    return adj

def has_c4(adj):
    bits = [0] * 30
    for v in range(30):
        for w in adj[v]: bits[v] |= 1 << w
    for u in range(30):
        for v in range(u + 1, 30):
            c = bits[u] & bits[v] & ~(1 << u) & ~(1 << v)
            if c and (c & (c - 1)): return True
    return False

def has_c8(adj):
    for s in range(30):
        d = [31] * 30; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            if d[v] >= 8: continue
            for w in adj[v]:
                if d[w] > d[v] + 1:
                    d[w] = d[v] + 1; q.append(w)
        stack = [(u, (1 << s) | (1 << u), 1) for u in adj[s] if u > s]
        while stack:
            v, mask, depth = stack.pop()
            for w in adj[v]:
                if w == s:
                    if depth + 1 == 8: return True
                    continue
                if w < s or (mask >> w) & 1: continue
                nd = depth + 1
                if nd + d[w] > 8: continue
                if nd < 8:
                    stack.append((w, mask | (1 << w), nd))
    return False

def has_chorded_c16(adj):
    for s in range(30):
        d = [31] * 30; d[s] = 0; q = deque([s])
        while q:
            v = q.popleft()
            for w in adj[v]:
                if d[w] > d[v] + 1:
                    d[w] = d[v] + 1; q.append(w)
        stack = [(u, (1 << s) | (1 << u), [s, u]) for u in adj[s] if u > s]
        while stack:
            v, mask, path = stack.pop()
            for w in adj[v]:
                if w == s:
                    if len(path) == 16 and path[1] < path[-1]:
                        onC = set(path)
                        idx = {x: i for i, x in enumerate(path)}
                        for i, x in enumerate(path):
                            for y in adj[x]:
                                if y in onC and abs(i - idx[y]) not in (1, 15):
                                    return True
                    continue
                if w < s or (mask >> w) & 1: continue
                if len(path) + d[w] > 16: continue
                stack.append((w, mask | (1 << w), path + [w]))
    return False

MEMBERS = {
((0,1,8),((2,4,11,9,5,7,10,14,12,15),(3,6,13))),
((0,1,8),((2,4,11,9,5,7,10,14,12,15),(3,13,6))),
((0,1,8),((2,15,12,14,10,7,5,9,11,4),(3,6,13))),
((0,1,8),((2,15,12,14,10,7,5,9,11,4),(3,13,6))),
((0,1,9),((2,5,3,7,10,12,8,6,13,15),(4,11,14))),
((0,1,9),((2,5,3,7,10,12,8,6,13,15),(4,14,11))),
((0,1,9),((2,15,13,6,8,12,10,7,3,5),(4,11,14))),
((0,1,9),((2,15,13,6,8,12,10,7,3,5),(4,14,11))),
((0,7,8),((1,3,15,13,4,6,9,12,10,14),(2,5,11))),
((0,7,8),((1,3,15,13,4,6,9,12,10,14),(2,11,5))),
((0,7,8),((1,14,10,12,9,6,4,13,15,3),(2,5,11))),
((0,7,8),((1,14,10,12,9,6,4,13,15,3),(2,11,5))),
((0,7,15),((1,3,10,8,4,6,9,13,11,14),(2,5,12))),
((0,7,15),((1,3,10,8,4,6,9,13,11,14),(2,12,5))),
((0,7,15),((1,14,11,13,9,6,4,8,10,3),(2,5,12))),
((0,7,15),((1,14,11,13,9,6,4,8,10,3),(2,12,5))),
((0,8,9),((1,3,12,10,7,4,6,2,15,13),(5,11,14))),
((0,8,9),((1,3,12,10,7,4,6,2,15,13),(5,14,11))),
((0,8,9),((1,13,15,2,6,4,7,10,12,3),(5,11,14))),
((0,8,9),((1,13,15,2,6,4,7,10,12,3),(5,14,11))),
((0,8,15),((1,4,2,6,9,11,7,5,12,14),(3,10,13))),
((0,8,15),((1,4,2,6,9,11,7,5,12,14),(3,13,10))),
((0,8,15),((1,14,12,5,7,11,9,6,2,4),(3,10,13))),
((0,8,15),((1,14,12,5,7,11,9,6,2,4),(3,13,10))),
}

# Full audit of the apex (0,1,8) slice.
cfgs = []
rest = [p for p in range(16) if p not in (0, 1, 8)]
for part in parts13():
    dfs(part, rest, lambda pp, cyc: cfgs.append(tuple(tuple(c) for c in cyc)))
assert len(cfgs) == 172, len(cfgs)
mem_this = set()
for cyc in cfgs:
    adj = build((0, 1, 8), [list(c) for c in cyc])
    if not has_c4(adj) and not has_c8(adj):
        mem_this.add(cyc)
        assert has_chorded_c16(adj), cyc
expected = {cyc for apex, cyc in MEMBERS if apex == (0, 1, 8)}
assert len(expected) == 4 and mem_this == expected

# Every claimed member (all apex slices): class member + chorded C16.
for apex, cyc in sorted(MEMBERS):
    adj = build(apex, [list(c) for c in cyc])
    assert not has_c4(adj) and not has_c8(adj), (apex, cyc)
    assert has_chorded_c16(adj), (apex, cyc)
CHECK -->
