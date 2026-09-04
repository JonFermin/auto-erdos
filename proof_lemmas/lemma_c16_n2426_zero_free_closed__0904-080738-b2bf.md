---
id: c16_n2426_zero_free_closed
status: proved
depends_on: [chordless_c16_ear_geometry, c16_n28_zero_free_closed]
discharged_by_round: 70
introduced_at_round: 70
---

# Lemma `c16_n2426_zero_free_closed` (proved — the $n = 24$ zero-free corner is EMPTY and the $n = 26$ corner is a single graph with chorded $C_{16}$s; the zero-free program closes except $(2,2,1^{12})$ at $n=30$)

**Setting.** $G$ cubic $\{C_4, C_8\}$-free on $n \in \{24, 26\}$
vertices, $C$ a chordless $16$-cycle whose spoke profile is
*zero-free* (every outside vertex has $\ge 1$ spoke). Outside vertex
counts $8$ and $10$; excesses $8$ and $6$; outside edge counts
$(3(n-16)-16)/2 = 4$ and $7$. Feasible profiles (spoke counts
$\le 3$; $2$-apexes pair up as path endpoints; $1$-spoke vertices
have outside degree $2$):

- $n = 24$: $(2^8)$, $(3,2^6,1)$, $(3^2,2^4,1^2)$, $(3^3,2^2,1^3)$
  — the profile $(3^4,1^4)$ is structurally infeasible (its four
  $1$-spoke vertices would have to partition into outside cycles of
  total length $4$ with parts $\ge 3$, $\ne 4$).
- $n = 26$: $(2^6,1^4)$, $(3,2^4,1^5)$, $(3^2,2^2,1^6)$,
  $(3^3,1^7)$.

**Claim.**

(a) *($n = 24$ emptiness)* NO cubic $\{C_4, C_8\}$-free graph on
$24$ vertices contains a chordless $C_{16}$ with a zero-free
profile: all $2{,}160{,}786$ configurations across all profiles
fail the exact $C_4/C_8$ test.

(b) *($n = 26$)* Exactly $24$ labeled configurations survive
($963{,}093$ enumerated), all in profile $(3^2, 2^2, 1^6)$ with
outside structure $\{$two $3$-apexes, one path with $3$ interior
vertices, one $C_3\}$ — and they are the dihedral/direction variants
of a SINGLE new class member, which **contains chorded $C_{16}$s**
($c_3 = 5$, $c_5 = 4$, $c_6 = 7$, $c_7 = 4$, $c_9 = 13$,
$c_{16} = 281$; share-1 sum-18 supply $691 > 562$).

(c) Consequently a supply falsifier (all $C_{16}$s chordless) at
$24 \le n \le 32$ cannot realize any chordless $C_{16}$ with a
zero-free profile, EXCEPT possibly profile $(2, 2, 1^{12})$ at
$n = 30$ — every other zero-free corner in the whole range is now
closed (`c16_matching_corner_closed` $n{=}32$,
`c16_three_apex_corner_closed` $n{=}30$ $(3,1^{13})$,
`c16_n28_zero_free_closed` $n{=}28$, this lemma $n \in \{24, 26\}$).

**Proof.** The enumeration framework of
`c16_n28_zero_free_closed` (unit DFS with per-unit cycle-length
exclusion tables, cross-unit double-ear pruning, own-min cycle
canonicalization, anchored rotation, exact $C_4/C_8$ re-test of
every survivor; validated bit-for-bit against the audited R67
slice), generalized only in the structure generator (profiles from
$(n_3, n_2, n_1)$ with $3 n_3 + 2 n_2 + n_1 = 16$,
$n_3 + n_2 + n_1 = n - 16$, $n_2$ even; interiors distributed over
paths, remainder to cycles). Anchor: a $3$-apex where the profile
has one, else a $2$-apex. Per-structure counts ($n = 24$, six
structures): $(2^8)$ $5{,}616$; $(3,2^6,1)$ $27{,}228$;
$(3^2,2^4,1^2)$ $238{,}254 + 542{,}964$ (interior splits $(0,2)$,
$(1,1)$); $(3^3,2^2,1^3)$ $479{,}016 + 867{,}708$ (splits with
cycles $(3)$ resp. interiors $3$). Zero members. For $n = 26$,
$23$ structures, $963{,}093$ configurations, members only in
$(3^2,2^2,1^6)$/path-$3$/$C_3$ as claimed; every member was built
and passed the exact class test, and each contains a chorded
$C_{16}$ by full enumeration. $\square$

**The new $n = 26$ class member** (canonical representative,
$C = 0\ldots15$; apexes $16$ (feet $0,1,4$), $17$ (feet $2,3,10$);
outside path $18{-}19{-}20{-}21{-}22$ with feet
$5$|$6$,$12$,$8$,$11$|$13$ at its five vertices ($18$ and $22$ the
$2$-apexes); outside triangle $23,24,25$ with feet $14, 7, 9|15$):
see CHECK 2's edge list. It is the SECOND-smallest known class
member ($24 \le n$ was proven nonempty first at $n = 28$ by the R57
pin — this beats it), mixed-regime ($c_3 = 5$ with $c_5 = 4$), and
supply-positive ($691$).

**Program consequence.** The zero-free side of the falsifier
analysis is DONE except the $n = 30$ two-apex profile
$(2,2,1^{12})$. The open continuations are (i) that profile (large
feet-map space; needs a compiled propagator or python-sat), and
(ii) the $0$-spoke (branch-vertex) profiles, where the graph is no
longer edge-determined and local structure lemmas must replace
whole-graph exhaustion.

<!-- CHECK
# CHECK 1 — n=24 emptiness spot-audit: profile (2^8) (four adjacent
# 2-apex pairs), anchored path endpoint pair fixed at (0,1). Claim:
# exactly 1152 configurations survive pruning, ZERO pass the exact test.
# ALSO n=26 single-member slice: profile (3^2,2^2,1^6) path-3 + C3 with
# both apex feet-triples fixed at (0,1,4) and (2,3,10): exactly 4 configs
# survive, exactly 2 are class members, both with chorded C16s.
from collections import deque
MD = [[min(abs(a-b)%16, 16-abs(a-b)%16) for b in range(16)] for a in range(16)]
def exm(m):
    return frozenset(x for x in (4-m, 8-m) if 1 <= x <= 8)

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
def chorded16(adj, n):
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

def run(units, n, prefix):
    """units: list of (kind, arg); generic within-unit exclusions +
    cross-unit double-ear pruning; prefix = pre-assigned feet."""
    slots = []      # (unit, si, host, unit_base, nunit)
    for ui, (kind, arg) in enumerate(units):
        if kind == "apex":
            hosts = [0]*arg
        elif kind == "path":
            hosts = [0,0]+list(range(1,arg+1))+[arg+1,arg+1]
        else:
            hosts = list(range(arg))
        base = len(slots)
        for si, h in enumerate(hosts):
            slots.append((ui, si, h, base, len(hosts)))
    K = len(slots)
    excl = [[] for _ in range(K)]; adj1 = [[] for _ in range(K)]
    for g in range(K):
        ui, si, h, base, nh = slots[g]
        kind, arg = units[ui]
        for gj in range(base, g):
            _, sj, hj, _, _ = slots[gj]
            if kind == "cycle":
                dl = abs(h - hj); dl = min(dl, arg - dl)
                e = exm(dl+2) | exm((arg-dl)+2)
                hd = dl
            else:
                t = abs(h - hj); e = exm(t+2); hd = t
            if e: excl[g].append((gj, e))
            if hd == 1: adj1[g].append((gj, frozenset(((ui,h),(ui,hj)))))
    feet = [-1]*K; used = [False]*16
    for i, p in enumerate(prefix):
        feet[i] = p; used[p] = True
    exc = []; out = [0, []]
    def cands(g):
        ui, si, h, base, nh = slots[g]
        kind, arg = units[ui]
        if kind == "apex":
            if si == 0: return [p for p in range(16) if not used[p]]
            return [p for p in range(feet[g-1]+1, 16) if not used[p]]
        if kind == "path":
            j = arg
            if si == 0: return [p for p in range(16) if not used[p]]
            if si == 1 or si == 3+j:
                return [p for p in range(feet[g-1]+1, 16) if not used[p]]
            if si == 2+j:
                lo = feet[base] if slots[base][0] != 0 or True else -1
                # non-anchored path: last endpoint min > first endpoint min;
                # the anchored path (unit 0 when no apex) also uses this in
                # the n=24 profile below (harmless extra quotient NOT applied
                # in the full run, so only for unit>0):
                if units[ui] != units[0] or ui != 0:
                    return [p for p in range(feet[base]+1, 16) if not used[p]]
                return [p for p in range(16) if not used[p]]
            return [p for p in range(16) if not used[p]]
        if si == 0:
            lo = -1
            if ui > 0 and units[ui-1] == units[ui]:
                lo = feet[base - nh]
            return [p for p in range(16) if not used[p] and p > lo]
        return [p for p in range(feet[base]+1, 16) if not used[p]]
    def rec(g):
        if g == K:
            out[0] += 1
            adj = [[] for _ in range(n)]
            def add(a,b): adj[a].append(b); adj[b].append(a)
            for i in range(16): add(i, (i+1)%16)
            v = 16; gg = 0
            for (kind, arg) in units:
                if kind == "apex":
                    hosts = [0]*arg; nh = 1
                elif kind == "path":
                    hosts = [0,0]+list(range(1,arg+1))+[arg+1,arg+1]; nh = arg+2
                else:
                    hosts = list(range(arg)); nh = arg
                for si2, h2 in enumerate(hosts): add(v+h2, feet[gg+si2])
                if kind == "path":
                    for h2 in range(nh-1): add(v+h2, v+h2+1)
                elif kind == "cycle":
                    for h2 in range(nh): add(v+h2, v+(h2+1)%nh)
                v += nh; gg += len(hosts)
            if not has_c4(adj, n) and not has_c8(adj, n):
                out[1].append((tuple(feet), chorded16(adj, n)))
            return
        for p in cands(g):
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
    rec(len(prefix))
    return out

# n=24 (2^8): anchored pair (0,1)
cnt, mem = run([("path",0)]*4, 24, [0,1])
assert cnt == 1152, cnt
assert mem == [], mem
# n=26 (3^2,2^2,1^6): both apexes fixed
cnt, mem = run([("apex",3),("apex",3),("path",3),("cycle",3)], 26,
               [0,1,4,2,3,10])
assert cnt == 4, cnt
assert len(mem) == 2 and all(c for _, c in mem), mem
assert sorted(f[13] for f, _ in mem) == [7, 7] and \
       sorted((f[14], f[15]) for f, _ in mem) == [(9, 15), (15, 9)], mem
CHECK -->

<!-- CHECK
# CHECK 2 — the claimed n=26 member: cubic, simple, C4-free, C8-free,
# contains a chorded C16, and its cycle census at short lengths matches
# the recorded fingerprint (c3=5, c5=4, c6=7, c7=4, c9=13).
from collections import deque
FLAT = "0,1,0,15,0,16,1,2,1,16,2,3,2,17,3,4,3,17,4,5,4,16,5,6,5,18,6,7,6,18,7,8,7,23,8,9,8,20,9,10,9,24,10,11,10,17,11,12,11,21,12,13,12,19,13,14,13,22,14,15,14,22,15,25,18,19,19,20,20,21,21,22,23,24,23,25,24,25"
xs = [int(t) for t in FLAT.split(",")]
E = list(zip(xs[0::2], xs[1::2]))
n = 26
adj = [[] for _ in range(n)]
for u, v in E:
    adj[u].append(v); adj[v].append(u)
assert all(len(set(a)) == 3 and v not in a for v, a in enumerate(adj))
bits = [0]*n
for v in range(n):
    for w in adj[v]: bits[v] |= 1 << w
for u in range(n):
    for v in range(u+1, n):
        c = bits[u] & bits[v] & ~(1<<u) & ~(1<<v)
        assert not (c and (c & (c-1))), "C4"
cnt = {}
chorded = False
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
                if len(path) >= 3 and path[1] < path[-1]:
                    L = len(path)
                    cnt[L] = cnt.get(L, 0) + 1
                    if L == 16 and not chorded:
                        onC = set(path); idx = {x:i for i,x in enumerate(path)}
                        for i, x in enumerate(path):
                            for y in adj[x]:
                                if y in onC and abs(i-idx[y]) not in (1,15):
                                    chorded = True
                continue
            if w < s or (mask>>w)&1: continue
            if len(path)+d[w] > 16: continue
            stack.append((w, mask|(1<<w), path+[w]))
assert cnt.get(8, 0) == 0, "C8"
assert cnt.get(4, 0) == 0, "C4 recount"
assert (cnt.get(3,0), cnt.get(5,0), cnt.get(6,0), cnt.get(7,0), cnt.get(9,0)) \
       == (5, 4, 7, 4, 13), cnt
assert chorded
CHECK -->
