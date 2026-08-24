# auto-erdos — Track 2 (proof attempts)

Parallel to `program.md` (the Track 1 search loop). Where Track 1 hunts for
a *construction* that beats a literature lower bound, Track 2 attempts a
*proof* of an open claim. The harness shape is the same — edit one
artifact, run a verifier, run a gatekeeper, keep/discard — but the
artifact is `proof_strategy.md` (markdown + LaTeX, plus optional witness
JSON), the verifier is `proof_prepare.py` (seven LLM critics +
deterministic lemma CHECK blocks + deterministic witness checker), and the
keep rule is structurally different: there is no "score > baseline"; a
round is kept either because it produces a verified counterexample
(`witness_valid == 1`) or because all critics return clean findings on a
partial / open writeup.

## Setup

To start a new proof attempt:

1. **Pick a problem**: choose a `PROOF_TAG` from `proofs/*.json`. Check
   `claim_status` FIRST:
   - `open` — a genuine target. Current open problems:
     `erdos_mollin_walsh` (no three consecutive powerful integers),
     `erdos_gyarfas` (power-of-2 cycles; witness-decidable — one finite
     graph settles it), `frankl_union_closed` (witness-decidable — one
     finite family settles it), `erdos_szemeredi_sum_product` (realistically
     beyond this loop; exploratory only).
   - `proved` — a REDISCOVERY BENCHMARK, not an open problem. As of the
     2026-07-11 literature audit this includes `primitive_set_erdos`
     (Erdős #1196, proved May 2026, arXiv:2605.00301) and
     `erdos_primitive_set_basic` (Lichtman 2022). On these, the goal is
     reconstructing the known argument to calibrate harness changes; a
     `witness_valid == 1` outcome is a verifier BUG by definition, never a
     result. See each spec's `literature_resolution` and `benchmark_mode`.
2. **Create a worktree on a fresh branch** off **`origin/master`** —
   ALWAYS `git fetch origin` first, then
   `git worktree add worktrees/<tag> -b erdos-proof/<tag> origin/master`.
   Never fork from the local `master` ref: it goes stale (nothing in the
   loop updates it), and a stale base means merged sibling-session results
   (disproofs, lemma statuses, strategy sections) are invisible to you.
   `proof_session_start.py` fetches origin and WARNS when the branch base
   is behind `origin/master` — treat that warning as "abandon this branch
   and re-fork" unless work is already committed here. Name the branch
   `erdos-proof/<MMDD-HHMMSS-rnd>`; the worktree keeps parallel attempts
   on the same problem from clashing.
3. **Read the in-scope files** end-to-end before editing:
   - `proofs/<PROOF_TAG>.json` — claim, claim_status, given_facts ledger,
     witness contract.
   - `proof_strategy.md` — the editable artifact (currently a stub).
   - `proof_lemmas/README.md` — lemma file format.
   - `uv run proof_ledger.py` — cross-branch lemma statuses. Ids the
     ledger marks `disproved` are DEAD: a revised claim takes a NEW id
     (e.g. `chain_locality` → `chain_locality_r3`); resurrecting a
     disproved id is rejected at log time (exit 8).
   - This file (`proof_program.md`).
4. **Run `proof_session_start.py` FIRST**. Always. It prints the prior
   handoff, the cumulative cross-branch notes, the live open-questions
   queue, and the most recent session_close reason.
5. **If the open-questions queue is empty or stale, run ideation before
   burning rounds**: the `/erdos-proof-ideation` skill fans out parallel
   proposer agents — problem-native lenses from the spec's
   `ideation_lenses` array, plus wildcard / analogy-miner / fresh-eyes /
   revivalist slots — against the spec + dead-end ledger, ranks them
   with a three-judge panel (rigor / novelty / upside), and queues each
   judge's top pick as a new qid tagged `kind: explore` or
   `kind: exploit`. Serial single-idea sessions are the weakest search
   over proof space — don't default to them.
6. **Confirm and go.**

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

## Dual attack — standing policy

Every session pushes the current minimal open lemma on BOTH fronts
simultaneously:

- **Prove it**: develop the argument in the lemma file / proof_strategy.md.
- **Falsify it**: write a `<!-- CHECK -->` block (stdlib Python,
  assert-style; see `proof_lemmas/README.md`) probing the lemma on
  concrete instances — boundary values, degenerate objects, regimes where
  an o(1) is large — and, where the problem has a witness contract, feed
  candidate counterexamples to the witness verifier.

**Write the CHECK before writing the proof.** Whichever front gives signal
first redirects the session: a failing CHECK kills the lemma in seconds
(set `status: disproved`, pick a new direction) instead of costing the
full session the trading-decomposition dead end cost on 2026-07-11. A
passing CHECK is evidence, not proof — but it is also a permanent
regression test: `proof_prepare.py` re-runs every CHECK block every time,
in critics-on AND critics-off modes, and a failure is a BLOCKING finding.

## Variance policy — standing (adopted 2026-08-23)

The keep rule rewards verifiability, not novelty: computational
campaigns always produce clean partial results, while half-formed
conceptual leaps attract critic findings — so left alone, the loop
drifts into census/SAT grinding (R38–R56 of `erdos_gyarfas` is the
case study; its one great idea, the R55 covering reframing, arrived
55 rounds in). These rules push back. None of them is enforced by the
gatekeeper — the handoff discipline below is what makes them stick.

### 1. Pre-committed exit criteria (mandatory for every program)

A **program** is any named, multi-session sequence of qids in service
of one mechanism or approach. The strategy section that DECLARES a
program must state, up front: (a) the falsifiable success criterion,
(b) the negative-closure criterion (what observation closes the
program as converged negative knowledge), and (c) a session budget.
Extending a program past its budget requires an explicit journal note
saying what changed. Precedent: the R51/R56 pre-commitment is the only
thing that ended a 56-round program — make the pattern the default,
not a late save.

The session handoff must carry a `program: <name> — session <m> of
<budget>` line; §2's "current program" means the program this line
names. When no program has been declared yet, the problem
(`PROOF_TAG`) itself is the current program.

### 2. Exploration quota

Every session handoff must state `consecutive exploit sessions on
current program: k`. When `k >= 2`, the next session MUST either
(i) claim a `kind: explore` qid (tagged at queue time by ideation —
see the skill for which winners get the tag), or (ii) open with a
fresh `/erdos-proof-ideation` fan-out AND claim one of the
`kind: explore` qids it queues as this session's first qid — running
the fan-out alone does not discharge the quota. Momentum is
useful; unbounded momentum is how one program consumes two months.
The "pick the lowest-numbered open qid" default in the Round cycle is
OVERRIDDEN by this quota when it fires.

`kind` lives on the qid's INITIAL `open` row (written at ideation
time) and is optional metadata everywhere else: later claim/resolve
rows need not repeat it, and harness-appended rows (orphan
auto-release) never carry it — so read a qid's kind from its first
row, and treat a qid with no kind anywhere as `exploit`.

Computing `k` for the handoff (the session_end template MUST carry the
line — nothing in the harness computes it for you): a session counts
as EXPLORE if it claimed a `kind: explore` qid, spent its rounds in a
critics-off sandbox burst, or was an ideation-only / literature-scout
session that claimed no exploit qid; otherwise it is EXPLOIT. `k` =
prior handoff's `k` + 1 if this session was exploit on the same
program, reset to 0 if it was explore or the program changed.
Bootstrap/repair: if the prior handoff lacks the line for ANY reason
(pre-policy handoff, session_end's built-in default template, a crash
left a stale handoff), initialize from this session alone (`k = 1` if
it was exploit, else `0`). If session_start reported an orphan
session, classify the orphan from its surviving queue/journal rows
and count it too; queue rows with `session_id: ideation-<ts>` newer
than the prior handoff mean an ideation pass ran in between — treat
`k` as reset.

### 3. Conjecture register

Every session that logged at least one round appends EXACTLY one new
falsifiable observation (<= 3 lines) to the notes channel before
session_end, formatted:
`CONJECTURE: <statement> | test: <how it could be killed>`.
A reframing, a suspected invariant, a pattern in the data — minted
this session, not restated. A session with nothing genuinely new
appends NOTHING — never mint filler: session_start prints the notes
in full but hard-truncates the OLDEST content past 100k chars, so
padding evicts the dead-end ledger, the one thing the loop cannot
afford to forget. When a conjecture dies, append
`CONJECTURE-KILLED: <ref> — <how>` so ideation passes can filter the
register. Rationale: nothing else in the loop rewards introducing a
new mathematical object, and reframings are where the real progress
has come from. Ideation passes read these lines as seed material.

### 4. Explore/consolidate cadence (critics-off bursts)

Critics-off mode (`AUTOERDOS_PROOF_CRITICS=0`) is not just a debug
switch — it is the sanctioned EXPLORE mode. An explore session may
develop speculative material under a dedicated
`## Sandbox (unscreened speculation)` section of `proof_strategy.md`.
Rules that keep the sandbox safe:

- Before the next critics-ON milestone run, every sandbox item is
  either PROMOTED (rewritten rigorously into a numbered section or a
  lemma file, with CHECK probes) or PRUNED to the notes channel. The
  sandbox section is EMPTY at every consolidation milestone.
  Enforcement is handoff + preflight: a session ending with a
  non-empty sandbox MUST add the handoff line `SANDBOX: <n> items
  pending — promote/prune before any critics-ON proof_prepare run`,
  and every session confirms the sandbox is empty before its FIRST
  critics-ON `proof_prepare.py` (the env var dies with the session
  that set it; a fresh session is critics-ON by default).
- Every `proof_log_result.py` thesis logged while critics are off
  starts `thesis: [critics-off] ...` — keep_progress records minted
  in this mode are otherwise indistinguishable from critic-screened
  partials in `records/` and `proof_results.tsv`.
- Resolution phrasing is banned in the sandbox like everywhere else —
  the `_compute_verdict_hint` defense-in-depth scans the whole file
  and does not know the section is speculative.
- A `<!-- WITNESS -->` block never goes in the sandbox — the witness
  regex scans the whole file, sandbox included. Keep `<!-- CHECK -->`
  blocks out too, for the opposite reason: they only EXECUTE from
  `proof_lemmas/lemma_*.md`, so a sandbox CHECK is dead text that
  reads like evidence but was never run.

Cadence: after any consolidation milestone (critics-on pass, zero
blocking), the next session on the problem may open with a critics-off
burst by default.

### 5. Portfolio rotation and the literature scout

- When a problem's queue is empty AND its latest program just closed,
  the next session must run ideation — UNLESS the last ideation pass
  on this problem queued nothing (the novelty-floor ground rule
  fired). In that case do NOT re-queue: let the convergence gate see
  the empty queue (exit 6 is a designed terminal, not a failure), run
  `expert_brief.py`, and rotate to another open problem. Either way,
  seriously weigh switching `PROOF_TAG` to another open spec
  (`frankl_union_closed`, `erdos_mollin_walsh`) rather than
  reflexively re-entering the same problem.
- Rotation floor (computable): the dated appends in
  `~/.cache/auto-erdos/proof_notes_<tag>.md` are the only
  cross-branch, cross-problem trace of session activity. When
  launching a NEW attempt, compare recent append dates across all
  `proof_notes_*.md`; if the last four sessions' worth of appends all
  belong to one problem, this attempt MUST target a different open
  spec. Cross-problem technique transfer (entropy jumping into
  union-closed, Pell structure into powerful triples) is a variance
  source a one-problem loop never sees.
- A **literature-scout session** is a sanctioned session type: no
  strategy edits, no rounds — sweep recent literature (arXiv listings,
  surveys, adjacent solved problems) for transplantable techniques,
  write findings WITH CITATIONS to the notes channel, and queue qids
  for promising transplants. Spec `given_facts` are read-only at
  runtime; a scout that finds a fact worth pinning proposes the spec
  edit on a harness branch for human review instead of editing it
  mid-loop.

### 6. Ideation is a panel, not a filter

`/erdos-proof-ideation` details live in the skill; the program-level
contract is: proposals are generated under problem-native lenses (the
spec's `ideation_lenses`) plus deliberately-decorrelated slots
(wildcard, analogy miner, fresh-eyes with an ablated context pack,
revivalist over released/abandoned directions), and selection takes
each judge's top pick — never a consensus ranking. Consensus selection
recreates the low-variance monoculture this policy exists to break.

## Round cycle

Inside one session, repeat this body until a logical chunk of work is
done OR the token budget is low:

```bash
# 0. (Once per session, NOT every round.)
uv run proof_session_start.py
# Read its stdout. It prints the handoff, the open queue, the last close
# reason. Pick the lowest-numbered open qid unless the handoff suggests
# otherwise — EXCEPT when the exploration quota fires (Variance policy
# §2: handoff says consecutive exploit sessions >= 2), which overrides
# the default with a kind: explore qid or a fresh ideation fan-out.

# 1. Claim the qid.
echo '{"qid":"Q3","status":"claimed","session_id":"<sid>","summary":"taking Q3","ts":"<iso>"}' \
    >> proof_open_questions.jsonl

# 2. Edit proof_strategy.md and/or a lemma file.
$EDITOR proof_strategy.md proof_lemmas/lemma_<id>.md

# 3. Commit (the round is one commit).
#    NEW lemma files are named lemma_<slug>__<MMDD-HHMMSS-rnd>.md (session
#    suffix from your session_id) so parallel sessions never collide on
#    filenames at merge time. The lemma's `id:` stays semantic and
#    session-free — the ledger tracks status by id.
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
#    8 → LEDGER VIOLATION. A lemma file re-opens an id the ledger has as
#        disproved. Nothing logged. Rename the revised claim to a NEW id
#        (and read the disproof it collided with before re-deriving it).

# 7. Append progress to the journal (round summary).
echo '{"event":"round","session_id":"<sid>","round_n":<n>,"ts":"<iso>","summary":"...","files_touched":[...]}' \
    >> proof_journal.jsonl

# 8. (When done.) Resolve the qid.
echo '{"qid":"Q3","status":"resolved","session_id":"<sid>","summary":"<outcome>","ts":"<iso>"}' \
    >> proof_open_questions.jsonl

# 9. Feed the cumulative notes channel (cross-branch, survives everything).
#    MANDATORY whenever you kill an approach, restate the minimal open
#    lemma, or learn something from the literature:
uv run proof_notes.py "approach <name> failed because <why>; would revive if <what>"
```

## Session end

When the token budget is low OR a logical milestone is reached, call:

```bash
uv run proof_session_end.py "reason: <one-line stop reason>" < /path/to/handoff_template.md
```

The handoff you pipe in MUST include the exploration-quota line
`consecutive exploit sessions on current program: <k>` (Variance
policy §2 defines `k` and its bootstrap) — the next session's quota
decision reads it from there.

`proof_session_end.py`:
1. Reads handoff from stdin (or writes a default template).
2. Overwrites `proof_session_handoff.md` with the new handoff.
3. Archives `proof_strategy.md` to `strategies/<problem>/<session>.md`
   and regenerates that folder's `INDEX.md`. This is the parallel-merge
   insurance: on a `proof_strategy.md` merge conflict, keep the version
   whose session_close is newest — every session's full narrative is
   already preserved under `strategies/`.
4. Appends a `session_close` event to `proof_journal.jsonl`.
5. `git add -A && git commit` of all dirty journal/handoff/lemma files.
6. Removes `.proof_session_active`.
7. Pushes the session branch to origin and opens a draft PR when none
   exists (best-effort; `--no-push` / `AUTOERDOS_NO_PUSH=1` skips).
   An unpushed branch is an invisible branch — never rely on a human
   remembering to publish it.

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

## Cumulative notes channel

`~/.cache/auto-erdos/proof_notes_<PROOF_TAG>.md` is the ONE cross-branch,
cross-session knowledge channel (Track 2's analogue of Track 1's
`notes_<TAG>.md`). Session handoffs are per-branch and one page; parallel
worktrees can't see each other's handoffs at all. The notes file is where
insight compounds instead of being re-derived. Read: printed IN FULL by
`proof_session_start.py` (100k-char pathology guard only), or
`uv run proof_notes.py`.
Write: `uv run proof_notes.py "<insight>"` or
`proof_prepare.append_proof_notes(...)`. Required content discipline:
approach → why it failed → what would revive it; the current minimal open
lemma, stated formally; literature findings with citations; numerical
constants future sessions will need.

## Lemma ledger (machine-readable statuses)

`proof_lemmas/ledger.jsonl` is the cross-branch source of truth for lemma
statuses — append-only JSONL, union-merged by git (`.gitattributes`), so
parallel branches never conflict on it. The latest entry per `lemma_id`
wins. `proof_log_result.py` appends entries automatically whenever a
logged round changes a lemma's frontmatter status, and REJECTS a round
(exit 8) whose lemma files re-open an id the ledger has as `disproved`.

Rules:
- Lemma ids are one global namespace (one shared `proof_lemmas/` dir).
- A revised claim takes a NEW id; never resurrect a disproved one.
- `uv run proof_ledger.py` lists statuses; `--check` dry-runs the gate;
  `--sync` records manual frontmatter edits made outside a logged round.
- `AUTOERDOS_LEDGER_ENFORCE=0` disables the gate (debug only — journal why).

## Formalization ladder (Lean)

Informal review — even seven critics deep — misses exactly the
quantifier/sign errors this problem family is famous for. The ladder:

1. **exploration** — markdown + LaTeX in `proof_lemmas/`;
2. **critic screen** — 7-critic pass clean at a milestone;
3. **numeric screen** — `<!-- CHECK -->` probes pass;
4. **Lean skeleton** — for a load-bearing `status: proved` lemma that has
   survived 3+ stable rounds, run
   `uv run formalize_lemma.py proof_lemmas/lemma_<id>.md`. It renders the
   frozen `prompts/lean_formalize.md` template, shells to `claude -p`
   (same provenance chain as `write_paper.py` — hashes in a `.meta.json`
   sidecar), and writes `lean/<tag>__<id>.lean`. The prompt instructs the
   model to report `-- DEFECT FOUND:` when the informal statement does not
   survive faithful formalization — that outcome is a RESULT (fix the
   lemma), not a failure;
5. **human compile** — a human (or CI with a Lean toolchain) runs
   `lake build` against mathlib4 and audits FIDELITY NOTES + `sorry`s.

Rungs 4-5 are post-loop, wall-clock-expensive, and optional per-lemma; a
final claimed proof of an open problem should not be announced without
them.

## Expert-brief escalation

A stable reduction is an artifact even while unproven. When open lemmas
have survived 2+ sessions (`proof_session_end.py` prints a hint), run:

```bash
uv run expert_brief.py            # briefs/<tag>_<date>.md
```

It deterministically renders a self-contained one-page statement: the
claim, the facts ledger, every open lemma verbatim (these ARE the minimal
open problems), the ruled-out approaches, and the notes tail. Hand it to
a human expert, post it, or feed it to a fresh `/erdos-proof-ideation`
fan-out.

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
- Don't treat a `claim_status: proved` spec as an open problem, and never
  report `witness_valid == 1` on one as a discovery — on a proved claim a
  valid witness is impossible and means the verifier is broken. File it as
  a bug.
- Don't re-enter an approach the notes channel or a
  `status: disproved/abandoned` lemma documents as dead without stating
  what is different this time (the strategy critic flags this).
- Don't declare a multi-session program without pre-committed exit
  criteria and a session budget (Variance policy §1), and don't extend
  one past its budget without a journal note saying what changed.
- Don't read F2's unsigned big-O as positive. The sign critic has a
  hard-coded clause that emits `unsigned-O-sign-confusion`.
- Don't edit critic prompts mid-loop. Their sha256 is logged into
  `proof_critic_log.jsonl`; an edit silently breaks reproducibility.
- Don't delete a lemma file. If a lemma turns out to be wrong, set
  `status: disproved` and keep the body — the dead end is part of the
  audit trail.
- Don't run `proof_prepare.py` every round. It's wall-clock expensive
  (~7 critic calls × ~30s each on a cold cache). Run it every K=5
  rounds, or at a logical milestone. (The deterministic parts — lemma
  CHECK blocks and the witness verifier — are cheap; critics-off mode
  gives you just those.)
- Don't edit `prompts/critic_strategy.md` / `prompts/critic_falsify.md`
  any more casually than the original five — same sha256-logged
  reproducibility contract.

## Critics-off mode (`AUTOERDOS_PROOF_CRITICS=0`)

Set `AUTOERDOS_PROOF_CRITICS=0` (or `off` / `false` / `no`) before the
loop to skip the LLM critic pass entirely. `proof_prepare.py` then:

- Still runs the deterministic witness verifier (a `keep_disproof`
  always requires a real verifier-accepted witness).
- Still runs every lemma `<!-- CHECK -->` block — a failing check is a
  BLOCKING finding even with critics off, so critic_blocking can be
  non-zero in this mode.
- Still applies the `_compute_verdict_hint` defense-in-depth — a proof
  on an `open` claim that contains resolution phrasing (`the conjecture
  is false`, `we disprove`, `qed`, …) without a witness is forced to
  `verdict_hint=blocked` regardless.
- Skips the seven `claude -p` critic calls; `reason=critics_off: …`, and
  the blocking/warn counts reflect only the deterministic checks above.

Trade-off: faster rounds (~30× wall-clock under cold cache), more raw
exploration, no critic-driven WARN findings to nudge the agent.
Speculative directions that the openness/sign critics would have flagged
slip through into the body — the agent must self-police more carefully.

The conservative gates that DO still apply:
- Witness verifier on any `<!-- WITNESS -->` block.
- Resolution-string defense-in-depth (above).
- proof_hash dedup in `proof_log_result.py` (no real change ⇒ exit 3).
- Round cap and convergence detection.

Recommended use: bursts of speculative work; flip back to `AUTOERDOS_PROOF_CRITICS=1`
(or unset) at consolidation milestones to re-screen the body with the
full critic panel before claiming convergence. This mode is the
sanctioned EXPLORE half of the explore/consolidate cadence — see
Variance policy §4 for the sandbox-section rules that keep speculative
material quarantined from the critic-screened body.
