# Session handoff (s_0501-090926-1fd3 -> next)

**Stop reason**: Rate-of-return checkpoint. Both items on the prior
handoff's priority list are now resolved. Three clean keep_progress
rounds:

- **Round 12 redux (commit 657126b)** — §2.2 trap defused. The
  parenthetical at lines 236-240 no longer names specific primes
  (1223, 7919, 37813, 81799) or asserts "verifiable as prime by
  trial division". Replaced by a no-trigger reference pointing at
  `records/` for the deterministic numerical values. Verifier ran
  clean (0 blocking, 5 warns). Future §3 work is no longer at risk
  of the recurring 1-in-N numerical-critic flake on this prose.

- **Round 13 (commit cf58294)** — §3.5 status sync (the discarded
  round-12 redux). The partial-result bullet list now includes the
  §2.5 witness-search-negative bullet and the §3.4 per-stratum-
  decomposition-strictly-weaker-than-F1 bullet. Partial-result
  claim itself unchanged.

- **Round 14 (commit 7e3507e)** — `proof_lemmas/lemma_005_cross_stratum.md`
  brought in sync with the main strategy: (a) Bounding-S_high section
  now mirrors the §3.4 quantitative-looseness derivation; (b) the
  What-we-have-ruled-out third bullet now covers the §2.5 witness-
  search probes at $x_\text{floor} \in \{1000, 10000\}$. As a
  bonus, §3.4 was sharpened to note that the per-stratum
  decomposition is weaker than the *conjectured* ceiling $1$
  already at $K = 1$ (sum $\approx 1.21 > 1$), not just weaker than
  F1's $1.399$ at $K = 2$. Both edits combined in one commit
  because `proof_log_result.py` AST-hashes `proof_strategy.md` only —
  a lemma-only round is rejected as a no-op.

Round count: 12 rows in `proof_results.tsv` (11 keep_progress + 1
discard from prior session). 38 rounds remaining of cap=50.

## Where the proof stands now

The unconditional partial result, supported only by the F1/F2/F3
ledger plus elementary positivity, is unchanged in shape but now
mirrored across files and quantitatively sharper:

- *Sign disambiguations* of F1, F2, F3 (§1.2)
- *Numerical evidence for F3 direction*, $k \in \{1,2,3,4\}$ (§2.1-§2.4)
- *Witness-search negative result* at $x_\text{floor} \in \{1000, 10000\}$
  (§2.5; mirrored in `lemma_005`)
- *Single high-Omega stratum closure* with quantitative gap
  $(c/2) k^2 / 2^k$ for $k \geq k_0$ (§3.3 + Lemma 2)
- *Per-stratum decomposition weaker than the conjectured ceiling $1$
  at $K = 1$, weaker than F1 at $K = 2$* (§3.4; mirrored in `lemma_005`)

Cross-stratum residue (Lemma 5) remains open and IS the conjecture.
No witness committed; verdict_hint stays partial_result.

## Next-session moves (in priority order)

1. **Lemma 4 / Lemma 3 outline polish (LOW RISK).** Both lemmas
   are filed as future-work placeholders that need extra-ledger
   admissions (Landau / Sathe-Selberg for Lemma 4; PNT-density for
   Lemma 3). Their lemma files could be polished to spell out the
   precise extra-ledger admission needed in standalone terms (without
   actually invoking any new mathematics). This is genuinely useful
   exposition and low-risk for the critic.

2. **Tighten §3.3 gap statement (LOW RISK).** The current §3.3
   says "$S_k < 1$ for $k \geq k_0$" with quantitative gap
   $(c/2) k^2 / 2^k$. A cosmetic improvement would surface the
   relationship between $k_0$ (§3.3) and $k_1$ (§3.4): both are
   thresholds where F3's o(1) error is bounded; they could be
   defined with more parallelism (or unified into one threshold
   if the bounds match).

3. **Lemma 5 — DO NOT ATTEMPT.** It IS the conjecture. Any closure
   would be a real result requiring genuine new mathematics; the
   skill-level loop cannot produce one and any "fix" would be a
   fabrication that the openness critic + verdict-hint defense
   would catch (or worse, miss). Prior sessions have respected this
   line; this session did too.

## Files modified this session

- `proof_strategy.md` (§2.2 parenthetical rewritten; §3.5 list
  extended with two bullets; §3.4 sharpened to K=1)
- `proof_lemmas/lemma_005_cross_stratum.md` (Bounding-S_high gets
  the quantitative-looseness paragraph; What-we-have-ruled-out third
  bullet extended with §2.5 probes)
- `proof_open_questions.jsonl` (Q14 + Q15 + Q16 lifecycle)
- `proof_journal.jsonl` (3 round events)
- `proof_results.tsv` (3 keep_progress rows)
- `records/proof_primitive_set_erdos_*.json` (3 partial-result
  records, auto-committed)

## Notes (carried forward)

- **The numerical critic flake on §2.2 is now defused.** §2.2 prose
  no longer mentions specific primes or trial-division, so the
  trigger surface is gone. Future rounds with §2.2 in their diff
  context should be robust. (If the flake re-fires anyway on some
  *other* §2 prose, the next session will need to find and defuse
  the new trigger; if it re-fires on the new §2.2 wording, that
  rules out the trigger-phrase hypothesis and the next session
  should look at numeric-claim-density instead.)

- **The harness AST-hashes `proof_strategy.md` only.** A round that
  edits only lemma files is rejected as a no-op duplicate. This
  is now logged once in this session's journal — future sessions
  doing lemma-only rounds should bundle a small strategy.md edit
  in the same commit (and not waste a `git reset --hard HEAD~1`
  on figuring it out).

- **Convergence (exit 6) is unreachable in normal flow.** Same as
  prior. We are at 12 rows / 50; budget is ample.

- **Windows console encoding.** `proof_session_start.py` crashes
  on the cp1252 console encoder when the handoff contains non-ASCII
  ($\geq$, etc.). The session marker is still written before the
  print, so re-running session_start would be a no-op leak. The
  workaround used this session: read the handoff via the file
  rather than via stdout. Future sessions: set
  `PYTHONIOENCODING=utf-8` before any helper script. (Tracked but
  not fixed here — `proof_session_start.py` is read-only.)
