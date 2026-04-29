# Summary: apr28-n7

## TRIALS RUN: 20

## BEST SCORE: 180, valid=yes

## BEAT BASELINE (236): no

## HYPOTHESES TRIED

- Seed run: randomized greedy baseline (score: 133)
- Best-of-50 random greedy restarts (score: 145)
- Simulated annealing with remove-1 add-N swap moves (score: 144)
- Tabu search: remove-1, greedy-rebuild with tabu list preventing cycling (score: 166)
- Product construction F_3^3 cap × F_3^4 cap to give F_3^7 cap (score: 162)
- Numpy-vectorized local search with precomputed AP-completor matrix (score: 165)
- Two-slice doubling: C×{0} ∪ D×{1} in F_3^7 plus greedy level-2 extension (score: 152)
- Large Neighborhood Search (LNS): remove-8 points, rebuild greedy (score: 162)
- Intensive F_3^6 LNS with tabu, then two-slice doubling to F_3^7 (score: 161)
- Seed with {0,1}^7 (provably cap-free, 128 points) then greedy extension (score: 128)
- Simulated annealing in F_3^6 with temperature schedule, then two-slice lift (score: 166)
- Incremental conflict-count LNS in F_3^7 with precomputed numpy AP-completor matrix (score: 178) — BEST
- Incremental CC-based LNS in F_3^6 then two-slice doubling to F_3^7 (score: 166)
- Adaptive-K LNS with numpy-vectorized CC updates (invalid — CC-update bug) (score: 0)
- Adaptive-K LNS with correct incremental CC tracking (score: 156)
- 5 independent restarts of K=5 CC-LNS in F_3^7, keeping global best (score: 180) — BEST TIED
- Population-intersection seeding: combine top-3 CC-LNS solutions, then LNS (score: 180)
- Numpy-vectorized min-conflict targeted K=3 removal LNS (score: 180)
- Random coset partitioning as structured seed for CC-LNS (score: 178)
- GRASP: min-blocking greedy construction with RCL randomization plus LNS polish (score: 176)

## WHAT WAS LEARNED

The incremental conflict-count (CC) family of algorithms (trials 11, 15-19) was clearly the strongest, with a ceiling around 178-180. These approaches precompute the AP-completion matrix and maintain cc[k] = number of pairs in the current cap whose completion would place point k, enabling O(|cap|) swap operations rather than O(|cap|^2) naive reverification. Simpler search families (random greedy restarts, tabu, LNS without CC) plateaued around 133-166.

The 180-point ceiling is a real local-optima barrier for all search-based approaches: multiple different perturbation strategies (random K=5 removal, min-conflict targeted removal, coset-guided seeding, population intersection, GRASP) all converge to the same ~180-point basin. This suggests 180 is a structural property of the local-optima landscape for this problem.

The Edel 236-cap in F_3^7 is an algebraic construction derived from the 112-cap in F_3^6 (Hill cap) via the affine cap doubling lemma. The gap of 56 points between 180 (search ceiling) and 236 (literature bound) is too large to bridge with pure local search in a 5-minute budget — it requires explicit reconstruction of the Hill cap, which is a specific mathematical object not discoverable by greedy-based methods.
