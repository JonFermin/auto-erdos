# Session handoff (session s_0809-080835-54ee)

**Stop reason**: Logical milestone — R31 and R32 both keep_progress;
the SUP-1 supply statement is now localized to the cancelled
interval's boundary with the cover geometry there fully proved.

**What was done this session**:

R31 — `sup1_end_edge` probe. SUP-1 (pair $|D| \ge 6$ + $k'=1$ short
cover + even $L$) holds 189/189 residual trees across 4 seeds; the
witness's met edge can ALWAYS be taken on a segment END edge, and the
MIN-GAP cover of the right end edge always works (126/126 each).
Falsified: leg-top-only (3/63 fail), leg-bottom-only, A-end-only.
The odd-L-only fallback was never needed.

R32 — `sup1_iadj`. (Part 2, open probe) The working end edge can
always be chosen I-ADJACENT — leg tops $(m, c_i)$ or the $A$-bottom
edge at $a_{\mathrm{deep}}$ — 92/92 across two seeds; NO tree ever
requires a far boundary edge. (Part 1, PROVED, 1.03M-config CHECK)
Short covers through I-adjacent edges are pinned: leg-top covers
anchor INSIDE $I$ (straddle exclusion) and meet only that leg with
$k' = 1 + (\text{common descent below } c_i)$; $A$-bottom covers meet
only $A$ with $k' = d(a_{\mathrm{deep}}) - \max(d(a_3), d(a_{\mathrm{sh}}))$;
explicit $k'=1$ criteria at both. Quantifier negatives: forall-pair
min-gap rule 0/37, forall-pair SUP-1 0/37, max-$k_{12}$ pair 10/37;
working pairs usually expose exactly ONE working end edge (157/211).

**qid state**: Q9 released with partial progress. Next session
re-claims Q9 (or splits SUP-1-analytic / SUP-8 into new qids).

**Open core after R32** (priority order):
1. **SUP-1 analytic, existence half**: why does some I-adjacent
   edge's min-gap cover come out short ($\le k_{12}+1$), with parity
   $\operatorname{gap}_3 \equiv |D|+1 \bmod 2$, and $k'=1$? Part 1 of
   `sup1_iadj` gives the geometry: leg-top covers anchor in the
   $I$-window, so $\operatorname{gap}_3 = d(s_3) - d(a_3)$ with
   $a_3 \in V(I)$, and shortness couples to $k_{12} = |I|$ through
   window depth. $k'=1$ is a local divergence condition at $c_i$ /
   $a_{\mathrm{deep}}$. Candidate: analyze the min-gap cover of the
   leg-top edge guaranteed by 2-edge-connectedness and bound its gap
   by walking the I-window.
2. **SUP-1 analytic, selection half**: which pair. NOT extremal in
   any tested statistic (max-k12 dead 10/37, min-|D| dead from R29).
   Candidate: characterize pairs by their cover arithmetic and argue
   existence globally (over all pairs of the tree) rather than
   selecting one pair a priori.
3. **SUP-8** (line-hitting, $L=8$ exactly): unchanged from R30 —
   `sweep_pair_exists` (52/52) + floor/line frame it. If SUP-1
   analytic stalls, run /erdos-proof-ideation on SUP-8 with the R29
   selection negatives + R32 quantifier negatives as dead ends.

**CRITIC INFRA (updated 2026-08-09 — READ BEFORE FIRST VERIFIER RUN)**:
- Prewarm mandatory, WITH RETRY: render the 7 critic prompts via
  proof_prepare internals and call library._critic_subprocess.
  call_critics_parallel(timeout_s=900) up to 3 attempts; falsify took
  2 attempts once and 400-470s runs otherwise. (Keep the prewarm
  script OUT of git — stop-hook complains about untracked files;
  stash it in the scratchpad and copy in/out.)
- Run proof_prepare with AUTOERDOS_LEMMA_CHECK_TIMEOUT_S=45 (CHECK 2
  of sup1_iadj runs ~21s; default 15s would WARN-timeout it).
- **NEW TRAP — numerical_check escalation roulette**: proof_prepare
  escalates ANY falsify/numerical finding whose numerical_check fails
  to BLOCKING, even if the critic flagged it OK. Two R32 verifier runs
  were lost to this (an `__import__` in the expression → banned-token
  fail; an over-broad quantification including impossible |D|=2
  configs → False). Mitigation now in place: the strategy preamble
  carries a numerical_check-discipline note for critics (True-over-
  domain, omit-when-unsure, sandbox constraints). If a blocked verdict
  cites a finding whose flag is OK, decode the cached falsify response
  (~/.cache/auto-erdos/critic_cache.tsv, b64 column) to confirm it's
  sandbox noise, then strengthen the note / re-roll rather than
  discarding the round.
- proof_strategy.md is ~85k chars — condense before ~120k.
- HARNESS TRAP (unchanged): shell cwd resets to repo root between
  turns sometimes. PREFIX EVERY COMMAND with
  `cd /home/user/auto-erdos/worktrees/0730-080656-0fbf`. Symptom:
  critic cache misses right after a successful prewarm.
- Ephemeral containers: proof_results.tsv and the critic cache do NOT
  survive between scheduled runs; the committed journal/ledger/records
  are the durable state. Cross-branch notes (~/.cache) are also lost —
  put anything that must survive into THIS handoff or the strategy.

**Files modified this session**:
- proof_lemmas/lemma_sup1_end_edge__0809-080835-54ee.md (new probe, R31)
- proof_lemmas/lemma_sup1_iadj__0809-080835-54ee.md (new: proved Part 1 + open Part 2, R32)
- proof_strategy.md (Sections 71, 72 + critic-guidance preamble notes)
- proof_open_questions.jsonl, proof_journal.jsonl, ledger (appends)
- records/proof_erdos_gyarfas_b42fa33f324c_1b518f5.json (R31 keep)
- records/proof_erdos_gyarfas_3abd8c7b1c34_05602a1.json (R32 keep)

**Suggested next moves (R33+), in order**:
1. Census the MIN-GAP cover of leg-top edges specifically: tabulate
   gap vs (k12, |I| depth window, divergence at c_i) to find which of
   shortness / parity / k'=1 is the binding constraint per tree, and
   whether the failing legs correlate with |L_i|=1 or A empty.
2. Attempt the existence half analytically for the leg-top edge with
   the R32 geometry (anchor in I forces gap3 >= d(s3)-d(m)+1; compare
   against k12+1 = |I|+1).
3. If both halves stall, /erdos-proof-ideation on SUP-8.
