---
id: c16_d1_ear_cover
status: open
depends_on: [c16_dip_decomposition, c16_landing_universal, chordless_c16_ear_geometry]
discharged_by_round: null
introduced_at_round: 84
---

# Lemma `c16_d1_ear_cover` (open — the three-layer ear-cover criterion at $d = 1$; sufficiency proved, supply open)

**Setting.** $G$ connected cubic $\{C_4, C_8\}$-free on
$24 \le n \le 30$ vertices, $C$ a chordless $16$-cycle,
$(f_1, u_1, v, u_2, f_2)$ a legal $\tau \ge 2$ landing at feet
distance $d = 1$, $H := G - \{u_1, v, u_2\}$. Fix the long-arc
coordinate: positions $0, 1, \dots, 15$ along the $15$-edge arc of
$C$ from $f_2$ (position $0$) to $f_1$ (position $15$). An
**interior ear** is a path in $H$ between two $C$-vertices at
positions $p \ne q$ in $\{1, \dots, 14\}$ whose interior is off $C$
(and, being in $H$, avoids $u_1, v, u_2$); write it
$(\mathrm{lo}, \mathrm{hi}, s)$ with $\mathrm{lo} < \mathrm{hi}$ the
endpoint positions and $s \ge 2$ its length. Its **shortening** is
$(\mathrm{hi} - \mathrm{lo}) - s$. By `c16_dip_decomposition`, a
completion at $d = 1$ is any length-$12$ $f_2 \to f_1$ path in $H$,
and every validity condition (16 distinct vertices, arc-sharing,
chordedness) is then automatic.

**Statement — proved part (three sufficient configurations).** Each
of the following ear configurations yields a valid completion, by an
explicit simple path of length $15 - 3 = 12$:

- **(L1) Single ear, shortening $3$**: an interior ear with
  $\mathrm{hi} - \mathrm{lo} = s + 3$. Path: arc
  $0 \to \mathrm{lo}$, ear, arc $\mathrm{hi} \to 15$. Simplicity is
  immediate (two disjoint arc pieces of length $\ge 1$ joined by an
  off-$C$ ear).

- **(L2) Sequential pair, total shortening $3$**: interior ears
  $e_1 = (\mathrm{lo}_1, \mathrm{hi}_1, s_1)$,
  $e_2 = (\mathrm{lo}_2, \mathrm{hi}_2, s_2)$ with
  $\mathrm{hi}_1 \le \mathrm{lo}_2$, vertex-disjoint interiors, and
  shortenings summing to $3$. Path: arc $0 \to \mathrm{lo}_1$,
  $e_1$, arc $\mathrm{hi}_1 \to \mathrm{lo}_2$, $e_2$, arc
  $\mathrm{hi}_2 \to 15$. (At $\mathrm{hi}_1 = \mathrm{lo}_2$ the
  middle arc is a single vertex, visited once.)

- **(L3) Interleaved pair, one backtrack**: interior ears with
  $\mathrm{lo}_1 < \mathrm{lo}_2 \le \mathrm{hi}_1 < \mathrm{hi}_2$,
  vertex-disjoint interiors, and
  $(\mathrm{hi}_2 - \mathrm{hi}_1) + (\mathrm{lo}_2 - \mathrm{lo}_1)
  = s_1 + s_2 + 3$. Path: arc $0 \to \mathrm{lo}_1$, $e_1$ (to
  $\mathrm{hi}_1$), arc BACKWARD $\mathrm{hi}_1 \to \mathrm{lo}_2$,
  $e_2$, arc $\mathrm{hi}_2 \to 15$. Length
  $\mathrm{lo}_1 + s_1 + (\mathrm{hi}_1 - \mathrm{lo}_2) + s_2 +
  (15 - \mathrm{hi}_2) = 12$ by the displayed identity; the three
  arc pieces $[0, \mathrm{lo}_1]$, $[\mathrm{lo}_2, \mathrm{hi}_1]$,
  $[\mathrm{hi}_2, 15]$ are pairwise disjoint by the position
  ordering, so the path is simple.

In all three cases the first and last edges are $C$-edges
($\mathrm{lo}_1 \ge 1$, $\mathrm{hi}_{\text{last}} \le 14$) and the
completion is valid by `c16_dip_decomposition` (a), (c), (e).

**Proved (R85 — supply-floor and exclusion arithmetic).** Three
further facts, each a proof:

- **(E1) Interiority is free.** In $H$, positions $0$ and $15$
  carry no spokes: $f_1$ is a foot of $u_1$, and since $C$ is
  chordless and $G$ cubic, each $C$-vertex has exactly ONE outside
  edge — so $f_1$'s unique outside edge goes to $u_1 \in
  \{u_1, v, u_2\}$, deleted in $H$ (likewise $f_2 \to u_2$). Hence
  EVERY ear of $H$ has both endpoints in positions $1..14$: the
  interior-ear restriction in the statement is vacuous, and every
  pigeonhole ear below lands in the usable range automatically.

- **(E2) Ear exclusion law.** Every ear $(\mathrm{lo}, \mathrm{hi},
  s)$ satisfies $c + s \notin \{4, 8\}$, where $c := \min(\mathrm{hi}
  - \mathrm{lo},\ 16 - (\mathrm{hi} - \mathrm{lo}))$ is the cycle
  distance of its feet. Proof: the ear together with the shorter
  $C$-arc between its feet is a cycle of length $c + s$, forbidden
  at $4$ and $8$ by $\{C_4, C_8\}$-freeness; the ear with the longer
  arc has length $(16 - c) + s \ge 10$ (as $s \ge 2$, $c \le 8$), so
  no second constraint arises. Corollaries: (i) an $s = 2$ ear has
  $c \notin \{2, 6\}$, position gap $\notin \{2, 6, 10, 14\}$, and
  shortening $\notin \{0, 4, 8, 12\}$; (ii) **odd shortenings are
  never obstructed**: a non-straddling ear ($\mathrm{hi} -
  \mathrm{lo} \le 8$) with odd shortening has $c + s = 2s +
  \mathrm{shortening}$ odd $\notin \{4, 8\}$ — in particular the L1
  shortening $3$ faces NO $C_4/C_8$ obstruction, matching its
  $95\%$ share of the census.

- **(E3) Supply floor.** Every legal $\tau \ge 2$, $d = 1$ landing's
  menu contains at least one $s = 2$ ear. Proof: by
  `chordless_c16_ear_geometry` (e) the $16$ spokes of $C$ land on
  $\le 14$ outside vertices; deleting $u_1, v, u_2$ removes three
  outside vertices and at most $4$ spokes ($u_1, u_2$ carry $\le 2$
  feet each, $v$ none), leaving $\ge 12$ spokes on $\le 11$ outside
  vertices. Pigeonhole: some surviving outside vertex $w$ carries
  $\ge 2$ spokes, and its two distinct feet give an $s = 2$ ear
  through $w$ — interior by (E1). By (E2)(i) its shortening lies in
  $\{-1, 1, 2, 3, 5, 6, 7, 9, 10, 11\}$; if $3$, the landing is L1
  outright.

- **(E4) 3-spoke arc-triple law (R86).** A surviving outside vertex
  $w$ with THREE spokes cuts $C$ into an arc triple $(x, y, z)$,
  $x + y + z = 16$, and each of $x, y, z$ avoids $\{2, 6, 10, 14\}$
  — apply (E2) to each of the three $s = 2$ ears through $w$ (a
  pair of feet at consecutive-arc distance $x$ has cycle distance
  $\min(x, 16 - x) \notin \{2, 6\}$). Exactly SEVEN unordered
  triples survive: $(1,3,12)$, $(1,4,11)$, $(1,7,8)$, $(3,4,9)$,
  $(3,5,8)$, $(4,4,8)$, $(4,5,7)$ — all seven occur on the corpus
  ($437$ 3-spoke vertices, distribution $145/68/62/47/33/50/32$).
  Six of the seven triples contain an arc in $\{3, 4, 5\}$ and so
  provide an $s = 2$ ear of shortening $1$, $2$, or $3$ (position
  gap = arc for feet consecutive along the triple, when interior);
  the single exception is $(1, 7, 8)$, whose ears have shortenings
  $\{-1, 5, 6\}$. So a 3-spoke vertex is a small-shortening
  supplier unless its triple is exactly $(1, 7, 8)$ — a dichotomy a
  supply proof can case on.

**Proved (shape exhaustion at depth $\le 2$).** A simple
$f_2 \to f_1$ path whose off-$C$ part consists of ONE ear is L1; of
TWO ears, it is L2 or L3: the first arc must start at $0$ and move
forward, so $e_1$ is traversed low-to-high; after $e_1$ the path
sits at $\mathrm{hi}_1$ with $[0, \mathrm{lo}_1] \cup \{$ear$_1\}$
used, and the next arc either moves forward to $\mathrm{lo}_2 \ge
\mathrm{hi}_1$ (L2) or backward to $\mathrm{lo}_2 \le \mathrm{hi}_1$
— and in the backward case $e_2$ must jump past $\mathrm{hi}_1$
(any $\mathrm{hi}_2 \le \mathrm{hi}_1$ strands the path behind
visited vertices), forcing the L3 ordering. So L1–L3 are the ONLY
depth-$\le 2$ completion shapes at $d = 1$.

**Census (probe record, R84).** Over all $1{,}629$ legal $d = 1$
landings of the corpus, the trio COVERS EVERYTHING, with partition:
L1 first: $1{,}543$; else L2: $79$; else L3: $7$. The seven
L3-only landings (graph, chordless-$C_{16}$ index in enumeration
order, $v$, $u_1$, $f_1$, $u_2$, $f_2$):
(n26, 7, 19, 12, 11, 20, 21), (n26, 8, 20, 19, 12, 21, 11),
(n28r1, 8, 3, 2, 18, 4, 17), (n28r1, 16, 4, 3, 2, 17, 18),
(n28r1, 18, 24, 13, 12, 25, 26), (n28r1, 19, 25, 24, 13, 26, 12),
(n28r3, 17, 25, 24, 5, 26, 6) — each with EXACTLY ONE valid L3
pair. Menu-arithmetic facts feeding the supply attack: the
single-ear shortening multiset per landing contains $-1$ in
$1{,}627/1{,}629$ landings, $+1$ in $1{,}607$, $+2$ in $1{,}574$,
$+3$ in exactly the $1{,}543$ L1 landings; interior menus carry
$13$–$78$ ears.

**Fragility census (probe record, R85).** Call an ear of a menu
**critical** if deleting it (alone) leaves a menu admitting no L1,
L2, or L3. Over all $1{,}629$ landings: exactly $8$ landings have a
critical ear — the seven L3-only landings above plus ONE L2-unique
landing hidden inside the L2 count, $(\mathrm{n28r4}, 2, 20, 12, 11,
21, 22)$ ($0$ L1 ears, exactly $1$ L2 pair, $0$ L3 pairs) — and each
fragile landing has EXACTLY $2$ critical ears, the two members of
its unique pair. The other $1{,}621$ landings survive every single
ear deletion. So the nearest falsifier candidates sit at distance
"one ear-deletion at one of 8 pinned landings"; a class member
realizing such a deletion (same landing geometry, one pair-ear
absent) is the sharpest falsification target. Further menu
arithmetic: $s = 2$ cycle gaps realize exactly $\{1, 3, 4, 5, 7,
8\}$ corpus-wide (the (E2) spectrum, all allowed values attained);
$816/1{,}629$ landings are covered by their $s = 2$ ears alone;
$53$ landings have ONLY gap-$1$ (triangle) $s = 2$ ears, so an
eventual supply proof cannot ride $s = 2$ ears exclusively; the
$-1$ shortening is absent from exactly $2$ menus (both L1
landings, pinned in CHECK 2).

**Extended census (probe record, R86 — the walk).** A seeded
2-edge-swap random walk INSIDE the class (each step preserves
cubicity; acceptance requires $C_4/C_8$-freeness and connectivity),
started at the five hosts n24, n26, n28r1, n28r3, n28r4 for $400$
accepted steps each, visited $1{,}690$ NEW class members carrying
chordless $C_{16}$s; ALL $31{,}377$ legal $\tau \ge 2$, $d = 1$
landings across them are covered by the trio (partition: L1
$24{,}930$, else-L2 $4{,}544$, else-L3 $1{,}903$) — ZERO uncovered
menus, a $\sim 20\times$ expansion of the R84 census, concentrated
deliberately around the fragile-8 hosts. The L3 share ($6\%$,
vs $0.4\%$ on the corpus) shows the walk reaches thinner menus
than the corpus, and the conjecture still holds. A trimmed
deterministic slice of the walk is pinned as CHECK 5.

**Open (the supply conjecture — sharpened by R85).** Every legal
$\tau \ge 2$, $d = 1$ landing in the class admits an L1, L2, or L3
configuration. This implies `c16_landing_universal` restricted to
$d = 1$ (sufficiency above); it is a priori STRONGER — depth-$\ge 3$
completions exist on the corpus but are never needed — so a
falsifier for THIS lemma (a menu missing all three layers) need not
falsify $d = 1$ closure itself. What (E1)–(E3) leave open is
exactly POSITION COMPATIBILITY: the menu provably contains an
$s = 2$ ear of unobstructed shortening, and odd-shortening ears are
arithmetically free, but nothing yet forces a shortening-$3$ ear or
a compatible (disjoint, sequential-or-interleaved,
total-shortening-$3$) pair to EXIST. The fragile-8 census bounds
how tight the corpus gets: never below two witnesses per landing.
Proof shape suggested by the data: (a) if some $w$ has $2$ spokes
at cycle gap $5$ (shortening $3$), done by L1; (b) otherwise mine
the $\ge 12$ spokes for TWO disjoint small-gap ears (gaps $3, 4$
give shortenings $1, 2$) at compatible positions, with the $53$
all-triangle-menu landings showing the needed fallback to $s \ge 3$
ears (shortening $0$ and $3$ at $s = 3$ are both legal there).

<!-- CHECK
# CHECK 1 - R84 three-layer census: over all 1,629 legal tau>=2 d=1
# landings, the interior ear menu admits L1 (single ear, shortening 3) in
# 1,543, else L2 (sequential disjoint pair, total shortening 3) in 79,
# else L3 (interleaved pair, one backtrack) in exactly 7 — pinned by
# identity, each with exactly ONE valid L3 pair. Trio covers everything;
# sufficiency of each layer is constructive (see statement). ~1.5s.
# CHECK 2 - R85 supply-floor + fragility census, verified per landing:
# (i) INTERIORITY FREE: f1 and f2 carry no spokes in H (their unique
#     outside edge goes to the deleted u1 / u2), so every ear is interior;
# (ii) EXCLUSION LAW: every ear (lo, hi, s) has c + s not in {4, 8},
#     c = min(hi-lo, 16-(hi-lo));
# (iii) SUPPLY FLOOR: every menu contains an s=2 ear;
# (iv) FRAGILITY: exactly 8 landings have a critical ear (an ear whose
#     single deletion kills L1/L2/L3 coverage) — the 7 L3-only landings
#     plus the L2-unique landing (n28r4, 2, 20, 12, 11, 21, 22) — and
#     each fragile landing has EXACTLY 2 critical ears (its unique pair);
# (v) the -1 shortening is absent from exactly 2 menus, both L1 landings:
#     (n30s3, 44, 20, 8, 7, 19, 18) and (n30s5, 40, 25, 15, 14, 26, 27).
# CHECK 5 - R86 walk slice: seeded (rng 86) 2-edge-swap walk from n28r1
# inside the class (cubic preserved by the swap; acceptance = C4-free,
# C8-free, connected): 66 accepted class members, 2,376 legal tau>=2 d=1
# landings, every menu admits L1, L2 or L3 (counts pinned; ~2s). The full
# R86 walk (5 seeds x 400 steps, 1,690 members, 31,377 landings, zero
# uncovered) is a probe record in Section 126 of proof_strategy.md.
# CHECK 3 - R81 slack floor: every legal tau>=2 landing at feet distance 1
# (the tightest geometry, 1,629 landings over the full corpus) has >= 3
# distinct valid completions (early-exit count). Contrast: of the 181
# tau=1 d=1 route choices, EXACTLY the two R80 failures (n28r0 v=7 f1=9
# f2=27; n28r6 v=0 f1=4 f2=3) have zero completions.
import random
from collections import deque
from itertools import combinations
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
def arc_dist(pathC, a, b):
    g = abs(pathC.index(a) - pathC.index(b)) % 16
    return min(g, 16 - g)
def ok_count_capped(adj, vsC, esC, seg, cap):
    f1 = seg[0]; f2 = seg[-1]
    banned = set(seg[1:-1])
    L = 16 - (len(seg) - 1)
    nok = 0
    stack = [(f2, [f2])]
    while stack:
        cur, path = stack.pop()
        for w in adj[cur]:
            if w == f1:
                if len(path) == L:
                    cyc = seg + path[1:]
                    if len(set(cyc)) != 16: continue
                    es2 = set(frozenset((cyc[i], cyc[(i+1) % 16])) for i in range(16))
                    if not (esC & es2): continue
                    s2 = set(cyc)
                    ch = False
                    for a in cyc:
                        for b in adj[a]:
                            if b in s2 and frozenset((a, b)) not in es2: ch = True
                    if ch:
                        nok += 1
                        if nok >= cap: return nok
                continue
            if w in banned or w in path or w == f2: continue
            if len(path) >= L: continue
            stack.append((w, path + [w]))
    return nok
graphs = [ADJ24, to_adj(FLAT26, 26)] + [to_adj(f, 28) for f in REPS28]
gp = [[] for _ in range(28)]
for a, b in PIN28: gp[a].append(b); gp[b].append(a)
graphs.append(gp)
names = ["n24", "n26"] + [f"n28r{i}" for i in range(12)] + ["n28pin"]
graphs += [t_pet()] + slice10()
names += ["n30tpet"] + [f"n30s{i}" for i in range(10)]
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
EXPECT_L3 = [("n26", 7, 19, 12, 11, 20, 21), ("n26", 8, 20, 19, 12, 21, 11),
             ("n28r1", 8, 3, 2, 18, 4, 17), ("n28r1", 16, 4, 3, 2, 17, 18),
             ("n28r1", 18, 24, 13, 12, 25, 26), ("n28r1", 19, 25, 24, 13, 26, 12),
             ("n28r3", 17, 25, 24, 5, 26, 6)]
EXPECT_FRAGILE = sorted(EXPECT_L3 + [("n28r4", 2, 20, 12, 11, 21, 22)])
EXPECT_NO_M1 = [("n30s3", 44, 20, 8, 7, 19, 18),
                ("n30s5", 40, 25, 15, 14, 26, 27)]
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
l1 = l2 = 0; l3 = []; fragile = []; no_m1 = []
for name, adj in zip(names, graphs):
    n = len(adj)
    cs = all_c16(adj)
    chl = []
    for vs, es, path in cs:
        ch = False
        for a in path:
            for b in adj[a]:
                if b in vs and frozenset((a, b)) not in es: ch = True
        if not ch: chl.append((vs, es, path))
    for ci, (vsC, esC, pathC) in enumerate(chl):
        interior = [w for w in range(n) if w not in vsC
                    and not any(t in vsC for t in adj[w])]
        for v in interior:
            if dist_to(adj, v, vsC) != 2: continue
            tn = [(w, [f for f in adj[w] if f in vsC]) for w in adj[v]]
            tn = [(w, F) for w, F in tn if F]
            if len(tn) < 2: continue
            for a in range(len(tn)):
                for b in range(a+1, len(tn)):
                    u1, F1 = tn[a]; u2, F2 = tn[b]
                    for f1 in F1:
                        for f2 in F2:
                            if arc_dist(pathC, f1, f2) != 1: continue
                            i2 = pathC.index(f2); i1 = pathC.index(f1)
                            if (i1 - i2) % 16 == 1:
                                order = [pathC[(i2 - t) % 16] for t in range(16)]
                            else:
                                order = [pathC[(i2 + t) % 16] for t in range(16)]
                            posmap = {vtx: t for t, vtx in enumerate(order)}
                            E = []
                            for x, y, s, iv in ears_full(adj, set(vsC), {u1, v, u2}):
                                px, py = posmap[x], posmap[y]
                                if 1 <= px <= 14 and 1 <= py <= 14 and px != py:
                                    E.append((min(px, py), max(px, py), s, iv))
                            ident = (name, ci, v, u1, f1, u2, f2)
                            for f in (f1, f2):
                                for t in adj[f]:
                                    assert t in vsC or t in (u1, v, u2), \
                                        ("spoke at position 0/15", ident, f, t)
                            for lo, hi, s, iv in E:
                                assert min(hi - lo, 16 - (hi - lo)) + s not in (4, 8), \
                                    ("exclusion law violated", ident, lo, hi, s)
                            assert any(s == 2 for lo, hi, s, iv in E), \
                                ("menu without s=2 ear", ident)
                            if all(hi - lo - s != -1 for lo, hi, s, iv in E):
                                no_m1.append(ident)
                            ncrit = sum(1 for e in E
                                        if not cov([x for x in E if x is not e]))
                            if ncrit:
                                fragile.append((ident, ncrit))
                            if hits1(E):
                                l1 += 1; continue
                            if hits2(E):
                                l2 += 1; continue
                            pairs = hits3(E)
                            assert len(pairs) == 1, \
                                ("not exactly one L3 pair", name, ci, v, f1, f2, len(pairs))
                            l3.append(ident)
assert l1 == 1543, l1
assert l2 == 79, l2
assert sorted(l3) == sorted(EXPECT_L3), l3
print("CHECK 1 ok: L1", l1, "| L2", l2, "| L3", len(l3),
      "— trio covers all 1629 d=1 landings; L3-only landings pinned")
assert sorted(i for i, k in fragile) == EXPECT_FRAGILE, fragile
assert all(k == 2 for i, k in fragile), fragile
assert sorted(no_m1) == sorted(EXPECT_NO_M1), no_m1
print("CHECK 2 ok: interiority free | exclusion law c+s not in {4,8} |",
      "s=2 supply floor universal | fragile =", len(fragile),
      "landings (ncrit=2 each) | -1-missing =", len(no_m1))
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
rng = random.Random(86)
wadj = to_adj(REPS28[1], 28)
acc = walked = 0; att = 0
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
        walked += 1
        assert hits1(E) or hits2(E) or hits3(E), \
            ("WALK FALSIFIER: d=1 menu without L1/L2/L3", acc, sorted(E)[:20])
assert (acc, walked) == (66, 2376), (acc, walked)
print("CHECK 5 ok: 2-swap walk from n28r1 —", acc,
      "class members,", walked, "d=1 landings, zero uncovered menus")
CHECK -->
