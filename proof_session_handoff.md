# Session handoff (session s_0915-080622-71a7)

**Stop reason**: logical milestone — two rounds, two keeps (R89:
s2/s2 catalog + antipodal participation law after a same-round
refutation of the draft placement law; R90: reuse law + T3 +
deterministic non-{3,8} family witnesses). The supply core is now
"companion supply" — strictly smaller than before.

**program**: arc-exchange (exploit; qid Q0905-082429-1 stays
claimed by this session's rows — re-claim or release explicitly
next session).

**Consecutive exploit sessions on current program**: 1
(s_0913 ended at 0 after its explore round; this session ran two
exploit rounds on arc-exchange with no explore round. At 2+ the
NEXT session must claim a kind: explore qid or open with ideation;
at 1 it MAY exploit once more, then must rotate.)

**What happened**:

1. **R89 (keep, 9fabf63 + revision)**: `template_placement` lemma
   opened. T1 proved: complete s2/s2 L3 span catalog under
   L1-lessness — EIGHT pairs ({3,4},{3,8},{4,7},{4,9},{7,8},
   {7,12},{8,9},{8,11}) from P1 offset-sum-7 + E2 + width bound.
   T2 proved: {3,4}'s unique realization is degenerate-sequential
   (hi1=lo2), hence itself an L2 — L2-lessness kills it. The DRAFT
   statement (every L1&L2-less menu carries the {3,8} template,
   n28r3 sole exception) was REFUTED the same round by the 5-seed
   walk (rng 91-95, 2,000 members, 36,364 landings, 3,046
   L2-less): families {3,8} 2,400 / {7,8} 256 / {8,9} 256 / empty
   134 — n28r3-stratum RECURS; H2 dead; fragility=L3-only dead
   (646 non-template L2-less menus have 4-5 pairs, not fragile).
   SURVIVED 100%: T1 catalog, trio coverage, family purity (never
   mixed), and the revised statement — antipodal participation:
   every s2/s2 pair in an L2-less menu contains a span-8 ear
   (2,912/2,912); every L2-less menu has an antipodal-ear valid
   pair (s in {2,3}; empty stratum rides shape ((.),(8,3,5))),
   single exception n28r3 (unique pair all-c=7). Sections 129 +
   addendum; refutations recorded — do NOT re-derive H2 or the
   fragility identity.

2. **R90 (keep, 794a04c)**: the REUSE LAW (open, 150/150): every
   valid non-antipodal s2/s2 pair in an L1-less menu has an ear
   that itself joins a valid L2 (9 corpus + 141 walk occurrences,
   no exception). T3 proved: non-antipodal pairs carry shortening
   multisets {2,5}/{2,7}/{5,10} — always an element of {2,5} —
   and the L2 companions (shortening 1 or -2) are E2-free.
   So statement (a) reduces to COMPANION SUPPLY: prove the
   shortening-1 (or -2) companion exists. CHECK C pins
   deterministic prefix-walk witnesses: empty family at rng-94
   n28r3-walk member 3; {7,8} AND {8,9} both first at rng-95
   n28r4-walk member 29 (seeds n24/n26/n28r1 never leave {3,8} in
   400 steps — the exotic strata are n28r3/n28r4-adjacent).
   Section 130.

**qid state**: Q0905-082429-1 claimed by s_0915 (this session) —
program continues. Q85, Q0905-082429-3 open. Stop criterion
(Section 127 extension note, restated Section 130): two further
critics-ON sessions without a proved supply lemma or a falsifying
landing => pivot to Q0905-082429-3. This session RESET that clock
(refutation landings found + T1/T2/T3 proved).

**Suggested next moves**:
1. R91 (exploit, one more allowed at counter 1): COMPANION SUPPLY
   for the {4,7} case — the walk's 46+7 realizations give
   per-position statistics of where the shortening-1 companion
   sits; try an E3-pigeonhole relative to the pair's occupied
   positions. Test bed: CHECK C's prefix walks.
2. The (8,3,5) floor of the empty stratum (Section 129 (b')):
   census WHY both empty-stratum shape-families carry an antipodal
   s=3 ear — spoke structure of those 134 menus.
3. If R91 stalls: rotate (counter hits 2) — claim Q0905-082429-3
   (triangle-cover) or run /erdos-proof-ideation.

**Files modified this session**:
- proof_strategy.md (Sections 129 + addendum, 130)
- proof_lemmas/lemma_template_placement__0915-080622-71a7.md (NEW,
  open: T1/T2/T3 proved, CHECK A/B/C)
- records/proof_erdos_gyarfas_c59d8394265e_9fabf63.json (R89)
- records/proof_erdos_gyarfas_ac10727d0ec9_794a04c.json (R90)
- proof_open_questions.jsonl, proof_journal.jsonl, ledger.jsonl

**CRITIC INFRA (standing, carried forward, s_0915 measurements)**:
prewarm ALL 7 critics BEFORE proof_prepare (cache replays);
prewarm.py rebuilt in scratchpad WITH the self-contradictory-OK
rule — NOW PRECISELY DEFINED: an OK/WARN finding from
numerical/falsify whose numerical_check fails _sandboxed_eval gets
escalated to BLOCKING by proof_prepare's _evaluate_numerical_findings
even though the critic passed it (R90 hit `(5 + 12 == 16)`, a
critic arithmetic typo, and a primitive-set-flavored stray check —
TWO bad draws in a row). Handling: parse each warmed response,
sandbox-eval its checks, and on contradiction re-call with
use_cache=False — CAUTION: use_cache=False also SKIPS the store,
so persist the clean response explicitly via _cache_store(sha,
name, resp) (newest entry shadows). Opus-4-7 latency this
session: falsify 369-448s with two 480s timeouts mid-session;
internal up to 443s; others 10-160s. proof_prepare warm replay
~185s. CHECK suite now 129 blocks (~13s), still 1 pre-existing
timeout (lemma_cyclic_orbit_avg_size). PROOF_TAG on the SAME
command line for EVERY helper; R-numbering by hand (next: R91).

