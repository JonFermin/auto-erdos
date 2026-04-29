# auto-erdos — agent program

Autonomous research loop on Erdős-style combinatorial problems. Port of the
`karpathy-quant-auto-research` harness with the statistics layer removed:
the verifier is deterministic, so there is no IS/OOS split, no bootstrap CI,
no Sharpe deflation. The score is the score.

## Setup

To set up a new experiment, work with the user to:

1. **Pick a problem**: choose a `PROBLEM_TAG` from `problems/*.json`. Default is
   `capset_n8` (cap sets in F_3^8, baseline 496).
2. **Agree on a run tag**: propose a tag based on today's date (e.g. `apr28`).
   The branch `erdos-research/<tag>` must not already exist — this is a fresh run.
3. **Create the branch**: `git checkout -b erdos-research/<tag>` from current main.
4. **Read the in-scope files**:
   - `README.md` — repository context.
   - `prepare.py` — the verifier and driver. Do not modify.
   - `strategy.py` — the file you modify.
   - `problems/<PROBLEM_TAG>.json` — the frozen problem spec and baseline.
5. **Initialize results.tsv**: empty (just the header). The first row will be
   the seed run; the literature baseline lives in the problem JSON, not in the TSV.
6. **Confirm and go**.

## Experimentation

Each experiment runs `strategy.py`, which constructs a candidate, hands it
to `verify()`, and prints the metric block:

    uv run strategy.py > run.log 2>&1

**What you CAN do:**
- Modify `strategy.py` — only the body of `generate_candidate()` plus any
  helpers it calls. Imports from `prepare` are fixed.
- Import from `library/` — pre-shipped constructions. See "Constructions
  library" below.

**What you CANNOT do:**
- Modify `prepare.py`. It contains the verifier and is the ground truth.
- Modify any `problems/*.json`. The baseline is fixed for the duration of
  the branch.
- Modify `library/*.py`. The constructions are part of the fixed environment.
- Install new packages. Use only what's in `pyproject.toml`.
- Read `verifier_results.tsv` or the trial cache directly — those are
  harness-side audit trails. The only things you may read are `run.log`
  (your own stdout) and `results.tsv` (your own log).

**The goal**: improve the score above the running best. For Port 1 (cap
sets), score = |S|, larger is better. The keep rule:

    is_valid == 1 AND score > running_best

`running_best` starts at the problem's literature baseline and ratchets
upward with each kept row. There are no constraint columns to satisfy
beyond validity itself — the verifier rejects malformed candidates outright.

**Overfitting discipline.** The 20-trial cap is here to keep you honest.
Twenty hypotheses each defended with a one-line thesis is worth more than
two-hundred mutations of the same greedy. If your idea is "tweak a constant
and see what happens," skip it. The AST-dedup will reject pure no-ops, but
it cannot tell the difference between an honest experiment and 19 vacuous
restarts of the same algorithm — that judgment is on you.

**The first (seed) run.** Run `strategy.py` as-is. The seed (randomized greedy)
gives a baseline score that is honest but well below the literature LB —
your job is to close that gap.

**CRITICAL — the seed run is non-committing.** `strategy.py` already exists
at HEAD; you do NOT make a git commit before running the seed. After
`log_result.py` grades the seed (almost always `discard`, since the seed
is below the literature LB), **DO NOT `git reset --hard HEAD~1`** — there
is no agent-made commit to reset, and resetting would move HEAD off the
current scaffold/fix commit onto its parent, silently downgrading the
verifier and other harness code under your feet. Just proceed straight to
the experiment loop with HEAD untouched. The `git reset` rule in the loop
applies only to commits *you* made (steps 2–3 below).

## Output format

`prepare.print_summary` emits exactly:

    ---
    problem:           capset_n8
    family:            capset
    score:             137.000000
    is_valid:          1
    verifier_seconds:  0.0234
    baseline:          496
    status_hint:       no_improvement
    reason:            valid cap set of size 137 in F_3^8

Extract the headline metrics from the log file:

    grep "^score:\|^is_valid:\|^verifier_seconds:\|^status_hint:" run.log

If grep is empty, the run crashed; `tail -n 50 run.log` to read the trace.
`status_hint` is informational — `improvement_eligible` / `no_improvement`
/ `invalid` — but the actual keep/discard decision belongs to `log_result.py`.

## Logging results (the grader, not you, decides the status)

```
uv run log_result.py "thesis: short one-line rationale for what I just tried"
```

`log_result.py` reads `verifier_results.tsv` (the harness-owned audit
trail), computes the status, writes the row to `results.tsv`, and exits
with a code that tells you what to do next.

**Exit codes** — branch the loop on these:

| Code | Meaning | What to do |
|------|---------|------------|
| 0 | row logged; `status=keep` or `status=discard` on stdout | `keep` → advance the branch. `discard` → `git reset --hard HEAD~1`. |
| 2 | description invalid (no `thesis:` prefix, or contains tab/newline) | Fix the command and rerun — nothing was logged. |
| 3 | AST duplicate of a prior trial on this problem (any branch) | `git reset --hard HEAD~1` and pick a genuinely different hypothesis. Nothing was logged. |
| 4 | trial cap reached (default 20 per branch) | **Stop the loop.** Surface `results.tsv` for review. Do not raise the cap without a good reason. |
| 5 | crash row logged (no `verifier_results.tsv` row for this commit — `strategy.py` never reached `print_summary`) | `git reset --hard HEAD~1`. Inspect `run.log`. |

**The keep rule (computed by `log_result.py`, not you)** — a run is kept
only if:

- `is_valid == 1`, AND
- `score > running_best` (where `running_best` = max(literature baseline,
  any kept score so far in this branch's `results.tsv`)).

The baseline is the problem's literature lower bound and is fixed for the
duration of the branch. The bar ratchets upward with each kept row, so
later trials must keep beating the most recent kept score, not just the
starting line.

The TSV has 6 columns:

    commit  score  is_valid  verifier_seconds  status  description

Example:

    commit	score	is_valid	verifier_seconds	status	description
    a1b2c3d	137.000000	1	0.0234	discard	thesis: randomized greedy seed — well below baseline
    b2c3d4e	248.000000	1	0.1023	discard	thesis: greedy with restart — still well under 496 baseline
    c3d4e5f	0.000000	0	0.0019	discard	thesis: tried a Behrend-style construction — verifier flagged AP

## State probes

```
uv run running_best.py              # current best kept score (baseline if none kept)
uv run running_best.py --baseline   # the problem's literature baseline
uv run running_best.py --trials     # rows logged / trial cap, e.g. "7/20"
```

## The experiment loop

The loop starts AFTER the seed run; each iteration is one agent commit.
LOOP until `log_result.py` exits 4 (trial cap) or the human stops you:

1. Look at git state: current branch/commit.
2. Tune `strategy.py` with an experimental idea by directly hacking the code.
   Frame the thesis *before* you edit — if you can't articulate why this
   construction would produce a bigger valid set, skip it.
3. `git commit` — a real code change. Comment/whitespace/docstring-only
   commits are auto-rejected by the AST dedup.
4. Run: `uv run strategy.py > run.log 2>&1` (always redirect — do not tee
   or let output flood your context).
5. `grep "^score:\|^is_valid:\|^status_hint:" run.log`. If empty, the run
   crashed; `tail -n 50 run.log`.
6. `uv run log_result.py "thesis: <one-line rationale>"`.
7. Branch on the grader's exit code:
   - **0** — last stdout line is `status=keep` (advance) or `status=discard`
     (`git reset --hard HEAD~1`).
   - **3** — AST-duplicate. `git reset --hard HEAD~1`, pick a different idea.
   - **4** — trial cap. Write `summaries/<branch>.md`, push the branch, stop.
   - **5** — crash row. `git reset --hard HEAD~1`. Read `run.log` before next attempt.

**Mindset**: "nothing beat baseline" is a perfectly legitimate outcome on
hard problems with mature literature. The cap-set lower bounds for n>=7
are decades of mathematician work — your loop is a long shot, not a
guarantee. Twenty honest hypotheses is the bar; padding with knob-twists
is worse than stopping at trial 8 with a clean log.

**Crashes**: If a run crashes (typo, missing import, bug in candidate
generator), use judgment: fix-and-retry for obvious bugs; skip-and-discard
if the idea itself is fundamentally broken.

**Ideas when stuck** (framed as theses, not a grid — pick ones you can defend):

- **Greedy variants**: different orderings (sphere shells from origin,
  reverse lex, random restart with k attempts and keep best), different
  acceptance rules (lazy: only check a sample of pairs; eager: check all).
- **Algebraic constructions**: pick a well-known cap-free set in F_3^k for
  small k and lift it via product / direct sum to F_3^n. Example: cap set
  of size 4 in F_3^2 → product gives a cap set of size 4^(n/2) in F_3^n.
  Compare against the current best.
- **Local search**: start from a random valid set, try swap moves
  (remove p, try to add q1, q2 not previously fittable). Hill-climb on size.
- **Simulated annealing**: same swap moves but accept downhill moves with
  decaying probability; run a budget of moves and report the best valid
  set seen.
- **Coset partitioning**: partition F_3^n into cosets of a small subspace,
  pick at most one point per coset, lift constraints.
- **Structured restarts**: when greedy stalls, restart from a known
  "good" subset (e.g., last kept solution if you serialized it — note
  that's only allowed via files outside the repo or via the strategy
  generating the same construction deterministically).

Frame each idea with a one-line thesis *before* you run. If the thesis is
"I have no idea, just trying stuff," reconsider.

**NEVER STOP EARLY**: Once the experiment loop has begun, do NOT pause to
ask the human if you should continue. You are autonomous until ONE of
three things happens:

1. `log_result.py` exits 4 — the trial cap was reached. Summarize and stop.
2. The human interrupts you.
3. You genuinely cannot think of a defensible hypothesis that isn't a
   micro-variant of something already tried. Stop, write a one-paragraph
   summary, do NOT fabricate a 19th trial just to fill the cap.

**Timeout**: Verifiers themselves are cheap (well under a second for
capset n≤8 and sidon up to N~10000). The wall-clock cap inside
`prepare.TimeBudget` is **15 minutes** (`AUTOERDOS_TIME_BUDGET_S=900`) —
that budget is yours to spend on DFS, SA, GA, exact sub-routines, etc.
inside `generate_candidate`. Runs that exceed it should bail gracefully
(check `tb.expired`) and return whatever valid candidate you have so far;
hard-killed runs are treated as crashes.

## Constructions library

`library/` ships literature-grade baselines that the agent can import as
starting points. Calling a library function is normal Python — no special
"used the library" gate; the keep rule still requires
`score > running_best`, so returning a library set verbatim discards
(it equals the running best by construction). The win is composition:
augment the library output with greedy / SA / swap-moves, etc.

```python
from library import sidon, capset

# Sidon: try the best Singer translate, then extend
seed = sidon.singer_for_n(spec["N"])              # largest fit in [1, N]
# ... try to add points to seed ...

# Capset: start from product-lift, augment in time budget
seed = capset.recursive_product(spec["n"])         # 4^(n//2) * 2^(n%2)
# ... or pull random_greedy as comparison baseline ...
greedy = capset.random_greedy(spec["n"], seed=0)
```

Public API:

| Module | Function | Returns |
|---|---|---|
| `library.sidon` | `singer(q)` | q+1-element Singer set in [0, q²+q] (q prime). |
| `library.sidon` | `erdos_turan(p)` | p-element ET set in [0, 2p²-p] (p prime). |
| `library.sidon` | `singer_for_n(N, base=1)` | Best translated Singer set in [base, base+N-1]. |
| `library.capset` | `random_greedy(n, seed=0)` | Randomized greedy cap (current strategy.py default). |
| `library.capset` | `cap_n1()` / `cap_n2_size4()` | Maximum caps in F_3^1 and F_3^2. |
| `library.capset` | `product_lift(A, n_a, B, n_b)` | A × B as cap in F_3^{n_a+n_b}. |
| `library.capset` | `lift_to_dim(cap, src, tgt)` | Zero-pad embedding. |
| `library.capset` | `recursive_product(n)` | Cap in F_3^n via repeated product-lift. |

**Note on size**: for sidon_500 / 1000 / 3000, `singer_for_n` already
beats the literature baseline (24 / 33 / 58 vs 23 / 32 / 53). For capset
problems, `recursive_product` is below baseline at all n>=4 — it's a
building block, not a solution. To beat capset baselines you need
better constructions or a smart augmentation of the library output.

## Sidon-specific hypothesis ideas

Frame each idea with a one-line thesis *before* you run.

- **Translated Singer set**: for prime power q, the Singer construction
  gives a (q+1)-element Sidon set in [0, q²+q]. Translate or restrict to
  fit [1, N]. Establishes the known LB cleanly.
- **Erdős–Turán construction**: {2pa + (a² mod p) : 0 ≤ a < p} is Sidon
  in [1, 2p²-p+1] for prime p. Variant baseline.
- **Greedy + augmentation**: start from a known Singer/E–T set and try
  to greedily add additional points from [1, N] that don't break Sidon.
- **Local search (swap moves)**: start from a Singer-base of size k, try
  remove-1 / add-2 swaps. Hill-climb on size.
- **Simulated annealing**: same swap moves, decaying acceptance for
  downhill moves. Restart from best every K iters.
- **Difference-set parameterization**: a Sidon set of size k corresponds
  to a perfect difference family in the additive group. Search over
  small-modulus structures.
- **Concatenation / direct sum**: join two disjoint Sidon sets in
  [1, M] and [M+1, N] — but check the cross-sums don't collide.
- **Kotzig-array / Costas-style constructions**: more exotic algebraic
  bases that occasionally beat Singer for specific N.
