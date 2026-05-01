# auto-erdos — Track 2 (proof attempts)

Parallel to `program.md` (the Track 1 search loop). Where Track 1 hunts for
a *construction* that beats a literature lower bound, Track 2 attempts a
*proof* of an open claim. The harness shape is the same — edit one
artifact, run a verifier, run a gatekeeper, keep/discard — but the
artifact is `proof_strategy.md` (markdown + LaTeX, plus optional witness
JSON), the verifier is `proof_prepare.py` (five LLM critics + deterministic
witness checker), and the keep rule is structurally different: there is no
"score > baseline"; a round is kept either because it produces a verified
counterexample (`witness_valid == 1`) or because all critics return clean
findings on a partial / open writeup.

## Setup

To start a new proof attempt:

1. **Pick a problem**: choose a `PROOF_TAG` from `proofs/*.json`. Default
   `primitive_set_erdos` (the seed problem motivated by the ChatGPT failure
   on Erdős's primitive-set conjecture).
2. **Create a worktree on a fresh branch** off master, named
   `erdos-proof/<MMDD-HHMMSS-rnd>`. Use a worktree (`worktrees/<tag>/`) so
   parallel attempts on the same problem don't clash.
3. **Read the in-scope files** end-to-end before editing:
   - `proofs/<PROOF_TAG>.json` — claim, claim_status, given_facts ledger,
     witness contract.
   - `proof_strategy.md` — the editable artifact (currently a stub).
   - `proof_lemmas/README.md` — lemma file format.
   - This file (`proof_program.md`).
4. **Run `proof_session_start.py` FIRST**. Always. It prints the prior
   handoff, the live open-questions queue, and the most recent
   session_close reason.
5. **Confirm and go.**

## Ground rules (do not violate)

- `proof_strategy.md` and `proof_lemmas/lemma_*.md` are the ONLY artifact
  files the agent edits during a proof round. The journals and the
  open-questions queue are append-only state files; you append rows
  programmatically (see "Round cycle" below) but do not rewrite history.
- `prepare.py`, `log_result.py`, `library/*.py` are READ-ONLY. Track 1
  must not be perturbed by the proof loop.
- `proof_prepare.py`, `proof_log_result.py`, the `prompts/critic_*.md`
  templates, and `proofs/*.json` are READ-ONLY at runtime. Editing a
  critic prompt mid-loop silently breaks reproducibility — the prompt's
  sha256 lands in `proof_critic_log.jsonl`.
- No new dependencies. The witness verifier uses stdlib only.

## Resumability — the central design choice

A proof attempt may take many sessions. Every round ends with a
`git commit`. Every session ends with a written
`proof_session_handoff.md`. The next agent boots cold, reads the handoff
plus the live open-questions queue, and continues. State files:

- `proof_journal.jsonl` — append-only round/session log
- `proof_open_questions.jsonl` — append-only worklist (status: open ↔
  claimed ↔ resolved ↔ released)
- `proof_critic_log.jsonl` — append-only critic-finding log (indexed by
  proof_hash so unchanged proofs reuse cached findings)
- `proof_session_handoff.md` — overwritten each session_close, ≤ 1 page
- `proof_lemmas/lemma_<id>.md` — one file per lemma, status frontmatter

A session that ends abnormally (SIGTERM, crash) leaves a `session_open`
without a matching `session_close`. The next `proof_session_start.py`
detects the orphan, releases any orphan-claimed qids, and stashes any
in-progress edit work to a labelled stash ref (`proof-wip-<sha>-<sid>`)
— never silently discarded.

## Round cycle

Inside one session, repeat this body until a logical chunk of work is
done OR the token budget is low:

```bash
# 0. (Once per session, NOT every round.)
uv run proof_session_start.py
# Read its stdout. It prints the handoff, the open queue, the last close
# reason. Pick the lowest-numbered open qid unless the handoff suggests
# otherwise.

# 1. Claim the qid.
echo '{"qid":"Q3","status":"claimed","session_id":"<sid>","summary":"taking Q3","ts":"<iso>"}' \
    >> proof_open_questions.jsonl

# 2. Edit proof_strategy.md and/or a lemma file.
$EDITOR proof_strategy.md proof_lemmas/lemma_<id>.md

# 3. Commit (the round is one commit).
git add proof_strategy.md proof_lemmas/ proof_open_questions.jsonl
git commit -m "<short imperative summary of the change>"

# 4. (Every K=5 rounds OR at logical milestones.) Run the proof verifier.
uv run proof_prepare.py > run.log 2>&1
grep "^claim_status:\|^witness_valid:\|^verdict_hint:\|^critic_blocking_count:" run.log

# 5. Log the round (gatekeeper writes status, not you).
uv run proof_log_result.py "thesis: <one-line rationale>"
rc=$?
echo "exit=$rc"

# 6. Branch on exit code:
#    0 → status=keep_progress or discard. discard → git reset --hard HEAD~1.
#                                          keep_progress → advance.
#    2 → bad description; nothing logged.
#    3 → proof_hash duplicate of a prior round. git reset --hard HEAD~1
#        and pick a different angle.
#    4 → ROUND CAP. Stop. Run session_end + archive sequence.
#    5 → verifier crash. git reset --hard HEAD~1, inspect run.log.
#    6 → CONVERGED (clean critics, stable content, no open qids). The
#        partial-result record is your kept artifact. Run session_end.
#    7 → COUNTEREXAMPLE PROVEN. Stop. Have a human re-run the witness
#        verifier independently before claiming a real result.

# 7. Append progress to the journal (round summary).
echo '{"event":"round","session_id":"<sid>","round_n":<n>,"ts":"<iso>","summary":"...","files_touched":[...]}' \
    >> proof_journal.jsonl

# 8. (When done.) Resolve the qid.
echo '{"qid":"Q3","status":"resolved","session_id":"<sid>","summary":"<outcome>","ts":"<iso>"}' \
    >> proof_open_questions.jsonl
```

## Session end

When the token budget is low OR a logical milestone is reached, call:

```bash
uv run proof_session_end.py "reason: <one-line stop reason>" < /path/to/handoff_template.md
```

`proof_session_end.py`:
1. Reads handoff from stdin (or writes a default template).
2. Overwrites `proof_session_handoff.md` with the new handoff.
3. Appends a `session_close` event to `proof_journal.jsonl`.
4. `git add -A && git commit` of all dirty journal/handoff/lemma files.
5. Removes `.proof_session_active`.

## Keep rule (computed by `proof_log_result.py`)

```
if witness_valid == 1:                                    status = keep_disproof
elif critic_blocking == 0
     AND verdict in {partial_result, open}
     AND proof_hash novel:                                status = keep_progress
else:                                                      status = discard
```

`witness_valid == 1` requires a `<!-- WITNESS -->` block in
`proof_strategy.md` whose JSON payload survives
`library.primitive_set_witness.verify_witness`. The verifier uses
`mpmath`-free stdlib `decimal` arithmetic with ULP-bumped `math.log` so
the lower bound on $\sum 1/(a \log a)$ is rigorous to ~50 decimal
digits. If you see `witness_valid == 1`, the counterexample is real (up
to a 4-ULP slack documented in the verifier).

## Convergence

The agent does NOT decide convergence. `proof_log_result.py` does, by:

- The most recent STABLE_CHECKPOINT_COUNT (=3) rows in
  `proof_results.tsv` all have the same `proof_hash`, AND
- All 3 of those rows have `verdict_hint in {partial_result, open}` and
  `critic_blocking == 0`, AND
- The live open-questions queue is empty.

When all three hold, exit 6 fires after the row is logged. The agent
should run session_end and archive the branch.

## Idea seeds (when stuck on the primitive-set seed problem)

- **Stratify by Omega(a)**. For each integer $a$ with $\Omega(a) = k$,
  bound the contribution of the stratum. F3 gives the per-stratum sum
  $1 - (c+o(1)) k^2/2^k$, all strictly less than $1$.
- **Argue the cross-stratum case**. A primitive $A$ is contained in the
  union $\bigcup_k A_k$, but generically uses a *subset* of each
  stratum. The challenge is bounding how much of each stratum a
  primitive set can use.
- **Search for counterexamples in the small**. Run
  `library.primitive_set_witness.verify_witness` on candidate primitive
  sets you can construct. If you find one whose rigorous lower bound
  exceeds 1, commit it as a `<!-- WITNESS -->` block.
- **Partial / conditional results**. If the proof structure has gaps you
  can't close, write up "this remains open; here is what was ruled out"
  — that's a valid partial-result keep.

## Stop conditions (the only four)

1. `proof_log_result.py` returns exit 4 → round cap reached. Run
   session_end + archive.
2. `proof_log_result.py` returns exit 6 → converged. The partial-result
   record is your kept artifact. Run session_end + archive.
3. `proof_log_result.py` returns exit 7 → counterexample proven. STOP.
   Run session_end + archive. Have a human independently re-run
   `library.primitive_set_witness.verify_witness` before claiming a
   real result.
4. Human interrupts. Leave state on disk; the next session_start
   detects the orphan and releases claims.

## What NOT to do

- Don't claim resolution of an open conjecture without a verified
  witness. The openness critic + the `_compute_verdict_hint`
  defense-in-depth check both fire on resolution phrasing.
- Don't read F2's unsigned big-O as positive. The sign critic has a
  hard-coded clause that emits `unsigned-O-sign-confusion`.
- Don't edit critic prompts mid-loop. Their sha256 is logged into
  `proof_critic_log.jsonl`; an edit silently breaks reproducibility.
- Don't delete a lemma file. If a lemma turns out to be wrong, set
  `status: disproved` and keep the body — the dead end is part of the
  audit trail.
- Don't run `proof_prepare.py` every round. It's wall-clock expensive
  (~5 critic calls × ~30s each on a cold cache). Run it every K=5
  rounds, or at a logical milestone.
