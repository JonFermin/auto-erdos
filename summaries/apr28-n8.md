# Summary: apr28-n8

## TRIALS RUN: 20 (including 2 crash trials)

## BEST SCORE: 400, valid=yes

## BEAT BASELINE (496): no

## HYPOTHESES TRIED

- Seed run: randomized greedy baseline (score 258)
- Best-of-50 randomized greedy restarts — averaging over orderings should beat single-pass (score 267)
- Product construction A x A with A the greedy n=4 cap set, plus augmentation (score 256)
- Exact max n4 cap set product giving ~324 after augmentation (score 324)
- Local search swap moves after greedy init — remove one point then re-fill greedily (score 280)
- Product of best-of-many greedy n=6 cap set and n=2 cap set, augmented (score 304)
- Simulated annealing with greedy re-fill steps (score 299)
- Structured orderings (fewest 1s first, coord sum mod 3, many random restarts) (score 270)
- Orbit-based greedy processing entire symmetry orbits at once (score 269)
- Genetic algorithm with crossover (intersection + refill) and mutation (drop + refill) (score 297)
- Targeted swap local search — find blockers for each excluded point, swap one out (score 291)
- GF(3^8) cyclic group construction using irreducible polynomial — CRASH (invalid, duplicate points)
- GF(3^8) with primitive element search and cyclic ordering for greedy (score 267)
- Numpy int-encoded GRASP with SA — CRASH (timed out, SA too slow)
- Numpy precomputed completion pairs fast greedy — CRASH (precomputation too slow)
- Degree-ordered greedy via numpy vectorized AP-triple count (score 270)
- Intensive greedy for max n6 cap set (500 restarts) × n2 cap set, augmented (score 304)
- DFS exact 20-element n4 cap set, product 20x20=400 in F_3^8 (score 400)
- Multiple distinct maximal n4 cap set pairs A x B asymmetric products — all 400, all saturated (score 400)
- DFS for exact n5 cap (4-min budget, reached 42 of 45) × exact n3 cap (9) = 378 (score 378)

## WHAT WAS LEARNED

The greedy approach (in all variants: random restarts, SA, genetic algorithm, orbit-based, degree-ordered) hits a hard ceiling of approximately 260-300 in F_3^8. This is far below the literature bound of 496, confirming that the Edel construction requires fundamentally non-greedy methods. The product construction using exact DFS-found maximal cap sets performed best: the exact 20-element cap set in F_3^4 (found by DFS in ~10 seconds) gave a product of 400, but this structure is provably saturated — no additional points can be added without creating an AP. To reach 496, one would need either the exact 112-element cap set in F_3^6 (which DFS cannot find within the 5-minute budget) or a direct encoding of the Edel construction, which requires access to the specific computer-search output from the 2004 paper that is not reconstructible within the available computational budget.
