# Session handoff (session s_0912-080614-b899)

**Stop reason**: logical milestone — two rounds, two keeps (R85:
E1–E3 proved + fragile-8 census; R86: class walk, zero falsifiers
in a 20× expanded census, + E4 arc-triple law). Clean stopping
point: the supply conjecture is now heavily falsification-tested
and its provable perimeter is mapped; what remains is the genuine
position-compatibility core.

**program**: arc-exchange — continuation window session 4.

**Consecutive exploit sessions on current program**: 0
(this session re-claimed Q0905-082429-1, kind: explore, so k stays
0 by the letter of the rule — BUT this was the FOURTH consecutive
session riding that one explore qid. The spirit of Variance policy
§2 is no longer served by another bare re-claim: the NEXT session
should rotate to Q0905-082429-2 (mod-4 invariant program;
Dean–Lesniak–Saito literature check is its committed STEP 0) or
Q0905-082429-3 / Q85, or re-enter the d=1 supply line only through
a fresh ideation pass that re-ranks it against the alternatives.)

**What happened**:

1. **R85 (keep, 8f39a23)**: three proofs added to
   `c16_d1_ear_cover` — (E1) interiority is free (f1/f2 carry no
   spokes in H, every ear lands in positions 1..14); (E2) the ONE
   ear exclusion law c+s ∉ {4,8} (all C4/C8 obstruction on menus;
   corollaries: s=2 gaps avoid {2,6,10,14}, odd shortenings —
   including L1's 3 — are never obstructed); (E3) supply floor
   (≥12 spokes on ≤11 outside vertices ⇒ every menu has an s=2
   ear). Falsification-first census: exactly 8 fragile landings
   (7 L3-only + hidden L2-unique (n28r4,2,20,12,11,21,22)), each
   with exactly 2 critical ears; pinned as CHECK 2. Section 125.

2. **R86 (keep, ff0d16b)**: seeded 2-edge-swap walk INSIDE the
   class from the 5 fragile hosts: 1,690 new class members, 31,377
   legal d=1 landings, ZERO menus missing L1/L2/L3 (partition
   24,930 / 4,544 / 1,903 — the 6% else-L3 share shows genuinely
   thinner menus than the corpus). Trimmed slice pinned as CHECK 5
   (66 members / 2,376 landings, ~2s). Fragile-8 anatomy: critical
   ears ride 3-spoke vertices in 6/8 cases. (E4) proved: 3-spoke
   arc triples (x,y,z), x+y+z=16, each ∉ {2,6,10,14}; exactly 7
   admissible triples, all realized; 6 of 7 contain an arc in
   {3,4,5} (direct small-shortening ear), unique exception (1,7,8)
   with shortenings {-1,5,6}. Tri-only mining: of the 53 landings
   with only triangle s=2 ears, 45 are L1 via s≥3 ears — the s≥3
   fallback branch is real. Section 126.

**qid state**: Q0905-082429-1 released at this session_end with a
rotation flag (see above). Q85, Q0905-082429-2, Q0905-082429-3
unchanged.

**Suggested next moves**:
1. ROTATION (default): Q0905-082429-2 — mod-4 invariant program.
   STEP 0 is the Dean–Lesniak–Saito-type literature check ("every
   graph with min degree ≥3 has a cycle ≡ 0 mod 4" — this may be a
   known theorem; if so, mine the technique, do not re-prove).
2. If continuing d=1 supply DESPITE the flag (via ideation only):
   the open core is now precisely stated — produce a shortening-3
   ear or a compatible pair from: every menu has an s=2 ear (E3),
   3-spoke vertices supply small shortenings unless triple
   (1,7,8) (E4), tri-only menus get L1 from s≥3 ears empirically.
   Attack: the 2-spoke gap dichotomy (Section 126 next-moves (a)) —
   prove triangle-heavy menus force adjacent-spoke chains into
   longer small-shortening ears.
3. d=2 row (chord not free; 90 multi-dip landings) after d=1.

**CRITIC INFRA (standing, carried forward)**: prewarm ALL 7
critics BEFORE proof_prepare (cache replays); prewarm.py rebuilt
in scratchpad per the s_0910 recipe WITH the self-contradictory-OK
rule (reject a cached candidate if an OK-flagged finding's
numerical_check evaluates False — falsify hit this on BOTH R85 and
R86 prewarm attempts 1; one retry fixed it each time). Genuine
WARN/BLOCKING findings with failing checks are real — keep them.
Finish ALL proof_lemmas/ edits BEFORE launching prewarm
(strategy+falsify embed the lemma corpus). PROOF_TAG on the SAME
command line for EVERY helper; cwd resets between shell calls.
R-numbering by hand (next: R87). Timings this session: prewarm
568s/1072s (falsify retry doubles it), proof_prepare ~175s warm,
lemma CHECK block now ~3.4s (CHECKs 1+2+5). proof_notes.py is
CACHE-DIR-backed and DIES with the container — durable insights go
in strategy sections + this handoff.

**Files modified this session**:
- proof_strategy.md (Sections 125, 126)
- proof_lemmas/lemma_c16_d1_ear_cover__0910-080911-1f4a.md
  (E1–E4 proved blocks, fragility + extended census prose,
  CHECK 2 and CHECK 5 added; CHECK block ~3.4s total)
- records/proof_erdos_gyarfas_6651179ba9e2_8f39a23.json (R85)
- records/proof_erdos_gyarfas_4d9e99ab728a_ff0d16b.json (R86)
- proof_open_questions.jsonl, proof_journal.jsonl
