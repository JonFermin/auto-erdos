---
name: erdos-autoresearch
description: Use when the user asks to kick off / start / begin a new combinatorial Erdős experiment in this repo, run the autonomous strategy loop, or launch an overnight auto-erdos run. Triggers on phrases like "kick off a new experiment", "start the autoresearch loop", "run program.md", "launch on capset_n8", "begin an erdos run". Drives the program.md loop: seed run → edit strategy.py → commit → verifier → log_result.py → keep/discard, inside a dedicated git worktree on a fresh erdos-research/<tag> branch (timestamped MMDD-HHMMSS so parallel launches don't collide), never stopping until the grader exits 4 or the human interrupts.
---

# erdos-autoresearch

Kicks off an autonomous Erdős-style combinatorial experiment loop in this repo per `program.md`. Runs inside a **dedicated git worktree** on a fresh `erdos-research/<tag>` branch, where `<tag>` is **timestamped** `MMDD-HHMMSS` (e.g. `0428-223742`) so two experiments can run in parallel without stomping on each other. Numeric tags only — locale-independent and sortable. Never stops until the grader returns exit 4 (trial cap) or the human interrupts.

## Non-negotiable ground rules (do not violate)

- `strategy.py` is the ONLY file you edit. Everything inside `generate_candidate()` (and helpers it calls) is fair game.
- `prepare.py` is READ-ONLY (verifier, time budget, audit-trail writer). The shared per-problem trial cache assumes the verifier is part of the fixed environment — do NOT modify it.
- `problems/*.json` are READ-ONLY — the literature baseline is fixed for the duration of the branch.
- Never stop to ask "should I keep going?". The human may be asleep. Only three exits: grader returns 4, human interrupts, or you genuinely run out of defensible hypotheses (documented in a one-paragraph chat summary — not a 19th micro-variant).
- Never `git add results.tsv`, `run.log`, or `verifier_results.tsv` — all gitignored by design.
- No new dependencies. No modifications to `prepare.py`, `log_result.py`, or `running_best.py`.
- Do not read `verifier_results.tsv` or the harness trial cache directly — those are harness-side audit trails. Read your own `run.log` and `results.tsv` only.

## Step 1 — Setup

You start in the repo root (the main checkout).

**First, resolve the problem.** If the launch prompt names a non-default problem (e.g. "on capset_n9", `PROBLEM_TAG=sidon_1000`, "/erdos-autoresearch sidon_3000"), `export PROBLEM_TAG=<tag>` **before** any preflight check, any loop command, and any helper invocation. Default is `capset_n8`. Every helper (`strategy.py`, `log_result.py`, `running_best.py`, `prepare.py`) reads this env var at import time, so the export must persist for the whole session. See "Problem selection" below.

Then run these checks in parallel:

```bash
git status
git rev-parse --abbrev-ref HEAD
ls problems/${PROBLEM_TAG:-capset_n8}.json
grep -q '^worktrees/' .gitignore && echo ok || echo "NEEDS worktrees/ in .gitignore"
```

Then:

1. **Pick a timestamped tag and export it**: numeric `MMDD-HHMMSS` from the current local time (e.g. `0428-223742`). Numeric only — locale-independent and sortable. The seconds suffix is what lets two concurrent skill launches coexist — do NOT drop it even if you're the only one running.
   ```bash
   TAG=$(date +%m%d-%H%M%S)
   git branch --list "erdos-research/$TAG"   # must be empty; if not, append b/c/d as a collision bump
   export TAG
   ```
   `$TAG` is used throughout the rest of the skill — setup, loop, archive. Do not retype the literal value.

2. **Create a dedicated worktree on a fresh branch from master**:
   ```bash
   mkdir -p worktrees
   git worktree add -b "erdos-research/$TAG" "worktrees/$TAG" master
   cd "worktrees/$TAG"
   ```
   Every subsequent command in the loop runs from **inside the worktree** (`worktrees/$TAG/`). `results.tsv`, `run.log`, and the `strategy.py` edits all live there — so parallel experiments never touch each other's state. If the main working tree has uncommitted changes, that's fine (worktrees are independent) — but check `worktrees/` is in `.gitignore` (the grep check above). If it isn't, stop and tell the human to add it; otherwise `git status` in the main tree fills with worktree noise.

3. **Verify problem JSON**: `ls problems/$PROBLEM_TAG.json`. Problems are committed to the repo, so this should always exist; if it doesn't, the human typoed the tag — stop and ask. There is no external price/data cache here (unlike the parent quant repo) — the verifier is bundled in `prepare.py` and runs in-process.

4. **Read context** (narrow — don't flood your window): `strategy.py` is small, read it in full. `prepare.py` is sizeable; do NOT read it whole — `grep` for the specific constant or helper you need (e.g. `grep -n 'TIME_BUDGET\|verify\|print_summary' prepare.py`). `program.md` you've already read. `README.md`, `log_result.py`, and `running_best.py` only if a specific question arises; don't re-derive their rules from scratch.

5. **Seed run is NON-COMMITTING** (per program.md). Do NOT make a baseline commit. Just run `strategy.py` as it sits at HEAD:
   ```bash
   PROBLEM_TAG=$PROBLEM_TAG uv run strategy.py > run.log 2>&1
   grep "^score:\|^is_valid:\|^verifier_seconds:\|^status_hint:" run.log
   PROBLEM_TAG=$PROBLEM_TAG uv run log_result.py "thesis: seed run — randomized greedy from scaffold strategy.py"
   ```
   - The grader will almost always emit `status=discard` (seed score < literature baseline).
   - **DO NOT `git reset --hard HEAD~1`** — there is no agent-made commit to reset. Resetting would move HEAD off the scaffold/fix commit onto its parent, silently downgrading the verifier. The reset rule applies only to commits *you* made in the loop below.
   - If `log_result.py` returns exit 3 (AST dup with a prior branch's seed in the shared per-problem cache), that's expected on second-and-subsequent runs of the same problem. Proceed straight to the loop with HEAD untouched.

### Problem selection

The experiment loop defaults to `PROBLEM_TAG=capset_n8`. If the human names a different problem in the launch prompt:

- Verify `problems/<tag>.json` exists.
- Export `PROBLEM_TAG=<tag>` on EVERY call to `strategy.py`, `log_result.py`, `running_best.py`. They all read it at import time.
- All shipped problems are fast on a typical laptop; `capset_n10` is the slowest at ~0.5–1s per verifier call on a large candidate. The wall-clock cap inside `prepare.TimeBudget` is **15 minutes** (`AUTOERDOS_TIME_BUDGET_S=900`) per `strategy.py` run — that budget is yours to spend on DFS / SA / GA / exact sub-routines. Runs that exceed it should bail gracefully (check `tb.expired`) and return whatever valid candidate they have.

### Parallel experiments

Two or more worktrees can run concurrently when each has a unique timestamped tag. But:

- Parallel runs on **different** `PROBLEM_TAG`s are fully independent — each problem has its own cache file (`~/.cache/auto-erdos/trial_cache_<PROBLEM_TAG>.tsv`), no contention.
- Parallel runs on the **same** problem share that per-problem AST cache — sister runs' AST-dedup will reject your hypothesis if a sibling tried the same thing first. This is intentional: pooled exploration without redundancy.
- Each worktree has its own `results.tsv` / `run.log`, so the grader and `running_best.py` see only that worktree's trials — they do NOT pool kept-scores across parallel experiments.
- Don't reach into a sibling worktree's files from inside your loop. If the human wants to compare across parallel branches, that's a morning-review job.

## Step 2 — The loop

Run every command from **inside the worktree** (`worktrees/<tag>/`). Repeat until the grader exits 4 or the human interrupts:

```bash
# 1. Form a hypothesis (one line, mathematical intuition, not a knob-twist)
# 2. Edit strategy.py — real code change (comments/whitespace/docstring-only is auto-rejected).
git add strategy.py
git commit -m "<short imperative summary of the change>"

# 3. Run the verifier — ALWAYS redirect, never tee/stream.
PROBLEM_TAG=$PROBLEM_TAG uv run strategy.py > run.log 2>&1

# 4. Extract headline metrics. If empty → crash; tail -n 50 run.log to read the trace.
grep "^score:\|^is_valid:\|^verifier_seconds:\|^status_hint:" run.log

# 5. Log the row (grader writes status, not you).
PROBLEM_TAG=$PROBLEM_TAG uv run log_result.py "thesis: <one-line rationale>"
rc=$?
echo "exit=$rc"

# 6. Branch on exit code:
#    0 → parse "status=keep" or "status=discard" from last stdout line.
#        keep    → advance (do nothing, next iteration starts from this HEAD)
#        discard → git reset --hard HEAD~1
#    2 → description invalid (missing 'thesis: ' prefix, or contains tab/newline).
#        Fix the command and rerun log_result.py. Nothing was logged; do NOT reset.
#    3 → AST-duplicate of a prior trial on this problem (any branch, via the
#        shared trial cache). git reset --hard HEAD~1, pick a genuinely
#        different hypothesis. Do not retry the same AST.
#    4 → TRIAL CAP. Stop. Run the Archive + push + cleanup block.
#    5 → crash row written. git reset --hard HEAD~1. tail -n 50 run.log,
#        learn, then try a different idea (or fix the bug if obvious).
```

### Probing state between iterations (all safe — deterministic verifier, nothing to mask)

```bash
PROBLEM_TAG=$PROBLEM_TAG uv run running_best.py              # current best kept score (baseline if none)
PROBLEM_TAG=$PROBLEM_TAG uv run running_best.py --baseline   # the problem's literature baseline
PROBLEM_TAG=$PROBLEM_TAG uv run running_best.py --trials     # rows on this branch / cap, e.g. "7/20"
git log --oneline -10                                        # recent experiment commits

# results.tsv has 6 cols: commit score is_valid verifier_seconds status description.
# Safe to read in full — there is no IS/OOS split here, the verifier is the truth.
column -t -s $'\t' results.tsv | head
awk -F'\t' 'NR>1 {print $1, $5, $6}' results.tsv               # full hypothesis history
awk -F'\t' 'NR>1 && $5=="keep" {print $1, $2, $6}' results.tsv  # survivors so far
```

There is no `oos_results.tsv`, no IS/OOS split, and nothing to mask — `score` is `score`. Peeking is just reading your own log.

## Hypothesis discipline

- **Review prior theses before forming a new one.** Before editing `strategy.py`, run `awk -F'\t' 'NR>1 {print $1, $5, $6}' results.tsv`. Scan for what you've already tried. Because each discard resets to baseline, nothing stops you from re-exploring the same tiny region of idea-space twenty times; this review is the only thing that does.
- **Name the axis in the thesis line.** Every `thesis:` must declare which dimension it moves along — for cap-set: `[greedy]` / `[algebraic]` / `[local-search]` / `[SA]` / `[coset]` / `[DFS]`; for Sidon: `[singer]` / `[erdos-turan]` / `[augmentation]` / `[swap]` / `[SA]` / `[difference-set]` / `[concat]`. Format: `thesis: [axis] <rationale>`, e.g. `thesis: [algebraic] lift cap-free F_3^4 set via product to F_3^8`. Near-duplicates become visible at a glance; every new thesis should move on an axis that prior trials haven't saturated.
- Frame the thesis **before** editing. Write it as the `thesis:` line first; if you can't, skip the idea.
- Prefer constructions with mathematical intuition (why this would yield a larger valid set) over parameter sweeps.
- A 5-line change with a thesis beats a 10-hyperparam grid search. Simpler is better. Deleting code that works equally well is a win.
- "Nothing beat baseline" is the most likely correct outcome on cap-set n≥7 and Sidon mid/large N — these LBs are decades of mathematician work. Do not pad the count to reach 20 — fewer honest hypotheses beats knob-twist churn.

## Idea seeds (from program.md — pick ones you can defend, don't sweep them)

**Cap sets in F_3^n** (`capset_n4` … `capset_n10`):
- Greedy variants: different orderings (sphere shells from origin, reverse lex, random restart with k attempts and keep best); different acceptance rules.
- Algebraic constructions: lift a small known cap-free set in F_3^k via product / direct sum to F_3^n. E.g. cap set of size 4 in F_3^2 → product gives 4^(n/2) in F_3^n. Compare against current best.
- Local search: start from random valid set, swap moves (remove p, try to add q1, q2 not previously fittable). Hill-climb on size.
- Simulated annealing: same swap moves but accept downhill moves with decaying probability.
- Coset partitioning: partition F_3^n into cosets of a small subspace, pick at most one point per coset, lift constraints.
- Structured restarts: when greedy stalls, restart from a deterministic "good" subset.
- Exact DFS sub-routine on a small fiber, glued to a greedy outer (mind the 15-min time budget — check `tb.expired`).

**Sidon / B₂ sets in [1, N]** (`sidon_100` … `sidon_3000`):
- Translated Singer set: for prime power q, the Singer construction gives a (q+1)-element Sidon set in [0, q²+q]. Translate or restrict to fit [1, N]. Establishes the known LB cleanly.
- Erdős–Turán: {2pa + (a² mod p) : 0 ≤ a < p} is Sidon in [1, 2p²-p+1] for prime p.
- Greedy + augmentation: start from a known Singer/E–T set; greedily add points that don't break Sidon.
- Local search (swap moves): start from a Singer base of size k, try remove-1 / add-2 swaps. Hill-climb on size.
- Simulated annealing: same swap moves, decaying acceptance for downhill.
- Difference-set parameterization: Sidon set ↔ perfect difference family in additive group. Search over small-modulus structures.
- Concatenation / direct sum: join two disjoint Sidon sets in [1, M] and [M+1, N] — check cross-sums don't collide.
- Kotzig-array / Costas-style algebraic bases: occasionally beat Singer for specific N.

## Stop conditions (the only three)

On a **graceful** stop (cases 1 and 3 below), run the **Archive + push + cleanup** sequence (next section) before returning to the human. On a human interrupt (case 2), do nothing — you can't clean up reliably mid-signal.

1. `log_result.py` returns exit 4 → trial cap reached. Print a one-screen summary: the worktree path, branch name, `PROBLEM_TAG`, count of keep / discard / crash rows, best kept score from `running_best.py`, baseline from `running_best.py --baseline`, `thesis:` lines grouped by status. Then run **Archive + push + cleanup**.
2. Human interrupts (Ctrl-C or explicit "stop"). Leave the worktree and branch as-is; do not tidy up. The human has taken over.
3. You cannot articulate a defensible non-micro-variant hypothesis. Write a one-paragraph summary to chat (not to a file) explaining what's been tried and why you're stopping. Then run **Archive + push + cleanup**. Do NOT fabricate a filler trial.

## Archive + push + cleanup

`results.tsv` is gitignored, so removing the worktree destroys it. The archive step folds its content into a committed **per-run** summary at `summaries/<tag>.md` so the branch on origin is self-describing. The path is tag-scoped — never a shared `SUMMARY.md` at the root — so parallel branches can be merged or compared without file-level conflicts. Do NOT maintain a rollup/index file in the loop; the morning-review step regenerates that on demand from the per-run files (see the hint at the bottom).

```bash
# (from inside worktrees/$TAG — $TAG exported back in Step 1)

# 0. Compute everything that goes into summaries/$TAG.md / commit message up-front.
#    No `<placeholder>` literals should survive past this block — if you see
#    `<...>` in the committed file, a substitution was missed.
BRANCH="erdos-research/$TAG"
SUMMARY_PATH="summaries/$TAG.md"
PROB="${PROBLEM_TAG:-capset_n8 (default)}"
BASELINE_LINE=$(uv run running_best.py --baseline 2>/dev/null || echo "n/a")
RUNNING_LINE=$(uv run running_best.py 2>/dev/null || echo "no kept rows")
TRIALS_LINE=$(uv run running_best.py --trials 2>/dev/null || echo "0/20")
N_KEEP=$(awk -F'\t' 'NR>1 && $5=="keep"    {n++} END {print n+0}' results.tsv)
N_DISCARD=$(awk -F'\t' 'NR>1 && $5=="discard" {n++} END {print n+0}' results.tsv)
N_CRASH=$(awk -F'\t' 'NR>1 && $5=="crash"  {n++} END {print n+0}' results.tsv)
N_TRIAL=$(awk -F'\t' 'NR>1                 {n++} END {print n+0}' results.tsv)
STOP_REASON="trial-cap"   # set manually: "trial-cap" | "no-defensible-hypothesis"

# 1. Build summaries/$TAG.md — capture the full audit trail in a committed file.
#    Per-run path (not SUMMARY.md) so parallel branches don't conflict on merge.
#    Build in pieces (NOT a single unquoted heredoc): thesis strings in
#    results.tsv are agent-authored and may contain `$(...)`, backticks, or
#    `\` that would be re-evaluated by bash inside `<<EOF`. Here they pass
#    through cat/awk only.
mkdir -p summaries
{
  printf '# %s\n\n' "$BRANCH"
  printf -- '- **PROBLEM_TAG**:   %s\n' "$PROB"
  printf -- '- **Baseline (LB)**: %s\n' "$BASELINE_LINE"
  printf -- '- **Running best**:  %s\n' "$RUNNING_LINE"
  printf -- '- **Trials logged**: %s\n' "$TRIALS_LINE"
  printf -- '- **Counts**:        keep=%s discard=%s crash=%s\n' "$N_KEEP" "$N_DISCARD" "$N_CRASH"
  printf -- '- **Stop reason**:   %s\n\n' "$STOP_REASON"
  printf '## results.tsv\n\n'
  printf '```\n'
  cat results.tsv
  printf '```\n\n'
  printf '## Theses by status\n\n'
  printf '### keep\n'
  awk -F'\t' 'NR>1 && $5=="keep"    {print "- " $6 "  (score " $2 ")"}' results.tsv
  printf '\n### discard\n'
  awk -F'\t' 'NR>1 && $5=="discard" {print "- " $6 "  (score " $2 ")"}' results.tsv
  printf '\n### crash\n'
  awk -F'\t' 'NR>1 && $5=="crash"   {print "- " $6}' results.tsv
} > "$SUMMARY_PATH"

# Sanity-check: no unresolved <...> placeholders snuck through.
if grep -q '<[a-z-]*>' "$SUMMARY_PATH"; then
  echo "ERROR: unresolved <placeholder> in $SUMMARY_PATH — fix before committing"
  grep -n '<[a-z-]*>' "$SUMMARY_PATH"
  exit 1
fi

# 2. Commit the summary.
git add "$SUMMARY_PATH"
git commit -m "summary: $BRANCH ($N_KEEP/$N_TRIAL)"

# 3. Push the branch — only if a remote exists. Do not force-push.
HAS_REMOTE=0
if git remote get-url origin >/dev/null 2>&1; then
  HAS_REMOTE=1
  git push -u origin "$BRANCH" || { echo "push failed — leaving worktree in place for manual recovery"; exit 0; }
else
  echo "no origin remote — skipping push, will still clean up the worktree (local branch + summary stay as audit trail)"
fi

# 4. Only remove the worktree if the push succeeded (or no remote was expected).
#    If push failed, the `exit 0` above kept us out of this block — do not
#    silently lose the branch state.
cd ../..    # back to repo root
# Exact-match check — `grep -q origin/$BRANCH` would prefix-match a sibling
# branch (e.g. 0428-2237 vs 0428-223742) and nuke the wrong worktree.
if [ "$HAS_REMOTE" -eq 0 ] || git rev-parse --verify --quiet "refs/remotes/origin/$BRANCH" >/dev/null; then
  # Try git's registered removal first (cleans .git/worktrees/ metadata),
  # then always force-remove the filesystem directory — on Windows `git
  # worktree remove` routinely fails with "Filename too long" / "Invalid
  # argument" on the `.git/` subtree (MAX_PATH), leaving orphan files. Once
  # origin has the branch (or there's no remote), the files are disposable.
  # Finally prune the registry so stale metadata doesn't accumulate. This
  # block is unconditional on the gate above — do NOT leave disk cleanup as
  # "optional for the human later".
  git worktree remove "worktrees/$TAG" 2>/dev/null \
    || echo "git worktree remove failed (likely Windows MAX_PATH on .git/) — forcing filesystem cleanup"
  rm -rf "worktrees/$TAG"
  git worktree prune

  # 5. Branch on outcome:
  #    - any keep → real literature improvement on this problem. Open a PR
  #      so the human reviews + independently re-verifies before merge.
  #    - zero keeps → delete the local branch ref. The branch stays on
  #      origin (if pushed) as an audit trail but doesn't clutter
  #      `git branch` locally.
  #
  # Note there is no "seed keep" carve-out here: unlike the parent quant
  # repo (where the first iteration is a behavior-preserving algebraic
  # rewrite that anchors the baseline), the auto-erdos seed run is
  # NON-COMMITTING and never produces a keep row by itself. Every keep is a
  # genuine post-seed improvement.
  if [ "$N_KEEP" -gt 0 ] && [ "$HAS_REMOTE" -eq 1 ]; then
    if command -v gh >/dev/null 2>&1; then
      PR_BODY="Auto-erdos run on \`$PROB\` kept $N_KEEP improvement(s) across $N_TRIAL trials.

- Baseline (literature LB): $BASELINE_LINE
- Running best after run:   $RUNNING_LINE
- Full audit:               \`summaries/$TAG.md\` on this branch

A keep means the construction beat the literature lower bound stored in \`problems/$PROB.json\`. **Do NOT merge without independently re-verifying the construction by hand** — the verifier is correct, but a kept score that exceeds an established LB warrants re-verification (and a literature search for prior art) before treating as a real result. Cap-set / Sidon LBs have a long history of false improvements that turned out to be coding bugs in the constructor."
      gh pr create --base master --head "$BRANCH" \
        --title "auto-erdos: $BRANCH ($N_KEEP improvements / $N_TRIAL trials on $PROB)" \
        --body "$PR_BODY" \
        || echo "gh pr create failed — branch is on origin, open the PR manually"
    else
      echo "gh CLI not installed — $BRANCH is pushed; open PR manually at origin"
    fi
    echo "archived with PR: $BRANCH (real improvement, local branch kept for review)"
  else
    git branch -D "$BRANCH" 2>/dev/null \
      || echo "local branch $BRANCH not found (already cleaned or never checked out here)"
    if [ "$HAS_REMOTE" -eq 1 ]; then
      echo "archived no-keep: $BRANCH pushed to origin, local branch removed"
    else
      echo "archived no-keep (no remote): summary committed locally on $BRANCH; local branch removed"
    fi
  fi
else
  echo "worktree preserved at worktrees/$TAG — manual cleanup required (origin missing $BRANCH)"
fi
```

Rules:
- Never `--force` on push. If origin rejects (somehow the branch exists upstream), STOP and report — do not overwrite.
- Never `git worktree remove --force` if the remote is missing the commits; that loses work. The unconditional `rm -rf worktrees/$TAG` in step 4 is gated on the `origin/$BRANCH` (or no-remote) check directly above it — do NOT move, delete, or skip that guard.
- Delete the local branch (`git branch -D "$BRANCH"`) **only** on no-keep runs — the origin copy (if any) is the audit trail, the local copy is dead weight. On keep runs the local branch stays so the human can `git checkout` it without refetching.
- Never force-push, never delete a branch on origin. No-keep branches stay on origin as an audit trail of what didn't work.
- If there is no `origin` remote configured, skip push and PR but still clean up the worktree — the local branch + committed `summaries/$TAG.md` are the audit trail. Tell the human. Do NOT try to add a remote.
- If `gh` CLI isn't available, skip PR creation and say so. Do NOT try to install it.

## Morning-review hint for the human (do NOT act on this during the loop)

After the human wakes up and the cleanup has run, they review via the pushed branch:

```bash
git fetch origin
git log origin/erdos-research/<tag> --oneline                  # trial commits + summary
git show origin/erdos-research/<tag>:summaries/<tag>.md        # the full archived summary

# Cross-run rollup: generate on demand from the per-run files (not committed).
git for-each-ref --format='%(refname:short)' refs/remotes/origin/erdos-research/ \
  | while read ref; do
      tag="${ref##*/}"
      git show "$ref:summaries/$tag.md" 2>/dev/null | head -10
      echo "---"
    done

# To independently re-verify a specific kept commit:
git checkout <commit>
PROBLEM_TAG=<tag> uv run strategy.py > /tmp/reverify.log 2>&1
grep "^score:\|^is_valid:\|^reason:" /tmp/reverify.log
```

If the loop was Ctrl-C'd (stop condition 2), the worktree is still at `worktrees/<tag>/` and `results.tsv` is intact there — review locally before deciding whether to archive.

Independent re-verification is the human's job, not yours. A keep here is a hypothesis worth checking against the literature — it is NOT a verdict. Cap-set / Sidon LBs have a long history of false improvements that turned out to be coding bugs.
