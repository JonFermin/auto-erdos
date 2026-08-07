# Session handoff (session s_0807-081112-b59a)

**Stop reason**: Logical milestone — R27 + R28 both keep_progress; the
R23 pigeonhole program (T1/T2/T3) is collapsed to a single existence
statement, and the censuses that justify the collapse are committed as
falsification probes.

**What was done this session**:

R27 — `t3_min_overlap_short_paste` (probe, open, unfalsified 62/62 at
192k trees): every pair-residual tree admits a config with k'=1,
gap3 <= k12+1, |D|+gap3 >= 9 odd — even L >= 8 inside the position-free
provable class. V_e never empty, never subset of {6}. ONE tree needed
the even-|D|/odd-gap3 family — the analytic argument must cover both
parity families; mixed-parity supply alone is not enough.

R28 — `tune8_short_paste` (probe, open, unfalsified 51/51 at 192k
trees, seed 20260807+28): every pair-residual tree admits a config with
gap3 <= k12+1 and |D|+gap3+1-2k' = 8 EXACTLY — so 8 in V(T) directly,
no interval-ness, no endpoints. k'=1-only variant FALSIFIED (3/51);
same-sender-only supply FALSIFIED (1/51). T1/T2/T3 demoted to fallback.

**qid in flight**: Q9 released with partial progress. Next session
re-claims Q9.

**Open core after R28** (in priority order):
1. ANALYTIC target: prove tune8_short_paste — exists pair (single-cycle
   D, overlap k12) + cover B3 with gap3 <= k12+1, D∩C3 a single path of
   k' edges, |D|+gap3 = 7+2k'. Candidate route (Section 68): from any
   single-cycle pair, enumerate covers of D's tree edges (guaranteed by
   2-edge-connectedness), show the value map B3 -> |D|+gap3-2k' sweeps
   wide enough to hit 7. A useful pre-census: per-tree, is the short-
   paste value set S(T) = {|D|+gap3-2k'} an interval? Which pairs
   contribute the 7? If stuck, run /erdos-proof-ideation.
2. Standing hypotheses (unchanged): 2-connectedness reduction
   (Section 29); all-even/all-odd pair-residual exclusion (Section 30);
   cubic -> min-degree-3 reduction (vertex-automatic sharp at deg 3).

**CRITIC INFRA (still true 2026-08-07)**: pre-warm the critic cache
before proof_prepare.py (script pattern: render via
proof_prepare._render_critic_prompt with witness_valid=0, then
library._critic_subprocess.call_critics_parallel(items, timeout_s=1200,
use_cache=True), retry loop; then proof_prepare.py replays from cache).
Full critic pass ~7 min wall (falsify is slowest, ~5-7 min). Keep
proof_strategy.md near ~60-70k chars. RUN FROM INSIDE THE WORKTREE —
the shell cwd resets to the repo root between commands; a prewarm run
from the root renders master's strategy and warms nothing.

**Files modified this session**:
- proof_lemmas/lemma_t3_min_overlap_short_paste__0807-081112-b59a.md (new probe)
- proof_lemmas/lemma_tune8_short_paste__0807-081112-b59a.md (new probe)
- proof_strategy.md (Sections 67, 68)
- proof_open_questions.jsonl, proof_journal.jsonl, ledger, notes (appends)
- records/proof_erdos_gyarfas_15eff97c58a0_8183d8c.json (R27 keep)
- records/proof_erdos_gyarfas_998c92aff0e0_5ad3a55.json (R28 keep)

**Suggested next moves (R29+), in order**:
1. Pre-census for the analytic route: per residual tree, tabulate
   S(T) = {|D|+gap3-2k' : short-paste configs} — interval? which pair
   shapes contribute 7? Then attempt the sweep argument.
2. If the sweep argument stalls, /erdos-proof-ideation on the exact-
   tuning statement with the two falsified variants as dead ends.
3. Periodically re-run the tune8 census at n in {24..32} (verifier cap
   is n <= 64) to stress the claim where the witness box lives.
