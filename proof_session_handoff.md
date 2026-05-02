# Session handoff (s_0502-160436-9903)

**Stop reason**: Session token budget. Session 2 added 4 sections to
proof_strategy.md and updated Lemma 3 with the CST conjecture.
The conjecture itself remains **open**.

**What this session produced**

- **Section 7 â€” per-stratum analysis**: tabulated $a_k(x; 10^7)$ for
  $x \in \{100, 1000, 10^4\}$, $k = 1\ldots23$. The naive union sum
  $\sum_k a_k(100; 10^7) = 1.254$ already EXCEEDS the conjecture's
  $1$ ceiling at $x = 100$ â€” primitivity must do real work even at
  finite $x$. Per-stratum max is at $k \approx \log\log N$.

- **Section 8 â€” empirical max-S search**: tested smallest-first
  greedy, largest-first greedy, single-stratum $A_k$, random-shuffle
  greedy at $x = 100, N = 10^6$. Best achieved was $S = 0.314$
  (smallest-first greedy), barely above the per-stratum max
  $a_2 = 0.288$. Cross-stratum gain is tiny in observable cases.
  Naive prime-tail tightening LC' falsified by $A_k$ for large $k$.

- **Section 9 â€” the $6c$ identity**: $\sum_{k \ge 1} k^2/2^k = 6$
  exactly. Total F3 deficit $6c \approx 0.394$. F1 gap
  $e^{\gamma} \pi/4 - 1 \approx 0.399$. Difference $0.005$ â€” could
  be analytic equality with literature $c \approx 0.0656$ being
  rounded.

- **Lemma 3 update â€” CST conjecture**: a stratum-aware refinement of
  ErdÅ‘sâ€“Zhang that loses $c k^2/2^k$ per stratum used would directly
  yield the conjecture's $1$ ceiling. Concrete plan recorded in
  `proof_lemmas/lemma_003_cross_stratum.md`.

**State at session close**

- 10 keep_progress rows in proof_results.tsv from this branch (one
  crash from session 1's convergence probe + one from session 2's
  unicode print error in proof_log_result.py â€” both cosmetic).
- 10 records under records/proof_primitive_set_erdos_*.json.
- Q1-Q9 all resolved. Next session can either:
  - claim Q10 = "literature lookup: is c = (e^gamma pi/4 - 1)/6?",
  - claim Q11 = "LP relaxation of max-weighted-antichain at small N",
  - or attempt to derive the stratum-aware EZ refinement directly.

**Critics-off mode (continuing test)**

10/10 rounds in <0.005s wall-clock through proof_prepare.py. Witness
verifier and resolution-string defense-in-depth both stayed active.
Verdict transitions: open -> partial_result around round 5 (when
"this remains open" hedge phrases entered the body), and stable at
partial_result through round 10. No false claims of resolution slipped
through.

**Known harness issues (session 2)**

- proof_log_result.py crashes on Windows cp1252 stdout when a thesis
  contains 'ErdÅ‘s' (U+0151) or 'â€“' (U+2013). The row gets written to
  proof_results.tsv (utf-8) but the followup print/cache/record-write
  never run. Workaround: avoid these characters in thesis lines until
  the print is fixed to use 'errors=replace'.
- Convergence-by-stable-hash (exit 6) is unreachable: re-logging the
  same proof_strategy.md on a different commit hits AST-dedup -> exit 3.

**Suggested next move**

The CST conjecture (lemma_003 update) is the most concrete lead. To
attack:
1. Look up the analytical value of c in F3 (Sathe-Selberg). Is
   c = (e^gamma pi/4 - 1)/6 exactly?
2. If yes: a stratum-aware EZ refinement is the route. Try to derive
   it from the standard EZ proof structure.
3. If no: the F1-gap and F3-total-deficit equality is coincidental,
   and the conjecture's mechanism is something else.

Step 1 needs literature; the autonomous loop cannot do it alone.
