# auto-erdos — agent program

Autonomous research loop on Erdős-style combinatorial problems. Port of the
`karpathy-quant-auto-research` harness with the statistics layer removed:
the verifier is deterministic, so there is no IS/OOS split, no bootstrap CI,
no Sharpe deflation. The score is the score.

## Setup

To set up a new experiment, work with the user to:

1. **Pick a problem**: choose a `PROBLEM_TAG` from `problems/*.json`. Default is
   `capset_n8` (cap sets in F_3^8, baseline 512).
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
- Read `verifier_results.tsv` or the AST trial cache directly — those are
  harness-side audit trails. The sanctioned cross-branch channels are:
  - `prepare.load_best_so_far()` — best valid candidate (warm-start);
  - `prepare.load_elites()` — top-8 distinct valid candidates (recombination);
  - `prepare.load_hypothesis_log()` — cross-branch trial log (see
    "Cross-branch hypothesis memory" below);
  - `prepare.load_problem_notes()` / `prepare.append_problem_notes()` — the
    agent-written knowledge channel (see "Problem notes" below);
  - `uv run problem_brief.py` and `uv run analyze.py` — free read-only
    digests of all of the above (no trial cost).
  You may also read `run.log` (your own stdout) and `results.tsv` (your own log).

**The goal**: improve the score above the running best. For Port 1 (cap
sets), score = |S|, larger is better. The keep rule:

    is_valid == 1 AND score > running_best

`running_best` is the max of (a) the problem's literature baseline,
(b) kept scores on this branch, and (c) the **cross-branch global best**
valid score from the hypothesis log. A keep is a genuinely new record for
the *problem*, not just for your branch — a sister branch's 59 means your
58 discards. (`AUTOERDOS_GLOBAL_RATCHET=0` restores branch-local ratcheting
for debugging only.) There are no constraint columns to satisfy beyond
validity itself — the verifier rejects malformed candidates outright.

**Problem status and headroom.** Every `problems/<tag>.json` carries
`upper_bound` (best known UB, with its provenance in `note`) and `status`:
`open` (real headroom), `sanity` (optimum known, trial_cap=1 null-control),
or `closed` (optimum known AND already reached — `log_result.py` refuses to
grade, exit 7). Check `uv run running_best.py --headroom` before investing:
the gap between global best and `upper_bound` is where the research is.

**Overfitting discipline.** The 20-trial cap is here to keep you honest.
Twenty hypotheses each defended with a one-line thesis is worth more than
two-hundred mutations of the same greedy. If your idea is "tweak a constant
and see what happens," skip it. The AST-dedup will reject pure no-ops, but
it cannot tell the difference between an honest experiment and 19 vacuous
restarts of the same algorithm — that judgment is on you.

**The first (seed) run.** Run `strategy.py` as-is. The shipped seed already
combines three layers and returns the largest:

  1. **Warm-start** — `prepare.load_best_so_far()` for this problem (highest
     valid score across all branches; None on a fresh machine).
  2. **Library** — `library.capset.best_seed(n)` (uses the shipped 20-cap
     building block) for capset; `library.sidon.singer_for_n(N)` (Singer
     perfect difference set) for Sidon.
  3. **Randomized greedy** — fallback, deterministic.

So the seed is at-or-above the literature LB on every Sidon problem out of
the box (e.g. sidon_1000: 33+ vs LB 32) and AT the literature LB for every
capset problem: n in {1,2,3,4} exactly, and n in {7,8,9,10} via the shipped
literature-record caps (`library.capset_records` — Edel's caps plus
FunSearch's 512-cap at n=8). Only n=5/6 sit below LB without the optional
cap_n6_size112 disk cache. Your job is to push ABOVE the seed — every trial
is an attempt at a genuinely new record, not a re-derivation of known ones.

**CRITICAL — the seed run is non-committing.** `strategy.py` already exists
at HEAD; you do NOT make a git commit before running the seed. After
`log_result.py` grades the seed (`discard` if score == LB; `keep` if
warm-start has lifted you above LB), **DO NOT `git reset --hard HEAD~1`**
— there is no agent-made commit to reset, and resetting would move HEAD
off the current scaffold/fix commit onto its parent, silently downgrading
the verifier and other harness code under your feet. Just proceed straight
to the experiment loop with HEAD untouched. The `git reset` rule in the
loop applies only to commits *you* made (steps 2–3 below).

**CRITICAL — your first commit must make a real change to `strategy.py`.**
The AST dedup hash strips docstrings, comments, and whitespace before
hashing, so a "first commit" that only edits comments or docstrings will
hash identically to the seed and trigger exit code 3 against either the
seed row (any prior branch's seed has the same hash and a different commit
than yours) or against an earlier branch's identical first commit. Adding
imports or new top-level functions DOES change the AST. The point is: have
a real hypothesis, not a no-op.

## Output format

`prepare.print_summary` emits exactly:

    ---
    problem:           capset_n8
    family:            capset
    score:             137.000000
    is_valid:          1
    verifier_seconds:  0.0234
    baseline:          512
    status_hint:       no_improvement
    reason:            valid cap set of size 137 in F_3^8
    search_seconds:    412.3
    budget_seconds:    1500
    budget_used_pct:   27.5
    frontier:          locally maximal — no single-point extension exists

The trailing lines are informational: `search_seconds` / `budget_used_pct`
show how much of the wall-clock search room the strategy actually used
(single-digit percentages on a search-based thesis mean you left budget on
the table — anytime loops should check `tb.expired`, not finish instantly),
and `frontier` reports +1-extendability of a valid candidate (computed by
the harness at verifier cost; `AUTOERDOS_FRONTIER=0` disables). Extract the
headline metrics from the log file:

    grep "^score:\|^is_valid:\|^verifier_seconds:\|^status_hint:\|^frontier:\|^budget_used_pct:" run.log

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
| 6 | hypothesis family exhausted — the thesis `[axis]` tag already has ≥ `AUTOERDOS_FAMILY_CAP` (default 5) failures and zero keeps across all branches of this problem | `git reset --hard HEAD~1`. Move to a **different axis** — another variant of this one is knob-twisting by definition. Nothing was logged. |
| 7 | problem is closed (`status: "closed"` in the spec — optimum known and reached) | Stop; pick an open problem (`running_best.py --headroom`). Nothing was logged. `AUTOERDOS_ALLOW_CLOSED=1` only for deliberate re-verification. |

**The keep rule (computed by `log_result.py`, not you)** — a run is kept
only if:

- `is_valid == 1`, AND
- `score > running_best` (where `running_best` = max(literature baseline,
  any kept score so far in this branch's `results.tsv`, and the best valid
  score across ALL branches of this problem from the hypothesis log)).

The baseline is the problem's literature lower bound and is fixed for the
duration of the branch. The bar ratchets upward with each kept row AND with
sister branches' results, so a keep is always a new global record for the
problem — never a duplicate of something another branch already found.

**On every keep**, `log_result.py` writes `records/<tag>_<score>_<commit>.json`
(candidate, score, baseline, branch, thesis, verifier_seconds) and auto-commits
it as a follow-up commit. This is the permanent, committed proof of a result —
unlike `results.tsv` (gitignored). `git reset --hard HEAD~1` after a *later*
discard will land on this record-commit, leaving strategy.py at the kept
version; semantics for the agent are unchanged.

**Paper writeup is OFF by default in the loop.** `log_result.py` reads
`AUTOERDOS_WRITEUP`; unset / `0` / `off` skips paper generation entirely.
Set it to `1` (or `opus,codex`) only outside the wall-clock-sensitive
autoresearch loop — model calls cost minutes per keep. To generate
papers retroactively from any record, run
`uv run write_paper.py records/<file>` after the loop completes.
`prompts/paper_writeup.md` is the frozen template; do not edit it
mid-loop.

The TSV has 6 columns:

    commit  score  is_valid  verifier_seconds  status  description

Example:

    commit	score	is_valid	verifier_seconds	status	description
    a1b2c3d	137.000000	1	0.0234	discard	thesis: randomized greedy seed — well below baseline
    b2c3d4e	248.000000	1	0.1023	discard	thesis: greedy with restart — still well under 512 baseline
    c3d4e5f	0.000000	0	0.0019	discard	thesis: tried a Behrend-style construction — verifier flagged AP

## State probes

```
uv run running_best.py              # the bar a keep must clear (global ratchet)
uv run running_best.py --baseline   # the problem's literature baseline
uv run running_best.py --trials     # rows logged / trial cap, e.g. "7/20"
uv run running_best.py --headroom   # baseline / current best / upper bound / status
uv run problem_brief.py             # full session-start digest (free)
uv run analyze.py                   # structural diagnostics of best_so_far (free)
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
   - **6** — family exhausted. `git reset --hard HEAD~1`, switch to a
     different `[axis]` — the gate only fires when the axis has ≥5
     cross-branch failures and zero keeps.
   - **7** — problem closed. Stop; pick an open problem.

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
- **MaxSAT / partial-MaxSAT encoding**: variables x_p for each p in F_3^n,
  hard clauses "for every 3-AP (a,b,c), at most 2 of x_a, x_b, x_c," soft
  unit clauses x_p with weight 1. Solve with `pysat.examples.RC2` for an
  exact answer at small n, or use it as a swap-oracle inside SA at larger
  n. `pysat.solvers.Glucose3` for plain SAT feasibility on threshold k.

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
`prepare.TimeBudget` is per-problem (`time_budget_s` in `problems/<tag>.json`,
default 900s; env `AUTOERDOS_TIME_BUDGET_S` overrides). Per-problem budgets
range from 60s (sanity checks) to 2400s (capset_n10 where the verifier
itself is non-trivial). Sidon at N=1000 / 3000 is set to 1200s / 1800s for
exploitative search.

That budget is yours to spend on DFS, SA, GA, SAT, exact sub-routines, etc.
inside `generate_candidate`. The shipped seed plumbs the `TimeBudget` into
the function signature: `generate_candidate(tb=None)`. Use `tb.expired`
to bail gracefully and return whatever valid candidate you have so far;
hard-killed runs are treated as crashes.

## Session-start brief + literature pass (do this BEFORE trial 1)

Two steps, both free (no trial cost):

1. **Brief**: `uv run problem_brief.py` — headroom (baseline / global best /
   upper bound), per-axis outcome counts across all prior branches (exhausted
   families are flagged), every kept thesis, the notes channel, and prior run
   summaries. A fresh session is a CONTINUATION of a research program; this
   is how it inherits the program's state.
2. **Literature pass**: every past record in this repo came from *knowledge*
   (OGR-26 marks, Singer multiplier orbits, cubic constructions in GF(q³)) —
   not from generic search. Before the first hypothesis, dump what you know
   about this problem from the literature: best known constructions, where
   the known LB comes from, what structures set records at nearby sizes,
   whether the record is theory-hard or search-soft. Write it to the notes
   channel (`prepare.append_problem_notes(...)` or via a tiny throwaway
   script) so every future session inherits it. If the notes already contain
   a literature section, read it instead of re-deriving.

## Analysis-only moves (free — no trial budget)

Not every step must produce a candidate. `uv run analyze.py` dissects the
current best_so_far (gap/fiber profiles, sum density, exact +1-extension
points, near-miss points blocked by a single collision). Use it whenever
you're stuck: knowing that the best set is locally maximal with zero
1-collision points *rules out* every remove-1-add-2 hypothesis at zero
cost. Paste durable findings into the notes channel.

## Problem notes — the knowledge channel

`prepare.load_problem_notes()` / `prepare.append_problem_notes(text)` read
and append to `~/.cache/auto-erdos/notes_<TAG>.md` — free-form markdown
shared across all branches and sessions. Use it for literature findings,
structural analyses, and "what the next session should try". This is the
only sanctioned agent-*written* cross-branch channel; everything else
(hypothesis log, best_so_far, elites) is harness-written.

## Warm-starting from prior trials

`prepare.load_best_so_far()` returns the best valid candidate seen across
all branches of the current `PROBLEM_TAG` (or `None` if nothing valid has
ever been logged). The cache is written automatically by `print_summary`
whenever a run's score beats the prior best — agents do not write it.

```python
from prepare import TimeBudget, load_best_so_far, print_summary, verify

def generate_candidate(tb=None):
    spec = load_spec()
    prior = load_best_so_far()
    if prior is not None:
        seed = prior["candidate"]   # list[int] for sidon, list[list[int]] for capset
        # ... extend / swap-move from seed; check tb.expired for budget ...
    return seed

if __name__ == "__main__":
    with TimeBudget() as tb:
        candidate = generate_candidate(tb)
        result = verify(candidate)
    print_summary(candidate, result)
```

The shipped `strategy.py` already calls `load_best_so_far()` in its seed
path and returns the largest of (warm-start, library construction,
randomized greedy). Reading the cache directly is just one of several
ways to leverage it.

## Elite archive — recombination beats re-mutation

`prepare.load_elites()` returns up to 8 *distinct* valid candidates for the
problem, best first (`[{score, commit, written_at, candidate, ...}]`).
best_so_far keeps only the single best; the elites keep structurally
different near-records. The hypothesis class this unlocks is recombination:
cross two different Sidon bases (splice prefixes/suffixes, check cross-sums),
product-lift two different caps, or seed SA from elite #3 instead of
re-mutating elite #1's basin for the tenth time. The archive is written by
the verifier path automatically; agents only read it.

## Cross-branch hypothesis memory

`prepare.load_hypothesis_log(tag=None, *, since_utc=None)` returns every
prior trial on the current `PROBLEM_TAG` across all branches as a list of
dicts:

    {written_at, branch_tag, commit, score, is_valid, status, thesis}

```python
from prepare import load_hypothesis_log

prior_trials = load_hypothesis_log()
sa_attempts = [t for t in prior_trials if "annealing" in t["thesis"].lower()]
if sa_attempts and all(t["status"] == "discard" for t in sa_attempts):
    # Skip another SA variant — the family has already failed.
    pass
```

The thesis strings are stored verbatim — there is no automatic family
classification, so consumers grep / regex / LLM-summarize as needed.
`since_utc` (ISO 8601) optionally filters to recent trials. The log is
append-only; to retire history, `rm` `~/.cache/auto-erdos/hypothesis_log_<TAG>.tsv`.

This is the one sanctioned channel for cross-branch *failure* memory
(successes leak via `load_best_so_far`). It's deliberately separate from
the AST trial cache (which remains harness-internal and forbidden).

## Constructions library

`library/` ships literature-grade baselines that the agent can import as
starting points. Calling a library function is normal Python — no special
"used the library" gate; the keep rule still requires
`score > running_best`, so returning a library set verbatim discards
(it equals the running best by construction). The win is composition:
augment the library output with greedy / SA / swap-moves, etc.

```python
from library import sidon, capset, sat_extensions

# Sidon: try the best Singer translate, then SAT-extend by 1
seed = sidon.singer_for_n(spec["N"])
extended = sat_extensions.extend_sidon_by_one(seed, spec["N"])
seed = extended if extended is not None else seed

# Capset: start from the strongest shipped seed (uses 20-cap × ...)
seed = capset.best_seed(spec["n"])
# ... try to augment seed via swap-moves / SA / SAT ...
greedy = capset.random_greedy(spec["n"], seed=0)   # comparison baseline
```

Public API:

| Module | Function | Returns |
|---|---|---|
| `library.sidon` | `singer(q)` | q+1-element Singer set in [0, q²+q] (q prime). |
| `library.sidon` | `erdos_turan(p)` | p-element ET set in [0, 2p²-p] (p prime). |
| `library.sidon` | `singer_for_n(N, base=1)` | Best translated Singer set in [base, base+N-1]. |
| `library.capset` | `random_greedy(n, seed=0)` | Randomized greedy cap (deterministic). |
| `library.capset` | `cap_n1()` / `cap_n2_size4()` | Maximum caps in F_3^1 / F_3^2 (sizes 2 / 4). |
| `library.capset` | `cap_n3_size9()` | Maximum cap in F_3^3 (size 9, exact DFS). |
| `library.capset` | `cap_n4_size20()` | Maximum cap in F_3^4 (size 20, exact DFS, disk-cached). |
| `library.capset` | `product_lift(A, n_a, B, n_b)` | A × B as cap in F_3^{n_a+n_b}. |
| `library.capset` | `lift_to_dim(cap, src, tgt)` | Zero-pad embedding. |
| `library.capset` | `recursive_product(n)` | Cap in F_3^n via repeated cap_n1/cap_n2 product-lift. |
| `library.capset` | `best_seed(n)` | Strongest shipped cap: uses cap_n4_size20 × small-cap by product-lift. |
| `library.capset_records` | `record_cap(n)` | Shipped literature-record cap in F_3^n (n=7: 236, n=8: 512, n=9: 1082, n=10: 2432), or None. Provenance: `library/data/records/SOURCES.md`. |
| `library.capset_records` | `record_sizes()` | `{n: size}` of every shipped record. |
| `library.capset_lifts` | `cap_n6_size112()` | Edel's 112-cap in F_3^6 (literature LB), if disk cache present (else None). |
| `library.capset_lifts` | `best_seed_v2(n)` | Strongest available product-lift; uses cap_n6_size112 when cached. n=10: 2240 (vs 1600 from `capset.best_seed`). |
| `library.capset_lifts` | `best_decomposition_size(n)` | Size of the best product-lift the library can build for F_3^n. |
| `library.capset_sat` | `extend_capset_by_one(seed, n)` | +1 extension (linear scan). |
| `library.capset_sat` | `extend_capset_by_k(seed, n, k)` | +k extension (SAT, k>=2; hard guard 3^n>20000). |
| `library.capset_sat` | `swap_remove_k_add_kplus1(seed, n, k)` | Drop-k add-k+1 net +1 swap (SAT). |
| `library.capset_orbit_sweep` | `random_invertible(n, rng)` | Uniformly random invertible n×n F_3-matrix. |
| `library.capset_orbit_sweep` | `apply_linear(A, cap)` / `apply_translate(t, cap)` | GL(n,3) and affine actions; both preserve cap-freeness. |
| `library.capset_orbit_sweep` | `best_orbit_extension(seed, n, extender, ...)` | Sweep orbit reps × translates × extender; track largest valid. |
| `library.sat_extensions` | `extend_sidon_by_one(seed, N)` | +1 extension (linear scan). |
| `library.sat_extensions` | `extend_sidon_by_k(seed, N, k)` | +k extension (SAT, k>=2; raises if N>2000). |
| `library.sat_extensions` | `swap_remove1_add2(seed, N)` | Remove-1-add-2 net +1 swap (SAT). |

**Note on size**: for sidon_100 / 500 / 1000 / 3000, `singer_for_n` already
matches or beats the literature baseline (11 / 24 / 33 / 53 vs 10 / 23 / 32 / 53).
For capset, `capset_lifts.best_seed_v2(n)` now serves the shipped
literature-record caps directly (`library.capset_records.record_cap(n)`,
provenance in `library/data/records/SOURCES.md`): n=7: 236, n=8: 512
(FunSearch), n=9: 1082, n=10: 2432 — the LB exactly at each open n. For
n>=11 the DP composes them via product-lift (n=11: 4864, n=12: 12544 with
cap_n6_size112 cached). To push capset *above* LB you need a genuinely new
construction or a smart augmentation of the record cap (orbit-sweep +
extend_capset_by_one, swap_remove_k_add_kplus1 from `capset_sat`, or the
candidate routes in `library/data/records/CONSTRUCTIONS.md`). Note the
n=10 record cap is COMPLETE — no +1 extension exists, ever.

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
- **SAT feasibility for "+1 extension"**: take a Singer set S of size k,
  encode "exists x in [1, N] \ S with S ∪ {x} Sidon" as a SAT instance
  (variable per candidate x, clauses forbidding sum collisions). Solve
  with `pysat.solvers.Glucose3`. UNSAT ⇒ S is locally maximal; SAT ⇒ a
  +1 augmentation exists, repeat. **Use `library.sat_extensions.extend_sidon_by_one`**
  — it does the linear scan version (no SAT needed for +1) and returns
  None if locally maximal.
- **SAT for +k or swap moves**: `library.sat_extensions.extend_sidon_by_k(seed, N, k)`
  and `swap_remove1_add2(seed, N)` ship the SAT formulations with a CEGAR
  loop. They hard-guard at N>2000 for k>1 (encoding too large); for big N
  do bisection or use repeated +1 calls.
