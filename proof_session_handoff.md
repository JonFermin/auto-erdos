# Session handoff (session s_0806-081011-9409)

**Stop reason**: Logical milestone — R25 + R26 both keep_progress; the
meeting half of Q9 is now FULLY proved (structure + vertex-automatic +
cover dichotomy). Token budget reserved for clean close.

**Branch state note**: this session merged origin/master (commit
18fc918) — the sibling depth-census line (PR #37) is now visible here —
and re-condensed the strategy narrative (Sections 19–57 → digest) to
keep the critic prompt inside its timeout budget. Live argument:
Sections 58–65 + live Sections 26–31 (R19–R24) + Sections 65–66.

**What was done this session**:

R25 — `pasting_vertex_automatic` (PROVED; was the R24 open conjecture):
- Two cycles of a subcubic graph sharing a vertex share an edge at that
  vertex (each uses 2 of the ≤3 incident edges; 2+2>3 pigeonhole).
- Hence no stray shared vertices when exactly one segment is met, and
  the pasting criterion collapses to: D ∩ C3 is a single path IFF P3
  meets exactly one of A, L1, L2 in an edge (k' = interval length).
- Sharp at degree 3; min-degree-3 non-cubic graphs NOT covered (the
  cubic reduction stays on the Section 29 gap list).

R26 — `pasting_cover_dichotomy` (PROVED) + census:
- Every cover of a tree edge of D either PASTES (one segment met) or
  STRADDLES: meets A + exactly one leg, P3 ⊇ I = [a_deep..m], anchor
  strictly above a_deep, sender strictly below m in the met leg's child
  subtree, P3∩A contains A's deepest edge, P3∩L_i contains (m, c_i),
  and gap3 ≥ k12+2.
- Paste criteria (contrapositives): gap3 ≤ k12+1, or anchor at/below
  a_deep, or sender at/above m ⇒ the cover pastes.
- CENSUS (important NEGATIVE): per-PAIR existence fails — over
  2-edge-connected cubic samples, ~3% of single-cycle pairs have NO
  pasting cover and ~16% no EVEN-gap pasting cover. T2/T3 and
  meeting-existence MUST be quantified per-tree ("some pair admits an
  even-gap pasting cover"), matching pasting_value_interval's per-tree
  census. Do NOT burn a round on per-pair existence.

**qid in flight**: Q9 claimed by this session; released with partial
progress at close. Next session re-claims Q9.

**Open core after R26** (tuning program, in priority order):
1. T3 (some even L ≥ 8 in V(T), per-tree): refined form — rule out
   V_e ⊆ {6} (if 4 ∈ V the tree fires anyway). Use the paste criteria:
   short covers (gap3 ≤ k12+1) paste with L = |D| + gap3 + 1 - 2k'.
   Note L even ⟺ |D|+gap3 odd — BOTH (odd |D|, even gap3) and
   (even |D|, odd gap3) contribute; the second family (same-parity
   pairs with |D| even ∉ PO2, odd-gap third) is so far unexploited.
2. T2 (some even L ≤ 8 per-tree): same-sender / leaf-pair mixed configs
   give small |D|; quantify with the dichotomy.
3. T1 (V_e interval-ness): config-graph ±2 moves. The k' freedom comes
   from different B3 choices; R26's structure (straddle covers pin the
   met interval to contain A's deepest edge / leg's top edge) may give
   the slide moves.
4. Standing hypotheses (load-bearing): 2-connectedness reduction
   (Section 29); all-even/all-odd pair-residual exclusion (Section 30).
   Note: bipartite G forces all gaps odd (depth-parity coloring), so
   all-even needs non-bipartite G; a pure counting obstruction was
   checked this session and does NOT exist (3|V0| = n-1+2b0 is
   consistent) — the exclusion must use the residual property, not
   counting alone.

**CRITIC INFRA (still true 2026-08-06)**: pre-warm the critic cache
before proof_prepare.py: render prompts via
proof_prepare._render_critic_prompt (witness_valid=0), call
library._critic_subprocess.call_critics_parallel(items, timeout_s=1200,
use_cache=True) in a retry loop, THEN run proof_prepare.py (replays
from cache). Keep proof_strategy.md near ~60k chars — the merge had
re-inflated it to 300k which would have broken the 240s per-critic
timeout again. numerical_check sandbox has no frozenset/bin (Section 1
note).

**Files modified this session**:
- proof_lemmas/lemma_pasting_vertex_automatic__0806-081011-9409.md (new, proved)
- proof_lemmas/lemma_pasting_cover_dichotomy__0806-081011-9409.md (new, proved)
- proof_strategy.md (merged origin/master; Sections 19–57 condensed to
  digest; Sections 65, 66 added; R24 table updated)
- proof_open_questions.jsonl, proof_journal.jsonl, ledger (appends)

**Suggested next moves (R27+), in order**:
1. T3 refined (rule out V_e ⊆ {6} per-tree): write the CHECK census
   first (dual attack) — over pair-residual trees, tabulate which pairs
   realize even L ≥ 8 and via which paste criterion; then try: if some
   mixed pair has |D| ≥ 5 or admits a paste cover with gap3 ≥ 4, L ≥ 8
   arithmetic; enumerate |D|=3 & gap3=2 exhaustively.
2. T2 via leaf-pair / same-sender configs (|D| = |g1-g2|+2 small).
3. T1 config-graph moves.
4. If stuck, run /erdos-proof-ideation for fresh lenses on the
   standing hypotheses (Section 30).
