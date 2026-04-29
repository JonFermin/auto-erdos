# auto-erdos

Autonomous research loop on Erdős-style combinatorial problems. Port of
[karpathy-quant-auto-research](../karpathy-quant-auto-research) — same
harness shape, but the oracle is a deterministic verifier instead of a
backtest, so the statistics layer collapses to "did the verifier accept it,
and is the score better than the running best."

## Status

Pre-research. The harness is up; no experimental branches have run yet.

## Design

Three ports were considered (see the original setup prompt). This repo
implements **Port 1: bound-improvement (FunSearch-shaped)** because it has
the densest feedback signal — most edits produce *some* valid candidate,
and the question is just whether it scores higher.

- The agent edits **one file** (`strategy.py`). Everything else is read-only.
- The verifier (`prepare.verify`) is deterministic and fast.
- The grader (`log_result.py`) is the sole gatekeeper — the agent never
  chooses keep/discard.
- Trials are AST-deduplicated across all branches of a given problem via a
  per-problem cache at `~/.cache/auto-erdos/trial_cache_<PROBLEM_TAG>.tsv`.
- 20-trial cap per branch.

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

| Tag | n | Baseline | Notes |
|---|---|---|---|
| `capset_n4` | 4 | 20 | Exact value — sanity check |
| `capset_n5` | 5 | 45 | Exact value (Pellegrino) — sanity check |
| `capset_n6` | 6 | 112 | Exact value (Edel) — sanity check |
| `capset_n7` | 7 | 236 | Lower bound, upper bound open |
| `capset_n8` | 8 | 496 | Default. Lower bound, upper bound open |
| `capset_n9` | 9 | 1082 | Lower bound, far from upper bound |
| `capset_n10` | 10 | 2474 | Lower bound. Verifier is slow at this size |

### sidon family (Sidon / B₂ sets in [1, N]: all pairwise sums distinct)

| Tag | N | Baseline | Notes |
|---|---|---|---|
| `sidon_100`  |   100 |  11 | Almost certainly exact — sanity check |
| `sidon_500`  |   500 |  23 | Singer-23 baseline; mild headroom |
| `sidon_1000` |  1000 |  32 | Singer-31 gives 32; 33 in [1,1000] would be a real result |
| `sidon_3000` |  3000 |  53 | Singer-53 baseline; real headroom |

The "sanity check" problems exist so you can confirm the loop terminates
without false positives — the agent should never produce a `keep` row on
small / exact-known sizes.

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
├── running_best.py       # state probe (current best, baseline, trials)
├── problems/             # frozen problem specs, one JSON per (family, n)
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
