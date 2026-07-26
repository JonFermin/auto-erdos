# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Autonomous combinatorial research loop. An agent repeatedly edits one file
(`strategy.py`), runs a deterministic verifier, and commits/discards. The
canonical agent instructions live in `program.md` — **read it before
starting any experimental loop**. `README.md` covers the design rationale.

This is a port of `karpathy-quant-auto-research` to Erdős-style problems.
The harness shape is the same — branch per run, edit one file, AST-dedup,
trial cap (default 20, per-problem override in `problems/*.json:trial_cap`
or env `AUTOERDOS_TRIAL_CAP`), gatekeeper script computes status — but
the statistics layer is removed (the verifier is deterministic; there's
no sample noise to deflate against).

`results.tsv`, `run.log`, `verifier_results.tsv`, and `worktrees/` are all
gitignored — `results.tsv` is the agent's experiment log (kept out of git
by design), `run.log` is transient stdout, `verifier_results.tsv` is the
harness audit trail. (`CLAUDE.md` itself IS tracked.)

`records/` is the **primary** committed artifact of a successful trial.
`log_result.py` writes `records/<tag>_<score>_<commit>.json` (and auto-commits
it as a follow-up commit) on every keep — the record carries the candidate
set, score, baseline, branch, thesis, and verifier_seconds. This is the
permanent claim that a problem's literature LB was beaten; everything else
(`results.tsv`, the trial cache, `best_so_far_*.json`) is local scratch.

`papers/` is the optional second committed artifact: an amsart LaTeX writeup
of a kept record, generated post-loop by `write_paper.py`. The paper is
downstream of the verifier — the construction itself is whatever
`records/<tag>_<score>_<commit>.json:candidate` says — so the paper cannot
fabricate a bound. Each `.tex` ships with a `.meta.json` sidecar capturing
the prompt-template hash, rendered-prompt hash, response hash, and full CLI
invocation, so a future reader can audit which prompt + record + model
produced which writeup. Paper generation is OFF by default in the autoresearch
loop (it's wall-clock-expensive and paid); see "Paper writeups" below.

## The one rule that matters

- **`strategy.py` is the ONLY file the agent edits.** Everything inside
  `generate_candidate()` (and helpers it calls) is fair game.
- **`prepare.py` is READ-ONLY.** It contains the verifier, the time budget,
  and the audit-trail writer. Do NOT modify it — log_result's AST hash and
  the per-problem cache assume the verifier is part of the fixed environment.
- **`problems/*.json` are READ-ONLY.** The literature baseline is fixed for
  the duration of the branch.
- **`library/` is READ-ONLY.** Importable constructions (Singer, Erdős–Turán,
  product-lifts) — call them, don't modify them. They're part of the fixed
  environment alongside the verifier.
- **`prompts/` is READ-ONLY at runtime.** `prompts/paper_writeup.md` is the
  frozen amsart template fed to `write_paper.py`; its sha256 lands in every
  generated paper's meta sidecar. Edit it deliberately and check in the
  change — casual edits silently break reproducibility.
- Do not add dependencies beyond `pyproject.toml` (numpy, pandas, pyarrow,
  python-sat, networkx). Use them deliberately — adding new deps mid-run
  isn't supported and breaks AST dedup if it changes the import graph.
- Do not read `verifier_results.tsv` or the harness trial cache directly.

## Commands

```bash
uv sync                                # install deps
PROBLEM_TAG=capset_n8 uv run strategy.py > run.log 2>&1   # one trial
grep "^score:\|^is_valid:\|^status_hint:\|^frontier:\|^budget_used_pct:" run.log
tail -n 50 run.log                     # crash trace if grep is empty
uv run log_result.py "thesis: [axis] ..."   # grade and append to results.tsv
uv run running_best.py                 # the bar a keep must clear (global ratchet)
uv run running_best.py --baseline      # problem's literature LB
uv run running_best.py --trials        # rows / trial cap
uv run running_best.py --headroom      # baseline / best / upper bound / status
uv run problem_brief.py                # FREE session-start cross-branch digest
uv run analyze.py                      # FREE structural diagnostics of best_so_far
```

`PROBLEM_TAG` defaults to `capset_n8`. Available problems are the
`problems/*.json` files (capset_n4–n10, sidon_100–sidon_10000). Each spec
carries `baseline`, `upper_bound`, and `status` (`open` / `sanity` /
`closed`); `log_result.py` refuses `closed` problems (exit 7) and hard-
rejects a thesis `[axis]` with ≥5 cross-branch failures and 0 keeps
(exit 6, `AUTOERDOS_FAMILY_CAP` overrides). The keep bar is globally
ratcheted across branches (`AUTOERDOS_GLOBAL_RATCHET=0` disables — debug
only). `AUTOERDOS_CACHE_DIR` points the whole cache layer elsewhere
(tests / dry runs).

A per-problem **trial cache** lives at
`~/.cache/auto-erdos/trial_cache_<PROBLEM_TAG>.tsv`. `log_result.py` writes
to it on every trial (AST hash + score + status) and reads from it to
reject AST-duplicate trials across all branches of the problem. To retire a
problem's accumulated history, `rm` the file.

A per-problem **best_so_far cache** lives at
`~/.cache/auto-erdos/best_so_far_<PROBLEM_TAG>.json`. `print_summary` writes
the highest-scoring valid candidate seen across all branches; agents may
read it via `prepare.load_best_so_far()` to warm-start swap-moves / SA from
the prior best. The agent does NOT write it — only the verifier path does.

Sibling caches (same directory, same read-only-for-agents rule unless noted):
`elites_<TAG>.json` — top-8 distinct valid candidates (`prepare.load_elites()`,
for recombination); `hypothesis_log_<TAG>.tsv` — every trial's status+thesis
across branches (`prepare.load_hypothesis_log()`); `notes_<TAG>.md` — the ONE
agent-written channel (`prepare.load_problem_notes()` /
`append_problem_notes()`) for literature findings and structural insights
that must survive across sessions.

## Experiment loop (from program.md)

1. Each run gets its own branch: `erdos-research/<tag>` (e.g. `erdos-research/apr28`).
2. Edit `strategy.py` → `git commit` → `uv run strategy.py > run.log 2>&1` → grep.
3. **Keep rule** (computed by `log_result.py`, not the agent):
   `is_valid == 1` AND `score > running_best`. `running_best` starts at the
   problem's literature LB and ratchets up with kept rows.
4. `keep` → advance branch. `discard`/`crash` → `git reset --hard HEAD~1`.
5. **Do not `git add results.tsv`** — it stays untracked.
6. **NEVER STOP** once the loop has begun — no "should I keep going?" prompts.
   Run until `log_result.py` exits 4 (trial cap) or you're manually interrupted.

## Verifier contracts

**capset family** (problems `capset_n4` … `capset_n10`):
- Input: iterable of length-n integer tuples, each coord in {0, 1, 2}.
- Validity: pairwise distinct AND no three distinct points
  a, b, c with a+b+c == 0 mod 3 elementwise.
- Score: |S| (cap set size).
- Verifier complexity: O(k² · n). Fast for n≤8; noticeable around k=2500 (n=10).

**sidon family** (problems `sidon_100` … `sidon_10000`; `sidon_100` and
`sidon_500` are `status: closed` — solved to their proven optimum):
- Input: iterable of distinct ints in [1, N].
- Validity: all pairwise sums a+b (a≤b, B₂ — includes 2a) distinct.
- Score: |S| (Sidon / B₂ set size).
- Verifier complexity: O(k²). Fast for any practical k.

**Wall-clock cap**: per-problem, set in `problems/<tag>.json:time_budget_s`.
Default 900s (15 min) when the field is absent. `AUTOERDOS_TIME_BUDGET_S`
env var overrides both. Per-problem defaults span 60s (sanity checks like
capset_n4, sidon_100) to 2400s (capset_n10, where the verifier alone is
non-trivial). Bumped from a flat 300s after the apr28 cap-set batch showed
exact-DFS sub-routines couldn't warm-start in 5 minutes.

## Output format (what `print_summary` emits)

```
---
problem:           capset_n8
family:            capset
score:             137.000000
is_valid:          1
verifier_seconds:  0.0234
baseline:          512
status_hint:       no_improvement | improvement_eligible | invalid
reason:            <verifier's one-line summary>
```

Empty grep output ⇒ the run crashed before reaching `print_summary`.

## Paper writeups

After a kept record, `write_paper.py` can render a frozen template
against that record and shell out to one or more model CLIs to generate
a writeup. The model gets the verified construction (the candidate set),
the literature baseline, and a strict rubric: prove validity, prove the
size, state the bound. It cannot fabricate the bound — the candidate is
fixed.

Two output modes:

| Mode | Template | Output | What it produces |
|---|---|---|---|
| `paper` (default) | `prompts/paper_writeup.md` | `.tex` | Full amsart writeup — title, abstract, theorem environments, ready to compile. ~5 min/call (Opus). |
| `proof` | `prompts/proof_only.md` | `.proof.md` | Lean plain-markdown proof with embedded LaTeX math — no preamble or section ceremony. ~30–60% cheaper. |

```bash
# Default: full paper, both models:
uv run write_paper.py records/capset_n8_137_a1b2c3d.json

# Lean proof from Opus only:
uv run write_paper.py records/sidon_500_26_a1c1c6b.json --mode proof --models opus

# Process every record without a paper:
uv run write_paper.py --all

# Process every record without a proof (re-runs even those with papers):
uv run write_paper.py --all --mode proof
```

Backends: `opus` shells out to `claude -p --model claude-opus-4-7` with
filesystem and web tools disabled. `codex` shells out to `codex exec
--sandbox read-only` (model id from codex's config by default; override
with `--codex-model`). Both CLIs must be on PATH; missing CLIs fail one
backend without affecting the other.

Outputs land in `papers/<tag>_<score>_<commit>__<model_id>.tex` plus a
`.meta.json` sidecar. Both files are intended to be committed alongside
the parent record.

**Auto-trigger.** `log_result.py` reads `AUTOERDOS_WRITEUP` after every
keep:
- unset / `0` / `off` / `false` → no writeup generation (the default — the
  autoresearch loop's wall-clock budget is for search, not writing)
- `1` / `on` / `all` → invoke both `opus` and `codex`
- comma list (e.g. `opus`, `opus,codex`) → that subset

`AUTOERDOS_WRITEUP_MODE` controls the mode (`paper` or `proof`, default
`paper`). Failures from `write_paper.py` are logged to stderr and
swallowed; a broken backend never undoes a kept record. The autoresearch
and deep-autoresearch skills do not set these env vars, so writeups stay
out of their hot path.

## Track 2 — proof attempts (proof_program.md)

Parallel harness for *proving/disproving claims* instead of beating
bounds. Canonical instructions: `proof_program.md` — read it before any
proof loop. Artifact: `proof_strategy.md` + `proof_lemmas/lemma_*.md`.
Verifier: `proof_prepare.py` — 7 LLM critics (ledger, sign, openness,
numerical, internal, strategy, falsify), deterministic lemma
`<!-- CHECK -->` blocks (stdlib Python falsification probes, run even in
critics-off mode), and per-problem deterministic witness verifiers in
`library/*_witness.py`. Gatekeeper: `proof_log_result.py` (exit 7 =
verified counterexample, exit 6 = converged partial result).

Problem specs live in `proofs/*.json` with `claim_status`:
- **open**: `erdos_mollin_walsh`, `erdos_gyarfas` (witness-decidable:
  one finite graph settles it), `frankl_union_closed` (witness-decidable:
  one finite family), `erdos_szemeredi_sum_product` (exploratory only).
- **proved** (rediscovery benchmarks, per the 2026-07-11 literature
  audit): `primitive_set_erdos` (Erdős #1196, proved May 2026,
  arXiv:2605.00301) and `erdos_primitive_set_basic` (Lichtman 2022).
  On these, `witness_valid == 1` means a verifier bug, never a result.

Track 2 commands:

```bash
uv run proof_session_start.py      # ALWAYS first — fetches origin, warns if the
                                   # branch base is behind origin/master, prints
                                   # handoff, FULL notes, ledger pointer, queue
uv run proof_ledger.py             # cross-branch lemma statuses (ledger.jsonl)
uv run proof_notes.py "<insight>"  # cumulative cross-branch notes channel
uv run proof_notes.py              # read the notes
uv run expert_brief.py             # one-page standalone brief of the open core
uv run formalize_lemma.py proof_lemmas/lemma_<id>.md   # Lean 4 skeleton (post-loop)
uv run proof_session_end.py "reason: ..."              # ALWAYS last — archives the
                                   # strategy to strategies/<problem>/, commits,
                                   # pushes the branch, opens a draft PR
```

Branch hygiene (the anti-progress-loss contract, 2026-07-25):
- Session branches fork from **origin/master** after `git fetch origin` —
  never from the stale local `master` ref.
- `proof_lemmas/ledger.jsonl` is the machine-readable lemma-status ledger
  (append-only, union-merged). `proof_log_result.py` exits 8 if a lemma
  file re-opens an id the ledger marks `disproved` — revised claims take
  a NEW id. It also auto-records status changes on every logged round.
- `proof_journal.jsonl`, `proof_open_questions.jsonl`,
  `proof_critic_log.jsonl`, and the ledger are `merge=union`
  (`.gitattributes`) so parallel session branches never conflict on them.
- New lemma files carry a session suffix (`lemma_<slug>__<session>.md`)
  so parallel sessions never collide on filenames; on a
  `proof_strategy.md` merge conflict, keep the newest session_close's
  version — each session's full narrative is archived under
  `strategies/<problem>/`.

Skills: `erdos-proof-attempt` drives rounds; `erdos-proof-ideation` fans
out N parallel proposer agents with distinct mathematical lenses + a
judge before rounds are spent — use it whenever the open-questions queue
is empty or a dead end was just documented.

Standing policy: **dual attack** — every open lemma gets a CHECK-block
falsification probe *before* proof effort is spent on it. The
witness contract for `primitive_set_erdos` carries `witness_min_x_floor`
(1e6): small-x witnesses are rejected because the claim's o(1) term
dominates there (this killed a spurious exit-7 from 2026-07-06).
