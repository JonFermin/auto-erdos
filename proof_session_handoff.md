# Session handoff (session s_0909-080743-06ca)

**Stop reason**: logical milestone — two rounds, two keeps (R81
probe/floor, R82 c16_dip_decomposition PROVED). Clean stopping point
before the d<=2 supply lower bound, which is a full proof attempt
best given a fresh session's budget.

**program**: arc-exchange — continuation window session 2 (the
s_0908 handoff justified continuation with 4 proved lemmas; this
session added a 5th, c16_dip_decomposition). Pre-committed sibling
if the NEXT session prefers rotation is still Q0905-082429-2 (mod-4
invariant, Dean–Lesniak–Saito literature check first).

**Consecutive exploit sessions on current program**: 0
(this session claimed Q0905-082429-1, whose ideation row carries
kind: explore, so it is an EXPLORE session — k resets to 0.)

**What happened**:

1. **R81 (keep, f20e7c9)**: mined the two failing tau=1 d=1 route
   choices (n28r0 v=7 route 25-26-27; n28r6 v=0 route 1-2-3). The
   obstruction is a PINPOINT f2->f1 path-spectrum gap at length 11
   (lengths 10 and 12 both present, no parity/connectivity
   obstruction) — dip-menu arithmetic in G-{u,v,x,y} misses total
   shortening 4. In BOTH failures the alternate foot of u with the
   SAME route closes, so per-pair (B) survives (7/8 resp. 9/10
   choices OK). Proved the contrast: ALL 1,629 tau>=2 d=1 landings
   carry >=3 valid completions (slack floor 3), vs floor 0 at
   tau=1 d=1. CHECK 3 added to lemma_c16_landing_universal pins
   both. Section 121.

2. **R82 (keep, a552053)**: NEW lemma c16_dip_decomposition
   (status: PROVED, ledger-recorded). The completion calculus at a
   dist-2 tau>=2 landing: for ANY length-12 f2->f1 path P in
   G-{u1,v,u2}, the closed walk (a) has 16 distinct vertices;
   (b) decomposes as arcs+off-C segments (chordless C); (c)
   arc-sharing is AUTOMATIC — the spokes of f1,f2 are exactly the
   deleted u1,u2, so P must leave f2 / enter f1 along C, i.e. its
   first and last edges are C-edges; (d) no pure-arc P (needs d=4,
   excluded); (e) at d=1 arc-sharing => chorded for FREE (the
   C-edge f1f2 is a chord). Corollary: the d=1 landing-closure
   question reduces to BARE length-12 path existence in the deleted
   graph. Corpus census: at d=1 all 18,325 paths are valid; at
   d>=2 the ONLY failure mode anywhere is chordlessness (~9.5%);
   noshare/not16 never occur. Section 122.

**qid state**: Q0905-082429-1 released at this session_end (program
continues, R83 next). Q85, Q0905-082429-2, Q0905-082429-3 unchanged.

**Suggested next moves (R83)**:
1. QUICK WIN: pin the completion-count floor >=3 across ALL feet
   distances d (not just d=1). The margin map (r83_probe.py, in the
   notes/CONJECTURE this session): floor is 3 at d in {1,2} only,
   8-12 for d>=3. An early-exit cap-3 CHECK over all 9,134 landings
   runs in ~2.2s (verified). This upgrades c16_landing_universal's
   quantitative backing to all-d and isolates d<=2 as the tight
   zone.
2. MAIN LINE: attack the d<=2 supply lower bound directly. By R82
   the d=1 obligation is: G-{u1,v,u2} always has a length-12
   f2->f1 path. Raw material: chordless_c16_ear_geometry (e) — 16
   spokes on <=14 outside vertices; deleting {u1,v,u2} removes <=3
   outside vertices and exactly 2 spokes, leaving >=14 spokes on
   <=11 outside vertices. This is a pure path-existence /
   blob-supply statement — the cleanest form the closure question
   has ever had. d=2 needs the same plus the chord argument (at
   d>=2 chordedness must be argued, not free).
3. FALLBACK / rotation: if the supply bound stalls, the
   pre-committed sibling is Q0905-082429-2 (mod-4 invariant;
   literature check Dean-Lesniak-Saito first).

**CRITIC INFRA (standing, carried forward + UPDATED)**: prewarm ALL
7 critics BEFORE proof_prepare (cache replays). Prewarm pattern
(rebuild in scratchpad each session — scratchpad dies with the
container): render via pp._render_critic_prompt(name, spec,
proof_md, witness_valid=wv); call library._critic_subprocess.
call_critic(use_cache=False, timeout_s=1500); store via _cache_store
ONLY if _parse_critic_response parses AND (numerical/falsify) no
numerical_check _sandboxed_eval dies on a sandbox ARTIFACT
(NameError/SyntaxError/banned-token; genuine False evals are real
findings — keep). This session: all 7 stored attempt 1 both rounds;
falsify is the slow one (~520-830s), full prewarm 748-826s.
proof_prepare then runs ~175s (lemma CHECKs dominate).
** NEW LESSON (cost me a wasted prewarm + two dead proof_prepare
runs this session): strategy+falsify prompts EMBED the whole lemma
corpus. Do NOT create a lemma file and then hold it aside (mv) while
a prewarm runs — those two critics render with the transient file
and store a stale prompt_sha that never matches the clean tree, so
proof_prepare MISSES falsify -> synthetic BLOCKING(falsify). Finish
ALL proof_lemmas/ edits for a round BEFORE launching the prewarm.
Run render/hash diagnostics ONLY from inside the worktree — a cwd
reset to the main checkout reads a different proof_strategy.md and
reports spurious MISS on all 7. ** PROOF_TAG on the SAME command
line for EVERY helper. cwd RESETS between shell calls. R-numbering
by hand (next: R83). proof_results.tsv is LOCAL — the journal is the
durable trail.

**Files modified this session**:
- proof_strategy.md (Sections 121, 122)
- proof_lemmas/lemma_c16_landing_universal__0908-080733-7e19.md (CHECK 3 + R81 amendment)
- proof_lemmas/lemma_c16_two_route_menu__0907-080748-6915.md (R81 anatomy note)
- proof_lemmas/lemma_c16_dip_decomposition__0909-080743-06ca.md (NEW, proved)
- records/proof_erdos_gyarfas_{305c565fd2e9_f20e7c9,e28a10bd8cf6_a552053}.json
- proof_open_questions.jsonl, proof_journal.jsonl, proof_notes (2 appends: CONJECTURE + CRITIC-INFRA)
