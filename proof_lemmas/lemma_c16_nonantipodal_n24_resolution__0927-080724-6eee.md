---
id: c16_nonantipodal_n24_resolution
status: proved
depends_on: [c16_712_exclusion, template_placement, c16_d1_ear_cover]
discharged_by_round: null
introduced_at_round: 99
---

# Lemma `c16_nonantipodal_n24_resolution` (proved — the $\{4,9\}$ pair is dead at $n = 24$; the $\{4,7\}$ pair is REALIZED, and its witness W24 REFUTES the antipodal-participation law (a))

**Setting.** As `c16_712_exclusion`: $G$ connected cubic
$\{C_4, C_8\}$-free, $C$ a chordless $16$-cycle, legal $\tau \ge 2$,
$d = 1$ landing, long-arc coordinate $0..15$. This lemma finishes
the non-antipodal half of the s$2$/s$2$ catalog at $n = 24$ by the
pinned-completion-enumeration method of `c16_712_exclusion`,
instance by instance: unlike $\{7,12\}$ (width $13$, fully pinned),
$\{4,7\}$ has width $9$ ($\mathrm{lo}_1 \in [1,5]$) and $\{4,9\}$
width $10$ ($\mathrm{lo}_1 \in [1,4]$), so the decision runs once
per translate, quotiented by the mirror $\rho: j \mapsto 15 - j$.

**Statement.**

- **(a) Instance arithmetic (proved).** Up to $\rho$, $\{4,7\}$
  has exactly $5$ realizations
  ($e_1 = (\mathrm{lo}, \mathrm{lo}{+}4)$,
  $e_2 = (\mathrm{lo}{+}2, \mathrm{lo}{+}9)$ for
  $\mathrm{lo} \in [1,5]$, the $\delta_1 = 7$ family being their
  mirrors), and $\{4,9\}$ exactly $4$
  ($e_1 = (\mathrm{lo}, \mathrm{lo}{+}4)$,
  $e_2 = (\mathrm{lo}{+}1, \mathrm{lo}{+}10)$,
  $\mathrm{lo} \in [1,4]$). (CHECK A.)

- **(b) $\{4,9\}$ exclusion at $n = 24$, UNCONDITIONAL (proved).**
  No connected cubic $\{C_4,C_8\}$-free graph on exactly $24$
  vertices realizes any $\{4,9\}$ instance at a legal $d = 1$
  landing: all four exhaustive completion enumerations are UNSAT
  ($173{,}090 / 179{,}008 / 212{,}532 / 204{,}563$ completions
  reach the full-graph test; zero survive). Together with
  `c16_712_exclusion`(e), TWO of the three non-antipodal catalog
  pairs are outright impossible at $n = 24$, no menu hypothesis
  needed. (CHECKs B1–B4.)

- **(c) $\{4,7\}$ realizability trichotomy at $n = 24$ (proved).**
  The five $\{4,7\}$ instances split: $\mathrm{lo} \in \{3, 5\}$
  (i.e. $e_1 e_2 = (3,7)(5,12)$ and $(5,9)(7,14)$) are UNSAT by
  the same exhaustive enumeration; $\mathrm{lo} \in \{1, 2, 4\}$
  are SAT, each realized by an explicit completion recorded in
  CHECK C. $\{4,7\}$ is the UNIQUE non-antipodal catalog pair
  realizable at $n = 24$ — matching its census signature as the
  "friendly" pair (the only one whose pilot route never fails).

- **(d) The witness W24 and the REFUTATION of the participation
  law (a) (proved).** The $\mathrm{lo} = 4$ completion — call the
  graph **W24**, explicit edge list in CHECK D — is a connected
  cubic $\{C_4, C_8\}$-free graph on $24$ vertices, with $C$
  chordless, a legal $\tau \ge 2$, $d = 1$ landing at feet
  $(15, 0)$, and a menu of $13$ ears that admits NO L1 and NO L2,
  in which the valid s$2$/s$2$ L3 pair
  $\{(4, 8, 2), (6, 13, 2)\}$ has span pair $\{4,7\}$ — no
  antipodal ($\delta = 8$) ear. This REFUTES statement (a) of
  `template_placement` ("every valid s$2$/s$2$ pair in an
  L1&L2-less menu contains a $\delta = 8$ ear; the catalog pairs
  $\{4,7\}, \{4,9\}, \{7,12\}$ never occur there"): $\{4,7\}$
  DOES occur, at $n = 24$, outside every walk stratum the census
  sampled. Statement (b) of `template_placement` SURVIVES in W24:
  the menu's only other valid L3 pair, $\{(5,8,2), (6,14,2)\}$,
  has span pair $\{3,8\}$ — the antipodal TEMPLATE itself — so
  the landing closes through an antipodal pair as (b) predicts.
  The menu's complete valid-L3-pair list is exactly these two.
  (CHECK D.)

- **(e) W24 is a NEW class member (proved).** W24 contains
  exactly $6$ triangles; adj24 has $7$ and spider24 has $3$, so
  W24 is isomorphic to neither — the third known $n = 24$ member
  of the chordless-$C_{16}$ class ($20$th corpus member). Its
  relation to the R96/R97 $k = 1$ classification (which is EXACT
  and two-membered) is a mandatory next question: W24 must sit in
  a $k \ne 1$ branch of the branch-vertex profile taxonomy, or
  expose a gap in it. (CHECK D counts the triangles; the
  profile computation is NOT claimed here.)

**Proof.** (a) is T1 arithmetic as in `c16_712_exclusion`(a),
enumerated in CHECK A. (b), (c): the completion enumeration of
`c16_712_exclusion`(e) run per pinned instance — the counting
skeleton ($|O| = 5$, exact degrees, forced spoke structure,
$v$/$u_1$/$u_2$ wiring, $O$–$O$ closure, mirror quotient and
$x$-label symmetry breaking) is identical, only the four pinned
feet move. Soundness of the early gap pruning ($\{2, 6, 10\}$
same-vertex gaps close a $C_4$/$C_8$ with a $C$-arc present in
every completion) is as proved there; NO L1 pruning is used, so
SAT/UNSAT is unconditional. (d): direct verification on the
explicit W24 — every claim (cubic, connected, no $C_4$/$C_8$ by
exhaustive cycle enumeration to length $8$, chordless $C$, legal
landing, the full $13$-ear menu, L1- and L2-emptiness, the two
valid L3 pairs and their spans) is finitely checkable and checked
(CHECK D); the refuted statement is quantified over exactly this
configuration class, so one legal witness suffices. It was also
re-verified through an independent code path (networkx
`simple_cycles` length-bounded census: cycle spectrum
$\{3{:}6,\ 5{:}2,\ 6{:}4,\ 7{:}2\}$ below length $8$, zero $C_4$,
zero $C_8$; independent `all_simple_paths` ear enumeration agrees
ear-for-ear). (e): triangle counts $6 \ne 7, 3$. $\square$

**Program consequences.**

1. The "attackable structured half" of `template_placement` is
   GONE — proof effort on per-span-pair exclusion of $\{4,7\}$
   would have been spent on a FALSE statement. The
   falsification-first policy paid for itself this round.
2. The live form of the participation law is exactly its (b):
   *some* valid pair containing an antipodal ear exists (W24 is
   consistent with it — and strikingly, W24's antipodal pair is
   the template $\{3,8\}$, extending the template's reach to a
   third graph family).
3. The route-disjunction program (Section 133) is UNAFFECTED in
   its census facts but its eventual target shifts: the $\{4,7\}$
   route analysis is now about a REALIZED configuration, not a
   to-be-excluded one.
4. W24 itself is new corpus material: profile classification
   (vs. R96/R97), its chordless-$C_{16}$ census, and whether its
   landing family generates more counterexamples are all next
   moves.

<!-- CHECK
# CHECK A - instance arithmetic: {4,7} = 10 realizations / 5 up to mirror,
# {4,9} = 8 / 4; explicit position lists.
ALLOWED = [1, 3, 4, 7, 8, 9, 11, 12, 13]
def realizations(spair):
    out = []
    for d1 in ALLOWED:
        for a in range(1, min(6, d1) + 1):
            d2 = d1 + 7 - 2 * a
            if d2 not in ALLOWED or frozenset([d1, d2]) != spair:
                continue
            width = d1 + 7 - a
            for lo1 in range(1, 15 - width):
                out.append(((lo1, lo1 + d1), (lo1 + a, lo1 + width)))
    return out
def mirror(inst):
    m = [tuple(sorted((15 - x, 15 - y))) for x, y in inst]
    m.sort()
    return (m[0], m[1])
def dedupe(insts):
    seen, keep = set(), []
    for i in insts:
        if i in seen or mirror(i) in seen:
            continue
        seen.add(i); keep.append(i)
    return keep
r47 = realizations(frozenset([4, 7])); k47 = dedupe(r47)
r49 = realizations(frozenset([4, 9])); k49 = dedupe(r49)
assert len(r47) == 10 and len(r49) == 8, (len(r47), len(r49))
assert k47 == [((1,5),(3,10)), ((2,6),(4,11)), ((3,7),(5,12)), ((4,8),(6,13)), ((5,9),(7,14))], k47
assert k49 == [((1,5),(2,11)), ((2,6),(3,12)), ((3,7),(4,13)), ((4,8),(5,14))], k49
print("CHECK A ok: {4,7} 10/5 instances, {4,9} 8/4 instances up to mirror")
CHECK -->

<!-- CHECK
# CHECK B1 - {4,9} instance (1,5)+(2,11) at n=24: exhaustive completion
# enumeration, UNSAT (173,090 completions, zero legal).
E1, E2, WANT_TRIED, WANT_FOUND = (1, 5), (2, 11), 173090, 0
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
XS = [21, 22, 23]; N = 24
OUT = [W1, W2] + XS
feet1, feet2 = list(E1), list(E2)
POS = [p for p in range(1, 15) if p not in set(feet1 + feet2)]
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(feet1[0], W1), (feet1[1], W1), (feet2[0], W2), (feet2[1], W2)]
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
PINNED = {W1: feet1, W2: feet2}
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
assert tried[0] == WANT_TRIED, tried[0]
assert found[0] == WANT_FOUND, found[0]
print("CHECK B1 ok: {4,9} instance (1,5)+(2,11) UNSAT (173,090 completions)")
CHECK -->

<!-- CHECK
# CHECK B2 - {4,9} instance (2,6)+(3,12) at n=24: UNSAT (179,008 completions).
E1, E2, WANT_TRIED, WANT_FOUND = (2, 6), (3, 12), 179008, 0
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
XS = [21, 22, 23]; N = 24
OUT = [W1, W2] + XS
feet1, feet2 = list(E1), list(E2)
POS = [p for p in range(1, 15) if p not in set(feet1 + feet2)]
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(feet1[0], W1), (feet1[1], W1), (feet2[0], W2), (feet2[1], W2)]
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
PINNED = {W1: feet1, W2: feet2}
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
assert tried[0] == WANT_TRIED, tried[0]
assert found[0] == WANT_FOUND, found[0]
print("CHECK B2 ok: {4,9} instance (2,6)+(3,12) UNSAT (179,008 completions)")
CHECK -->

<!-- CHECK
# CHECK B3 - {4,9} instance (3,7)+(4,13) at n=24: UNSAT (212,532 completions).
E1, E2, WANT_TRIED, WANT_FOUND = (3, 7), (4, 13), 212532, 0
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
XS = [21, 22, 23]; N = 24
OUT = [W1, W2] + XS
feet1, feet2 = list(E1), list(E2)
POS = [p for p in range(1, 15) if p not in set(feet1 + feet2)]
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(feet1[0], W1), (feet1[1], W1), (feet2[0], W2), (feet2[1], W2)]
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
PINNED = {W1: feet1, W2: feet2}
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
assert tried[0] == WANT_TRIED, tried[0]
assert found[0] == WANT_FOUND, found[0]
print("CHECK B3 ok: {4,9} instance (3,7)+(4,13) UNSAT (212,532 completions)")
CHECK -->

<!-- CHECK
# CHECK B4 - {4,9} instance (4,8)+(5,14) at n=24: UNSAT (204,563 completions).
E1, E2, WANT_TRIED, WANT_FOUND = (4, 8), (5, 14), 204563, 0
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
XS = [21, 22, 23]; N = 24
OUT = [W1, W2] + XS
feet1, feet2 = list(E1), list(E2)
POS = [p for p in range(1, 15) if p not in set(feet1 + feet2)]
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(feet1[0], W1), (feet1[1], W1), (feet2[0], W2), (feet2[1], W2)]
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
PINNED = {W1: feet1, W2: feet2}
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
assert tried[0] == WANT_TRIED, tried[0]
assert found[0] == WANT_FOUND, found[0]
print("CHECK B4 ok: {4,9} instance (4,8)+(5,14) UNSAT (204,563 completions)")
CHECK -->

<!-- CHECK
# CHECK D - W24: full verification of the participation-law counterexample.
# Connected cubic {C4,C8}-free n=24, C chordless, legal d=1 landing, menu
# L1-less AND L2-less, exactly two valid L3 pairs: {4,7} (non-antipodal,
# the refuting pair) and {3,8} (the template — law (b) survives). 6 triangles.
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
N = 24
EDGES = [(0,1),(0,15),(0,18),(1,2),(1,18),(2,3),(2,21),(3,4),(3,21),(4,5),
         (4,19),(5,6),(5,19),(6,7),(6,20),(7,8),(7,16),(8,9),(8,19),(9,10),
         (9,22),(10,11),(10,22),(11,12),(11,23),(12,13),(12,23),(13,14),
         (13,20),(14,15),(14,20),(15,16),(16,17),(17,18),(17,22),(21,23)]
adj = [[] for _ in range(N)]
for a, b in EDGES:
    adj[a].append(b); adj[b].append(a)
assert all(len(set(x)) == len(x) == 3 for x in adj), "not simple cubic"
seen = {0}; st = [0]
while st:
    v = st.pop()
    for w in adj[v]:
        if w not in seen:
            seen.add(w); st.append(w)
assert len(seen) == N, "not connected"
# cycle census to length 8 (start = min vertex)
census = {}
for s in range(N):
    stack = [(s, 1 << s, 1)]
    while stack:
        x, mask, L = stack.pop()
        for w in adj[x]:
            if w == s and L >= 3:
                census[L] = census.get(L, 0) + 1
            if w <= s or (mask >> w) & 1 or L >= 8:
                continue
            stack.append((w, mask | (1 << w), L + 1))
census = {k: v // 2 for k, v in census.items()}   # each cycle counted twice
assert census.get(4, 0) == 0 and census.get(8, 0) == 0, census
assert census.get(3, 0) == 6, census   # 6 triangles: not adj24 (7), not spider24 (3)
# C = 0..15 chordless
for a in range(16):
    for b in adj[a]:
        if b < 16:
            assert min(abs(a - b), 16 - abs(a - b)) == 1, (a, b)
# landing legality: v 0-spoke, u1/u2 T-neighbours, feet 15/0, d=1
assert all(nb >= 16 for nb in adj[V])
assert 15 in adj[U1] and V in adj[U1] and 0 in adj[U2] and V in adj[U2]
# menu of H = G - {u1,v,u2}
banned = {U1, V, U2}
ears = []
for p in range(1, 15):
    for w in adj[p]:
        if w < 16 or w in banned:
            continue
        stack = [(w, [p, w])]
        while stack:
            v, path = stack.pop()
            for u in adj[v]:
                if u in banned or u in path:
                    continue
                if u < 16:
                    if 1 <= u <= 14 and u > p:
                        ears.append((p, u, len(path), tuple(path[1:])))
                    continue
                if len(path) < 12:
                    stack.append((u, path + [u]))
assert len(ears) == 13, len(ears)
assert not any(hi - lo - s == 3 for lo, hi, s, _ in ears), "L1 present"
for A in ears:
    for B in ears:
        if A[1] <= B[0] and not (set(A[3]) & set(B[3])):
            assert (A[1]-A[0]-A[2]) + (B[1]-B[0]-B[2]) != 3, ("L2", A, B)
l3 = []
for A in ears:
    for B in ears:
        if A[0] < B[0] <= A[1] < B[1] and not (set(A[3]) & set(B[3])):
            if (B[1]-A[1]) + (B[0]-A[0]) == A[2] + B[2] + 3:
                l3.append((A[:3], B[:3]))
spans = sorted(frozenset((b[1]-b[0], a[1]-a[0])) for a, b in l3)
assert len(l3) == 2, l3
assert sorted(map(sorted, spans)) == [[3, 8], [4, 7]], spans
print("CHECK D ok: W24 legal, menu L1&L2-less, valid {4,7} pair present ->")
print("  template_placement (a) REFUTED at n=24; (b) survives via the {3,8} template")
CHECK -->

<!-- CHECK
# CHECK C0 - the three SAT {4,7} instances (lo = 1, 2, 4) each have an explicit
# legal completion: connected cubic {C4,C8}-free n=24 realizing the pinned pair.
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
N = 24
WITS = [
    ((1, 5), (3, 10), [(2, 19), (4, 18), (6, 20), (7, 21), (8, 21), (9, 22),
                       (11, 21), (12, 22), (13, 23), (14, 23), (17, 23), (16, 22)]),
    ((2, 6), (4, 11), [(1, 21), (3, 19), (5, 21), (7, 20), (8, 22), (9, 22),
                       (10, 23), (12, 22), (13, 23), (14, 16), (17, 21), (18, 23)]),
    ((4, 8), (6, 13), [(1, 18), (2, 21), (3, 21), (5, 19), (7, 16), (9, 22),
                       (10, 22), (11, 23), (12, 23), (14, 20), (17, 22), (21, 23)]),
]
for e1, e2, extra in WITS:
    edges = [(i, i + 1) for i in range(15)] + [(15, 0)]
    edges += [(15, U1), (U1, V), (V, U2), (U2, 0)]
    edges += [(e1[0], W1), (e1[1], W1), (e2[0], W2), (e2[1], W2)]
    edges += extra
    adj = [[] for _ in range(N)]
    for a, b in edges:
        adj[a].append(b); adj[b].append(a)
    assert all(len(set(x)) == len(x) == 3 for x in adj), (e1, e2)
    seen = {0}; st = [0]
    while st:
        v = st.pop()
        for w in adj[v]:
            if w not in seen:
                seen.add(w); st.append(w)
    assert len(seen) == N, (e1, e2)
    for s in range(N):
        stack = [(s, 1 << s, 1)]
        while stack:
            x, mask, L = stack.pop()
            for w in adj[x]:
                if w == s:
                    assert L not in (4, 8), (e1, e2, "C4/C8")
                if w <= s or (mask >> w) & 1 or L >= 8:
                    continue
                stack.append((w, mask | (1 << w), L + 1))
    for a in range(16):
        for b in adj[a]:
            if b < 16:
                assert min(abs(a - b), 16 - abs(a - b)) == 1, (a, b)
print("CHECK C0 ok: {4,7} lo=1,2,4 witnesses all legal (SAT confirmed)")
CHECK -->

<!-- CHECK
# CHECK C1 - {4,7} instance (3,7)+(5,12) at n=24: UNSAT (212,532 completions).
E1, E2, WANT_TRIED, WANT_FOUND = (3, 7), (5, 12), 212532, 0
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
XS = [21, 22, 23]; N = 24
OUT = [W1, W2] + XS
feet1, feet2 = list(E1), list(E2)
POS = [p for p in range(1, 15) if p not in set(feet1 + feet2)]
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(feet1[0], W1), (feet1[1], W1), (feet2[0], W2), (feet2[1], W2)]
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
PINNED = {W1: feet1, W2: feet2}
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
assert tried[0] == WANT_TRIED, tried[0]
assert found[0] == WANT_FOUND, found[0]
print("CHECK C1 ok")
CHECK -->

<!-- CHECK
# CHECK C2 - {4,7} instance (5,9)+(7,14) at n=24: UNSAT (173,090 completions).
E1, E2, WANT_TRIED, WANT_FOUND = (5, 9), (7, 14), 173090, 0
U1, V, U2, W1, W2 = 16, 17, 18, 19, 20
XS = [21, 22, 23]; N = 24
OUT = [W1, W2] + XS
feet1, feet2 = list(E1), list(E2)
POS = [p for p in range(1, 15) if p not in set(feet1 + feet2)]
BASE = [(i, i + 1) for i in range(15)] + [(15, 0)]
BASE += [(15, U1), (U1, V), (V, U2), (U2, 0)]
BASE += [(feet1[0], W1), (feet1[1], W1), (feet2[0], W2), (feet2[1], W2)]
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
PINNED = {W1: feet1, W2: feet2}
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
assert tried[0] == WANT_TRIED, tried[0]
assert found[0] == WANT_FOUND, found[0]
print("CHECK C2 ok")
CHECK -->
