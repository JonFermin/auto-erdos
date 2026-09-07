# Session handoff (session s_0907-080748-6915)

**Stop reason**: clean session end — two rounds, both keeps (R76
`c16_two_routes` proved; R77 `c16_two_route_menu` opened with
2,440-pair CHECKs).

**program**: arc-exchange — session 3 of 3; BUDGET WINDOW CLOSED with
three consecutive keep sessions (R74–R75, R76–R77). The Section 113
pre-commitment fires only on STALL (no proved rung and no falsifier);
the program instead produced four proved lemmas in the window, so
continuation is justified. If the next session prefers rotation
anyway, the pre-committed sibling is Q0905-082429-2 (mod-4
invariant), opening with the Dean–Lesniak–Saito literature check.

**Consecutive exploit sessions on current program**: 0
(this session claimed Q0905-082429-1, whose ideation row carries
kind: explore.)

**What happened**:

1. **R76 (`c16_two_routes` proved, keep, 2b61ae4)**: every 0-spoke
   vertex of a chordless C16 in a class member on 24<=n<=30 has TWO
   v->C paths sharing only v, distinct feet, interiors off C. Proof:
   Menger fan + cutvertex blob kill — a separating cutvertex forces a
   connected C4+C8-free blob with d_w in {1,2} degree-2 vertices
   (parity-forced: d_w == k mod 2), rest cubic, on k <= 9 vertices
   (0-spoke budget |Z| <= n-22, +1 iff w on C); NO such graph exists
   on k=4..9 (CHECK 1: C4-freeness alone kills k<=7; the 360/10,080
   C4-free candidates at k=8/9 all contain C8s). k=10 (413,280) and
   k=11 (11,340,000 candidates, 359 s) also enumerate to ZERO, so the
   conclusion extends to n=32 by documented (not CHECK-backed) runs.
   Plug-forcing signature (C8 fails last) now 3-for-3.

2. **R76 instrumentation (whole corpus + first hardcoded n=24
   member)**: single-arc exchange is NOT per-pair universal (218/2437
   pairs lack one: 7/14 at n26, 38/745 at n28, 173/1678 at n30); ALL
   have m=2 witnesses, 215/218 via a length-2 ear second segment. The
   universal law is the ROUTE MENU: per pair, some witness has routes
   (c1,c2) in {(2,2),(2,3)} at dist-2 / (3,3) at dist-3, segment
   <= 6 — per-pair optimal. (2,2) segments are forced composite
   (single-arc L=4 makes the complementary cycle a C8).

3. **R77 (`c16_two_route_menu` opened, logged)**: the menu as an open
   lemma with two CHECKs (762 pairs n<=28 + n24; 1,678 pairs n=30
   with the 39 dist-3 fallback pairs verified to be exactly the
   (3,3) rows). Arc-exchange lemma file amended with the R76
   universality correction.

4. **Geometry probe for R78** (scratchpad r77_probe_geo.py, results
   in this handoff only): for minimal (2,2)+ear witnesses the
   v-segment feet arc-distance menu is {1,2,3,5,6,7,8} — the d=4 gap
   predicted by the exclusion table ({d+L,16-d+L} cap {4,8} empty) is
   EXACTLY realized, everything allowed occurs. So the dist-2 menu
   proof must be pigeonhole-over-allowed-configs (some allowed
   (d_seg, d_ear) completion always exists), not unique-shape
   forcing. Ear supply comes from chordless_c16_ear_geometry(e)
   (some 2-ear apex exists at n<=31).

**qid state**: Q0905-082429-1 claimed by this session — release it at
session_end (program continues, R78 next). Q85, Q0905-082429-2,
Q0905-082429-3 unchanged.

**Suggested next moves (R78)**:
1. Prove the dist-2 row of the menu at n<=28 first (uniform dist-2,
   |Z| <= 6): two routes of length 2 exist by c16_two_routes +
   distance; the feet are spoke-hosts of two distinct T-neighbours of
   v('s neighbourhood). Count the allowed (d_seg, d_ear, arcs)
   completions against |T| >= 6 and the ear menu; the blob-kill /
   plug-forcing style may again reduce to a finite enumeration.
2. The (3,3) fallback at n=30: re-run the c16_dist3_le30 plug
   forcing one level up — the dist-3 geometry already pins B(v,2).
3. If the menu stalls: falsifier hunt at n=30 walk states targeting
   pairs with ONLY long-route witnesses (none seen in 1.5M pairs).

**CRITIC INFRA (standing, carried forward + NEW lesson)**: prewarm
ALL critics via scratchpad prewarm.py THEN proof_prepare (cache
replays; newest cache row shadows older). NEW: store a critic
response ONLY if every numerical_check sandbox-evals without
ERROR — the sandbox lacks `sorted` (also itertools); a CORRECT
OK-flagged falsify finding using sorted() got NameError-escalated to
BLOCKING this session and had to be re-warmed (rewarm_falsify.py
pattern: up to 4 attempts, require parse OK + zero eval-ERRORs;
genuine False evals are real findings — keep those). internal and
falsify critics each need ~8-13 min and often fail parse on attempt
1; budget ~25 min per full prewarm. PROOF_TAG on the SAME command
line for EVERY helper. cwd RESETS between shell calls. R-numbering
by hand (next: R78). proof_results.tsv is LOCAL — the journal is the
durable trail.

**Files modified this session**:
- proof_strategy.md (Sections 116, 117)
- proof_lemmas/lemma_c16_two_routes__0907-080748-6915.md (NEW, proved)
- proof_lemmas/lemma_c16_two_route_menu__0907-080748-6915.md (NEW, open)
- proof_lemmas/lemma_arc_exchange_witness__0905-080544-2e51.md (R76 amendment)
- records/proof_erdos_gyarfas_4ac8804f82e5_2b61ae4.json (R76 keep)
- proof_open_questions.jsonl, proof_journal.jsonl, notes channel
