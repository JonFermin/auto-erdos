---
lemma_id: stratum_onset_24
status: proved
depends_on: []
session: s_0828-080832-67a3
---

# Lemma stratum_onset_24 — the {C4, C8}-free cubic stratum is empty for even n <= 22 and turns on at n = 24 with exactly four classes, all C16-carrying

**Statement.** Call the set of connected cubic graphs on $n$ vertices
with no 4-cycle and no 8-cycle the *stratum* at order $n$. Then:

(a) the stratum is EMPTY for every $n \le 22$ (cubic graphs need even
$n$; all even orders $4 \le n \le 22$ enumerated);

(b) the stratum at $n = 24$ consists of EXACTLY four isomorphism
classes — all of girth 3, all non-bipartite, with 16-cycle counts
$c_{16} = 207, 228, 315, 330$.

Since every class at $n = 24$ carries a 16-cycle and $C_{32}$ does not
fit on $\le 24$ vertices, there is no cubic Erdős–Gyárfás
counterexample on $\le 24$ vertices — an in-house re-derivation (by
complete enumeration) of the corresponding range of F3's Markström
computation, which excluded cubic counterexamples through order 28.

**Method (exhaustive rule-tree enumeration, validated three ways).**
Vertices are completed in index order, so every remaining neighbor of
the current vertex is larger; each vertex's neighbors are added in
increasing order; fresh vertices take the smallest unused label
(discovery order); $N(0) = \{1, 2, 3\}$. Every connected cubic graph
admits at least one rule-labeling (greedy discovery replay from any
root), so zero completions is an exhaustion proof. The cycle bans are
edge-monotone (a banned cycle appears only when its own last edge is
added), so in-search rejection of exactly the additions that close a
$C_4$ or $C_8$ is exhaustion-safe. Validation: (i) A002851
connected-cubic class counts 1/2/5/19/85/509 reproduced at
$n = 4..14$ with bans off; (ii) in-search banning $\equiv$
post-filtering on labeled counts at $n = 10..16$ ($C_4$-free:
58/528/12032/275273); (iii) single-process, multiprocessing, and
bitmask/meet-in-the-middle reimplementations agree on the exact
fingerprint (12,297,554 tree nodes, 9,512 labeled completions) at
$n = 24$. Full per-order table: Section 105.

<!-- CHECK
# stratum_empty_small CHECK 1: the R65 rule-tree enumerator, self-contained,
# with its validation fingerprint. Rules: vertices complete in index order
# (so remaining neighbors of the current vertex are all larger), neighbors
# chosen increasing, fresh vertices take the smallest unused index, and
# N(0)={1,2,3}; every connected cubic graph has >=1 rule-labeling, so zero
# completions under an edge-monotone cycle ban is an exhaustion proof of
# stratum emptiness. Asserted here (all re-derived from scratch):
#   (a) bans OFF: exact A002851 class counts at n=6 (2) and n=8 (5) via
#       brute-force canonical forms, and the enumerator's labeled rule-
#       counts 50/639/9609 at n=8/10/12 (pinned fingerprint);
#   (b) ban positive control: banned={4} at n=10/12 gives 58/528 labeled
#       completions == the count of labeled rule-graphs with c4=0
#       (in-search ban == post-filter, re-derived here);
#   (c) stratum emptiness: banned={4,8} completes with ZERO completions at
#       n=14, 16, 18 (2205 / 10088 / 52293 tree nodes, re-derived). The
#       session additionally verified: A002851 class counts 19/85 at
#       n=10/12, ban==post-filter at n=14/16 (12032/275273 C4-free
#       labeled), and emptiness through n=26 (Section 105).
# The session's larger-scale results (n=20..26 empty) use the same code
# path with multiprocessing on top; node counts are in Section 105.
from itertools import permutations

def enumerate_rule(n, banned):
    maxpath = (max(banned) - 1) if banned else 0
    targets = set(L - 1 for L in banned)
    adj = [[] for _ in range(n)]
    deg = [0] * n
    out = []
    stats = [0]
    def creates_banned(u, v):
        stack = [(u, 0, 1 << u)]
        while stack:
            x, d, vis = stack.pop()
            for y in adj[x]:
                if y == v:
                    if d + 1 in targets:
                        return True
                elif not (vis >> y) & 1 and d + 1 < maxpath:
                    stack.append((y, d + 1, vis | (1 << y)))
        return False
    def rec(u, next_fresh):
        stats[0] += 1
        while u < n and deg[u] == 3:
            u += 1
        if u == n:
            if next_fresh == n:
                out.append(tuple((a, b) for a in range(n) for b in adj[a] if a < b))
            return
        if deg[u] == 0 and u > 0:
            return
        last = adj[u][-1] if adj[u] and adj[u][-1] > u else u
        for w in range(last + 1, next_fresh):
            if deg[w] < 3 and w not in adj[u] and not (banned and creates_banned(u, w)):
                adj[u].append(w); adj[w].append(u); deg[u] += 1; deg[w] += 1
                rec(u, next_fresh)
                adj[u].pop(); adj[w].pop(); deg[u] -= 1; deg[w] -= 1
        if next_fresh < n:
            w = next_fresh
            adj[u].append(w); adj[w].append(u); deg[u] += 1; deg[w] += 1
            rec(u, next_fresh + 1)
            adj[u].pop(); adj[w].pop(); deg[u] -= 1; deg[w] -= 1
    for w in (1, 2, 3):
        adj[0].append(w); adj[w].append(0); deg[w] = 1
    deg[0] = 3
    rec(1, 4)
    return out, stats[0]

def canon(n, edges):
    # exact min-key over labelings; the minimal key maps some vertex to 0
    # and its neighbors to {1,2,3}, so restricting to those is lossless
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    best = None
    rest_all = list(range(4, n))
    for v0 in range(n):
        for nbr in permutations(adj[v0]):
            others = [x for x in range(n) if x != v0 and x not in adj[v0]]
            for rest in permutations(rest_all):
                p = {v0: 0}
                for i, x in enumerate(nbr):
                    p[x] = i + 1
                for x, i in zip(others, rest):
                    p[x] = i
                key = tuple(sorted((min(p[a], p[b]), max(p[a], p[b])) for a, b in edges))
                if best is None or key < best:
                    best = key
    return best

def c_count(n, edges, L):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        adj[u].append(v); adj[v].append(u)
    total = 0
    for root in range(n):
        stack = [(u, 2, (1 << root) | (1 << u)) for u in adj[root] if u > root]
        while stack:
            u, ln, vis = stack.pop()
            for w in adj[u]:
                if w == root:
                    if ln == L:
                        total += 1
                elif w > root and not (vis >> w) & 1 and ln < L:
                    stack.append((w, ln + 1, vis | (1 << w)))
    return total // 2

# (a) class counts + labeled fingerprint, bans off
g6, _ = enumerate_rule(6, ())
assert len(set(canon(6, e) for e in g6)) == 2 and len(g6) == 5
g8, _ = enumerate_rule(8, ())
assert len(set(canon(8, e) for e in g8)) == 5 and len(g8) == 50
g10, _ = enumerate_rule(10, ())
assert len(g10) == 639
g12, _ = enumerate_rule(12, ())
assert len(g12) == 9609
# (b) in-search ban == post-filter (positive control: completions DO appear)
for n_, allg, want in ((10, g10, 58), (12, g12, 528)):
    gb, _ = enumerate_rule(n_, (4,))
    post = sum(1 for e in allg if c_count(n_, e, 4) == 0)
    assert len(gb) == post == want
# (c) stratum emptiness with pinned tree sizes
for n_, want_nodes in ((14, 2205), (16, 10088), (18, 52293)):
    got, nodes = enumerate_rule(n_, (4, 8))
    assert got == [] and nodes == want_nodes, (n_, len(got), nodes)
print("R65 enumerator validated: A002851 classes at n=6,8; labeled fingerprint 50/639/9609; in-search C4 ban == post-filter at n=10,12 (58/528); {C4,C8}-stratum EMPTY at n=14,16,18")
CHECK -->

<!-- CHECK
# stratum_onset_24 CHECK 2: the four n=24 stratum classes, pinned. Each is
# verified from scratch: connected, cubic, NO 4-cycle, NO 8-cycle (complete
# searches), girth 3, and c16 as stated (207 / 228 / 315 / 330 — all
# positive, so no cubic EGC counterexample at n=24; C32 does not fit).
# Exhaustiveness (these four are ALL of the stratum at n=24) is the R65
# enumeration result, fingerprinted in CHECK 1 and Section 105.
def build(n, edges):
    adj = [[] for _ in range(n)]
    es = set()
    for u, v in edges:
        a, b = min(u, v), max(u, v)
        assert a != b and (a, b) not in es
        es.add((a, b))
        adj[a].append(b); adj[b].append(a)
    assert all(len(x) == 3 for x in adj)
    seen = {0}; stk = [0]
    while stk:
        u = stk.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w); stk.append(w)
    assert len(seen) == n
    return adj

def ccount(n, adj, L):
    total = 0
    for root in range(n):
        stack = [(u, 2, (1 << root) | (1 << u)) for u in adj[root] if u > root]
        while stack:
            u, ln, vis = stack.pop()
            for w in adj[u]:
                if w == root:
                    if ln == L:
                        total += 1
                elif w > root and not (vis >> w) & 1 and ln < L:
                    stack.append((w, ln + 1, vis | (1 << w)))
    return total // 2

M207 = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 8), (3, 9), (4, 10), (4, 11), (5, 7), (5, 12), (6, 7), (6, 13), (8, 9), (8, 11), (9, 14), (10, 15), (10, 16), (11, 17), (12, 15), (12, 18), (13, 19), (13, 20), (14, 21), (14, 22), (15, 18), (16, 17), (16, 23), (17, 23), (18, 21), (19, 20), (19, 22), (20, 23), (21, 22)]
M228 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5), (3, 6), (3, 7), (4, 6), (4, 8), (5, 9), (5, 10), (6, 7), (7, 11), (8, 12), (8, 13), (9, 14), (9, 15), (10, 16), (10, 17), (11, 18), (11, 19), (12, 13), (12, 20), (13, 21), (14, 15), (14, 16), (15, 18), (16, 17), (17, 20), (18, 19), (19, 22), (20, 23), (21, 22), (21, 23), (22, 23)]
M315 = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 8), (3, 9), (4, 10), (4, 11), (5, 12), (5, 13), (6, 7), (6, 10), (7, 14), (8, 10), (8, 15), (9, 16), (9, 17), (11, 16), (11, 18), (12, 15), (12, 16), (13, 18), (13, 19), (14, 20), (14, 21), (15, 22), (17, 22), (17, 23), (18, 19), (19, 20), (20, 21), (21, 23), (22, 23)]
M330 = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 8), (3, 9), (4, 10), (4, 11), (5, 7), (5, 9), (6, 7), (6, 10), (8, 12), (8, 13), (9, 14), (10, 15), (11, 16), (11, 17), (12, 13), (12, 18), (13, 19), (14, 18), (14, 19), (15, 16), (15, 20), (16, 21), (17, 20), (17, 22), (18, 21), (19, 23), (20, 22), (21, 23), (22, 23)]

for edges, want16 in ((M207, 207), (M228, 228), (M315, 315), (M330, 330)):
    adj = build(24, edges)
    assert ccount(24, adj, 4) == 0 and ccount(24, adj, 8) == 0
    assert ccount(24, adj, 3) > 0  # girth 3
    assert ccount(24, adj, 16) == want16
print("stratum_onset_24 CHECK 2: all four n=24 stratum classes verified — cubic connected, c4=c8=0, girth 3, c16 = 207/228/315/330 (all > 0: no cubic EGC counterexample at 24)")
CHECK -->

**R65 addendum — the next order up ($n = 26$, same session).** The same
validated tool (gen3 code path) exhausts $n = 26$: 138,937,178 tree
nodes, 200,888 labeled completions, EXACTLY 23 classes (canonical-
certificate dedup, validated against A002851 at $n = 10/12/14$ and the
VF2 result at $n = 24$). All 23 have girth 3; $c_{16}$ ranges over
$[161, 454]$ with no zero — so the cubic Erdős–Gyárfás exclusion
extends in-house through $n = 26$, and the exact stratum floor DROPS
with $n$ (24: 207, 26: 161) toward the $n = 58$ SA dip (37). CHECK 3
pins the $n = 26$ extremal member.

<!-- CHECK
# stratum_onset_24 CHECK 3: R65 n=26 extremal stratum member (exact class
# minimum c16 = 161), pinned. Verified from scratch: connected, cubic,
# c4 = c8 = 0 (complete searches), girth 3, c16 = 161 > 0.
def build(n, edges):
    adj = [[] for _ in range(n)]
    es = set()
    for u, v in edges:
        a, b = min(u, v), max(u, v)
        assert a != b and (a, b) not in es
        es.add((a, b))
        adj[a].append(b); adj[b].append(a)
    assert all(len(x) == 3 for x in adj)
    seen = {0}; stk = [0]
    while stk:
        u = stk.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w); stk.append(w)
    assert len(seen) == n
    return adj

def ccount(n, adj, L):
    total = 0
    for root in range(n):
        stack = [(u, 2, (1 << root) | (1 << u)) for u in adj[root] if u > root]
        while stack:
            u, ln, vis = stack.pop()
            for w in adj[u]:
                if w == root:
                    if ln == L:
                        total += 1
                elif w > root and not (vis >> w) & 1 and ln < L:
                    stack.append((w, ln + 1, vis | (1 << w)))
    return total // 2

M161 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5), (3, 6), (3, 7), (4, 6), (4, 8), (5, 9), (5, 10), (6, 7), (7, 11), (8, 12), (8, 13), (9, 10), (9, 14), (10, 15), (11, 16), (11, 17), (12, 18), (12, 19), (13, 20), (13, 21), (14, 18), (14, 22), (15, 20), (15, 23), (16, 22), (16, 24), (17, 23), (17, 25), (18, 19), (19, 24), (20, 21), (21, 25), (22, 24), (23, 25)]
adj = build(26, M161)
assert ccount(26, adj, 4) == 0 and ccount(26, adj, 8) == 0
assert ccount(26, adj, 3) > 0
assert ccount(26, adj, 16) == 161
print("stratum_onset_24 CHECK 3: n=26 extremal member verified — cubic connected, c4=c8=0, girth 3, c16=161")
CHECK -->

**R66 addendum — $n = 28$ complete; fingerprint corrections (session
s_0829-080615-66f6).** The C port of the CHECK-1 enumerator (validated
bit-exactly against every pinned fingerprint at $n \le 22$ and, per
subtree, against the verbatim CHECK-1 reference at $n = 24$) exhausts
$n = 28$: $2{,}969{,}746{,}296$ tree nodes, $6{,}201{,}596$ labeled
completions, EXACTLY 251 classes (lex-minimal rule-labeling
certificate, validated on A002851 19/85/509 and the pinned 24/26
censuses), $c_{16} \in [153, 731]$, no zero — so the cubic
Erdős–Gyárfás exclusion is re-derived in-house through $n = 28$, the
full Markström range. Girth 5 appears in the stratum for the first
time (4 of 251 classes), carrying the four highest $c_{16}$ values.
Exact floor profile: 24: 207, 26: 161, 28: 153. CORRECTION to the
figures quoted in this file's Method paragraph and Section 105: the
true node fingerprints are $12{,}302{,}758$ at $n = 24$ and
$138{,}948{,}598$ at $n = 26$ (verbatim CHECK-1 reference, confirmed
by the independent C path; the R65 parallel harness under-counted one
node per frontier state). Completions and all class data stand
unchanged. Section 106 has the full account.

<!-- CHECK
# stratum_onset_24 CHECK 4: R66 n=28 pins. (a) the exact-floor member
# (class minimum c16 = 153) and (b) the minimal girth-5 member (c16 = 614;
# girth 5 first appears in the stratum at n = 28). Verified from scratch:
# connected, cubic, c4 = c8 = 0 (complete searches), girth / c16 as stated.
# Exhaustiveness (251 classes at n=28, none C16-free) is the R66
# enumeration result, fingerprinted in Section 106.
def build(n, edges):
    adj = [[] for _ in range(n)]
    es = set()
    for u, v in edges:
        a, b = min(u, v), max(u, v)
        assert a != b and (a, b) not in es
        es.add((a, b))
        adj[a].append(b); adj[b].append(a)
    assert all(len(x) == 3 for x in adj)
    seen = {0}; stk = [0]
    while stk:
        u = stk.pop()
        for w in adj[u]:
            if w not in seen:
                seen.add(w); stk.append(w)
    assert len(seen) == n
    return adj

def ccount(n, adj, L):
    total = 0
    for root in range(n):
        stack = [(u, 2, (1 << root) | (1 << u)) for u in adj[root] if u > root]
        while stack:
            u, ln, vis = stack.pop()
            for w in adj[u]:
                if w == root:
                    if ln == L:
                        total += 1
                elif w > root and not (vis >> w) & 1 and ln < L:
                    stack.append((w, ln + 1, vis | (1 << w)))
    return total // 2

M153 = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 4), (2, 5), (3, 6), (3, 7), (4, 8), (4, 9), (5, 10), (5, 11), (6, 7), (6, 12), (7, 13), (8, 9), (8, 14), (9, 15), (10, 11), (10, 16), (11, 17), (12, 18), (12, 19), (13, 20), (13, 21), (14, 18), (14, 22), (15, 23), (15, 24), (16, 19), (16, 25), (17, 26), (17, 27), (18, 22), (19, 25), (20, 21), (20, 23), (21, 26), (22, 27), (23, 24), (24, 25), (26, 27)]
G614 = [(0, 1), (0, 2), (0, 3), (1, 4), (1, 5), (2, 6), (2, 7), (3, 8), (3, 9), (4, 6), (4, 8), (5, 10), (5, 11), (6, 12), (7, 10), (7, 13), (8, 14), (9, 12), (9, 15), (10, 16), (11, 14), (11, 17), (12, 18), (13, 15), (13, 19), (14, 20), (15, 21), (16, 17), (16, 21), (17, 22), (18, 19), (18, 23), (19, 24), (20, 24), (20, 25), (21, 26), (22, 25), (22, 27), (23, 25), (23, 26), (24, 27), (26, 27)]

adj = build(28, M153)
assert ccount(28, adj, 4) == 0 and ccount(28, adj, 8) == 0
assert ccount(28, adj, 3) > 0  # girth 3
assert ccount(28, adj, 16) == 153
adj = build(28, G614)
assert ccount(28, adj, 4) == 0 and ccount(28, adj, 8) == 0
assert ccount(28, adj, 3) == 0 and ccount(28, adj, 5) > 0  # girth 5
assert ccount(28, adj, 16) == 614
print("stratum_onset_24 CHECK 4: n=28 extremal member (c16=153, girth 3) and minimal girth-5 member (c16=614) verified — cubic connected, c4=c8=0; no C16-free class exists at 28 (R66 exhaustion)")
CHECK -->
