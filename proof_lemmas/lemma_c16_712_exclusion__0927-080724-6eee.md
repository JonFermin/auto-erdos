---
id: c16_712_exclusion
status: proved
depends_on: [c16_d1_ear_cover, template_placement, c16_dip_decomposition]
discharged_by_round: null
introduced_at_round: 98
---

# Lemma `c16_712_exclusion` (proved — the $\{7,12\}$ span pair is pinned, third-foot-rigid, and DEAD at $n = 24$ unconditionally)

**Setting.** As `c16_d1_ear_cover`: $G$ connected cubic
$\{C_4, C_8\}$-free, $24 \le n \le 30$, $C$ a chordless $16$-cycle,
$(f_1, u_1, v, u_2, f_2)$ a legal $\tau \ge 2$ landing at feet
distance $d = 1$ ($v$ a $0$-spoke outside vertex at distance $2$,
$u_1 \ne u_2$ T-neighbours of $v$ with feet $f_1, f_2$ adjacent on
$C$), long-arc coordinate $0..15$ with $f_2$ at $0$, $f_1$ at $15$.
This lemma resolves the $\{7,12\}$ case of `template_placement`'s
participation law (a) — the span pair the entire $\sim 29{,}500$-menu
census has never once realized — by proving it is the MOST rigid of
the three non-antipodal catalog pairs, and outright impossible at
$n = 24$.

**Statement.**

- **(a) Pinning (proved, all $n$ in the box).** A valid s$2$/s$2$
  L3 pair with span pair $\{7,12\}$ has EXACTLY two realizations in
  the long-arc coordinate, and they are mirror images: realization
  A $= \{e_1 = (1, 8, 2),\ e_2 = (2, 14, 2)\}$ and realization
  B $= \{(1, 13, 2), (7, 14, 2)\}$, the image of A under the
  reflection $\rho : j \mapsto 15 - j$. Since reversing the landing
  tuple to $(f_2, u_2, v, u_1, f_1)$ is again a legal $\tau \ge 2$,
  $d = 1$ landing of the same graph and relabels positions by
  $\rho$, realization A is fully general.

- **(b) Spoke pinning (proved).** In realization A the interior
  vertices $w_1$ (of $e_1$) and $w_2$ (of $e_2$) are distinct, the
  four spokes at positions $1, 8 \to w_1$ and $2, 14 \to w_2$ are
  the UNIQUE outside edges of those four $C$-vertices, $w_1 w_2
  \notin E(G)$ (else $w_1\,1\,2\,w_2$ is a $C_4$), and each of
  $w_1, w_2$ has exactly one further edge.

- **(c) Third-foot menus (proved, all $n$ in the box).** If
  $w_1$'s third edge is a spoke to position $p$, then in any menu
  $p \in \{4, 5, 9, 12, 13\}$ (pure $C_4/C_8$ arithmetic), and in
  an L1-less menu $p \in \{4, 5, 9, 12\}$ (the ear $8\,w_1\,13$ has
  shortening $3$). If $w_2$'s third edge is a spoke to position
  $q$, then $q \in \{3, 6, 10, 13\}$ by pure $C_4/C_8$ arithmetic —
  NO menu hypothesis needed — via four cross-vertex $C_8$ kills
  BEYOND the same-vertex law (E2): $q = 5$ dies to the $C_8$
  $w_1\,1\,2\,w_2\,5\,6\,7\,8\,w_1$, $q = 11$ to
  $w_1\,8\,9\,10\,11\,w_2\,2\,1\,w_1$, $q = 7$ to
  $w_2\,7\,8\,w_1\,1\,0\,15\,14\,w_2$ (the length-$1$ arc $7\,8$
  paired with the length-$3$ wrap arc $1\,0\,15\,14$), and $q = 9$
  to its partner $w_1\,8\,9\,w_2\,14\,15\,0\,1\,w_1$.

- **(d) Compatible-pair law (proved, all $n$ in the box).** If
  both $w_1, w_2$ are $3$-spoke with third feet $(p, q) \in
  \{4,5,9,12\} \times \{3,6,10,13\}$, the cross-vertex $C_8$ law
  kills exactly TEN of the $16$ combinations:
  $(4,3), (5,6), (9,6), (9,10), (12,13)$ via a length-$1$ arc
  between the third feet paired with a wrap arc ($2\,1$ or
  $14\,15\,0\,1$), and $(4,6), (4,10), (12,3), (12,6), (12,10)$
  via two length-$2$ arcs (e.g. $(4,6)$: $C_8 =
  w_1\,4\,3\,2\,w_2\,6\,7\,8\,w_1$). Exactly SIX pairs survive:
  $(4,13), (5,3), (5,10), (5,13), (9,3), (9,13)$ — in particular
  $p = 12$ is incompatible with EVERY third foot of $w_2$, and
  every surviving pair has $q \in \{3, 10, 13\}$.

- **(e) $n = 24$ exclusion (proved, UNCONDITIONAL).** No connected
  cubic $\{C_4, C_8\}$-free graph on exactly $24$ vertices contains
  realization A — hence, by (a), any valid $\{7,12\}$ pair — at any
  legal $\tau \ge 2$, $d = 1$ landing. No appeal to L1- or
  L2-lessness is needed. In particular the participation law (a) of
  `template_placement` holds vacuously for $\{7,12\}$ at $n = 24$.

**Proof of (a).** By T1 of `template_placement` (self-contained
arithmetic proved there): an s$2$/s$2$ pair has
$a + b = 7$, $\delta_2 = \delta_1 + 7 - 2a$, width
$\delta_1 + 7 - a$, and $\{7,12\}$ arises only at
$(\delta_1, a) \in \{(7, 1), (12, 6)\}$, both of width $13$. Width
$13$ with $\mathrm{lo}_1 \ge 1$, $\mathrm{hi}_2 \le 14$ forces
$\mathrm{lo}_1 = 1$, $\mathrm{hi}_2 = 14$: $(\delta_1, a) = (7,1)$
gives A, $(12, 6)$ gives B. $\rho$ maps A's $(1,8) \mapsto (7,14)$
and $(2,14) \mapsto (1,13)$, i.e. A $\mapsto$ B. (CHECK A.)

**Proof of (b).** $C$ chordless and $G$ cubic give each $C$-vertex
exactly one outside edge (E1 of `c16_d1_ear_cover`), so the ear
spokes are those unique edges. $w_1 = w_2$ would need $4$ spokes on
one cubic vertex. $w_1 w_2 \in E$ closes the $4$-cycle
$w_1, 1, 2, w_2$ ($1\,2$ is a $C$-edge). $\square$

**Proof of (c) and (d).** Finite $C_4/C_8$ arithmetic on the pinned
partial graph $C \cup \{f_1 u_1, u_1 v, v u_2, u_2 f_2\} \cup
\{1 w_1, 8 w_1, 2 w_2, 14 w_2\}$ plus the candidate spoke(s): any
$C_4$ or $C_8$ in a partial graph survives into every completion,
so a candidate that closes one is dead for all $G$. Same-vertex
kills are E2 (gaps $2, 6, 10$ close a $C_4$ resp. $C_8$ with the
short arc); the cross-vertex kills in (c) and (d) are $8$-cycles
using two spokes of $w_1$, two of $w_2$, and two vertex-disjoint
$C$-arcs of total length $4$, realized as $1 + 3$ (a length-$1$
arc plus a wrap arc through $0, 15$ or the pinned edge $1\,2$) or
$2 + 2$ (two length-$2$ arcs, one off each pinned foot pair).
Exhaustively verified by cycle enumeration on the actual partial
graphs (CHECK B, CHECK C); the survivor sets are exactly as stated.
The single L1-kill is the gap-$5$ ear $8\,w_1\,13$. A hand audit
of three machine-found kills — $(12,3)$:
$w_1\,12\,13\,14\,w_2\,3\,2\,1\,w_1$; $(4,10)$:
$w_1\,4\,3\,2\,w_2\,10\,9\,8\,w_1$; $(12,6)$:
$w_1\,8\,7\,6\,w_2\,14\,13\,12\,w_1$ — confirms each is a simple
$8$-cycle of $G$. $\square$

**Proof of (e).** Exhaustive completion enumeration; every step is
forced by counting, so the enumeration is COMPLETE:

1. At $n = 24$ the outside set has $8$ vertices: $u_1, v, u_2$ and
   $O := V \setminus (C \cup \{u_1, v, u_2\})$ with $|O| = 5$,
   namely $w_1, w_2$ and three further vertices $x_1, x_2, x_3$.
2. Positions $0$ and $15$ spoke to $u_2, u_1$; positions
   $1, 2, 8, 14$ spoke to $w_1, w_2$ (pinned). Each remaining
   position in $\{3,4,5,6,7,9,10,11,12,13\}$ carries exactly one
   outside edge, to one of: $u_1$ (a second foot, $\le 1$), $u_2$
   ($\le 1$), $w_1$ ($\le 1$, its third edge), $w_2$ ($\le 1$), or
   an $x_i$ ($\le 3$ each).
3. $v$ is $0$-spoke with neighbours $u_1, u_2$, so its third edge
   goes into $O$. $u_1$'s third slot (if not a foot) is an
   $O$-vertex or the edge $u_1 u_2$; likewise $u_2$. All remaining
   degree deficits in $O$ are closed by $O$–$O$ edges (simple
   graph). Every vertex must end at degree exactly $3$.
4. Enumerate ALL such completions ($x$-label symmetry broken by
   first-empty-slot; same-consumer position pairs at gaps
   $2, 6, 10$ pruned early — each closes a $C_4$/$C_8$ with the
   corresponding $C$-arc, sound for every completion). $173{,}090$
   assignments reach the full-graph test; each is tested directly
   for $C_4$/$C_8$ subgraphs (exhaustive cycle search to length
   $8$) and connectivity. ZERO survive. (CHECK D.)

The kill needs neither L1-lessness nor any menu hypothesis: the
pinned $\{7,12\}$ geometry is incompatible with cubic
$\{C_4, C_8\}$-freeness at $n = 24$ full stop. $\square$

**Relation to the program.** This is pre-committed next-move (b) of
Section 133 (the arc-exchange pause record). Combined with the
census ($0$ occurrences of $\{7,12\}$ in $\sim 29{,}500$ L1-less
non-antipodal menus, all seeds $n \in \{28\}$-stratum walks), the
$\{7,12\}$ case of the participation law now stands: proved at
$n = 24$, third-foot-rigid with an $11$-pair compatibility table at
$25 \le n \le 30$. The open remainder of the participation law is
the $\{4,7\}$/$\{4,9\}$ half (next-moves (a) and (c) of Section
133). The same completion-enumeration method extends to $n = 26$
($|O| = 7$, $O$–$O$ edges appear); a first $n = 26$ run is in
flight as a probe — if it closes UNSAT the exclusion extends; if
SAT, any survivor is a fully explicit legal graph whose menu
realizes $\{7,12\}$, i.e. a constructive falsifier of the
$\{7,12\}$ exclusion at $n = 26$ — either outcome is decisive
content for the next round.

<!-- CHECK
# CHECK A - pinning: {7,12} has exactly 2 realizations, mirrors, lo1=1.
reals = []
for d1 in [1, 3, 4, 7, 8, 9, 11, 12, 13]:
    for a in range(1, min(6, d1) + 1):
        d2 = d1 + 7 - 2 * a
        if d2 not in [1, 3, 4, 7, 8, 9, 11, 12, 13]:
            continue
        if frozenset([d1, d2]) != frozenset([7, 12]):
            continue
        width = d1 + 7 - a
        # lo1 >= 1 and lo1 + width <= 14
        for lo1 in range(1, 15 - width):
            e1 = (lo1, lo1 + d1)
            e2 = (lo1 + a, lo1 + width)
            reals.append((e1, e2))
assert len(reals) == 2, reals
A, B = reals if reals[0][0] == (1, 8) else reals[::-1]
assert A == ((1, 8), (2, 14)) and B == ((1, 13), (7, 14)), reals
mirror = tuple(sorted([tuple(sorted((15 - x, 15 - y))) for x, y in A]))
assert mirror == tuple(sorted(B)), (mirror, B)
print("CHECK A ok: exactly 2 realizations, A=(1,8)+(2,14), B = rho(A)")
CHECK -->

<!-- CHECK
# CHECK B - third-foot menus by partial-graph C4/C8 test: w1 in {4,5,9,12,13},
# w2 in {3,6,7,9,10,13}; L1 then kills 13 (w1) and 7,9 (w2).
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(1, W1), (8, W1), (2, W2), (14, W2)]
def has48(edges, nv):
    adj = [[] for _ in range(nv)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    for s in range(nv):
        stack = [(s, 1 << s, 1)]
        while stack:
            x, mask, L = stack.pop()
            for w in adj[x]:
                if w == s and L in (4, 8):
                    return True
                if w <= s or (mask >> w) & 1 or L >= 8:
                    continue
                stack.append((w, mask | (1 << w), L + 1))
    return False
free = [3, 4, 5, 6, 7, 9, 10, 11, 12, 13]
m1 = [p for p in free if not has48(BASE + [(p, W1)], 21)]
m2 = [q for q in free if not has48(BASE + [(q, W2)], 21)]
assert m1 == [4, 5, 9, 12, 13], m1
assert m2 == [3, 6, 10, 13], m2
# L1 tier for w1: gap-5 same-vertex pair (shortening-3 s=2 ear) kills 13
l1_1 = [p for p in m1 if 5 not in (abs(p - 1), abs(p - 8))]
assert l1_1 == [4, 5, 9, 12], l1_1
# w2's menu needs NO L1 tier: 5, 7, 9, 11 all die to pure cross-C8
for q in (5, 7, 9, 11):
    assert has48(BASE + [(q, W2)], 21), q
print("CHECK B ok: menus {4,5,9,12}(w1, L1 tier) / {3,6,10,13}(w2, pure C8)")
CHECK -->

<!-- CHECK
# CHECK C - compatible-pair law: exactly 10 of the 16 menu pairs die in the
# partial graph; the 6 survivors are (4,13),(5,3),(5,10),(5,13),(9,3),(9,13).
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(1, W1), (8, W1), (2, W2), (14, W2)]
def has48(edges, nv):
    adj = [[] for _ in range(nv)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    for s in range(nv):
        stack = [(s, 1 << s, 1)]
        while stack:
            x, mask, L = stack.pop()
            for w in adj[x]:
                if w == s and L in (4, 8):
                    return True
                if w <= s or (mask >> w) & 1 or L >= 8:
                    continue
                stack.append((w, mask | (1 << w), L + 1))
    return False
dead = []
alive = []
for p in [4, 5, 9, 12]:
    for q in [3, 6, 10, 13]:
        (dead if has48(BASE + [(p, W1), (q, W2)], 21) else alive).append((p, q))
assert sorted(dead) == [(4, 3), (4, 6), (4, 10), (5, 6), (9, 6), (9, 10),
                        (12, 3), (12, 6), (12, 10), (12, 13)], dead
assert sorted(alive) == [(4, 13), (5, 3), (5, 10), (5, 13), (9, 3), (9, 13)], alive
print("CHECK C ok: 10 cross-C8 pair kills, 6 of 16 pairs survive; p=12 fully dead")
CHECK -->

<!-- CHECK
# CHECK D - n=24 exclusion, UNCONDITIONAL: exhaustive completion enumeration
# of realization A at n=24; 173,090 assignments reach the full-graph test,
# ZERO are cubic+connected+{C4,C8}-free. No L1/L2 hypothesis used.
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
XS = [21, 22, 23]; N = 24
OUT = [W1, W2] + XS
POS = [3, 4, 5, 6, 7, 9, 10, 11, 12, 13]
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(1, W1), (8, W1), (2, W2), (14, W2)]
def has48(adj):
    for s in range(N):
        stack = [(s, 1 << s, 1)]
        while stack:
            x, mask, L = stack.pop()
            for w in adj[x]:
                if w == s and L in (4, 8):
                    return True
                if w <= s or (mask >> w) & 1 or L >= 8:
                    continue
                stack.append((w, mask | (1 << w), L + 1))
    return False
def connected(adj):
    seen = {0}; st = [0]
    while st:
        v = st.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); st.append(w)
    return len(seen) == N
tried = [0]; found = [0]
def full_check(extra):
    adj = [[] for _ in range(N)]
    for a, b in BASE + extra:
        adj[a].append(b); adj[b].append(a)
    if any(len(set(a)) != len(a) for a in adj):
        return
    if any(len(a) != 3 for a in adj):
        return
    tried[0] += 1
    if connected(adj) and not has48(adj):
        found[0] += 1
BADGAP = {2, 6, 10}
PINNED = {W1: [1, 8], W2: [2, 14]}
def close(pa, s1, s2):
    extra = list(pa.items())
    deg = {t: 0 for t in OUT}
    for p, c in pa.items():
        if c in deg:
            deg[c] += 1
    cap = {W1: 1, W2: 1, 21: 3, 22: 3, 23: 3}
    free = {t: cap[t] - deg[t] for t in OUT}
    if any(f < 0 for f in free.values()):
        return
    for zv in OUT:
        if free[zv] <= 0:
            continue
        free[zv] -= 1
        opts = []
        if s1 is None and s2 is None:
            opts.append(('uu',))
            for z1 in OUT:
                for z2 in OUT:
                    opts.append(('oo', z1, z2))
        elif s1 is None:
            opts += [('o1', z) for z in OUT]
        elif s2 is None:
            opts += [('o2', z) for z in OUT]
        else:
            opts.append(('none',))
        for uo in opts:
            f2 = dict(free); ue = []; ok = True
            if uo[0] == 'uu':
                ue.append((U1, U2))
            elif uo[0] == 'oo':
                for z, u in ((uo[1], U1), (uo[2], U2)):
                    if f2[z] <= 0:
                        ok = False; break
                    f2[z] -= 1; ue.append((u, z))
            elif uo[0] in ('o1', 'o2'):
                z = uo[1]; u = U1 if uo[0] == 'o1' else U2
                if f2[z] <= 0:
                    ok = False
                else:
                    f2[z] -= 1; ue.append((u, z))
            if not ok or sum(f2.values()) % 2:
                continue
            def oo(rc, acc):
                verts = [t for t in OUT if rc[t] > 0]
                if not verts:
                    full_check(extra + [(V, zv)] + ue + acc)
                    return
                a = verts[0]
                rc[a] -= 1
                for b in OUT:
                    if b == a or rc[b] <= 0 or (a, b) in acc or (b, a) in acc:
                        continue
                    rc[b] -= 1
                    oo(rc, acc + [(a, b)])
                    rc[b] += 1
                rc[a] += 1
            oo(dict(f2), [])
        free[zv] += 1
def assign(i, pa, s1, s2):
    if i == len(POS):
        close(pa, s1, s2)
        return
    p = POS[i]
    opts = []
    if s1 is None:
        opts.append('u1')
    if s2 is None:
        opts.append('u2')
    opts += [W1, W2]
    empty_seen = False
    for x in XS:
        if any(c == x for c in pa.values()):
            opts.append(x)
        elif not empty_seen:
            opts.append(x); empty_seen = True
    for c in opts:
        if c == 'u1':
            assign(i + 1, {**pa, p: U1}, 'f', s2); continue
        if c == 'u2':
            assign(i + 1, {**pa, p: U2}, s1, 'f'); continue
        feet = PINNED.get(c, []) + [q for q, cc in pa.items() if cc == c]
        if len(feet) >= 3:
            continue
        if any(abs(p - q) in BADGAP for q in feet):
            continue
        assign(i + 1, {**pa, p: c}, s1, s2)
assign(0, {}, None, None)
assert tried[0] == 173090, tried[0]
assert found[0] == 0, found[0]
print("CHECK D ok: n=24 exhaustive - 173,090 completions, 0 legal: {7,12} dead")
CHECK -->
