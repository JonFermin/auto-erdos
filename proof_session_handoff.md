# Session handoff (session s_0906-080631-d6e8)

**Stop reason**: Major milestone — the BRANCH-DISTANCE THEOREM is
proved over the whole witness-decidable range (R74 + R75, both
keep_progress).

**program**: arc-exchange — session 2 of 3

**Consecutive exploit sessions on current program**: 0
(this session claimed Q0905-082429-1, whose ideation row carries
kind: explore; the orphaned s_0905 that opened the program was
explore for the same reason.)

**What happened**:

1. **R74 (`c16_dist3_le30` proved, keep, afb6b50)**: in class
   members on 24<=n<=30, every 0-spoke vertex of a chordless C16
   has dist(v,C) <= 3. Proof: radius-2 ball bound in cubic C4-free
   graphs (|B(v,2)| = 8 on a triangle / 10 otherwise) + spoke
   pigeonhole (|T| >= 6) kills n<=28; at n=30 the forced 8-vertex
   plug G[Z]=B(v,2) (degree seq (3^6,2^2) or (3^7,1), radius 2)
   does not exist — 129,584-graph enumeration, validated against
   the known 19,355 labeled cubic count + differential prune test,
   ZERO survive (C8-freeness kills the last 2,520).

2. **R74 cross-n sweep**: corpus (n=26 member 14 pairs; twelve n=28
   reps + pin 745 pairs) + walks (n=24 42,300 / n=26 67,312 /
   n=28 59,397 / n=32 201,612 pairs): the CORE arc-exchange
   conjecture passes every one of ~411k new pairs. ALL THREE R73
   refinements FALSIFIED at n=32 with reproducible CHECK witnesses:
   dist-3 (37 dist-4 pairs), share-8 (min 7), off-6 (up to 8).
   At n<=28 the invariants are STRONGER (dist=2, share>=9, off<=5).
   R73's ear-menu/replaced-arc conflation fixed in Section 113 +
   lemma file.

3. **R75 (`c16_dist4_n32` proved, keep, 9b4f90b)**: at n=32,
   dist(v,C) <= 4, sharp. The dist-5 forcing pins |T|=8 dead,
   |T|=7 -> Z = B(v,2)+{z*}, |T|=6 -> Z = B(v,2)+{e1,e2}; the ball
   is the rigid 8-vertex triangle shape (interior degrees full), so
   only 71 completions exist across all four cases — every one has
   a C4 or C8. Same-session turnaround of the R74 conjecture-
   register entry.

**qid state**: Q0905-082429-1 RELEASED back to open (program
continues, R76 next). Q85 (branch-vertex umbrella) open.
Q0905-082429-2 (mod-4) and Q0905-082429-3 (triangle-cover) open;
the Section 113 sibling pre-commitment order stands.

**Suggested next moves (R76)**:
1. The (a,b,c) MENU LEMMA at n <= 30: v at dist <= 3 from C; the
   exchange needs TWO disjoint v-C routes (not necessarily
   shortest — that is the gap the corollary remark flags).
   Instrument the walk data first: record the two-route length
   pairs (c1,c2) and foot arc-distances actually used by minimal
   witnesses; then prove the menu against chordless_c16_ear_geometry
   + the off-C budget |Z| <= 16-|T|.
2. If the menu lemma stalls this session or next, the pre-committed
   sibling program is Q0905-082429-2 (mod-4 invariant), opening
   with the Dean-Lesniak-Saito literature check (Section 113).
3. The plug-forcing method (rigid ball + tiny completion space +
   C8 kills last) is now 2-for-2; it may also settle the n=32
   two-route geometry directly.

**CRITIC INFRA (standing, carried forward)**: prewarm ALL critics
via scratchpad prewarm.py THEN proof_prepare (cache replays); the
prewarm pattern: solo call_critic per critic (900s window,
use_cache=False), validate parse + every numerical_check
sandbox-evals truthy (sandbox lacks sorted/itertools!), only then
_cache_store. PROOF_TAG on the SAME command line for EVERY helper.
cwd RESETS between shell calls. R-numbering by hand (next: R76).
proof_results.tsv is LOCAL and dies with the container — the
journal is the durable trail. Walk/probe scripts (r74_lib.py has
the shared probe_graph with strict=False mode) died with this
container's scratchpad; the CHECK blocks in the two lemma files
carry everything reproducible.

**Files modified this session**:
- proof_strategy.md (Sections 114, 115 + R73 conflation fixes in 113)
- proof_lemmas/lemma_c16_dist3_le30__0906-080631-d6e8.md (NEW, proved)
- proof_lemmas/lemma_c16_dist4_n32__0906-080631-d6e8.md (NEW, proved)
- proof_lemmas/lemma_arc_exchange_witness__0905-080544-2e51.md (R74 section, CHECKs 4-5, amended invariant table)
- records/proof_erdos_gyarfas_{b910b0026c44_afb6b50,...R75...}.json
- proof_open_questions.jsonl, proof_journal.jsonl, notes channel
