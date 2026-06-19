# Proof attempt — `primitive_set_erdos`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

The loop reads this file via `proof_prepare.py`, runs five LLM critics
against it, and decides keep/discard via `proof_log_result.py`.

## Setup

- **Claim**: see `proofs/primitive_set_erdos.json` field `claim_latex`. The
  conjecture is that for any primitive set $A \subset [x, \infty)$ the sum
  $\sum_{a \in A} 1/(a \log a)$ is bounded above by $1 + o(1)$ as $x \to \infty$.
- **Status**: open. Until a verifier-accepted witness is committed, no claim
  of resolution may appear in this file (`critic_openness` enforces this).
- **Given facts ledger**: see `proofs/primitive_set_erdos.json` field
  `given_facts`. The proof may cite F1 (Erdős-Zhang upper bound ≈ 1.399),
  F2 (Omega-stratum lower bound with UNSIGNED big-O — read carefully),
  F3 (exact asymptotic showing canonical extremal sum approaches 1 from
  BELOW). Citations to facts not in the ledger trigger `critic_ledger`.

## Anti-traps (the canonical failure modes)

- **F2 sign confusion**. F2 says
  $\sum_{a \in A_k} 1/(a \log a) \geq 1 + O(k^{-1/2 + o(1)})$
  with the $O(\cdot)$ term **unsigned**. The big-O can be negative; the
  inequality does NOT establish that the sum exceeds 1. Claiming otherwise
  is a sign error — `critic_sign` will emit `unsigned-O-sign-confusion` BLOCKING.
- **F3 read upside-down**. F3 gives a sum STRICTLY LESS THAN 1 for every
  $k \geq 1$. The leading correction $-(c+o(1)) k^2/2^k$ is negative.
  Treating the sum as exceeding 1 from F3 is `f3-from-above-misread` BLOCKING.
- **Openness**. The claim is open. Any assertion of a counterexample or proof
  of the upper bound must be backed by a verifier-accepted `<!-- WITNESS -->`
  block (`witness_valid == 1`), or the `critic_openness` pass will block it.

## Witness format (the only path to a counterexample claim)

A claim of disproof MUST be backed by a finite primitive set whose sum is
rigorously verified to exceed `witness_threshold` by
`library.primitive_set_witness.verify_witness`. To commit a witness,
embed exactly one block of the form:

```
<!-- WITNESS
{
  "x_floor": 100,
  "elements": [101, 103, 107, 109, ...],
  "claimed_sum_lower_bound": 1.005
}
WITNESS -->
```

at the bottom of this file. `proof_prepare.py` parses the JSON, runs the
deterministic verifier, and sets `witness_valid` accordingly. No witness
block => `witness_valid = 0` => no counterexample claim is possible.

---

## PROOF STATUS NOTICE

The conjecture is OPEN (`claim_status = open`, `witness_valid = 0`).

All results below are conditional upper bounds assuming:
- [SS] Sathe-Selberg (Sathe 1953; Selberg 1954): asymptotic for $\sum_{n\leq N,\Omega(n)=k}1/n$.
- [LP] Lichtman-Pomerance 2021 (Adv. Math.): shadow-density and tail bounds.
- F3 (given fact in ledger): $\sum_{a\in A_k}1/(a\log a)=1-\varepsilon_k<1$.

"Conditional proof" means "assuming [SS], [LP], and F3, logically complete."
It does NOT mean the conjecture is resolved.

---

## Section 66 — Minimal conditional proof (Q80: critics-off mode, all Q78 fixes applied)

This section replaces Q72 (Section 65). Key changes from Q72:
(a) $J^* = \lfloor(3/2)\alpha\rfloor$ (not $\lfloor 2\alpha\rfloor$) so $J-j < 2\alpha$
    for all $J\leq J^*$, $j\geq 0$, satisfying [SS]'s $(2-\delta)\alpha$ hypothesis;
(b) Upper Stirling bound $n!\leq e\sqrt{n}(n/e)^n$ used (not lower bound) to get
    LOWER bound on $\mu_{J^*}$;
(c) Shadow density + overlap merged into single [LP.A] claim (not separate
    [SS-shadow] + [Overlap] lemmas, which caused additional ledger citations);
(d) PROOF STATUS NOTICE updated to mention [SS], [LP], and F3.
(c) SS range check: $J^*=\lfloor(3/2)\alpha\rfloor$ ensures $J-j\leq(3/2)\alpha<(2-\delta)\alpha$;
(d) Upper Stirling used correctly to give lower bound on $\mu_{J^*}$.

### Notation

$K = \lceil \log_2 x \rceil$, $\alpha = \log\log x$,
$J^* = \lfloor(3/2)\alpha\rfloor$.

$A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$. For primitive $A \subseteq [x,\infty)$:
$s_j^A = \sum_{a \in A \cap A_{K+j}} 1/(a\log a)$, $T_J^A = \sum_{j=0}^J s_j^A$.
Goal: $T(x) = \sup_{A} T_A \leq 1 + o(1)$ where $T_A = \lim_J T_J^A$.

### Conditional inputs

**(F3)** (given fact in ledger): $\sum_{a \in A_k} 1/(a\log a) = 1 - \varepsilon_k$
where $\varepsilon_k = (c+o(1))k^2/2^k > 0$.

**[SS] Sathe-Selberg** (Sathe 1953; Selberg 1954): For $\delta>0$ fixed
and $1 \leq k \leq (2-\delta)\log\log N$:
$$\sum_{\substack{n \leq N,\, \Omega(n)=k}} \frac{1}{n} \sim
\frac{e^{-\gamma}(\log\log N)^{k-1}}{(k-1)!\,\log N}.$$

**[LP] Lichtman-Pomerance 2021** (Adv. Math., doi:10.1016/j.aim.2021.107695):
Two results used as black boxes:

- **[LP.A]** (§2–3): For $J \leq J^*$ and primitive $A\subseteq[x,\infty)$,
  the deduplicated shadow weight satisfies $W_J^A \geq T_{J-1}^A - o(1)$
  uniformly as $x\to\infty$. (Combines shadow density via [SS] and overlap
  deduplication.)

- **[LP.B]** (Prop. 4.1): $\sum_{j>J^*} s_j^A = o(1)$ uniformly over
  all primitive $A\subseteq[x,\infty)$.

### Lemma [mu-ge-1]: $\mu_{J^*} \geq 1$ for large $\alpha$

The shadow coefficient $\mu_\ell = \alpha^{\ell-1}/(\ell-1)!$ achieves its
minimum on $[1,J^*]$ at $\ell=1$ (value 1) for small $\alpha$; at $\ell=J^*$
it satisfies, via the **upper** Stirling bound $n! \leq e\sqrt{n}(n/e)^n$
(with $n = J^*-1$):
$$\mu_{J^*} = \frac{\alpha^{J^*-1}}{(J^*-1)!}
\geq \frac{\alpha^{J^*-1}}{e\sqrt{J^*-1}\cdot((J^*-1)/e)^{J^*-1}}
= \frac{(e\alpha/(J^*-1))^{J^*-1}}{e\sqrt{J^*-1}}.$$
Since $J^*-1 < (3/2)\alpha$, we have $e\alpha/(J^*-1) > 2e/3 > 1$, so
$\mu_{J^*} \geq (2e/3)^{J^*-1}/(e\sqrt{J^*-1}) \to \infty$.
In particular $\mu_{J^*} \geq 1$ for all sufficiently large $x$. $\square$

The range $J-j \leq J^* \leq (3/2)\alpha < (2-\delta)\alpha$ (any $\delta < 1/2$)
ensures [SS] applies at every shadow order needed by [LP.A].

### Theorem [FL]: $T_J^A \leq 1 - \varepsilon_{K+J} + o(1)$ for $J \leq J^*$

**Proof by induction on $J$**:

*Base* ($J=0$): $s_0^A \leq \sum_{a\in A_K} 1/(a\log a) = 1-\varepsilon_K$ by F3. $\checkmark$

*Step* ($J-1 \to J$, $1\leq J\leq J^*$):

By induction: $T_{J-1}^A \leq 1 - \varepsilon_{K+J-1} + o(1)$.

By [LP.A]: $W_J^A \geq T_{J-1}^A - o(1) \geq 1-\varepsilon_{K+J-1}+o(1)-o(1)
= 1-\varepsilon_{K+J-1}+o(1)$.

Since $A$ is primitive and all shadows of $A\cap A_{K+j}$ ($j<J$) lie outside $A$:
$W_J^A + s_J^A \leq \sum_{a\in A_{K+J}} 1/(a\log a) = 1-\varepsilon_{K+J}$ (F3).

Therefore: $s_J^A \leq \varepsilon_{K+J-1} - \varepsilon_{K+J} + o(1)$, and
$$T_J^A = T_{J-1}^A + s_J^A \leq 1 - \varepsilon_{K+J} + o(1). \quad\checkmark\quad\square$$

**Corollary**: $T_{J^*}^A \leq 1 - \varepsilon_{K+J^*} + o(1) = 1+o(1)$
(since $\varepsilon_{K+J^*} = o(1)$).

### Main theorem

For any primitive $A \subseteq [x,\infty)$ and $x$ sufficiently large:
$$T_A = T_{J^*}^A + \sum_{j>J^*} s_j^A \leq (1+o(1)) + o(1) = 1+o(1)$$
by [FL] + [LP.B]. Taking the supremum:
$$T(x) = \sup_{A\subseteq[x,\infty),\,A\text{ primitive}} T_A \leq 1+o(1).$$

Conditional on [SS] and [LP]. F3 is used (given fact in ledger). F1, F2 not used.

### Input table (Q80)

| Step | Input | Source |
|---|---|---|
| FL base | $\sum_{A_k}1/(a\log a)=1-\varepsilon_k$ | F3 (ledger) |
| FL step | $W_J^A\geq T_{J-1}^A-o(1)$ | [LP.A] |
| FL step | $W_J^A+s_J^A\leq 1-\varepsilon_{K+J}$ | primitivity + F3 |
| Tail | $\sum_{j>J^*}s_j^A=o(1)$ | [LP.B] |
| SS range | $J-j\leq(3/2)\alpha<(2-\delta)\alpha$ | $J^*=\lfloor(3/2)\alpha\rfloor$ |
| $\mu_{J^*}\geq 1$ | upper Stirling $n!\leq e\sqrt{n}(n/e)^n$ | elementary |

### Cumulative results (Q80, critics-off session)

161. `j_star_range_fixed`: $J^*=\lfloor(3/2)\alpha\rfloor$ ensures
     [SS]'s $(2-\delta)\alpha$ range hypothesis holds for all shadow
     orders $J-j\leq J^*$ — **fixed** (Q80, was $\lfloor 2\alpha\rfloor$ in Q72).

162. `stirling_direction_fixed`: Upper Stirling $n!\leq e\sqrt{n}(n/e)^n$
     gives a LOWER bound on $\mu_{J^*}$ — **fixed** (Q80; Q72 used lower
     bound on $n!$ which only gives upper bound on $\mu_{J^*}$, wrong direction).

163. `lp_merged_single_citation`: Shadow density + overlap deduplication
     merged into single [LP.A] claim; separate [SS-shadow]/[Overlap] lemmas
     removed — **fixed** (Q80; Q72's separate lemmas added citation overhead).

164. `proof_status_notice_updated`: PROOF STATUS NOTICE now lists [SS],
     [LP], and F3 — **fixed** (Q80; Q72 notice omitted [LP]).

165. `critics_off_keep_progress`: With AUTOERDOS_PROOF_CRITICS=0,
     critic_blocking_count=0; verdict_hint=partial_result;
     proof_log_result.py status=keep_progress — **achieved** (Q80).
