---
name: erdos-deep-autoresearch
description: Use when the user asks to run many parallel autoresearch experiments on the SAME problem to explore a wider hypothesis space — "deep autoresearch", "N parallel runs on capset_n8", "fan out 5 agents on sidon_3000", "deep dive on capset_n9", "run a bunch of experiments on capset_n10". Spawns N general-purpose subagents, all with the same PROBLEM_TAG but distinct pre-assigned MMDD-HHMMSS tags, each executing the full `erdos-autoresearch` skill (20-trial loop) in its own git worktree. Cross-branch AST dedup is already handled by `log_result.py`'s shared per-problem trial cache, so parallelism is safe by construction.
---

# erdos-deep-autoresearch

Parallelize the `erdos-autoresearch` skill **within a single problem**. Sister skill to `erdos-autoresearch-all` (which fans across problems, one agent each). Here we fan N agents across one problem to explore a wider hypothesis space — total effective trials = 20 × N, cross-branch AST-deduped via the shared `~/.cache/auto-erdos/trial_cache_<PROBLEM_TAG>.tsv`.

Each subagent runs the full `erdos-autoresearch` loop and archives to its own branch on origin.

## Arguments

Parse from the invocation:

- **Problem** (required). Accepts `capset_n8`, `sidon_3000`, etc. Verify `problems/<tag>.json` exists. Default `capset_n8` if nothing named.
- **N** (default `5`, clamp to `[2, 12]`). Number of parallel subagents. Each runs a 20-trial branch.
- **Cap override** (optional). If the invoker says "deep + tall" or passes `TRIAL_CAP=<n>`, export `AUTOERDOS_TRIAL_CAP=<n>` in every subagent's environment. Leave unset by default — 20 × N is usually plenty given that AST collisions rise as the cohort fills the cache.

If either is ambiguous ("run a bunch of experiments on capset_n9" → N unclear), pick a reasonable default (N=5) and state it explicitly in the ack before spawning.

## When deep is and isn't worth it

Tell the human in one sentence before spawning:

- **Worth it on**: open-LB problems where the search space is huge and the LB is decades old (`capset_n9`, `capset_n10`, `sidon_500`, `sidon_1000`, `sidon_3000`). N parallel agents widen the hypothesis-axis coverage rather than re-trying the same greedy 20×N times.
- **Not worth it on**: exact-known sanity-check problems (`capset_n4`, `capset_n5`, `capset_n6`, `sidon_100`). The LB is the answer; deep just runs more null controls. If the human really wants this, do it — but say once that 0 keeps is the only correct outcome.
- **`capset_n8` is borderline**: it's the default and well-trodden but still has open upper bound. Deep is fine, just temper expectations.

## Parallelism tradeoffs the invoker should know

State these once, in one or two sentences, before spawning — not after.

- **AST collision rate rises with N.** All N agents explore ideas against the same shared cache. With N=5 on a problem like `capset_n8` (which has been explored in prior runs), expect 10–25% of trials to hit exit 3 (AST duplicate) — the agent resets and tries a different hypothesis. Not wasted, but counts against the 20-trial cap.
- **API concurrency.** N subagents run concurrently. Each is a full Claude loop doing edits + verifier runs. Don't set N > ~8 without reason — diminishing returns once AST collisions dominate. The verifier itself is cheap, so wall-clock isn't the bottleneck (unlike the parent quant repo's longer backtests); subagent token cost is.

## Step 1 — Preflight

From the repo root (main checkout):

```bash
git status                                    # should be clean-ish (worktrees/ is gitignored)
git rev-parse --abbrev-ref HEAD               # note the starting branch; worktrees branch from master
ls "problems/<problem>.json"                  # confirm the requested problem exists
grep -q '^worktrees/' .gitignore && echo ok   # required — else parallel worktrees pollute main tree
```

**Missing problem JSON** — stop; the human has mistyped the problem or it doesn't exist yet.

There is no external data cache to download — the verifier is bundled in `prepare.py` and runs in-process. So preflight is fast.

## Step 2 — Assign unique tags

The `erdos-autoresearch` skill requires each run to have a unique numeric `MMDD-HHMMSS` tag, and two concurrent runs with the same tag collide on the worktree path. Pre-assign N tags with second-offsets, then verify against all three collision surfaces (sister CC instances may also be running):

```bash
git fetch origin --prune                          # so origin-ref check sees sister-instance branches
BASE_EPOCH=$(date +%s)
N=5                                               # replace with actual N
TAGS=()
for i in $(seq 0 $((N-1))); do
  TAGS+=("$(date -d "@$((BASE_EPOCH + i))" +%m%d-%H%M%S)")
done

COLLIDED=()
for TAG in "${TAGS[@]}"; do
  if git branch --list "erdos-research/$TAG" | grep -q .; then COLLIDED+=("$TAG(local)"); fi
  if [ -d "worktrees/$TAG" ]; then COLLIDED+=("$TAG(worktree)"); fi
  if git ls-remote --heads origin "erdos-research/$TAG" 2>/dev/null | grep -q .; then COLLIDED+=("$TAG(origin)"); fi
done
if [ ${#COLLIDED[@]} -gt 0 ]; then
  echo "COLLISION: ${COLLIDED[@]} — add 30s to BASE_EPOCH and retry"
  exit 1
fi
```

If any collision, bump `BASE_EPOCH=$((BASE_EPOCH + 30))` and regenerate. Do not drop the seconds suffix.

## Step 3 — Spawn parallel subagents

Spawn N `general-purpose` subagents in a single message (multiple Agent tool calls in one response so they launch concurrently). All agents use the SAME `PROBLEM_TAG`; each gets a distinct pre-assigned timestamp tag.

Required prompt content per subagent (identical template for all N — only `TAG` varies):

- Path to the skill: `C:/Users/honsf/DEVELOP/auto-erdos/.claude/skills/erdos-autoresearch/SKILL.md` — read in full before starting.
- Working directory: `C:\Users\honsf\DEVELOP\auto-erdos`.
- `PROBLEM_TAG=<problem>` — must be exported on every invocation of `strategy.py`, `log_result.py`, `running_best.py`, `prepare.py`.
- The **pre-assigned** timestamp tag. State explicitly: "do not generate your own tag — it's been pre-assigned to avoid collisions with N−1 parallel sister runs **on the same problem**."
- Worktree path: `worktrees/<tag>`.
- Branch: `erdos-research/<tag>`.
- Reminder: the **seed run is non-committing** — do NOT do a baseline algebraic rewrite (parent quant repo's pattern; doesn't apply here).
- **Same-problem cohort note (unique to this skill)**: "N−1 sister runs are exploring this same problem concurrently. The shared `trial_cache_<PROBLEM_TAG>.tsv` deduplicates AST across all of them — if `log_result.py` returns exit 3, your hypothesis collided with a sister run, not your own prior trial. `git reset --hard HEAD~1` and pick a genuinely different axis from the hypothesis seeds in the `erdos-autoresearch` skill (greedy / algebraic / local-search / SA / coset / DFS for cap-set; singer / erdos-turan / augmentation / swap / SA / difference-set / concat for Sidon)."
- Full "Archive + push + cleanup" on graceful stop.
- Windows cleanup note: the skill's Archive block falls back from `git worktree remove` to unconditional `rm -rf worktrees/$TAG` once `origin/$BRANCH` is confirmed (or no remote exists) — do NOT skip.
- Explicit isolation rule: do not reach into sibling worktrees.
- Ask for a brief end-of-run summary (branch, keep/discard/crash counts, baseline, running_best, count of exit-3 AST collisions observed, push status).

Spawn all subagents with `run_in_background: true` so they run concurrently and you're notified as each finishes.

## Step 4 — Aggregate

As each subagent reports, record: branch, baseline, running_best, keep/trial counts, exit-3 count, push status. Do NOT Read subagent output JSONL files — they overflow context.

When all N are done, emit a single cohort summary table to the human:

```
Deep auto-erdos on <PROBLEM_TAG> — N=<N> parallel runs

| Branch                    | Baseline (LB) | Running Best | Keeps | Trials | AST collisions |
|---------------------------|---------------|--------------|-------|--------|----------------|
| erdos-research/<tag_1>    | <baseline>    | <best>       | <k>   | <t>    | <c>            |
| erdos-research/<tag_2>    | ...           | ...          | ...   | ...    | ...            |
...

Total keeps across cohort: <N>
Best score in cohort:      <value> (branch erdos-research/<tag>)
```

Call out any branch where `running_best > baseline` — that branch beat the literature LB and warrants independent hand re-verification before trusting. The typical cohort outcome on a hard open problem (e.g. `capset_n9`) is 0 keeps across all N branches; even one is noteworthy.

## Step 5 — Worktree cleanup

Each subagent runs the `erdos-autoresearch` skill's Archive + push + cleanup block. Expect `worktrees/` to be empty after all subagents succeed.

If any `worktrees/<tag>/` remains after completion, the push to origin failed for that agent (and a remote was configured) — tell the human, do NOT `rm -rf` yourself, and do NOT `git worktree prune` aggressively. Confirm with `git ls-remote --heads origin erdos-research/<tag>`.

## Common pitfalls

- **Picking N > 8 without reason**: AST collisions dominate, diminishing returns. If the human wants more throughput, prefer raising `AUTOERDOS_TRIAL_CAP` over raising N — same cross-branch dedup, fewer concurrent processes.
- **Picking a sanity-check problem**: deep on `capset_n4` or `sidon_100` is just running null controls in parallel. Allowed but pointless — say so once, then proceed if the human insists.
- **Reusing the same epoch base across back-to-back invocations**: if the human runs `/erdos-deep-autoresearch` twice within the same minute, the second invocation's tag candidates collide with the first's. The Step 2 collision check catches this — bump `BASE_EPOCH` by 30+ seconds, don't force through.
- **Conflating with `erdos-autoresearch-all`**: that skill fans ONE agent per problem across N problems (different `PROBLEM_TAG` each). This skill fans N agents within ONE problem (same `PROBLEM_TAG`). If the human says "deep run on all problems", that's deep × all — ask whether they mean N per problem (expensive) or just `erdos-autoresearch-all`'s default of 1-per-problem.
- **Waiting synchronously**: you're notified when background agents complete — do not sleep-poll.
- **Summarizing before all are done**: report each branch as its notification arrives; the cohort table comes only after the last one.
