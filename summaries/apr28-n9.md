# Summary: apr28-n9 (cap sets in F_3^9, baseline 1082)

## TRIALS RUN: 20

## BEST SCORE: 800, valid=yes

## BEAT BASELINE (1082): no

## HYPOTHESES TRIED

- **Seed**: Randomized greedy baseline — single pass, score 482
- **Trial 1**: Greedy with 30+ random restarts over 110s budget, keep best — score 491
- **Trial 2**: {0,1}^n binary cap set (2^9=512 pts) greedily extended — score 512, product maximally closed
- **Trial 3**: Product construction F_3^6 × F_3^3 via greedy restarts on each factor — score 702 (78×9)
- **Trial 4**: Local search: remove k pts from greedy cap then re-greedy from remaining — score 515
- **Trial 5**: Hyperplane extension H_0/H_1/H_2 with F_3^8 cap — INVALID (bug: same-vector triple AP)
- **Trial 6**: Fixed hyperplane extension with correct forbidden set for H_2 — score 542
- **Trial 7**: Numpy-accelerated greedy with blocked-set tracking for more restarts — score 493
- **Trial 8**: Triple product C_3 × C_3 × C_3 using exact backtracking 9-pt cap in F_3^3 — score 729
- **Trial 9**: Triple product 729-pt cap extended greedily from complement — score 729, product maximally closed
- **Trial 10**: Remove-k-regreedy local search on F_3^6 then product with exact 9-pt F_3^3 cap — score 747 (83×9)
- **Trial 11**: Aggressive adaptive SA on F_3^6 with restarts, product with 9-pt F_3^3 cap — score 738 (82×9)
- **Trial 12**: Binary {0,1}^8 hyperplane extension — score 512 ({0,1}^8 has 2^8=256 not 512 pts, error in reasoning)
- **Trial 13**: Double product C3×C3 in F_3^6 extended greedily — score 729, double product also maximally closed at 81
- **Trial 14**: Exposure-array local search with numpy (O(k^2) rebuild) — score 490, too slow for n=9
- **Trial 15**: F_3^5 × F_3^4 product using backtracking (cap5=38, cap4=20, product=760) — score 760
- **Trial 16**: Same as trial 15 with 100s time budget for cap5 backtracking — score 760, still 38 (greedy ceiling)
- **Trial 17**: Perturbation of 729-pt triple product with k removals then regreedy — score 729, product basin is deep
- **Trial 19**: Incremental exposure-array local search with numpy — score 569 (exposure undo logic drifts)
- **Trial 20 (Final)**: Least-blocking-first priority greedy on F_3^5 (finds 40-pt cap vs random 38) × exact F_3^4 (20 pts) — score 800 (best result)

## WHAT WAS LEARNED

**Product constructions are the strongest family found**: The F_3^a × F_3^b product of two cap sets in lower dimensions gives a valid cap set in F_3^9, and scored 700–800. However, all product caps tested were **maximally closed** — no point from the complement can be added — meaning the product structure fully saturates the local AP constraints. The best product result was 800 (40×20 from F_3^5 × F_3^4 using priority-based greedy).

**The greedy ceiling is a real and hard constraint**: Both random-order and priority-order greedy algorithms plateau well below the theoretical optima for each sub-dimension: F_3^5 greedy finds ~38-40 (optimum 45), F_3^6 greedy finds ~82-83 (optimum 112). Backtracking cannot escape these local optima within the 5-minute time budget. The Hill cap (112 pts in F_3^6) and Pellegrino cap (45 pts in F_3^5) require algebraic construction rather than search.

**To reach the 1082 Edel bound**, one would need to hardcode the Hill cap in F_3^6 (112 pts) via its known algebraic description (related to the unique ovoid in PG(3,3)), then take the product 112×9=1008, and apply Edel's "extension" method to add the remaining 74 points. This requires specialized combinatorial geometry knowledge beyond what can be derived computationally within the time constraints of this loop.
