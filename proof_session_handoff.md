# Session handoff (session s_0924-080701-ca63)

**Stop reason**: logical milestone — one round (R93), one keep. The
arc-exchange program's pre-committed stop-criterion clock EXPIRED
this session (critics-ON session TWO of two since the R89/R90 reset
without a proved supply lemma): the program PAUSES.

**Consecutive exploit sessions on current program**: 1
(this session ran an exploit round on the arc-exchange program after
s_0923's explore reset; the program is now PAUSED by its own stop
criterion, so the NEXT session must NOT re-claim Q0905-082429-1 —
pivot to Q85 (branch-vertex program, kind: exploit on a DIFFERENT
program) or open with /erdos-proof-ideation to mint a fresh explore
queue. Q0905-082429-1 is released with a pause note.)

**What happened (Section 133; T6 added to lemma
template_placement; record
records/proof_erdos_gyarfas_28bac29a6d86_3289fa5.json)**:

R93 (keep_progress, commit e479dad + follow-ups). Executed Section
131's (b*) FIRST: 18 fresh walks beyond every visited seed (12 new
n28r3 seeds rng99-110 x1200, 4 n28r4 starts rng99-102 x1200 — first
n28r4 probes past 400 steps, and rng96/97 extended to 4000 steps).
23,668 non-antipodal occurrences, ZERO route-disjunction failures —
the sharpest falsification target stays unrealized at ~29,500
cumulative. NEW LAW (open): the {4,9} route XOR — pilot-only 18,409
/ long-only 453 / both 0: the routes are mutually exclusive AND
exhaustive (R91's 4,046/74 obeyed it unremarked). {4,7}'s pilot
route never fails. Mechanism purity: all 453 pilot-fails are T5's
self-block in minimal form (menu has EXACTLY ONE shortening-1 ear,
on the pilot's host). (1,7,8) long anchor 29,553/29,553; {4,7}
pilot (1,3,12) typing 4,806/4,806; {7,12} still 0 occurrences;
n28r4 still produces nothing. Then (a*) partial: T6 PROVED (the
route-shape and window catalog, CHECK G): realizations/widths
(9/10/13), flank bounds (pilot delta'<=9 resp. 6; long <=6/4/1),
spectra (sigma'=1 never E2-blocked, delta' in [3,9]; sigma'=-2 loses
{1,3}; sigma'=-4 = {(1,5),(3,7),(4,8)} ONLY; sigma'=-7 = single
(1,8) slot), probe soundness (every route companion has s'<=8 so
maxs=10 probes are exhaustive — the 453 failures are real), and the
constructible both-fail falsifier profile ((alpha)+(beta), T6(v)).

**qid state**: Q0905-082429-1 RELEASED with pause note. Q85 open
(branch-vertex program — the designated pivot). Q81 released
(background). Queue may need ideation if Q85 stalls.

**Suggested next moves**:
1. PIVOT (mandatory): claim Q85 (branch-vertex program: every
   chordless C16 needs a 0-spoke outside vertex; attacks (a) local
   structure of 0-spoke vertices, (b) 16-spokes-on-<=n-17-vertices
   pigeonhole, (c) mine the 120-member corpus for all-chordless-C16
   proximity) — or run /erdos-proof-ideation for a fresh queue.
2. When arc-exchange RESUMES (after >=1 session away), the stored
   leads (Section 133 next-moves): (a) prove the {4,9} XOR forward
   half — window arithmetic + C8-freeness on (1,5)/(3,7)/(4,8)
   shapes; (b) prove the {7,12} exclusion outright (width 13 pins
   lo1=1, both ears pinned, 0 sightings in ~29,500); (c) supply
   core = show the T5-minimal configuration forces a long-flank
   companion (E3/E4 spoke counting on <=8 flank positions).

**Files modified this session**:
- proof_strategy.md (Section 133)
- proof_lemmas/lemma_template_placement__0915-080622-71a7.md (T6 +
  R93 census paragraph + CHECK G; lemma stays status: open)
- records/proof_erdos_gyarfas_28bac29a6d86_3289fa5.json (R93 record)
- proof_open_questions.jsonl, proof_journal.jsonl, notes channel

**CRITIC INFRA (standing, carried forward + s_0924 measurements)**:
prewarm ALL 7 critics BEFORE proof_prepare (call_critics_parallel,
timeout_s=1500). This container: cold parallel draw 185s, zero
timeouts. Re-roll taxonomy AGAIN confirmed: internal critic's first
draw was BLOCKING critic_unparseable (formatting, not math);
re-rolled clean on first try. GOTCHA: a use_cache=False call_critic
from a scratchpad script did NOT land in the cache row for the
harness-rendered prompt — after re-rolling, explicitly
_cache_store(sha_of_harness_prompt, name, resp) and verify with
_cache_lookup before re-running proof_prepare. CHECK suite: 136 ran,
0 failed, 1 pre-existing WARN timeout (cyclic_orbit_avg_size) on
this container. ~/.cache/auto-erdos does NOT survive the container
boundary. PROOF_TAG on the SAME command line for EVERY helper.
R-numbering by hand (next: R94).
