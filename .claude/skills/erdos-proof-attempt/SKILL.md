---
name: erdos-proof-attempt
description: Use when the user asks to start / kick off / run an Erdős *proof* attempt in this repo (Track 2), as opposed to the search loop (Track 1, `erdos-autoresearch`). Triggers on phrases like "start a proof attempt on primitive_set_erdos", "run the proof loop", "attempt the primitive-set conjecture", "begin a proof-attempt run", "/erdos-proof-attempt". Drives the `proof_program.md` loop: session_start → claim qid → edit proof_strategy.md → commit → proof_prepare.py → proof_log_result.py → keep/discard, inside a dedicated git worktree on a fresh `erdos-proof/<tag>` branch (timestamped MMDD-HHMMSS-rnd so parallel attempts don't collide), with explicit session lifecycle so a session that ends mid-round can be resumed cold by a fresh invocation. Never stops until the gatekeeper exits 4, 6, or 7, or the human interrupts.
---

# erdos-proof-attempt

Kicks off an autonomous proof-attempt loop in this repo per `proof_program.md`. Runs inside a **dedicated git worktree** on a fresh `erdos-proof/<tag>` branch, where `<tag>` is timestamped `MMDD-HHMMSS-rnd4` (matching the session-id format from `proof_session_start.py`) so two attempts can run in parallel without stomping. Never stops until the gatekeeper exits 4 (round cap), 6 (converged), or 7 (counterexample proven), or the human interrupts.

A proof attempt may take MANY sessions. This skill drives ONE session — but is also responsible for resuming a prior session via `proof_session_start.py`. If the user re-invokes this skill on an existing worktree (after a token-cap stop, a SIGTERM, or an interrupt), the skill detects the existing branch + handoff and continues from disk state.

## Non-negotiable ground rules (do not violate)

- `proof_strategy.md` and `proof_lemmas/lemma_*.md` are the ONLY artifact files you edit during a round. Append rows to `proof_journal.jsonl`, `proof_open_questions.jsonl`, and `proof_critic_log.jsonl`; do NOT rewrite history in those files.
- `proof_prepare.py`, `proof_log_result.py`, `proofs/*.json`, `prompts/critic_*.md`, and `library/primitive_set_witness.py` are READ-ONLY at runtime. Editing a critic prompt mid-loop silently breaks reproducibility (its sha256 is logged into `proof_critic_log.jsonl`).
- `prepare.py`, `log_result.py`, `library/*.py` (search loop) are READ-ONLY. Track 1 stays untouched.
- Never `--force` push, never delete a branch on origin, never `git reset --hard` a kept-record commit.
- Never claim resolution of an open conjecture without a verifier-accepted witness. The openness critic + the `_compute_verdict_hint` defense-in-depth catch this.
- Never read another worktree's state from inside this loop.
- No new dependencies.

## Step 1 — Setup

You start in the repo root (the main checkout).

**First, resolve the proof tag.** If the launch prompt names a non-default proof (e.g. "on primitive_set_erdos", `PROOF_TAG=primitive_set_erdos`), `export PROOF_TAG=<tag>` **before** any preflight check, any loop command, and any helper invocation. Default is `primitive_set_erdos`. Every helper (`proof_prepare.py`, `proof_log_result.py`, `proof_session_start.py`) reads this env var at import time, so the export must persist for the whole session.

Then run these checks in parallel:

```bash
git status
git rev-parse --abbrev-ref HEAD
ls proofs/${PROOF_TAG:-primitive_set_erdos}.json
grep -q '^worktrees/' .gitignore && echo ok || echo "NEEDS worktrees/ in .gitignore"
```

Then decide: NEW attempt, or RESUME existing?

### Decision: new vs. resume

- If the user names an existing `erdos-proof/<tag>` branch (e.g. "resume erdos-proof/0501-090045-a3f1"), or there is exactly ONE existing `worktrees/<some-tag>/` whose branch is `erdos-proof/<some-tag>` and the human's prompt suggests "continue", "resume", "pick up", "again": **RESUME** that worktree.
- Otherwise: **NEW** attempt with a fresh tag.

### NEW attempt setup

1. **Pick a tag and export it**: numeric `MMDD-HHMMSS-<4hex>` from current time (e.g. `0501-090045-a3f1`). The 4-hex suffix prevents collisions when two skill launches land in the same second.
   ```bash
   TAG=$(date +%m%d-%H%M%S)-$(uv run python -c 'import os; print(os.urandom(2).hex())')
   git branch --list "erdos-proof/$TAG"   # must be empty
   export TAG
   ```

2. **Create a dedicated worktree on a fresh branch from master**:
   ```bash
   mkdir -p worktrees
   git worktree add -b "erdos-proof/$TAG" "worktrees/$TAG" master
   cd "worktrees/$TAG"
   ```
   Every subsequent command runs from inside the worktree.

3. **Verify proof JSON**: `ls proofs/$PROOF_TAG.json`. Stop and ask if it's missing.

4. **Read context** (narrow — don't flood your window):
   - `proof_program.md` end-to-end (you've already read this).
   - `proofs/$PROOF_TAG.json` — the claim, given_facts ledger, witness contract.
   - `proof_strategy.md` — the editable artifact (currently a stub).
   - `proof_lemmas/README.md` — lemma file format.
   - `prompts/critic_*.md` — skim ONE (e.g. `critic_sign.md`) to understand the contract; do not read all five in full.

### RESUME setup

1. **Switch to the existing worktree**:
   ```bash
   cd "worktrees/<tag>"
   export TAG=<tag>
   ```

2. **Read context (narrow)**:
   - `proof_session_handoff.md` — the FIRST thing you read on resume.
   - `proof_strategy.md` — the current state of the proof.
   - The most recently-edited file under `proof_lemmas/`.

## Step 2 — session_start (ALWAYS run this first)

Whether NEW or RESUME, the FIRST action inside the worktree is:

```bash
PROOF_TAG=$PROOF_TAG uv run proof_session_start.py
```

Read its stdout end-to-end. It prints:

- The newly-issued `session_id` (e.g. `s_0501-090045-a3f1`).
- The contents of `proof_session_handoff.md` (or "(no handoff yet — this is a cold first start)" on a fresh attempt).
- The top open questions in `proof_open_questions.jsonl`.
- Any orphan-session warning (a previous session ended without `session_close`).
- The most recent `session_close` reason.

Cache the `session_id` (call it `$SID`) — every journal/queue append uses it.

If a stash was created (the worktree had untracked edits from a prior crash), inspect with `git stash show -p stash@{0}` and decide whether to apply or drop. Do NOT silently apply.

## Step 3 — The round loop

Run every command from inside the worktree. Repeat until one of the four stop conditions fires:

```bash
# 1. Pick a qid. Default is the lowest-numbered open / released qid from
#    the printout above; the handoff may suggest a different priority.
QID=Q1  # or whatever you picked

# 2. Claim the qid.
NOW=$(uv run python -c 'from datetime import datetime, timezone; print(datetime.now(timezone.utc).isoformat(timespec="seconds"))')
echo "{\"qid\":\"$QID\",\"status\":\"claimed\",\"session_id\":\"$SID\",\"summary\":\"taking $QID\",\"ts\":\"$NOW\"}" \
    >> proof_open_questions.jsonl

# 3. Edit proof_strategy.md and/or a lemma file. Real change, not a no-op
#    (proof_log_result.py rejects content-hash duplicates).

# 4. Commit (the round is one commit).
git add proof_strategy.md proof_lemmas/ proof_open_questions.jsonl
git commit -m "<short imperative summary>"

# 5. Run the verifier — but NOT every round. proof_prepare runs 5 LLM
#    critics; ~30s/critic. Run on logical milestones, OR every 5 rounds
#    as a safety net.
PROOF_TAG=$PROOF_TAG uv run proof_prepare.py > run.log 2>&1
grep "^claim_status:\|^witness_valid:\|^verdict_hint:\|^critic_blocking_count:\|^critic_warn_count:" run.log

# 6. Log the round (gatekeeper writes status, not you).
PROOF_TAG=$PROOF_TAG uv run proof_log_result.py "thesis: <one-line rationale>"
rc=$?
echo "exit=$rc"

# 7. Branch on exit code:
#    0 → status on stdout's last line is keep_progress or discard.
#         keep_progress → advance (next iteration starts from this HEAD)
#         discard       → git reset --hard HEAD~1
#    2 → bad description; nothing logged. Fix and rerun proof_log_result.
#    3 → proof_hash duplicate of a prior round. git reset --hard HEAD~1
#         and pick a different angle.
#    4 → ROUND CAP. Stop. Go to Step 5 (session_end + archive).
#    5 → verifier crash. git reset --hard HEAD~1, inspect run.log.
#    6 → CONVERGED. Stop. Go to Step 5.
#    7 → COUNTEREXAMPLE PROVEN. Stop. Go to Step 5.

# 8. Resolve the qid (only if you finished it; partial work stays "claimed").
echo "{\"qid\":\"$QID\",\"status\":\"resolved\",\"session_id\":\"$SID\",\"summary\":\"<outcome>\",\"ts\":\"$(date -u +%FT%TZ)\"}" \
    >> proof_open_questions.jsonl

# 9. Append a round summary to the journal.
echo "{\"event\":\"round\",\"session_id\":\"$SID\",\"ts\":\"$(date -u +%FT%TZ)\",\"summary\":\"<one-line>\",\"qid\":\"$QID\",\"status\":\"<keep_progress|discard|...>\",\"commit\":\"$(git rev-parse --short=7 HEAD)\"}" \
    >> proof_journal.jsonl
```

### When to call session_end (this is the resumability hinge)

Call `proof_session_end.py` BEFORE one of these happens:

- **Token budget low**: if your context is approaching the cap (a soft signal: you've consumed most of your context window, or the harness warns you), STOP at the next round boundary and call session_end. Do NOT keep going hoping there's room.
- **Logical milestone**: a lemma is closed, a sub-section of the proof finalized, an open question resolved. session_end here gives a clean handoff for the next session.
- **Stop conditions** (exit 4, 6, 7): always call session_end before archiving.

NEVER skip session_end except on hard interrupt (Ctrl-C, SIGTERM). The next session_start handles those cases by detecting the orphan and stashing dirty work, but a clean session_end is much cheaper.

```bash
# session_end takes the stop reason as argv and an optional handoff template
# on stdin. Write a focused 1-page handoff so the next session boots fast.
cat <<EOF | PROOF_TAG=$PROOF_TAG uv run proof_session_end.py "reason: token budget low; next: prove sub-bound (b) of Lemma 2"
# Session handoff (session $SID)

**Stop reason**: token budget low

**Current focus**: Working on Lemma 2 sub-bound (b). Lemma 1 is proved
(see proof_lemmas/lemma_001.md). Lemma 2's frontmatter is status:open.

**qid in flight**: Q3 is claimed by this session, work in progress.

**Obstacle**: The Mertens-style estimate I tried gives a bound off by
a $\log\log x$ factor. Need to revisit the partial summation.

**Files modified this session**:
- proof_strategy.md (added Section 2 + cite of Lemma 1)
- proof_lemmas/lemma_001.md (status: open → proved)
- proof_lemmas/lemma_002.md (created, status: open)

**Suggested next move**:
1. Read proof_lemmas/lemma_002.md.
2. Try a Plünnecke / Brun-style sieve estimate for sub-bound (b).
3. If still stuck, set lemma_002 status: abandoned and try a different decomposition.
EOF
```

## Step 4 — Probing state between rounds

```bash
# Check round count vs cap.
PROOF_TAG=$PROOF_TAG uv run python -c "import pandas as pd; print(len(pd.read_csv('proof_results.tsv', sep='\t')) if __import__('os').path.exists('proof_results.tsv') else 0, 'rounds')"

# Read the current verdict trail.
column -t -s $'\t' proof_results.tsv | tail

# Re-read the live open queue.
PROOF_TAG=$PROOF_TAG uv run proof_session_start.py --json | python -c "import sys, json; d = json.load(sys.stdin); print(len(d['open_questions']), 'open;', d['live_open_count'], 'total live')"
# (Note: this would create a new session_id — DON'T do it mid-session;
# instead, parse proof_open_questions.jsonl directly.)

# Most recent critic findings (cached responses are b64-encoded):
tail proof_critic_log.jsonl
```

## Step 5 — Archive + session_end + cleanup

On a graceful stop (exit 4, 6, or 7), run this block. On a human interrupt (Ctrl-C), do nothing — leave state as-is for the human to inspect.

```bash
# (from inside worktrees/$TAG)

BRANCH="erdos-proof/$TAG"
SUMMARY_PATH="summaries/$TAG.md"
PROOF="${PROOF_TAG:-primitive_set_erdos}"
ROUNDS=$(awk -F'\t' 'NR>1 {n++} END {print n+0}' proof_results.tsv 2>/dev/null || echo 0)
KEEPS=$(awk -F'\t' 'NR>1 && ($10=="keep_progress" || $10=="keep_disproof") {n++} END {print n+0}' proof_results.tsv 2>/dev/null || echo 0)
DISPROOFS=$(awk -F'\t' 'NR>1 && $10=="keep_disproof" {n++} END {print n+0}' proof_results.tsv 2>/dev/null || echo 0)

# 1. session_end (writes handoff + commits + removes active marker).
cat <<EOF | PROOF_TAG=$PROOF_TAG uv run proof_session_end.py "reason: <one-line>"
# Final handoff
**Stop reason**: <round cap | converged | counterexample | interrupted>
**Outcome**: <kept records / partial result / disproof / no progress>
**For human review**: <pointers — kept records under records/proof_*.json>
EOF

# 2. Build summaries/$TAG.md.
mkdir -p summaries
{
  printf '# %s\n\n' "$BRANCH"
  printf -- '- **PROOF_TAG**:     %s\n' "$PROOF"
  printf -- '- **Rounds logged**: %s\n' "$ROUNDS"
  printf -- '- **Keep rows**:     %s (of which disproofs: %s)\n' "$KEEPS" "$DISPROOFS"
  printf '\n## proof_results.tsv\n\n```\n'
  cat proof_results.tsv 2>/dev/null
  printf '```\n\n## journal events (newest 20)\n\n```\n'
  tail -n 20 proof_journal.jsonl 2>/dev/null
  printf '```\n'
} > "$SUMMARY_PATH"

# 3. Commit summary.
git add "$SUMMARY_PATH"
git commit -m "summary: $BRANCH ($KEEPS/$ROUNDS)"

# 4. Push branch (skip if no origin remote).
HAS_REMOTE=0
if git remote get-url origin >/dev/null 2>&1; then
  HAS_REMOTE=1
  git push -u origin "$BRANCH" || { echo "push failed — leaving worktree for manual recovery"; exit 0; }
fi

# 5. Cleanup worktree (only if push succeeded or no remote).
cd ../..
if [ "$HAS_REMOTE" -eq 0 ] || git rev-parse --verify --quiet "refs/remotes/origin/$BRANCH" >/dev/null; then
  git worktree remove "worktrees/$TAG" 2>/dev/null \
    || echo "git worktree remove failed (Windows MAX_PATH on .git/) — forcing fs cleanup"
  rm -rf "worktrees/$TAG"
  git worktree prune

  # 6. PR on a real result; delete local branch otherwise.
  if [ "$DISPROOFS" -gt 0 ] && [ "$HAS_REMOTE" -eq 1 ]; then
    if command -v gh >/dev/null 2>&1; then
      gh pr create --base master --head "$BRANCH" \
        --title "auto-erdos PROOF: $BRANCH ($DISPROOFS disproof(s) on $PROOF)" \
        --body "**A keep_disproof means a verified counterexample to an open conjecture. Do NOT merge before independently re-running \`library.primitive_set_witness.verify_witness\` on the witness payload in records/proof_*.json AND a literature search.** History is full of false improvements that were coding bugs."
    fi
  elif [ "$KEEPS" -eq 0 ] && [ "$HAS_REMOTE" -eq 1 ]; then
    git branch -D "$BRANCH" 2>/dev/null
  fi
fi
```

## Multi-session usage (the 80-minute case)

If a single proof attempt takes longer than your token budget, the workflow is:

1. Session 1: skill is invoked. New worktree + branch. session_start. Rounds. Session_end on token-budget warning.
2. Session 2: human (or higher-level loop) re-invokes the skill, naming the existing branch / worktree. The skill RESUMES (Step 1's "RESUME setup"). session_start detects the existing handoff. Rounds continue.
3. Session N: same pattern. The handoff is the only context that crosses session boundaries.
4. When `proof_log_result.py` exits 4, 6, or 7, the LAST session runs the archive block (Step 5).

If a session dies abnormally (SIGTERM, crash, hard kill), the next `proof_session_start.py` detects the orphan, stashes any dirty edits to `proof-wip-<sha>-<sid>`, and auto-releases any qids the orphan claimed. Nothing is silently lost.

## Stop conditions (the only four)

1. `proof_log_result.py` returns 4 → round cap. Run Step 5.
2. `proof_log_result.py` returns 6 → converged. Run Step 5. The kept partial-result record is the artifact.
3. `proof_log_result.py` returns 7 → counterexample proven. Run Step 5. The kept disproof record is the artifact. Have a human re-verify before claiming a real result.
4. Human interrupts. Leave state on disk. Next session_start will detect the orphan.

## What the human should know

A `keep_disproof` record under `records/proof_*.json` means the verifier confirmed a finite primitive set whose rigorous lower bound on $\sum 1/(a \log a)$ exceeds the threshold. **This is a candidate counterexample, not a confirmed one.** Before treating as a real result:

1. Independently re-run `library.primitive_set_witness.verify_witness` on the witness payload (the record's `witness_payload` field).
2. Cross-check against the conjecture's $o(1)$ caveat: the conjecture says the sum is bounded by $1 + o(1)$ as $x \to \infty$. A witness at finite $x_\text{floor}$ that exceeds 1 is meaningful only if the implicit $o(1)$ at that $x$ is also small — a separate analytical estimate the agent must provide and the human must verify.
3. Search the literature for prior art. Erdős's primitive-set bound has decades of mathematician work behind it; an actual disproof would be huge news.
