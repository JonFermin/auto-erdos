# Session handoff (session s_0724-080703-5c51)

**Stop reason**: token budget low (approaching limit after 8 productive rounds)

**PROOF_TAG**: erdos_gyarfas  
**Branch**: erdos-proof/0724-080701-4f9d  
**Critics mode**: AUTOERDOS_PROOF_CRITICS=0 (sandbox bug still unfixed — always run critics-off)

## What was accomplished this session (R1–R8)

### Proved lemmas (new this session)
- **`lemma_same_leaf_sym_diff`** (R2): same-leaf sym-diff length = (d2-d1)+2. Status: proved.
- **`lemma_sym_diff_nested`** (R5-R6): unified sym-diff theorem — for any two same-branch back edges (nested or crossing), sym-diff length = (δ1-δ2)+2. Different-branch = never simple cycle. Status: proved. CHECK: 2865 nested + 1246 crossing configs.
- **`lemma_backedge_density` Parts A+B** (R7): back-edge count ≥ floor(n/2)+1 (proved); DFS leaves forced ≥2 back edges → same-branch pairs (proved). CHECK: exhaustive n≤6 min-deg-3 graphs.

### Empirical/check coverage (new this session)
- **`lemma_dfs_chain_locality`**: 1885 exhaustive n≤6 + Cube/Wagner/Petersen/Franklin(n=12)/Heawood(n=14)/GP(5,1)(n=10) all PASS.
- **Petersen mechanism** (R3): all 10 DFS roots have fundamental C8. No sym-diff needed.
- **n=7 stride-5 sample** (R4): ~47,000 graphs, 0 failures.
- **Girth-6 mechanism** (R4): Franklin/Heawood pass via sym-diff (no fundamental C4/C8).
- **Gap-pair density** (R8): 510/741 = 68.8% of pairs (δ≤40) are valid. Arithmetic alone insufficient.

### Open
- **`lemma_dfs_chain_locality`**: still status:open (only small-n verified; no proof for all n).
- **`lemma_backedge_density` Part C**: the structural forcing argument — showing min-degree-3 DFS structure forces a violation of the gap-pair constraint system — is the key gap.

## Current open questions queue (Q9 is the focus)

**Q9** is CLAIMED by this session. Key sub-problems:
1. **Part C** of `lemma_backedge_density`: structural forcing. This is the essential next step.
2. **Exhaustive n=7**: 236,926 graphs. Doable in ~5-10 minutes (stride-5 took ~6s for 47k; exhaustive ≈ 5×).
3. **n≥8 exhaustive or dense sample**: named graphs at n=8 (all 5 cubic graphs) and n=9 could increase confidence.

## Files modified this session
- `proof_strategy.md`: Sections 5-6 substantially extended (Q8 resolution, Q9 approach, all R1-R8 findings)
- `proof_lemmas/lemma_dfs_chain_locality.md`: major CHECK extension (Petersen mechanism, Franklin, Heawood, GP(5,1), n=7 stride-5)
- `proof_lemmas/lemma_same_leaf_sym_diff.md`: created (R2)
- `proof_lemmas/lemma_sym_diff_nested.md`: created (R5-R6, unified theorem)
- `proof_lemmas/lemma_backedge_density.md`: created (R7-R8, Parts A+B+D)

## Suggested next move

1. Read `proof_lemmas/lemma_backedge_density.md` Parts A-D carefully.
2. For Part C: attempt to show that for a DFS tree of a min-degree-3 graph, the set of depth-gaps at all leaves cannot ALL be from valid pairs. Key tools:
   - Min-degree-3 means every vertex has ≥3 neighbors; every DFS leaf has ≥2 back edges.
   - In a path-structured DFS tree (worst case for counterexample), back edges must "skip" forbidden depths.
   - The forbidden set at depth-gaps {3,7,15,31} and differences {2,6,14,30} creates a 2D constraint.
   - If two leaves are at different depths, their gap constraints interact — maybe forcing overlap.
3. Alternative: try an ILP/enumeration to find a DFS tree configuration consistent with Part C's constraints on ≤20 vertices. If no configuration exists → Part C might be provable.
4. If Part C proves too hard for the current approach, consider abandoning Q9 in favor of:
   - The "girth-biased random cubic graph" counterexample search (next Q10 if opened).
   - Structural arguments for specific subclasses (e.g., planar min-degree-3 graphs).

## Known bugs
- `proof_prepare._sandboxed_eval` allowlist is broken (frozenset, sorted, etc. not in namespace). Workaround: `AUTOERDOS_PROOF_CRITICS=0` always.
