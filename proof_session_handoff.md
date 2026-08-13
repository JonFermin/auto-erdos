# Session handoff (session s_0813-080958-9732)

**Stop reason**: Logical milestone + context budget. R39 and R40 both
keep_progress with committed records.

**What was done this session**:

R39 — **paste-8 cell census** (seed 20260813, 153,600 trees, 46
residual): tabulated ALL paste-8 witnesses per residual tree on the
8-line $g_3 = 2k'+7-|D|$. Findings: $k' \le 2$ witness on 46/46;
$k'=1$ universal FALSE (3 fresh n=14 pins + sup1_dead_tree — its six
paste-8s are (6,2)/(10,4) only); $k' \le 2 \wedge$ short FALSE
(sup1_dead_tree's (6,2)s are non-short). Proved the finite $k' \le 2$
cell menu (8 cells: k'=1: |D| in {3,5,7}; k'=2: |D| in {3,5,6,7,9})
via po2 exclusions. Committed `paste8_k2_universal` (open).

R40 — **paste8_k2_universal DISPROVED at witness-box scale.**
Rejection sampling: 0 residuals in 3,160 trees at n>=28 girth>=5 —
dead end. Adversarial SA over (cubic graph, DFS tree) pairs
(energy = #po2 singles + #po2 pair sym-diffs, moves = 2-opt rewire
keeping girth>=5 + DFS re-root/re-order, 391 restarts/420s) constructed
**20 pair-residual trees at n in {30,32,36,40}** — the first residual
population above the F3 floor. 4/20 have NO $k' \le 2$ paste-8 (min
$k'$ = 3/4); three pinned deterministically in the lemma's CHECK 2
(viol1_n30, viol2_n30, viol3_n40). Ledger: paste8_k2_universal ->
disproved. **No O(1)-local / bounded-k' supply certificate exists.**
All 20 trees DO have a paste-8: `paste8_tree_universal` now has 20/20
adversarial above-floor evidence (bullet added to its lemma file).

Also: internal-critic BLOCKING (floor-vs-line misread of §70(A))
fixed with hypothesis anchors at §70(A)/(B) — on residual trees the
(6;1,3) window entry is unrealizable (C_4 cover), matching §79's menu.

**qid state**: Q69 released (census + falsification done; analytic
supply core remains). **Q70 opened**: SA-harden the surviving ladder —
bias the R40 SA energy AGAINST paste-8 / any-8 / any-po2 availability
and attack paste8_tree_universal, sup8_tree_universal,
triple_alive_universal at n in [30,64]. A falsifier at any level
redirects the program cheaply; survival is the strongest evidence
obtainable before analytic effort.

**Open core after R40** (priority order):
1. **Q70** (SA-harden the ladder) — do this FIRST; the R40 harness
   pattern is in the notes channel (and §80). Energy for level 2:
   e.g. lexicographic (po2-firings, then #paste-8 triples) or a
   penalty sum; keep girth>=5 and n in [30,64].
2. If the ladder survives: analytic supply for paste8_tree_universal
   with UNBOUNDED k' — value side closed by shortpaste_floor_line for
   all k'; candidate handle: dichotomy paste certificates (c1)-(c3)
   (they do not bound k').
3. Fallback (untouched): graph-level quantifier — choose the DFS tree.
4. Straddle 8-line proved and idle (target only if paste dies).

**CRITIC INFRA (unchanged + one new trap)**:
- Prewarm internal AND falsify BEFORE proof_prepare on every round
  that edits strategy/lemmas: render via pp._render_critic_prompt with
  PROOF_TAG=erdos_gyarfas exported, call_critic(..., timeout_s=900),
  from INSIDE the worktree. Assert pp.PROOF_TAG == "erdos_gyarfas".
- PROOF_TAG trap hit AGAIN this session: a bare `uv run proof_notes.py`
  wrote to proof_notes_primitive_set_erdos.md (deleted, rewritten with
  the tag). EVERY helper needs the export, not just prepare/log.
- Python sys.path trap: `uv run python /abs/script.py` puts the SCRIPT
  dir on sys.path, not cwd — scripts importing proof_prepare need
  sys.path.insert(0, worktree) or run via heredoc.
- proof_strategy.md is ~114k chars — condense before ~120k.
- HARNESS TRAP (unchanged): PREFIX EVERY COMMAND with
  `cd /home/user/auto-erdos/worktrees/0730-080656-0fbf`.

**Files modified this session**:
- proof_lemmas/lemma_paste8_k2_universal__0813-080958-9732.md (new R39,
  DISPROVED R40 — CHECK 1 = 5 small pins, CHECK 2 = 3 disproof pins)
- proof_lemmas/lemma_paste8_tree_universal__0812-081033-f881.md
  (evidence bullet: 20/20 adversarial at n=30..40)
- proof_strategy.md (§79, §80, hypothesis anchors at §70(A)/(B))
- proof_open_questions.jsonl (Q69 released, Q70 opened), journal,
  ledger (paste8_k2_universal disproved)
- records/proof_erdos_gyarfas_40a2030ad255_9d5a50a.json (R39 keep)
- records/proof_erdos_gyarfas_034a356205fa_402f073.json (R40 keep)
- notes channel: R39+R40 summary + SA-harness lesson

**Suggested next moves (R41+), in order**:
1. Claim Q70. Port the SA harness to penalize 8-availability; run
   against paste8_tree_universal first (it is the strongest live
   claim, so a falsifier there is cheapest to find if one exists).
2. Any falsifier -> pin it deterministically, flip the lemma, drop to
   the next ladder level (the R40 lemma-edit pattern is the template).
3. If 50+ adversarial trees at multiple n all survive: switch to the
   analytic unbounded-k' supply attack, or /erdos-proof-ideation with
   the SA-survival data as framing.
