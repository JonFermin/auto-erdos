# Session handoff (session s_0922-080602-4fe4)

**Stop reason**: logical milestone — one round (R91), one keep.
The round proposed two sharpenings from the rng-94 census
(companion supply law: pilot route always; E4-typing: pilot on
(1,3,12), long ear on (1,7,8)), proved T5 (the pilot host's own
gap-3 ear is self-blocked as L2 companion), then the fresh-seed
hunt (rng 96-98 x 1,200 steps from n28r3) REFUTED the pilot-route
law (74 failures, all {4,9}), the {4,9} pilot typing (960 2-spoke
pilots), and the route asymmetry — while the R90 reuse law,
statement (a), the {4,7} pilot typing, and the long-ear (1,7,8)
typing SURVIVED all 5,744 occurrences (a 40x census expansion).

**program**: arc-exchange (exploit; qid Q0905-082429-1 stays
claimed by this session's rows — re-claim or release explicitly
next session).

**Consecutive exploit sessions on current program**: 2
(s_0915 ran exploit -> 1; this session ran one exploit round ->
2. The NEXT session MUST claim a kind: explore qid — Q85 or
Q0905-082429-3 — or open with /erdos-proof-ideation and claim one
of its explore qids, BEFORE any exploit round.)

**What happened (Section 131 + addendum; lemma
template_placement revised in place)**:

1. R91 (keep, 8a818be; record
   records/proof_erdos_gyarfas_fc45bcf12685_8a818be.json).
   Mining: per-occurrence companion statistics over the 5-seed
   walk, then vertex/host-level typing, then the fresh-seed hunt.
   Survivors are the load-bearing facts: EVERY long ear of a
   non-antipodal pair rides a (1,7,8) 3-spoke host
   (5,744/5,744, all seeds); reuse law and statement (a) at zero
   violations; {4,7} pilots all on (1,3,12). The supply core is
   now the ROUTE DISJUNCTION: pilot route (disjoint sequential
   shortening-1 companion; 5,670/5,744) OR long route
   (shortening -2/-4 companion; rescues all 74 pilot failures).
   T5 (proved): the pilot triple's own gap-3 ear shares the host
   vertex, so it can never be the companion — this is the
   observed failure mechanism at the pinned witness.
   CHECK D (rng-94 prefix witnesses, members 90/92), CHECK E
   (host typing + T5 + supply on the prefix), CHECK F (STATIC
   member-164 falsifier graph: pilot route fails, (7,-4) route
   rescues) all pass, ~5.5s total added to the suite.

2. Ledger discipline hardening (same round, commit 8a818be):
   a strict ledger-critic draw blocked on Section 127's (R87)
   external mod-4 citations. Reworded title + verdict + items to
   claim-quoting form ("reportedly"), retirement grounded on
   internal evidence alone. The subsequent draw returned [] —
   keep this phrasing style for ALL external literature.

**qid state**: Q0905-082429-1 claimed (this session). Q85,
Q0905-082429-3 open — both are the natural explore claims for the
mandated rotation.

**Stop-criterion clock**: critics-ON session ONE of two without a
proved supply lemma since the R89/R90 reset (T5 is an obstruction
proof, not the supply lemma; refutation landings were found, but
the clock language in Section 130 counts proved-supply-or-
falsifying-landing — the fresh-seed refutations of R91's OWN
sharpenings arguably reset nothing). One more critics-ON session
without a proved supply lemma or a falsifying landing => pivot to
Q0905-082429-3 (which is also the explore rotation target — the
two pressures point the same way).

**Suggested next moves**:
1. MANDATORY: claim an explore qid (Q0905-082429-3
   triangle-cover, or Q85), or run /erdos-proof-ideation.
2. When arc-exchange resumes: prove the route disjunction from
   the surviving anchor (long ear always on a (1,7,8) host); the
   member-164 configuration (CHECK F) is the hard case — pilot
   route dead by T5 self-block, (7,-4) rescue present.
3. Falsification frontier: a non-antipodal pair where BOTH routes
   fail. Hunt deeper (seeds >98, longer walks, n28r4 starts)
   before spending proof effort on the disjunction.

**Files modified this session**:
- proof_strategy.md (Section 131 + addendum; Section 127 ledger
  hardening)
- proof_lemmas/lemma_template_placement__0915-080622-71a7.md
  (companion supply + E4-typing sections with refutation record,
  T5, CHECKs D/E/F)
- records/proof_erdos_gyarfas_fc45bcf12685_8a818be.json (R91)
- proof_open_questions.jsonl, proof_journal.jsonl, notes channel

**CRITIC INFRA (standing, carried forward + s_0922 measurements)**:
prewarm ALL 7 critics BEFORE proof_prepare (cache replays; warm
replay ~227s incl. ~25s CHECK suite). The self-contradictory-OK
re-roll rule now has a sharper failure taxonomy: (a) checks using
`sorted`/`frozenset` ALWAYS fail _sandboxed_eval (not in
safe_builtins) — a NameError contradiction says nothing about the
math; (b) genuine critic arithmetic typos; both need a re-roll
with use_cache=False + explicit _cache_store (newest shadows).
Falsify clean-draw rate this session ~1/4 (one 780s and one 900s
timeout across ~8 calls; latency 370-900s). LEDGER critic draws
vary in strictness: R87's external citations passed R89/R90's
draws but blocked here until reworded to claim-quoting. PROOF_TAG
on the SAME command line for EVERY helper; R-numbering by hand
(next: R92).
