# auto-erdos — Track 3 (resolve an external open problem)

Mission: move a currently-open problem on erdosproblems.com into a resolved
status by either **(a)** locating a previously published resolution the
database hasn't captured, or **(b)** onboarding the problem into this repo's
Track 2 harness and executing the finite computation for a problem that is
witness-decidable.

This is the outward-facing sibling of `program.md` (Track 1: beat a bound)
and `proof_program.md` (Track 2: prove/disprove a claim). Track 3 differs in
one way: the target problem starts *outside* the repo, so the session has an
**onboarding phase** where files that are read-only during a loop
(`proofs/*.json`, `library/*_witness.py`, tests) are legitimately created.
Once the loop starts, the standard read-only rules snap back on.

Read `proof_program.md` end-to-end before any loop rounds — the round
cycle, keep rule, exit codes, and stop conditions there govern path (b).

## Sources

- https://www.erdosproblems.com — canonical, per-problem pages + threads
- https://github.com/teorth/erdosproblems — community DB; one markdown file
  per problem with statement, references, tags, status
- https://teorth.github.io/erdosproblems/ — filterable table (fastest way
  to apply the filters below)
- Per-problem discussion: https://www.erdosproblems.com/forum/thread/<n>

Use WebSearch/WebFetch for all of the above; none of this is cached locally.

## Phase 0 — session setup

1. Work in a dedicated worktree on a fresh branch off master:
   `erdos-resolve/<MMDD-HHMMSS>` under `worktrees/<tag>/` (same collision
   discipline as Tracks 1 and 2).
2. Already-onboarded problems are OUT OF SCOPE as targets (they belong to
   Track 2): `erdos_mollin_walsh`, `erdos_gyarfas`, `frankl_union_closed`,
   `erdos_szemeredi_sum_product`, and the proved benchmarks
   `primitive_set_erdos`, `erdos_primitive_set_basic`. Read their specs
   anyway — `proofs/erdos_gyarfas.json` and `proofs/frankl_union_closed.json`
   are the onboarding templates.
3. `prepare.py`, `proof_prepare.py`, `log_result.py`, `proof_log_result.py`,
   and `prompts/` remain READ-ONLY in all phases. Onboarding adds new files;
   it never edits the harness.

## Target selection

1. Filter to Status = Open in the table/DB. Deprioritize problems with a
   prize > $100, entries on Bloom's "Top 10" list, and anything with >10
   references — those are the well-attacked ones.
2. Prefer problems that:
   - Are a single specific question with concrete parameters, not a program
   - Have few references and no active discussion thread
   - Cite sources that haven't been reviewed since original publication
   - Sit in a mature subfield where the solution space is well-mapped
     (analytic number theory, additive combinatorics, extremal
     combinatorics on small structures)
3. **Path (b) hard gate** (repo constraint, checked before shortlisting a
   computation target): the problem must reduce to a finite check that a
   *stdlib-only, deterministic, conservative* verifier can decide — one
   finite object settles the claim, the check runs in seconds-to-minutes
   per candidate, and total search cost is under ~24 CPU-hours. The two
   in-repo shapes to pattern-match: a graph property checked exhaustively
   with a node-expansion budget where budget exhaustion is a REJECTION
   (`library/erdos_gyarfas_witness.py`), or a set-family property checked
   fully polynomially (`library/union_closed_witness.py`). If the check
   needs floating point, it must be made rigorous the way
   `library/primitive_set_witness.py` does (stdlib `decimal`, ULP-bumped
   logs, documented slack). No new dependencies — `pyproject.toml` is fixed.
4. Produce a shortlist of 5 candidates with one-paragraph tractability
   notes. Commit it as `briefs/resolve_shortlist_<MMDD>.md` BEFORE
   committing to a target, and state in the file which path (a or b) each
   candidate gets and why.
5. If the chosen problem turns out to be one of Erdős's deep favorites,
   stop and report — don't burn the session on it.

## Path (a) — literature search

1. Extract the verbatim statement, every cited reference, and any weaker
   or stronger variants named in the entry.
2. Search MathSciNet, zbMATH, Google Scholar, arXiv, Semantic Scholar for
   the statement's key quantities, Erdős's coauthors on the cited
   references, and papers citing those references.
3. Follow forward citations two hops. Open papers with vague titles like
   "On a problem of P. Erdős" — those are frequently the resolutions.
4. Check Erdős's collected problem papers and the problem sections of
   Combinatorica and other journals he ran problem columns in.
5. Record every finding — including negative ones — in the **given_facts
   discipline** from `proofs/*.json`: each result gets `id`, `statement`,
   `sign_disambiguation` (what it does and does NOT imply — this repo's
   defense against the scope/sign errors that killed prior sessions), a
   precise `citation` (DOI or arXiv id), and `warns`. Build this ledger in
   the working brief as you go; it becomes the writeup's evidence section.
6. When a candidate paper is found: extract its theorem statement verbatim,
   translate into the notation of the erdosproblems entry, and write out
   the equivalence **in both directions**. Do not accept "essentially the
   same" — if the reduction can't be written, it isn't a match.
7. The in-repo template for a correct path-(a) outcome is the 2026-07-11
   audit that reclassified `primitive_set_erdos` (Erdős #1196 → proved,
   arXiv:2605.00301): verbatim statement match, `literature_resolution`
   recorded in the spec, status flipped, benchmarks re-purposed. Match
   that standard of specificity.

## Path (b) — finite computation

Only for a problem that passed the hard gate in Target selection.

### Onboarding (ordinary commits on the resolve branch, BEFORE the loop)

1. Reproduce the finite reduction from the entry or original paper, in
   writing, in the brief. If the reduction is the entry's claim rather
   than something you verified, say so and cite where it's proved.
2. Write `proofs/<tag>.json` following the `erdos_gyarfas.json` schema:
   `claim_status: "open"`, `claim_latex` verbatim from the entry (with the
   erdosproblems number), `given_facts` with `sign_disambiguation` per
   fact, a witness contract (`witness_type`, `witness_schema` with
   explicit size caps, `witness_verifier_module`), `round_cap`,
   `time_budget_s`, `status_audited` with today's date and what was
   checked, and a `note` naming the sanity anchors (known objects the
   verifier must REJECT) and the plausible witness search space.
3. Write `library/<tag>_witness.py` — deterministic, stdlib-only,
   conservative (any budget exhaustion or ambiguity is a rejection).
4. **Cross-validate before trusting anything**: add tests to
   `tests/test_new_witnesses.py` in the existing style — schema rejection,
   hypothesis-class rejection, sanity anchors (e.g. K₄ / Petersen for
   erdos_gyarfas), and the conservative-budget path. Additionally
   implement the core predicate a SECOND time, independently (different
   algorithm, in the test file), and assert agreement on a seeded
   randomized corpus. Since the claim is open, no test may contain a
   `witness_valid == 1` example — pin down the rejection surface instead.
5. Estimate total compute for the search. Over ~24 CPU-hours → downgrade
   the target to path (a) or back to the shortlist; note why in the brief.

### The loop

Run the standard Track 2 machinery — the onboarded problem is now just
another `PROOF_TAG`:

```bash
uv run proof_session_start.py                 # ALWAYS first
# empty queue on a fresh problem → run /erdos-proof-ideation before rounds
# then the proof_program.md round cycle, dual attack policy included:
# CHECK blocks before proof effort, witness candidates fed to the verifier
```

Search guidance: Track 1-style generate-and-screen fits witness hunting
(the specs' `note` fields sketch this — girth-biased lifts / voltage
graphs for graph targets, evolved generator closures for family targets).
The loop's only success exits are the gatekeeper's:

- **exit 7** (witness verified) → STOP. A human must independently re-run
  the witness verifier — and the second implementation from step 4 —
  before anything is claimed publicly. This is stop condition 3 of
  `proof_program.md` and is not negotiable.
- **exit 6** (converged partial result) → the problem stays open; report
  as partial progress, never as a resolution.

**NEVER STOP mid-loop** once rounds have begun — no "should I keep
going?" prompts. Run until the gatekeeper exits 4, 6, or 7, or a human
interrupts. Feed every dead end to `uv run proof_notes.py "<insight>"`.

## Deliverable

One markdown writeup ready to post on the problem's discussion thread,
committed as `briefs/<tag>_resolution_<MMDD>.md`:

- Problem number and verbatim statement
- What was found: author, year, venue, precise citation (path a) — or the
  witness object verbatim plus both independent verifier outputs and the
  exact `uv run` reproduction commands (path b)
- The equivalence argument between the cited result and the problem's
  statement, written in both directions
- Recommended status change (Proved / Disproved / Solved) with reasoning
- Any statement ambiguity encountered and how it was resolved

If the target was onboarded and resolved, also update its
`proofs/<tag>.json` the way `primitive_set_erdos` was handled: flip
`claim_status`, add `literature_resolution` (path a) or the witness record
reference (path b), refresh `status_audited`.

## Rules

- No claim of resolution without either a verifiable citation with a
  written two-way equivalence, or a reproducible computation that passed
  BOTH independent implementations and a human re-run.
- If the statement is ambiguous, surface the ambiguity in the brief and
  the writeup — do not silently pick an interpretation (see erdosproblems
  #728 for why this matters). If path (b) depends on the interpretation,
  the ambiguity blocks onboarding until resolved on the forum thread or
  from the primary source.
- Close-but-not-quite literature matches are partial progress, not
  solutions. Record them in the given_facts ledger with an honest
  `sign_disambiguation` and move on.
- Posting to the forum thread is a human action. The deliverable ends at
  the committed markdown file; never attempt to post, and never contact
  authors.
- The harness is fixed: no edits to `prepare.py`, `proof_prepare.py`, the
  gatekeepers, `prompts/`, or existing `proofs/*.json` specs other than
  the sanctioned status flip above. No new dependencies.
- On a `claim_status: proved` spec, `witness_valid == 1` is a verifier
  bug, never a result — the same logic applies to any Track 3 target
  found during path (a) to be already resolved: from that moment it is a
  rediscovery benchmark, not a discovery.
