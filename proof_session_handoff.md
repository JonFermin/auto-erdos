# Session handoff (session s_0720-080701-9061)

**Stop reason**: logical milestone — 3 keep_progress rounds on Q9; token budget approaching.

**Outcome**: 3 keep_progress records committed on `erdos_gyarfas`:
- `proof_erdos_gyarfas_844f48dd2a77_fbea36c.json` (round 1: lemma introduced, CHECK 1 passes)
- `proof_erdos_gyarfas_883cde623441_78af681.json` (round 2: girth-constraint proved, Petersen adversarial sampling)
- `proof_erdos_gyarfas_16f4acac6c9f_dadbeec.json` (round 3: CHECK 3 KILLS universal claim)

**What was established this session**:
1. **Lemma `dfs_chain_locality`** (status: open, in proof_lemmas/): DFS back-edge
   pairwise gap analysis for Erdős–Gyárfás. Three CHECK blocks:
   - CHECK 1 (passed): all 27 cubic graphs n≤10 have C4/C8 AND SOME DFS detects via gap/gap-diff.
   - CHECK 2 (passed): 3000 adversarial DFS orderings on Petersen graph all detected.
   - CHECK 3 (KEY KILL): 14/27 cubic graphs on n≤10 have DFS orderings that AVOID detection (girth 3 and 4 graphs). **Universal claim ("any DFS tree detects") is FALSE.**

2. **Girth-constraint proved** (proof_strategy.md Section 6): pairwise sym-diff cycle has
   length d2-d1+2 ≥ girth(G). For girth-5 graphs on n≤10, pairwise detection is impossible
   (requires d2≥10); only gap-7 individual detection works.

3. **Petersen graph is robust**: no adversarial ordering (among 3000 tried) avoids detection.
   This aligns with the girth-5 analysis — only gap-7 works, and the Petersen's C8 always
   appears as a fundamental cycle in practice.

4. **Redirect established**: Q9 should pursue "CANONICAL DFS always detects" instead of
   "ANY DFS tree detects." Candidate canonical rule: depth-maximizing DFS (root at min-
   eccentricity vertex, explore neighbors in depth-first order).

**qid state**: Q9 is released (not resolved). Canonical-DFS sub-claim is the next step.
Q10 and Q11 (frankl_union_closed) remain open — consider them if Q9 canonical approach
stalls.

**Harness bug still present**: critic sandbox allowlist excludes frozenset/sorted/bin. All
3 rounds were logged in critics-off mode (deterministic gates only). Bug must be fixed by
human before full-panel runs.

**Suggested next move**:
1. Q9 canonical DFS: write a CHECK that tests whether, for each cubic graph on n≤10,
   the depth-maximizing DFS (start from min-eccentricity vertex, break ties by degree)
   achieves gap-7 detection for girth-5 and gap-3 detection for girth-4. If CHECK passes,
   write the proof argument.
2. If Q9 stalls: take Q10 (frankl_union_closed KL deficiency) — an independent direction
   with a killable first lemma (deficiency lower bound, quantitative).

**Files modified this session**:
- proof_strategy.md (added Section 6 on Q9 progress, girth analysis, CHECK 3 kill)
- proof_lemmas/lemma_dfs_chain_locality.md (new, 3 CHECK blocks, girth analysis, kill doc)
- proof_open_questions.jsonl (claimed then released Q9)
- proof_journal.jsonl (3 round entries)
