---
id: template_placement
status: open
depends_on: [c16_d1_ear_cover, fragile_pair_geometry]
discharged_by_round: null
introduced_at_round: 89
---

# Lemma `template_placement` (open — the antipodal participation law; s=2/s=2 L3 catalog proved; the draft "template-only" placement law REFUTED same-round at 5-seed scale)

**Setting.** As `c16_d1_ear_cover`: $G$ connected cubic
$\{C_4, C_8\}$-free, $C$ a chordless $16$-cycle, a legal $\tau \ge 2$
landing at feet distance $d = 1$, interior ears
$(\mathrm{lo}, \mathrm{hi}, s)$ in the long-arc coordinate with
$1 \le \mathrm{lo} < \mathrm{hi} \le 14$, span
$\delta := \mathrm{hi} - \mathrm{lo}$, shortening $\delta - s$. The
**template** is a valid s$2$/s$2$ L3 pair with span set $\{3, 8\}$ —
in $(c, s, \text{shortening})$ terms $((3,2,1), (8,2,6))$, the shape
of all $270$ template-fragile critical pairs of
`fragile_pair_geometry`.

**Statement (open — the antipodal participation law).** In every
legal $\tau \ge 2$, $d = 1$ landing whose menu admits NO L1 and NO
L2:

- **(a)** every valid s$2$/s$2$ L3 pair contains an antipodal
  ($\delta = 8$) ear — equivalently (by T1 + T2 below) its span
  pair is one of $\{3,8\}, \{7,8\}, \{8,9\}, \{8,11\}$, i.e. the
  catalog pairs $\{4,7\}, \{4,9\}, \{7,12\}$ never occur in an
  L2-less menu;
- **(b)** the menu admits SOME valid L3 pair containing an
  antipodal ear (observed with $s \in \{2, 3\}$) — single named
  exception $(\mathrm{n28r3}, 17, 25, 24, 5, 26, 6)$, whose unique
  valid pair is the all-$c{=}7$ mixed $((7,2,5), (7,3,6))$.

(b) restricted to existence-of-any-pair is the L3 arm of
`c16_d1_ear_cover`'s supply conjecture; (a) is the attackable
structured half: three per-span-pair exclusion cases.

**REFUTATION RECORD (same round — do not re-derive).** The first
draft of this lemma stated a stronger "placement law": every
L1&L2-less menu carries the template $\{3,8\}$ pair, sole exception
n28r3. A 5-seed $\times$ 400-step walk (rng 91–95, seeds n24, n26,
n28r1, n28r3, n28r4; 2,000 members, 36,364 legal $d=1$ landings,
7,678 L1-less, 3,046 L2-less) REFUTES it, and with it the
collapse-hypothesis H2 ("non-template s$2$/s$2$ pairs occur only in
L2-present menus"): $646/3{,}046$ L2-less menus have no template —
$256$ carry a $\{7,8\}$ pair, $256$ an $\{8,9\}$ pair, $134$ have
no s$2$/s$2$ pair at all (the n28r3-type stratum RECURS; it is not
a finite named exception). The rng-86 slice's $264/264$
$\{3,8\}$-purity (CHECK B below) was seed locality. Also refuted
at scale: R88/R89's "fragility $=$ L3-onlyness" identity — the
$646$ non-template L2-less menus all have $4$–$5$ valid L3 pairs
and are NOT fragile ($295$ members show fragile $\ne$ L3-only).
What SURVIVED the same walk, $100\%$: T1's catalog ($0$ violations
on $7{,}678$ L1-less menus), trio coverage ($0$ uncovered menus in
$36{,}364$), and the participation law above ($2{,}912/2{,}912$
s$2$/s$2$ pairs contain $\delta = 8$; all $134$ empty-stratum menus
carry an antipodal-$s{=}3$ pair, shape $((\cdot),(8,3,5))$).

**T1 — the s$2$/s$2$ L3 span catalog (proved).** In any menu of an
L1-less landing, a valid s$2$/s$2$ L3 pair has unordered span pair in

$$\{3,4\},\ \{3,8\},\ \{4,7\},\ \{4,9\},\ \{7,8\},\ \{7,12\},\ \{8,9\},\ \{8,11\}.$$

*Proof.* Write the pair $e_1 = (\mathrm{lo}_1, \mathrm{hi}_1, 2)$,
$e_2 = (\mathrm{lo}_2, \mathrm{hi}_2, 2)$ with
$\mathrm{lo}_1 < \mathrm{lo}_2 \le \mathrm{hi}_1 < \mathrm{hi}_2$,
$a := \mathrm{lo}_2 - \mathrm{lo}_1 \ge 1$,
$b := \mathrm{hi}_2 - \mathrm{hi}_1 \ge 1$. L3 validity forces
$a + b = s_1 + s_2 + 3 = 7$, so $1 \le a \le 6$ and
$\delta_2 = \delta_1 + 7 - 2a$ (`fragile_pair_geometry` P1: opposite
parity). The constraints are:
(i) $a \le \delta_1$ (interleaving $\mathrm{lo}_2 \le \mathrm{hi}_1$);
(ii) $\delta_1 + 7 - a \le 13$ (positions: $\mathrm{lo}_1 \ge 1$ and
$\mathrm{hi}_2 = \mathrm{lo}_1 + \delta_1 + b \le 14$);
(iii) $\delta_1, \delta_2 \in \{1, 3, 4, 7, 8, 9, 11, 12, 13\}$ — an
$s = 2$ ear has $\delta \notin \{2, 6, 10, 14\}$ by the exclusion law
(E2)(i) of `c16_d1_ear_cover`, and $\delta \ne 5$ because a
$\delta = 5$, $s = 2$ ear has shortening $3$, i.e. is an L1 ear,
contradicting L1-lessness.
Enumerating $\delta_1$ over the nine allowed values and
$a \in \{1, \dots, \min(6, \delta_1)\}$: $\delta_1 = 1$ gives only
$\delta_2 = 6$ (excluded); $\delta_1 = 3$ gives $\{3,8\}$ ($a=1$) and
$\{3,4\}$ ($a=3$); $\delta_1 = 4$ gives $\{4,9\}$, $\{4,7\}$,
$\{3,4\}$ ($a = 1, 2, 4$; $a = 3$ hits $\delta_2 = 5$); $\delta_1 = 7$
gives $\{7,12\}$, $\{7,8\}$, $\{4,7\}$ ($a = 1, 3, 5$); $\delta_1 = 8$
gives $\{8,11\}$, $\{8,9\}$, $\{7,8\}$, $\{3,8\}$ ($a = 2, 3, 4, 6$;
$a = 1$ fails (ii): width $14$); $\delta_1 = 9$ gives $\{8,9\}$
($a=4$), $\{4,9\}$ ($a=6$); $\delta_1 = 11$ gives $\{8,11\}$ ($a=5$);
$\delta_1 = 12$ gives $\{7,12\}$ ($a=6$); $\delta_1 = 13$ fails (ii)
for every $a$ (width $\ge 14$). No other value of $\delta_2$ survives
(iii). $\square$

**T2 — L2-lessness kills $\{3,4\}$ (proved).** The catalog's
$\{3,4\}$ pair has a UNIQUE realization: $\delta_1 = 3$ forces
$a = 3$ (T1's enumeration), i.e.
$\mathrm{lo}_2 = \mathrm{lo}_1 + 3 = \mathrm{hi}_1$ — the two ears
are in the degenerate-sequential position
$\mathrm{hi}_1 = \mathrm{lo}_2$ (likewise from the $\delta_1 = 4$
side, $a = 4$). Their shortenings are $1 + 2 = 3$ and their
interiors are disjoint, so the SAME pair is a valid L2 pair (L2
permits $\mathrm{hi}_1 = \mathrm{lo}_2$: single-vertex middle arc).
Hence in an L2-less menu no $\{3,4\}$ pair exists, and the feasible
s$2$/s$2$ catalog shrinks to SEVEN span pairs, of which the template
$\{3, 8\}$ is the only one the census below ever realizes in an
L1-less, L2-less menu. $\square$

**Census (probe records, R89).** Corpus ($1{,}629$ landings, $86$
L1-less, $7$ L2-less), rng-86 slice ($2{,}376$ landings, $396$
L1-less, $264$ L2-less; CHECK B), 5-seed walk ($36{,}364$
landings, $7{,}678$ L1-less, $3{,}046$ L2-less; probe record):

- **s$2$/s$2$ family purity.** Every L2-less menu realizes at most
  ONE s$2$/s$2$ span-pair family, never a mixture. 5-seed
  histogram: $\{3,8\}$: $2{,}400$; $\{7,8\}$: $256$; $\{8,9\}$:
  $256$; none: $134$. Corpus: $\{3,8\}$: $6$; none: $1$ (n28r3).
  rng-86 slice: $\{3,8\}$: $264$.
- **Antipodal participation, $100\%$.** Zero s$2$/s$2$ pairs
  without a $\delta = 8$ ear across all L2-less menus, all three
  censuses. The $134$ empty-stratum menus split into exactly two
  menu shape-families (counts $84$ / $50$), and BOTH contain a
  valid pair of shape $((\cdot), (8,3,5))$ — an antipodal
  $s = 3$ ear. Statement (b)'s only failure anywhere: corpus
  n28r3 (its $s{=}2$ spans are $\{1,4,7,11\}$; unique pair
  all-$c{=}7$).
- **Fragility refined.** Over the 5-seed walk's L2-less menus:
  fragile $\Leftrightarrow$ family $\{3,8\}$ with a UNIQUE valid
  pair ($2{,}400$ menus, each exactly $1$ pair); the $646$
  non-template L2-less menus all have $4$–$5$ valid pairs, none
  fragile. R88's template-fragility law survives (every fragile
  landing IS template-shaped); its converse ("L3-only
  $\Rightarrow$ fragile") does not.
- **Catalog occupancy.** L1-less menus, corpus: $\{3,8\}$ $16$,
  $\{4,7\}$ $7$, $\{4,9\}/\{7,8\}/\{7,12\}/\{8,9\}$ $1$ each
  ($\{8,11\}$ under L1 only; $\{3,4\}$ never). 5-seed L1-less:
  the non-antipodal pairs $\{4,7\}$ ($46$ menus) and $\{4,9\}$
  ($95$) occur ONLY in L2-present menus — statement (a)
  unfalsified at $7{,}678$-menu scale.

**Open (the revised supply core).**
- **(a) three exclusion cases:** show an L1-less menu containing a
  valid $\{4,7\}$, $\{4,9\}$, or $\{7,12\}$ s$2$/s$2$ pair admits
  an L2 (or an L1). Data to mine: $\{4,7\}$ has $46 + 7$
  realizations, $\{4,9\}$ has $95 + 1$; $\{7,12\}$ is
  near-extinct ($1$ corpus menu). The T2 mechanism (a pair
  configuration that IS an L2) is the model — look for forced
  companion ears from the pair's own feet via E3/E4 spoke
  arithmetic.
- **(b) existence:** every L2-less menu admits a valid pair
  containing an antipodal ear ($s \in \{2,3\}$ observed),
  exceptions finite/named. Sub-question: why does the
  empty-s$2$/s$2$ stratum always carry the $(8,3,5)$
  antipodal-$s{=}3$ shape — is there an E3-style floor for
  antipodal $s \le 3$ ears in L2-less menus?
- **Next falsification targets:** scale the walk further hunting
  for (i) a non-antipodal s$2$/s$2$ pair in an L2-less menu (kills
  (a)), (ii) an L2-less menu with no antipodal-ear valid pair
  (kills (b) or grows its exception class), (iii) a non-antipodal
  pair none of whose ears joins an L2 (kills the reuse law below).

**T3 — the reuse candidate is always available (proved, R90).**
The three non-antipodal catalog pairs have shortening multisets
$\{4,7\} \to \{2,5\}$, $\{4,9\} \to \{2,7\}$,
$\{7,12\} \to \{5,10\}$ (shortening $= \delta - 2$); each contains
an element of $\{2, 5\}$. A shortening-$2$ ear completes to an L2
with any disjoint sequential shortening-$1$ ear, a
shortening-$5$ ear with any disjoint sequential
shortening-$(-2)$ ear — and BOTH companion types are E2-legal
(odd shortenings are never obstructed by (E2)(ii); a
shortening-$(-2)$ ear has $c + s = 2s - 2 \notin \{4, 8\}$ iff
$s \notin \{3, 5\}$, and $s = 4$ realizes it, e.g. the observed
$(1,3,4)$ companions). $\square$

**The reuse law (open, R90 — census-backed $150/150$).** In an
L1-less menu, EVERY valid non-antipodal s$2$/s$2$ L3 pair has an
ear that itself participates in a valid L2 pair of the menu.
Census: all $9$ corpus occurrences ($\{4,7\}$: $7$, $\{4,9\}$: $1$,
$\{7,12\}$: $1$) and all $141$ 5-seed-walk occurrences ($\{4,7\}$:
$46$, $\{4,9\}$: $95$) — no exception. Observed reuse mechanisms
match T3: the pair's shortening-$2$ ear joins a shortening-$1$
companion, or its shortening-$5$ ear joins a
shortening-$(-2)$ companion. The reuse law IMPLIES statement (a)
(the menu admits an L2), and is sharper: it says WHERE the L2
lives. Proving it needs a supply argument for the companion ear —
the same engine statement (b) needs; the T2 degenerate mechanism
(companion forced by the pair's own feet) is the model to
generalize.

**The companion supply law (open, R91 — the reuse law refined to
one route).** Call the minimum-span ear of a non-antipodal
s$2$/s$2$ pair its **pilot** ($\delta = 4$ for $\{4,7\}$ and
$\{4,9\}$, $\delta = 7$ for the position-pinned $\{7,12\}$;
pilot shortenings $2, 2, 5$). Claim: in an L1-less menu the pilot
of every valid non-antipodal pair admits a sequential
interior-disjoint companion of the complementary shortening
($3 - \mathrm{short}$: $+1$, $+1$, $-2$), hence joins a valid L2.
This implies the reuse law and statement (a). R91 re-mining of the
5-seed walk ($7{,}700$ L1-less menus re-derived; occurrence counts
reproduce R90: $\{4,7\}$ $46$, $\{4,9\}$ $95$, $\{7,12\}$ $0$):

- **Route asymmetry.** $\{4,7\}$: BOTH T3 routes are available in
  $46/46$ menus (short-$2$ ear $+$ short-$1$ companion AND
  short-$5$ ear $+$ short-$(-2)$ companion). $\{4,9\}$: the pilot
  route exists in $95/95$, while the short-$7$ ear's $(-4)$
  companion — E2-legal at $(\delta, s) \in \{(1,5), (3,7),
  (4,8)\}$ — is realized in $0/95$. The reuse mechanism for
  $\{4,9\}$ is EXCLUSIVELY the pilot route.
- **Shape rigidity ($\{4,7\}$).** The short-$1$ companion is
  UNIQUE in all $46$ menus and always $(\delta, s) = (3, 2)$ at
  window gap $4$ from the pilot; the $(-2)$ companion is always
  $(2, 4)$ at window gap $1$. Only two pair realizations occur:
  $(2,6)\,\&\,(4,11)$ ($44$ menus) and $(4,11)\,\&\,(9,13)$
  ($2$) — both carry the ear $(4,11)$.
- **$\{4,9\}$ companions.** $1$–$2$ per menu ($57$ menus have
  exactly one, $38$ have two), shapes $(3,2)/(4,3)/(6,5)$ — all
  shortening $1$, mixed sides.
- **Stratum locality.** ALL $141$ walk occurrences lie on the
  n28r3 seed's walk (first $\{4,9\}$ at member $90$, first
  $\{4,7\}$ at member $92$); seeds n24, n26, n28r1, n28r4 produce
  NONE in $400$ steps each. Non-antipodal pairs are an
  n28r3-adjacent phenomenon, like the empty family (CHECK C) —
  the exotic strata cluster around the same host.
- **Diversity (not one recurring landing).** The $141$
  occurrences spread over $93$ distinct walk members, $60$
  distinct landing identities, and $50$ distinct pair
  interior-vertex-sets; the companion's host interior varies too
  ($37$ distinct vertex-sets). Unlike the rng-86 purity artifact
  (seed locality, refuted at 5-seed scale), the census weight
  here is carried by genuinely distinct configurations — the
  invariant is the forced companion SHAPE, not a recurring host.

Proof target as sharpened: prove the short-$1$ companion for
$\delta = 4$ pilots (covers $\{4,7\}$ and $\{4,9\}$) and the
$(-2)$ route for the pinned $\{7,12\}$ realization
$(1,8)\,\&\,(2,14)$ — the census says the $\delta 4$-pilot route
is what the class actually supplies, and for $\{4,7\}$ it
supplies it with a forced shape.
<!-- CHECK
# CHECK A - R89 placement law + catalog on the four hosting reps
# (n26, n28r1, n28r3, n28r4 — every corpus L1&L2-less landing lives here):
# (i) the L1-less, L2-less landings are EXACTLY the seven pinned idents;
# (ii) six of them have s2/s2 valid-L3 span-set family exactly {{3,8}}
#      (the template, present and unique);
# (iii) the n28r3 exception has NO s2/s2 valid pair and carries the mixed
#      ((7,2,5),(7,3,6)) pair;
# (iv) EVERY s2/s2 valid L3 pair in EVERY L1-less landing of these hosts
#      has unordered span pair inside the proved 8-catalog (T1).
from collections import deque
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
CAT8 = {(3, 4), (3, 8), (4, 7), (4, 9), (7, 8), (7, 12), (8, 9), (8, 11)}
N28R3 = ("n28r3", 17, 25, 24, 5, 26, 6)
EXPECT_L3ONLY = {("n26", 7, 19, 12, 11, 20, 21), ("n26", 8, 20, 19, 12, 21, 11),
    ("n28r1", 8, 3, 2, 18, 4, 17), ("n28r1", 16, 4, 3, 2, 17, 18),
    ("n28r1", 18, 24, 13, 12, 25, 26), ("n28r1", 19, 25, 24, 13, 26, 12), N28R3}
graphs = [("n26", to_adj(FLAT26, 26))] + [(k, to_adj(v, 28)) for k, v in R28.items()]
l3only = set()
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
                            if hits1(E): continue
                            ident = (name, ci, v, u1, f1, u2, f2)
                            p3 = hits3(E)
                            s22 = set(tuple(sorted((e1[1]-e1[0], e2[1]-e2[0])))
                                      for e1, e2 in p3 if e1[2] == 2 and e2[2] == 2)
                            for sp in s22:
                                assert sp in CAT8, ("catalog violation", ident, sp)
                            if hits2(E): continue
                            l3only.add(ident)
                            if ident == N28R3:
                                assert not s22, ("n28r3 grew an s2/s2 pair", s22)
                                shapes = set()
                                for e1, e2 in p3:
                                    sh = tuple(sorted(
                                        (min(e[1]-e[0], 16-(e[1]-e[0])), e[2],
                                         e[1]-e[0]-e[2]) for e in (e1, e2)))
                                    shapes.add(sh)
                                assert ((7, 2, 5), (7, 3, 6)) in shapes, shapes
                            else:
                                assert s22 == {(3, 8)}, ("template missing/impure",
                                                         ident, s22)
assert l3only == EXPECT_L3ONLY, sorted(l3only)
print("CHECK A ok: 7 L1&L2-less landings pinned — 6x template {3,8}",
      "(present AND the only s2/s2 shape), n28r3 exception has no s2/s2",
      "pair and carries ((7,2,5),(7,3,6)); s2/s2 catalog holds on 4 hosts")
CHECK
-->

<!-- CHECK
# CHECK B - R89 catalog + antipodal participation on the rng-86 walk slice
# (the CHECK-5 walk of c16_d1_ear_cover): 66 class members, 2,376 legal
# tau>=2 d=1 landings, 396 L1-less of which 264 L1&L2-less. Asserts: every
# s2/s2 valid L3 pair in an L1-less menu is inside the T1 8-catalog, and
# every L1&L2-less menu here has s2/s2 family exactly {{3,8}} — a pinned
# SLICE fact (this slice is seed-local: the 5-seed walk also realizes
# {7,8}, {8,9} and empty families — see the refutation record above; what
# {3,8}-purity witnesses for the lemma is antipodal participation).
import random
from collections import deque
def to_adj(flat, n):
    nums = [int(x) for x in flat.split(",")]
    adj = [[] for _ in range(n)]
    for a, b in zip(nums[::2], nums[1::2]):
        adj[a].append(b); adj[b].append(a)
    return adj
REPS28_1 = "0,1,0,15,0,16,1,2,1,16,2,3,2,18,3,4,3,23,4,5,4,17,5,6,5,21,6,7,6,25,7,8,7,22,8,9,8,20,9,10,9,20,10,11,10,19,11,12,11,19,12,13,12,26,13,14,13,24,14,15,14,27,15,27,16,17,17,18,18,19,20,21,21,22,22,23,23,24,24,25,25,26,26,27"
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
CAT8 = {(3, 4), (3, 8), (4, 7), (4, 9), (7, 8), (7, 12), (8, 9), (8, 11)}
rng = random.Random(86)
wadj = to_adj(REPS28_1, 28)
acc = att = 0; n_l1less = n_l2less = 0
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
        if hits1(E): continue
        n_l1less += 1
        s22 = set(tuple(sorted((e1[1]-e1[0], e2[1]-e2[0])))
                  for e1, e2 in hits3(E) if e1[2] == 2 and e2[2] == 2)
        for sp in s22:
            assert sp in CAT8, ("WALK catalog violation", acc, sp)
        if hits2(E): continue
        n_l2less += 1
        assert s22 == {(3, 8)}, ("WALK placement falsifier", acc, s22)
assert (acc, n_l1less, n_l2less) == (66, 396, 264), (acc, n_l1less, n_l2less)
print("CHECK B ok: walk slice — 66 members, 396 L1-less (catalog holds),",
      "264 L1&L2-less ALL with s2/s2 family exactly {{3,8}}: the template",
      "is present and unique, zero exceptions")
CHECK
-->

<!-- CHECK
# CHECK C - R90 deterministic witnesses that the non-{3,8} L2-less families
# are REAL and nearby (the 5-seed walk is too slow for a CHECK, so two short
# prefix walks pin one witness each): (i) rng-94 walk from n28r3, 3 accepted
# steps: member 3 carries an EMPTY-family (no-s2/s2) L2-less menu, members
# 1-2 carry none; (ii) rng-95 walk from n28r4, 29 accepted steps: member 29
# carries BOTH a {7,8}-family and an {8,9}-family L2-less menu, members 1-28
# carry neither. Along both prefixes, every L1-less menu re-verifies the T1
# catalog, antipodal participation, family purity, and the reuse law (every
# non-antipodal s2/s2 pair has an ear inside a valid L2 pair). ~2s.
import random
from collections import deque
def to_adj(flat, n):
    nums = [int(x) for x in flat.split(",")]
    adj = [[] for _ in range(n)]
    for a, b in zip(nums[::2], nums[1::2]):
        adj[a].append(b); adj[b].append(a)
    return adj
R28 = {"n28r3": "0,1,0,15,0,16,1,2,1,21,2,3,2,17,3,4,3,18,4,5,4,16,5,6,5,24,6,7,6,26,7,8,7,17,8,9,8,18,9,10,9,27,10,11,10,27,11,12,11,19,12,13,12,25,13,14,13,22,14,15,14,20,15,23,16,17,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27", "n28r4": "0,1,0,15,0,16,1,2,1,16,2,3,2,21,3,4,3,17,4,5,4,23,5,6,5,25,6,7,6,18,7,8,7,18,8,9,8,26,9,10,9,19,10,11,10,19,11,12,11,22,12,13,12,20,13,14,13,24,14,15,14,27,15,27,16,17,17,18,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27"}
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
        if any(b in vs and frozenset((a, b)) not in es
               for a in path for b in adj[a]): continue
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
CAT8 = {(3, 4), (3, 8), (4, 7), (4, 9), (7, 8), (7, 12), (8, 9), (8, 11)}
def prefix_walk(host_flat, seed, nsteps):
    rng = random.Random(seed)
    wadj = to_adj(host_flat, 28)
    acc = att = 0
    fams = []
    while acc < nsteps and att < 60000:
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
            if hits1(E): continue
            p2 = hits2(E)
            s22 = set(tuple(sorted((e1[1]-e1[0], e2[1]-e2[0])))
                      for e1, e2 in hits3(E) if e1[2] == 2 and e2[2] == 2)
            for sp in s22:
                assert sp in CAT8, ("catalog", acc, sp)
                if 8 not in sp:
                    assert p2, ("participation", acc, sp)
                    prs = [(e1, e2) for e1, e2 in hits3(E)
                           if e1[2] == 2 and e2[2] == 2
                           and tuple(sorted((e1[1]-e1[0], e2[1]-e2[0]))) == sp]
                    for e1, e2 in prs:
                        assert any(f1 in (e1, e2) or f2 in (e1, e2)
                                   for f1, f2 in p2), ("reuse law", acc, sp)
            if p2: continue
            assert len(s22) <= 1, ("family purity", acc, s22)
            fams.append((acc, "empty" if not s22 else
                         {(3, 8): "38", (7, 8): "78",
                          (8, 9): "89"}.get(next(iter(s22)), "other")))
    assert acc == nsteps, acc
    return fams
f3 = prefix_walk(R28["n28r3"], 94, 3)
assert any(step == 3 and fam == "empty" for step, fam in f3), f3
assert all(fam == "38" for step, fam in f3 if step < 3), f3
f4 = prefix_walk(R28["n28r4"], 95, 29)
got = {fam for step, fam in f4 if step == 29}
assert {"78", "89"} <= got, sorted(f4)[-6:]
assert all(fam == "38" for step, fam in f4 if step < 29), \
    [x for x in f4 if x[0] < 29 and x[1] != "38"][:5]
print("CHECK C ok: empty-family witness at (n28r3-walk rng94, member 3);",
      "{7,8} and {8,9} witnesses both at (n28r4-walk rng95, member 29),",
      "none earlier; catalog + participation + purity + reuse law hold",
      "on all L1-less menus of both prefix walks")
CHECK
-->

<!-- CHECK
# CHECK D - R91 companion supply law: deterministic witnesses on the rng-94
# prefix walk from n28r3 (92 accepted steps, ~3s). Asserts: (i) NO
# non-antipodal s2/s2 pair occurs in any L1-less menu before member 90;
# (ii) member 90 carries exactly one {4,9} occurrence — pair (4,13)&(10,14),
# pilot (10,14) with short-1 companions exactly {(2,5,2),(3,9,5)} and NO
# (-4) companion for the short-7 ear; (iii) member 92 carries exactly two
# {4,7} occurrences, both pair (2,6)&(4,11), pilot short-1 companion
# UNIQUE = (10,13,2), and (1,3,4) among the (-2) companions of (4,11);
# (iv) every occurrence satisfies the companion supply law (pilot has a
# sequential disjoint complementary-shortening companion).
import random
from collections import deque
def to_adj(flat, n):
    nums = [int(x) for x in flat.split(",")]
    adj = [[] for _ in range(n)]
    for a, b in zip(nums[::2], nums[1::2]):
        adj[a].append(b); adj[b].append(a)
    return adj
N28R3 = "0,1,0,15,0,16,1,2,1,21,2,3,2,17,3,4,3,18,4,5,4,16,5,6,5,24,6,7,6,26,7,8,7,17,8,9,8,18,9,10,9,27,10,11,10,27,11,12,11,19,12,13,12,25,13,14,13,22,14,15,14,20,15,23,16,17,18,19,19,20,20,21,21,22,22,23,23,24,24,25,25,26,26,27"
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
def hits3(EE):
    return [(e1, e2) for e1 in EE for e2 in EE
            if e1 is not e2 and e1[0] < e2[0] <= e1[1] < e2[1]
            and (e2[1]-e1[1]) + (e2[0]-e1[0]) == e1[2]+e2[2]+3
            and not (e1[3] & e2[3])]
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
        if any(b in vs and frozenset((a, b)) not in es
               for a in path for b in adj[a]): continue
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
TARGETS = {(4, 7), (4, 9), (7, 12)}
rng = random.Random(94)
wadj = to_adj(N28R3, 28)
acc = att = 0
occ = []
while acc < 92 and att < 200000:
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
        if hits1(E): continue
        for e1, e2 in hits3(E):
            if e1[2] != 2 or e2[2] != 2: continue
            sp = tuple(sorted((e1[1]-e1[0], e2[1]-e2[0])))
            if sp not in TARGETS: continue
            pilot = e1 if (e1[1]-e1[0]) <= (e2[1]-e2[0]) else e2
            other = e2 if pilot is e1 else e1
            pc = sorted((g[0], g[1], g[2]) for g in E if g is not pilot
                        and (g[1]-g[0]-g[2]) == 3-(pilot[1]-pilot[0]-pilot[2])
                        and not (g[3] & pilot[3])
                        and (g[1] <= pilot[0] or g[0] >= pilot[1]))
            oc = sorted((g[0], g[1], g[2]) for g in E if g is not other
                        and (g[1]-g[0]-g[2]) == 3-(other[1]-other[0]-other[2])
                        and not (g[3] & other[3])
                        and (g[1] <= other[0] or g[0] >= other[1]))
            assert pc, ("companion supply law violated", acc, sp, pilot)
            occ.append((acc, sp, (pilot[0], pilot[1]), (other[0], other[1]),
                        tuple(pc), tuple(oc)))
assert acc == 92, acc
assert all(o[0] >= 90 for o in occ), occ
o90 = [o for o in occ if o[0] == 90]
assert len(o90) == 1 and o90[0][1] == (4, 9), o90
assert o90[0][2] == (10, 14) and o90[0][3] == (4, 13), o90
assert set(o90[0][4]) == {(2, 5, 2), (3, 9, 5)}, o90
assert o90[0][5] == (), o90   # the (-4) route: no companion for the short-7 ear
o92 = [o for o in occ if o[0] == 92]
assert len(o92) == 2 and all(o[1] == (4, 7) for o in o92), o92
for o in o92:
    assert o[2] == (2, 6) and o[3] == (4, 11), o
    assert o[4] == ((10, 13, 2),), o     # pilot short-1 companion UNIQUE
    assert (1, 3, 4) in o[5], o          # the (-2) companion of (4,11)
assert len(occ) == 3, occ
print("CHECK D ok: rng-94 prefix (92 members) — no non-antipodal pair before",
      "member 90; {4,9} witness at 90 (pilot (10,14), 2 short-1 companions,",
      "no -4 route); two {4,7} occurrences at 92 (pilot (2,6), companion",
      "(10,13,2) unique, (1,3,4) is the -2 companion); companion supply law",
      "holds on every occurrence")
CHECK
-->
