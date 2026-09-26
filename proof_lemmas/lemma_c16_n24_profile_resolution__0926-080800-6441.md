---
id: c16_n24_profile_resolution
status: proved
depends_on: [c16_branch_vertex_arithmetic, c16_dip_decomposition, chordless_c16_ear_geometry]
discharged_by_round: 97
introduced_at_round: 97
---

# Lemma `c16_n24_profile_resolution` (Q85: the $n=24$, $k=1$ classification is EXACT)

**Setting.** $G$ cubic, $\{C_4, C_8\}$-free, $n = |V(G)| = 24$, $C$ a
chordless $C_{16}$ in $G$, $H := G - V(C)$ (8 vertices), $k$ the number
of $0$-spoke (branch) vertices. `c16_branch_vertex_arithmetic` (B5)
proved $k \le 1$ and that $k = 1$ forces $H$ to be one of three
profiles: $\{K_{1,3}, K_2, 2K_1\}$ (STAR, realized by adj24),
$\{S(2,1,1), 3K_1\}$ (SPIDER), or $\{C_3{+}\text{pendant}, 4K_1\}$
(TRIPEND). This lemma settles the two open profiles.

**Statement.**

- **(P1) (TRIPEND is infeasible)** No cubic $\{C_4, C_8\}$-free graph
  on $24$ vertices contains a chordless $C_{16}$ whose outside graph is
  $\{C_3{+}\text{pendant}, 4K_1\}$.
- **(P2) (SPIDER is realized)** The explicit graph **spider24** (flat
  edge list in CHECK C; vertices $0$–$15$ = the cycle $C$, $16$–$23$ =
  $H$ with $16 = c$, $17 = m$, $18 = e$, $19 = l_1$, $20 = l_2$,
  $21, 22, 23$ = the three isolated apexes; spider feet:
  $m \mapsto \{0\}$, $e \mapsto \{3,6\}$, $l_1 \mapsto \{1,2\}$,
  $l_2 \mapsto \{11,15\}$, apexes $\{4,7,8\}, \{5,9,12\}, \{10,13,14\}$)
  is cubic, connected, $\{C_4, C_8\}$-free, and has exactly $3$
  chordless $C_{16}$s, each with $k = 1$ and profile
  $\{S(2,1,1), 3K_1\}$. It is NOT isomorphic to adj24 ($3$ triangles
  vs. adj24's $7$) — the SECOND known class member at $n = 24$.
- **(P3) (rigidity)** Up to rotation–reflection of $C$ and
  $H$-automorphisms, exactly ONE feet assignment realizes SPIDER (the
  exhaustive search returns two rotation-canonical assignments, and
  they are mirror images of each other); consequently every
  $(G, C)$ with the SPIDER profile has $G \cong$ spider24.
- **(P4) (corollary — exact classification)** At $n = 24$, every
  chordless $C_{16}$ in a class member has $k \le 1$, and in the
  $k = 1$ case the profile is exactly one of $\{K_{1,3}, K_2, 2K_1\}$
  or $\{S(2,1,1), 3K_1\}$ — both realized, by adj24 and spider24
  respectively, each on all $3$ of its chordless $C_{16}$s.

## Proof

**Step 1 (a feet assignment determines $G$).** At $n = 24$,
$V(G) = V(C) \sqcup V(H)$ with $|V(H)| = 8$. The edges of $G$ are: the
$16$ cycle edges; the edges of $H$ (fixed by the hypothesized
profile); and the third edge of each $C$-vertex, which by
chordlessness leaves $C$ — a spoke (`c16_dip_decomposition` (c) /
(B0): exactly one spoke per $C$-vertex, all $16$ feet distinct, i.e.
the feet PARTITION the $16$ positions). A touched $H$-vertex $v$
carries $s(v) = 3 - \deg_H(v)$ spokes. Hence $G = G(\varphi)$ is
completely determined by the profile plus the assignment
$\varphi$ of positions $\mathbb{Z}_{16}$ to $H$-vertices with
$|\varphi^{-1}(v)| = 3 - \deg_H(v)$. Conversely any such $\varphi$
yields a cubic graph in which $C$ is a chordless $C_{16}$ with outside
graph $H$; it is connected because the unique degree-$3$ vertex of
$H$ is $H$-adjacent to touched vertices (both profiles) and every
touched vertex meets $C$. So the profile is feasible **iff** some
$\varphi$ makes $G(\varphi)$ $\{C_4, C_8\}$-free.

**Step 2 (complete cycle decomposition).** Let $D$ be any simple cycle
of $G(\varphi)$. If $D$ avoids $V(C)$ it is a cycle of $H$ — both
profiles have all components on $\le 5$ vertices whose only cycle is a
$C_3$, so $D \notin \{C_4, C_8\}$ automatically. Otherwise $D$ meets
$C$. A $C$-vertex has exactly one non-$C$ edge, so $D$ cannot enter
AND leave a $C$-vertex off-cycle: every maximal visit of $D$ to $C$
is an arc of length $\ge 1$. Between consecutive arcs, $D$ runs
spoke → simple $H$-path (length $\ell \ge 0$, possibly a single
vertex) → spoke: a *segment* of length $L = \ell + 2 \ge 2$. With $m$
arcs and $m$ segments, $|D| \ge 3m$, so $|D| \le 8$ forces
$m \le 2$. For $m = 1$: $|D| = a + L$ where $a$ is one of the two
arc lengths $\{dd, 16 - dd\}$ between the segment's feet. For
$m = 2$: the two segments' $H$-paths are vertex-disjoint (simplicity),
$|D| = L_1 + L_2 + a_1 + a_2 \ge 6$ (so never a $C_4$), and the two
arcs are position-disjoint and avoid the other segment's feet in
their interiors. Conversely every configuration of these two kinds IS
a simple cycle of $G(\varphi)$. Hence $G(\varphi)$ is
$\{C_4, C_8\}$-free **iff** $\varphi$ admits (i) no one-segment
configuration of length $4$ or $8$ (the pairwise arc-distance menu —
exactly (B3)/`chordless_c16_ear_geometry` (b)/(d) instantiated), and
(ii) no two-segment configuration of length $8$ with
$L_1 + L_2 \le 6$. The constraint system is *exactly*
$\{C_4, C_8\}$-freeness — no approximation in either direction.

**Step 3 (exhaustive normalized search).** Constraints (i)–(ii) are
invariant under rotating $C$ (relabeling positions by $+1$) and under
$H$-automorphisms preserving spoke counts. Both target profiles have
a spoke-count-$1$ vertex that is unique up to $H$-automorphism
(SPIDER: $m$; TRIPEND: $b \leftrightarrow c$ swap), so WLOG its foot
is at position $0$; interchangeable-class members (SPIDER:
$\{l_1, l_2\}$, the $3$ apexes; TRIPEND: the $4$ apexes) are WLOG
ordered by first foot. The backtracker in CHECK A assigns positions
$0..15$ in order under exactly these normalizations and prunes ONLY
on genuine violations of (i)–(ii) among already-placed feet (both
constraint families are monotone: violated once placed, violated
forever), so it visits every normalized assignment that satisfies
(i)–(ii). Results: **TRIPEND admits $0$ assignments** — with Step 1
and 2 this proves (P1); **SPIDER admits exactly $2$**, mirror images
of each other, each independently re-verified $\{C_4, C_8\}$-free by
a direct whole-graph cycle count — this proves (P2) (taking the first
as spider24) and (P3): any SPIDER realization normalizes to one of
the two, i.e. is dihedral-plus-automorphism equivalent to spider24's
assignment, and equivalent assignments give isomorphic graphs.

**(P4)** is (B5) plus (P1) plus the two realizations (adj24: CHECK C
of `c16_branch_vertex_arithmetic`; spider24: CHECK C below). $\square$

**Model validation (defense in depth).** CHECK B draws $3600$ seeded
random complete assignments across all three profiles plus the full
$32$-element dihedral orbit of spider24's assignment and asserts the
Step-2 constraint model gives the SAME verdict as a direct
$C_4$/$C_8$ count on the built $24$-vertex graph in every case — the
model is exercised on both violating and satisfying instances.

**Infrastructure note (repaired this round).** `proof_prepare.py`
extracts CHECK blocks with the closing delimiter `CHECK -->`; the
blocks of `c16_branch_vertex_arithmetic` (R96) and `pendant_9_cap`
(R~57) closed with a bare `-->` and were silently never executed by
the harness. All four orphaned blocks were run manually (all pass,
$< 0.5$ s total) and their delimiters fixed in this round's commit.

<!-- CHECK
# CHECK A — the decision search: TRIPEND has NO valid feet assignment;
# SPIDER has exactly 2 (mirror images), both directly C4/C8-verified.
from collections import deque

def profile(name):
    if name == "SPIDER":     # S(2,1,1): c,m,e,l1,l2  +  3K1
        hedges = [(0,1),(1,2),(0,3),(0,4)]
        caps = [0,1,2,2,2,3,3,3]; classes = [[3,4],[5,6,7]]; anchor = 1
    elif name == "TRIPEND":  # triangle a,b,c + pendant p at a  +  4K1
        hedges = [(0,1),(0,2),(1,2),(0,3)]
        caps = [0,1,1,2,3,3,3,3]; classes = [[4,5,6,7]]; anchor = 1
    elif name == "STAR":     # K_{1,3}: z,3 leaves  +  K2  +  2K1
        hedges = [(0,1),(0,2),(0,3),(4,5)]
        caps = [0,2,2,2,2,2,3,3]; classes = [[1,2,3],[4,5],[6,7]]; anchor = None
    assert sum(caps) == 16
    return caps, hedges, classes, anchor

def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
        if caps[u] == 0: continue
        stack = [(u, frozenset([u]))]
        while stack:
            x, used = stack.pop()
            for w in adj[x]:
                if w in used: continue
                nu = used | frozenset([w])
                if caps[w] >= 1 and u < w: paths.append((u,w,len(nu)-1,nu))
                stack.append((w, nu))
    return paths

def pair_forbidden(paths):
    forb = {}
    for u,w,ell,_ in paths:
        s = forb.setdefault((u,w), set())
        for dd in range(1,16):
            if dd+ell+2 in (4,8) or 16-dd+ell+2 in (4,8): s.add(dd)
    return forb

def two_path_pairs(paths):
    return [(paths[i], paths[j]) for i in range(len(paths))
            for j in range(i+1, len(paths))
            if paths[i][2]+paths[j][2] <= 2 and not (paths[i][3] & paths[j][3])]

def arc_set(p,q,dr):
    out = [p]; x = p
    while x != q: x = (x+dr) % 16; out.append(x)
    return out

def quad_c8(al,be,L1,ga,de,L2):
    for (b,c,d,a) in ((be,ga,de,al),(be,de,ga,al)):
        for d1 in (1,-1):
            A1 = arc_set(b,c,d1)
            if a in A1 or d in A1: continue
            for d2 in (1,-1):
                A2 = arc_set(d,a,d2)
                if b in A2 or c in A2 or set(A1) & set(A2): continue
                if L1+L2+len(A1)+len(A2)-2 == 8: return True
    return False

def seg_feet(P, feet):
    u,w,_,_ = P
    if u != w:
        return [(a,b) for a in feet[u] for b in feet[w]]
    return [(a,b) for i,a in enumerate(feet[u]) for b in feet[u][i+1:]]

def build_graph(name, feet):
    caps, hedges, _, _ = profile(name)
    adj = [[] for _ in range(24)]
    def add(a,b): adj[a].append(b); adj[b].append(a)
    for i in range(16): add(i, (i+1) % 16)
    for a,b in hedges: add(16+a, 16+b)
    for v in range(8):
        for p in feet[v]: add(16+v, p)
    return adj

def count_c4_c8(adj):
    n = len(adj); cnt = {4:0, 8:0}
    for s in range(n):
        stack = [(u, frozenset([s,u]), 1) for u in adj[s] if u > s]
        while stack:
            v, used, ln = stack.pop()
            for w in adj[v]:
                if w == s and ln >= 2:
                    if ln+1 in (4,8): cnt[ln+1] += 1
                    continue
                if w < s or w in used or ln >= 8: continue
                stack.append((w, used | frozenset([w]), ln+1))
    return {4: cnt[4]//2, 8: cnt[8]//2}

def search(name, max_sol):
    caps, hedges, classes, anchor = profile(name)
    paths = h_paths(caps, hedges)
    forb = pair_forbidden(paths)
    pairs2 = two_path_pairs(paths)
    feet = [[] for _ in range(8)]; placed = [0]*8; sols = []
    def allowed(v):
        for cl in classes:
            if v in cl:
                i = cl.index(v)
                if i > 0 and placed[cl[i-1]] == 0: return False
        return True
    def ok(v, p):
        for w in range(8):
            if not feet[w]: continue
            s = forb.get((min(v,w), max(v,w)) if v != w else (v,v))
            if s and any(q != p and (p-q) % 16 in s for q in feet[w]): return False
        for P1, P2 in pairs2:
            for (A, B) in ((P1,P2),(P2,P1)):
                u1,w1,e1,_ = A
                if v != u1 and v != w1: continue
                other = w1 if v == u1 else u1
                bf = [q for q in feet[other] if q != p]
                for b in bf:
                    for g,d in seg_feet(B, feet):
                        if len({p,b,g,d}) == 4 and (
                           quad_c8(p,b,e1+2,g,d,B[2]+2) or quad_c8(b,p,e1+2,g,d,B[2]+2)):
                            return False
        return True
    def bt(pos):
        if pos == 16:
            sols.append([list(f) for f in feet]); return len(sols) >= max_sol
        for v in range(8):
            if placed[v] >= caps[v] or not allowed(v): continue
            if anchor is not None and ((pos == 0) != (v == anchor)): continue
            if ok(v, pos):
                feet[v].append(pos); placed[v] += 1
                if bt(pos+1): return True
                feet[v].pop(); placed[v] -= 1
        return False
    bt(0)
    return sols
# CHECK A tail — the decision runs
sols_t = search("TRIPEND", 10**9)
assert sols_t == [], sols_t                      # TRIPEND: KILLED
sols_s = search("SPIDER", 10**9)
assert len(sols_s) == 2, sols_s                  # SPIDER: exactly 2 canonical
for sol in sols_s:
    g = build_graph("SPIDER", sol)
    assert all(len(set(a)) == 3 for a in g)
    assert count_c4_c8(g) == {4:0, 8:0}, sol     # direct graph verification
# the two are mirror images (reflect sol0, swap l1/l2, x-classes as sets)
r = [sorted((-p) % 16 for p in v) for v in sols_s[0]]
r[3], r[4] = r[4], r[3]
assert (r[:5] == sols_s[1][:5] and
        sorted(map(tuple, r[5:])) == sorted(map(tuple, sols_s[1][5:]))), r
assert len(search("STAR", 1)) == 1               # sanity: realized profile is feasible
print("CHECK A ok: TRIPEND 0 assignments; SPIDER exactly 2 (mirror pair), both C4/C8-free")
CHECK -->

<!-- CHECK
# CHECK B — model completeness probe: the Step-2 constraint model must agree
# with a direct C4/C8 count on random complete assignments (seeded) and on
# the full dihedral orbit of the spider witness.
from collections import deque

def profile(name):
    if name == "SPIDER":     # S(2,1,1): c,m,e,l1,l2  +  3K1
        hedges = [(0,1),(1,2),(0,3),(0,4)]
        caps = [0,1,2,2,2,3,3,3]; classes = [[3,4],[5,6,7]]; anchor = 1
    elif name == "TRIPEND":  # triangle a,b,c + pendant p at a  +  4K1
        hedges = [(0,1),(0,2),(1,2),(0,3)]
        caps = [0,1,1,2,3,3,3,3]; classes = [[4,5,6,7]]; anchor = 1
    elif name == "STAR":     # K_{1,3}: z,3 leaves  +  K2  +  2K1
        hedges = [(0,1),(0,2),(0,3),(4,5)]
        caps = [0,2,2,2,2,2,3,3]; classes = [[1,2,3],[4,5],[6,7]]; anchor = None
    assert sum(caps) == 16
    return caps, hedges, classes, anchor

def h_paths(caps, hedges):
    adj = [[] for _ in range(8)]
    for a,b in hedges: adj[a].append(b); adj[b].append(a)
    paths = [(v,v,0,frozenset([v])) for v in range(8) if caps[v] >= 2]
    for u in range(8):
        if caps[u] == 0: continue
        stack = [(u, frozenset([u]))]
        while stack:
            x, used = stack.pop()
            for w in adj[x]:
                if w in used: continue
                nu = used | frozenset([w])
                if caps[w] >= 1 and u < w: paths.append((u,w,len(nu)-1,nu))
                stack.append((w, nu))
    return paths

def pair_forbidden(paths):
    forb = {}
    for u,w,ell,_ in paths:
        s = forb.setdefault((u,w), set())
        for dd in range(1,16):
            if dd+ell+2 in (4,8) or 16-dd+ell+2 in (4,8): s.add(dd)
    return forb

def two_path_pairs(paths):
    return [(paths[i], paths[j]) for i in range(len(paths))
            for j in range(i+1, len(paths))
            if paths[i][2]+paths[j][2] <= 2 and not (paths[i][3] & paths[j][3])]

def arc_set(p,q,dr):
    out = [p]; x = p
    while x != q: x = (x+dr) % 16; out.append(x)
    return out

def quad_c8(al,be,L1,ga,de,L2):
    for (b,c,d,a) in ((be,ga,de,al),(be,de,ga,al)):
        for d1 in (1,-1):
            A1 = arc_set(b,c,d1)
            if a in A1 or d in A1: continue
            for d2 in (1,-1):
                A2 = arc_set(d,a,d2)
                if b in A2 or c in A2 or set(A1) & set(A2): continue
                if L1+L2+len(A1)+len(A2)-2 == 8: return True
    return False

def seg_feet(P, feet):
    u,w,_,_ = P
    if u != w:
        return [(a,b) for a in feet[u] for b in feet[w]]
    return [(a,b) for i,a in enumerate(feet[u]) for b in feet[u][i+1:]]

def model_valid(name, feet):
    caps, hedges, _, _ = profile(name)
    paths = h_paths(caps, hedges)
    for (u,w), s in pair_forbidden(paths).items():
        for p in feet[u]:
            for q in feet[w]:
                if p != q and (p-q) % 16 in s: return False
    for P1, P2 in two_path_pairs(paths):
        L1, L2 = P1[2]+2, P2[2]+2
        for a,b in seg_feet(P1, feet):
            for g,d in seg_feet(P2, feet):
                if quad_c8(a,b,L1,g,d,L2) or quad_c8(b,a,L1,g,d,L2): return False
    return True

def build_graph(name, feet):
    caps, hedges, _, _ = profile(name)
    adj = [[] for _ in range(24)]
    def add(a,b): adj[a].append(b); adj[b].append(a)
    for i in range(16): add(i, (i+1) % 16)
    for a,b in hedges: add(16+a, 16+b)
    for v in range(8):
        for p in feet[v]: add(16+v, p)
    return adj

def count_c4_c8(adj):
    n = len(adj); cnt = {4:0, 8:0}
    for s in range(n):
        stack = [(u, frozenset([s,u]), 1) for u in adj[s] if u > s]
        while stack:
            v, used, ln = stack.pop()
            for w in adj[v]:
                if w == s and ln >= 2:
                    if ln+1 in (4,8): cnt[ln+1] += 1
                    continue
                if w < s or w in used or ln >= 8: continue
                stack.append((w, used | frozenset([w]), ln+1))
    return {4: cnt[4]//2, 8: cnt[8]//2}

def search(name, max_sol):
    caps, hedges, classes, anchor = profile(name)
    paths = h_paths(caps, hedges)
    forb = pair_forbidden(paths)
    pairs2 = two_path_pairs(paths)
    feet = [[] for _ in range(8)]; placed = [0]*8; sols = []
    def allowed(v):
        for cl in classes:
            if v in cl:
                i = cl.index(v)
                if i > 0 and placed[cl[i-1]] == 0: return False
        return True
    def ok(v, p):
        for w in range(8):
            if not feet[w]: continue
            s = forb.get((min(v,w), max(v,w)) if v != w else (v,v))
            if s and any(q != p and (p-q) % 16 in s for q in feet[w]): return False
        for P1, P2 in pairs2:
            for (A, B) in ((P1,P2),(P2,P1)):
                u1,w1,e1,_ = A
                if v != u1 and v != w1: continue
                other = w1 if v == u1 else u1
                bf = [q for q in feet[other] if q != p]
                for b in bf:
                    for g,d in seg_feet(B, feet):
                        if len({p,b,g,d}) == 4 and (
                           quad_c8(p,b,e1+2,g,d,B[2]+2) or quad_c8(b,p,e1+2,g,d,B[2]+2)):
                            return False
        return True
    def bt(pos):
        if pos == 16:
            sols.append([list(f) for f in feet]); return len(sols) >= max_sol
        for v in range(8):
            if placed[v] >= caps[v] or not allowed(v): continue
            if anchor is not None and ((pos == 0) != (v == anchor)): continue
            if ok(v, pos):
                feet[v].append(pos); placed[v] += 1
                if bt(pos+1): return True
                feet[v].pop(); placed[v] -= 1
        return False
    bt(0)
    return sols
# CHECK B tail — the equivalence probe
import random
rng = random.Random(97)
agree = 0
for name in ("SPIDER", "TRIPEND", "STAR"):
    caps, _, _, _ = profile(name)
    for _ in range(1200):
        pos = list(range(16)); rng.shuffle(pos)
        feet = []; i = 0
        for c in caps: feet.append(sorted(pos[i:i+c])); i += c
        mv = model_valid(name, feet)
        gv = count_c4_c8(build_graph(name, feet)) == {4:0, 8:0}
        assert mv == gv, (name, feet, mv, gv)
        agree += 1
base = search("SPIDER", 1)[0]
nval = 0
for r in range(16):
    for refl in (False, True):
        feet = [sorted(((-p if refl else p) + r) % 16 for p in v) for v in base]
        mv = model_valid("SPIDER", feet)
        assert mv == (count_c4_c8(build_graph("SPIDER", feet)) == {4:0, 8:0})
        nval += mv
assert nval == 32
print("CHECK B ok:", agree, "random assignments + 32 dihedral images, model == direct check")
CHECK -->

<!-- CHECK
# CHECK C — the explicit witness spider24: cubic, connected, {C4,C8}-free,
# exactly 3 chordless C16s, each k=1 with profile {S(2,1,1), 3K1};
# triangle count 3 (adj24 has 7 -> non-isomorphic). Absorption identities hold.
from collections import deque
FLAT = ("0,1,0,15,0,17,1,2,1,19,2,3,2,19,3,4,3,18,4,5,4,21,5,6,5,22,6,7,"
        "6,18,7,8,7,21,8,9,8,21,9,10,9,22,10,11,10,23,11,12,11,20,12,13,"
        "12,22,13,14,13,23,14,15,14,23,15,20,16,17,16,19,16,20,17,18")
nums = [int(x) for x in FLAT.split(",")]
n = 24
adj = [[] for _ in range(n)]
for a, b in zip(nums[::2], nums[1::2]):
    adj[a].append(b); adj[b].append(a)
assert all(len(set(a)) == 3 for a in adj)                      # cubic, simple
seen = {0}; q = deque([0])
while q:
    v = q.popleft()
    for w in adj[v]:
        if w not in seen: seen.add(w); q.append(w)
assert len(seen) == n                                          # connected
tri = sum(1 for u in range(n) for v in adj[u] for w in adj[v]
          if u < v < w and w in adj[u])
assert tri == 3, tri            # adj24 has 7 triangles -> not isomorphic
cyc = {4: 0, 8: 0, 16: 0}
allc16 = []
for s in range(n):
    stack = [(u, frozenset([s, u]), [s, u]) for u in adj[s] if u > s]
    while stack:
        v, used, path = stack.pop()
        for w in adj[v]:
            if w == s and len(path) >= 3:
                if len(path) in cyc:
                    cyc[len(path)] += 1
                    if len(path) == 16 and path[1] < path[-1]:
                        allc16.append(tuple(path))
                continue
            if w < s or w in used or len(path) >= 16: continue
            stack.append((w, used | frozenset([w]), path + [w]))
assert cyc[4] == 0 and cyc[8] == 0, cyc                        # class membership
chordless = []
for c in allc16:
    cs = set(c); pos = {v: i for i, v in enumerate(c)}
    if all(w not in cs or abs(pos[v]-pos[w]) in (1, 15)
           for v in c for w in adj[v]):
        chordless.append(c)
assert len(chordless) == 3, len(chordless)
SPIDER = sorted([(5,0,(1,1,1,2,3)), (1,0,(0,)), (1,0,(0,)), (1,0,(0,))])
for c in chordless:
    cs = set(c)
    outside = [v for v in range(n) if v not in cs]
    hadj = {v: [w for w in adj[v] if w not in cs] for v in outside}
    spokes = {v: [w for w in adj[v] if w in cs] for v in outside}
    feet = [f for v in outside for f in spokes[v]]
    assert len(feet) == 16 and len(set(feet)) == 16            # B0
    assert sum(1 for v in outside if len(hadj[v]) == 3) == 1   # k = 1
    seen2 = set(); prof = []
    for v in outside:
        if v in seen2: continue
        comp = []; qq = deque([v]); seen2.add(v)
        while qq:
            x = qq.popleft(); comp.append(x)
            for w in hadj[x]:
                if w not in seen2: seen2.add(w); qq.append(w)
        qn = len(comp); en = sum(len(hadj[x]) for x in comp)//2
        mu = en - qn + 1
        assert sum(len(spokes[x]) for x in comp) == qn + 2 - 2*mu  # B1
        prof.append((qn, mu, tuple(sorted(len(hadj[x]) for x in comp))))
    assert sorted(prof) == SPIDER, sorted(prof)
print("CHECK C ok: spider24 is a {C4,C8}-free cubic member, 3 chordless C16s, all k=1 SPIDER; 3 triangles vs adj24's 7")
CHECK -->
