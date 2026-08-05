# Session handoff (session s_0805-080844-5fb3)

**Stop reason**: Logical milestone — R23 + R24 both keep_progress; token
budget spent on critic-infra recovery.

**Current focus**: Q9 — pasting-existence for pair-residual trees. After
R23 (tuning skeleton) + R24 (meeting structure proved), the open core is:
(1) vertex-automatic conjecture, (2) T1/T2/T3 tuning proofs, (3) the two
standing hypotheses (2-connectedness reduction; no all-even/all-odd
pair-residual trees).

**What was done this session**:

R23 — `pasting_value_interval` (open probe, unfalsified):
- Census over 192k trees (n=12–22): every one of 50 pair-residual trees
  has 8 in its pasting value set V(T) = {|D|+gap3+1-2k'}, and the even
  part V_e is a gap-free step-2 interval; v_min ∈ {4,6,8}, v_max ∈
  {10..18} growing with n. Tuning reduced to: (T1) interval-ness via ±2
  local moves, (T2) some even L ≤ 8, (T3) some even L ≥ 8.
- proof_strategy.md Sections 2–18 CONDENSED to a digest (full text at
  commit 9e2eb14 and in strategies/erdos_gyarfas/). This was necessary:
  the assembled critic prompt hit ~180k chars and the internal/falsify
  critics exceeded the fixed 240s timeout.
- Critic-flagged gaps now documented in-artifact: the 2-connectedness
  REDUCTION GAP (blocks of min-deg-3 graphs need not be min-deg-3; the
  minimal-counterexample-is-2-connected surgery is unproven), the
  empirical-only "pair-residual ⊆ mixed-parity" assumption (an all-even
  pair-residual tree would have NO rescue route — ruling those out is
  load-bearing), and in-repo provenance for Moore/DFS facts.

R24 — `pasting_meeting_structure` (proved):
- E(D) ∩ tree = A ⊔ L1 ⊔ L2 (anchor interval above lca(s1,s2) + two
  legs below it); P3 meets each in a contiguous interval, at most 2 of 3
  nonempty; D ∩ C3 is a single path (pasting hypothesis) IFF exactly one
  is nonempty and carries all shared vertices. 167k triples, 0
  violations.
- BONUS: the stray-vertex condition held automatically in 92,894/92,894
  single-nonempty configs → "vertex-automatic" conjecture: in cubic DFS
  trees, one-nonempty-segment alone implies pasting. If proved, meeting
  existence reduces to: some even-gap back edge covers a tree edge of
  exactly one segment (coverage of every tree edge is guaranteed by
  mixed_overlap_supply(1) in 2-connected graphs).

**qid in flight**: Q9 released with partial progress. Next session
re-claims Q9.

**Suggested next moves (R25+), in order**:
1. Prove vertex-automatic (cubic): a stray shared vertex v of D and C3
   off the meeting interval needs ≥ 2 of its ≤ 3 incidences on D and
   ≥ 2 on C3-but-not-D-edges — count incidences at v; cubic should
   forbid it. Write the CHECK census per stray-vertex type first.
2. T3 (some even L ≥ 8): min-overlap config k'=1 with gap3 ≥ 5 (gaps
   avoid {3,7,15,31} and |D| ≥ 3 odd ⇒ L = |D|+gap3-1 ≥ 8 unless
   |D|+gap3 ≤ 8 — enumerate the few small cases).
3. T2 (some even L ≤ 8): same-sender mixed pair at a leaf gives |D| =
   |g1-g2|+2 with k' up to the inner gap; quantify.
4. T1 (interval): define the config graph (slide meeting interval by one
   edge / swap B3 to the covering back edge of the adjacent tree edge)
   and show moves change L by ±2 and connect the config space.
5. The 2-connectedness reduction lemma and the all-even/all-odd
   exclusion (Section 30 standing hypotheses) are still open and
   load-bearing for the final assembly.

**CRITIC INFRA (important for next session)**: the internal and falsify
critics time out at the hard-coded 240s when the assembled prompt is
large; ledger/numerical/sign intermittently fail fast with 'claude -p
exited 1 after ~3s' (transient; retry after ~60s). WORKING RECIPE: call
library._critic_subprocess.call_critics_parallel directly with
timeout_s=1200 and use_cache=True on the EXACT rendered prompts
(proof_prepare._render_critic_prompt) to pre-warm the cache, retrying
failures in a loop; then run proof_prepare.py, which replays everything
from cache in ~80s. Also: the numerical_check sandbox has no frozenset
(a harness note is now in proof_strategy.md Section 1 so critics write
set()-based checks).

**Files modified this session**:
- proof_lemmas/lemma_pasting_value_interval__0805-080844-5fb3.md (new, open probe)
- proof_lemmas/lemma_pasting_meeting_structure__0805-080844-5fb3.md (new, proved)
- proof_strategy.md (Sections 2–18 condensed; Sections 30, 31 added;
  Section 21 caveat; Section 29 reduction-gap note + spelled-out
  low-point step; Section 1 harness note)
- notes channel appended
