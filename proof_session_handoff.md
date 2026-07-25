# Session handoff (session s_0725-091155-f9f5)

**Stop reason**: token budget low

**Current focus**: Q9 DFS depth-chain discharging — chain_locality sub-argument.

## Progress this session (rounds 1–5, all keep_progress)

### Round 1: chain_locality CHECK initial
- Created `lemma_chain_locality.md` with CHECK covering:
  - n≤6: exhaustively all labeled connected min-deg-3 graphs
  - n=7..10: named/structured spot-checks (K4, K5, Prism, K33, Wagner, Cube, Petersen)
- CHECK passed: 0 BLOCKING, 0 WARN.

### Round 2: Extended n=7 ne=11 exhaustive (5670 graphs)
- Extended chain_locality CHECK to n=7, ne=11 (minimum-edge, sparsest, hardest case).
- All 5670 graphs pass chain_locality.
- Added pair-gap symmetry analysis to proof_strategy.

### Round 3: chain_locality_girth4 proved analytically
- Created `lemma_chain_locality_girth4.md` (status: proved).
- Analytic proof for girth≤4 sub-cases:
  - 3 tree edges of C4 in DFS tree → back edge has depth-gap 3 → fundamental C4 (=2²). ✓
  - 2 tree edges with adjacent non-tree edges sharing vertex v → sym-diff length = dep[u2]-dep[u1]+2 = 4. ✓
  - Remaining sub-cases: computationally discharged.
- **Key result**: any EG counterexample must have girth≥5.

### Round 4: chain_locality_girth5 — delta_1 >= 8 constraint
- Created `lemma_chain_locality_girth5.md` (status: open).
- Proved analytically: in a girth-5 EG counterexample, every DFS leaf with 2 back edges has δ₁ ≥ 8:
  - girth≥5 → δ₂ ≥ 4
  - sym-diff cycle length = δ₁-δ₂+2 ≥ girth=5 → δ₁-δ₂ ≥ 3 → δ₁ ≥ 7
  - δ₁=7 → fundamental C₈=2³ → contradicts counterexample assumption
  - Therefore δ₁ ≥ 8.
- CHECK: GP(n,k) family up to n=30 vertices (GP(15,k) for k=2,4,7).

### Round 5: Extended girth-5 CHECK + numerical validation
- Extended GP sweep to n=50 vertices (GP(25,k) for k=2,11,12).
- Added `verify_delta1_bound` assertion: δ₁ ≥ 7 for every leaf at every DFS root/ordering.
- Numerical data: δ₁=7 occurs frequently (→ C₈ trivially). δ₁=8 also occurs (harder case).
- Noted: I-graph lemma already proves C4-or-C8 for ALL GP(n,k) analytically; GP sweep is redundant but provides DFS-tree structural data.

## Files modified this session

- `proof_strategy.md` — Sections 6 and 5 updated extensively with Q9 analysis
- `proof_lemmas/lemma_chain_locality.md` — Created (round 1), extended (round 2)
- `proof_lemmas/lemma_chain_locality_girth4.md` — Created (round 3), status: proved
- `proof_lemmas/lemma_chain_locality_girth5.md` — Created (round 4), extended (round 5)
- `proof_open_questions.jsonl` — Q9 claimed and released
- `proof_journal.jsonl` — 5 round events

## What's PROVED so far (chain_locality analysis)

1. girth≤4 → C4 exists → chain_locality holds for ALL DFS trees (Lemma `chain_locality_girth4`).
2. girth≥5 EG counterexample → every DFS leaf has δ₁ ≥ 8.
3. Computationally: chain_locality holds for all min-deg-3 graphs on n≤7 (exhaustive at ne=11) and n≤10 spot-checks.

## Key remaining gap

**girth-5 global argument**: Prove that in a girth-5 min-degree-3 graph where every DFS leaf has δ₁ ≥ 8, chain_locality still holds (there's a power-of-2 cycle from CROSS-VERTEX back-edge pairs or non-leaf back edges).

This requires analyzing pairs of fundamental cycles from different vertices, not just within the same leaf. The specific sub-case to attack:
- Non-leaf vertex v (tree-degree 2) has 1 back edge to ancestor u, depth-gap ∈ {4,5,6,8,...} (not 7,15,...).
- Combine v's back edge fundamental cycle with a leaf's back edge fundamental cycle.
- When does their symmetric difference give a power-of-2 cycle?

## Suggested next move

1. Read `proof_lemmas/lemma_chain_locality_girth5.md` — Current obstacle section.
2. Focus: prove that in any girth-5 cubic graph with ≥10 vertices, some pair of fundamental cycles (possibly from different vertices) gives a power-of-2 sym-diff cycle. This would close chain_locality for girth-5.
3. Alternatively: try the cubic girth-5 case analytically using the I-graph structure (GP=I-graph, already proved C4-or-C8 by igraph lemma).
4. If the analytic proof for general girth-5 is too hard, extend the computational CHECK to n=8 cubic graphs exhaustively (there are ≤5 connected cubic graphs on 8 vertices, but all have girth≤4 by Moore bound, so the girth-5 case for n<10 is vacuous).

## qid status

- Q9: released (partial progress, girth-5 gap remains open)
- Q10, Q11: not yet started (see proof_open_questions.jsonl)
