# Session handoff (session s_0913-080612-48e5)

**Stop reason**: logical milestone — two rounds, two keeps (R87:
mod-4 STEP 0 verdict + gadget mining; R88: critical-pair rigidity
law + falsification-infra repair). Clean stopping point: the
rotation obligation is discharged, the mod-4 program is settled
(known theorem, mined, resolved), and the supply core is restated
strictly smaller.

**program**: arc-exchange — resumed as exploit AFTER this session's
explore round; extension note posted (Section 127) with a fresh
stop criterion (see below).

**Consecutive exploit sessions on current program**: 0
(this session claimed and resolved Q0905-082429-2, kind: explore —
the rotation the s_0912 handoff demanded. R88 applied that qid's
mined technique to the incumbent program's fragile-8; no bare
re-claim of the released supply qid occurred.)

**What happened**:

1. **R87 (keep, 5b48ac5)**: Q0905-082429-2's committed STEP 0
   (literature check) fired immediately: L_mod4 is
   Dean–Lesniak–Saito 1993 (min degree >=2 with <=2 degree-2
   vertices suffices); Dean's conjecture known for all k != 5
   (Choi–Chu 2026, arXiv:2605.02731). Falsifier arm retired,
   constraint engines never launched. Mined into
   `lemma_mod4_even_theta` (proved, CHECK-verified): T1 theta
   parity pigeonhole (all-even theta always carries a 0-mod-4
   cycle; all-odd unless paths congruent mod 4), T2 C16-ear
   residue-pair law (even ear at even span sends BOTH its cycles
   into ONE mod-4 class), C1 conditional EGC profile (external
   antecedent — NOT ledger-citable; ledger discipline paragraph in
   Section 127; FLAG FOR MAINTAINER: adding DLS 1993 to
   proofs/erdos_gyarfas.json:given_facts would make C1
   unconditional). Qid RESOLVED. Sections 127.

2. **R88 (keep, 38f82d7)**: `fragile_pair_geometry` (proved):
   the fragile-8's critical pairs realize exactly 3 shapes — SIX
   are the template ((3,2,1),(8,2,6)) (antipodal s=2 ear +
   interleaved (3,2) ear), exceptions n28r3/n28r4 pinned by name.
   Walk-slice criticality census (66 members / 2,376 landings):
   264 fragile landings, ALL 264 template — zero new shapes. P1:
   s=2 L3 pairs are parity-forced to opposite spans (offset sum
   7). P2 (via T2): the template's ears yield cycles {10,10} and
   {5,15} — no even cycle besides C, nothing in {4,8,16}; the
   critical apparatus is exactly what the ambient exclusions
   cannot touch. P4: naive mod-4 residue-lock REFUTED (recorded —
   do not re-derive). Section 128.

3. **INFRA (silent falsification gaps, both repaired in R88)**:
   (a) CHECK blocks require a closing `CHECK` sentinel before
   `-->` (`_CHECK_RE` in proof_prepare.py) — R87's block initially
   lacked it and was silently unregistered; fixed. ALWAYS verify
   new CHECK blocks register via
   `pp.run_lemma_checks()` meta counts. (b) `c16_d1_ear_cover`'s
   merged 21,345-char CHECK was over the 20,000 cap and SKIPPED
   (R84–R86 census probes not running!); split into two blocks
   (17,347 + 7,366), byte-identical assertions, both run. Current
   state: 126 checks ran / 0 failed / 1 pre-existing timeout
   (lemma_cyclic_orbit_avg_size, old primitive-set corpus).

**qid state**: Q0905-082429-2 RESOLVED (verdict in its resolution
row). Q85, Q0905-082429-3 open. Q0905-082429-1 released (rotation
flag satisfied by this session's explore round).

**Suggested next moves**:
1. R89+ (exploit, arc-exchange): the PLACEMENT proof — Section 128
   next-move (a): prove every L1-less, sequential-pair-less d=1
   menu contains the template (antipodal s=2 ear + interleaved
   (3,2) ear at offset sum 7), exceptions by name. Ingredients:
   E3 (s=2 floor), E4 (arc-triple law), P1 (parity-canonicity).
   Test bed: the walk's 264 template instances.
2. STOP CRITERION (Section 127 extension note): if two further
   critics-ON sessions pass without (a) a proved supply lemma for
   2-spoke-only tri-heavy menus or (b) a falsifying landing in an
   expanded walk census, the program closes and pivots to
   Q0905-082429-3 (triangle-cover stratum).
3. Background: scale the walk criticality census (5 seeds x 400
   steps) as falsification pressure on the rigidity law.

**CRITIC INFRA (standing, carried forward, s_0913 measurements)**:
prewarm ALL 7 critics BEFORE proof_prepare (cache replays);
prewarm.py rebuilt in scratchpad per the standing recipe WITH the
self-contradictory-OK rule AND a try/except around call_critic
(it RAISES CriticUnavailable on timeout, does not return None).
Opus-4-7 latency was PATHOLOGICAL this session: falsify took 5x
540s-timeout retries mid-session (backend congestion), then 360s
and 398s on later attempts; internal ran 348-408s (would breach
proof_prepare's hard 240s wall — prewarm with timeout_s>=420 and
let proof_prepare replay from cache). ledger/numerical ~100s,
sign/openness/strategy fast. proof_prepare warm ~40s. Lemma CHECK
suite now ~10s total. PROOF_TAG on the SAME command line for EVERY
helper; cwd resets between shell calls (background tasks too —
sys.path.insert(0, os.getcwd()) needed for `uv run python
/abs/path.py`). R-numbering by hand (next: R89). proof_notes.py is
CACHE-DIR-backed and DIES with the container — durable insights go
in strategy sections + this handoff. Ledger critic enforces the
given-facts ledger STRICTLY: external literature is quotable only
as program-steering context or conditional antecedents, never as
"theorem-backed" internal steps (cost R87 two edit-refire cycles).

**Files modified this session**:
- proof_strategy.md (Sections 127, 128)
- proof_lemmas/lemma_mod4_even_theta__0913-080612-48e5.md (NEW,
  proved: T1/T2/C1 + literature notes)
- proof_lemmas/lemma_fragile_pair_geometry__0913-080612-48e5.md
  (NEW, proved: P1-P4 + 4-host CHECK)
- proof_lemmas/lemma_c16_d1_ear_cover__0910-080911-1f4a.md
  (CHECK split only — assertions byte-identical)
- records/proof_erdos_gyarfas_16263cbf995f_5b48ac5.json (R87)
- records/proof_erdos_gyarfas_bc706c2b83b3_38f82d7.json (R88)
- proof_open_questions.jsonl, proof_journal.jsonl
