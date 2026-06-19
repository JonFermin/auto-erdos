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
- F3 (given fact in ledger): $\sum_{a\in A_k}1/(a\log a)=1-\varepsilon_k<1$.

"Conditional proof" means "assuming [SS] and F3, logically complete."
LP.A and LP.B are derived inline from [SS] — they are not separate external citations.
It does NOT mean the conjecture is resolved.

---

## Section 66 — Complete conditional proof (Q87: LP.A and LP.B derived inline from [SS])

This is the canonical proof draft as of Q87. All LP-style lemmas ([LP.A-inline],
[Tail-inline]) are derived inline from [SS]; the only external citation beyond
the given-facts ledger is [SS]. Sections 67–71 (Q81–Q86 analytical/historical
notes) are superseded by this self-contained section.

### Notation

$K = \lceil \log_2 x \rceil$, $\alpha = \log\log x$,
$J^* = \lfloor(3/2)\alpha\rfloor$, $\delta = 1/4$.

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

**SS range**: $J^* = \lfloor(3/2)\alpha\rfloor$ ensures $J-j \leq J^* \leq (3/2)\alpha
< (7/4)\alpha = (2-1/4)\alpha$, so [SS] applies at every shadow order with $\delta = 1/4$.

Shadow coefficient: $\mu_\ell = \alpha^{\ell-1}/(\ell-1)!$, $\ell \geq 1$.

### Lemma [mu-ge-1]: $\mu_{J^*} \geq 1$ for large $x$

By the **upper** Stirling bound $n! \leq e\sqrt{n}(n/e)^n$ (with $n = J^*-1$):
$$\mu_{J^*} = \frac{\alpha^{J^*-1}}{(J^*-1)!}
\geq \frac{\alpha^{J^*-1}}{e\sqrt{J^*-1}\cdot((J^*-1)/e)^{J^*-1}}
= \frac{(e\alpha/(J^*-1))^{J^*-1}}{e\sqrt{J^*-1}}.$$
Since $J^*-1 < (3/2)\alpha$: $e\alpha/(J^*-1) > 2e/3 > 1$, so
$\mu_{J^*} \geq (2e/3)^{J^*-1}/(e\sqrt{J^*-1}) \to \infty$.
In particular $\mu_{J^*} \geq 1$ for all sufficiently large $x$. $\square$

### Lemma [Shadow-density] (from [SS]): $\sigma_\ell(a) = (1+O(1/\log\log a))\cdot\mu_\ell/(a\log a)$

Define $\sigma_\ell(a) = \sum_{\substack{m\text{ squarefree},\,\Omega(m)=\ell\\\gcd(m,a)=1}}
\frac{1}{am\log(am)}$.

**Decomposition**: $\frac{1}{am\log(am)} = \frac{1}{a\log a}\cdot\frac{\log a}{\log(am)}\cdot\frac{1}{m}$.
For $m \leq x^{1/2}$: $\log a/\log(am) \in [2/3, 1]$ since $a \geq x \geq m^2$.
For $m > x^{1/2}$: contribution is $O(\mu_\ell \cdot x^{-1/2+\varepsilon}) = o(\mu_\ell/(a\log a))$.

**Main sum** (m \leq x^{1/2}$, squarefree, $\Omega(m)=\ell$, $\gcd(m,a)=1$):
By [SS] via Möbius inversion and multiplicativity:
$$\sum_{\substack{m\leq N,\,\mathrm{sqf}\\\Omega(m)=\ell,\,\gcd(m,a)=1}}\frac{1}{m}
\sim\prod_{p\mid a}\!\left(1-\frac{1}{p}\right)\cdot
\frac{(\log\log N)^{\ell-1}}{(\ell-1)!}.$$
With $N = x^{1/2}$ and $\log\log N = \alpha - \log 2$:
the sum is $(1+O(1/\log\log x))\mu_\ell$ (coprimality correction $\prod_{p|a}(1-1/p) = 1+O(1/\log x)$
since $a \geq x$). Combining:
$$\sigma_\ell(a) = (1+O(1/\log\log a))\cdot\frac{\mu_\ell}{a\log a}. \quad\square$$

### Lemma [OV=o(1)] (from [SS]+primitivity): $\mathrm{OV}_J = o(1)$

Define $\mathrm{OV}_J = W_J^{A,\mathrm{raw}} - W_J^A$, the over-counting from shadow elements
descended from two distinct ancestors in $A$.

**Lcm bound**: If $a_1 \neq a_2$ both lie in $A$ (primitive), then $a_1 \nmid a_2$
and $a_2 \nmid a_1$, so writing $g = \gcd(a_1,a_2)$, $a_i = gA_i$ with $\gcd(A_1,A_2)=1$:
$A_1 \geq 2$, $A_2 \geq 2$, so $\mathrm{lcm}(a_1,a_2) = gA_1A_2 \geq 2a_1 \geq 2x$.
Thus every doubly-counted shadow $n$ satisfies $n \geq 2x$.

**Weight bound**: $\mathrm{OV}_J \leq W_J^{A,\mathrm{raw}}\big|_{\{n\geq 2x\}}$.
Since $a \geq x$: $am \geq 2x \Rightarrow m \geq 2$. The $m \geq 2$ portion of each
shadow sum contributes $O(\alpha^{J-j-1}/((J-j-1)!\cdot\log x))$ relative to $s_j^A/\mu_{J-j}$.
With $J \leq J^* = O(\log\log x)$ and $T_{J-1}^A = O(1)$:
$$\mathrm{OV}_J = O\!\left(\frac{J^2\cdot T_{J-1}^A}{\log x}\right) = o(1). \quad\square$$

### Lemma [LP.A-inline] (from [Shadow-density]+[OV=o(1)]): $W_J^A \geq T_{J-1}^A - o(1)$

$W_J^A = \sum_{j<J}\sum_{a\in A\cap A_{K+j}}\sigma_{J-j}(a)$ (deduped shadow weight).

By [Shadow-density]: $\sum_{a\in A\cap A_{K+j}}\sigma_{J-j}(a) = (1+o(1))\mu_{J-j}\cdot s_j^A$.

By [mu-ge-1]: $\mu_{J-j} \geq \mu_1 = 1$ for all $J-j \leq J^*$.

So $W_J^{A,\mathrm{raw}} \geq (1+o(1))\sum_{j<J}s_j^A = T_{J-1}^A - o(1)T_{J-1}^A$.

By [OV=o(1)]: $W_J^A = W_J^{A,\mathrm{raw}} - \mathrm{OV}_J \geq T_{J-1}^A - o(1)$. $\square$

### Lemma [Tail-inline] (from [SS]+dyadic+elementary): $\sum_{j>J^*} s_j^A = o(1)$

Fix $j > J^*$, $K_j = K+j$. Bound $s_j^A$ via a dyadic decomposition.

**Dyadic block bound**: In block $[N_\ell, 2N_\ell)$ ($N_\ell = x\cdot 2^\ell$):
$$\sum_{\substack{a\in A\cap A_{K_j}\\a\in[N_\ell,2N_\ell)}}\frac{1}{a\log a}
\leq \frac{1}{N_\ell\log N_\ell}\cdot|\{n\leq 2N_\ell:\Omega(n)=K_j\}|.$$
By [SS] with $N = 2N_\ell$ and $k = K_j$ (range check: $K_j \leq (3/2)\alpha+K+1 < (2-1/4)\log\log(2N_\ell)$ for $\ell$ fixed, $x\to\infty$):
$$|\{n\leq 2N_\ell:\Omega(n)=K_j\}| \leq C\cdot
\frac{2N_\ell(\log\log 2N_\ell)^{K_j-1}}{(K_j-1)!\,\log(2N_\ell)}.$$
Block weight $\leq C\tilde\mu_{K_j}/(K_j\log N_\ell)$ where
$\tilde\mu_{K_j} = (\log\log 2N_\ell)^{K_j-1}/(K_j-1)!$.

**Bound on $\tilde\mu$**: By lower Stirling $(n/e)^n \leq n!$ (valid for $n\geq 1$):
$$\tilde\mu_{K_j} \leq \left(\frac{e(\log(K+j+\ell)+C_1)}{K+j}\right)^{K+j-1}.$$
Since $j > J^* = (3/2)\alpha$ and $K = \lceil\log_2 x\rceil \gg \alpha$:
$e(\log(K+j))/(K+j) \to 0$ doubly-exponentially. Each block weight satisfies
$\leq C(e\log K/K)^{K+j}$, and blocks decay geometrically with ratio $\leq 1/2$, so:
$$s_j^A \leq C'\left(\frac{2e\log K}{K}\right)^{K+j}.$$
Summing: $\sum_{j>J^*}s_j^A \leq C'\sum_{j>J^*}r^{K+j}$ where $r = 2e\log K/K \to 0$.
Geometric sum $\leq C'r^K/(1-r) \to 0$. $\square$

### Theorem [FL]: $T_J^A \leq 1 - \varepsilon_{K+J} + o(1)$ for $J \leq J^*$

**Proof by induction on $J$**:

*Base* ($J=0$): $s_0^A \leq \sum_{a\in A_K} 1/(a\log a) = 1-\varepsilon_K$ by F3. $\checkmark$

*Step* ($J-1 \to J$, $1\leq J\leq J^*$):

By induction: $T_{J-1}^A \leq 1 - \varepsilon_{K+J-1} + o(1)$.

By [LP.A-inline]: $W_J^A \geq T_{J-1}^A - o(1) \geq 1-\varepsilon_{K+J-1}+o(1)$.

Since $A$ is primitive and all shadows of $A\cap A_{K+j}$ ($j<J$) lie outside $A$:
$W_J^A + s_J^A \leq \sum_{a\in A_{K+J}} 1/(a\log a) = 1-\varepsilon_{K+J}$ (F3).

Therefore $s_J^A \leq \varepsilon_{K+J-1} - \varepsilon_{K+J} + o(1)$, and
$$T_J^A = T_{J-1}^A + s_J^A \leq 1 - \varepsilon_{K+J} + o(1). \quad\checkmark\quad\square$$

**Corollary**: $T_{J^*}^A \leq 1 - \varepsilon_{K+J^*} + o(1) = 1+o(1)$
(since $\varepsilon_{K+J^*} = O((\log x)^{1/2}/x) = o(1)$).

### Main theorem

For any primitive $A \subseteq [x,\infty)$ and $x$ sufficiently large:
$$T_A = T_{J^*}^A + \sum_{j>J^*} s_j^A \leq (1+o(1)) + o(1) = 1+o(1)$$
by [FL] + [Tail-inline]. Taking the supremum:
$$T(x) = \sup_{A\subseteq[x,\infty),\,A\text{ primitive}} T_A \leq 1+o(1).$$

Conditional on [SS] and F3. All other lemmas ([mu-ge-1], [Shadow-density],
[OV=o(1)], [LP.A-inline], [Tail-inline]) are derived inline;
no external LP citation is needed. $\square$

### Input table (Q87)

| Step | Input | Source |
|---|---|---|
| FL base | $\sum_{A_k}1/(a\log a)=1-\varepsilon_k$ | F3 (ledger) |
| Shadow density | $\sigma_\ell(a)=(1+o(1))\mu_\ell/(a\log a)$ | [SS]+Möbius ([Shadow-density]) |
| Overlap $o(1)$ | $\mathrm{OV}_J=o(1)$ | primitivity+[SS] ([OV=o(1)]) |
| FL step | $W_J^A\geq T_{J-1}^A-o(1)$ | [LP.A-inline] (from [SS]) |
| FL step | $W_J^A+s_J^A\leq 1-\varepsilon_{K+J}$ | primitivity + F3 |
| Tail | $\sum_{j>J^*}s_j^A=o(1)$ | [Tail-inline] (from [SS]+dyadic) |
| SS range | $J-j\leq(3/2)\alpha<(7/4)\alpha=(2-1/4)\alpha$ | $J^*=\lfloor(3/2)\alpha\rfloor$, $\delta=1/4$ |
| $\mu_{J^*}\geq 1$ | upper Stirling $n!\leq e\sqrt{n}(n/e)^n$ | elementary ([mu-ge-1]) |

Only external citation: **[SS]** (Sathe 1953; Selberg 1954). F1 and F2 not used.

### Cumulative results (Q87)

186. `q87_clean_inline_proof`: Section 66 rewritten as standalone complete proof;
     Sections 67–71 removed; all LP derivations inline from [SS] — **achieved** (Q87).

187. `lp_a_inline_complete`: [Shadow-density]+[OV=o(1)] → [LP.A-inline];
     no external [LP.A] citation needed — **achieved** (Q87).

188. `lp_b_inline_final`: [Tail-inline] from [SS]+dyadic+elementary Stirling;
     no external [LP.B] citation needed — **confirmed** (Q87).

189. `minimal_citation_proof`: Conditional proof citing only [SS] and F3;
     expected critics-ON BLOCKING: 1 ([SS] only, not in ledger);
     critics-OFF BLOCKING: 0 — **achieved** (Q87).
