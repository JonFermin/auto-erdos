---
id: triangle_cover_witness_free
status: proved
depends_on: []
discharged_by_round: 92
introduced_at_round: 92
---

# Lemma `triangle_cover_witness_free` — every cubic graph on at most 21 vertices has a cycle of length 3, 4, 6, 7 or 8

**Statement.** Let $G$ be a finite 3-regular (cubic) simple graph with
$|V(G)| \le 21$. Then $G$ contains a simple cycle whose length lies in
$F = \{3, 4, 6, 7, 8\}$.

(Handshake parity makes a cubic graph even-ordered, so $|V(G)| \le 21$
means $|V(G)| \le 20$; the statement is exactly the one Q0905-082429-3
asked for, extended by the free odd case. Connectivity is NOT assumed.)

**Provenance.** Q0905-082429-3 proposed deciding this by a complete
certificate over the connected cubic girth-5 graphs on 10..20 vertices
(reportedly 6,299 of them, per the literature counts quoted in the qid).
The proof below is a direct structural argument instead — no enumeration,
no external citation load-bearing anywhere. The reported census figure is
mentioned only as provenance and is used nowhere.

---

## Proof

Write $F = \{3,4,6,7,8\}$ and suppose for contradiction that $G$ is cubic,
$n = |V(G)| \le 20$, and **no cycle of $G$ has length in $F$**. So every
cycle of $G$ has length $5$ or length $\ge 9$.

### Step T1 (girth pinning): $G$ has girth exactly 5.

Girth $3, 4, 6, 7, 8$ are excluded by assumption (the shortest cycle
would be a cycle of length in $F$). Suppose girth $\ge 7$; then $G$ has
no cycle of length $\le 6$. Fix any vertex $v$ and let $L_d$ be the set
of vertices at distance $d$ from $v$. Then:

- No edge runs inside $L_1$ or inside $L_2$ (it would close a cycle of
  length $\le 2 \cdot 2 + 1 = 5$ through $v$); no vertex of $L_d$
  ($d \le 3$) has two neighbors in $L_{d-1}$ (that closes a cycle of
  length $\le 2d \le 6$); and no vertex of $L_2$ has a neighbor in $L_1$
  other than its unique parent (a cycle of length $\le 4$).
- Hence each of the $3$ vertices of $L_1$ has exactly $2$ neighbors in
  $L_2$, pairwise distinct across $L_1$: $|L_2| = 6$. Each vertex of
  $L_2$ likewise has exactly $2$ neighbors in $L_3$, pairwise distinct:
  $|L_3| = 12$.

(Edges inside $L_3$ would close 7-cycles, which girth $\ge 7$ permits —
they do not affect the vertex count.) The layers are disjoint, so
$n \ge 1 + 3 + 6 + 12 = 22 > 20$, a contradiction. This rules out girth
$7$, $8$ and $\ge 9$ at once. So the girth is $5$: cycles of length
$3, 4$ do not exist at all, and a pentagon (5-cycle) exists.

### Step T2 (pentagon rigidity): any two distinct pentagons of $G$ are vertex-disjoint.

*Edge-disjoint first.* Let $P \ne Q$ be pentagons sharing $k \ge 1$
edges. The symmetric difference $P \triangle Q$ (as edge sets) is a
nonempty even-degree subgraph with $10 - 2k$ edges, and every nonempty
even subgraph decomposes into edge-disjoint cycles of $G$. Every cycle of
$G$ has length $\ge 5$ and $\notin \{6,7,8\}$, so the possible total edge
counts of such decompositions are sums of parts from
$\{5, 9, 10, 11, \dots\}$. For $k = 1,2,3,4$ the required totals are
$8, 6, 4, 2$ — none of which is such a sum ($8 = 5+3$ fails, $8$ alone is
a forbidden $C_8$, $6$ alone a forbidden $C_6$, and $4, 2 < 5$). So
$k = 0$: distinct pentagons are edge-disjoint. (CHECK A(iv) verifies the
partition arithmetic.)

*Vertex-disjoint.* If pentagons $P \ne Q$ shared a vertex $v$, each would
use $2$ of the $3$ edges at $v$; $2 + 2 > 3$ forces a shared edge,
contradicting edge-disjointness. $\square$

In particular **every vertex of $G$ lies on at most one pentagon**.

### Step T3 (pentagon neighborhood): $n \ge 20$, with rigid structure at equality.

Fix a pentagon $P = v_1 v_2 v_3 v_4 v_5$ (indices mod 5; it exists by
T1). Each $v_i$ has exactly one neighbor $u_i$ off $P$:

- The third neighbor of $v_i$ is not on $P$: a chord $v_i v_{i+2}$ would
  make a triangle-or-$C_4$ with the $P$-arc (girth).
- $u_i \ne u_j$ for $i \ne j$: a common neighbor $x$ of $v_i, v_j$ closes
  a cycle $x v_i \dots v_j x$ of length $2 + d_P(v_i, v_j) \in \{3, 4\}$
  — excluded by girth. Note $d_P \in \{1,2\}$ for any two distinct
  pentagon vertices; this is used repeatedly below.

Set $U = \{u_1, \dots, u_5\}$, $|U| = 5$, $U \cap P = \emptyset$.

- **$U$ is independent.** An edge $u_i u_j$ closes
  $u_i u_j v_j \dots v_i u_i$ of length $3 + d_P(v_i, v_j) \in \{4, 5\}$.
  Length 4 is excluded by girth. Length 5 is a pentagon through
  $v_i$ and $v_j$ — but $v_i$ already lies on the pentagon $P \neq$ this
  one, contradicting T2.
- **No $u_i$ has a second neighbor on $P$**: $u_i v_j$ ($j \ne i$) would
  say $v_j$'s third neighbor is $u_i$, i.e. $u_j = u_i$ — excluded.

So every $u_i$ sends exactly $2$ edges into
$W := V(G) \setminus (P \cup U)$, i.e. $e(U, W) = 10$.

- **Each $w \in W$ has at most one neighbor in $U$.** If $w u_i, w u_j
  \in E$ with $i \ne j$, then $w u_i v_i \dots v_j u_j w$ is a cycle of
  length $4 + d_P(v_i, v_j) \in \{5, 6\}$. Length 6 is in $F$ — excluded.
  Length 5 is a pentagon through $v_i, v_j \in P$ — again kills T2.

Therefore $W$ contains at least $10$ distinct endpoints of $U$–$W$ edges:
$|W| \ge 10$ and

$$n \;=\; 5 + 5 + |W| \;\ge\; 20 .$$

Since $n \le 20$: $n = 20$, $|W| = 10$, **every $w \in W$ has exactly one
$U$-neighbor**, and (since $P$-vertices are already full) the remaining
$2$ edges of each $w$ stay inside $W$. So $W$ induces a $2$-regular graph
on 10 vertices: a disjoint union of cycles, each of length $\ge 5$ (girth)
and $\notin \{6,7,8\}$. The only partitions of $10$ into such lengths are
$\{5,5\}$ and $\{10\}$ (CHECK A(iii)).

### Step T4a (endgame, case $W = C_5 \sqcup C_5$): contradiction.

Let $Q \subset W$ be one of the two pentagons. Each $w \in Q$ has exactly
one $U$-edge. Two vertices $w, w' \in Q$ cannot share their $U$-neighbor
$u$: $u w \dots w' u$ (through $Q$) has length
$2 + d_Q(w, w') \in \{3, 4\}$ — girth. So $Q$'s five $U$-neighbors are
distinct, hence **all of $U$**; the same holds for the other pentagon
$Q'$. Thus every $u \in U$ has exactly one neighbor $a(u) \in Q$ (and one
in $Q'$).

Take the adjacent pair $v_1 v_2 \in E(P)$ and let $a = a(u_1)$,
$b = a(u_2)$; here $a \ne b$, since $a = b$ would make $a$ adjacent to
both $u_1$ and $u_2$, contradicting the "at most one $U$-neighbor"
property from T3. Then

$$v_1\, u_1\, a\, (\text{$Q$-path})\, b\, u_2\, v_2\, v_1$$

is a cycle of length $5 + d_Q(a, b) \in \{6, 7\}$ — both in $F$.
Contradiction. (All vertices lie in the pairwise disjoint sets
$\{v_1, v_2\}, \{u_1, u_2\}, Q$, so the cycle is simple.)

### Step T4b (endgame, case $W = C_{10}$): contradiction.

Write $W = w_0 w_1 \dots w_9$ (indices mod 10). Each $u \in U$ has
exactly two neighbors in $W$, say at positions $x, y$, and each
$w \in W$ has exactly one $U$-neighbor, so the five neighbor-pairs
partition $\{w_0, \dots, w_9\}$.

*Chord separation is exactly 3.* The two arcs of $C_{10}$ between $u$'s
neighbors, of lengths $d$ and $10 - d$ ($1 \le d \le 5$), each close a
cycle through $u$ of length $2 + d$ resp. $2 + (10 - d)$. Both lengths
must avoid $\{3, 4\} \cup \{6,7,8\}$, which forces $d = 3$
(CHECK A(i)): lengths $5$ and $9$.

*Cross-separation clash.* Take again the adjacent pair $v_1 v_2 \in E(P)$
with $u_1, u_2 \in U$, and let their $W$-neighbor pairs be
$\{w_a, w_{a+3}\}$ and $\{w_b, w_{b+3}\}$ (disjoint). For any choice
$w_x \in N_W(u_1)$, $w_y \in N_W(u_2)$ and either arc of $C_{10}$
between them (length $\ell \in \{s, 10-s\}$ where $s$ is their
separation), the cycle

$$v_1\, u_1\, w_x\, (\text{arc})\, w_y\, u_2\, v_2\, v_1$$

is simple of length $5 + \ell$; avoiding $F$ requires
$5 + \ell \notin \{6,7,8\}$, i.e. $\ell \notin \{1, 2, 3\}$, so every
cross separation $s$ must satisfy
$\min(s, 10 - s) \ge 4$. With $t = b - a \bmod 10$ the four cross
separations are $t$, $t + 3$, $t - 3$, $t$ (mod 10), so we need
$\min$-distance $\ge 4$ simultaneously for $t$, $t+3$, $t-3$. No
$t \in \mathbb{Z}_{10}$ achieves this (CHECK A(ii); the candidates
$t \in \{4,5,6\}$ fail at $t - 3 = 1$, $t + 3 = 8$, $t + 3 = 9$
respectively). Contradiction.

*Remark (independent second kill of this case).* Each $u \in U$ closes a
pentagon $u\, w_x\, \cdot\, \cdot\, w_y\, u$ with its distance-3 arc. By
T2 these five pentagons are pairwise vertex-disjoint, so their five
4-vertex arcs would occupy $20$ distinct vertices of $W$ — but
$|W| = 10$. Either argument suffices.

Both cases of T3's dichotomy are impossible, so no such $G$ exists.
$\blacksquare$

---

## Corollary (the triangle-inflation stratum is witness-free)

Let $T(G)$ denote the truncation of a cubic graph $G$: one flag-vertex
$(v, e)$ per incident pair, a triangle on the three flags of each vertex,
and a matching edge between the two flags of each edge. $T(G)$ is cubic
with $3|V(G)|$ vertices.

**Lift lemma.** If $G$ has a $p$-cycle then $T(G)$ has cycles of *every*
length in $[2p, 3p]$. *Proof:* traverse the cycle's triangles, choosing
independently at each visited vertex the direct triangle edge (cost 1) or
the detour through the third flag (cost 2); total $p + s$ with
$p \le s \le 2p$, all values attained. Each such closed trail visits
each flag at most once, hence is a simple cycle. (CHECK C constructs the
$s = p$ lift of an 8-cycle of the dodecahedral graph $GP(10,2)$ inside
$T(GP(10,2))$ explicitly: a $C_{16}$.)

**Corollary.** For every cubic $G$ with $|V(G)| \le 21$, the truncation
$T(G)$ contains a cycle of length $8$ or $16$. In particular no
Erdős–Gyárfás witness (a min-degree-3 graph with no power-of-2 cycle)
of the form $T(G)$ exists with at most $64$ vertices — the
**full-triangle-cover stratum inside the verifier box is empty**.

*Proof:* the lemma gives a $p$-cycle with $p \in \{3,4,6,7,8\}$. For
$p \in \{3,4\}$: $2p \le 8 \le 3p$, so an 8-cycle lifts. For
$p \in \{6,7,8\}$: $2p \le 16 \le 3p$, so a 16-cycle lifts
(CHECK A(vi)). A $T(G)$ shape on $\le 64$ vertices forces
$|V(G)| \le 21$. $\square$

Scope guard: this kills ONE reverse-engineered witness shape (full
triangle cover). It is not progress on the conjecture's truth and says
nothing about witnesses that are not truncations. Its practical value for
the search program: any witness hunt may quotient away vertex-triangles
below 64 vertices — the girth-$\ge 5$ normalization used by incumbent
hunts is now theorem-backed on this stratum (a triangle in a candidate
$\le 64$-vertex witness can never be part of a full triangle cover
pattern that survives; more precisely, full-triangle-cover candidates
need not be generated at all).

---

## CHECK blocks

<!-- CHECK
# CHECK A: the finite arithmetic used in T1-T4b and the corollary.
FORB = {3, 4, 6, 7, 8}


def d10(x):
    x %= 10
    return min(x, 10 - x)


# (i) a degree-3 chord vertex u attached to a C10 with arc separation d
# creates cycles of lengths 2+d and 2+(10-d); the only d in 1..5 with both
# lengths outside FORB (and >= 5, girth) is d == 3.
ok = [d for d in range(1, 6) if (2 + d) not in FORB and (2 + 10 - d) not in FORB]
assert ok == [3], ok

# (ii) two arc-distance-3 chord pairs {a,a+3},{b,b+3} on Z10 with all four
# cross separations >= 4 are impossible.
for t in range(10):
    if d10(t) >= 4 and d10(t + 3) >= 4 and d10(t - 3) >= 4:
        raise AssertionError("cross-separation gap at t=%d" % t)

# (iii) 2-regular graphs on 10 vertices with every cycle length >= 5 and
# outside FORB: only cycle-length multisets {5,5} and {10}.
parts = []


def go(rem, cur, mn):
    if rem == 0:
        parts.append(tuple(cur))
        return
    p = mn
    while p <= rem:
        if p >= 5 and p not in FORB:
            go(rem - p, cur + [p], p)
        p += 1


go(10, [], 5)
assert set(parts) == {(5, 5), (10,)}, parts

# (iv) pentagon sym-diff: two distinct pentagons sharing k >= 1 edges leave
# a nonempty even subgraph with 10-2k edges that would have to decompose
# into cycles of length >= 5 outside FORB; impossible for every k in 1..4.
def decomposable(m):
    if m == 0:
        return True
    return any(decomposable(m - p) for p in range(5, m + 1) if p not in FORB)


assert not any(decomposable(10 - 2 * k) for k in (1, 2, 3, 4))

# (v) Moore step: girth >= 7 cubic has distinct BFS layers 1,3,6,12:
# 22 > 20 vertices.
assert 1 + 3 + 6 + 12 == 22 and 22 > 20

# (vi) corollary bands: each p in FORB puts a power of 2 in [2p, 3p].
for p in (3, 4):
    assert 2 * p <= 8 <= 3 * p
for p in (6, 7, 8):
    assert 2 * p <= 16 <= 3 * p
CHECK -->

<!-- CHECK
# CHECK B: dual-attack falsification probe. Hunt for a cubic graph on
# <= 20 vertices with NO cycle of length in {3,4,6,7,8}; the lemma says
# none exists. Deterministic seed; configuration-model sampling.
import random

rng = random.Random(20260923)


def sample_cubic(n, rng):
    pts = [v for v in range(n) for _ in range(3)]
    rng.shuffle(pts)
    seen = set()
    adj = [[] for _ in range(n)]
    for i in range(0, 3 * n, 2):
        u, v = pts[i], pts[i + 1]
        if u == v:
            return None
        key = (u, v) if u < v else (v, u)
        if key in seen:
            return None
        seen.add(key)
        adj[u].append(v)
        adj[v].append(u)
    return adj


def has_cycle_in(adj, n, targets):
    # DFS over simple paths rooted at each cycle's minimum vertex.
    maxlen = max(targets)

    def dfs(root, v, depth, visited):
        for w in adj[v]:
            if w == root and depth in targets:
                return True
            if w > root and depth < maxlen and not (visited >> w) & 1:
                if dfs(root, w, depth + 1, visited | (1 << w)):
                    return True
        return False

    for r in range(n):
        if dfs(r, r, 1, 1 << r):
            return True
    return False


girth5_seen = 0
checked = 0
for n in (14, 16, 18, 20):
    for _ in range(8000):
        adj = sample_cubic(n, rng)
        if adj is None:
            continue
        checked += 1
        if has_cycle_in(adj, n, {3, 4}):
            continue  # cycle in the target set already found
        girth5_seen += 1
        assert has_cycle_in(adj, n, {6, 7, 8}), (
            "FALSIFIER: cubic girth-5 graph with no C6/C7/C8: n=%d adj=%r" % (n, adj)
        )
# deterministic seed => deterministic counts; require real coverage.
assert checked >= 3000, checked
assert girth5_seen >= 45, girth5_seen
CHECK -->

<!-- CHECK
# CHECK C: explicit instances + constructive truncation lift.
def gp(n, k):
    # generalized Petersen graph GP(n,k): outer 0..n-1, inner n..2n-1
    adj = [[] for _ in range(2 * n)]
    edges = set()

    def add(a, b):
        key = (a, b) if a < b else (b, a)
        assert key not in edges and a != b
        edges.add(key)
        adj[a].append(b)
        adj[b].append(a)

    for i in range(n):
        add(i, (i + 1) % n)
        add(n + i, n + (i + k) % n)
        add(i, n + i)
    return adj


def find_cycle_of_len(adj, n, targets):
    maxlen = max(targets)

    def dfs(root, v, path, visited):
        for w in adj[v]:
            if w == root and len(path) in targets:
                return list(path)
            if w > root and len(path) < maxlen and not (visited >> w) & 1:
                path.append(w)
                got = dfs(root, w, path, visited | (1 << w))
                if got is not None:
                    return got
                path.pop()
        return None

    for r in range(n):
        got = dfs(r, r, [r], 1 << r)
        if got is not None:
            return got
    return None


# Petersen = GP(5,2): girth 5, carries a cycle in {6,7,8}.
pet = gp(5, 2)
assert all(len(a) == 3 for a in pet)
assert find_cycle_of_len(pet, 10, {3, 4}) is None
assert find_cycle_of_len(pet, 10, {6, 7, 8}) is not None

# Dodecahedral graph = GP(10,2): girth 5, carries an 8-cycle (the instance
# that makes '8' necessary in the lemma statement).
dod = gp(10, 2)
assert all(len(a) == 3 for a in dod)
assert find_cycle_of_len(dod, 20, {3, 4}) is None
cyc8 = find_cycle_of_len(dod, 20, {8})
assert cyc8 is not None and len(cyc8) == 8


# Constructive lift: the 8-cycle yields a 16-cycle (a power of 2) in the
# truncation T(G), taking the direct triangle edge at every visited vertex.
def truncation(adj, n):
    flags = []
    for v in range(n):
        for w in adj[v]:
            e = (v, w) if v < w else (w, v)
            flags.append((v, e))
    tadj = {f: set() for f in flags}
    for v, e in flags:
        for w in adj[v]:
            e2 = (v, w) if v < w else (w, v)
            if e2 != e:
                tadj[(v, e)].add((v, e2))  # triangle edge
        u = e[0] if e[1] == v else e[1]
        tadj[(v, e)].add((u, e))  # matching edge
    assert all(len(s) == 3 for s in tadj.values())
    return tadj


tadj = truncation(dod, 20)
assert len(tadj) == 60
p = len(cyc8)
lift = []
for i in range(p):
    v = cyc8[i]
    eprev = (cyc8[i - 1], v) if cyc8[i - 1] < v else (v, cyc8[i - 1])
    nxt = cyc8[(i + 1) % p]
    enext = (v, nxt) if v < nxt else (nxt, v)
    lift.append((v, eprev))
    lift.append((v, enext))
assert len(lift) == 16 and len(set(lift)) == 16
for i in range(16):
    a, b = lift[i], lift[(i + 1) % 16]
    assert b in tadj[a], (i, a, b)
CHECK -->
