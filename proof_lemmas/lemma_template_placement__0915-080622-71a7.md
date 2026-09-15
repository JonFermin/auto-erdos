---
id: template_placement
status: open
depends_on: [c16_d1_ear_cover, fragile_pair_geometry]
discharged_by_round: null
introduced_at_round: 89
---

# Lemma `template_placement` (open — the placement law: L1-less, L2-less menus carry the template; s=2/s=2 L3 catalog proved)

**Setting.** As `c16_d1_ear_cover`: $G$ connected cubic
$\{C_4, C_8\}$-free, $C$ a chordless $16$-cycle, a legal $\tau \ge 2$
landing at feet distance $d = 1$, interior ears
$(\mathrm{lo}, \mathrm{hi}, s)$ in the long-arc coordinate with
$1 \le \mathrm{lo} < \mathrm{hi} \le 14$, span
$\delta := \mathrm{hi} - \mathrm{lo}$, shortening $\delta - s$. The
**template** is a valid s$2$/s$2$ L3 pair with span set $\{3, 8\}$ —
in $(c, s, \text{shortening})$ terms $((3,2,1), (8,2,6))$, the shape
of all $270$ template-fragile critical pairs of
`fragile_pair_geometry`.

**Statement (open — the placement law).** Every legal $\tau \ge 2$,
$d = 1$ landing whose menu admits NO L1 and NO L2 admits a template
L3 pair — with the single named exception
$(\mathrm{n28r3}, 17, 25, 24, 5, 26, 6)$, whose menu has no
s$2$/s$2$ valid pair at all and is covered by a mixed
$((7,2,5), (7,3,6))$ L3 pair. This, plus a proof that the exception
class stays finite/named, is exactly the remaining supply gap of
`c16_d1_ear_cover` (its L3 arm).

**T1 — the s$2$/s$2$ L3 span catalog (proved).** In any menu of an
L1-less landing, a valid s$2$/s$2$ L3 pair has unordered span pair in

$$\{3,4\},\ \{3,8\},\ \{4,7\},\ \{4,9\},\ \{7,8\},\ \{7,12\},\ \{8,9\},\ \{8,11\}.$$

*Proof.* Write the pair $e_1 = (\mathrm{lo}_1, \mathrm{hi}_1, 2)$,
$e_2 = (\mathrm{lo}_2, \mathrm{hi}_2, 2)$ with
$\mathrm{lo}_1 < \mathrm{lo}_2 \le \mathrm{hi}_1 < \mathrm{hi}_2$,
$a := \mathrm{lo}_2 - \mathrm{lo}_1 \ge 1$,
$b := \mathrm{hi}_2 - \mathrm{hi}_1 \ge 1$. L3 validity forces
$a + b = s_1 + s_2 + 3 = 7$, so $1 \le a \le 6$ and
$\delta_2 = \delta_1 + 7 - 2a$ (`fragile_pair_geometry` P1: opposite
parity). The constraints are:
(i) $a \le \delta_1$ (interleaving $\mathrm{lo}_2 \le \mathrm{hi}_1$);
(ii) $\delta_1 + 7 - a \le 13$ (positions: $\mathrm{lo}_1 \ge 1$ and
$\mathrm{hi}_2 = \mathrm{lo}_1 + \delta_1 + b \le 14$);
(iii) $\delta_1, \delta_2 \in \{1, 3, 4, 7, 8, 9, 11, 12, 13\}$ — an
$s = 2$ ear has $\delta \notin \{2, 6, 10, 14\}$ by the exclusion law
(E2)(i) of `c16_d1_ear_cover`, and $\delta \ne 5$ because a
$\delta = 5$, $s = 2$ ear has shortening $3$, i.e. is an L1 ear,
contradicting L1-lessness.
Enumerating $\delta_1$ over the nine allowed values and
$a \in \{1, \dots, \min(6, \delta_1)\}$: $\delta_1 = 1$ gives only
$\delta_2 = 6$ (excluded); $\delta_1 = 3$ gives $\{3,8\}$ ($a=1$) and
$\{3,4\}$ ($a=3$); $\delta_1 = 4$ gives $\{4,9\}$, $\{4,7\}$,
$\{3,4\}$ ($a = 1, 2, 4$; $a = 3$ hits $\delta_2 = 5$); $\delta_1 = 7$
gives $\{7,12\}$, $\{7,8\}$, $\{4,7\}$ ($a = 1, 3, 5$); $\delta_1 = 8$
gives $\{8,11\}$, $\{8,9\}$, $\{7,8\}$, $\{3,8\}$ ($a = 2, 3, 4, 6$;
$a = 1$ fails (ii): width $14$); $\delta_1 = 9$ gives $\{8,9\}$
($a=4$), $\{4,9\}$ ($a=6$); $\delta_1 = 11$ gives $\{8,11\}$ ($a=5$);
$\delta_1 = 12$ gives $\{7,12\}$ ($a=6$); $\delta_1 = 13$ fails (ii)
for every $a$ (width $\ge 14$). No other value of $\delta_2$ survives
(iii). $\square$

**T2 — L2-lessness kills $\{3,4\}$ (proved).** The catalog's
$\{3,4\}$ pair has a UNIQUE realization: $\delta_1 = 3$ forces
$a = 3$ (T1's enumeration), i.e.
$\mathrm{lo}_2 = \mathrm{lo}_1 + 3 = \mathrm{hi}_1$ — the two ears
are in the degenerate-sequential position
$\mathrm{hi}_1 = \mathrm{lo}_2$ (likewise from the $\delta_1 = 4$
side, $a = 4$). Their shortenings are $1 + 2 = 3$ and their
interiors are disjoint, so the SAME pair is a valid L2 pair (L2
permits $\mathrm{hi}_1 = \mathrm{lo}_2$: single-vertex middle arc).
Hence in an L2-less menu no $\{3,4\}$ pair exists, and the feasible
s$2$/s$2$ catalog shrinks to SEVEN span pairs, of which the template
$\{3, 8\}$ is the only one the census below ever realizes in an
L1-less, L2-less menu. $\square$

**Census (probe record, R89 — corpus + walk slice, CHECK-pinned
below).** Over the $1{,}629$ corpus landings plus the $2{,}376$
walk-slice landings (rng 86, 66 members):

- **Placement law holds, $270/271$.** L1-less, L2-less landings:
  $7$ corpus (the L3-only seven) $+ 264$ walk. All but
  $(\mathrm{n28r3}, 17, \dots)$ contain the template; each of the
  $270$ has s$2$/s$2$ span-set family EXACTLY $\{\{3,8\}\}$ — no
  L2-less menu anywhere realizes a second s$2$/s$2$ shape. The
  n28r3 exception has NO s$2$/s$2$ pair (its $s = 2$ spans are
  $\{1, 4, 7, 11\}$: no odd/even pair at offset sum $7$ fits) and
  is covered by $((7,2,5),(7,3,6))$.
- **Catalog is tight-ish.** Corpus-wide (L1-less menus), six of the
  seven surviving catalog pairs occur: $\{3,8\}$ ($16$ menus),
  $\{4,7\}$ ($7$), $\{4,9\}$, $\{7,8\}$, $\{7,12\}$, $\{8,9\}$
  ($1$ each); $\{8,11\}$ occurs in L1-present menus only; $\{3,4\}$
  never occurs (consistent with T2 — its host menus would carry the
  L2 anyway). Non-template pairs occur ONLY in menus that also
  admit an L2 (hypothesis H2 below).
- **Fragility $=$ L3-onlyness on the walk.** The walk's fragile set
  (R88's $264$) IS its L1-less-L2-less set — identical $264$; on
  the corpus, fragile $=$ L3-only seven $\cup$ the L2-unique
  n28r4 landing. So template-fragility and L3-only coverage are the
  same phenomenon up to the named n28r4 landing.
- **Deficit correlation.** Antipodal ($\delta = 8$, $s = 2$) supply
  is NOT forced by L1-lessness alone: $23/86$ corpus L1-less menus
  have it. It is the L2-less stratum that always carries it
  (via the template), $270/271$.

**Open (the two-step supply core).**
- **H1 (existence):** every L1-less, L2-less menu outside a
  finite named exception class contains SOME valid s$2$/s$2$ L3
  pair. (E3 gives one $s = 2$ ear; nothing yet forces a second at
  compatible position.)
- **H2 (collapse):** an L1-less menu containing a valid s$2$/s$2$
  pair with span set $\ne \{3,8\}$ admits an L2. True on all data
  ($482$ L1-less menus). H1 $+$ H2 $+$ T1 $+$ T2 $\Rightarrow$ the
  placement law with exception class $=$ menus with no s$2$/s$2$
  pair (n28r3-type), which would then need its own finite
  treatment. Attack order: H2 first — it is per-span-pair case
  analysis ($6$ cases), each case a concrete arithmetic question
  about what else the menu must contain; the walk census gives
  falsification pressure cheaply (any L2-less menu with a
  non-template s$2$/s$2$ pair kills H2).

<!-- CHECK
# CHECK A - R89 placement law + catalog on the four hosting reps
# (n26, n28r1, n28r3, n28r4 — every corpus L1&L2-less landing lives here):
# (i) the L1-less, L2-less landings are EXACTLY the seven pinned idents;
# (ii) six of them have s2/s2 valid-L3 span-set family exactly {{3,8}}
#      (the template, present and unique);
# (iii) the n28r3 exception has NO s2/s2 valid pair and carries the mixed
#      ((7,2,5),(7,3,6)) pair;
# (iv) EVERY s2/s2 valid L3 pair in EVERY L1-less landing of these hosts
#      has unordered span pair inside the proved 8-catalog (T1).
from collections import deque
def to_adj(flat, n):
    nums = [int(x) for x in flat.split(",")]
    adj = [[] for _ in range(n)]
    for a, b in zip(nums[::2], nums[1::2]):
        adj[a].append(b); adj[b].append(a)
    return adj
R28 = {"n28r1": "0,1,0,15,0,16,1,2,1,16,2,3,2,18,3,4,3,23,4,5,4,17,5,6,5,21,6,7,6,25,7,8,7,22,8,9,8,20,9,10,9,20,10,11,10,19,11,12,11,19,12,13,12,26,13,14,13,24,14,15,14,27,15,27,16,17,17,18,18,19,20,21,21,22,22,23,23,24,24,25,25,26,26,27", "n28r3": "0,1,0,15,0,16,1,2,1,21,2,3,2,17,3,4,3,18,4,5,4,16,5,6,5,24,6,7,6,26,7,8,7,17,8,9,8,18,9,10,9,27,10,11,10,27,11,12,11,19,12,13,12,25,13,14,13,22,14,15,14,20,15,23,16,17,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27", "n28r4": "0,1,0,15,0,16,1,2,1,16,2,3,2,21,3,4,3,17,4,5,4,23,5,6,5,25,6,7,6,18,7,8,7,18,8,9,8,26,9,10,9,19,10,11,10,19,11,12,11,22,12,13,12,20,13,14,13,24,14,15,14,27,15,27,16,17,17,18,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27"}
FLAT26 = "0,1,0,15,0,16,1,2,1,16,2,3,2,17,3,4,3,17,4,5,4,16,5,6,5,18,6,7,6,18,7,8,7,23,8,9,8,20,9,10,9,24,10,11,10,17,11,12,11,21,12,13,12,19,13,14,13,22,14,15,14,22,15,25,18,19,19,20,20,21,21,22,23,24,23,25,24,25"
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
def ears_full(adj, vsC, banned, maxs=10):
    out = []
    for x in range(len(adj)):
        if x not in vsC: continue
        for w in adj[x]:
            if w in vsC or w in banned: continue
            stack = [(w, [x, w])]
            while stack:
                cur, path = stack.pop()
                for t in adj[cur]:
                    if t in banned: continue
                    if t in vsC:
                        if t != x and len(path) <= maxs:
                            out.append((x, t, len(path), frozenset(path[1:])))
                        continue
                    if t in path: continue
                    if len(path) >= maxs: continue
                    stack.append((t, path + [t]))
    seen = set(); res = []
    for x, y, s, iv in out:
        k = (min(x, y), max(x, y), s, iv)
        if k not in seen: seen.add(k); res.append((x, y, s, iv))
    return res
def hits1(EE):
    return [e for e in EE if e[1] - e[0] - e[2] == 3]
def hits2(EE):
    return [(e1, e2) for e1 in EE for e2 in EE
            if e1 is not e2 and e1[1] <= e2[0]
            and (e1[1]-e1[0]-e1[2]) + (e2[1]-e2[0]-e2[2]) == 3
            and not (e1[3] & e2[3])]
def hits3(EE):
    return [(e1, e2) for e1 in EE for e2 in EE
            if e1 is not e2 and e1[0] < e2[0] <= e1[1] < e2[1]
            and (e2[1]-e1[1]) + (e2[0]-e1[0]) == e1[2]+e2[2]+3
            and not (e1[3] & e2[3])]
CAT8 = {(3, 4), (3, 8), (4, 7), (4, 9), (7, 8), (7, 12), (8, 9), (8, 11)}
N28R3 = ("n28r3", 17, 25, 24, 5, 26, 6)
EXPECT_L3ONLY = {("n26", 7, 19, 12, 11, 20, 21), ("n26", 8, 20, 19, 12, 21, 11),
    ("n28r1", 8, 3, 2, 18, 4, 17), ("n28r1", 16, 4, 3, 2, 17, 18),
    ("n28r1", 18, 24, 13, 12, 25, 26), ("n28r1", 19, 25, 24, 13, 26, 12), N28R3}
graphs = [("n26", to_adj(FLAT26, 26))] + [(k, to_adj(v, 28)) for k, v in R28.items()]
l3only = set()
for name, adj in graphs:
    n = len(adj)
    chl = [(vs, es, path) for vs, es, path in all_c16(adj)
           if not any(b in vs and frozenset((a, b)) not in es
                      for a in path for b in adj[a])]
    for ci, (vs, es, path) in enumerate(chl):
        vsC = set(vs)
        for v in range(n):
            if v in vsC or any(t in vsC for t in adj[v]): continue
            if dist_to(adj, v, vsC) != 2: continue
            tn = [(w, [f for f in adj[w] if f in vsC]) for w in adj[v]]
            tn = [(w, F) for w, F in tn if F]
            if len(tn) < 2: continue
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    u1, F1 = tn[a]; u2, F2 = tn[b]
                    for f1 in F1:
                        for f2 in F2:
                            if arc_dist(path, f1, f2) != 1: continue
                            i2 = path.index(f2); i1 = path.index(f1)
                            if (i1 - i2) % 16 == 1:
                                order = [path[(i2 - t) % 16] for t in range(16)]
                            else:
                                order = [path[(i2 + t) % 16] for t in range(16)]
                            pm = {vtx: t for t, vtx in enumerate(order)}
                            E = []
                            for x, y, s, iv in ears_full(adj, vsC, {u1, v, u2}):
                                px, py = pm[x], pm[y]
                                if 1 <= px <= 14 and 1 <= py <= 14 and px != py:
                                    E.append((min(px, py), max(px, py), s, iv))
                            if hits1(E): continue
                            ident = (name, ci, v, u1, f1, u2, f2)
                            p3 = hits3(E)
                            s22 = set(tuple(sorted((e1[1]-e1[0], e2[1]-e2[0])))
                                      for e1, e2 in p3 if e1[2] == 2 and e2[2] == 2)
                            for sp in s22:
                                assert sp in CAT8, ("catalog violation", ident, sp)
                            if hits2(E): continue
                            l3only.add(ident)
                            if ident == N28R3:
                                assert not s22, ("n28r3 grew an s2/s2 pair", s22)
                                shapes = set()
                                for e1, e2 in p3:
                                    sh = tuple(sorted(
                                        (min(e[1]-e[0], 16-(e[1]-e[0])), e[2],
                                         e[1]-e[0]-e[2]) for e in (e1, e2)))
                                    shapes.add(sh)
                                assert ((7, 2, 5), (7, 3, 6)) in shapes, shapes
                            else:
                                assert s22 == {(3, 8)}, ("template missing/impure",
                                                         ident, s22)
assert l3only == EXPECT_L3ONLY, sorted(l3only)
print("CHECK A ok: 7 L1&L2-less landings pinned — 6x template {3,8}",
      "(present AND the only s2/s2 shape), n28r3 exception has no s2/s2",
      "pair and carries ((7,2,5),(7,3,6)); s2/s2 catalog holds on 4 hosts")
CHECK
-->

<!-- CHECK
# CHECK B - R89 placement law on the walk slice (rng 86, the CHECK-5 walk
# of c16_d1_ear_cover): 66 class members, 2,376 legal tau>=2 d=1 landings,
# 396 L1-less of which 264 L1&L2-less. Asserts: every s2/s2 valid L3 pair
# in an L1-less menu is inside the T1 8-catalog, and EVERY L1&L2-less menu
# has s2/s2 span-set family exactly {{3,8}} — the template is present and
# is the only s2/s2 shape (the placement law, zero exceptions here).
import random
from collections import deque
def to_adj(flat, n):
    nums = [int(x) for x in flat.split(",")]
    adj = [[] for _ in range(n)]
    for a, b in zip(nums[::2], nums[1::2]):
        adj[a].append(b); adj[b].append(a)
    return adj
REPS28_1 = "0,1,0,15,0,16,1,2,1,16,2,3,2,18,3,4,3,23,4,5,4,17,5,6,5,21,6,7,6,25,7,8,7,22,8,9,8,20,9,10,9,20,10,11,10,19,11,12,11,19,12,13,12,26,13,14,13,24,14,15,14,27,15,27,16,17,17,18,18,19,20,21,21,22,22,23,23,24,24,25,25,26,26,27"
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
def ears_full(adj, vsC, banned, maxs=10):
    out = []
    for x in range(len(adj)):
        if x not in vsC: continue
        for w in adj[x]:
            if w in vsC or w in banned: continue
            stack = [(w, [x, w])]
            while stack:
                cur, path = stack.pop()
                for t in adj[cur]:
                    if t in banned: continue
                    if t in vsC:
                        if t != x and len(path) <= maxs:
                            out.append((x, t, len(path), frozenset(path[1:])))
                        continue
                    if t in path: continue
                    if len(path) >= maxs: continue
                    stack.append((t, path + [t]))
    seen = set(); res = []
    for x, y, s, iv in out:
        k = (min(x, y), max(x, y), s, iv)
        if k not in seen: seen.add(k); res.append((x, y, s, iv))
    return res
def hits1(EE):
    return [e for e in EE if e[1] - e[0] - e[2] == 3]
def hits2(EE):
    return [(e1, e2) for e1 in EE for e2 in EE
            if e1 is not e2 and e1[1] <= e2[0]
            and (e1[1]-e1[0]-e1[2]) + (e2[1]-e2[0]-e2[2]) == 3
            and not (e1[3] & e2[3])]
def hits3(EE):
    return [(e1, e2) for e1 in EE for e2 in EE
            if e1 is not e2 and e1[0] < e2[0] <= e1[1] < e2[1]
            and (e2[1]-e1[1]) + (e2[0]-e1[0]) == e1[2]+e2[2]+3
            and not (e1[3] & e2[3])]
def c4free(adj):
    n = len(adj); bits = [0]*n
    for a in range(n):
        for b in adj[a]: bits[a] |= 1 << b
    for a in range(n):
        for b in range(a+1, n):
            c = bits[a] & bits[b] & ~(1 << a) & ~(1 << b)
            if c and (c & (c-1)): return False
    return True
def c8free(adj):
    n = len(adj)
    for s0 in range(n):
        stack = [(u, (1 << s0) | (1 << u), 2) for u in adj[s0] if u > s0]
        while stack:
            vv, mask, ln = stack.pop()
            for w in adj[vv]:
                if w == s0:
                    if ln == 8: return False
                    continue
                if w < s0 or (mask >> w) & 1 or ln >= 8: continue
                stack.append((w, mask | (1 << w), ln+1))
    return True
def conn(adj):
    seen = {0}; q = deque([0])
    while q:
        a = q.popleft()
        for b in adj[a]:
            if b not in seen: seen.add(b); q.append(b)
    return len(seen) == len(adj)
def d1_menus(adj):
    n = len(adj)
    for vs, es, path in all_c16(adj):
        ch = False
        for a in path:
            for b in adj[a]:
                if b in vs and frozenset((a, b)) not in es: ch = True
        if ch: continue
        vsC = set(vs)
        for v in range(n):
            if v in vsC or any(t in vsC for t in adj[v]): continue
            if dist_to(adj, v, vsC) != 2: continue
            tn = [(w, [f for f in adj[w] if f in vsC]) for w in adj[v]]
            tn = [(w, F) for w, F in tn if F]
            if len(tn) < 2: continue
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    u1, F1 = tn[a]; u2, F2 = tn[b]
                    for f1 in F1:
                        for f2 in F2:
                            if arc_dist(path, f1, f2) != 1: continue
                            i2 = path.index(f2); i1 = path.index(f1)
                            if (i1 - i2) % 16 == 1:
                                order = [path[(i2 - t) % 16] for t in range(16)]
                            else:
                                order = [path[(i2 + t) % 16] for t in range(16)]
                            pm = {vtx: t for t, vtx in enumerate(order)}
                            E = []
                            for x, y, s, iv in ears_full(adj, vsC, {u1, v, u2}):
                                px, py = pm[x], pm[y]
                                if 1 <= px <= 14 and 1 <= py <= 14 and px != py:
                                    E.append((min(px, py), max(px, py), s, iv))
                            yield E
CAT8 = {(3, 4), (3, 8), (4, 7), (4, 9), (7, 8), (7, 12), (8, 9), (8, 11)}
rng = random.Random(86)
wadj = to_adj(REPS28_1, 28)
acc = att = 0; n_l1less = n_l2less = 0
while acc < 100 and att < 8000:
    att += 1
    eds = [(a, b) for a in range(28) for b in wadj[a] if a < b]
    (a, b) = rng.choice(eds); (c, d) = rng.choice(eds)
    if len({a, b, c, d}) != 4: continue
    pr = ((a, c), (b, d)) if rng.random() < 0.5 else ((a, d), (b, c))
    if any(y in wadj[x] for x, y in pr): continue
    cand = [list(nb) for nb in wadj]
    for x, y in ((a, b), (c, d)):
        cand[x].remove(y); cand[y].remove(x)
    for x, y in pr:
        cand[x].append(y); cand[y].append(x)
    if not (c4free(cand) and c8free(cand) and conn(cand)): continue
    wadj = cand; acc += 1
    for E in d1_menus(wadj):
        if hits1(E): continue
        n_l1less += 1
        s22 = set(tuple(sorted((e1[1]-e1[0], e2[1]-e2[0])))
                  for e1, e2 in hits3(E) if e1[2] == 2 and e2[2] == 2)
        for sp in s22:
            assert sp in CAT8, ("WALK catalog violation", acc, sp)
        if hits2(E): continue
        n_l2less += 1
        assert s22 == {(3, 8)}, ("WALK placement falsifier", acc, s22)
assert (acc, n_l1less, n_l2less) == (66, 396, 264), (acc, n_l1less, n_l2less)
print("CHECK B ok: walk slice — 66 members, 396 L1-less (catalog holds),",
      "264 L1&L2-less ALL with s2/s2 family exactly {{3,8}}: the template",
      "is present and unique, zero exceptions")
CHECK
-->
