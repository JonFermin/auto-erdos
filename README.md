# auto-erdos

Autonomous research loop on Erdős-style combinatorial problems. Port of
[karpathy-quant-auto-research](../karpathy-quant-auto-research) — same
harness shape, but the oracle is a deterministic verifier instead of a
backtest, so the statistics layer collapses to "did the verifier accept it,
and is the score better than the running best."

## Status

Active. The loop has produced real records (see `records/`): sidon_100 → 12
(now proven exact and closed), sidon_500 → 26 (proven exact via OGR-27,
closed), sidon_1000 → 35, sidon_3000 → 59. Cap-set problems remain open
above their literature LBs.

## Design

Three ports were considered (see the original setup prompt). This repo
implements **Port 1: bound-improvement (FunSearch-shaped)** because it has
the densest feedback signal — most edits produce *some* valid candidate,
and the question is just whether it scores higher.

- The agent edits **one file** (`strategy.py`). Everything else is read-only.
- The verifier (`prepare.verify`) is deterministic and fast.
- The grader (`log_result.py`) is the sole gatekeeper — the agent never
  chooses keep/discard. The keep bar is **globally ratcheted**: a keep must
  beat the best valid score across ALL branches of the problem, not just
  this branch's.
- Trials are AST-deduplicated across all branches of a given problem via a
  per-problem cache at `~/.cache/auto-erdos/trial_cache_<PROBLEM_TAG>.tsv`,
  and hypothesis *families* are gated: an `[axis]` with ≥5 cross-branch
  failures and zero keeps is rejected (exit 6) until a new axis is tried.
- 20-trial cap per branch (per-problem overrides in the spec JSONs).
- Problems carry `upper_bound` and `status` (`open` / `sanity` / `closed`);
  the grader refuses closed problems (exit 7).
- Cross-branch memory beyond the single best: an 8-slot **elite archive**
  (`prepare.load_elites()`) for recombination, a public hypothesis log,
  an agent-written **notes channel** (literature findings persist across
  sessions), plus free read-only tools `problem_brief.py` (session-start
  digest) and `analyze.py` (structural diagnostics — no trial cost).

## What dropped from the quant harness

| Quant feature | Status here | Why |
|---|---|---|
| IS/OOS split | dropped | configurations and proofs don't have sample noise |
| Bootstrap CI on the metric | dropped | verifier is deterministic |
| Walk-forward folds | dropped | no time-series structure to fold |
| Sharpe deflation across N trials | dropped | no sampling distribution to correct against |
| `SHOW_OOS=0` masking | dropped | nothing to mask |
| T+1 execution shift | dropped | no execution semantics |

What remains: branch-per-run, AST-dedup, trial-cap, audit-trail-as-source-
of-truth, gatekeeper computes status.

## Currently shipped problems

### capset family (cap sets in F_3^n: no 3-term AP, scored by |S|)

| Tag | n | Baseline | UB | Status | Notes |
|---|---|---|---|---|---|
| `capset_n4` | 4 | 20 | 20 | sanity | Exact value |
| `capset_n5` | 5 | 45 | 45 | sanity | Exact value (Pellegrino) |
| `capset_n6` | 6 | 112 | 112 | sanity | Exact (Hill construction, Potechin optimality) |
| `capset_n7` | 7 | 236 | 288 | open | Real but decades-hard headroom |
| `capset_n8` | 8 | 496 | 864* | open | Default. *trivial 3× tripling of n=7 UB |
| `capset_n9` | 9 | 1082 | 2592* | open | Big gap |
| `capset_n10` | 10 | 2474 | 7776* | open | Verifier is slow at this size |

### sidon family (Sidon / B₂ sets in [1, N]: all pairwise sums distinct)

| Tag | N | Baseline | UB | Status | Notes |
|---|---|---|---|---|---|
| `sidon_100`   |   100 |  11 |  12 | **closed** | F₂(100)=12 exactly (OGR-13 length 106 > 99); 12 achieved |
| `sidon_500`   |   500 |  23 |  26 | **closed** | F₂(500)=26 exactly (OGR-27 length 553 > 499); 26 achieved |
| `sidon_1000`  |  1000 |  32 |  38 | open | Best achieved 35; UB via Lindström |
| `sidon_3000`  |  3000 |  53 |  63 | open | Best achieved 59; UB via Lindström |
| `sidon_10000` | 10000 | 102 | 111 | open | Baseline = library Singer window; most headroom |

`status: sanity` problems confirm the loop terminates without false
positives (one null-control trial). `status: closed` problems are solved —
`log_result.py` refuses to grade them (exit 7).

### Adding zoo problems — what makes a target winnable

New problems earn their slot by three criteria: (1) the **verifier** is
cheap and deterministic (O(k²)-ish membership checking); (2) the **library
reproduces the literature LB** as a seed — a problem is not "open for the
loop" until the seed starts at the LB, otherwise every trial is spent
re-deriving known results; (3) the record is **search-soft** — set by
computation (rulers, windowed algebraic constructions, SAT-able sizes)
rather than by deep theory, so an LLM+search loop has a real shot. Every
record this loop has produced came from knowledge (OGR marks, Singer
multiplier orbits, GF(q³) constructions) composed with local search.

## Commands

```bash
uv sync
PROBLEM_TAG=capset_n8 uv run strategy.py > run.log 2>&1
uv run log_result.py "thesis: <one-liner>"
uv run running_best.py
```

See [`program.md`](./program.md) for the full agent loop.

## Layout

```
auto-erdos/
├── prepare.py            # READ-ONLY verifier + driver helpers
├── strategy.py           # AGENT EDITS — generate_candidate()
├── log_result.py         # gatekeeper (status computed here, not by agent)
├── running_best.py       # state probe (keep bar, baseline, trials, --headroom)
├── analyze.py            # FREE structural diagnostics of best_so_far
├── problem_brief.py      # FREE session-start cross-branch digest
├── library/              # READ-ONLY literature-grade constructions
├── problems/             # frozen problem specs (baseline, upper_bound, status)
├── records/              # committed proof-of-keep snapshots
├── papers/               # optional post-loop writeups (write_paper.py)
├── summaries/            # graceful-exit branch summaries (committed)
├── worktrees/            # per-branch worktrees (gitignored)
├── program.md            # agent loop spec
├── CLAUDE.md             # repo-level Claude Code rules
└── README.md
```

## Future ports

- **Port 2: counterexample search** — conjectures of the form
  "for all n ≥ N, P(n) holds." Most trials produce nothing, so the
  information density is low; need richer logging in the description column.
- **Port 3: formalized proof attempts (Lean / mathlib)** — agent fills
  named `sorry`s in a human-authored skeleton; metric is `sorry_count`.
  Hardest port — most edits don't typecheck.

Both are out of scope for v1.
