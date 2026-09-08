---
id: c16_landing_universal
status: open
depends_on: [c16_menu_dist2_supply, c16_two_routes, c16_two_route_menu]
discharged_by_round: null
introduced_at_round: 79
---

# Lemma `c16_landing_universal` (open — every legal dist-2 landing closes; conjecture + dual-attack probes)

**Statement (conjecture).** Let $G$ be a connected cubic
$\{C_4, C_8\}$-free graph on $24 \le n \le 30$ vertices, $C$ a
chordless $16$-cycle, $v$ a $0$-spoke outside vertex with
$\mathrm{dist}(v, C) = 2$ and $\tau(v) \ge 2$ T-neighbours. Then for
EVERY choice of distinct T-neighbours $u_1 \ne u_2$ and every choice
of feet $f_1 \in \mathrm{feet}(u_1)$, $f_2 \in \mathrm{feet}(u_2)$ —
all of which are legal landings by `c16_menu_dist2_supply` (a)–(b) —
there is a chorded $16$-cycle $C'$ containing the branch path
$f_1 u_1 v u_2 f_2$ with $E(C') \cap E(C) \ne \emptyset$. Any such
$C'$ has routes $(2, 2)$ at $v$ by construction.

**Why per-landing, not per-pair.** R78 reduced the dist-$2$ row of
`c16_two_route_menu` at $\tau \ge 2$ to "SOME landing closes"
(closure statement (A)). The R79 probe shows the corpus satisfies
the far stronger per-landing form: all $9{,}134$ legal landings
($3{,}474$ at $n \le 28$, $5{,}660$ at $n = 30$) close — not one
requires choosing the RIGHT landing. This is the strongest
falsifiable local form of (A): its negation is a single landing
$(C, v, u_1, f_1, u_2, f_2)$ in a class member with NO completion —
a purely local object the blob-kill style can attack, and a much
easier falsification target than the per-pair menu.

**Completion anatomy (probe record, R79).** A completion is an
$f_2 \to f_1$ path of length $12$ in $G - \{u_1, v, u_2\}$ closing a
chorded, arc-sharing $16$-cycle. Minimal completions on the corpus:
one extra off-$C$ segment ($8{,}884$ landings; segment length $2$:
$3{,}614$, $3$: $2{,}428$, $4$: $1{,}941$, $5..10$: $901$) or two
extra segments, both $\le 4$ ($250$ landings). Every feet distance
$d \in \{1,2,3,5,6,7,8\}$ closes at every observed multiplicity; a
single-arc completion is impossible ($L = 4$ would make the
complementary cycle a $C_8$ — `c16_two_route_menu`, optimality 2),
so ONE extra segment is completion-minimal, and the dominant shape
is branch path + one arc + one short segment + one arc.

**Arithmetic skeleton (proved inline).** Fix the landing with feet
gap $g$ ($d = \min(g, 16-g) \ne 4$). A one-extra-segment completion
with segment endpoints $a, b \in C \setminus \{f_1, f_2\}$ and
segment length $s$ uses two arcs totalling $12 - s$, so
$2 \le s \le 10$ (arcs $\ge 1$ each — a length-$0$ arc at BOTH ends
would put the segment endpoints on the branch feet; one zero arc is
allowed when $a = f_2$ or $b = f_1$). Every C-cycle rides along:
the second segment between its own feet at gap $h$ must satisfy
$\{h + s, 16 - h + s\} \cap \{4, 8\} = \emptyset$ (the exclusion
table of `c16_two_route_menu`), and the closed count is
automatically consistent — the probe found NO landing where the
arithmetic admits a shape but the graph denies every instance of it,
which is exactly the pigeonhole the eventual proof must formalize:
the supply of off-$C$ paths between spoke-hosts (16 spokes into
$\le 14$ outside vertices, `chordless_c16_ear_geometry` (e)) always
covers at least one admissible $(a, b, s)$ triple.

**Dual-attack record (probe BEFORE proof effort, standing policy).**
CHECKs 1–2 below re-verify the full universality claim
deterministically ($9{,}134$ landings, zero failures; enumerators
identical to `c16_two_route_menu` CHECKs). Falsifier value: a class
member + landing with no completion would kill the per-landing form
while leaving the per-pair menu (and so the arc-exchange program)
intact — it would locate exactly how much landing-choice freedom the
exchange needs.

**Consequences if proved.** `c16_landing_universal` +
`c16_menu_dist2_supply` (b) $\Rightarrow$ closure statement (A)
$\Rightarrow$ the $(2,2)$/dist-$2$ row of `c16_two_route_menu` at
$\tau \ge 2$. Together with a $\tau = 1$ closure argument (statement
(B)) and the dist-$3$ $(3,3)$ case, the full menu follows, and with
it the finite local shape list feeding `arc_exchange_witness`.

<!-- CHECK
# CHECK 1 - per-landing universality at n<=28 (n24 member, n26, twelve n28
# reps, R57 pin): every legal landing (u1 != u2 T-neighbours of a dist-2
# 0-spoke v, any feet choice) extends to a chorded C16 through the branch
# path sharing an edge with C. 3,474 landings, zero failures.
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
def dist_to(adj, v, S):
    d = {v: 0}; q = deque([v])
    while q:
        u = q.popleft()
        if u in S: return d[u]
        for w in adj[u]:
            if w not in d: d[w] = d[u]+1; q.append(w)
    return 99
def closes(adj, vsC, esC, seg):
    f1, u1, v, u2, f2 = seg
    banned = {u1, v, u2}
    stack = [(f2, [f2], False)]
    while stack:
        cur, path, sh = stack.pop()
        for w in adj[cur]:
            e_onC = frozenset((cur, w)) in esC
            if w == f1:
                if len(path) == 12 and (sh or e_onC):
                    cyc = seg + path[1:]
                    if len(set(cyc)) != 16: continue
                    es2 = set(frozenset((cyc[i], cyc[(i+1) % 16])) for i in range(16))
                    if not (esC & es2): continue
                    s2 = set(cyc)
                    for x in cyc:
                        for y in adj[x]:
                            if y in s2 and frozenset((x, y)) not in es2:
                                return True
                continue
            if w in banned or w in path or w == f2: continue
            if len(path) >= 12: continue
            stack.append((w, path + [w], sh or e_onC))
    return False
graphs = [ADJ24, to_adj(FLAT26, 26)] + [to_adj(f, 28) for f in REPS28]
gp = [[] for _ in range(28)]
for a, b in PIN28: gp[a].append(b); gp[b].append(a)
graphs.append(gp)
tot = 0
for adj in graphs:
    n = len(adj)
    cs = all_c16(adj)
    chl = []
    for vs, es, path in cs:
        ch = False
        for x in path:
            for y in adj[x]:
                if y in vs and frozenset((x, y)) not in es: ch = True
        if not ch: chl.append((vs, es, path))
    for vsC, esC, pathC in chl:
        interior = [u for u in range(n) if u not in vsC
                    and not any(t in vsC for t in adj[u])]
        for v in interior:
            if dist_to(adj, v, vsC) != 2: continue
            tn = [(u, [f for f in adj[u] if f in vsC]) for u in adj[v]]
            tn = [(u, F) for u, F in tn if F]
            if len(tn) < 2: continue
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    u1, F1 = tn[a]; u2, F2 = tn[b]
                    for f1 in F1:
                        for f2 in F2:
                            tot += 1
                            assert closes(adj, vsC, esC, [f1, u1, v, u2, f2]), \
                                ("no completion", n, sorted(vsC), v, u1, f1, u2, f2)
assert tot == 3474, tot
print("CHECK 1 ok:", tot, "landings")
CHECK -->

<!-- CHECK
# CHECK 2 - per-landing universality at n=30 (T(Petersen) + 10 slice
# members): 5,660 landings, zero failures.
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
def closes(adj, vsC, esC, seg):
    f1, u1, v, u2, f2 = seg
    banned = {u1, v, u2}
    stack = [(f2, [f2], False)]
    while stack:
        cur, path, sh = stack.pop()
        for w in adj[cur]:
            e_onC = frozenset((cur, w)) in esC
            if w == f1:
                if len(path) == 12 and (sh or e_onC):
                    cyc = seg + path[1:]
                    if len(set(cyc)) != 16: continue
                    es2 = set(frozenset((cyc[i], cyc[(i+1) % 16])) for i in range(16))
                    if not (esC & es2): continue
                    s2 = set(cyc)
                    for x in cyc:
                        for y in adj[x]:
                            if y in s2 and frozenset((x, y)) not in es2:
                                return True
                continue
            if w in banned or w in path or w == f2: continue
            if len(path) >= 12: continue
            stack.append((w, path + [w], sh or e_onC))
    return False
tot = 0
for adj in [t_pet()] + slice10():
    n = 30
    cs = all_c16(adj)
    chl = []
    for vs, es, path in cs:
        ch = False
        for x in path:
            for y in adj[x]:
                if y in vs and frozenset((x, y)) not in es: ch = True
        if not ch: chl.append((vs, es, path))
    for vsC, esC, pathC in chl:
        interior = [u for u in range(n) if u not in vsC
                    and not any(t in vsC for t in adj[u])]
        for v in interior:
            if dist_to(adj, v, vsC) != 2: continue
            tn = [(u, [f for f in adj[u] if f in vsC]) for u in adj[v]]
            tn = [(u, F) for u, F in tn if F]
            if len(tn) < 2: continue
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    u1, F1 = tn[a]; u2, F2 = tn[b]
                    for f1 in F1:
                        for f2 in F2:
                            tot += 1
                            assert closes(adj, vsC, esC, [f1, u1, v, u2, f2]), \
                                ("no completion", sorted(vsC), v, u1, f1, u2, f2)
assert tot == 5660, tot
print("CHECK 2 ok:", tot, "landings")
CHECK -->
