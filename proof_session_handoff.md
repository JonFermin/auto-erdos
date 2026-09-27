# Session handoff (session s_0927-080724-6eee)

**Stop reason**: logical milestone — TWO keeps in one session (R98,
R99), the non-antipodal s2/s2 catalog fully resolved at n=24, and a
program-level law refuted by an explicit new graph.

**Consecutive exploit sessions on current program**: 0
(this session ran the mandated EXPLORE rotation: both rounds on the
kind: explore qid Q0905-082429-1, re-claimed legally after the
s_0925+s_0926 rotation away. The quota is fully discharged; the next
session may exploit freely.)

**What happened (Sections 136–137; lemmas `c16_712_exclusion` and
`c16_nonantipodal_n24_resolution`, both proved; records
proof_erdos_gyarfas_6157c3e5f8e6_2b1eeb6.json and
proof_erdos_gyarfas_3844fb1bc897_9af4bb2.json)**:

R98 (keep, 2b1eeb6): executed Section 133's pre-committed move (b).
NEW METHOD for the program: pinned-configuration completion
enumeration — {7,12} has width 13, zero translational freedom, so
realizability at fixed n is a finite exact-degree decision. Results:
{7,12} is width-13-pinned (2 mirror realizations), third-foot-rigid
(w1 menu {4,5,9,12}, w2 menu {3,6,10,13} by PURE C4/C8 arithmetic —
the machine found cross-C8 kills the hand pass missed; only 6 of 16
double-third pairs survive, p=12 dies against everything), and DEAD
at n=24 UNCONDITIONALLY (173,090 completions, zero legal — no
L1/L2 hypothesis needed). Also this round: the mod-4 external
citation quarantine COMPLETED (statement content now lives ONLY in
lemma_mod4_even_theta; Section 127 keeps a pointer + named
antecedent A-DLS) — the ledger critic's every-other-draw re-raise
came back CLEAN twice after this; treat as closed.

R99 (keep, 9af4bb2): the same sweep per translate over {4,9} and
{4,7}. {4,9}: DEAD at n=24 unconditionally (all 4 translates UNSAT).
{4,7}: trichotomy — lo=3,5 UNSAT, lo=1,2,4 SAT with explicit
completions. THE HEADLINE: the lo=4 completion W24 (explicit 36-edge
list in the lemma's CHECK D) is a NEW n=24 class member (6 triangles
vs adj24's 7, spider24's 3 — 3rd n=24 member, 20th of the class)
whose legal d=1 landing menu is L1&L2-less yet contains the valid
non-antipodal {4,7} pair {(4,8,2),(6,13,2)} — REFUTING
template_placement's participation law (a). Its (b) SURVIVES: W24's
only other valid L3 pair is the antipodal TEMPLATE {3,8}. W24 was
independently re-verified via networkx (cycle census 3:6/5:2/6:4/7:2
below 8, ear-for-ear menu agreement). Refutation record written into
lemma_template_placement.

**INFRA (critic pass, durable)**: the falsify critic times out at
the harness's fixed 240s on fresh prompts here. The WORKING prewarm
is: render the critic prompt with proof_prepare._render_critic_prompt
and call library._critic_subprocess.call_critic(prompt,
critic_name=..., timeout_s=1500) BEFORE proof_prepare — the response
lands in the shared cache and the harness replays it. Prewarm
falsify AND internal (both have timed out); a bare `claude -p warm`
is NOT sufficient. Also: ~/.cache/auto-erdos is EPHEMERAL in cloud
containers — proof_notes.py content does NOT survive; the committed
handoff + strategy are the only durable channels.

**qid state**: Q0905-082429-1 released with continuation plan
(program CONTINUES, healthy — 2 keeps). Q81, Q85 released
(background). Exploit counter 0.

**Suggested next moves** (Section 137 has the full list):
1. **W24 taxonomy**: compute its branch-vertex profile (k,
   c(H)-mu(H)) and reconcile with the R96/R97 k=1 EXACT
   classification (W24 must be k!=1 or expose a gap — either answer
   matters). Census its chordless C16s. adj24/spider24 edge lists
   are in the R97 lemma; W24's is in
   c16_nonantipodal_n24_resolution CHECK D.
2. **Retarget the placement program at (b)** (antipodal-pair
   EXISTENCE): at n=24 it may be decidable by the same completion
   enumeration over the L1&L2-less landing families of all three
   n=24 members.
3. **{4,7} SAT-family census at n=24**: enumerate ALL completions
   of the three SAT translates (not first-found), classify up to
   iso, count refuting landings. Cheap (~6s per translate).
4. **n=26 {7,12} decision**: the naive |O|=7 enumeration does NOT
   scale (killed after 1h). Needs case-splitting on t/e(O) or
   orderly generation before it fits CHECK budgets.

**Files modified this session**:
- proof_strategy.md (Sections 136, 137; Section 127 literature
  passage replaced by quarantine pointer; consequences items 2-3
  rewritten against named antecedent A-DLS)
- proof_lemmas/lemma_c16_712_exclusion__0927-080724-6eee.md (NEW,
  proved, 4 CHECKs)
- proof_lemmas/lemma_c16_nonantipodal_n24_resolution__0927-080724-6eee.md
  (NEW, proved, 9 CHECKs)
- proof_lemmas/lemma_template_placement__0915-080622-71a7.md
  (R99 refutation record prepended; (a) dead, (b) live)
- records/proof_erdos_gyarfas_6157c3e5f8e6_2b1eeb6.json,
  records/proof_erdos_gyarfas_3844fb1bc897_9af4bb2.json
- proof_open_questions.jsonl, proof_journal.jsonl, ledger

**For maintainer (standing, unchanged)**: promote Dean–Lesniak–Saito
1993 (and optionally Choi–Chu 2026) to given_facts F4/F5 in
proofs/erdos_gyarfas.json; update lemma_mod4_even_theta's quarantine
CHECK in the same commit.
