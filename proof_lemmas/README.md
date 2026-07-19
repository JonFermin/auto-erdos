# proof_lemmas/

One file per lemma the agent has tried (or plans to try). Decomposing the
proof into named lemmas is what makes 80-minute thinking sessions tractable:
the agent picks one lemma per round, focuses on closing it, then commits.

## File contract

Filename: `lemma_<id>.md` where `<id>` is a short slug, e.g.
`lemma_strat_omega_k_bound.md`. Numeric IDs are fine too (`lemma_001.md`).

Each file MUST start with YAML frontmatter:

```yaml
---
id: strat_omega_k_bound
status: open | proved | disproved | abandoned
depends_on: []                # list of other lemma ids; empty if self-contained
discharged_by_round: null     # int round number where status became proved/disproved/abandoned, else null
introduced_at_round: 3        # round when this lemma file was created
---
```

The body is markdown with embedded LaTeX. For a `proved` lemma the body
IS the proof. For an `open` lemma the body is the current state of attack:
what's been tried, what blocks progress, what the next move would be.

## Status semantics

- **open** — the lemma is conjectured but not yet proven. The body should
  end with a one-paragraph "current obstacle" so a future session can pick
  up. Anyone may attempt it next round.
- **proved** — body contains a complete proof. `discharged_by_round` is set.
  proof_strategy.md may cite this lemma by id.
- **disproved** — counterexample found in the body, or a proof that the
  lemma is false. `discharged_by_round` is set. proof_strategy.md should NOT
  cite this lemma; agent should rework the proof structure.
- **abandoned** — explicitly given up because the approach didn't pay off.
  Body explains why (so future agents don't re-derive the dead end).
  `discharged_by_round` is set.

## CHECK blocks — machine falsification tests (dual attack)

Any lemma file may embed one or more falsification tests:

```markdown
<!-- CHECK
# stdlib-only Python. Exit 0 = the lemma survives the tested instances.
# Raise (AssertionError is idiomatic) = the lemma is FALSIFIED.
import math
for k in range(1, 50):
    assert some_claimed_inequality(k), f"fails at k={k}"
CHECK -->
```

`proof_prepare.py` runs every CHECK block in every non-dead lemma
(status not in {disproved, abandoned}) in an isolated subprocess
(`python -I`, 15s timeout via `AUTOERDOS_LEMMA_CHECK_TIMEOUT_S`, 20k char
cap). A failing check is a deterministic **BLOCKING** finding — it fires
in both critics-on and critics-off modes. The intended discipline:

- **Write the CHECK before writing the proof.** Ten seconds of compute
  kills a false lemma that would otherwise cost a full session (the
  trading-decomposition dead end of 2026-07-11 is the canonical example
  of a session spent on something a numeric probe could have redirected).
- A check that passes is *evidence*, not proof — the lemma still needs
  its `status: proved` body.
- When a check fails, set `status: disproved` and keep both the body and
  the check — the falsifying instance is part of the audit trail.

## Citing lemmas in the main proof

In `proof_strategy.md`, cite by lemma id:

```markdown
By Lemma `strat_omega_k_bound`, the contribution of A_k to the sum is
strictly less than 1 - c k^2 / 2^k.
```

The critic_internal pass scans for `Lemma <id>` patterns and verifies the
referenced file is `status: proved`. If a cited lemma is `open`, that's a
WARN at minimum and BLOCKING if it's part of the central inequality chain.

## Append-only discipline

Do NOT delete lemma files. If a lemma turns out to be wrong, set its
`status: disproved` and keep the body — the disproof IS the body. Future
sessions read the file to learn the dead end. Deleting it loses that
context across the session boundary.
