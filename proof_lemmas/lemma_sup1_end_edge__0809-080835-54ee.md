---
id: sup1_end_edge
status: open
depends_on: [shortpaste_floor_line, pasting_cover_dichotomy, pasting_vertex_automatic, t3_min_overlap_short_paste]
discharged_by_round: null
introduced_at_round: 31
---

# Lemma `sup1_end_edge` (conjecture + probe: SUP-1 with an end-edge witness, via the min-gap selection rule)

**Setting.** $T$ a pair-residual DFS tree of a connected cubic graph.
For a pair $(B_1, B_2)$ with single-cycle $D = C_1 \triangle C_2$
(overlap $k_{12} \ge 1$), $D$'s tree edges decompose into the segments
$A = [a_{\mathrm{sh}} .. a_{\mathrm{deep}}]$, $L_1 = [m .. s_1]$,
$L_2 = [m .. s_2]$ ($m = \operatorname{lca}(s_1, s_2)$;
`pasting_meeting_structure`). An **end edge** of a segment is an edge
incident to one of its two boundary vertices ($a_{\mathrm{sh}}$ or
$a_{\mathrm{deep}}$ for $A$; $m$ or $s_i$ for $L_i$). A **SUP-1
witness** for the pair is a back edge $B_3$ with
$\operatorname{gap}_3 \le k_{12} + 1$ (short), $D \cap C_3$ a single
edge ($k' = 1$), and $|D| + \operatorname{gap}_3$ odd (so
$L = |D| + \operatorname{gap}_3 - 1$ is even, hence $L \ge 8$ by
`shortpaste_floor_line`(3) whenever $|D| \ge 6$... in fact directly:
$|D|$ odd $\ge 7$ gives $L \ge |D| + 1 \ge 8$; $|D|$ even $\ge 6$ gives
$L \ge |D| + 2 \ge 8$).

**Claim (open, universally quantified — sampling can only falsify).**
Every pair-residual tree $T$ admits a pair with $|D| \ge 6$ and a SUP-1
witness whose met edge is an **end edge** of its segment. Moreover the
witness can be selected by the **min-gap rule**: for some pair
($|D| \ge 6$) and some end edge $e$, the minimum-gap back edge covering
$e$ is itself a SUP-1 witness.

**Consequence.** With `shortpaste_floor_line`(b), the claim closes the
T3 leg of the Q9 tuning program: every pair-residual tree has an even
short-paste value $\ge 8$, i.e. $V_e(T) \not\subseteq \{4, 6\}$ and
$V_e(T) \ne \emptyset$ (`t3_min_overlap_short_paste` discharges modulo
this supply statement).

**Census (R31, three independent seeds, $n \in \{12..24\}$, 480k
sampled DFS trees total, 152 pair-residual).**

- SUP-1 (some pair $|D| \ge 6$ with a $k'=1$ short even-$L$ cover):
  **152/152**. No tree needed the odd-$L$-only fallback (0 occurrences
  of "$k'=1$ short covers exist but never with even $L$").
- End-edge witness: **89/89** (checked on seeds 1 and 3).
- Min-gap selection rule over all end edges: **89/89**.
- **Falsified finer variants** (do NOT chase these): leg-TOP-only
  (met edge incident to $m$) fails 3/63 on seed 2; leg-BOTTOM-only
  (incident to a sender) fails 1/39; $A$-end-only fails 1/39. The
  end-edge disjunction over all six boundary edges is the survivor,
  not any single boundary.
- Witness arithmetic (seed 2, first witness per tree): min gap
  $\operatorname{gap}_3 \in \{2 (33), 4 (21), 5 (4), 9 (2)\}$;
  $|D| \in \{6..13\}$ dominated by odd (7: 26, 9: 20); $k_{12}$ spans
  $2..10$. For leg-top witnesses the cover's anchor $a_3$ lies in the
  cancelled interval $I = [a_{\mathrm{deep}} .. m]$ **60/60**, and
  $s_3 = c_i$ (the child of $m$ on the leg) 47/60.

**Analytic traction (why end edges — partial, not yet proved).** A
short cover pastes (`pasting_cover_dichotomy` c1), so its met set is a
single path inside ONE segment ($\Delta \le 3$:
`pasting_vertex_automatic`). For the leg-top edge $(m, c_i)$: a cover
containing it with $a_3$ a strict ancestor of $a_{\mathrm{deep}}$ would
contain the whole chain $I$ plus $A$'s deepest edge, i.e. straddle,
forcing $\operatorname{gap}_3 \ge k_{12} + 2$ — so every SHORT cover of
the leg-top edge anchors inside $I$ (consistent with the 60/60 census
line). Its $k'$ is the number of $L_i$-edges below $c_i$ on $P_3$;
$s_3$'s chain diverging from $L_i$ immediately below $c_i$ (e.g.
$s_3 = c_i$) gives $k' = 1$ automatically. The remaining analytic
burden: (i) existence of a covering back edge of an end edge that is
short with the right parity — 2-edge-connectedness supplies SOME cover
of every tree edge, but shortness is NOT automatic (90 non-short
$k'=1$ even-$L$ end-edge covers observed on seed 3); (ii) the parity
class $\operatorname{gap}_3 \equiv |D| + 1 \pmod 2$.

**Status.** Open. The CHECK below is the committed dual-attack probe:
an assertion failure exhibits a pair-residual tree where SUP-1, the
end-edge refinement, or the min-gap selection rule fails, each with a
distinct message so the failing layer is identified immediately.

---

<!-- CHECK
# sup1_end_edge: every pair-residual cubic DFS tree admits (1) a pair
# |D|>=6 with a k'=1 short even-L cover (SUP-1); (2) such a witness on
# an END edge of its segment; (3) an end edge whose MIN-GAP cover is
# such a witness.  Three layered asserts, distinct messages.
import random

PO2_LENS = {4, 8, 16, 32}


def sample_cubic(nn, rnd, tries=3000):
    for _ in range(tries):
        stubs = [v for v in range(nn) for _ in range(3)]
        rnd.shuffle(stubs)
        edges = set(); ok = True
        for i in range(0, len(stubs), 2):
            a, b = stubs[i], stubs[i + 1]
            if a == b or (min(a, b), max(a, b)) in edges:
                ok = False; break
            edges.add((min(a, b), max(a, b)))
        if not ok: continue
        el = list(edges)
        deg = [0] * nn
        for a, b in el: deg[a] += 1; deg[b] += 1
        if min(deg) == 3 and max(deg) == 3:
            adj = [[] for _ in range(nn)]
            for a, b in el: adj[a].append(b); adj[b].append(a)
            seen = {0}; stack = [0]
            while stack:
                u = stack.pop()
                for w in adj[u]:
                    if w not in seen: seen.add(w); stack.append(w)
            if len(seen) == nn: return el
    return None


def is_ancestor(u, v, depth, par):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u


def dfs_tree(n, edges, r, shuffled_adj):
    depth = [-1] * n; par = [-1] * n
    depth[r] = 0; visited = [False] * n; visited[r] = True
    stack = [(r, iter(shuffled_adj[r]))]
    while stack:
        u, it = stack[-1]; adv = False
        for w in it:
            if not visited[w]:
                visited[w] = True; depth[w] = depth[u] + 1; par[w] = u
                stack.append((w, iter(shuffled_adj[w]))); adv = True; break
        if not adv: stack.pop()
    tree_mask = 0
    for i, (u, v) in enumerate(edges):
        if depth[u] == depth[v] + 1 and par[u] == v: tree_mask |= 1 << i
        elif depth[v] == depth[u] + 1 and par[v] == u: tree_mask |= 1 << i
    nontree = []
    for i, (u, v) in enumerate(edges):
        if not (tree_mask >> i & 1):
            a, b = (u, v) if depth[u] <= depth[v] else (v, u)
            if not is_ancestor(a, b, depth, par): return None
            nontree.append((b, a, depth[b] - depth[a]))
    return depth, par, nontree


def fund_cycle_edges(sender, ancestor, par):
    path = set(); u = sender
    while u != ancestor:
        p = par[u]; path.add((min(u, p), max(u, p))); u = p
    path.add((min(sender, ancestor), max(sender, ancestor)))
    return path


def single_cycle_len(sym):
    if not sym: return None
    deg = {}
    for u, v in sym: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if any(d != 2 for d in deg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    start = next(iter(deg)); seen = {start}; stk = [start]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(deg) else None


def path_len_of_intersection(cyc1, cyc2):
    es = cyc1 & cyc2
    if not es: return None
    vs1 = {v for e in cyc1 for v in e}
    vs2 = {v for e in cyc2 for v in e}
    shared_v = vs1 & vs2
    deg = {}
    for u, v in es: deg[u] = deg.get(u, 0) + 1; deg[v] = deg.get(v, 0) + 1
    if set(deg) != shared_v: return None
    ends = [v for v, d in deg.items() if d == 1]
    if len(ends) != 2 or any(d > 2 for d in deg.values()): return None
    adjP = {}
    for u, v in es:
        adjP.setdefault(u, []).append(v); adjP.setdefault(v, []).append(u)
    seen = {ends[0]}; stk = [ends[0]]
    while stk:
        u = stk.pop()
        for w in adjP[u]:
            if w not in seen: seen.add(w); stk.append(w)
    if len(seen) != len(deg): return None
    return len(es)


def lca(u, v, depth, par):
    while depth[u] > depth[v]: u = par[u]
    while depth[v] > depth[u]: v = par[v]
    while u != v: u = par[u]; v = par[v]
    return u


def chain_edges(lo, hi, par):
    es = set(); u = lo
    while u != hi:
        p = par[u]; es.add((min(u, p), max(u, p))); u = p
    return es


rng = random.Random(20260809 + 331)
trees_seen = 0
residual = 0
n_end = 0
n_rule = 0

for nn, trials in ((12, 4000), (14, 4000), (16, 4000),
                   (18, 2500), (20, 2500), (22, 2000)):
    rnd = random.Random(rng.randrange(1 << 30))
    for trial in range(trials):
        ed = sample_cubic(nn, rnd)
        if not ed: continue
        edges = [tuple(sorted(e)) for e in ed]
        adj = [[] for _ in range(nn)]
        for u, v in edges: adj[u].append(v); adj[v].append(u)
        for _ in range(8):
            r = rnd.randrange(nn)
            shuffled = [list(adj[v]) for v in range(nn)]
            for v in range(nn): rnd.shuffle(shuffled[v])
            res = dfs_tree(nn, edges, r, shuffled)
            if res is None: continue
            trees_seen += 1
            depth, par, be = res
            m = len(be)
            fc = [fund_cycle_edges(s, a, par) for s, a, _ in be]
            if any(len(c) in PO2_LENS for c in fc): continue
            pair_fires = False
            for i in range(m):
                for j in range(i + 1, m):
                    if single_cycle_len(fc[i] ^ fc[j]) in PO2_LENS:
                        pair_fires = True; break
                if pair_fires: break
            if pair_fires: continue
            residual += 1

            sup1 = False; has_end = False; rule = False
            for x in range(m):
                for y in range(x + 1, m):
                    D = fc[x] ^ fc[y]
                    LD = single_cycle_len(D)
                    if LD is None or LD < 6: continue
                    k12 = (len(fc[x]) + len(fc[y]) - LD) // 2
                    s1, a1, _ = be[x]; s2, a2, _ = be[y]
                    mm = lca(s1, s2, depth, par)
                    a_sh, a_deep = (a1, a2) if depth[a1] <= depth[a2] else (a2, a1)
                    A = chain_edges(a_deep, a_sh, par)
                    L1 = chain_edges(s1, mm, par)
                    L2 = chain_edges(s2, mm, par)
                    ends = set()
                    for seg, bot, top in ((A, a_deep, a_sh), (L1, s1, mm), (L2, s2, mm)):
                        for (u, v) in seg:
                            if bot in (u, v) or top in (u, v): ends.add((u, v))
                    for z in range(m):
                        if z in (x, y): continue
                        kk = path_len_of_intersection(D, fc[z])
                        if kk != 1: continue
                        g3 = len(fc[z]) - 1
                        if g3 > k12 + 1 or (LD + g3) % 2 != 1: continue
                        sup1 = True
                        if next(iter(D & fc[z])) in ends: has_end = True
                    if not rule:
                        for e in ends:
                            covers = [z for z in range(m)
                                      if z not in (x, y) and e in fc[z]]
                            if not covers: continue
                            zc = min(covers, key=lambda z: len(fc[z]))
                            kk = path_len_of_intersection(D, fc[zc])
                            g3 = len(fc[zc]) - 1
                            if kk == 1 and g3 <= k12 + 1 and (LD + g3) % 2 == 1:
                                rule = True; break

            assert sup1, \
                (f"FALSIFIED SUP-1: pair-residual tree with NO pair |D|>=6 "
                 f"admitting a k'=1 short even-L cover "
                 f"(n={nn}, edges={edges}, root={r})")
            assert has_end, \
                (f"FALSIFIED end-edge refinement: SUP-1 holds but no witness "
                 f"met edge is a segment end edge "
                 f"(n={nn}, edges={edges}, root={r})")
            assert rule, \
                (f"FALSIFIED min-gap rule: end-edge witness exists but no end "
                 f"edge's MIN-GAP cover is one "
                 f"(n={nn}, edges={edges}, root={r})")
            if has_end: n_end += 1
            if rule: n_rule += 1

assert trees_seen > 10000, f"too few trees: {trees_seen}"
assert residual >= 20, f"too few residual trees sampled: {residual} — probe vacuous"
print(f"trees={trees_seen} residual={residual} end={n_end} rule={n_rule} "
      f"— every pair-residual tree has a pair |D|>=6 with a k'=1 short "
      f"even-L cover on a segment end edge, selectable by the min-gap rule")
CHECK -->

## Summary

Open computational conjecture with falsification probe, closing the T3
supply gap positionally: every pair-residual cubic DFS tree admits a
pair with $|D| \ge 6$ and a $k' = 1$ short cover of even pasted length
whose met edge is an END edge of its $D$-segment — and the witness is
selectable by taking the minimum-gap cover of the right end edge. R31
census (3 seeds, 480k trees, 152 residuals): SUP-1 152/152, end-edge
refinement 89/89, min-gap rule 89/89; leg-top-only, leg-bottom-only,
and $A$-end-only all falsified (the disjunction over all six boundary
edges is the survivor). Short covers of the leg-top edge provably
anchor inside the cancelled interval (straddle exclusion); observed
60/60. With `shortpaste_floor_line`, this claim discharges
`t3_min_overlap_short_paste` (even $L \ge 8$ supply), leaving SUP-8
(line-hitting, $L = 8$ exactly) as the other half of Q9.
