---
name: erdos-proof-ideation
description: Use when a Track 2 proof session needs NEW attack directions before committing rounds — at the start of a proof attempt on a fresh open question, after a dead end is documented, after a program closes, or whenever the user asks to "brainstorm approaches", "fan out ideas on the proof", "run proof ideation", "/erdos-proof-ideation". Spawns parallel proposer subagents with forced-distinct mathematical lenses (problem-native lens sets from proofs/<tag>.json, plus wildcard / analogy-miner / fresh-eyes / revivalist slots) against the problem spec + dead-end ledger, then a THREE-JUDGE panel with distinct value functions ranks the proposals; each judge's top pick becomes an open question (qid) for the round loop. Complements erdos-proof-attempt (which drives rounds); this skill only generates and ranks directions — it edits nothing but proof_open_questions.jsonl and the notes channel.
---

# erdos-proof-ideation

Serial single-idea sessions are the weakest possible search over proof
space: one direction per session, dead end documented, hand off. This
skill front-loads the search — independent proposers, each locked to a
different lens, judged by a panel before any round is spent.

Design intent (read this before customizing anything): the fan-out
exists to buy VARIANCE. Every mechanism below — problem-native lenses,
ablated context packs, wildcard slots, a disagreeing judge panel,
per-judge picks instead of consensus — is there because the failure
mode of an autonomous proof loop is not bad ideas, it is the SAME idea
re-proposed forever. Do not "simplify" this skill back to five fixed
lenses and one judge.

## Inputs

- `PROOF_TAG` — must name a `proofs/<tag>.json`. If not given, use the
  tag of the most recent `session_open` event in `proof_journal.jsonl`;
  if the journal is empty, ask the user. (Do NOT default to
  `primitive_set_erdos` — that spec is a rediscovery benchmark now.)
- Optional: `L`, the lens-proposer count (default: all lenses in the
  problem's lens set, capped at 6). The four special slots below are
  always added on top of `L`.

## Step 1 — Assemble the context packs (plural)

Read, in full:

1. `proofs/<PROOF_TAG>.json` — claim, claim_status, given_facts WITH
   their sign_disambiguations, witness contract, and the
   `ideation_lenses` array if present. If `claim_status` is `proved`,
   the problem is a rediscovery benchmark — proposers must be told the
   goal is reconstructing the literature argument, not conquering an
   open problem.
2. `uv run proof_notes.py` — the cumulative cross-branch notes (killed
   approaches, minimal open lemma, literature findings, prior IDEATION
   digests, CONJECTURE lines).
3. Every `proof_lemmas/lemma_*.md` with `status: disproved` or
   `status: abandoned` — the dead-end ledger.
4. `proof_strategy.md` — current state of the draft.
5. The queue history in `proof_open_questions.jsonl` — collect every
   qid whose latest status is `released` (these were let go, not
   refuted; they are revival candidates).

Build TWO context packs:

- **FULL pack** (one markdown block): the claim, the facts ledger
  verbatim, a bullet list of DEAD approaches with one-line reasons, the
  current minimal open lemma (if the notes state one), and one
  paragraph on what the current strategy's machinery already does.
- **BARE pack**: ONLY the claim and the facts ledger verbatim. No dead
  ends, no strategy summary, no notes. This pack exists to produce
  proposals free of anchoring on everything tried so far — collisions
  with known dead ends are handled at judge time, not prevented at
  proposal time.

Also build the **revival docket**: every `released` qid (id + last
summary) and every `status: abandoned` lemma (id + one-line reason),
each annotated with what has been LEARNED since it was shelved (scan
the notes digests and strategy sections newer than its shelving).
`disproved` lemma ids stay dead per the ledger rule — but a disproof
whose failure was contingent (a specific scale, a specific sub-case)
may be reborn under a NEW id with changed hypotheses; note those
explicitly in the docket.

## Step 2 — The lens set

Use the `ideation_lenses` array from `proofs/<PROOF_TAG>.json` when
present — those lenses are written for the problem's mathematical
family, and a problem-native lens set is the single highest-leverage
variance mechanism in this skill. (Precedent: the R55 covering/cotree
reframing on `erdos_gyarfas` — the most productive idea of that whole
attempt — is a cycle-space/matroid-duality idea, and the generic lens
list below contains nothing that would have proposed it.)

Fallback when the spec has no `ideation_lenses` (generic list):

1. **sieve/density** — comparison of multiplicative or combinatorial
   densities; Mertens-type normalization; disjointness ⇒ densities sum ≤ 1.
2. **weight-redistribution / martingale** — reassign each object's weight
   along chains; look for a sub-invariance inequality. (The lens that
   resolved Erdős #1196.)
3. **entropy / information** — encode the structure's constraint as an
   entropy inequality (Gilmer's union-closed breakthrough lens).
4. **extremal / stability** — assume near-extremality, derive structure,
   contradict.
5. **counterexample-first** — assume the claim is FALSE; derive the
   strongest structural constraints a counterexample must satisfy;
   either the constraints become contradictory (a proof sketch) or they
   describe a search space (hand to Track 1 / the witness verifier).

(If more lens proposers are requested than lenses exist, add:
generating functions / Dirichlet series; probabilistic deletion;
local-global compactness.)

## Step 3 — Fan out the proposers (parallel subagents)

Spawn ALL proposers IN ONE MESSAGE (they must run concurrently):

- **`L` lens proposers** — each gets the FULL pack plus ONE lens it may
  not abandon.
- **The analogy miner** — gets the FULL pack and NO lens. Its task:
  name a SOLVED theorem (any field) whose proof overcame an obstacle
  structurally similar to this problem's current minimal open lemma,
  summarize that proof's skeleton in 3-5 steps, and port the skeleton
  step-by-step onto this problem, stating exactly where the analogy is
  load-bearing and where it is decorative.
- **The wildcard** — gets the FULL pack and this instruction verbatim:
  "The safe directions are already covered by other proposers. Propose
  the attack you believe is UNDERPRICED — the one a careful committee
  would rank last but that wins big if it works. Do not hedge toward
  respectability."
- **The fresh-eyes proposer** — gets the BARE pack only. It does not
  know what has been tried and must not be told; it returns its best
  first attack on the problem as stated.
- **The revivalist** — gets the FULL pack plus the revival docket. It
  must either (a) pick the ONE shelved direction most worth reviving
  and state precisely what new knowledge changes its prospects, or
  (b) report "nothing worth reviving" with one line per docket entry
  on why not. An honest (b) is a valid, useful return.

Model diversity: when the harness supports per-subagent model or
reasoning-effort selection, do not run all proposers on identical
settings — spread them across at least two models (or effort tiers),
assigning the wildcard and fresh-eyes slots to the strongest setting
available. Homogeneous proposers reconverge on homogeneous proposals.

Each proposer must return, as raw data:

- `direction`: 3-6 sentence sketch of the attack.
- `first_lemma`: ONE formally stated lemma that is (a) strictly weaker
  than the full claim, (b) killable — a finite numeric probe or short
  argument could falsify it. Include a draft `<!-- CHECK -->` block
  (stdlib Python, assert-style) when the lemma is finitely probeable.
- `dead_end_delta`: one sentence on why this is NOT one of the
  documented dead approaches (or what is different this time).
  Fresh-eyes proposers SKIP this field (they cannot know); the
  orchestrator annotates collisions before judging.
- `predicted_obstacle`: where this attack most likely dies.
- `if_true_payoff`: one sentence — what changes about the problem if
  `first_lemma` holds.

## Step 4 — Judge panel (three judges, distinct value functions)

Spawn THREE judge subagents in one message, each with all proposals
plus the FULL pack (annotate fresh-eyes proposals with any dead-end
collisions first). Each judge ranks ALL proposals 1-10 under its OWN
value function and must NOT balance across criteria — disagreement
between judges is the point, not a defect:

- **Judge RIGOR** — scores killability of `first_lemma`, consistency
  with the given-facts ledger (sign disambiguations included), and
  plausible depth (does the predicted obstacle look like the REAL
  difficulty or a warm-up?). Ignores novelty.
- **Judge NOVELTY** — scores distance from the dead-end ledger AND from
  the current strategy's existing machinery. A proposal that re-skins
  the incumbent program's toolkit scores ≤ 3 no matter how sound.
  Ignores tractability.
- **Judge UPSIDE** — scores "most interesting if true": how much the
  proof landscape changes if `first_lemma` holds (`if_true_payoff`,
  stress-tested). Explicitly instructed to ignore feasibility and the
  probability the lemma is provable.

Each judge returns its ranking with one paragraph of justification per
proposal.

## Step 5 — Commit the output (the only writes this skill makes)

1. Take each judge's TOP pick (deduplicate — if two judges crown the
   same proposal, take the next distinct pick from the judge with the
   stronger justification). Queue 2-3 distinct winners as new qids in
   `proof_open_questions.jsonl` (status `open`, summary = direction +
   first_lemma, session_id = `ideation-<MMDD-HHMMSS>`), each with a
   `kind` field: `"exploit"` for Judge RIGOR's pick, `"explore"` for
   Judge NOVELTY's and Judge UPSIDE's picks (and for any winning
   wildcard/fresh-eyes/revivalist proposal regardless of which judge
   picked it). The `kind` field is what the exploration quota in
   `proof_program.md` schedules against. Do NOT collapse the panel to
   a consensus ranking — consensus selection is a variance killer and
   defeats the panel's purpose.
2. Append a digest to the notes channel:
   `uv run proof_notes.py "IDEATION <date>: <P> proposals (<lenses used>), 3-judge panel — <one line each with R/N/U scores>; queued Q<i> (kind), Q<j> (kind), ..."`
   Losing proposals go in the digest too — a future ideation pass must
   not re-propose them from scratch.
3. Report the ranking to the user, including where the judges
   DISAGREED most (the max-spread proposal) — that disagreement is
   signal about where the problem's difficulty is misunderstood.
   Do NOT start editing `proof_strategy.md` — that is
   `erdos-proof-attempt`'s job.

## Ground rules

- This skill NEVER edits `proof_strategy.md`, lemma files, or any
  read-only harness file (`proofs/*.json` included — lens sets are
  edited on harness branches by humans, not mid-ideation).
- Proposers are idea generators, not verifiers — nothing they claim is
  trusted until the round loop's critics + CHECK blocks screen it.
- The fresh-eyes proposer's ignorance is load-bearing: never leak the
  FULL pack into its prompt "for efficiency".
- If every proposal scores ≤ 4 with Judge NOVELTY (all collide with the
  dead-end ledger), report that honestly and suggest the expert-brief
  escalation (`uv run expert_brief.py`) instead of queueing junk qids.
- If the revivalist returns "nothing worth reviving", record that in
  the digest — it prices the docket for the next pass.
