---
id: pendant_9_cap
status: disproved
depends_on: [criticality_edge_witness, cycle_pair_sym_diff_exclusions]
discharged_by_round: 60
introduced_at_round: 60
---

# Lemma `pendant_9_cap` (DISPROVED at introduction — the R59 target falsified before proof effort, per the dual-attack policy)

**Claim (as targeted by R59's closing note — the "$9$-analogue of
`c5_rigidity_c8free`(ii)"):** in a cubic graph with girth $\ge 5$ and
no $C_8$, every edge carries at most $2$ pendant-$9$ witnesses; more
weakly, per-edge caps small enough that the set of $9$-witnessable
edges is a proper (bounded-fraction) subset of the edge set, so that
the R58 saturation ledger can register a supply gap at length $9$.

**Status: DISPROVED** — falsified on the R57 pinned instance itself
(CHECK 2 of `c5_rigidity_c8free`: cubic, $n = 28$, girth $5$, no
$C_8$, five $5$-cycles), i.e. on the program's own non-vacuous
exemplar of the witness class, before any proof effort was spent.

## Definitions

A *pendant-$9$ witness* for edge $e = uv$ at endpoint $u$ is a
$9$-cycle through $u$ but not $v$ whose two cycle-edges at $u$ are
$u$'s two other edges $ua$, $ub$ (equivalently: $ua \cup ub$ plus a
$7$-path $a \to b$ in $G - u$ avoiding $v$). This is exactly the
$k = 2^3$ pendant case of `criticality_edge_witness`. A $9$-cycle
through both $u$ and $v$ with cycle-neighbors $\{a, b\}$ at $u$ has
$e$ as a chord and is NOT a pendant witness (the chord splits
$9 + 2 = 11$ into $\{5, 6\}$ — consistent, but not the witness shape).

## The falsification data (deterministic enumeration, all 34 nine-cycles of the pin)

1. **Per-(endpoint, edge) count reaches $6$** (distribution over the
   $(u, e)$ pairs with $\ge 1$ witness:
   $\{1{:}8,\ 2{:}20,\ 3{:}17,\ 4{:}12,\ 5{:}17,\ 6{:}8\}$).
2. **Per-edge count reaches $10$** (top five: $9, 9, 9, 10, 10$) —
   against the targeted cap of $2$.
3. **Every one of the $42$ edges is $9$-witnessable** (carries a
   pendant-$9$ witness at some endpoint). The $9$-supply alone
   saturates the R58 demand ($3n/2$ edges) in one stroke; $24$ of
   $42$ edges are additionally chord-$10$ witnessed (chord at
   cycle-distance $4$ or $5$ of a $C_{10}$, the only distances R58's
   corollary allows).
4. The finer structure is exactly as `cycle_pair_sym_diff_exclusions`
   predicts and no finer: within a fixed $(u, e)$ family the realized
   pairwise shared-edge spectrum is exactly $\{2, 3, 4, 6\}$, and
   $(\text{first},\text{last})$-edge groups of the induced $7$-paths
   reach size $3$, killing the "$\le 2$ per group" refinement too.
5. Unlike length $5$ (incidence cap $2$, $\#C_5 \le 3n/5$), $9$-cycles
   are abundant: the pin has $\#C_9 = 34 > n$ and per-edge
   $C_9$-incidence up to $12$.

## Consequence for the Q80 program

The cardinality version of the supply-vs-demand ledger (Section 98,
"the count so far") is dead in the girth-$\ge 5$ + $C_8$-free class:
no per-edge witness cap can create a gap when the $9$-witnessable set
is TOTAL on a class member. What the pin does NOT belong to is the
minimal-counterexample class proper — it contains a $C_{16}$ (F3
forces one at $n = 28$). A vertex-minimal counterexample with
$n \le 32$ is also $C_{16}$-free, so any surviving ledger must draw
its scarcity from $C_{16}$-freeness. See Section 100 and the Q81
coupling (`c8free_c16_floor`).

Revised claims (a $C_{16}$-free supply cap, or a witnessability
obstruction) take NEW ids per the ledger contract.

<!-- CHECK
# pendant_9_cap CHECK 1 (audit trail — this lemma is disproved, so the
# harness skips this block; it ran green in-session at R60).
# Pins the falsification: on the R57 n=28 instance, strict pendant-9
# families reach 6 per (endpoint,edge), 10 per edge, every edge is
# 9-witnessable, pairwise spectrum inside families is exactly {2,3,4,6},
# and some (first,last) group reaches size 3.
from collections import defaultdict
E28 = [(0, 11), (0, 19), (0, 27), (1, 17), (1, 19), (1, 21), (2, 9), (2, 13),
       (2, 14), (3, 22), (3, 24), (3, 25), (4, 5), (4, 7), (4, 26), (5, 14),
       (5, 18), (6, 7), (6, 8), (6, 20), (7, 13), (8, 14), (8, 25), (9, 17),
       (9, 24), (10, 16), (10, 21), (10, 27), (11, 15), (11, 16), (12, 19),
       (12, 23), (12, 26), (13, 18), (15, 22), (15, 26), (16, 25), (17, 23),
       (18, 23), (20, 21), (20, 24), (22, 27)]
n = 28
adj = [set() for _ in range(n)]
for u, v in E28:
    adj[u].add(v); adj[v].add(u)
assert all(len(a) == 3 for a in adj)

def cycles_of_length(L):
    out = []
    for s in range(n):
        stack = [(s, (s,))]
        while stack:
            u, path = stack.pop()
            if len(path) == L:
                if s in adj[u] and path[1] < path[-1]:
                    out.append(path)
                continue
            for w in adj[u]:
                if w > s and w not in path:
                    stack.append((w, path + (w,)))
    return out

assert not cycles_of_length(3) and not cycles_of_length(4), "pin girth"
assert not cycles_of_length(8), "pin C8-free"
c9s = cycles_of_length(9)
assert len(c9s) == 34, len(c9s)

def edge_set(cyc):
    return frozenset(frozenset((cyc[i], cyc[(i + 1) % len(cyc)]))
                     for i in range(len(cyc)))

fam = defaultdict(list)       # (u, far_endpoint) -> [(edge_set, path_7)]
for cyc in c9s:
    es = edge_set(cyc)
    for i, u in enumerate(cyc):
        a, b = cyc[(i - 1) % 9], cyc[(i + 1) % 9]
        (w3,) = adj[u] - {a, b}
        if w3 in cyc:
            continue          # chord shape, not a pendant witness
        pa = es - {frozenset((u, a)), frozenset((u, b))}
        fam[(u, w3)].append((es, pa, a, b))

sizes = sorted(len(v) for v in fam.values())
assert max(sizes) == 6, max(sizes)
per_edge = defaultdict(int)
for (u, w3), v in fam.items():
    per_edge[frozenset((u, w3))] += len(v)
assert max(per_edge.values()) == 10, max(per_edge.values())
assert len(per_edge) == 42, "every edge 9-witnessable"

pset, gmax = set(), 0
for key, v in fam.items():
    groups = defaultdict(int)
    for i in range(len(v)):
        es1, pa1, a, b = v[i]
        fe = tuple(sorted(tuple(sorted(e)) for e in pa1 if a in e))
        le = tuple(sorted(tuple(sorted(e)) for e in pa1 if b in e))
        groups[(fe, le)] += 1
        for j in range(i + 1, len(v)):
            es2 = v[j][0]
            if es1 != es2:
                pset.add(len(es1 & es2))
    gmax = max(gmax, max(groups.values()))
assert pset == {2, 3, 4, 6}, sorted(pset)
assert gmax == 3, gmax
print("pendant_9_cap falsification pin verified")
-->
