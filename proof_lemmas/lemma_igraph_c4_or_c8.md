---
id: igraph_c4_or_c8
status: proved
depends_on: []
discharged_by_round: 1
introduced_at_round: 1
---

# Lemma: every simple I-graph contains a $C_4$ or a $C_8$

**Scope restriction.** The conditions $2a \not\equiv 0$ and $2b \not\equiv 0
\pmod m$ are necessary: if $2b \equiv 0$ (e.g., $I(6,1,3)$ where $2 \cdot 3
\equiv 0 \pmod 6$) the inner polygon degenerates with multi-edges, and the
graph is not 3-regular in the simple sense. This lemma applies only to simple
cubic I-graphs satisfying both conditions.

**Statement.** Let $m \ge 3$ and $a, b \in \mathbb{Z}_m$ be such that the
I-graph $I(m,a,b)$ is simple and cubic; that is, $a \not\equiv 0$,
$2a \not\equiv 0$, $b \not\equiv 0$, $2b \not\equiv 0 \pmod m$.
(The conditions $2a \not\equiv 0$ and $2b \not\equiv 0$ exclude multi-edges
in the outer and inner polygons respectively.) (Vertices
$u_0,\dots,u_{m-1}, v_0,\dots,v_{m-1}$; edges $u_j u_{j+a}$ ("outer"),
$v_j v_{j+b}$ ("inner"), $u_j v_j$ ("spokes"), indices mod $m$.) Then
$I(m,a,b)$ contains a simple cycle of length $4$ or a simple cycle of
length $8$.

Since $GP(n,k) = I(n,1,k)$, every generalized Petersen graph contains a
$C_4$ or a $C_8$; in particular the Erdős–Gyárfás conjecture holds for
the entire I-graph family, and no I-graph of any size is an
Erdős–Gyárfás witness.

**Proof.**

*Case 1: $b \equiv a$ or $b \equiv -a \pmod m$.* Inner polygon edges are
unordered pairs $\{v_j, v_{j+b \bmod m}\}$ for $j \in \mathbb{Z}_m$.
- **Sub-case $b \equiv a$:** Taking $j = 0$ gives inner edge $\{v_0, v_b\} = \{v_0, v_a\}$.
- **Sub-case $b \equiv -a$:** Taking $j = a$ gives inner edge $\{v_a, v_{a+b}\} = \{v_a, v_0\}$.

In both sub-cases $\{v_0, v_a\}$ is an inner edge. The walk
$u_0 \to u_a \to v_a \to v_0 \to u_0$ uses: outer edge $u_0 u_a$; spoke
$u_a v_a$ (NOT outer edge $u_a u_{2a}$); inner edge $\{v_a, v_0\}$; spoke
$v_0 u_0$. Its four vertices are distinct (since $a \not\equiv 0$), its
four edges are pairwise distinct (two spokes at different indices, one outer,
one inner), so it is a $C_4$.
(Concreteness: $I(6,2,2)$ has inner edges $\{v_j, v_{j+2}\}$, so
$\{v_0,v_2\}=\{v_0,v_a\}$ is present for $a=b=2$ via $j=0$; and
$I(4,1,3)$ has inner edge $\{v_1,v_0\}$ for $j=1, b=3, j+b=4\equiv 0$,
giving $\{v_1,v_{a}\}=\{v_1,v_0\}$ via the $b\equiv -a$ sub-case.
Smallest case: $I(3,1,2)$ ($m=3$, 6 vertices) has $b=2\equiv -a\pmod{3}$,
so Case~1 applies; $C_4$: $u_0\to u_1\to v_1\to v_0\to u_0$.)

*Case 2: $b \not\equiv \pm a \pmod m$ (equivalently, all four residues
$0, a, b, a+b$ are pairwise distinct mod $m$; $I(3,1,2)$ has
$b\equiv -a\pmod 3$ and is handled by Case~1 above, NOT here).*

**4-residue distinctness for Case 2.** Under the Case 2 precondition
$b \not\equiv \pm a \pmod m$, the four residues $\{0, a, b, a+b\}$ are
pairwise distinct mod $m$. Proof of all six pair-inequalities:
- $0 \ne a \pmod m$: simplicity ($a \not\equiv 0$).
- $0 \ne b \pmod m$: simplicity ($b \not\equiv 0$).
- $0 \ne a+b \pmod m$: if $a+b\equiv 0$ then $b\equiv -a$, contradicting
  Case~2 precondition.
- $a \ne b \pmod m$: Case~2 precondition ($b \not\equiv a$).
- $a \ne a+b \pmod m$: would require $b\equiv 0$, contradicting simplicity.
- $b \ne a+b \pmod m$: would require $a\equiv 0$, contradicting simplicity.

Hence all four residues are pairwise distinct. (CHECK probe~1 below
verifies the same fact exhaustively for all simple $I(m,a,b)$,
$m \le 60$.)

Now consider the closed walk
$$u_0 \to u_a \to v_a \to v_{a+b} \to u_{a+b} \to u_b \to v_b \to v_0 \to u_0 .$$
Each step uses an actual edge: $u_0 u_a$ outer; $u_a v_a$ spoke;
$v_a v_{a+b}$ inner; $v_{a+b} u_{a+b}$ spoke; $u_{a+b} u_b$ outer
(difference $a$); $u_b v_b$ spoke; $v_b v_0$ inner (difference $b$);
$v_0 u_0$ spoke. The eight vertices are the $u$- and $v$-copies of the
four pairwise-distinct residues above, hence all eight are distinct.
The eight edges are pairwise distinct: the four spokes sit at four
distinct indices; the two outer edges $\{u_0,u_a\}$ and
$\{u_b, u_{a+b}\}$ are distinct because $\{0,a\} \cap \{b, a+b\} =
\emptyset$; likewise the two inner edges. (The conditions $2a \not\equiv 0$
and $2b \not\equiv 0$ ensure no outer/inner edge is a loop or multi-edge.)
Hence the walk is a simple $8$-cycle. $\square$

**Excluded case ($2a \equiv 0$ or $2b \equiv 0$).** If $2a \equiv 0 \pmod m$,
the outer polygon has multi-edges; $I(m,a,b)$ is not simple. Analogously for
$2b \equiv 0$. The statement does not apply to such I-graphs; they are
excluded by the simplicity hypothesis stated in the scope restriction above.

**Sandbox-checkable core.** The entire content of the proof beyond
edge-by-edge membership inspection is (i) the residue-distinctness claim
of Case 2 and (ii) distinctness of the two outer edges and of the two
inner edges as unordered pairs. Both are expressible with the
aggregator's allowed builtins only — `set`, `len`, `min`, `max`,
`range`, `all` (note: `frozenset`, `sorted`, `bin` are NOT available in
the aggregator sandbox; unordered pairs are encoded as
`(min(x,y),max(x,y))` tuples) — as the single complete expression

```
all((b%m==a%m or (a+b)%m==0) or (len({0,a%m,b%m,(a+b)%m})==4
    and len({(min(0,a%m),max(0,a%m)),(min(b%m,(a+b)%m),max(b%m,(a+b)%m))})==2
    and len({(min(a%m,(a+b)%m),max(a%m,(a+b)%m)),(min(0,b%m),max(0,b%m))})==2)
    for m in range(3,25) for a in range(1,m) for b in range(1,m)
    if (2*a)%m!=0 and (2*b)%m!=0)
```

which evaluates True (verified in the aggregator sandbox; 300 chars).
This is the complete one-line re-derivation — spoke-edge distinctness is
immediate from residue-distinctness, and edge MEMBERSHIP (that
$u_ju_{j+a}$, $v_jv_{j+b}$, $u_jv_j$ are edges) is definitional for the
I-graph, so nothing further is one-line checkable. Re-deriving edge
membership independently requires building the lift graph, which cannot
fit a sandbox expression; that part is covered by the CHECK blocks below
(probe 1 validates edges and distinctness on all simple $I(m,a,b)$,
$m \le 60$; probe 2 cross-checks against exhaustive search for
$m \le 12$).

**Remarks.**

- **Degenerate cases are excluded by hypothesis, not overlooked.** The
  scenario $2a \equiv 0 \pmod m$ (e.g. $m$ even, $a = m/2$), under which
  $u_a = u_{-a}$ and the outer edges degenerate, violates the standing
  simplicity/cubicity hypothesis $2a \not\equiv 0$; likewise
  $2b \not\equiv 0$ rules out the inner-ring analogue. Within Case 2 the
  four residues $\{0, a, b, a+b\}$ are pairwise distinct (shown above), so
  the four spokes are distinct and the closing spoke $v_0 u_0$ is not a
  repeat; the walk cannot self-intersect. CHECK probe 1 verifies exactly
  this construction on every simple $I(m,a,b)$ with $3 \le m \le 60$,
  which includes every even $m$ and all $a, b$ permitted by the
  hypotheses.
- The lemma is insensitive to connectivity: if $\gcd(m,a,b) > 1$ the
  graph is disconnected, but the displayed cycles live inside one
  component.
- Some I-graphs have a $C_4$ in Case 2 as well (e.g. $GP(4k, k)$ has
  inner 4-cycles); the lemma only asserts existence of one of the two
  lengths.
- Machine verification (ranges match the CHECK blocks below): the
  explicit construction is arithmetically validated on every simple
  $I(m,a,b)$ with $3 \le m \le 60$, and cross-checked against an
  independent exhaustive per-length cycle search on every simple
  $I(m,a,b)$ with $3 \le m \le 12$. Separately, the window screen found
  the first power-of-2 cycle at length 4 or 8 on all 198 graphs
  $GP(n,k)$, $15 \le n \le 32$, and on all 1,248 simple $I(m,a,b)$ with
  $m \in [15,32]$ — none reached 16. Consistent with the case split
  above.

<!-- CHECK
# Boundary probe: I(3,1,2) — the smallest simple I-graph, m=3, only 6 vertices.
# KEY FACTS PROVED HERE:
# (A) b=2 equiv -a=-1 mod 3 => Case 1 (not Case 2). C4 exists via Case 1.
# (B) The Case 2 formula gives a NON-SIMPLE walk (u0 appears TWICE), confirming
#     Case 2 correctly does NOT apply to I(3,1,2).
# (C) NO C8 exists: exhaustive DFS confirms (6 vertices can't contain C8).

m312, a312, b312 = 3, 1, 2

# --- (A) Case 1 applies ---
assert b312 % m312 == (m312 - a312) % m312, "b=2 must be equiv -a mod 3"
# Build adjacency (vertices 0..m-1 are u, m..2m-1 are v)
adj312 = [set() for _ in range(2 * m312)]
for j312 in range(m312):
    adj312[j312].add((j312 + a312) % m312)
    adj312[(j312 + a312) % m312].add(j312)
    adj312[m312 + j312].add(m312 + (j312 + b312) % m312)
    adj312[m312 + (j312 + b312) % m312].add(m312 + j312)
    adj312[j312].add(m312 + j312)
    adj312[m312 + j312].add(j312)
# C4: u0-u1-v1-v0-u0 = vertices [0,1,4,3]
c4_312 = [0, 1, m312 + 1, m312 + 0]
assert len(set(c4_312)) == 4, "C4 vertices not distinct"
assert all(c4_312[(i+1)%4] in adj312[c4_312[i]] for i in range(4)), "C4 edge absent"
print("OK (A): I(3,1,2) Case 1 gives C4 =", c4_312)

# --- (B) Case 2 formula gives NON-SIMPLE walk (proves Case 2 doesn't apply) ---
# Case 2 walk: u0, u_a, v_a, v_{a+b}, u_{a+b}, u_b, v_b, v0
A312, B312, AB312 = a312 % m312, b312 % m312, (a312 + b312) % m312
case2_walk = [0, A312, m312+A312, m312+AB312, AB312, B312, m312+B312, m312+0]
# AB312 = (1+2)%3 = 0, so u_{a+b}=u0 appears at positions 0 and 4 => repeated!
assert len(set(case2_walk)) < 8, (
    "Case 2 walk unexpectedly has 8 distinct vertices for I(3,1,2) — would be C8!"
)
print("OK (B): Case 2 walk has repeated vertices:", case2_walk,
      "— NOT a simple cycle, confirming Case 2 doesn't apply")

# --- (C) No C8 in I(3,1,2) ---
def exhaustive_cycle_len(adj, L, n):
    """Return True if any simple cycle of length L exists in adj (n vertices)."""
    if L > n:
        return False  # impossible: simple cycle needs L distinct vertices
    def dfs(start, curr, depth, vis):
        if depth == L:
            return start in adj[curr]
        for w in adj[curr]:
            if w >= start and not (vis >> w) & 1:
                if dfs(start, w, depth + 1, vis | (1 << w)):
                    return True
        return False
    return any(dfs(s, s, 1, 1 << s) for s in range(n))

assert not exhaustive_cycle_len(adj312, 8, 2 * m312), (
    "I(3,1,2) has C8?! Impossible — only 6 vertices"
)
print("OK (C): I(3,1,2) has NO C8 (6 vertices < 8 required, confirmed by DFS)")
CHECK -->

<!-- CHECK
# Falsification probe 1: verify the explicit C4/C8 construction on every
# simple I-graph I(m,a,b) with 3 <= m <= 60 (pure arithmetic: the claimed
# cycle must consist of distinct vertices joined by actual edges).
def igraph_edges(m, a, b):
    es = set()
    for j in range(m):
        es.add(frozenset((j, (j + a) % m)))                    # outer u
        es.add(frozenset((m + j, m + (j + b) % m)))            # inner v
        es.add(frozenset((j, m + j)))                          # spoke
    return es

def is_cycle(cyc, es):
    L = len(cyc)
    if len(set(cyc)) != L:
        return False
    used = set()
    for i in range(L):
        e = frozenset((cyc[i], cyc[(i + 1) % L]))
        if len(e) != 2 or e not in es or e in used:
            return False
        used.add(e)
    return True

checked = 0
for m in range(3, 61):
    for a in range(1, m):
        if a % m == 0 or (2 * a) % m == 0:
            continue
        for b in range(1, m):
            if b % m == 0 or (2 * b) % m == 0:
                continue
            es = igraph_edges(m, a, b)
            # simple+cubic sanity: 3m distinct edges
            assert len(es) == 3 * m, (m, a, b, len(es))
            if b % m == a % m or (a + b) % m == 0:
                cyc = [0, a % m, m + a % m, m + 0]             # u0 ua va v0
            else:
                A, B, AB = a % m, b % m, (a + b) % m
                cyc = [0, A, m + A, m + AB, AB, B, m + B, m + 0]
            assert is_cycle(cyc, es), f"explicit cycle fails at I({m},{a},{b})"
            checked += 1
assert checked > 10000, checked
CHECK -->

<!-- CHECK
# Falsification probe 2: independent exhaustive cross-check on small
# instances — brute-force fixed-length cycle search must agree that a C4
# or C8 exists in every simple I(m,a,b), 3 <= m <= 12 (covers GP(n,k),
# n <= 12, the original Q8 first-lemma range, and non-GP I-graphs).
import sys
sys.setrecursionlimit(100)

def igraph_adj(m, a, b):
    adj = [set() for _ in range(2 * m)]
    for j in range(m):
        for u, v in ((j, (j + a) % m), (m + j, m + (j + b) % m), (j, m + j)):
            adj[u].add(v); adj[v].add(u)
    return [sorted(s) for s in adj]

def has_cycle_len(adj, L):
    n = len(adj)
    def dfs(s, v, depth, used):
        if depth == L:
            return s in adj[v]
        for w in adj[v]:
            if w > s and not (used >> w) & 1:
                if dfs(s, w, depth + 1, used | (1 << w)):
                    return True
        return False
    return any(dfs(s, s, 1, 1 << s) for s in range(n))

for m in range(3, 13):
    for a in range(1, m):
        if (2 * a) % m == 0:
            continue
        for b in range(1, m):
            if (2 * b) % m == 0:
                continue
            adj = igraph_adj(m, a, b)
            assert all(len(x) == 3 for x in adj), (m, a, b)
            assert has_cycle_len(adj, 4) or has_cycle_len(adj, 8), \
                f"no C4/C8 in I({m},{a},{b}) — lemma falsified"
CHECK -->
