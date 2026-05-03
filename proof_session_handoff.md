# Session handoff (session s_0503-170719-5bd6)

**Stop reason**: One round logged. Returning to /loop driver.

**This session's contribution (Round 19, §18)**

Computed explicit two-stratum cross-exclusion sums
$S(A^{(k_1)} \sqcup A^{(k_2)}_\text{kept})$ for
$(k_1, k_2) \in \{(2,3),(2,4),(2,5),(3,4),(3,5),(3,6)\}$
at $x \in \{10^2, 10^3, 10^4\}$, $N = 10^6$.

KEY RESULT: maximum two-stratum sum decays
$0.337 \to 0.212 \to 0.133$ as $x$ grows. Decay is faster than
$1/\log x$. Pair $(k_1, k_2) = (2, 4)$ dominates at every tested
$x$. Kept fraction grows above the §13 threshold $k_1 < \sqrt{2 k_2}$:
at $(2,5)$ it reaches 38% at $x=10^4$, while at $(3,4)$ it stays
at 1.5%.

This is the strongest pro-conjecture numerical signal across
19 rounds — the data is consistent with $\sup S(A) \to 0$ as
$x \to \infty$ (stronger than the $\le 1 + o(1)$ conjecture asks).

**For next session**

Concrete analytic target identified in §18.5: prove a saddle-point
inequality
\[
\sup_A S(A) \;\le\; \sum_k a_k(x) \cdot \rho_k(x) \;\to\; 1\;(\text{or } 0)
\]
where $\rho_k(x)$ is the cross-stratum kept fraction. §13's
Erdős–Kac threshold $k_1 < \sqrt{2 k_2}$ gives $\rho_k$ asymptotics;
the missing step is bounding $\sum_k a_k \rho_k$ by a single
integral via saddle-point.

**Two productive next moves**

(a) **Extend the §18 table to $N = 10^7$** and $x \in \{10^5, 10^6\}$
    to confirm the decay rate. Wallclock ~5 min.
(b) **Sketch the saddle-point bound on $\sum_k a_k(x) \rho_k(x)$**
    in §13/§18 framework. This is the analytical step toward Lemma 3.

Recommendation: do (b) first — the empirical evidence in §18 is
already compelling; further numerical extension adds confidence
but doesn't move the proof forward. The saddle-point sketch is
the substantive step.

**Encoding note for future sessions**

`proof_log_result.py` crashes with `UnicodeEncodeError` on Windows
when the thesis string contains characters outside cp1252 (e.g.,
`→`, em-dashes are sometimes affected too). Workaround: use ASCII
in thesis strings, or set `PYTHONIOENCODING=utf-8` env var. Round
19 hit this and required a manual rollback of `proof_results.tsv`
plus re-run with ASCII thesis. Section 18 in `proof_strategy.md`
itself uses Unicode freely (UTF-8 source file is fine), only the
thesis arg to `proof_log_result.py` is constrained. Recording for
the next session — set `PYTHONIOENCODING=utf-8` proactively.

**Files modified this session**

- `proof_strategy.md` — added Section 18 (~120 lines).
- `proof_lemmas/lemma_003_cross_stratum.md` — Round 19 update.
- `proof_open_questions.jsonl` — Q18 claimed and resolved.
- `proof_journal.jsonl` — round 19 entry.
- 1 new record in `records/`.

**qid in flight**: none. Q18 resolved. Next is Q19.

**Status**

19 rounds across 10 sessions. 19 keeps. 0 disproofs. Conjecture
remains open. The §11.4/§13/§18 cross-stratum exclusion route is
now the strongest empirical-and-structural path — but the
analytical closing step is still ahead.
