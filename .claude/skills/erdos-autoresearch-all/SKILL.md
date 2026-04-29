---
name: erdos-autoresearch-all
description: Use when the user asks to run autoresearch across ALL problems (capset_n4 through capset_n10 plus sidon_100/500/1000/3000) or any multi-problem subset in parallel. Spawns one general-purpose subagent per problem, each running the `erdos-autoresearch` skill end-to-end in its own git worktree with a pre-assigned unique timestamp tag. Default is all 11 shipped problems; pass a comma-separated subset to narrow. Triggers on phrases like "all possible problems", "run autoresearch on all problems", "every capset/sidon in parallel", "fan out across the whole problem set".
---

# erdos-autoresearch-all

Fan out the `erdos-autoresearch` skill across multiple problems in parallel. One subagent per problem, each with a pre-assigned unique timestamp tag so their worktrees don't collide. Each subagent runs the full 20-trial loop and archives to its own branch on origin.

## Default problem set

Unless the invoker names a subset, run all 11 shipped problems:

**capset family** (cap sets in F_3^n: no 3-term AP, score = |S|):
- `capset_n4` (LB 20, exact — sanity-check / null-control)
- `capset_n5` (LB 45, exact — sanity-check)
- `capset_n6` (LB 112, exact — sanity-check)
- `capset_n7` (LB 236 — open at top)
- `capset_n8` (LB 496 — default, open at top)
- `capset_n9` (LB 1082 — open, far from upper bound)
- `capset_n10` (LB 2474 — slowest verifier, open)

**sidon family** (B₂ sets in [1, N]: pairwise sums distinct, score = |S|):
- `sidon_100`  (LB 11 — almost certainly exact, sanity-check)
- `sidon_500`  (LB 23 — Singer-23, mild headroom)
- `sidon_1000` (LB 32 — Singer gives 32, real result would be 33)
- `sidon_3000` (LB 53 — Singer-53, real headroom)

The canonical list is whatever `problems/*.json` files are present in the repo root — if the human adds a new problem JSON, treat it as part of the default set going forward.

A subset can be passed as a comma-separated list (e.g. `capset_n8,capset_n9,sidon_3000`, or just `capset_n8,sidon_3000`). If the invoker says "the open ones" or "skip sanity-checks", drop `capset_n{4,5,6}` and `sidon_100` and run the remaining 7.

The "sanity-check" problems (exact-known LBs) are useful as null controls — a kept row on `capset_n4` would indicate a bug in the verifier or harness, not a real result. Including them by default catches such regressions.

## Step 1 — Preflight

From the repo root (main checkout), verify:

```bash
git status                                    # should be clean-ish (worktrees/ is gitignored)
git rev-parse --abbrev-ref HEAD               # note the starting branch; worktrees branch from master
ls problems/                                  # confirm all requested problems have a JSON
grep -q '^worktrees/' .gitignore && echo ok   # required — else parallel worktrees pollute main tree
```

**Missing problem JSON** — stop and ask. There is no autonomous fallback (we don't generate problem specs).

There is **no external data cache** to download here (unlike the parent quant repo) — the verifier is bundled in `prepare.py` and runs in-process from each problem's JSON. So preflight is fast.

## Step 2 — Assign unique tags

The `erdos-autoresearch` skill requires each run to have a unique numeric `MMDD-HHMMSS` tag, and two concurrent runs with the same tag collide on the worktree path. Crucially, another Claude Code instance may be running this same skill simultaneously — so tags must be second-precision AND cross-checked against local branches, existing worktrees, AND origin refs before spawning.

Build N tags by incrementing the current epoch one second at a time, then formatting with GNU `date -d @<epoch>`:

```bash
git fetch origin --prune                          # pull remote branches so collision check sees sister CC instances
BASE_EPOCH=$(date +%s)
N=11                                              # replace with actual number of problems requested (default 11)
TAGS=()
for i in $(seq 0 $((N-1))); do
  TAGS+=("$(date -d "@$((BASE_EPOCH + i))" +%m%d-%H%M%S)")
done
# e.g. TAGS=(0428-212759 0428-212800 0428-212801 ...)
# Minute/hour rollover is handled by date(1) — no manual carry logic needed.
```

Verify every candidate is free across all three collision surfaces:

```bash
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

**If any collision:** bump `BASE_EPOCH=$((BASE_EPOCH + 30))`, regenerate TAGS, re-check. Typical cause is another CC instance launched within the same window. A 30-second bump (larger than the 11-tag span) clears it cleanly.

Do not drop the seconds suffix — the `erdos-autoresearch` skill insists on full `MMDD-HHMMSS`, and the seconds are what make cross-instance invocation safe.

If the repo has no `origin` remote configured, the `git ls-remote` check is a no-op (silently skipped via `2>/dev/null`) — safe, but the local-branch and worktree-dir checks still run.

## Step 3 — Spawn parallel subagents

Spawn one `general-purpose` subagent per problem, all in a single message (multiple Agent tool calls in one response so they launch concurrently). Each subagent's prompt must be self-contained — it has no memory of this conversation.

Required prompt content per subagent (adapt fields in angle brackets):

- Path to the skill: `C:/Users/honsf/DEVELOP/auto-erdos/.claude/skills/erdos-autoresearch/SKILL.md` — tell the subagent to **read it in full before starting**.
- Working directory: `C:\Users\honsf\DEVELOP\auto-erdos`.
- `PROBLEM_TAG=<problem>` — emphasize it must be exported on every invocation of `strategy.py`, `log_result.py`, `running_best.py`, `prepare.py` (all read it at import time).
- The **pre-assigned** timestamp tag from Step 2 (e.g. `0428-070001`). State explicitly: "do not generate your own tag — it's been pre-assigned to avoid collisions with N parallel sister runs."
- Worktree path: `worktrees/<tag>`.
- Branch: `erdos-research/<tag>`.
- Full "Archive + push + cleanup" on graceful stop.
- Reminder: the **seed run is non-committing** — do NOT do a baseline algebraic rewrite (that's the parent quant repo's pattern; auto-erdos's seed is just the scaffold strategy.py at HEAD).
- Windows cleanup note: the skill's Archive block falls back from `git worktree remove` (which routinely errors "Filename too long" / "Invalid argument" on MAX_PATH) to an unconditional `rm -rf worktrees/$TAG` once `origin/$BRANCH` is confirmed (or no remote exists). Do NOT skip or short-circuit that fallback — leaving the directory stranded is no longer acceptable.
- Explicit isolation rule: do not reach into sibling worktrees; the other N−1 runs are concurrent.
- Ask for a brief end-of-run summary (branch, problem, keep/discard/crash counts, baseline, running_best, push status, PR URL if a keep was archived).

Spawn all agents with `run_in_background: true` so they run concurrently and you're notified as each finishes.

**Domain hints**: pass a one-line hint per family to the relevant subagent. Keep it one sentence — don't over-specify, the subagent is autonomous.

- **capset_n{4,5,6}**: "exact value sanity-check — a `keep` row here would indicate a bug, not a real result. Expected outcome: 0 keeps across all 20 trials. Useful as a null control."
- **capset_n{7,8,9,10}**: "open lower bound — promising axes are algebraic constructions (lift small cap-free sets via product), coset partitioning, and exact DFS sub-routines on small fibers (mind the 15-min time budget). Greedy-only is unlikely to beat the LB."
- **sidon_100**: "almost certainly exact — null control."
- **sidon_500/1000/3000**: "Singer construction is the LB. Promising axes: greedy augmentation from a Singer base, swap-search local moves, difference-set parameterization. Concatenation has subtle cross-sum constraints — check carefully."

## Step 4 — Aggregate

As each subagent reports completion, record: branch, problem, baseline, running_best, keep/trial counts, push status. Do NOT Read the subagent's output JSONL file (it's the full transcript and will overflow context).

When all N are done, emit a single cross-problem summary table to the human:

```
| Problem      | Baseline (LB) | Running Best | Keeps | Trials | Branch                    |
|--------------|---------------|--------------|-------|--------|---------------------------|
| capset_n4    | 20            | 20           | 0     | 20     | erdos-research/<tag>      |
| capset_n8    | 496           | 503          | 1     | 20     | erdos-research/<tag>  ★   |
| ...          | ...           | ...          | ...   | ...    | ...                       |
```

Call out any problem where `running_best > baseline` with a ★ — that branch beat a literature LB and warrants independent re-verification. The typical outcome on the open problems is 0 keeps (the literature LBs are decades of mathematician work). On the sanity-check problems, anything other than 0 keeps is a bug.

Multiple ★s across the open problems is noteworthy and the human should hand-verify each construction before trusting.

## Step 5 — Worktree cleanup (handled by each subagent)

Each subagent runs the `erdos-autoresearch` skill's **Archive + push + cleanup** block, which unconditionally `rm -rf`s its worktree directory once `origin/<branch>` is confirmed (or no remote exists) — `git worktree remove` is attempted first for metadata hygiene, but the forced filesystem removal is the real cleanup step (Windows' MAX_PATH routinely breaks the `git` variant). You should therefore expect `worktrees/` to be empty after all subagents report success.

If, after all subagents complete, any `worktrees/<tag>/` directory still exists:

- The only safe reason is that subagent's push to origin failed AND a remote was configured — meaning the worktree is the last copy of the work. Tell the human; do NOT `rm -rf` it yourself, and do NOT `git worktree prune` aggressively (that would desync the registry from the stranded work).
- Confirm with `git ls-remote --heads origin erdos-research/<tag>` before considering any further action.

## Common pitfalls

- **Same-tag collisions**: if two subagents somehow get the same tag (e.g. spawned from distinct skill invocations or from a sister CC instance running this same skill), their `git worktree add` races. Step 2's second-precision epoch-increment scheme plus the three-surface collision check (local branch, worktree dir, origin ref) prevents this — but only if you actually `git fetch origin` first so the origin check sees sister-instance branches.
- **Passing the skill content instead of a path**: the `erdos-autoresearch` skill is long. Pasting it into every subagent prompt wastes tokens. Just hand them the absolute path and tell them to read it.
- **Waiting synchronously**: do not sleep-poll for background agents. You are automatically notified when each completes — continue other work or respond to the user in the meantime.
- **Summarizing before all are done**: report each problem's result as its notification arrives. Produce the cross-problem table only after the last one reports.
- **Conflating with `erdos-deep-autoresearch`**: this skill fans ONE agent per problem across N problems (different `PROBLEM_TAG` each). The deep variant fans N agents within ONE problem (same `PROBLEM_TAG`). If the human says "deep run on all problems", that's deep × all — ask whether they mean N per problem (expensive) or just this skill's default of 1-per-problem.
- **Skipping the sanity-checks "to save time"**: don't, unless the human explicitly says to. They cost almost nothing (verifier is fast on small n / small N) and any non-zero keep on them is a regression you want to know about.
