# Session handoff (session s_0503-163730-1b00)

**Stop reason**: One round logged. Returning control to /loop driver.

**This session's contribution (Round 18, Â§17)**

Direct SPF sieve at $N = 10^7$, computing $S_k(N)$ for $k=1\ldots10$.
The asymptotic $1 - S_k \approx c k^2/2^k$ does NOT approximately
hold at this $N$ â€” implied $c$ grows from $0.10$ at $k=2$ to $10.2$
at $k=10$. Reason: $A_k$ mass saturates at $u_k = e^{e^k}$, which
is $\sim 10^{65}$ at $k=5$ and $\sim 10^{1295}$ at $k=8$. No feasible
sieve reaches the regime.

Conclusion: the Â§16 dichotomy (whether literature $c \approx 0.0656$
is the exact $c_\star = 0.06647517\ldots$) **cannot be settled
autonomously by numerical experiment**. Option (1) from the prior
handoff is closed.

**Three remaining paths to close Â§9**

(a) Literature lookup of explicit Satheâ€“Selberg formula â€” outside
    autonomous scope.
(b) First-principles re-derivation via Mertens integrals â€” research
    paper scale.
(c) Side-step Â§9 entirely: pursue Â§11.4 cross-stratum exclusion as
    the route to Lemma 3, without needing the Â§9 identity.

**For the next session: pursue (c)**

Section 11.4 sketches that cross-stratum primitivity excludes
$b \in A_{k_2}$ unless every $k_1$-divisor of $b$ falls below the
floor $x$. The Â§13 ErdÅ‘sâ€“Kac analysis already gives the threshold
$k_1 < \sqrt{2 k_2}$. The unfinished step is **quantifying the
mass loss** â€” showing that the cross-stratum-restricted sum is
sub-Behrend by enough to drop the EZ ceiling from $1.399$ to $1$.

Concrete next move: write a candidate Section 18 attempting an
explicit bound on
\[
S\!\left(\bigsqcup_{k_1 < k_2} A^{(k_1)} \cup A^{(k_2)}\right)
\]
using the Â§13.2 mass-loss estimate. If even a heuristic
calculation gives the right $\sim 1$ asymptotic, that's a strong
sign the Lemma 3 closing direction is via Â§11.4 / Â§13 rather than
Â§9.

**Files modified this session**

- `proof_strategy.md` â€” added Section 17 (~95 lines).
- `proof_lemmas/lemma_003_cross_stratum.md` â€” Round 18 update.
- `proof_open_questions.jsonl` â€” Q17 claimed and resolved.
- `proof_journal.jsonl` â€” round 18 entry.
- 1 new record in `records/`.

**qid in flight**: none. Q17 resolved. Next qid is Q18.

**Status of partial result**

The Â§9 closing route is downgraded (was: contingent on literature
lookup; now: also confirmed not-resolvable-by-sieve). The Â§11.4
cross-stratum exclusion route remains the most promising
autonomous direction. 18 rounds across 9 sessions; 18 keeps;
0 disproofs; conjecture remains open with no false claim.
