---
name: erdos-proof-ideation
description: Use when a Track 2 proof session needs NEW attack directions before committing rounds — at the start of a proof attempt on a fresh open question, after a dead end is documented, or whenever the user asks to "brainstorm approaches", "fan out ideas on the proof", "run proof ideation", "/erdos-proof-ideation". Spawns N parallel proposer subagents with forced-distinct mathematical lenses against the same problem spec + dead-end ledger, then a judge pass ranks the proposals and the top 1-2 become open questions (qids) for the round loop. Complements erdos-proof-attempt (which drives rounds); this skill only generates and ranks directions — it edits nothing but proof_open_questions.jsonl and the notes channel.
---

# erdos-proof-ideation

Serial single-idea sessions are the weakest possible search over proof
space: one direction per session, dead end documented, hand off. This
skill front-loads the search — N independent proposers, each locked to a
different lens, judged before any round is spent.

## Inputs

- `PROOF_TAG` (default `primitive_set_erdos`) — must name a `proofs/<tag>.json`.
- Optional: N, the proposer count (default 5).

## Step 1 — Assemble the context pack

Read, in full:

1. `proofs/<PROOF_TAG>.json` — claim, claim_status, given_facts WITH their
   sign_disambiguations, witness contract. If `claim_status` is `proved`,
   the problem is a rediscovery benchmark — proposers must be told the
   goal is reconstructing the literature argument, not conquering an open
   problem.
2. `uv run proof_notes.py` — the cumulative cross-branch notes (killed
   approaches, minimal open lemma, literature findings).
3. Every `proof_lemmas/lemma_*.md` with `status: disproved` or
   `status: abandoned` — the dead-end ledger.
4. `proof_strategy.md` — current state of the draft.

Distill into a context pack (one markdown block): the claim, the facts
ledger verbatim, a bullet list of DEAD approaches with one-line reasons,
and the current minimal open lemma (if the notes state one).

## Step 2 — Fan out N proposers (parallel subagents)

Spawn N `general-purpose` subagents IN ONE MESSAGE (they must run
concurrently). Each gets the same context pack plus ONE lens it may not
abandon:

1. **sieve/density** — comparison of multiplicative or combinatorial
   densities; Mertens-type normalization; disjointness ⇒ densities sum ≤ 1.
2. **weight-redistribution / martingale** — reassign each object's weight
   along chains (divisor chains, subset chains); look for a sub-invariance
   inequality that makes total weight non-increasing. (This is the lens
   that resolved Erdős #1196 — von Mangoldt weights on divisibility
   chains.)
3. **entropy / information** — encode the structure's constraint as an
   entropy inequality (this is Gilmer's union-closed breakthrough lens).
4. **extremal / stability** — assume near-extremality, derive structure,
   contradict; what does the extremal object have to look like?
5. **counterexample-first** — assume the claim is FALSE; derive the
   strongest structural constraints a counterexample must satisfy; either
   the constraints become contradictory (a proof sketch) or they describe
   a search space (hand to Track 1 / the witness verifier).

(If N > 5, add: generating functions / Dirichlet series; probabilistic
deletion; local-global compactness.)

Each proposer must return, as raw data:

- `direction`: 3-6 sentence sketch of the attack.
- `first_lemma`: ONE formally stated lemma that is (a) strictly weaker
  than the full claim, (b) killable — a finite numeric probe or short
  argument could falsify it. Include a draft `<!-- CHECK -->` block
  (stdlib Python, assert-style) when the lemma is finitely probeable.
- `dead_end_delta`: one sentence on why this is NOT one of the documented
  dead approaches (or what is different this time).
- `predicted_obstacle`: where this attack most likely dies.

## Step 3 — Judge

Spawn ONE judge subagent with all N proposals plus the context pack. It
scores each 1-10 on: novelty vs. the dead-end ledger, killability of
first_lemma, consistency with the given-facts ledger (sign
disambiguations included), and plausible depth (does the obstacle look
like the REAL difficulty or a warm-up?). It returns a ranking with one
paragraph of justification per proposal.

## Step 4 — Commit the output (the only writes this skill makes)

1. Append the top 1-2 proposals as new qids to
   `proof_open_questions.jsonl` (status `open`, summary = direction +
   first_lemma, session_id = `ideation-<MMDD-HHMMSS>`).
2. Append a digest to the notes channel:
   `uv run proof_notes.py "IDEATION <date>: ranked N proposals — <one line each with scores>; queued Q<i>, Q<j>."`
   Losing proposals go in the digest too — a future ideation pass must
   not re-propose them from scratch.
3. Report the ranking to the user. Do NOT start editing
   `proof_strategy.md` — that is `erdos-proof-attempt`'s job.

## Ground rules

- This skill NEVER edits `proof_strategy.md`, lemma files, or any
  read-only harness file.
- Proposers are idea generators, not verifiers — nothing they claim is
  trusted until the round loop's critics + CHECK blocks screen it.
- If every proposal scores ≤ 4 on novelty (all collide with the dead-end
  ledger), report that honestly and suggest the expert-brief escalation
  (`uv run expert_brief.py`) instead of queueing junk qids.
