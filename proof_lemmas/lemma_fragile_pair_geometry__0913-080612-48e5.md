---
id: fragile_pair_geometry
status: proved
depends_on: [c16_d1_ear_cover, mod4_even_theta]
discharged_by_round: 88
introduced_at_round: 88
---

# Lemma `fragile_pair_geometry` (proved — critical-pair rigidity: fragility has essentially ONE shape)

**Setting.** Exactly as `c16_d1_ear_cover`: $G$ connected cubic
$\{C_4, C_8\}$-free, $C$ a chordless $16$-cycle, a legal
$\tau \ge 2$ landing at feet distance $d = 1$, ears written
$(\mathrm{lo}, \mathrm{hi}, s)$ in the long-arc coordinate, span
$\delta := \mathrm{hi} - \mathrm{lo}$, chord distance
$c := \min(\delta, 16 - \delta)$, shortening $\delta - s$. A
*critical ear* of a landing's menu is one whose single deletion
kills L1/L2/L3 coverage; a landing is *fragile* if it has one.
R85 pinned: exactly 8 fragile landings on the 25-host corpus, each
with exactly 2 critical ears.

**P3 — Census law (CHECK-pinned below).** On the corpus, the 8
critical pairs realize exactly THREE shapes, written as sorted
$(c, s, \text{shortening})$ pairs:

- **the template** $((3,2,1), (8,2,6))$ — SIX of eight landings
  (both n26 landings, all four n28r1 landings): an antipodal
  ($c = 8$) $s = 2$ ear interleaved with a $(c = 3, s = 2)$ ear;
- n28r3: $((7,2,5), (7,3,6))$;
- n28r4 (the L2-unique landing): $((1,2,-1), (8,4,4))$.

**Walk corroboration (probe record, Section 128 — too slow for a
CHECK).** Extending the R86 seeded 2-edge-swap walk slice (rng 86,
66 class members, 2,376 legal $d = 1$ landings) with per-landing
criticality: 264 fragile landings, and ALL 264 have critical-pair
shape exactly the template $((3,2,1), (8,2,6))$. Zero new shapes.
Fragility in this class is, empirically, ONE phenomenon: the
antipodal-plus-$(3,2)$ interleaved pair as sole coverage route.

**P1 — Template arithmetic (proved).** For an interleaved pair
$e_1 = (\mathrm{lo}_1, \mathrm{hi}_1, s_1)$,
$e_2 = (\mathrm{lo}_2, \mathrm{hi}_2, s_2)$ with
$\mathrm{lo}_1 < \mathrm{lo}_2 \le \mathrm{hi}_1 < \mathrm{hi}_2$,
the L3 one-backtrack completion $0 \to \mathrm{lo}_1$, $e_1$,
backward arc $\mathrm{hi}_1 \to \mathrm{lo}_2$, $e_2$, arc
$\mathrm{hi}_2 \to 15$ has length
$15 + s_1 + s_2 - (\mathrm{lo}_2 - \mathrm{lo}_1) -
(\mathrm{hi}_2 - \mathrm{hi}_1)$, so it is a valid ($=12$)
completion iff
$(\mathrm{lo}_2 - \mathrm{lo}_1) + (\mathrm{hi}_2 - \mathrm{hi}_1)
= s_1 + s_2 + 3$. For $s_1 = s_2 = 2$ this reads
$(\mathrm{lo}_2 - \mathrm{lo}_1) + (\mathrm{hi}_2 - \mathrm{hi}_1) = 7$:
an ODD offset sum, forcing the two spans to have OPPOSITE parity
($\delta_2 - \delta_1 =
(\mathrm{hi}_2 - \mathrm{hi}_1) - (\mathrm{lo}_2 - \mathrm{lo}_1)$
is odd exactly when the offset sum is odd). In particular an
$s = 2$ L3 pair can NEVER consist of two even-span or two odd-span
ears — the template's $\{8, 3\}$ span pair is parity-forced.
$\square$

**P2 — Theta cycle profile of the template (proved, via
`mod4_even_theta` T2).** The antipodal $s = 2$ ear has
$\delta = 8$: both its theta cycles with $C$ have length
$8 + 2 = 16 - 8 + 2 = 10 \equiv 2 \pmod 4$. By T2(b) (even span,
even length, $\delta + s \equiv 2 \bmod 4$), the only 0-mod-4
cycle in $C \cup e_A$ is $C$ itself. The $(3, 2)$ ear gives cycle
lengths $\{5, 15\}$, both odd. Hence the ENTIRE critical
apparatus of a template-fragile landing creates no even cycle
other than $C$ and no cycle of length in $\{4, 8, 16\}$ — the
two ear types whose induced cycles are maximally unconstrained by
the ambient $C_4/C_8$-free hypothesis and by power-of-2 avoidance.
(Heuristic reading: fragility survives exactly where the exclusion
laws have no purchase; every other route through the menu is
census-abundant.) The n28r3 and n28r4 exception pairs have
profiles $\{10, 12\}, \{9, 11\}$ and $\{3, 17\}, \{12, 12\}$
respectively — CHECK-verified to avoid $\{4, 8, 16\}$ throughout.

**P4 — Negative result: the naive mod-4 residue-lock is REFUTED.**
Section 127's next-move (b) hypothesized the two critical ears of
each fragile landing are mod-4 residue-locked partners. They are
not: observed $(\delta + s) \bmod 4$ pairs are $\{1, 2\}$ (the
six template landings), $\{0, 1\}$ (n28r3), $\{0, 3\}$ (n28r4)
— no single residue relation covers them. The mod-4 lens's real
yield here is P2 (cycle-length profiles), not a residue pairing.
Do not re-derive.

**Consequence for the supply core.** The open
`c16_d1_ear_cover` supply problem now has a sharply smaller
hard kernel: prove that a landing whose menu admits NO L1 and NO
disjoint sequential pair must contain the template — an antipodal
$s = 2$ ear AND an interleaved $(3, 2)$ ear at offset sum 7 (with
the two pinned exceptions handled by name). P1 shows the shape is
parity-canonical; what is missing is existence (supply) of the two
ears, which is where E3 (s=2 floor) + E4 (arc-triple law) should
be brought to bear.

<!-- CHECK
import random
from collections import deque
from itertools import combinations
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
def cov(EE):
    return bool(hits1(EE)) or bool(hits2(EE)) or bool(hits3(EE))
graphs = [("n26", to_adj(FLAT26, 26))] + [(k, to_adj(v, 28)) for k, v in R28.items()]
TEMPLATE = ((3, 2, 1), (8, 2, 6))          # (c, s, shortening) pair, sorted
EXPECT_SHAPES = {
    ("n26", 7, 19, 12, 11, 20, 21): TEMPLATE,
    ("n26", 8, 20, 19, 12, 21, 11): TEMPLATE,
    ("n28r1", 8, 3, 2, 18, 4, 17): TEMPLATE,
    ("n28r1", 16, 4, 3, 2, 17, 18): TEMPLATE,
    ("n28r1", 18, 24, 13, 12, 25, 26): TEMPLATE,
    ("n28r1", 19, 25, 24, 13, 26, 12): TEMPLATE,
    ("n28r3", 17, 25, 24, 5, 26, 6): ((7, 2, 5), (7, 3, 6)),
    ("n28r4", 2, 20, 12, 11, 21, 22): ((1, 2, -1), (8, 4, 4)),
}
found = {}
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
                            crits = [e for e in E if not cov([x for x in E if x is not e])]
                            if not crits: continue
                            ident = (name, ci, v, u1, f1, u2, f2)
                            shape = tuple(sorted(
                                (min(hi - lo, 16 - (hi - lo)), s, hi - lo - s)
                                for lo, hi, s, iv in crits))
                            found[ident] = shape
                            # P2 cycle-length profile: theta cycles d+s, 16-d+s
                            for lo, hi, s, iv in crits:
                                d = hi - lo
                                for cyc in (d + s, 16 - d + s):
                                    assert cyc not in (4, 8, 16), (ident, lo, hi, s, cyc)
assert found == EXPECT_SHAPES, (sorted(found.items()), "vs", sorted(EXPECT_SHAPES.items()))
tpl = [i for i, sh in found.items() if sh == TEMPLATE]
assert len(tpl) == 6
print("CHECK ok: fragile-8 critical-pair shapes pinned on 4 hosts —",
      "6x template ((3,2,1),(8,2,6)) + n28r3 ((7,2,5),(7,3,6)) + n28r4 ((1,2,-1),(8,4,4));",
      "all critical-ear theta cycles avoid {4,8,16}")
CHECK
-->
