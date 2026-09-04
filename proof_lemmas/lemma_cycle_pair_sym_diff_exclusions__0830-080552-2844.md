---
id: cycle_pair_sym_diff_exclusions
status: proved
depends_on: []
discharged_by_round: 59
introduced_at_round: 59
---

# Lemma `cycle_pair_sym_diff_exclusions` (universal pair-interaction exclusions under girth $\ge 5$ + $C_8$-freeness)

Third rung of the Q80 criticality program: ONE pair-interaction lemma
covering every witness length at once, replacing per-length ad hoc
arguments. It subsumes part (i) of `c5_rigidity_c8free` and corrects
the ideation proposal's false claim that two $9$-cycles sharing one
edge force a $C_{16}$ (they need not — see Remark 2). Unlike the
Program-1 sym-diff lemmas (`sym_diff_cycle_formula`,
`sym_diff_nested`, `triple_sym_diff_structure`), which concern
fundamental cycles of a normal spanning tree, this is a statement
about ARBITRARY cycles of the graph, tree-free.

**Lemma.** Let $G$ be a simple graph with girth $\ge 5$ and no cycle
of length $8$. ($G$ need not be cubic or connected.) Then for any two
distinct cycles $C_1, C_2$ of $G$ (as edge sets):

$$|C_1 \triangle C_2| \notin \{2, 4, 8\}.$$

Equivalently, writing $L_i = |C_i|$ and $p = |C_1 \cap C_2|$, since
$|C_1 \triangle C_2| = L_1 + L_2 - 2p$:

$$p \notin \left\{ \tfrac{L_1 + L_2 - 2}{2},\ \tfrac{L_1 + L_2 - 4}{2},\ \tfrac{L_1 + L_2 - 8}{2} \right\}.$$

Moreover:

1. if $|C_1 \triangle C_2| = 6$, the symmetric difference is a single
   $6$-cycle of $G$;
2. if $|C_1 \triangle C_2| = 10$, it is a single $10$-cycle or two
   edge-disjoint $5$-cycles;
3. if $|C_1 \triangle C_2| = 12$, its cycle decomposition has parts
   from $\{12\}$, $\{7, 5\}$, or $\{6, 6\}$.

## Proof

The symmetric difference $D = C_1 \triangle C_2$ of two distinct
cycles is a nonempty subgraph in which every vertex has even degree,
and every such subgraph decomposes into edge-disjoint simple cycles of
$G$; each part has length $\ge$ girth $\ge 5$, and no part has length
$8$ ($C_8$-free). So $|D|$ is a sum of integers each $\ge 5$ and
$\ne 8$:

- $|D| = 2$ or $4$: impossible — the smallest part is $\ge 5$.
- $|D| = 8$: the only partition of $8$ into parts $\ge 5$ is $\{8\}$
  ($5 + 3$ has a part $< 5$), and an $8$-edge part is a $C_8$ —
  excluded.
- $|D| = 6$: only $\{6\}$ — a single part, so $D$ itself is one
  $6$-cycle (a vertex of degree $\ge 4$ in $D$ would force $\ge 2$
  parts and $|D| \ge 10$).
- $|D| = 10$: partitions into parts $\ge 5$, none equal to $8$:
  $\{10\}$ or $\{5, 5\}$.
- $|D| = 12$: $\{12\}$, $\{7, 5\}$, $\{6, 6\}$ (partitions with a
  part $8$, e.g. $\{8, 4\}$, are excluded twice over). $\blacksquare$

## Supply-table entries (immediate corollaries for the witness lengths)

For witness lengths $\{5, 9, 10, 17, 18\}$ (Section 98), the excluded
shared-edge counts $p$ for distinct cycle pairs (recall also the
trivial bound $p \le \min(L_1, L_2) - 1$: a cycle has no proper
sub-cycle, so $p = \min(L_1, L_2)$ would force $C_1 = C_2$ when
$L_1 = L_2$, and is impossible when $L_1 \ne L_2$):

| pair | $L_1 + L_2$ | excluded $p$ (in range) | allowed $p$ |
|---|---|---|---|
| $(5, 5)$ | 10 | $4, 3, 1$ | $0, 2$ |
| $(5, 9)$ | 14 | $3$ ($6, 5$ out of range) | $0, 1, 2, 4$ |
| $(5, 10)$ | 15 | — (all three non-integral) | $0, \dots, 4$ |
| $(9, 9)$ | 18 | $8, 7, 5$ | $0, 1, 2, 3, 4, 6$ |
| $(9, 10)$ | 19 | — (non-integral) | $0, \dots, 8$ |
| $(10, 10)$ | 20 | $9, 8, 6$ | $0, \dots, 5, 7$ |
| $(17, 17)$ | 34 | $16, 15, 13$ | rest |
| $(17, 18)$ | 35 | — (non-integral) | rest |
| $(18, 18)$ | 36 | $17, 16, 14$ | rest |

The $(5,5)$ row is `c5_rigidity_c8free`(i). The $(9,9)$ row is the
corrected form of the ideation claim: two $9$-cycles sharing exactly
$5$ edges are impossible (sym-diff $9 + 9 - 2 \cdot 5 = 8$), but
sharing exactly $1$ edge is NOT excluded — the $16$-edge sym-diff may
decompose as $\{11, 5\}$, $\{10, 6\}$, $\{9, 7\}$, $\{6, 5, 5\}$,
etc., so no $C_{16}$ is forced (Remark 2 of the program notes).

*Pendant-pair corollary (used by the supply count):* two distinct
cycles of equal length $L$ both pendant-witnessing the same edge
$e = uv$ at the same endpoint $u$ both contain the two $u$-edges
other than $e$, so $p \ge 2$; for $L = 9$ this leaves
$p \in \{2, 3, 4, 6\}$.

<!-- CHECK
# cycle_pair_sym_diff_exclusions CHECK 1 (deterministic, stdlib).
# (a) Petersen anchor: 5-cycle pairs with |sym-diff| = 8 exist AND a C8
#     exists (the exclusion's contrapositive at work).
# (b) pinned n=28 girth-5 C8-free instance: across ALL cycles of lengths
#     {5,6,7,9}, no pair has |sym-diff| in {2,4,8}; every |sym-diff|=6
#     is a single 6-cycle.
# (c) random cubic graphs: any pair with |sym-diff| in {2,4} has C3/C4
#     present; |sym-diff|=8 has C3/C4/C8 present.
import random

def adj_of(n, edges):
    a = [set() for _ in range(n)]
    for u, v in edges:
        a[u].add(v); a[v].add(u)
    return a

def cycles_of_length(adj, n, L):
    out = []
    for s in range(n):
        stack = [(s, (s,))]
        while stack:
            u, path = stack.pop()
            if len(path) == L:
                if s in adj[u] and path[1] < path[-1]:
                    out.append(frozenset(frozenset((path[i], path[(i + 1) % L]))
                                         for i in range(L)))
                continue
            for w in adj[u]:
                if w > s and w not in path:
                    stack.append((w, path + (w,)))
    return out

def is_single_cycle(edges):
    deg = {}
    for e in edges:
        for v in e:
            deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()):
        return False
    adjl = {}
    for e in edges:
        a, b = tuple(e)
        adjl.setdefault(a, []).append(b)
        adjl.setdefault(b, []).append(a)
    vs = set(deg)
    s = next(iter(vs))
    seen, stk = {s}, [s]
    while stk:
        u = stk.pop()
        for w in adjl[u]:
            if w not in seen:
                seen.add(w); stk.append(w)
    return seen == vs

def rand_cubic(n, rng):
    for _ in range(500):
        stubs = [v for v in range(n) for _ in range(3)]
        rng.shuffle(stubs)
        E, ok = set(), True
        for i in range(0, 3 * n, 2):
            u, v = stubs[i], stubs[i + 1]
            if u == v or (min(u, v), max(u, v)) in E:
                ok = False
                break
            E.add((min(u, v), max(u, v)))
        if ok:
            return sorted(E)
    return None

def stress(n, E, name, lens, expect_g5_c8free=False):
    adj = adj_of(n, E)
    has3 = bool(cycles_of_length(adj, n, 3))
    has4 = bool(cycles_of_length(adj, n, 4))
    has8 = bool(cycles_of_length(adj, n, 8))
    if expect_g5_c8free:
        assert not has3 and not has4 and not has8, name
    allc = []
    for L in lens:
        allc.extend(cycles_of_length(adj, n, L))
    checked = 0
    for i in range(len(allc)):
        for j in range(i + 1, len(allc)):
            d = allc[i] ^ allc[j]
            if len(d) in (2, 4):
                assert has3 or has4, f"{name}: |sd|={len(d)} without C3/C4"
            elif len(d) == 8:
                assert has3 or has4 or has8, f"{name}: |sd|=8 without C3/C4/C8"
            if not has3 and not has4 and not has8:
                assert len(d) not in (2, 4, 8), f"{name}: exclusion FALSIFIED"
                if len(d) == 6:
                    assert is_single_cycle(d), f"{name}: |sd|=6 not one C6"
            checked += 1
    return checked

pet = sorted(tuple(sorted(e)) for e in
             [(i, (i + 1) % 5) for i in range(5)] + [(i, i + 5) for i in range(5)]
             + [(5 + i, 5 + (i + 2) % 5) for i in range(5)])
padj = adj_of(10, pet)
p5 = cycles_of_length(padj, 10, 5)
assert any(len(p5[i] ^ p5[j]) == 8 for i in range(len(p5)) for j in range(i + 1, len(p5)))
assert cycles_of_length(padj, 10, 8)
total = stress(10, pet, "petersen", (5, 6))

E28 = [(0, 11), (0, 19), (0, 27), (1, 17), (1, 19), (1, 21), (2, 9), (2, 13),
       (2, 14), (3, 22), (3, 24), (3, 25), (4, 5), (4, 7), (4, 26), (5, 14),
       (5, 18), (6, 7), (6, 8), (6, 20), (7, 13), (8, 14), (8, 25), (9, 17),
       (9, 24), (10, 16), (10, 21), (10, 27), (11, 15), (11, 16), (12, 19),
       (12, 23), (12, 26), (13, 18), (15, 22), (15, 26), (16, 25), (17, 23),
       (18, 23), (20, 21), (20, 24), (22, 27)]
total += stress(28, E28, "pin28", (5, 6, 7, 9), expect_g5_c8free=True)

rng = random.Random(20260830)
for n in (10, 12, 14):
    for s in range(4):
        E = rand_cubic(n, rng)
        if E:
            total += stress(n, E, f"rand{n}_{s}", (5, 6, 7))
assert total >= 500, "probe vacuous"
CHECK -->
