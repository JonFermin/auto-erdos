---
id: pastePO2_tree_universal
status: disproved
depends_on: [triple_alive_universal, pasting_vertex_automatic, paste8_projected_coords]
discharged_by_round: 47
introduced_at_round: 47
---

# Lemma `pastePO2_tree_universal` (DISPROVED at introduction, R47 — falsified by its designated SA falsifier BEFORE the lemma was committed)

**Claim (as it would have been).** Every pair-residual normal spanning
tree of a connected cubic graph admits a pair of back edges (ANY class
— same-branch or branched) with single-cycle sym-diff $D$ and a third
back edge whose cycle meets $D$ in a single arc, with
$$L \;=\; |D| + |C_3| - 2\,|D \cap C_3| \;\in\; \{4, 8, 16, 32\}.$$
Equivalently $V(T) \cap \{4, 8, 16, 32\} \ne \emptyset$. This was the
last surviving successor candidate above `triple_alive_universal`
after the R46 complementary-falsifier pinch, satisfied by both R46
falsifiers (`sb_falsifier_n18` at $L = 16$ via 8 chain configs,
`po2_falsifier_n18` at $L = 8$ via 2 branched configs).

**DISPROOF (R47, session s_0818-081353-a397 — per Q76's mandatory
SA-first discipline, the designated falsifier ran BEFORE
introduction).** SA over (cubic graph, root, normal DFS tree) states,
energy $=$ (residuality violations, \#single-arc PO2 pasting configs
over all pairs with single-cycle $D$), sanity-locked against the full
R46 pin corpus. Result: five distinct pair-residual $n = 18$ trees
with **zero** single-arc PO2 pasting configs — because they have zero
PO2 firing triples of ANY kind (single-arc pasting configs fire by
`pasting_vertex_automatic`, so triple-dead $\Rightarrow$ config-free).
The falsifiers kill `triple_alive_universal` itself (see that lemma's
R47 disproof section and CHECK 3, which pins two of them); this lemma
dies a fortiori, and the whole depth-$\le 3$ certificate layer
terminates with it.

The CHECK below verifies the a-fortiori step concretely on the primary
pinned falsifier: exhaustively, no (pair, third-edge) single-arc
config attains a PO2 length (the direct falsification of THIS claim,
not routed through the triple statement).

<!-- CHECK
# pastePO2_tree_universal CHECK 1 (deterministic pin, the DISPROOF):
# ta_falsifier_warm_n18 is pair-residual yet admits NO single-arc
# pasting config of any pair class with L in {4, 8, 16, 32} —
# exhaustive over all pairs with single-cycle D and all third edges.
PO2_LENS = {4, 8, 16, 32}

def single_cycle_len(sym):
    if not sym: return None
    dg = {}
    for u, v in sym: dg[u] = dg.get(u, 0) + 1; dg[v] = dg.get(v, 0) + 1
    if any(d != 2 for d in dg.values()): return None
    adjS = {}
    for u, v in sym:
        adjS.setdefault(u, []).append(v); adjS.setdefault(v, []).append(u)
    st = next(iter(dg)); seen = {st}; stk = [st]
    while stk:
        u = stk.pop()
        for w in adjS[u]:
            if w not in seen: seen.add(w); stk.append(w)
    return len(sym) if len(seen) == len(dg) else None

def n_arcs(es):
    if not es: return 0
    adjP = {}
    for u, v in es:
        adjP.setdefault(u, []).append(v); adjP.setdefault(v, []).append(u)
    seen = set(); comps = 0
    for s in list(adjP):
        if s in seen: continue
        comps += 1; seen.add(s); stk = [s]
        while stk:
            u = stk.pop()
            for w in adjP[u]:
                if w not in seen: seen.add(w); stk.append(w)
    return comps

nn = 18
edges = [(0, 7), (0, 9), (0, 16), (1, 2), (1, 15), (1, 17), (2, 8), (2, 13),
         (3, 12), (3, 13), (3, 14), (4, 5), (4, 11), (4, 15), (5, 7), (5, 10),
         (6, 9), (6, 10), (6, 11), (7, 16), (8, 11), (8, 12), (9, 10),
         (12, 17), (13, 14), (14, 16), (15, 17)]
root = 17
par = [7, 17, 13, 12, 15, 4, 9, 16, 11, 10, 5, 6, 8, 3, 13, 1, 14, -1]

edges = [tuple(sorted(e)) for e in edges]
depth = [-1] * nn; depth[root] = 0
pending = [v for v in range(nn) if v != root]
while pending:
    nxt = []
    for v in pending:
        if depth[par[v]] >= 0: depth[v] = depth[par[v]] + 1
        else: nxt.append(v)
    assert len(nxt) < len(pending)
    pending = nxt
tre = {(min(v, par[v]), max(v, par[v])) for v in range(nn) if v != root}

def is_anc(u, v):
    if depth[u] > depth[v]: return False
    x = v
    while depth[x] > depth[u]: x = par[x]
    return x == u

fc = []; pe = []
for e in edges:
    if e in tre: continue
    u, v = e
    a, b = (u, v) if depth[u] <= depth[v] else (v, u)
    assert is_anc(a, b), f"non-ancestral back edge {e}"
    es = set(); x = b
    while x != a:
        p = par[x]; es.add((min(x, p), max(x, p))); x = p
    path = set(es)
    es.add(e)
    fc.append(es); pe.append(path)
m = len(fc)
assert m == 10

assert all(len(c) not in PO2_LENS for c in fc), "fund cycle fires"
pair_single = {}
for i in range(m):
    for j in range(i + 1, m):
        D = fc[i] ^ fc[j]
        L = single_cycle_len(D)
        assert L not in PO2_LENS, f"pair ({i},{j}) fires"
        if L is not None:
            pair_single[(i, j)] = D

n_pairs = len(pair_single)
n_configs = 0
for (i, j), D in pair_single.items():
    for z in range(m):
        if z == i or z == j: continue
        arc = D & pe[z]
        if not arc or n_arcs(arc) != 1: continue
        L = len(D) + len(pe[z]) + 1 - 2 * len(arc)
        n_configs += 1
        assert L not in PO2_LENS, \
            f"pasting config pair=({i},{j}) z={z} fires at L={L}"

assert n_pairs >= 5, f"only {n_pairs} single-cycle pairs — probe near-vacuous"
assert n_configs >= 20, f"only {n_configs} single-arc configs examined"
print(f"pastePO2_tree_universal DISPROVED: ta_falsifier_warm_n18 is "
      f"pair-residual with {n_pairs} single-cycle pairs and "
      f"{n_configs} single-arc pasting configs, NONE at a PO2 length")
CHECK -->

## Summary

The R46 pinch's last surviving successor candidate, killed by its own
designated SA falsifier before a single analytic round was spent on it
— the SA-first standing policy working exactly as intended. The
falsifier class (five distinct $n = 18$ pair-residual trees with no
PO2 firing triple at all) simultaneously disproves
`triple_alive_universal`; this file exists to pin the DIRECT
falsification of the pasting-config form (exhaustive over all
single-arc configs of all pair classes) independently of the triple
framing. Successor question: Q77 (depth escalation).
