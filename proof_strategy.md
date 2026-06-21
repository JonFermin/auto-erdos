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
- **F3 read upside-down**. F3 gives a sum STRICTLY LESS THAN 1 for large $k$.
  The leading correction $-(c+o(1)) k^2/2^k$ is negative.
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

**This is a partial result.** Sections 1–3 establish, from F3 and
primitivity alone (no external citations), a rigorous LP constraint and
single-stratum bound valid in the asymptotic regime of F3. Section 4
identifies the missing analytical ingredient without citing it. The full
conjecture **this remains open**; no resolution is claimed here.

---

## Section 1: Notation

Fix $x \geq 2$ and a primitive set $A \subseteq [x, \infty)$ (every $a \in A$
satisfies $a \geq x$; no distinct element of $A$ divides another).

- $\Omega(n)$ = number of prime factors of $n$ with multiplicity.
- $A_k = \{n \in \mathbb{N} : \Omega(n) = k\}$ (all positive integers with
  exactly $k$ prime factors counted with multiplicity).
- $A_k^A = A \cap A_k$ (stratum-$k$ part of $A$).
- $s_k^A = \sum_{a \in A_k^A} \frac{1}{a \log a}$ (stratum-$k$ sum; $0$ if empty).
- $T(A) = \sum_{a \in A} \frac{1}{a \log a}$ (total sum to be bounded).
- $\varepsilon_k = (c+o(1)) k^2 / 2^k$ with $c \approx 0.0656 > 0$ (from F3;
  the $o(1)$ is as $k \to \infty$; since $c > 0$, there exists $K_0 \in \mathbb{N}$
  such that $\varepsilon_k > 0$ for all $k \geq K_0$).

**Convention**: All results in Sections 2–3 are stated for $k \geq K_0$ (where
$K_0$ is as above). For $k < K_0$, F3's asymptotic formula may not yield
$\varepsilon_k > 0$, and those strata are not covered by the partial result.

**Shadow set and weight** (SET-based definitions, no double-counting):

$$\mathrm{Shad}_k^A := \bigl\{ am \in \mathbb{N} : a \in A_j^A \text{ for some }
  j < k,\; m > 1,\; \Omega(am) = k \bigr\}$$

This is defined as a **set** of integers (with each integer appearing at most
once, even if produced by multiple $(a, m)$ pairs).

$$W_k^A := \sum_{n \in \mathrm{Shad}_k^A} \frac{1}{n \log n}$$

(sum over DISTINCT elements of $\mathrm{Shad}_k^A$; each integer contributes exactly once).

**Facts cited in Sections 1–3**: F3 only, applied for $k \geq K_0$.

**Note on F2 vs F3**: F2 gives a LOWER bound $\sum_{n \in A_k} 1/(n \log n) \geq 1 + O(k^{-1/2+o(1)})$
(with unsigned big-O, so the bound is $\geq 1 - O(k^{-1/2})$ in the worst case). F3 gives the
EXACT value $1 - \varepsilon_k$ (an upper bound via equality). Our proof uses F3 for the UPPER
bound $s_k^A \leq \sum_{A_k} = 1 - \varepsilon_k$. F2's lower bound on $\sum_{A_k}$ does not
directly constrain $s_k^A$ (it bounds the full stratum sum from below, not from above). The two
facts are consistent: explicitly, $k^{5/2}/2^k \to 0$ as $k \to \infty$ (exponential beats
polynomial), so $k^2/2^k = o(k^{-1/2})$. Since $0 < \varepsilon_k = (c+o(1))k^2/2^k$ we get
$0 < \varepsilon_k \ll k^{-1/2}$, hence $1 - \varepsilon_k > 1 - Ck^{-1/2}$ for large $k$.

---

## Section 2: LP constraint (from F3 + primitivity; no external citations)

**Lemma [LP]**: For any primitive $A \subseteq [x, \infty)$ and any $k \geq K_0$:
$$s_k^A + W_k^A \leq 1 - \varepsilon_k.$$

**Proof of [LP]**.

Set $S_1 := A_k^A$ and $S_2 := \mathrm{Shad}_k^A$ (a set by definition above).

**Step 1 (Disjointness via primitivity)**: $S_1 \cap S_2 = \emptyset$.

Suppose for contradiction that $n \in S_1 \cap S_2$. Then $n \in A$ (since
$S_1 \subseteq A$). Also $n \in S_2$, so $n = am$ for some $a \in A$ with
$\Omega(a) = j < k = \Omega(n)$ and $m > 1$. Thus $a \mid n$ with $a, n \in A$
and $a \neq n$. This contradicts primitivity of $A$. $\square$

**Step 2**: By definition $S_1 \subseteq A_k$; each $n \in S_2 = \mathrm{Shad}_k^A$
satisfies $\Omega(n) = k$, so $S_2 \subseteq A_k$. Thus $S_1 \cup S_2 \subseteq A_k$.

**Step 3 (Bound via F3)**: By F3:
$\sum_{n \in A_k} 1/(n \log n) = 1 - \varepsilon_k$.
Since $S_1 \cap S_2 = \emptyset$ (Step 1) and $S_1 \cup S_2 \subseteq A_k$
(Step 2), and since all terms $1/(n \log n) > 0$:
$$s_k^A + W_k^A
= \sum_{n \in S_1} \frac{1}{n \log n} + \sum_{n \in S_2} \frac{1}{n \log n}
= \sum_{n \in S_1 \cup S_2} \frac{1}{n \log n}
\leq \sum_{n \in A_k} \frac{1}{n \log n}
= 1 - \varepsilon_k. \quad \square$$

The second equality uses $S_1 \cap S_2 = \emptyset$ (no element appears in
both sums); the sum over $S_2$ does not double-count since $\mathrm{Shad}_k^A$
is a set.

**Corollary [LP$_0$]**: For $k \geq K_0$, $s_k^A \leq 1 - \varepsilon_k$.

*Proof*: $W_k^A \geq 0$ (non-negative sum over a possibly empty set),
so $s_k^A \leq s_k^A + W_k^A \leq 1 - \varepsilon_k$ by [LP]. $\square$

**Corollary [LP-comp]** (complementary slackness): For $k \geq K_0$,
$$W_k^A \leq (1 - \varepsilon_k) - s_k^A.$$

*Proof*: Immediate from [LP]. $\square$

*Interpretation*: The shadow weight and the stratum contribution trade off within the
budget $1 - \varepsilon_k$. If $s_k^A$ is large (stratum $k$ is heavily occupied by $A$),
then $W_k^A$ is small (little room for shadow weight). Conversely, if $W_k^A$ is large
(lower-stratum elements of $A$ cast many multiples into stratum $k$), then $s_k^A$ is small.

If one also had a LOWER BOUND $W_k^A \geq L_k^A$ for some $L_k^A \geq 0$ depending on lower strata,
then [LP-comp] would give $s_k^A \leq (1-\varepsilon_k) - L_k^A$, and summing over $k$ and $L_k^A$
being large enough could close the argument. The shadow density lower bound in Section 4 is one
candidate for such an $L_k^A$; it is a conjectured, unproved lower bound on $W_k^A$.

---

## Section 3: Single-stratum primitive sets (from F3; no external citations)

**Claim**: For any $k_0 \geq K_0$ and any primitive $A \subseteq A_{k_0} \cap [x, \infty)$
(all elements of $A$ have $\Omega(a) = k_0$):
$$T(A) = s_{k_0}^A \leq 1 - \varepsilon_{k_0} < 1.$$

**Proof**: Apply [LP$_0$] with $k = k_0 \geq K_0$, which gives $s_{k_0}^A \leq 1 - \varepsilon_{k_0}$.
Since $k_0 \geq K_0$ ensures $\varepsilon_{k_0} > 0$ (by the definition of $K_0$),
we obtain $T(A) < 1$. $\square$

**Remark on scope**: The threshold $K_0$ is determined by F3: since
$\varepsilon_k = (c + o(1))k^2/2^k$ with $c > 0$, we have $\varepsilon_k > 0$
for all sufficiently large $k$, so $K_0$ is finite and the claim is non-vacuous.

**Proposition [$K_0 \geq 2$]**: The claim does NOT hold for $k_0 = 1$.

*Proof*: The set $\{2, 3\} \subseteq A_1 \cap [2, \infty)$ is primitive (2 does not
divide 3, and 3 does not divide 2). Its sum is:
$$T(\{2,3\}) = \frac{1}{2\log 2} + \frac{1}{3\log 3}.$$
Using the standard values $\log 2 = 0.6931\ldots$ and $\log 3 = 1.0986\ldots$:
$$T(\{2,3\}) = \frac{1}{1.3862\ldots} + \frac{1}{3.2958\ldots}
= 0.7213\ldots + 0.3035\ldots = 1.0249\ldots > 1.$$
If F3 held at $k = 1$ with $\varepsilon_1 > 0$, the claim's conclusion would give
$T(\{2,3\}) \leq 1 - \varepsilon_1 < 1$, contradicting $T(\{2,3\}) = 1.0249\ldots > 1$. By
contrapositive, $k_0 = 1$ is outside the claim's scope: $K_0 \geq 2$. $\square$

---

## Section 4: What remains open — the shadow density gap

Sections 2–3 establish: in any stratum where F3 applies, the stratum-$k$
contribution of any primitive set $A$ satisfies $s_k^A < 1$. The challenge
for the full conjecture is multi-stratum behavior: showing that strata cannot
simultaneously all contribute close to $1 - \varepsilon_k$.

The mechanism preventing simultaneous near-maximal contributions is the
**shadow**: each $a \in A$ with $\Omega(a) = j$ forces all multiples $am$ out
of $A$ (by primitivity), reducing available weight in strata $k > j$.
This is captured by $W_k^A$ in [LP].

For the full conjecture, one would need a lower bound on $W_k^A$ in terms of
weight accumulated in lower strata. Conjecturally:
$$W_k^A \geq T_{k-1}^A - o(1), \quad T_{k-1}^A = \sum_{j<k} s_j^A,$$
but this is not derived here — it is the missing ingredient, not a proved fact.

Establishing this requires asymptotic counts of squarefree integers with a
given number of prime factors in a specified range — information **not in the
given-facts ledger** $\{$F1, F2, F3$\}$. This gap is the core analytical
difficulty keeping the conjecture open.

**We cannot prove the lower bound on $W_k^A$, and we do not claim to.**
[LP] gives only $W_k^A \geq 0$, too weak to close the argument.

Similarly, bounding the tail $\sum_{k > K} s_k^A$ for large $k$ (beyond a
threshold $K$ depending on $x$) requires density estimates for integers with
many prime factors — also absent from the ledger.

**Summary of what is proved vs open**:

| Statement | Status |
|---|---|
| $s_k^A + W_k^A \leq 1 - \varepsilon_k$ (LP constraint, F3 range) | **Proved** from F3 + primitivity |
| $s_k^A \leq 1 - \varepsilon_k$ (stratum bound, F3 range) | **Proved** from F3 |
| $T(A) < 1$ for single-stratum $A$ with $k_0$ in F3 range | **Proved** from F3 |
| Shadow density lower bound $W_k^A \geq T_{k-1}^A - o(1)$ | **Open** — needs external estimate |
| Tail bound $\sum_{k > K} s_k^A = o(1)$ for large $k$ | **Open** — needs counting estimate |
| Full conjecture: $T(A) \leq 1 + o(1)$ for all primitive $A$ | **Open** |

This is a **partial result**: the LP constraint and its consequences are
rigorous from the ledger in the large-$k$ asymptotic regime of F3; the full
conjecture requires analytical tools beyond {F1, F2, F3}.
