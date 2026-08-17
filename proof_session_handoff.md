# Session handoff (session s_0817-081104-2f11)

**Stop reason**: Logical milestone (R46 logged — the densest round of
the branch) + context budget.

**What happened this session (R46, one round, five commits)**:

1. **`paste8_projected_coords` PROVED** — the same-branch paste
   predicate is pure interval arithmetic in projected coordinates on
   one root chain: arc $= \pi(B_3) \cap$ side, $\pi = [d(a_3),
   d(\mathrm{lca}(s_3, s_d))]$, off-chain tail = nonnegative slack
   weight. CHECK: 5,514 covers on 9 pins, 0 exceptions. This lemma is
   length-agnostic and SURVIVES everything below.
2. **The census→SA killing field (4 kills in one round)**:
   `slack_ladder_above5` (introduced + disproved same round,
   `ladder_gap9_n14`), then the big one — **`sb_falsifier_n18`**
   (cold SA, wide class): pair-residual, $V(T)$ holed EXACTLY at 8,
   rescued only by chain pastes at $L = 16$. Kills
   `paste8_samebranch_universal`, `paste8_tree_universal`,
   `sup8_tree_universal`, `pasting_value_interval` in one tree.
   Then **`po2_falsifier_n18`**: no same-branch paste at ANY PO2
   slack, rescued only by BRANCHED paste at $L = 8$ — kills the
   successor `pastePO2_samebranch_universal` at introduction.
3. **The pinch**: the two falsifiers are complementary (one kills the
   length coordinate, the other the class coordinate).
   `triple_alive_universal` (R34) is the exact terminal tree-level
   universal; every natural strengthening now has a pinned
   counterexample. Anti-PO2 SA final tally: 3 falsifiers (2 cold
   n=18, 1 at n=16 from the ladder_gap3 graph re-rooted at 10 — not
   yet pinned, in tasks output only). Anti-samebranch tally: 11
   falsifiers, 4.74M iters, 19.5k residual states.
4. Strategy condensed (Sections 26–31 → digest); Q74/Q75 resolved,
   Q76 opened.

**qid state**: Q76 open and next (see queue for full text). Q69
[released] — consider resolving it against the R46 state if
convergence is ever declared (it references the dead
paste8_tree_universal target; its "remaining analytic core" claim is
now superseded by Q76).

**Suggested next moves (R47+)**:
1. **SA-probe `pastePO2_tree_universal` BEFORE introducing it**
   ($V(T) \cap \{4,8,16,32\} \ne \emptyset$, all pair classes).
   Harness: scratchpad r47_sa.py/r46_sb_sa.py pattern — energy =
   (viol, #configs with slack in {1,5,13,29} over ALL pairs with
   single-cycle D). The projected-coords fast evaluator only covers
   same-branch pairs; for branched pairs use set-based arcs or extend
   the evaluator via fund_pair_overlap/pasting_meeting_structure
   (legs L1, L2 + anchor interval A — 3 segments, P3 meets each in an
   interval; single-arc iff exactly one nonempty).
2. **Try to PROVE pasting-exhaustiveness** (R19: 2,604/2,604 firing
   triples factor through pasting). If proved, pastePO2_tree becomes
   EQUIVALENT to triple_alive_universal. Start from
   triple_sym_diff_structure(3): S single cycle → some pair's D
   single cycle + single-arc meet? (Careful: probably needs the
   even-subgraph decomposition; run a designated SA falsifier for
   exhaustiveness itself FIRST — energy = residuality then
   #firing-triples-with-pasting-factorization minus #firing-triples.)
3. Study the falsifier anatomy pair (Q76 handle): what geometry
   forces class/length switching.
4. If both tracks stall: /erdos-proof-ideation with the pinch as
   framing, or declare convergence — the partial result (proved
   machinery + pinched terminal universal + 14 pinned
   counterexamples) is publishable-grade negative knowledge.

**CRITIC INFRA (standing list, all live)**:
- Prewarm internal AND falsify (timeout_s=900) before proof_prepare —
  BOTH took 412s this session, over the 240s in-run cap. MUST export
  `NODE_EXTRA_CA_CERTS=/root/.ccr/ca-bundle.crt` for claude -p to work
  in the remote container (TLS proxy; without it critics fail in ~4s).
- Check falsify's numerical_checks from the cache BEFORE
  proof_prepare (R41/R45 trap). This session: all 4 checks true, no
  trap.
- Strategy is at ~114k bytes — nearing the 120k critic threshold
  AGAIN. Condense Sections 65–77 (R25–R37 narratives, mostly
  superseded by the R46 disproofs) EARLY next session.
- HARNESS TRAP (bit twice this session despite the warning): shell
  cwd resets unpredictably between Bash calls; one strategy append
  landed in the MAIN checkout and had to be reverted. cd to the
  worktree INSIDE every command; never use bare relative paths.
- Stop-hook forces mid-session commits+pushes; journal/queue rows are
  fine to push, keep doing it.
- proof_results.tsv is container-local (gitignored): the round cap
  counter resets each container. R-numbering lives in the strategy
  narrative — keep it monotone by hand.

**Files modified this session**:
- proof_strategy.md (Sections 26–31 digest; Section 86 + 3 addenda)
- proof_lemmas/lemma_paste8_projected_coords__0817-081104-2f11.md (NEW, proved)
- proof_lemmas/lemma_slack_ladder_above5__0817-081104-2f11.md (NEW, disproved same round)
- proof_lemmas/lemma_pastePO2_samebranch_universal__0817-081104-2f11.md (NEW, disproved same round)
- proof_lemmas/lemma_paste8_samebranch_universal__0815-080733-7bd0.md (open → disproved, CHECK 4 = sb_falsifier_n18)
- proof_lemmas/lemma_paste8_tree_universal__0812-081033-f881.md, lemma_sup8_tree_universal__0811-081051-a768.md, lemma_pasting_value_interval__0805-080844-5fb3.md (open → disproved)
- queue (Q74 claimed→resolved, Q75 opened→resolved, Q76 opened), journal, notes
