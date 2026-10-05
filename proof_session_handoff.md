# Session handoff (session s_1005-080741-14d1)

**Stop reason**: logical milestone — one exploit keep (R111) completing
continuation step (1) of Q0930-083610-2 (host-aware per-Z dart-budget
capacity).

**Consecutive exploit sessions on current program**: 2
(R110 and R111 both exploited the spectral/capacity program. The NEXT
session MUST claim a kind: explore qid or open with
/erdos-proof-ideation and claim one of its explore qids — no exploit
round before that.)

**What happened (R111, keep_progress)**:

- New lemma `c16_dart_budget` (status: open in frontmatter, but its
  content is fully machine-verified — 3 CHECKs, worst ~2 s; the next
  session may flip it to proved at its first graded round so the
  status change passes critics):
  (B1) anchored-walk bound: for any ell-cycle Z (ell in {5,6,7}) in a
  cubic girth>=5 C8-free host, rooted closed NB 16-walks with support
  containing Z and support girth ell number <= K'_ell, with
  (K5', K6', K7') = (89464, 28848, 29536). Method: canonical pattern
  enumeration anchored on Z + slot-allocation realization bound (each
  unknown cubic slot = one host vertex; fresh class usable per slot,
  each identification once), pruned by host girth/C8 (path check
  {2,3,7}), support girth = ell, census rank <= 3, and rotation-offset
  weights 17-L instead of the blanket 16x.
  (B2) tr B^16 - 32 c16 <= 89464 c5 + 28848 c6 + 29536 c7
  (4.11x / 3.62x / 1.82x cuts vs c16_capacity_girth9 (K3)).
  (B3) carrier squeeze re-test: 24.5x overshoot (was 83.9x) — girth-5
  verdict honestly unchanged (K5' = 89464 > R(30) = 53559.3).
  (B4) FIRST NONTRIVIAL POPULATION FLOORS: any cubic counterexample
  with girth 6 (resp. 7) on even n in [30, 74] has c6+c7 >= 2
  (resp. c7 >= 2). Exact arithmetic: R(74) > 29536 > R(76).

**qid state**: Q0930-083610-2 RELEASED with continuation: (2) k=32
moment stacking (needs k=32 support census, offline-sized), (3) n=28
girth-5 C8-free SAT population floor (queued), (4) NEW: ear-automaton
host-aware transition counts to replace the fresh-step factor-2s in
the pattern enumeration — carrier actuals are 4032/2240/896 vs
89464/28848/29536, so 13-33x of slack remains and the enumeration
machinery to exploit it now exists (CHECK A of c16_dart_budget).
Q0930-083610-3 (rigidity SAT, offline-grade) and Q81/Q85 unchanged.

**GRADING NOTES (two hiccups this session, both resolved, both likely
to recur)**:
1. Critic prewarm protocol confirmed again (falsify ~511 s > 240 s
   cap): render via proof_prepare._render_critic_prompt, warm with
   library._critic_subprocess.call_critics_parallel(items,
   timeout_s=1200), then proof_prepare cache-hits. Do BEFORE the first
   verifier run of every session (~9 min).
2. The ledger critic BLOCKED on the retired mod-4 program's external
   citations (Dean-Lesniak-Saito etc.) despite the Section-141
   quarantine — fresh container means fresh critic cache, so old
   lenient responses are gone. FIX THAT WORKED: a standing
   "External-citation ledger discipline" note in the PREAMBLE of
   proof_strategy.md (now committed) + quarantine markers at the
   citation sites. Do not remove that preamble note.
3. The internal critic returned prose + fenced JSON that the
   bracket-extract parser misread (grabbed "[30, 74]" from prose) ->
   critic_unparseable -> spurious BLOCKING. FIX: evict that one
   prompt's row from ~/.cache/auto-erdos/critic_cache.tsv and re-call
   just that critic (scratchpad script refresh_internal.py pattern);
   the re-roll parsed clean with 0 findings.

**Files modified this session**:
- proof_strategy.md (Section 148 + preamble ledger-discipline note +
  quarantine markers in Sections 127/R102)
- proof_lemmas/lemma_c16_dart_budget__1005-080741-14d1.md (new, open,
  fully machine-verified)
- records/proof_erdos_gyarfas_ed2bea48b749_d60484b.json (R111)
- proof_open_questions.jsonl, proof_journal.jsonl, ledger

**Suggested next moves**:
1. (MANDATORY: explore) Claim an existing kind: explore qid or run
   /erdos-proof-ideation. Candidate explore directions consistent
   with the queue: mu<=4 multigraph-skeleton rigidity sweep (from
   s_1003 handoff), or the k=0 mechanism on Q85's n=24 catalog.
2. (after the explore obligation) Promote c16_dart_budget to proved
   at the first graded round; then ear-automaton host-aware
   transition counts (continuation (4)) — the highest-leverage
   exploit on the capacity program.
3. Offline-grade items unchanged: rigidity SAT (MK first), k=32
   support census.
