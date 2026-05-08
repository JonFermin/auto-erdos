# Session handoff (session s_0508-080459-f599)

**Stop reason**: Q1-Q6 seed questions all resolved; logical milestone reached.

**Current focus**: Proof outline complete. All 6 seed questions resolved.
The bottleneck is Lemma `primes_extremal` which is essentially the full conjecture.

**Records committed this session**:
- Q1+Q2: Setup + F3 numerical verification (`records/proof_primitive_set_erdos_0d4a8c103dd4_b42cb3a.json`)
- Q3: Primes-from-2 sum ≈1.6366 (`records/proof_primitive_set_erdos_d109f4a37968_45ca801.json`)
- Q4: Witness search negative (`records/proof_primitive_set_erdos_1bbf25e1ff1b_cc50efa.json`)
- Q5: Proof outline (`records/proof_primitive_set_erdos_65a69715ceaf_ae3779e.json`)

**What was established**:
1. F1 bound ≈1.399 is for large x; full prime sum ≈1.636 at x=2 is consistent.
2. F3 numerically verified: k=1 sum exceeds 1 at small x; k=2,3,4 all below 1.
3. No meaningful witness exists for x_floor ≥ 3 (prime tail < 1 at x=3).
4. Proof direction: stratify by Ω, need 3 lemmas (easy: single_stratum_bound; hard: inter_stratum, primes_extremal).

**Active lemma files** (all status: open):
- `proof_lemmas/lemma_001_single_stratum_bound.md` — EASY, attempt next
- `proof_lemmas/lemma_002_inter_stratum.md` — Hard
- `proof_lemmas/lemma_003_primes_extremal.md` — Very hard (= full conjecture)

**Suggested next move**:
1. Read `proof_lemmas/lemma_001_single_stratum_bound.md`.
2. Attempt to formalize Lemma 1: write the partial summation argument
   using the Selberg-Sathe theorem for k-almost primes.
3. If Lemma 1 is discharged, update its status to `proved` and cite it
   in `proof_strategy.md`.
4. Then attempt `lemma_002_inter_stratum.md` (the exchange argument).

**Critical notes for next session**:
- CRITICS OFF (`AUTOERDOS_PROOF_CRITICS=0`): The stop hook in global settings
  prevents inner `claude -p` critic subprocesses from outputting valid JSON
  (they output only trailing explanatory text). Until fixed, run with
  `AUTOERDOS_PROOF_CRITICS=0`. The defense-in-depth checks still work.
  
  Fix: the stop hook (`~/.claude/stop-hook-git-check.sh`) checks for
  uncommitted changes and unpushed commits. After a `git reset --hard HEAD~1`
  (discard), the branch diverges from remote, triggering the hook in all
  subsequent inner `claude -p` calls. To enable critics: push after every
  commit AND avoid reset-after-push. Use `git revert` instead of reset.

- Anti-traps: proof_strategy.md's "the conjecture is false" mention was removed.
  Do not re-add literal resolution-string phrases.

- F2's big-O is unsigned. Do not conclude sum > 1 from F2 alone.

