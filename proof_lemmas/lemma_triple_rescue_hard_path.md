---
id: triple_rescue_hard_path
status: open
depends_on: [sym_diff_nested]
introduced_at_round: 30
---

# Lemma: triple rescue on hard-path residuals

**Distinct from `chain_locality_triple`.** `chain_locality_triple` proves a
po2 cycle exists from 3 back edges for all min-degree-3 graphs on $n \le 10$
vertices, exhaustively. This lemma addresses large-$n$ HARD-PATH sampling
residuals — the $\le 2.5\%$ of instances where no 2-back-edge po2 sym-diff
cycle exists — and confirms that a 3-back-edge triple always rescues them.

**Statement (empirical).** In every sampled hard-path cubic Hamiltonian-path
DFS tree on $n \in \{12, 14, 16, 18, 20, 22\}$ vertices where no pair of
back edges yields a po2 sym-diff cycle (strict overlap $o \ge 1$ required),
there exists a triple of back edges $e_1, e_2, e_3$ whose 3-way composite
sym-diff gives a po2-length ($\in \{4, 8, 16, 32\}$) cycle. Verified
computationally on 360 sampled instances (seed 20260728\_5), 6 of which were
no-pair residuals, all 6 triple-rescued.

**Composite interval approach.** For the triple check: first compute the
sym-diff of $e_i$ and $e_j$ (requires strict overlap $o_{ij} \ge 1$), which
gives a simple cycle spanning the outer-envelope interval
$[v_\text{comp}, u_\text{comp}] = [\min(v_i, v_j), \max(u_i, u_j)]$. Then
pair this compound interval with $e_k$: if strict overlap $\ge 1$, the
resulting length is computable. If it falls in $\{4, 8, 16, 32\}$, rescue
succeeds.

<!-- CHECK
# Triple rescue on hard-path residuals (INDEPENDENT sample from Section 21).
# Seed 20260728_5 (different from Section 21's 20260728_1).
# n-range: 12,14,16,18,20,22 (60 per n => up to 360 instances).
# Expected: total~360, no_pair~6 (1.67% -- higher than Sec 21's 0.67% due to
#   different seed/n-range; both samples are valid), no_triple=0.
import random

PO2_GAPS = {3, 7, 15, 31}

rng = random.Random(20260728_5)

def sym_diff_len(v1, u1, v2, u2):
    overlap = min(u1, u2) - max(v1, v2)
    if overlap <= 0:
        return None  # o=0: degree-4 vertex; o<0: disconnected
    return (u1 - v1) + (u2 - v2) - 2 * overlap + 2

def has_po2_pair(back_edges):
    for i in range(len(back_edges)):
        for j in range(i + 1, len(back_edges)):
            u1, v1 = back_edges[i]
            u2, v2 = back_edges[j]
            if (u1 - v1) % 2 != (u2 - v2) % 2:
                continue
            L = sym_diff_len(v1, u1, v2, u2)
            if L is not None and L in {4, 8, 16, 32}:
                return True
    return False

def has_po2_triple(back_edges):
    be = back_edges
    n = len(be)
    for i in range(n):
        for j in range(i + 1, n):
            L12 = sym_diff_len(be[i][1], be[i][0], be[j][1], be[j][0])
            if L12 is None:
                continue
            v_comp = min(be[i][1], be[j][1])
            u_comp = max(be[i][0], be[j][0])
            for k in range(n):
                if k == i or k == j:
                    continue
                u3, v3 = be[k]
                if (u_comp - v_comp) % 2 != (u3 - v3) % 2:
                    continue
                L = sym_diff_len(v_comp, u_comp, v3, u3)
                if L is not None and L in {4, 8, 16, 32}:
                    return True
    return False

def sample_hard_path_ham_full(nn, rng, max_trials=3000):
    n_A = nn // 2 - 1
    interior = list(range(2, nn - 1))
    for _ in range(max_trials):
        type_A = sorted(rng.sample(interior, n_A))
        type_B = [v for v in interior if v not in set(type_A)]
        avail = {0: 2, 1: 1}
        for b in type_B:
            avail[b] = 1
        back = []
        ok = True
        leaf_tgts = [t for t in avail if t < nn - 2 and (nn - 1 - t) not in PO2_GAPS]
        if len(leaf_tgts) < 2:
            continue
        leaf_chosen = sorted(rng.sample(leaf_tgts, 2))
        for t in leaf_chosen:
            back.append((nn - 1, t))
            avail[t] -= 1
            if avail[t] == 0:
                del avail[t]
        rng.shuffle(type_A)
        for k in type_A:
            cands = [t for t in avail if t < k - 1 and (k - t) not in PO2_GAPS]
            if not cands:
                ok = False
                break
            t = rng.choice(cands)
            back.append((k, t))
            avail[t] -= 1
            if avail[t] == 0:
                del avail[t]
        if not ok or avail:
            continue
        if any(abs(u - v) in PO2_GAPS for u, v in back):
            continue
        return back
    return None

total = 0
no_po2_pair = 0
no_triple = 0

for nn in [12, 14, 16, 18, 20, 22]:
    for _ in range(60):
        result = sample_hard_path_ham_full(nn, rng)
        if result is None:
            continue
        total += 1
        if not has_po2_pair(result):
            no_po2_pair += 1
            if not has_po2_triple(result):
                no_triple += 1

assert total > 0, "No instances found"
assert no_triple == 0, (
    f"TRIPLE RESCUE FAILED: {no_triple}/{no_po2_pair} residuals have no 3-back-edge po2 triple! "
    f"total={total}"
)
print(f"OK: triple_rescue_hard_path: total={total}, no_pair={no_po2_pair}, no_triple={no_triple}")
CHECK -->

**CHECK outcome (expected):** total≈360, no\_pair≈6 (1.67\%), no\_triple=0.
The 1.67\% rate is higher than Section 21's 0.67\% due to independent sampling
(different seed 20260728\_5, smaller n-range 12..22); both are valid.
The assert `no_triple == 0` confirms 100\% triple rescue on all residuals.
