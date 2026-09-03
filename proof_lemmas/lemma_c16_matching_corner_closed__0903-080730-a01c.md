---
id: c16_matching_corner_closed
status: proved
depends_on: [chordless_c16_ear_geometry, c16_chord_equiv]
discharged_by_round: 66
introduced_at_round: 66
---

# Lemma `c16_matching_corner_closed` (proved — exhaustive enumeration of the $n = 32$ matching branch)

**Claim.** Let $G$ be a cubic $\{C_4, C_8\}$-free graph on $32$
vertices containing a chordless $16$-cycle $C$ whose $16$ spokes end
in $16$ DISTINCT outside vertices (the "matching branch" of
`chordless_c16_ear_geometry`(f)). Then $G$ contains a $16$-cycle
with a chord. Consequently, in any $n = 32$ falsifier of
`share1_supply_18` (a class member all of whose $16$-cycles are
chordless), EVERY chordless $C_{16}$ has an outside vertex catching
$\ge 2$ spokes; combined with part (e) of
`chordless_c16_ear_geometry`, in every class member at
$24 \le n \le 32$ with all $C_{16}$s chordless, every $C_{16}$
carries a multi-spoke ear apex. The $n = 32$ "tight end" flagged in
Sections 101–105 is closed.

**Step 1 — the matching branch determines the whole graph.** By
`chordless_c16_ear_geometry`(f): spokes form a perfect matching
$C \to V \setminus C$, every $C$-to-outside edge is a spoke, and the
outside graph is $2$-regular — a disjoint union of cycles
$D_1, \dots, D_r$ with $\sum |D_i| = 16$. Edge count:
$16$ ($C$) $+ 16$ (spokes) $+ 16$ (outside rings) $= 48 = 3 \cdot 32 / 2$ —
ALL edges of $G$. So $G$ is completely specified by (i) the partition
$(|D_1|, \dots, |D_r|)$ of $16$ and (ii) the *feet map*: for each
$D_i$ its cyclic sequence of spoke feet, a bijection onto
$\mathbb{Z}_{16}$ (positions on $C$).

**Step 2 — class membership is EQUIVALENT to a finite constraint
system.** In such a graph every cycle $Z$ is of one of four kinds:

1. $Z \subseteq C$: then $Z = C$ (inside $V(C)$ the only edges are
   $C$-edges), length $16$.
2. $Z \subseteq$ outside: the outside graph is $2$-regular, so
   $Z = D_i$, length $|D_i|$.
3. $Z$ alternates once: one $C$-arc (length $a \ge 1$) + one
   $D_i$-path with both spokes (edge count $k \ge 3$). Length
   $a + k$, and the complementary-arc cycle has length $(16-a)+k$.
4. $Z$ alternates $t \ge 2$ times: length
   $\sum_j a_j + \sum_j k_j \ge t \cdot (1 + 3)$; for $t = 2$
   equality at length $8$ forces $a_1 = a_2 = 1$ and
   $k_1 = k_2 = 3$ (two single outside edges, feet pairwise
   adjacent); $t \ge 3$ gives length $\ge 12$.

Hence $c_4 = c_8 = 0$ holds **iff**:

- (P) every $|D_i| \notin \{4, 8\}$ (kind 2; kind 1 is length 16);
- (A) for every pair $u, v$ in the same $D_i$ at ring distance
  $\delta$, and each of the two $u$–$v$ ring paths (edge counts
  $k = \delta + 2$ and $k = (|D_i| - \delta) + 2$ including spokes),
  the min-form arc distance $m$ of their feet avoids
  $\{4 - k, 8 - k\} \cap [1, 8]$ (kind 3: $a + k \in \{4, 8\}$ or
  $(16 - a) + k \in \{4, 8\}$, and
  $16 - (12 + k) = 4 - k$, $16 - (8 + k) = 8 - k$ fold into the same
  min-form set);
- (B) no two vertex-disjoint outside edges $(u, v), (u', v')$ have
  parallel-adjacent feet pairs
  ($m(f_u, f_{u'}) = 1 \wedge m(f_v, f_{v'}) = 1$, or crosswise) —
  the kind-4 $t = 2$ octagon
  $f_u\,u\,v\,f_v\,f_{v'}\,v'\,u'\,f_{u'}$.

(Only-if is immediate: each violated constraint exhibits a $C_4$ or
$C_8$. If: the four kinds are exhaustive and each is handled.)

**Step 3 — exhaustive enumeration.** The allowed partitions of $16$
into parts $\ge 3$, $\ne 4, 8$ are exactly ten. DFS over feet maps
with rotation of $C$ fixed (the first — largest — outside cycle's
traversal starts at the vertex with foot $0$; each later cycle
starts at its minimal unused foot; both traversal directions and
reflections are enumerated redundantly, which is harmless), pruning
by (A)/(B) incrementally and re-checking (A) in full plus (P) at
closure. Every surviving configuration was BUILT as a graph and
re-verified from scratch: $c_4 = c_8 = 0$ by direct cycle count.
Result (configs per partition, every one a verified class member —
confirming Step 2's equivalence empirically as well):

| partition | configs | partition | configs |
|---|---|---|---|
| $(16)$ | 3104 | $(9,7)$ | 864 |
| $(13,3)$ | 2028 | $(7,6,3)$ | 504 |
| $(11,5)$ | 924 | $(7,3,3,3)$ | 784 |
| $(10,6)$ | 2280 | $(6,5,5)$ | 384 |
| $(10,3,3)$ | 4240 | $(5,5,3,3)$ | 144 |

Total: **15,256** graphs (up to rotation; reflections/directions
double-counted). For every single one, a full $C_{16}$ enumeration
found a $16$-cycle with a chord: **15,256 / 15,256 chorded, 0
all-chordless.** (Runtime $\approx 9$ min in CPython; the CHECK
below re-runs the smallest partition's full census plus a
deterministic spot sample of every other partition inside the
harness budget.)

**Step 4 — consequences.**

1. An $n = 32$ class member in which some chordless $C_{16}$ has no
   multi-spoke apex IS (after rotating $C$) one of the 15,256 — and
   therefore has a chorded $C_{16}$. Contrapositive: in an $n = 32$
   all-chordless falsifier, every $C_{16}$ has a multi-spoke ear
   apex.
2. With `chordless_c16_ear_geometry`(e) ($n \le 31$ pigeonhole):
   **in every class member at $24 \le n \le 32$ whose $C_{16}$s are
   all chordless, every $C_{16}$ carries an ear apex with feet
   distance $d \in \{1, 3, 4, 5, 7, 8\}$** (girth-$5$:
   $\{3,4,5,7,8\}$). The supply question is now: derive a
   contradiction (or a chorded $C_{16}$) from a $C_{16}$ + ear apex
   configuration — with NO matching escape at any in-range order.
3. The enumeration also shows the matching branch is far from
   vacuous: it contains thousands of genuine class members at
   $n = 32$ (each a cubic $\{C_4,C_8\}$-free graph, novel supply of
   in-class states for future hunts) — but every one of them
   satisfies the supply lemma via a chorded $C_{16}$.

<!-- CHECK
# CHECK — re-derivation inside the harness budget: (i) the full
# census of partition (5,5,3,3): exactly 144 configs, each a
# verified class member (c4=c8=0 by direct count on the built
# graph) WITH a chorded C16; (ii) the first 5 DFS configs of each
# of the other nine partitions: same verification.
from itertools import combinations
from collections import deque

def md16(a, b):
    d = abs(a - b) % 16
    return min(d, 16 - d)

def excl_for_k(k):
    return {x for x in (4 - k, 8 - k) if 1 <= x <= 8}

def pair_excl(l):
    return {dl: excl_for_k(dl + 2) | excl_for_k((l - dl) + 2)
            for dl in range(1, l // 2 + 1)}

def solve(partition, cap):
    n_cyc = len(partition); used = [False] * 16
    cycles = [[] for _ in range(n_cyc)]
    excl = [pair_excl(l) for l in partition]
    edges = []; sols = []
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
        if len(sols) >= cap: return
        if ci == n_cyc:
            sols.append([list(c) for c in cycles]); return
        L = partition[ci]; cyc = cycles[ci]
        if len(cyc) == L:
            rec(ci + 1); return
        if not cyc:
            starts = [0] if ci == 0 else [min(p for p in range(16) if not used[p])]
        else:
            starts = range(16)
        for p in starts:
            if used[p]: continue
            cyc.append(p); used[p] = True
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
            cyc.pop(); used[p] = False
    rec(0)
    return sols

def build(partition, cycles):
    adj = [[] for _ in range(32)]
    def add(a, b): adj[a].append(b); adj[b].append(a)
    for i in range(16): add(i, (i + 1) % 16)
    base = 16
    for cyc in cycles:
        L = len(cyc)
        for i in range(L):
            add(base + i, base + (i + 1) % L)
            add(base + i, cyc[i])
        base += L
    return adj

def class_and_chorded(adj):
    n = 32
    c4 = c8 = 0; chorded = False
    for s in range(n):
        d = [n + 1] * n; d[s] = 0; q = deque([s])
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
                    if path[1] < path[-1]:
                        if len(path) == 4: c4 += 1
                        if len(path) == 8: c8 += 1
                        if len(path) == 16 and not chorded:
                            onC = set(path)
                            idx = {x: i for i, x in enumerate(path)}
                            for i, x in enumerate(path):
                                for y in adj[x]:
                                    if y in onC and abs(i - idx[y]) not in (1, 15):
                                        chorded = True
                    continue
                if w < s or (mask >> w) & 1: continue
                if len(path) + d[w] > 16: continue
                stack.append((w, mask | (1 << w), path + [w]))
    return c4 == 0 and c8 == 0, chorded

PARTS = [(16,), (13, 3), (11, 5), (10, 6), (10, 3, 3), (9, 7),
         (7, 6, 3), (7, 3, 3, 3), (6, 5, 5), (5, 5, 3, 3)]

# Full census of the smallest partition: exactly 144 configs, every one a
# class member with a chorded C16.
sols = solve((5, 5, 3, 3), cap=10**9)
assert len(sols) == 144, len(sols)
for cyc in sols:
    is_mem, ch = class_and_chorded(build((5, 5, 3, 3), cyc))
    assert is_mem and ch, cyc

# Deterministic spot-check: first 5 DFS configs of every other partition.
for part in PARTS[:-1]:
    for cyc in solve(part, cap=5):
        is_mem, ch = class_and_chorded(build(part, cyc))
        assert is_mem and ch, (part, cyc)
CHECK -->
