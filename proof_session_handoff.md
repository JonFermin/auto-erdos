# Session handoff (session s_0811-081051-a768)

**Stop reason**: Logical milestone + token budget. R35 and R36 both
keep_progress with committed records.

**What was done this session**:

R35 — **L=8 per-firing exactness is FALSE** (`l8_exactness_dead`,
PROVED). A 12-vertex cubic graph with a pair-residual normal tree
(root 10) fires one triple at L=4 — the fired 4-cycle is an ordinary
C4 of the graph invisible to every fundamental cycle and pair
sym-diff — alongside six L=8 triples. At scale (5 seeds + smoke,
1,605,440 trees, 465 residuals): firings L=8 3017 / L=16 199 / L=4 52.
R34's "all firings L=8" was census-window luck (and contradicted R18's
old C4-39x datum). Census also verified: triple-aliveness 465/465
(cumulative 641/641), every firing triple has a usable pairing
(3268/3268), arc bound |components(D∩C3)| <= 2 on all 8307 pairings
(k''=1 always 1-arc; k''>=2 split 4843 paste / 1771 straddle), length
identity L=|D|+gap3+1-2k'' exact everywhere, max k''=16, max |D|=22.

R36 — **`sup8_tree_universal`** (new open lemma + probe): every
pair-residual tree has SOME L=8 firing triple. Strictly stronger than
triple_alive_universal; 8 was present in the firing-length set of
295/295 tracked residuals (R35) + 176/176 (R34) = 471/471 across ten
seeds. CHECK 1 anchors on the l8_exactness_dead pin (fires 4 AND 8);
CHECK 2 = fresh-seed (20260811) 125k-tree probe, ~10s, 39 residuals,
prints falsifier for pinning.

**qid state**: Q68 released with progress (R35+R36 done). Next session
re-claims Q68 for the straddle value theory, or opens a new qid.

**Open core after R36** (priority order):
1. **k''>=2 straddle value theory** — the analogue of
   shortpaste_floor_line for straddling covers (the 2-arc branch of
   pasting_cover_dichotomy: I ⊆ P3, gap3 >= k12+2). What (|D|, gap3,
   k'') values can straddle configs realize, and when do they hit
   L=8? Straddle = 1771/8307 firing pairings; 24/465 trees fire ONLY
   via k''>=2. The R35 joint census data (scratchpad, regenerate with
   the sweep harness if needed) showed no channel is length-pure.
2. **Prove sup8_tree_universal on a structured subclass** (e.g. trees
   where some k''=1 witness exists — the parked R33 selection rule
   held 123/123 there and shortpaste_floor_line pins the value side).
3. Fallback (untouched): graph-level quantifier — choose the DFS tree.
4. Caveat to keep in view (falsify critic, valid): all censuses are
   n<=26; the witness box is n in [30,64] girth>=5. Sampling can only
   falsify; the universal needs proof.

**CRITIC INFRA (2026-08-11 session — READ BEFORE FIRST VERIFIER RUN)**:
- The escalation-roulette mitigation WORKS: after 2 rolls of textual
  fixes (superseded markers on stale summary tables, worked
  single-instance arithmetic anchors near every formula the falsify
  critic re-derives) both rounds cleared to 0 BLOCKING.
- NEW TRAP: prewarming from the WRONG CWD silently caches prompts for
  master's stale content (proof_prepare resolves files from its own
  __file__). ALWAYS `cd worktrees/0730-080656-0fbf` INSIDE the same
  shell command before `uv run python` prewarm scripts AND check the
  printed strategy path.
- NEW TRAP: an UNPARSEABLE critic response (prose instead of JSON) is
  CACHED and re-runs replay it forever. Recovery: evict the corrupt
  row from ~/.cache/auto-erdos/critic_cache.tsv (match critic name,
  _parse_critic_response fails), then re-call with timeout_s=900.
- NEW TRAP: `git commit --amend` after a bookkeeping commit rewrites
  the WRONG commit (and if pushed, strands the branch). Check `git
  log -1` before amending; prefer a new commit + normal push.
- Worked-instance anchors added this session: shortpaste_floor_line
  boundary tuples (§70 area), leaf-pair formula instances (§58),
  v_min-vs-min-E_p reconciliation (§69), T2/T3/T1 parity note (§48
  area). Do not remove them — they are what keeps the falsify/internal
  critics at 0 BLOCKING.
- proof_strategy.md is ~99k chars — condense before ~120k.
- HARNESS TRAP (unchanged): shell cwd resets between turns; PREFIX
  EVERY COMMAND with `cd /home/user/auto-erdos/worktrees/0730-080656-0fbf`.

**Files modified this session**:
- proof_lemmas/lemma_l8_exactness_dead__0811-081051-a768.md (new, PROVED, R35)
- proof_lemmas/lemma_sup8_tree_universal__0811-081051-a768.md (new open probe, R36)
- proof_lemmas/lemma_triple_alive_universal__0810-081024-1a40.md (R35 census + refs)
- proof_strategy.md (§75, §76, critic-anchor fixes in §48/§58/§69/§70, R31 table superseded markers, R25 step-2 gap closed)
- proof_open_questions.jsonl, proof_journal.jsonl, ledger (appends)
- records/proof_erdos_gyarfas_9123b324ca28_ee6ea4e.json (R35 keep)
- records/proof_erdos_gyarfas_921c2b27ca0d_2b21098.json (R36 keep)
- cross-branch notes channel seeded (was empty): killed list + open core

**Suggested next moves (R37+), in order**:
1. Straddle census: enumerate straddle firing pairings' (|D|, gap3,
   k'', k12) jointly with the pasting_cover_dichotomy constraints
   (I ⊆ P3 forces gap3 >= k12+2); look for the floor and the 8-line.
2. If a clean straddle floor/line emerges, attempt the two-channel
   cover: k''=1 line (proved) OR straddle line always solvable on a
   residual tree => sup8_tree_universal.
3. If the value theory stalls, /erdos-proof-ideation on
   sup8_tree_universal with the 24 k''>=2-only trees as the framing.
