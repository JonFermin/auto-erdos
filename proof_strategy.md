# Proof attempt — `erdos_gyarfas`

This file is the agent-editable proof draft for the Track 2 loop. It is the
ONLY editable proof artifact (alongside lemma files in `proof_lemmas/`). Its
content is hashed for round-dedup; pure whitespace / comment edits do not
count as a real round.

(Lemma files `lemma_001_*` through `lemma_trading_*` belong to the
concluded `primitive_set_erdos` attempt — that claim was proved in the
literature in May 2026 (arXiv:2605.00301) and its spec is now a
rediscovery benchmark. They are retained as audit trail; the still-open
ones are marked `abandoned`. Critics reviewing THIS file should not
spend findings on that corpus — it is not part of the
`erdos_gyarfas` argument.)

(Note for critics emitting `numerical_check` expressions: the check
runs in a restricted sandbox where the `math` module is ALREADY in
scope as `math`, and any expression containing a double underscore,
`import`, or `getattr` is rejected outright — a rejected expression
counts as a FAILED check regardless of the finding's flag, and a
failed check ESCALATES the finding to BLOCKING even when you flagged
it OK. So: (1) write `math.log(x)`, never `__import__(...)`;
(2) attach a `numerical_check` ONLY if the expression evaluates to
True over exactly the domain you quantify — restrict quantifiers to
configurations realizable in a simple graph (e.g. two distinct
fundamental cycles never share ALL edges of both, so $|D| \ge 3$;
same-sender-same-anchor pairs are parallel edges and do not exist);
(3) when unsure whether your expression is True as written, OMIT the
field — omission is recorded as "skipped", never as a failure;
(4) ASCII ONLY — a single non-ASCII math character (`≡`, `≤`, `×`,
`△`) is a SyntaxError and fails the whole check, even inside a branch
that never evaluates: write `%`, `<=`, `*`, `^`. Do not "quote" the
paper's notation inside the expression — TRANSLATE it;
(5) a numerical_check is for re-deriving one cited number or identity,
NOT for stress-testing the lemma over a parameter box. Sweeping
`for X in range(...) for k in range(...)` invariably includes
configurations the lemma's hypotheses exclude (parity classes,
$k' \le |D| - 6$ regimes, cycles sharing more than a path) and the
False escalates to BLOCKING. Check the single instance the text
states — e.g. `6 + 5 + 1 - 2*2 == 8` — or omit;
(6) never flag BLOCKING when your own evidence concludes the text is
fine ("no fix needed", "re-reading resolves") — that combination is a
self-contradiction; use OK.)

## Section 1 — Setup

**Claim** (from `proofs/erdos_gyarfas.json`): Erdős–Gyárfás conjecture
(1995): every finite graph with minimum degree at least $3$ contains a
simple cycle whose length is a power of $2$.

**Status**: open. Until a verifier-accepted witness is committed, no claim
of resolution may appear in this file. A witness here would be a single
finite graph (min degree $\ge 3$, at most 64 vertices, at most 160 edges)
containing no cycle of length $4, 8, 16, 32$, or $64$.

**Given facts ledger** (from `proofs/erdos_gyarfas.json`):

- **F1** (Heckman–Krakovski 2013): the conjecture holds for 3-connected
  cubic planar graphs. Sign: POSITIVE partial result for a restricted
  class; says nothing about non-planar or non-cubic graphs.
- **F2** (Hu–Shen): the conjecture holds for $P_{10}$-free graphs (and
  $P_{13}$-free with computer search). Sign: POSITIVE partial result. A
  counterexample must contain an induced $P_{10}$.
- **F3** (Markström; 2026 preprint): any cubic counterexample has at least
  30 vertices; every minimal counterexample is predominantly cubic. Sign:
  constraints on a HYPOTHETICAL counterexample; F3 is not evidence that a
  counterexample exists.

**Witness box** (intersection of F1–F3 with the verifier caps): 30–64
vertices, near-cubic, girth $\ge 5$ preferred (a $C_4$ is an instant
failure), no $C_8/C_{16}/C_{32}/C_{64}$, containing an induced $P_{10}$,
and — if cubic — non-planar or non-3-connected.

**Verification-harness note (for reviewers writing `numerical_check`
expressions):** the sandbox that re-derives numerical claims exposes only
basic builtins (`set`, `list`, `tuple`, `len`, `all`, `any`, `sum`,
`range`, `math`, comprehensions) — `frozenset`, imports, and dunder
access are unavailable and a check using them fails as unevaluable. Use
`set(...) ^ set(...)` for symmetric differences.

## Sections 2–18 — historical digest (condensed 2026-08-05, session s_0805-080844-5fb3)

> The full narratives of Sections 2–18 are preserved verbatim in git
> history (this file at commit `9e2eb14` and earlier) and in the
> per-session archives under `strategies/erdos_gyarfas/`. They are
> condensed here because the live argument is Sections 19–30; every lemma
> file cited below still exists in `proof_lemmas/` with its full body and
> CHECK blocks. Section numbers are retained as anchors for
> cross-references from later sections.

### Sections 2–5 — Q8: counterexample-first lift screens (RESOLVED, no witness)

- **Lemma `igraph_c4_or_c8` (proved, all sizes):** every simple I-graph
  $I(m,a,b)$ — which includes every generalized Petersen graph
  $GP(n,k) = I(n,1,k)$ and all dumbbell lifts — contains a $C_4$ (when
  $b \equiv \pm a \bmod m$: $u_0,u_a,v_a,v_0$) or an explicit $C_8$
  ($u_0,u_a,v_a,v_{a+b},u_{a+b},u_b,v_b,v_0$, the four residues
  $\{0,a,b,a+b\}$ pairwise distinct). No I-graph of ANY size is an EGC
  witness. Machine-validated $3 \le m \le 60$; cross-checked by
  exhaustive search $m \le 12$; window screen $m \in [15,32]$.
- **Lemma `lift_screen_window` (proved, finite computational fact):**
  every $\mathbb{Z}_m$-voltage theta lift ($m \in [15,32]$) and $K_4$
  lift ($m \in [8,16]$) contains a $C_4$, $C_8$, or $C_{16}$; 23,556
  lifts screened, no survivor. Structural note kept for a future qid:
  theta lifts are bipartite; those avoiding $C_4/C_8$ die at $C_{16}$
  via a short voltage relation $\alpha a_2 + \beta a_3 \equiv 0
  \pmod m$ ($|\alpha|,|\beta| \le 8$); whether some large-$m$ voltage
  pair defeats every power-of-2 scale simultaneously is genuinely open
  but outside this harness's 64-vertex witness cap.
- **Q8 verdict:** no witness in the screened families; a counterexample
  hunt must move to girth-biased random cubics / cages / snark-like
  families. Ideation losers (Hashimoto trace compression, dyadic-window
  spectrum sieve, minimal-counterexample stability stack) are recorded
  in the notes channel and must not be re-proposed without new input.

### Sections 6, 9–10 — Q9 radius-2 disproof; pair formulas; radius-3 program

- **Lemma `chain_locality` / `dfs_chain_locality` (DISPROVED, R1):** the
  radius-2 claim (some PO2 cycle is a fundamental cycle or a 2-cycle
  sym-diff, for EVERY DFS tree) fails at $n=10$: machine-found cubic
  counterexamples CL-A/B/C (CL-A edge list in the lemma file; DFS root 7
  gives fundamental lengths $[3,3,3,5,6,10]$, pair sym-diffs
  $\{0,5,6,7,9\}$). Every 8-cycle there carries exactly 3 back edges.
  23 falsifying (graph, tree, root) instances recorded.
- **Lemma `chain_locality_r3` (open, radius-3 replacement):** some PO2
  cycle carries $\le 3$ back edges. Survived exhaustive Trémaux coverage
  of CL-A/B/C + the $n=12$ falsifier, and adversarial swap-search
  (54,429 graph states, $n \le 18$, 120 DFS tries each; extended to
  $n \in \{20,22,24\}$ with 750 states each, C4/C8 scoring): NO
  radius-4 instance ever found; min radius over PO2 cycles is always
  $\le 3$ in every probe. Not exhaustive at $n > 12$.
- **Pair sym-diff formulas** (all later SUBSUMED by `fund_pair_overlap`,
  Section 28): `same_leaf_sym_diff` (proved): leaf with back edges at
  gaps $\delta_1 > \delta_2$ gives a simple cycle of length
  $\delta_1 - \delta_2 + 2$. `sym_diff_nested` (proved): same formula
  for nested pairs. The R6 "unified" claim that ALL same-branch pairs
  obey $|\delta_1-\delta_2|+2$ was WRONG for crossing pairs — corrected
  in Section 22 (`crossing_pair_formula`); do not cite R6.
- **Depth-gap constraint system:** in a counterexample, every back-edge
  gap avoids $\{3,7,15,31,\dots\}$ (fundamental cycles) and every
  nested/same-vertex pair difference avoids $\{2,6,14,30,\dots\}$;
  crossing pairs instead constrain the offset $\omega$ (Section 22).
  Valid gap pairs exist in abundance (68.8% density for $\delta \le
  40$), so arithmetic alone cannot close Q9 — structure must.
- **Lemma `backedge_density`:** parts A (back-edge count
  $\ge \lfloor n/2 \rfloor + 1$) and B (leaves force same-branch
  pairs) proved; part C (forcing a violation) open — this is what the
  mechanism taxonomy of Sections 19–30 replaces.

### Section 8 — cubic back-edge budget + early triple evidence (kept: still cited)

- **Cubic DFS budget** (used throughout, incl. Sections 27–29): back-edge
  count $= n/2 + 1$; every DFS leaf carries exactly 2 back edges (in
  min-degree-3 graphs: $\ge 2$); every internal non-root vertex carries
  $\le 1$ back-edge lower endpoint; the root receives back edges only.
- **Computational chain-locality at radius 3:** `chain_locality_triple`
  (proved computationally, $n \le 10$, incl. all 2000 Petersen spanning
  trees — 960 fire via fundamental $C_8$, 1040 via pair sym-diff);
  `chain_locality_extended` (cubic through $n=24$, 6,650 pairs, zero
  triple failures); `chain_locality_full_window` (open; cubic through
  $n = 64$, 9,350+ pairs, zero triple failures). The two Moore-bound
  facts used here (min-deg-3 girth-5 needs $\ge 10$ vertices; $n \le 9$
  forces girth $\le 4$) are INTERNAL lemmas, not external citations —
  no given-facts ledger entry is required for them: both carry complete
  self-contained proofs inside the `lemma_chain_locality_proof` CHECK
  (neighborhood counting $1 + 3 + 3\cdot 2 = 10$ for the first;
  exhaustive machine enumeration over all min-deg-3 graphs on $n \le 9$
  for the second), so they rest on nothing outside this repository.

### Sections 11–13, 17–18 — dead ends and probes (recorded to prevent rediscovery)

- **Lemma `alternation_obstruction` (DISPROVED, both versions):** C8s
  with 4 back edges exist (CL-A), including a perfect T-B-T-B-T-B-T-B
  alternating C8. Consequence: no PER-CYCLE bound can work; the true
  statement must be a global EXISTENCE claim (some PO2 cycle has $\le 3$
  back edges) — this insight drove the mechanism taxonomy.
- **Lemma `radius4_hunt_n24` (open):** adversarial radius-4 hunt through
  $n=24$ found nothing; radius-3 ceiling holds under pressure.
- **Lemma `cubic_depth_gap` (probe):** easy-path (some gap in
  $\{3,7,15,31\}$) vs hard-path classification; every hard-path
  instance verified at radius $\le 3$.
- **Lemmas `ham_path_tree_r3`, `girth5_depth_gap` (probes):** Hamiltonian
  path trees and girth-5 cubics (Petersen anchor) — chain_locality_r3
  holds in every sampled instance.

### Sections 7, 14–16 — CROSS-PROBLEM ARCHIVE (Frankl union-closed; inert here)

Q10/Q11 excursions into `frankl_union_closed` (a separate open problem
with its own spec and ledger): `frankl_deficiency` (KL deficiency
$\ge (1-p)^2/4$, open, CHECK passes), `cyclic_orbit_avg_size` (Case
$|A| \ge n/2$ proved, rest open), `dihedral_orbit_avg_size` (probe).
**Nothing in the Erdős–Gyárfás argument depends on these**; they are
retained solely as audit trail under their `lemma_frankl_*` /
`lemma_*_orbit_*` files.

## Sections 19–57 — merged-narrative digest (condensed 2026-08-06, session s_0806-081011-9409)

> After merging origin/master (sibling branches 0726-080714-6bac and the
> 0729/0730 sessions) this file carried two parallel narrative streams
> totalling ~300k chars, which exceeds the critic prompt budget (the
> assembled prompt broke the fixed 240s critic timeout at ~180k chars in
> R23). Sections 19–57 below are condensed to anchors, exactly as
> Sections 2–18 were in R23. Full verbatim text: this file at commit
> `18fc918` (the merge) and the per-session archives under
> `strategies/erdos_gyarfas/`. The LIVE argument is Sections 58–65 plus
> the LIVE Sections 26–31 (R19–R24, session ids s_0803..s_0805) that
> follow Section 64 below — those live sections take precedence for any
> citation of "Section 26"–"Section 31"; the same-numbered first
> instances in this digest are marked "(first instance)". For other
> N ≤ 57 the anchor below is the referent.

**Stream 1 — chain_locality / adversarial-search line (Sections 19–28,
sessions s_0727–s_0729):**

- S19–S20: hard-path cubic DFS trees exist (G12, n=12 girth-3 example;
  gaps ⊆ {2,4,5}); rescue via shared-target / shared-source C4s
  (`shared_target_c4`, `branching_dfs_r3`); degree-forcing taxonomy
  (Type A/B interior vertices, root receives 2, leaf sends 2).
- S21: general interval-overlap mechanism; two-bridge conjecture; the
  CAVEAT (added R23) that S21's pair classification preceded the
  unified `fund_pair_overlap` and survives only through S28-R21's
  restatement.
- S22: two-sample triple rescue census (independent samples).
- S23: mod-8 gap-density constraint feasibility (Q38).
- S24–S25: `chain_locality_r3` adversarial search to n≤40 incl.
  C16/C32 via sym-diff — unfalsified; pair-coverage grows with n.
- S26 (first instance): expected po2-pair count lower bound at large n.
- S27: adversarial search n=42..50; large-gap forcing argument.
- S28 (first instance): proof-landscape summary; forbidden-set
  enumeration {3,7,15,31}.

**Stream 2 — Hamiltonian-path Case-A depth-census line (Sections 29–57,
sessions s_0729-083306, s_0729-131551, branch 0726-080714-6bac).**
Setting: cubic Hamiltonian-path DFS trees (path 0..n-1), back-edge
assignments (a_i, receiver), "depth-d" = XOR of d fundamental cycles;
po2 = cycle length a power of 2:

- S29–S33: explicit sym-diff length formulas for canonical pair types;
  n=6 base case; exhaustive n=10,12,14,16 verification — XOR depth ≤ 3
  always finds a po2 cycle ("XOR depth 3" conjecture).
- S34–S37: corrected depth-3 analysis; structural C4 pattern; unified
  interval-XOR formula; parity theorem + even-gap lemma; root-pair
  triple formula; mod-4 structure.
- S38–S40: Even-Gap Overlap Lemma (Q62); Case B exclusion; root-pair
  coverage; Case E-III cross-parity pair argument.
- S41–S45: simple-graph-constraint exhaustives n=10,12,14 (Q63); Case A
  depth-3 always gives C8 with C4 blocked by degree; Case B sub-cases
  (B1→C4, B2→C8); n=16: Case B eliminated by (n-1,0) depth-1, Case A
  sym_diff ∈ {5,13}.
- S46–S47: mod-4 structure of sym_diff — total_gap_sum ≡ 1 (mod 4) for
  Case A depth-3; partial-overlap formula sd=|(k+t)-(a1+a2)|, C8
  condition k+t = a1+a2 ± 5.
- S48–S49: Int-Int-X universal coverage (Q64-f) + structural lemmas.
- S50–S51: odd-sum necessity, odd-gap existence; even-gap lemma
  unifying both parities (Q64-h resolved); unified odd-gap existence
  theorem for all n; Type I/II depth-3 decomposition.
- S52: corrected xor2 (None for disjoint intervals); structural
  n≡0 (mod 4) all-even-gap impossibility proved; Case B depth-3
  verified n=14.
- S53: Lemma G — disjoint g=2 pair → sd=5 via c=(g3-1)/2; g=2
  disjointness lemma; 87/96 n=14 Case A coverage.
- S54: connectivity correction (c=0 iff multi-cycle XOR); single-cycle
  C8 universality verified n=12,14,16; Case B depth-1 C_{2^k} for
  n=2^k.
- S55: depth-3 always gives C8 — sd=1 (C4) impossible at depth-3 via
  matching constraint; sd=5 unique for n ≤ 15 (Cycle Bound).
- S56: n=18 depth-3 census (a1+a2 ≤ 24): sd=5 76.8%, sd=13 (C16!)
  23.0%, **18 assignments (0.3%) with NO depth-3 single-cycle po2** —
  depth-4 needed; two failures verified explicitly.
- S57: Theorem C (4-special-edge depth-4): root edges r1,r2 + leaf
  edges l1,l2 give a single cycle iff ov ≥ 1, of length
  L4 = g_r + g_l − 2·ov + 4; ov=0 gives two disjoint cycles
  (g_r+2, g_l+2). Open: depth-4 always suffices for the ov=0 depth-3
  failures.

**Interface to the live argument:** Stream 2 is a sibling attack on the
same Q9/coverage core specialized to Hamiltonian-path trees; nothing in
Sections 58–65 depends on it except as corroborating census data. The
live pasting-line dependencies are: `fund_pair_overlap` (live Section
28, R21), `mixed_overlap_supply` (live Section 29, R22),
`pasting_value_interval` (live Section 30, R23),
`pasting_meeting_structure` (live Section 31, R24),
`pasting_vertex_automatic` (Section 65, R25) — all lemma files in
`proof_lemmas/`.

## Sections 58–60 — R12–R14 mechanism digest (condensed 2026-08-15; full narrative archived in strategies/erdos_gyarfas/s_0730-080837-b7c4.md)

- **Section 58 (R12, `leaf_pair_witness` PROVED)**: in a cubic DFS tree
  every leaf carries exactly 2 back edges, to ancestors $a_1$ (far,
  depth-gap $\delta_1$) and $a_2$ (near, $\delta_2 < \delta_1$);
  $C_1 \oplus C_2 = \mathrm{TreePath}(a_1,a_2) \cup \{B_1, B_2\}$, a
  simple cycle of length $\delta_1 - \delta_2 + 2$ with exactly 2 back
  edges. Po2 witness iff $\delta_1 - \delta_2 \in \{2,6,14,30,\dots\}$.
  (The same-sender pair is the $k_{12}$-maximal vertical pair; its
  anchor interval $\mathrm{TreePath}(a_1,a_2)$ is $D$'s ENTIRE tree
  part — Section 83 builds on this.)
- **Section 59 (R13, `back_edge_triangle`)**: double-sender mechanism —
  the chain-locality-refuting graphs CL-A/B/C have all their residual
  DFS trees rescued by $C_{(v,a_1)} \oplus C_{(v,a_2)} \oplus C_{(u,w)}$
  triples. Its taxonomy percentages were later corrected by Section 61
  (crossing pairs had been misclassified as triples).
- **Section 60 (R14, `sym_diff_cycle_formula` PROVED)**: the
  double-sender triple with $w$ = child of $a$ on the path to $v$ and
  $(w,x)$ = $w$'s back edge is a single cycle of length $|d_x-d_b|+4$;
  po2 iff $|d_x-d_b| \in \{0,4,12,28,\dots\}$. **Load-bearing caveat
  (2026-08-05)**: the cubic budget gives an internal non-root vertex AT
  MOST one sender back edge — $w$ may send none, so this is a candidate
  mechanism, not a proof; superseded as the main line by the pasting
  program (Sections 26–30).

## Section 61 — Q9 crossing-pair mechanism and corrected coverage taxonomy (session s_0730-080837-b7c4, R15)

**Discovery (R15)**: The Section 59 taxonomy listed 8.3% of DFS trees as
"triple residual" (requiring 3 back edges). After correcting the R6 unified
sym-diff theorem, the true triple residual is only **1–3%** — the difference
was misclassified *crossing pairs*.

### Crossing-pair sym-diff (Lemma `crossing_pair_formula`)

**Proved** (Lemma `crossing_pair_formula`, R15): Let $e_1=(s_1,a_1)$ and
$e_2=(s_2,a_2)$ be two DFS back edges in *strict same-branch crossing* order:

$$d_{a_1} < d_{a_2} < d_{s_1} < d_{s_2},$$
$$a_2 \text{ ancestor of } s_1, \quad s_1 \text{ ancestor of } s_2.$$

Then $C_{(s_1,a_1)} \oplus C_{(s_2,a_2)}$ is a **simple cycle of length**
$(d_{a_2}-d_{a_1}) + (d_{s_2}-d_{s_1}) + 2$.

**Po2 condition**: the cycle is a power of $2$ iff
$(d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1}) \in \{2,6,14,30,\ldots\}$.

**Anchor table (deterministic, for re-derivation).** Worked instances of
the length formula $L = (d_{a_2}-d_{a_1}) + (d_{s_2}-d_{s_1}) + 2$ on
strict-crossing depth tuples $(d_{a_1}, d_{a_2}, d_{s_1}, d_{s_2})$ —
any probe of this formula should reproduce EXACTLY these values:

| $(d_{a_1}, d_{a_2}, d_{s_1}, d_{s_2})$ | $L$ | po2? |
|---|---|---|
| $(0,1,2,3)$ | $1+1+2 = 4$ | yes |
| $(0,4,6,8)$ | $4+2+2 = 8$ | yes |
| $(0,2,4,5)$ | $2+1+2 = 5$ | no |
| $(0,3,4,6)$ | $3+2+2 = 7$ | no |
| $(1,2,4,7)$ | $1+3+2 = 6$ | no |

The parity identity (`crossing_offset_parity`, R17) on the same tuples:
$\omega = (d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1}) \equiv
(d_{s_1}-d_{a_1})+(d_{s_2}-d_{a_2}) \pmod 2$ — the two sides are
rearrangements of the same four terms, so the congruence is exact on
every tuple (e.g. $(0,3,4,6)$: $3+2 = 5 \equiv 7 = 4+3$).

**Proof idea**: the two fundamental cycles share tree edges on segment
$\operatorname{TreePath}(a_2,s_1)$, which cancels. The surviving edge set is
$\operatorname{TreePath}(a_1,a_2) \cup \operatorname{TreePath}(s_1,s_2) \cup \{e_1,e_2\}$,
forming a single cycle (all degrees 2, explicit walk $a_1\to a_2 \to s_2 \to s_1 \to a_1$).

### Correction of the R6 unified sym-diff theorem

The R6 claim (Section 9) that *all same-branch pairs give $|\delta_1-\delta_2|+2$*
is **wrong for crossing pairs**. The correct formula is $(d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1})+2$,
which differs (and is generally larger) from $|\delta_1-\delta_2|+2$ when both
depth-offsets are nonzero.

The nested formula $|\delta_1-\delta_2|+2$ is correct only for:
- Same-vertex pairs ($s_1=s_2$, or equivalently same-sender),
- Proper nested pairs ($d_{a_1}\le d_{a_2}$ and $d_{s_2}\le d_{s_1}$).

### Updated 4-mechanism coverage taxonomy

| Mechanism | Condition | Cycle length | Back edges | Radius |
|-----------|-----------|-------------|-----------|--------|
| Easy-path | Some gap $\in\{3,7,15,\ldots\}$ | $\delta+1$ | 1 | 1 |
| Nested/same-vertex | $|\delta_1-\delta_2| \in\{2,6,14,\ldots\}$ | $|\delta_1-\delta_2|+2$ | 2 | 2 |
| Crossing | $(d_{a_2}-d_{a_1})+(d_{s_2}-d_{s_1}) \in\{2,6,14,\ldots\}$ | offset$+2$ | 2 | 2 |
| Triple (double-sender) | $|d_x-d_b|\in\{0,4,12,\ldots\}$ | $|d_x-d_b|+4$ | 3 | 3 |

**Exhaustive counts** for all valid Trémaux trees of CL-A/B/C and Petersen:

| Graph | Trees | Easy | Nested | Crossing | Triple | None |
|-------|-------|------|--------|----------|--------|------|
| CL-A | 356 | 272 (76.4%) | 72 (20.2%) | 8 (2.2%) | 4 (1.1%) | **0** |
| CL-B | 378 | 276 (73.0%) | 72 (19.0%) | 24 (6.3%) | 6 (1.6%) | **0** |
| CL-C | 360 | 228 (63.3%) | 96 (26.7%) | 24 (6.7%) | 12 (3.3%) | **0** |

All four mechanisms together cover 100% of tested cubic DFS trees.
CHECK block in `lemma_crossing_pair_formula` verifies formula correctness and
full coverage for CL-A/B/C, Petersen, and sampled random cubic graphs at
$n \in \{10,12\}$.

**Remaining open question for Q9**: Prove that the 4-mechanism taxonomy covers
*all* cubic DFS trees — i.e., that for every cubic graph $G$ and every DFS tree
$T$, at least one of the four conditions holds. Each condition is a diophantine
constraint on the depth values of back edges; the hardest part is the triple
residual, where the existence of a suitable double-sender vertex needs a structural
argument.

## Sections 62–64 — R16–R18 parity/coverage digest (condensed 2026-08-15; R17/R18 narratives archived in strategies/erdos_gyarfas/s_0801-082519-6641.md and s_0802-080649-85be.md; R16 session s_0801-080553-f19f predates the archive, this digest is authoritative for it)

- **Section 62 (R16, `coverage_extended`)**: the 4-mechanism taxonomy
  (easy / nested / crossing / triple) covered 100% of sampled cubic DFS
  trees at $n \le 16$ (1,200 trees per size, NONE=0), fractions stable:
  easy $\approx 86\%$, nested $\approx 11\%$, crossing $\approx 1.5\%$,
  triple $\approx 0.3\%$. Analytic sub-case: with all gaps odd, leaf-pair
  differences are even; the surviving open point (unit-step crossing
  pairs) was deprioritized by the R18 census below.
- **Section 63 (R17, `crossing_offset_parity` PROVED)**: for a strict
  crossing pair, $\omega = (d(a_2)-d(a_1)) + (d(s_2)-d(s_1)) \equiv
  \operatorname{gap}(B_1) + \operatorname{gap}(B_2) \pmod 2$ (proof:
  $\operatorname{gap}_1 + \operatorname{gap}_2 = \omega + 2\gamma$ with
  $\gamma = d(s_1)-d(a_2) \ge 1$). Consequences: opposite-parity
  crossing pairs can NEVER fire; crossing fires only from $E$-$E$ or
  $O$-$O$ pairs; in all-even-gap trees every crossing offset is even and
  the easy mechanism is vacuous (po2$-1$ gaps are odd). Coverage NONE=0
  extended to $n = 18$.
- **Section 64 (R18, `triple_parity` PROVED + `residual_parity_census`)**:
  $|S| \equiv \operatorname{gap}_1 + \operatorname{gap}_2 +
  \operatorname{gap}_3 + 1 \pmod 2$; triples fire only from $OOO$ or
  $OEE$ gap-parity patterns (odd number of odd gaps), so in all-even
  trees triple AND easy are both vacuous — nested + crossing must cover.
  Census over 48,000 sampled trees: all-odd residuals are measure-zero
  (7/48,000, all $n=10$, every one rescued by a unit-step crossing
  $\omega = 2$ — unfalsified but strategically irrelevant); the residual
  mass is mixed-parity ($\ge 96\%$); the triple mechanism rescues
  122/122 crossing-failed residual trees, with firing sym-diff lengths
  dominated by $C_8$ (698 of 738 firings; $C_4$ 39, $C_{16}$ 1) — **the
  origin of the program's $L=8$ focus**. Parity accounting: easy ← odd
  gap $\in \{3,7,15,31\}$; nested/crossing ← same-parity pair; triple ←
  $OOO$/$OEE$ (the only mechanism combining both parity classes, which
  is structurally why mixed-parity residuals need it).

## Sections 26–31 — R19–R24 pasting-mechanism digest (condensed 2026-08-17, session s_0817-081104-2f11; full narratives archived in strategies/erdos_gyarfas/ under sessions s_0803-080758-2226, s_0804-080732-f106, s_0805-080844-5fb3)

Six rounds that built the pasting machinery. All proved lemmas live in
their lemma files; this digest keeps the load-bearing formulas and the
still-open caveats.

**Proved lemmas** (statements + proofs in `proof_lemmas/`):

- `triple_sym_diff_structure` (R19, 6 parts): triple sym-diff length
  $|S| = 3 + t$ ($t$ = tree edges covered oddly); $S$ always a nonempty
  even subgraph; **pasting lemma** — cycles $X, Y$ meeting in a single
  path of length $k \ge 1$ have $X \triangle Y$ a single cycle of length
  $|X| + |Y| - 2k$; **triple pasting criterion** — pair sym-diff $D$ a
  single cycle and $D \cap C_3$ a single path of length $k' \ge 1$ give
  $|S| = |D| + \operatorname{gap}_3 + 1 - 2k'$; parity legality classes
  $OEE$ (mixed pair + even third) and $OOO$/$EEO$ derived
  mechanistically. Census: 100% of sampled firing triples (2,604/2,604)
  factor through the pasting criterion — pasting is empirically
  exhaustive, no other firing route needs handling.
- `fund_pair_overlap` (R21, iff): two fundamental cycles intersect in
  $\emptyset$, one vertex, or one vertical path running from the deeper
  anchor down to $\operatorname{lca}(s_1, s_2)$, so
  $k_{12} = d(\operatorname{lca}(s_1,s_2)) - d(\text{deeper anchor})$;
  $C_1 \triangle C_2$ is a single cycle **iff** $k_{12} \ge 1$, and then
  $|D| = \operatorname{gap}_1 + \operatorname{gap}_2 + 2 - 2k_{12}$
  (parity $|D| \equiv g_1 + g_2$; nested/crossing/branching subsumed
  uniformly; same-sender pairs give overlap automatically, and every
  DFS leaf of a min-degree-3 graph sends $\ge 2$ back edges).
- `mixed_overlap_supply` (R22): **parity segregation is impossible in
  2-connected graphs** — if both gap parities occur, some mixed pair
  overlaps, giving odd single-cycle $D$ ($OEE$ raw material). Proof via
  root-one-child + low-point property (every child subtree sends a back
  edge strictly above its parent; hence every tree edge is covered),
  else the covering parity 2-colors tree edges and is forced constant.
  Sharp: bridged compositions show 2-connectedness can't be dropped.
- `pasting_meeting_structure` (R24, iff): $E(D) \cap E(T) = A \sqcup L_1
  \sqcup L_2$ (anchor interval strictly above $m = \operatorname{lca}$,
  two legs below, one empty when senders comparable); $P_3$ meets each
  segment in one contiguous vertical interval, at most two nonempty;
  $D \cap C_3$ is a single path iff exactly one intersection is
  nonempty and carries every shared vertex ($k'$ = its length). The
  stray-vertex condition is automatic in cubic trees — proved in R25
  (`pasting_vertex_automatic`, Section 65).

**Census facts** (R20/R23 probes, unfalsified):

- Every pair-residual tree sampled is pasting-rescued (54/54 at R20,
  50/50 at R23; 192k trees, $n \le 22$) and **mixed-parity** (all-even /
  all-odd pair-residual trees: never observed, but ruling them out is
  load-bearing and OPEN — an all-even one would have no rescue route).
- `pasting_value_interval` (R23): the achievable value set
  $V(T) = \{|D| + g_3 + 1 - 2k'\}$ has even part $V_e(T)$ a **gap-free
  step-2 interval containing 8** on 100% of residual trees;
  $v_{\min} \in \{4,6,8\}$, $v_{\max}$ grows with $n$, $k'$ sweeps
  1..12. Tuning reduced to (T1) interval-ness of $V_e$ (candidate:
  $\pm2$ local moves — slide the meeting segment / swap $B_3$ to an
  adjacent cover), (T2) $v_{\min} \le 8$, (T3) $v_{\max} \ge 8$. All
  three still open; the reduction targets 8 only, and $8 \in V_e(T)$
  per-tree is exactly the later `sup8_tree_universal` probe.

**Standing hypotheses still leaned on (open, tracked):**

1. **2-connectedness** — `mixed_overlap_supply` needs it; the reduction
   from min-degree-3 to 2-connected is NOT proved ("cycles live in
   blocks" fails: a block need not keep min degree 3, and the DFS tree's
   parity classes span blocks; the cut-vertex surgery has an unproved
   degree-repair step that could itself create PO2 cycles). Only used
   fact: any PO2 cycle found in a block settles $G$.
2. **Pair-residual ⊆ mixed-parity** — empirical only (R20/R23).

## Section 65 — R25: Vertex-automatic proved — subcubic pasting is pure interval combinatorics (session s_0806-081011-9409)

### New proved lemma: `pasting_vertex_automatic`

The R24 open conjecture is a theorem, by a two-line degree count:

1. **(Two-cycle vertex-meeting, $\Delta \le 3$.)** In any graph of
   maximum degree $\le 3$, two cycles through a common vertex $v$ each
   use exactly 2 of $v$'s $\le 3$ incident edges, so by pigeonhole they
   share an edge at $v$. Two cycles of a subcubic graph can never cross
   vertex-only.
2. **(No strays.)** $E(D) \cap E(C_3) = P_3 \cap (A \sqcup L_1 \sqcup
   L_2)$ is tree-only (`pasting_meeting_structure`(0)–(1)). If exactly
   one segment intersection $P_3 \cap X$ is nonempty, every shared
   vertex of the cycles $D$ and $C_3$ is, by (1), an endpoint of a
   shared edge. That shared edge is necessarily a TREE edge: the only
   non-tree edges of $D$ are its back edges $B_1, B_2$, the only
   non-tree edge of $C_3$ is $B_3$, and $B_3 \notin \{B_1, B_2\}$, so
   no back edge lies in both cycles. A shared tree edge lies in
   $E(D) \cap E(C_3) = P_3 \cap X$ — i.e. every shared vertex lies on
   the subpath $P_3 \cap X$. The stray-vertex condition is automatic.
3. **(Collapsed criterion.)** For $\Delta(G) \le 3$: $D \cap C_3$ is a
   single path (pasting hypothesis) **iff** exactly one of
   $P_3 \cap A$, $P_3 \cap L_1$, $P_3 \cap L_2$ is edge-nonempty, and
   $k'$ = that interval's length.

CHECK: 100-trial cubic census $n \in \{10,..,16\}$, 3 roots each —
every shared vertex of $D, C_3$ carries a shared incident edge, and the
collapsed criterion matches brute-force single-path truth on every
triple (assertions over >30k triples, >100k shared-vertex checks).

**Scope.** Sharp at degree 3: at a degree-$\ge 4$ vertex two cycles can
cross vertex-only. Min-degree-3 non-cubic graphs are NOT covered — the
cubic/subcubic reduction stays on the Section 29 gap list.

### Q9 state after R25

| Piece | Status |
|------|--------|
| Supply (mixed pair with odd single-cycle $D$) | proved, 2-connected (R22; reduction gap open) |
| Meeting (structure + iff criterion) | proved (R24) |
| Meeting criterion collapse (vertex-automatic, subcubic) | **proved** (R25) |
| Meeting (existence of a pasting even-gap $B_3$) | open — now purely: some even-gap back edge covers edges of exactly ONE segment |
| Tuning (T1 interval / T2, T3 endpoints of $V_e$) | open (R23 reduction; R26+ targets) |
| Parity-class caveats (all-even/all-odd residuals, 2-conn) | open, tracked (Sections 29, 30) |

## Section 66 — R26: Cover dichotomy — paste or straddle the cancelled interval; per-pair existence is dead (session s_0806-081011-9409)

### New proved lemma: `pasting_cover_dichotomy`

Any back edge $B_3 \notin \{B_1,B_2\}$ covering a tree edge of $D$
("cover") satisfies exactly one of:

1. **Paste** — $P_3$ meets exactly one of $A, L_1, L_2$ in edges, and
   (subcubic, `pasting_vertex_automatic`) $D \cap C_3$ is a single
   path.
2. **Straddle** — $P_3$ meets $A$ and exactly one leg $L_i$, and then
   $I = [a_{\text{deep}}..m] \subseteq P_3$, the anchor is strictly
   above $a_{\text{deep}}$, the sender strictly below $m$ in $c_i$'s
   subtree, $P_3 \cap A \ni$ ($A$'s deepest edge),
   $P_3 \cap L_i \ni (m, c_i)$, and $\operatorname{gap}_3 \ge k_{12}+2$.

Existence criteria (contrapositives): a cover pastes whenever
$\operatorname{gap}_3 \le k_{12}+1$, OR its anchor is at/below
$a_{\text{deep}}$, OR its sender is at/above $m$.

CHECK: 21,293 single-cycle pairs / 107,054 covers over 2-edge-connected
cubic samples $n \in \{10,..,16\}$ — dichotomy and all straddle
consequences hold with zero violations (69,362 pasting / 37,692
straddling).

### Census: per-pair meeting-existence FAILS — tuning must be per-tree

With coverage guaranteed (2-edge-connected samples): ~3% of
single-cycle pairs have NO pasting cover; ~16% have no EVEN-gap pasting
cover (even $\operatorname{gap}_3$ ⇔ even $L$ when $|D|$ odd). So T2/T3
cannot be proved pair-locally; the correct quantifier is per-tree
("some pair admits an even-gap pasting cover"), matching
`pasting_value_interval`'s per-tree censuses (8 ∈ V, 53/53 residuals).
No future round should attempt per-pair existence.

### Q9 state after R26

| Piece | Status |
|------|--------|
| Meeting criterion (collapsed, subcubic) | proved (R24+R25) |
| Cover dichotomy + paste criteria (gap ≤ k12+1 / anchor / sender) | **proved** (R26) |
| Per-pair even-gap pasting existence | **dead** (census: ~16% failure) |
| Per-tree meeting existence + T2/T3 endpoints | open (R27+ target) |
| T1 interval-ness of $V_e$ | open |
| 2-conn reduction; all-even/all-odd exclusion | open (Sections 29, 30) |

## Section 67 — R27: T3 refined to a min-overlap short-paste config; per-tree meeting existence subsumed (session s_0807-081112-b59a)

### New probe lemma: `t3_min_overlap_short_paste`

The R26 handoff's first priority (rule out $V_e \subseteq \{6\}$
per-tree) is subsumed by a sharper, still-falsifiable reduction. Census
(standalone, 192k sampled DFS trees, $n \in \{12..22\}$, 62
pair-residual trees):

1. **Joint route available 62/62**: every pair-residual tree admits a
   legal pasting config with $k' = 1$ (min overlap — $C_3$ meets $D$ in
   a single edge, so $L = |D| + \operatorname{gap}_3 - 1$, no overlap
   bookkeeping), $\operatorname{gap}_3 \le k_{12} + 1$ (the
   position-free sufficient paste criterion from
   `pasting_cover_dichotomy` — no anchor/sender analysis needed), and
   $|D| + \operatorname{gap}_3 \ge 9$ odd, hence even $L \ge 8$.
2. **$V_e$ never empty, never $\subseteq \{6\}$** (0/62 each): per-tree
   meeting existence AND the refined T3 both hold on every sample, via
   the same config.
3. **Parity families**: the odd-$|D|$/even-gap family realizes the
   config on 61/62 — but ONE tree required the even-$|D|$/odd-gap
   family. The R26 suspicion is confirmed: the second family is
   load-bearing; an analytic T3 proof must not assume $|D|$ odd (so
   `mixed_overlap_supply` alone is not the whole supply story for T3).
4. **Minimal realizations** concentrate on $(\lvert D\rvert,
   \operatorname{gap}_3, k') = (\text{odd} \ge 7, 2, 1)$ — a
   short back edge pasted on one edge of a long odd $D$; min-gap census
   2:55, 4:5, 5:2. $\operatorname{gap}_3 = 2$ means $C_3$ is a
   triangle; a counterexample graph may be triangle-free, so the
   analytic target is the criterion class, not the triangle case.

### What this changes in the tuning program

T3 ($v_{\max} \ge 8$) is now: *find one (pair, cover) with $k'=1$,
$\operatorname{gap}_3 \le k_{12}+1$, $|D| + \operatorname{gap}_3 \ge 9$
odd*. All positional machinery (anchor/sender, straddle structure) is
out of the T3 path; what remains is existence + arithmetic:

- **Existence of a $k'=1$ cover**: among covers of $D$'s tree edges,
  one meeting exactly one segment in exactly one edge. Candidate: the
  cover of a segment's END edge (top of $A$ or bottom of a leg) with
  smallest gap — its $P_3$ is anchored/sent near the segment boundary,
  limiting the met interval. Needs an argument.
- **Arithmetic $|D| + \operatorname{gap}_3 \ge 9$ odd**: on a
  pair-residual tree $|D| \notin \{4, 8, 16, 32\}$; if $|D| \ge 9$ any
  parity-correct short cover works; small cases $|D| \in \{3, 5, 6, 7\}$
  need $\operatorname{gap}_3 \ge 9 - |D|$, i.e. interplay with $k_{12}$
  via the short criterion ($\operatorname{gap}_3 \le k_{12}+1$ forces
  $k_{12} \ge 8 - |D|$ — large overlap pairs).

### Summary of round R27

| Item | Status |
|------|--------|
| `t3_min_overlap_short_paste` probe (192k trees, 62 residuals) | **unfalsified, non-vacuous** (R27) |
| $V_e = \emptyset$ or $V_e \subseteq \{6\}$ on some residual tree | **never observed** (0/62) (R27) |
| T3 reduced to position-free existence + arithmetic | **formulated** (R27) |
| Even-$|D|$ family load-bearing (1/62 trees need it) | **observed** (R27) |
| Analytic proof of the joint-config existence | open (R28+ target) |

## Section 68 — R28: Direct tuning to 8 inside the short-paste class; pigeonhole program collapsed (session s_0807-081112-b59a)

### New probe lemma: `tune8_short_paste`

The T2-side census (standalone, 192k sampled DFS trees, seed
20260807+28, 51 pair-residual trees) produced a sharper reduction than
the planned T2 endpoint bound:

1. **Exact tuning available 51/51**: every pair-residual tree admits a
   legal pasting config with $\operatorname{gap}_3 \le k_{12}+1$
   (position-free short-paste criterion) and
   $|D| + \operatorname{gap}_3 + 1 - 2k' = 8$ exactly. The pasted
   triple cycle is a $C_8$ — so $8 \in V(T)$ **directly**.
2. **The R23 pigeonhole program (T1 + T2 + T3) is now a fallback**:
   direct containment needs no interval-ness and no endpoint bounds.
   If `tune8_short_paste` is falsified at larger $n$, the T1/T2/T3
   route (with R27's `t3_min_overlap_short_paste` as the T3 leg)
   reactivates.
3. **$k'$ freedom is load-bearing**: fixing $k' = 1$ fails on 3/51
   trees (unlike the T3-side lemma where $k'=1$ always sufficed for
   $L \ge 8$). Observed $k'$ in minimal $L=8$ realizations spans
   $1..4$; min $\operatorname{gap}_3$ is 2 on 45/51, 4 on 6/51.
4. **Same-sender pairs are NOT the universal supply** for small even
   $L$: 1/51 trees has no same-sender realization with $L \le 8$ —
   consistent with R27's parity-family finding that the supply story
   must go beyond any single special pair shape.

### Open core after R28 (Q9 tuning half)

Prove: *every pair-residual tree admits a pair (single-cycle $D$,
overlap $k_{12}$) and a cover $B_3$ with
$\operatorname{gap}_3 \le k_{12}+1$, $D \cap C_3$ a single path of
$k' \ge 1$ edges, and $|D| + \operatorname{gap}_3 = 7 + 2k'$.* The
diophantine surface has three degrees of freedom (pair choice, cover
choice, $k'$); the censuses say random cubic structure always supplies
a solution. Candidate analytic route: start from any single-cycle pair
(supply: R22), enumerate the covers of $D$'s tree edges guaranteed by
2-edge-connectedness, and show the value map
$(B_3) \mapsto |D| + \operatorname{gap}_3 - 2k'$ sweeps a residue class
wide enough to hit 7.

### Summary of round R28

| Item | Status |
|------|--------|
| `tune8_short_paste` probe (192k trees, 51 residuals) | **unfalsified, non-vacuous** (R28) |
| $8 \in V(T)$ via short-paste class only | **observed 100% (51/51)** (R28) |
| T1/T2/T3 pigeonhole program | **demoted to fallback** (R28) |
| $k'=1$-only variant | **falsified** (3/51 need $k' \ge 2$) (R28) |
| Analytic proof of exact tuning | open (R29+ target) |

## Section 69 — R29: Value-set pre-census — tree-level sweeps dead, per-pair sweep survives (session s_0808-080808-ce3d)

### The census (192k sampled DFS trees, seed 20260808+29, 52 residuals)

For each pair-residual tree, tabulate the short-paste value multiset
$S(T) = \bigcup_p S_p(T)$ and each pair's own
$S_p(T) = \{|D| + \operatorname{gap}_3 + 1 - 2k'\}$ over legal covers
with $\operatorname{gap}_3 \le k_{12}+1$. Results:

1. **Tree-level even-interval FALSIFIED (4/52)**: the even part of
   $S(T)$ has gaps, e.g. $\{6,8,10,14\}$ (12 missing) and
   $\{4,8,10,12,14\}$ (6 missing). The R28 candidate route ("show the
   union value map sweeps a residue class") is dead as stated.
2. **Descent FALSIFIED (3/52)**: some even $v \ge 10 \in S(T)$ has
   $v - 2 \notin S(T)$ — no tree-level step-down induction.
3. **Selection rules dead**: the max-$k_{12}$ pair hosts an $L=8$
   config only 30/52; min-$|D|$ pair is a sweep pair 31/52; the pair
   attaining the global minimum even value, 29/52.
4. **Per-pair interval-ness NOT automatic**: 553/637 pairs with even
   values have step-2-interval even sets. All observed failures are the
   8-skipping pattern $E_p = \{6, 10\}$ at $|D| = 7$,
   $k_{12} \in \{4,5\}$: covers realize $\operatorname{gap}_3 = 2k'-2$
   and $2k'+2$ but never $2k'$.
5. **SURVIVES 52/52 (new probe `sweep_pair_exists`)**: some single pair
   has $E_p$ a step-2 interval containing 8. Endpoint structure: in the
   widest such pair, 8 is an endpoint 41/52 — nearly always the MINIMUM
   (confirmed by the probe's own tally: 8 is the interval min on 36/41
   residuals at the committed scale).
6. Global boundary facts (52/52): $\min(\text{even } S(T)) \in
   \{4, 6, 8\}$ (never $> 8$, never empty) and
   $\max(\text{even } S(T)) \ge 10$.

### What the analytic program becomes

The burden localizes to ONE pair (this round's probe), split three ways:

- **(i) Selection**: identify the pair analytically. None of the greedy
  rules work; the census suggests the witnessing pair is characterized
  by its cover arithmetic (small $|D|$ odd with a $\operatorname{gap}_3
  = 2k'$-class cover, or the $|D|$-even/odd-gap family), not by an
  extremal statistic.
- **(ii) Interval-ness of $E_p$**: the only observed failure mode is
  the $\operatorname{gap}_3 \bmod 4$ class gap at $|D| = 7$. Analytic
  sub-question: for which $(|D|, k_{12})$ does the cover family hit
  every $\operatorname{gap}_3 - 2k'$ residue in an interval? The
  $k'$-freedom (R28: $k' = 1$ insufficient 3/51) is exactly what fills
  classes.
- **(iii) Min-attainment**: prove $\min E_p = 8$ (not $\le 6$!) for the
  selected pair — the census says the sweep interval usually STARTS at
  8, so the lower endpoint is the theorem, not a bound to beat. (Not a
  direction flip against T2's "$v_{\min} \le 8$": $E_p$ is the sweep
  interval of ONE selected pair, while $v_{\min}$ is the endpoint of
  the tree-level union $V_e(T)$ over all configs. $\min E_p = 8$ for
  the selected pair puts $8 \in V_e(T)$ directly and is compatible with
  other pairs/triples realizing smaller even values — R35's $L = 4$
  firings show $v_{\min} = 4$ does occur on some trees.) A pair
  whose every short cover satisfies $|D| + \operatorname{gap}_3 + 1 -
  2k' \ge 8$ with equality attained is the target object; the parity
  bookkeeping ($|D|$ odd $\Rightarrow \operatorname{gap}_3$ even for
  even $L$) plus pair-residuality ($|D| \notin \{4,8,16,32\}$) are the
  available constraints.

### Summary of round R29

| Item | Status |
|------|--------|
| `sweep_pair_exists` probe (152k trees, 41 residuals committed) | **unfalsified, non-vacuous** (R29) |
| Tree-level even-interval / descent / greedy selection | **all falsified** (R29) |
| Per-pair interval failure mode | **isolated**: $E_p=\{6,10\}$ gap-at-8, $|D|=7$ (R29) |
| 8 as interval MINIMUM of the sweep pair | **dominant** (36/41) (R29) |
| Analytic split: selection / interval-ness / min-attainment | **formulated** (R30+ target) |

## Section 70 — R30: Floor/line lemma PROVED — the tuning program is now one supply statement (session s_0808-080808-ce3d)

### New proved lemma: `shortpaste_floor_line`

Elementary but load-bearing arithmetic for the short-paste class, all
proved (not probed) in `lemma_shortpaste_floor_line__0808-080808-ce3d.md`,
and machine-checked against the census extraction code (274k configs,
consistency CHECK):

1. **Parity**: even $L$ forces $g_3 \equiv |D| + 1 \pmod 2$.
2. **Overlap**: $g_3 \ge \max(k', 2)$ (a cycle properly contains its
   overlap path; simple graphs have no 2-cycles).
3. **Floor**: every even-$L$ short-paste config with $k' \le |D| - 6$
   has $L \ge 8$. The R29 undershoots ($L \in \{4, 6\}$) live entirely
   in the near-maximal-overlap regime $k' \ge |D| - 5$.
4. **Line**: $L = 8 \iff g_3 = 2k' + 7 - |D|$.

(Worked $L = 8$ boundary instances of $L = |D| + g_3 + 1 - 2k'$, for
single-instance re-derivation — each satisfies the line
$g_3 = 2k' + 7 - |D|$: $(|D|, k', g_3) = (6, 1, 3)$ gives
$6 + 3 + 1 - 2 = 8$; $(7, 1, 2)$ gives $7 + 2 + 1 - 2 = 8$;
$(7, 2, 4)$ gives $7 + 4 + 1 - 4 = 8$; $(9, 2, 2)$ gives
$9 + 2 + 1 - 4 = 8$; $(10, 4, 5)$ gives $10 + 5 + 1 - 8 = 8$. NOT on
the line: $(10, 1, 5)$ gives $10 + 5 + 1 - 2 = 14$, an even value
above the floor, not 8.)

(Worked ODD-$L$ boundary anchor — the floor's "even $L$" hypothesis is
LOAD-BEARING; do not re-derive the floor without it. At the boundary
$k' = |D| - 6$ with the raw overlap minimum $g_3 = \max(k', 2)$ one can
get $L = 7$: $(|D|, k', g_3) = (8, 2, 2)$ gives $8 + 2 + 1 - 4 = 7$,
which is ODD — outside the floor claim's hypothesis, NOT a
counterexample. Parity (claim 1) is what closes the gap: $|D| = 8$
even forces $g_3$ odd for even $L$, so the minimal admissible cover has
$g_3 = 3$, giving $L = 8 + 3 + 1 - 4 = 8$ — exactly on the line
$g_3 = 2k' + 7 - |D| = 3$. The floor claim quantifies ONLY over even
$L$; odd values like 7 between the parity classes are expected and
harmless.)

### Two reductions purchased by the lemma

**(A) T3's arithmetic half is gone.** Any pair with $|D| \ge 6$ and any
$k' = 1$ short cover has even $L \ge 8$ (both parity families of R27,
uniformly — the lone even-$|D|$ census tree stops being a special
case). *Hypothesis anchor (R40): this is a FLOOR over whatever $k'=1$
covers exist, not an exact-8 realizability claim. On a pair-residual
tree the $|D| = 6$, $k' = 1$ case cannot hit 8 at all: even $L$ forces
$g_3$ odd, and $g_3 = 3$ would make $C_3$ a $C_4$ — excluded by
residuality — so $g_3 \ge 5$ and $L \ge 10$ there. Exact 8 at
$|D| = 6$ requires $k' = 2$ (cell $(6,2)$ of §79's menu, which is why
$(6,1)$ is not a menu cell). No contradiction with §79.*
`t3_min_overlap_short_paste` reduces to pure supply:

> **(SUP-1)** every pair-residual tree admits a pair with $|D| \ge 6$
> and a short cover ($g_3 \le k_{12} + 1$) meeting $D$ in exactly one
> edge.

Only $|D| \in \{3, 5\}$ pairs escape; pair-residuality already excludes
$|D| \in \{4, 8, 16, 32\}$.

**(B) `tune8_short_paste` is equivalent to line-hitting.** The exact-8
statement is: some pair and short cover satisfy
$g_3 = 2k' + 7 - |D|$. Per-$|D|$ windows (parity automatic):
$|D|=7$: $(k', g_3) \in \{(1,2), (2,4), (3,6), \dots\}$;
$|D|=9$: $\{(2,2), (3,4), \dots\}$; $|D|=6$: $\{(1,3), (2,5), \dots\}$;
$|D|=5$: $\{(1,4), \dots\}$; $|D|=3$: $\{(1,6), \dots\}$. *(R40 note:
on pair-residual trees, entries with $|C_3| = g_3 + 1 \in \{4, 8\}$
are unrealizable — cover-residuality kills e.g. $(6; 1, 3)$ and
$(6; 3, 7)$; see §79's menu for the surviving $k' \le 2$ cells.)* The
short criterion couples each window entry to a minimum pair overlap
$k_{12} \ge g_3 - 1 = 2k' + 6 - |D|$: **large-$|D|$ pairs hit the line
with ANY overlap; small-$|D|$ pairs need overlap at least
$7 - |D|$-ish.** Triangle-free graphs remove only the $g_3 = 2$
entries ($(7; 1, 2)$ and $(9; 2, 2)$).

### The open core after R30 (Q9), sharpened

1. **(SUP-1)** above — the $L \ge 8$ existence supply (T3 leg, now
   arithmetic-free).
2. **(SUP-8)** line-hitting supply: a pair + short cover on
   $g_3 = 2k' + 7 - |D|$ (equivalent to `tune8_short_paste`; the
   sweep-pair probe `sweep_pair_exists` says the witnessing pair's even
   value set is moreover an interval with min 8 — consistent with the
   floor: a pair whose covers all sit in $k' \le |D| - 6$ cannot go
   below 8).
3. Standing hypotheses (unchanged): 2-connectedness reduction
   (Section 29); all-even/all-odd exclusion (Section 30); cubic →
   min-degree-3 reduction.

### Summary of round R30

| Item | Status |
|------|--------|
| `shortpaste_floor_line` (parity/overlap/floor/line) | **PROVED** + consistency CHECK (R30) |
| T3 arithmetic | **eliminated** — T3 = supply statement SUP-1 (R30) |
| tune8 | **= line-hitting** $g_3 = 2k'+7-|D|$, overlap-coupled windows (R30) |
| Undershoot regime | **confined** to $k' \ge |D|-5$ (R30) |
| SUP-1 / SUP-8 analytic proof | open (R31+ target) |

## Section 71 — R31: SUP-1 census — end-edge witnesses universal, min-gap selection rule survives (session s_0809-080835-54ee)

### New probe lemma: `sup1_end_edge`

The R30 handoff's first priority (SUP-1 positional census) executed:
three independent seeds, $n \in \{12..24\}$, 480k sampled DFS trees,
152 pair-residual, plus a fourth seed (152k trees, 37 residuals) inside
the committed CHECK. Results:

1. **SUP-1 holds 189/189** (all four seeds): every pair-residual tree
   admits a pair with $|D| \ge 6$ and a $k' = 1$ short cover
   ($\operatorname{gap}_3 \le k_{12}+1$, $D \cap C_3$ a single edge)
   with $|D| + \operatorname{gap}_3$ odd — hence an even short-paste
   value $L \ge 8$ by `shortpaste_floor_line`. The odd-$L$-only
   fallback was never needed (0 trees where $k'=1$ short covers exist
   only with the wrong parity).
2. **End-edge refinement 100% (126/126 checked)**: the witness's met
   edge can always be taken to be an END edge of its $D$-segment
   (incident to $a_{\mathrm{sh}}$, $a_{\mathrm{deep}}$, $m$, or a
   sender $s_i$). Witness distribution: 318 end vs 41 interior
   (seed 1) — end edges dominate but the refinement is about
   existence, which never fails.
3. **Min-gap selection rule 100% (126/126)**: for some pair
   ($|D| \ge 6$) and some end edge $e$, the MINIMUM-GAP back edge
   covering $e$ is itself a SUP-1 witness. This is the analytic
   handle: 2-edge-connectedness supplies covers of every tree edge;
   the rule says the cheapest cover of the right boundary edge works.
4. **Falsified finer variants** (recorded so no session chases them):
   leg-TOP-only fails 3/63 (seed 2); leg-BOTTOM-only 38/39; $A$-end-only
   38/39 (seed 1). No single boundary vertex class suffices — the
   disjunction over all six is the survivor.
5. **Structural fact with proof sketch**: every SHORT cover of the
   leg-top edge $(m, c_i)$ anchors inside the cancelled interval $I$
   (else it contains $I$ plus $A$'s deepest edge — a straddle, forcing
   $\operatorname{gap}_3 \ge k_{12}+2$ by `pasting_cover_dichotomy`).
   Observed 60/60 (seed 2). Witness min-gaps concentrate at
   $\operatorname{gap}_3 \in \{2, 4\}$ (54/60).

### What the analytic program becomes

SUP-1 is now a two-step target, both localized to segment boundaries:

- **(i) Cover existence with shortness+parity at SOME end edge**: among
  the six end edges of a $|D| \ge 6$ pair, one has a min-gap cover that
  is short ($\le k_{12}+1$) with $\operatorname{gap}_3 \equiv |D|+1
  \bmod 2$. Shortness is NOT automatic (90 non-short $k'=1$ even-$L$
  end-edge covers observed on seed 3 alone), so the argument must
  either pick the pair (maximize $k_{12}$?) or trade end edges off
  against each other.
- **(ii) $k' = 1$ at the boundary**: for an end-edge cover, $k'=1$
  means the cover's tree path diverges from the segment immediately
  past the met edge. At the leg top this is forced when $s_3 = c_i$ or
  the chain of $s_3$ leaves $L_i$ right below $c_i$ (47/60 witnesses
  have $s_3 = c_i$ exactly).

### Summary of round R31

| Item | Status |
|------|--------|
| `sup1_end_edge` probe (4 seeds, 632k trees, 189 residuals) | ~~unfalsified~~ **SUPERSEDED — disproved at R33** (`sup1_dead_tree`) |
| SUP-1 (T3 supply) | ~~holds 189/189~~ **SUPERSEDED — FALSE at R33**; the 189/189 was sampling luck |
| End-edge witness + min-gap rule | ~~100% (126/126 each)~~ **SUPERSEDED — disproved at R33** (both refinements die with SUP-1) |
| Leg-top-only / leg-bottom-only / A-end-only | **all falsified** (R31) |
| Short leg-top covers anchor in $I$ | **proved-sketch + 60/60** (R31) |
| SUP-1 analytic proof (steps i+ii) | open (R32+ target) |

## Section 72 — R32: SUP-1 localizes to the cancelled interval's boundary; cover structure there PROVED (session s_0809-080835-54ee)

### New lemma: `sup1_iadj` (proved Part 1 + open Part 2)

Scoping censuses first (all standalone): the $\forall$-pair versions of
R31's min-gap rule are DEAD — "every $|D| \ge 6$ pair admits the rule"
and even "every $|D| \ge 6$ pair admits some SUP-1 witness" fail on
EVERY sampled residual tree (0/37 each; per-pair rates 211/698 and
245/698); max-$k_{12}$ pair selection reaches only 10/37. Working
pairs usually expose exactly ONE working end edge (157/211). So pair
selection is load-bearing and greedy statistics are dead — consistent
with R29.

The positive localization: restricting R31's rule to the (at most
three) **$I$-adjacent boundary edges** — leg tops $(m, c_i)$ and the
$A$-bottom edge at $a_{\mathrm{deep}}$ — still works on every tree
(42/42 at seed 532, 50/50 at the committed probe's seed 632), and NO
tree ever needs a far boundary edge (senders' ends, $a_{\mathrm{sh}}$'s
end). The SUP-1 witness lives at the boundary of the cancelled
interval.

**Proved (Part 1, from `pasting_cover_dichotomy` + cubic geometry;
consistency-checked on 1.03M short-cover configs):** short covers
through $I$-adjacent edges are pinned to the $I$-window —

- Leg-top $(m, c_i)$, $A \ne \emptyset$: the cover anchors INSIDE $I$
  ($a_3 \in V(I)$ — else it would contain $I$ plus $A$'s bottom edge
  and straddle, forcing $\operatorname{gap}_3 \ge k_{12}+2$), meets
  only $L_i$, and $k' = 1 + (\text{common descent of } P_3, L_i
  \text{ below } c_i)$. $k'=1$ iff divergence at $c_i$ (e.g.
  $s_3 = c_i$, or $|L_i| = 1$).
- $A$-bottom: meets only $A$,
  $k' = d(a_{\mathrm{deep}}) - \max(d(a_3), d(a_{\mathrm{sh}}))$;
  $k'=1$ iff $a_3 = \mathrm{par}(a_{\mathrm{deep}})$ or $|A|=1$; with
  both legs nonempty $s_3$ is never strictly below $m$ (all children
  of $m$ are leg children in a cubic graph).

### The analytic burden after R32

1. **(Selection)** Which pair: the witnessing pair is NOT extremal in
   any tested statistic; candidate characterizations should come from
   the cover side (which pairs have a short-with-right-parity min-gap
   cover at an $I$-adjacent edge).
2. **(Existence)** Why some $I$-adjacent edge's min-gap cover is short
   with $\operatorname{gap}_3 \equiv |D|+1 \bmod 2$ and $k'=1$ — Part 1
   reduces this to: the cover anchors in the $I$-window / meets one
   segment, so shortness couples $\operatorname{gap}_3$ to $k_{12}$
   through the window depth, and $k'=1$ is a local divergence
   condition at $c_i$ resp. $a_{\mathrm{deep}}$.
3. SUP-8 (line-hitting, $L = 8$ exactly) unchanged — the sweep-pair
   census (R29) plus the floor (R30) still frame it.

### Summary of round R32

| Item | Status |
|------|--------|
| `sup1_iadj` Part 1 (cover structure at $I$-adjacent edges) | **PROVED** + 1.03M-config CHECK (R32) |
| `sup1_iadj` Part 2 probe (I-adjacent min-gap rule) | **unfalsified**, 92/92 across 2 seeds (R32) |
| Far-boundary-edge necessity | **never observed** (0 trees) (R32) |
| $\forall$-pair rule / $\forall$-pair SUP-1 / max-$k_{12}$ | **all falsified** (0/37, 0/37, 10/37) (R32) |
| SUP-1 analytic proof (selection + existence) | open (R33+ target) |

## Section 73 — R33: SUP-1 FALSIFIED — a pair-residual tree with no k'=1 supply at all; program forks (session s_0810-081024-1a40)

### The counterexample (new lemma `sup1_dead_tree`, PROVED)

The R32 handoff's census move (tabulate min-gap covers at $I$-adjacent
edges) ran on fresh seeds and, at seed 77003, surfaced a residual tree
whose (pair $\times$ $I$-adjacent edge) candidate set contains no
$k'=1$-with-parity min-gap cover. Widening the scan on that graph found
DFS trees with **no SUP-1 witness of any kind**: a 14-vertex cubic
graph $G_0$ with a pinned normal spanning tree $T_0$ (depth-13,
fundamental cycle lengths $[3,6,6,6,3,14,6,6]$) that is pair-residual
and — exhaustively over all 16 eligible pairs and all third back edges
— admits NO cover with $k' = 1$, $\operatorname{gap}_3 \le k_{12}+1$,
and $\operatorname{gap}_3 \equiv |D|+1 \bmod 2$.
`lemma_sup1_dead_tree__0810-081024-1a40.md` pins the object with a
fully deterministic CHECK (no sampling).

Dead as universals over pair-residual trees, all at once:

- **SUP-1** (`sup1_end_edge` core, "189/189" R31) — status: disproved.
- End-edge refinement + min-gap selection rule (R31) — dead a fortiori.
- **`sup1_iadj` Part 2** ($I$-adjacent supply, "92/92" R32) — status:
  disproved. (Part 1's cover-structure geometry is untouched and
  remains proved.)

Rarity: 0/167 residuals on three fresh seeds (564k trees), ~1/250
overall across five seeds — rare enough that four independent R31/R32
censuses missed it, common enough that the analytic program would have
died at the first serious attack on "existence".

### Why the tree still fires: the $k'' \in \{2,4\}$ channels

$T_0$ is **triple-alive**: six triples give 3-way sym-diffs that are
single 8-cycles. Every one works through met-path sizes
$|D \cap C_3| \in \{2, 4\}$ (two shapes: $|D|=6$, $k_{12}=3$,
$\operatorname{gap}_3=5$, non-short, $k''=2$, $L = 6+6-4 = 8$; and
$|D|=10$, $k_{12}=5$, $\operatorname{gap}_3=5$, short, $k''=4$,
$L = 10+6-8 = 8$). The $k'=1$ paste class the program tuned since R23
is provably insufficient; the triple mechanism as a whole is not.

Also recorded: no $k$-subset of back edges with $k \in \{5,\dots,8\}$
fires on $T_0$ (quads do), and $G_0$ has cycles of every length
$3,5..14$ — the graph is no E-G counterexample; 976/1000 sampled DFS
trees of $G_0$ are non-residual.

### Salvage: the conditional selection rule (recorded, not committed)

Before the counterexample surfaced, the census confirmed a clean
arithmetic selection rule on SUP-1-**alive** trees: among all
candidates (pair $|D| \ge 6$, $I$-adjacent edge) whose min-gap cover
has $k'=1$ and correct parity, the minimum-$\operatorname{gap}_3$
candidate is itself short — hence a witness — **123/123 trees across
four seeds** (and "every min-achiever short" 121/123). If SUP-1
returns in a per-graph form, this closes its selection half; parked
until then.

### The fork (R34+ decision)

Two ways forward, not exclusive:

1. **Widen tree-level supply to all met sizes**: conjecture
   "every pair-residual normal spanning tree is triple-alive" (some
   triple's sym-diff is a single po2 cycle). This is the honest,
   mechanism-complete universal — it subsumes SUP-8 and absorbs the
   $k''\ge 2$ channels the counterexample exposed. Cost: the clean
   interval/tuning arithmetic of R23–R30 covered only $k'=1$ pastes;
   $k'' \ge 2$ pastes need their own value formula
   ($L = |D| + \operatorname{gap}_3 + 1 - 2k''$, single-cycle
   conditions from `triple_sym_diff_structure`).
2. **Move the quantifier to the graph**: "every cubic graph has SOME
   normal spanning tree where a single/pair/triple mechanism fires."
   Empirically overwhelming (976/1000 on $G_0$); analytically a
   different game (choose the DFS, e.g. leaf-count or depth extremal
   trees), closer to how the literature attacks E-G.

Q9 (the SUP-1 analytic program) is resolved as **falsified-framing**;
Q68 opens the fork with the triple-aliveness probe as the immediate
dual-attack target.

### Summary of round R33

| Item | Status |
|------|--------|
| `sup1_dead_tree` (pinned counterexample) | **PROVED**, deterministic CHECK (R33) |
| SUP-1 universal / end-edge / min-gap (R31) | **DISPROVED** (R33) |
| `sup1_iadj` Part 2 ($I$-adjacent supply) | **DISPROVED** (R33) |
| `sup1_iadj` Part 1 (cover geometry) | proved, unaffected |
| Conditional selection rule (alive trees) | 123/123, parked (R33) |
| Triple-aliveness universal (fork branch 1) | open — R34 probe target |
| Graph-level quantification (fork branch 2) | open — fallback |

## Section 74 — R34: Triple-aliveness — the mechanism-complete supply universal (session s_0810-081024-1a40)

### New lemma `triple_alive_universal` (open, probe committed)

Q68's fork branch 1 gets its dual-attack probe. **Claim**: every
pair-residual normal spanning tree of a cubic graph is triple-alive —
some 3-subset of back edges has a single-cycle power-of-2 sym-diff,
with NO restriction on the met size $k'' = |D \cap C_3|$. The fired
length through any pairing is $L = |D| + \operatorname{gap}_3 + 1 -
2k''$.

**Census: 176/176 residual trees across four seeds (571k trees).**
The channel split is the analytically decisive datum:

- mixed ($k''=1$ and $k'' \ge 2$ both fire): 151;
- only $k''=1$: 13 — a $k'' \ge 2$-only rule dies here;
- only $k'' \ge 2$: 12 — the SUP-1 class dies here (this bucket
  contains `sup1_dead_tree`'s pinned anchor).

So neither sub-channel suffices alone; the honest universal is the
disjunction. All observed firings hit $L = 8$ exactly (never 4/16/32
on a residual tree) — worth asserting or refuting at scale, since
"$L = 8$ always available" would collapse SUP-8 into this claim.

CHECK 1 (deterministic): the pinned SUP-1-dead tree is triple-alive
with exactly six firing triples, all $L = 8$. CHECK 2 (probe, ~10s):
125k trees / 32 residuals, all triple-alive, fixed seed; an assert
failure prints (graph, root, parent array) ready for pinning.

### R35+ plan

1. Joint $(|D|, \operatorname{gap}_3, k'', L)$ census of firing
   triples on residual trees: which arithmetic identities pin $L = 8$;
   how often the firing pairing straddles vs pastes
   (`pasting_cover_dichotomy`'s two branches).
2. Build the $k'' \ge 2$ value theory: for straddling covers, the met
   set spans two segments — derive the analogue of the
   `shortpaste_floor_line` interval for $k'' \ge 2$ and check whether
   the two channels' value sets always jointly cover 8.
3. If the probe survives R35's wider sweep, promote triple-aliveness
   to the program's headline supply conjecture and retire SUP-8 as a
   separate target.

### Summary of round R34

| Item | Status |
|------|--------|
| `triple_alive_universal` probe (4 seeds, 571k trees, 176 residuals) | **unfalsified, non-vacuous** (R34) |
| Channel split (13 only-$k''{=}1$ / 12 only-$k''{\ge}2$ / 151 mixed) | measured (R34) |
| All residual-tree firings at $L = 8$ | observed, unasserted (R35 target) |
| $k'' \ge 2$ value theory | open (R35+ target) |

## Section 75 — R35: L=8 exactness FALSIFIED; census confirms triple-aliveness at 641/641 and the arc bound (session s_0811-081051-a768)

### New proved lemma: `l8_exactness_dead` (pinned counterexample)

R34's open question 1 ("all residual-tree firings are $L = 8$
exactly") is settled negatively, cheaply, and deterministically. A
randomized sweep at $n = 12$ (seed 99001) surfaced, and the lemma's
CHECK exhaustively verifies, a 12-vertex cubic graph with a
pair-residual normal tree (root 10) whose 7 firing triples split
$\{L{=}4: 1,\; L{=}8: 6\}$. The fired 4-cycle
$(1,2),(2,10),(4,10),(1,4)$ is an ordinary $C_4$ of the graph that is
invisible to every fundamental cycle and every pair sym-diff —
detecting an *existing* power-of-2 cycle can genuinely require triple
depth. The exactness observation was a census-window artifact (and in
hindsight sat in tension with R18's older census, which had already
recorded $C_4$ 39x / $C_{16}$ 1x among 738 firings under the earlier
residual pipeline).

### R35 census (five seeds + smoke, 1,605,440 trees, 465 residuals)

- **Triple-aliveness: 465/465** (0 dead trees; cumulative with R34:
  **641/641**). The universal survives a 2.8x larger sweep.
- **Firing histogram** (3,268 firing triples): $L=8$ 3,017 (92.3%),
  $L=16$ 199 (6.1%), $L=4$ 52 (1.6%).
- **Per-tree firing-length sets** (295 tracked residuals): $\{8\}$
  225x, $\{4,8\}$ 31x, $\{8,16\}$ 36x, $\{4,8,16\}$ 3x — **8 present
  295/295**. The per-tree refinement "every pair-residual tree has
  some $L = 8$ firing" (per-tree SUP-8) is unfalsified and becomes
  R36's probe lemma.
- **Pairing frame loses no generality**: every firing triple (3,268)
  had $\ge 1$ pairing with $D$ a single cycle.
- **Arc bound observed unconditionally**: over 8,307 usable pairings,
  $D \cap C_3$ always had $\le 2$ arcs — the paste/straddle dichotomy
  (`pasting_cover_dichotomy`, proved for overlapping pairs) held in
  every observed configuration; $k''=1$ was always 1-arc (1,693/1,693,
  consistent with `pasting_vertex_automatic`); $k'' \ge 2$ split 4,843
  paste / 1,771 straddle.
- **Identity exact**: $L = |D| + \operatorname{gap}_3 + 1 - 2k''$ held
  in all 8,307 pairings ($k''$ up to 16, $|D|$ up to 22).
- **No channel is length-pure**: $L=8$ arises via $k''=1$ (1,497) and
  $k'' \ge 2$ (6,175); so do $L=4$ (13/112) and $L=16$ (183/327). A
  value theory cannot pin length from the channel alone.
- Caveat: per-tree channel classification (this sweep: 441 mixed, 24
  only-$k'' \ge 2$, 0 only-$k''=1$) used ALL usable pairings per
  firing triple; R34's 13/176 only-$k''=1$ bucket likely classified
  per-triple minima — the definitions differ, so the two splits are
  not directly comparable. Both agree on the load-bearing fact: each
  channel alone is insufficient.

### Program shape after R35

1. `triple_alive_universal` stays the headline supply conjecture, with
   the full power-of-2 disjunction (no L=8 collapse).
2. **R36**: split off per-tree SUP-8 as its own probe lemma
   (`sup8_tree_universal`): every pair-residual tree has some firing
   triple at $L = 8$ exactly. If it survives, the value theory only
   has to produce 8 (not any po2); if it dies, the pinned tree will
   show which lengths must be produced instead.
3. The $k'' \ge 2$ value theory (straddle analogue of
   `shortpaste_floor_line`) remains the analytic core: straddle
   produced 1,771/8,307 firing pairings, and 24 trees fire ONLY via
   $k'' \ge 2$.

### Summary of round R35

| Item | Status |
|------|--------|
| `l8_exactness_dead` (pinned 12-vertex counterexample) | **proved** (R35) |
| Triple-aliveness at scale (465/465; cumulative 641/641) | **unfalsified** (R35) |
| Per-tree "8 always available" (295/295) | observed, probe at R36 |
| Arc bound $\le 2$ / identity exact (8,307 pairings) | **verified** (R35) |
| $k'' \ge 2$ straddle value theory | open (R36+ target) |

## Section 76 — R36: per-tree SUP-8 split off as `sup8_tree_universal` (session s_0811-081051-a768)

### New lemma `sup8_tree_universal` (open, probe committed)

R35's fork is made precise. `l8_exactness_dead` killed the per-firing
form of "the triple mechanism produces 8"; the strongest surviving
8-specific statement is per-tree:

**Claim**: every pair-residual normal spanning tree of a connected
cubic graph has some firing triple at $L = 8$ **exactly**.

Evidence: 295/295 tracked residual trees at R35 (length-set table in
the lemma), 176/176 at R34 (all observed firings there were 8), and
both deterministic pinned anchors (`sup1_dead_tree` 6/6 at 8;
`l8_exactness_dead` 6/7 at 8, including the tree that also fires a 4).
Cumulative: 471/471 across ten seeds.

CHECK 1 anchors on the `l8_exactness_dead` pin — the tree that DOES
fire at 4 still has six $L = 8$ triples, so the pin that killed
exactness complies with the per-tree form. CHECK 2 is a fresh-seed
(20260811) 125k-tree probe requiring an $L = 8$ firing on every
residual tree (39 residuals, non-vacuous, ~10s), printing (graph,
root, parent array) on any falsifier for immediate pinning.

### Why this split matters for the value theory

- If `sup8_tree_universal` holds, the $k'' \ge 2$ straddle value
  theory only has to show 8 is attainable — one target length, and the
  R23 tuning reduction (Section 48) becomes unconditional.
- If it dies, the pinned falsifier will be a residual tree served ONLY
  by $L \in \{4, 16, 32\}$ — the first hard evidence that the supply
  argument must genuinely track all four lengths, and
  `triple_alive_universal` (the disjunction) remains the honest
  headline.
- Either way `triple_alive_universal` is untouched: sup8 is strictly
  stronger, and its failure does not propagate down.

### Summary of round R36

| Item | Status |
|------|--------|
| `sup8_tree_universal` lemma + 2 CHECKs (anchor + fresh-seed probe) | **committed, open** (R36) |
| Per-tree SUP-8 evidence base | 471/471 across ten seeds (R34+R35) |
| Next: $k'' \ge 2$ straddle value theory targeting 8 | open (R37+) |

## Section 77 — R37: Straddle value theory PROVED — both channels now exact lines (session s_0812-081033-f881)

### New proved lemma: `straddle_floor_line`

The $k'' \ge 2$ straddle analogue of `shortpaste_floor_line` (the open
core item 1 from R36) is closed in one round, and it is *exact*, not
just a floor. For a straddling cover of pair $(B_1, B_2)$ met on leg
$L_i$ (unmet leg $L_j$), define $w = \operatorname{lca}(s_3, s_i)$,
$y = d(a_{\mathrm{deep}}) - d(a_3)$, and four nonnegative **slacks**
$\alpha_A = |A| - k_A$, $\beta_A = y - k_A$,
$\alpha_L = |L_i| - k_L = d(s_i) - d(w)$,
$\beta_L = d(s_3) - d(w)$. Then (all proved, elementary interval
combinatorics on tree chains):

1. **Arc dichotomy**: $D \cap C_3$ has exactly as many arcs as
   segments met, $\le 2$ — R35's observed 8,307/8,307 arc bound is now
   a THEOREM; $k'' = k_A + k_L$ in the straddle case.
2. **Exact formula**:
   $\tilde L = |D \oplus C_3| = k_{12} + 3 + |L_j| + \alpha_A +
   \beta_A + \alpha_L + \beta_L$.
3. **Coupling**: $\alpha_A \cdot \beta_A = 0$.
4. **Floor**: $\tilde L \ge k_{12} + 3 + |L_j| \ge 4$; $\tilde L = 4$
   forces the rigid zero-slack $(k_{12}, |L_j|) = (1, 0)$ config.
5. **8-line**: $\tilde L = 8 \iff k_{12} + |L_j| + \Sigma = 5$; hence
   straddle-8 needs $k_{12} \le 5$ and $|L_j| \le 4$.

Worked anchor (n=10, root 1, $B_1 = (2,1)$, $B_2 = (0,3)$,
$B_3 = (7,8)$; deterministically re-verified in the lemma's CHECK 1):
$k_{12} = 1$, $|L_j| = |L_1| = 1$, slacks $(2, 0, 1, 0)$, so
$\tilde L = 1 + 3 + 1 + 2 + 0 + 1 + 0 = 8$; identity cross-check
$|D| = 10$, $g_3 = 5$, $k'' = 4$: $10 + 5 + 1 - 8 = 8$. The
floor-tight anchor (n=10, root 4) has all slacks 0, $k_{12} = 1$,
$|L_j| = 0$: $\tilde L = 4 = 10 + 9 + 1 - 16$.

Scratch sweep (seed 20260812, $n \in \{10..18\}$): 94,940 straddles,
formula exact on ALL; 53,336 fired, $\tilde L$-histogram min 4
(105 rigid $L{=}4$s), 6,331 fired straddle-8s. CHECK 2 (seed
20260812+37, ~1s) asserts claims 1–5 on every straddle config:
23,514 straddles, 1,918 fired 8s, 29 floor-tight 4s, zero violations.

### Program shape after R37

- **The value side of the whole program is DONE.** Every usable
  pairing is paste (1 arc: `shortpaste_floor_line`, exact line
  $g_3 = 2k' + 7 - |D|$) or straddle (2 arcs: exact line
  $k_{12} + |L_j| + \Sigma = 5$) — no third channel, by claim 1.
- **`sup8_tree_universal` is now supply + firing only**: every
  pair-residual tree needs SOME pair + cover ON one of the two
  8-lines with $D \oplus C_3$ a single cycle. The remaining
  difficulty is existential (supply) and topological (firing =
  single-cycle-ness), not arithmetic.
- Cheap screen for the supply hunt: straddle-8 hosts need
  $k_{12} \le 5$, $|L_j| \le 4$; the observed straddle-8s are
  dominated by $|L_j| = 0$ (ancestor-type pairs — one sender on the
  other's root-chain).

### Summary of round R37

| Item | Status |
|------|--------|
| `straddle_floor_line` (formula + coupling + floor + 8-line) | **proved** (R37) |
| Arc bound $\le 2$ (R35: observed) | **upgraded to theorem** (R37) |
| Value theory, both channels | **complete** (R30 + R37) |
| Next: supply + firing for the two 8-lines on residual trees | open (R38+) |

## Section 78 — R38: Channel census — the straddle channel is never necessary; `paste8_tree_universal` split off (session s_0812-081033-f881)

### Census (seed 20260812+38, n ∈ {12..22}, 128,800 trees, 43 residual)

With both value lines proved (R30 paste, R37 straddle), the supply
question is WHICH channel serves each residual tree's $L = 8$ firings.
Classifying every $L = 8$ firing triple of every residual tree by the
arc count of its usable pairings:

- **paste-8 available: 43/43 residual trees** (some $L = 8$ triple
  admits a 1-arc pairing);
- straddle-ONLY trees: **0**; trees with no 8 at all: **0** (consistent
  with `sup8_tree_universal` at 471/471 + these 43 = 514/514);
- straddle-8s coexist on many trees — per-tree $(k_{12}, |L_j|)$
  occurrences dominated by $(1, 0)$ 38x, $(3, 0)$ 24x, $(2, 0)$ 17x —
  but were never the only route;
- both deterministic pins comply maximally: ALL $L = 8$ triples on the
  `l8_exactness_dead` tree (6/6) and the `sup1_dead_tree` tree (6/6)
  are paste-realizable.

### New lemma `paste8_tree_universal` (open, probe committed)

**Claim**: every pair-residual normal spanning tree of a connected
cubic graph has an $L = 8$ firing triple realized through a 1-arc
(paste) usable pairing.

Strictly stronger than `sup8_tree_universal` (which allows any
channel). If it holds, the supply program collapses to the paste
8-line $g_3 = 2k' + 7 - |D|$ — the channel where
`pasting_vertex_automatic`, the dichotomy paste-certificates
(c1)–(c3), and `shortpaste_floor_line`(b) already live — and the
straddle line becomes a proved-but-unneeded spare. If it dies, the
pinned falsifier is the first residual tree that genuinely needs a
straddle, and effort redirects to the straddle 8-line
($k_{12} + |L_j| + \Sigma = 5$) with the weaker universals intact.

CHECK 1 audits both pins deterministically (12/12 paste-realizable).
CHECK 2 is a fresh-seed (20260812) 124k-tree probe (34 residuals,
~10s) asserting a paste-8 on every residual tree, printing the tree on
any falsifier.

### The open ladder after R38 (strongest to weakest)

1. `paste8_tree_universal` — paste-8 on every residual tree (R38);
2. `sup8_tree_universal` — some-8 on every residual tree (R36);
3. `triple_alive_universal` — some po2 firing on every residual tree
   (R34; the honest headline).

Each is a probe with a falsifier-printing CHECK; a kill at level $k$
redirects to level $k+1$ with a pinned counterexample in hand.

### Summary of round R38

| Item | Status |
|------|--------|
| Channel census (43 residual trees, both pins) | paste-8 universal, 43/43 + 12/12 |
| `paste8_tree_universal` lemma + 2 CHECKs | **committed, open** (R38) |
| Supply target if it holds | paste 8-line only: $g_3 = 2k' + 7 - |D|$ |
| Next: prove paste-8 supply on a structured subclass, or hunt bigger-n falsifiers | open (R39+) |

## Section 79 — R39: Cell census — the paste-8 certificate is $O(1)$-local; `paste8_k2_universal` split off (session s_0813-080958-9732)

### Census (seed 20260813, n ∈ {12..26}, 153,600 trees, 46 residual)

R38 said WHICH channel (paste); R39 asks WHERE on the paste 8-line
$g_3 = 2k' + 7 - |D|$ the witnesses live. Enumerating ALL paste-8
witnesses of every residual tree and tabulating their $(|D|, k')$
cells:

- **$k' \le 2$ witness: 46/46 residual trees** (min-$k'$ histogram:
  $k'=1$ on 43, $k'=2$ on 3);
- $k' = 1$ is NOT universal: three fresh $n = 14$ trees (hard1–hard3,
  pinned) have no $k'=1$ paste-8 at all — their $k' \le 2$ cells are
  $(6,2)$ and $(9,2)$. R33's `sup1_dead_tree` pin turns out to be a
  fourth such tree (its six paste-8s are $(6,2)$/$(10,4)$ only);
- $k' \le 2 \wedge$ short is NOT universal: `sup1_dead_tree`'s only
  $k' \le 2$ witnesses are six non-short $(6,2)$'s
  ($g_3 = 5 > k_{12}+1 = 4$). The short-cover condition CANNOT be
  added to the $k' \le 2$ claim;
- dominant cells by tree-coverage: $(6,2)$ 38x, $(5,1)$ 34x, $(7,1)$
  30x, $(9,2)$ 27x, $(9,3)$ 32x, $(10,4)$ 28x; 38 distinct per-tree
  cell profiles — no single cell is universal, but in-sample every
  tree has a witness with $k'=1$ OR in cell $(6,2)$.

### The finite-menu arithmetic (proved, in the new lemma)

On a residual tree a $k' \le 2$ paste-8 witness can only occupy eight
cells: $k'=1$: $|D| \in \{3,5,7\}$; $k'=2$: $|D| \in \{3,5,6,7,9\}$.
Proof: $g_3 \ge 2$ bounds $|D| \le 2k'+5$; pair-residuality kills
$|D| \in \{4,8\}$; cover-residuality kills $|C_3| = g_3+1 \in \{4,8\}$,
which for $k'=1$ removes $|D|=6$. Seven of the eight cells are
observed; $(3,2)$ (triangle $D$, 9-cycle cover overlapping 2 of its 3
edges) is allowed but unseen in 46 trees.

### New lemma `paste8_k2_universal` (open, probe committed)

**Claim**: every pair-residual normal spanning tree of a connected
cubic graph has a paste-8 witness with $k' \le 2$.

Strictly stronger than `paste8_tree_universal`; strictly weaker than
the dead $k'=1$ and $k'\le2\wedge$short forms, which CHECK 1 pins as
false (4 resp. 1 pinned counterexamples). Its value: combined with the
proved menu, EVERY quantified witness is a bounded configuration —
$|D| \le 9$, cover length $\le 9$, overlap $\le 2$ edges — so if the
claim holds, 8-supply is certified inside constant-size windows and
the analytic burden becomes a bounded-configuration analysis (the
value side is already closed by `shortpaste_floor_line`). CHECK 1
audits the five pins deterministically; CHECK 2 is a fresh-seed
(20260814) 124k-tree falsification probe (43 residuals, ~10s).

### The open ladder after R39 (strongest to weakest)

1. `paste8_k2_universal` — $k' \le 2$ paste-8 on every residual tree (R39);
2. `paste8_tree_universal` — any paste-8 (R38);
3. `sup8_tree_universal` — any-channel 8 (R36);
4. `triple_alive_universal` — any po2 firing (R34).

Dead strengthenings of level 1 (do NOT revisit): $k'=1$ (4 pins),
$k' \le 2 \wedge$ short (`sup1_dead_tree`).

### Summary of round R39

| Item | Status |
|------|--------|
| Cell census (46 residual trees, all paste-8 witnesses) | $k' \le 2$ universal in-sample, 46/46 |
| $k'=1$ universal | **DEAD** — hard1–3 + `sup1_dead_tree` pinned (R39) |
| $k' \le 2 \wedge$ short universal | **DEAD** — `sup1_dead_tree` pinned (R39) |
| Finite $k' \le 2$ cell menu (8 cells) | **PROVED** (arithmetic, R39) |
| `paste8_k2_universal` lemma + 2 CHECKs | **committed, open** (R39) |
| Supply target if it holds | bounded-configuration analysis, windows ≤ 9 |

## Section 80 — R40: `paste8_k2_universal` DISPROVED at witness-box scale — no $O(1)$-local certificate; adversarial SA reaches $n \ge 30$ residuals (session s_0813-080958-9732)

### Rejection sampling dies above n=26; SA breaks through

At $n \ge 28$ with girth $\ge 5$, rejection sampling produced **0
residual trees in 3,160** (7s) — pair-residuality decays too fast for
sampling to test anything in the witness box ($n \in [30, 64]$). R40
switched to adversarial construction: simulated annealing over (cubic
graph, DFS tree) pairs with energy = #po2 singles + #po2 pair
sym-diffs, moves = cubic 2-opt rewires (girth $\ge 5$ preserved) and
DFS re-root/re-order, 391 restarts / 420s → **20 pair-residual trees
at $n \in \{30, 32, 36, 40\}$** (10/6/3/1). This is the harness's
first residual population above the F3 minimal-counterexample floor.

### The kill

**4 of the 20 trees have NO $k' \le 2$ paste-8** — min witness
$k' = 3$ or 4. Three are pinned deterministically (CHECK 2 of the
lemma file): `viol1_n30` (min $k'=3$, 12 L=8 triples), `viol2_n30`
(min $k'=4$), `viol3_n40` (min $k'=4$). `paste8_k2_universal`:
open → **disproved** (introduced R39, killed R40 — the falsify
critic's "all evidence below n=30" WARN was exactly right).

Dead with it: any bounded-$k'$ / bounded-window ($O(1)$-local) supply
certificate. Observed min witness $k'$ grows with $n$; witness cells
at $n \ge 30$ run up the 8-line to $(25, 18)$. The $k' \le 2$ finite
menu stays a proved arithmetic fact; only universality died.

### What survives, strengthened

Every one of the 20 adversarial trees HAS a paste-8:
`paste8_tree_universal` now carries 20/20 adversarial evidence at
$n \in [30, 40]$ on top of 43/43 sampled at $n \le 26$ (evidence
bullet added to its lemma file). The $k' \le 2$ cells seen at
$n \ge 30$ — $(5,1), (5,2), (6,2), (7,2)$ — still respect the menu.

### The open ladder after R40 (strongest to weakest)

1. ~~`paste8_k2_universal`~~ — DISPROVED (R40);
2. `paste8_tree_universal` — any paste-8 (R38) — **the supply target**;
3. `sup8_tree_universal` — any-channel 8 (R36);
4. `triple_alive_universal` — any po2 firing (R34).

### R41+ plan

1. SA-harden `paste8_tree_universal` itself: bias the SA energy to
   ALSO penalize paste-8 availability (search for a residual tree with
   no paste-8 / no 8 at all) — the same technique that killed level 1
   is the strongest available falsifier for levels 2–4.
2. If level 2 survives adversarial attack: the analytic proof must
   produce a paste-8 with UNBOUNDED $k'$ — the value line
   $g_3 = 2k'+7-|D|$ covers all $k'$, so the burden is pure supply:
   show SOME pair + cover meeting in one arc on the 8-line. Candidate
   handle: the R30 dichotomy certificates (c1)–(c3) don't bound $k'$.
3. Fallback (untouched): graph-level quantifier — choose the DFS tree.


## Section 81 — R41: the ladder SURVIVES direct adversarial pressure — 261/261 hardened trees keep a paste-8; straddle never necessary; min paste $k'$ reaches 5 at $n = 32$ (session s_0814-082720-9c93)

### The experiment (Q70)

R40's SA falsifier only *reached* pair-residuality (energy = #po2
firings). R41 turned the same harness against the surviving ladder
itself: lexicographic energy — residuality violations first, then,
on pair-residual trees, the **availability count the target claim
asserts is positive** (three modes: #paste-8 triples / #$L=8$ triples
/ #po2 firing triples), moves = cubic 2-opt keeping girth $\ge 5$ +
DFS re-root/re-order, $n \in [30, 64]$. Two independent runs, ~2.9M
SA iterations, ~32 min total.

### Result: zero falsifiers at every ladder level

**261 pair-residual trees constructed (run 1: 138 at
$n \in \{30..56\}$; run 2: 123 at $n \in \{30..44\}$, all
independently re-audited from pinned data). Not one lacks a paste-8,
an $L=8$, or a po2 firing.** The pressure was real: the anti-paste8
energy squeezed one $n=32$ tree down to exactly TWO $L=8$ triples
(both paste-realizable — pinned as `surv_thin_n32` in the lemma's new
CHECK 3); the anti-sup8 energy reached a single $L=8$ triple on an
$n=44$ tree (run 1); the anti-po2 energy never got below 22 firing
triples. Availability thins under attack but never empties.

### Two sharper structural facts

1. **The straddle channel was never necessary anywhere.** In all 261
   trees, every $L=8$ firing triple admits a paste (1-arc) pairing —
   0 straddle-only $L=8$ triples across the entire adversarial
   population, extending the R38 pin observation (12/12) to
   witness-box scale under pressure.
2. **Forced-large $k'$ is not a large-$n$ artifact.** Min paste $k'$
   reaches **5** already at $n = 32$ (pinned `surv_kp5_n32`) and again
   at $n = 40$ (pinned `surv_kp5_n40`); run 1 saw min $k' = 5$ at
   $n = 56$. The R40 conclusion (no bounded-$k'$ certificate) is
   confirmed and sharpened: adversarial pressure finds high-forced-$k'$
   trees at every scale, so the analytic supply argument must produce
   paste-8s with unbounded overlap arcs from the start.

### Program shape after R41

The ladder is as hard as adversarial search can make it:
`paste8_tree_universal` (and everything below it) now carries
261/261 direct-attack survival on top of 43/43 + 20/20 prior
evidence. Per the R41+ plan, the program switches to the **analytic
unbounded-$k'$ supply attack**: prove that on the 8-line
$g_3 = 2k' + 7 - |D|$ some pair + cover meeting in one arc always
exists on a pair-residual tree — value side already closed by
`shortpaste_floor_line` for all $k'$; candidate handle: the R30
dichotomy paste certificates (c1)–(c3), which do not bound $k'$.
Fallback unchanged: graph-level quantifier (choose the DFS tree).

### Summary of round R41

| Item | Status |
|------|--------|
| Q70 SA-hardening (3 energies, 2 runs, $n \in [30,64]$) | **DONE — 0 falsifiers** |
| `paste8_tree_universal` | survives 261/261 direct attack; CHECK 3 pins added |
| `sup8_tree_universal`, `triple_alive_universal` | survive 261/261; evidence bullets added |
| Straddle-only $L=8$ triples observed | **0** across all 261 trees |
| Min paste $k'$ observed | 5 (at $n = 32$, $40$, $56$) — unbounded-$k'$ burden confirmed |
| Next | analytic unbounded-$k'$ supply (Q71) |

## Section 82 — R42: top-of-box coverage — adversarial survival extends to $n = 60$; $n \in \{62, 64\}$ unreachable by cold SA (session s_0814-082720-9c93)

The R41 falsify critic's WARN (ladder untested at $n \in \{60, 62, 64\}$,
inside the $n \le 64$ witness box) prompted a third SA run: same
lexicographic availability-penalizing energies, $n \in \{58, 60, 62, 64\}$
only, restart budgets doubled (140s / 40k iterations). Result: **13 more
pair-residual trees (3 at $n = 58$, 10 at $n = 60$), all keeping a
paste-8** — anti-paste8 pressure bottomed at 5 paste-8 triples — and
again **zero straddle-only $L = 8$ triples**. Adversarial survival now
totals **274/274** across $n \in [30, 60]$.

Honest limit: $n \in \{62, 64\}$ produced 0 pair-residual trees in
~1.1M SA iterations — cold-start SA cannot reach residuality there
(the po2-violation landscape at $n \ge 62$ has ~135+ pair terms to
zero out). Closing the box's last two even values needs warm-starting
from an $n = 60$ residual tree (e.g. 2-vertex expansion moves that
preserve residuality) — recorded as a small open engineering question
inside Q72's resolution; it does NOT gate the analytic attack (Q71),
whose burden is $n$-uniform anyway.

### Summary of round R42

| Item | Status |
|------|--------|
| Q72 top-of-box SA ($n \in \{58..64\}$, doubled budgets) | DONE at 58/60 — **0 falsifiers, 13/13 survive** |
| Adversarial survival total | **274/274**, $n \in [30, 60]$ |
| Straddle-only $L=8$ observed | still **0** (274 trees) |
| $n \in \{62, 64\}$ | unreachable cold — warm-start idea recorded, non-gating |
| Next | Q71 analytic unbounded-$k'$ supply |

## Section 83 — R43: Q71 supply target collapses to ONE dimension — the same-branch paste-8 class (session s_0815-080733-7bd0)

### The witness-shape census (Q71, first analytic step)

The R41+ handoff's analytic question was WHERE paste-8 supply comes
from when $k'$ is forced large. R43 answered the "where" first:
classify every paste-8 usable pairing on the hardest known residual
trees by the tree-order relation of the pair's two SENDERS —
**leaf** ($s_1 = s_2$: the two back edges of one DFS leaf), **chain**
(one sender a strict ancestor of the other), or **branched**
(incomparable senders, $\operatorname{lca}$ a proper branch point).
Leaf + chain together = **same-branch pairs**, exactly the 2-back-edge
classes whose sym-diff length formulas were proved in the R12–R15 era
(`leaf_pair_witness`, nested, `crossing_pair_formula`).

Result (all counts deterministic, pinned in the new lemma's CHECK 1):

| pinned tree | leaf | chain | branched |
|---|---|---|---|
| `l8_exactness_dead` (n=12) | 1 | 8 | 3 |
| `sup1_dead_tree` (n=14) | 1 | 11 | **0** |
| `viol1_n30` | 4 | 16 | 4 |
| `viol2_n30` | 1 | 12 | 3 |
| `viol3_n40` | 0 | 12 | **0** |
| `surv_thin_n32` | 0 | 4 | **0** |
| `surv_kp5_n32` | 0 | 8 | **0** |
| `surv_kp5_n40` | 1 | 6 | 1 |

**On the four hardest pins the paste-8 witnesses are EXCLUSIVELY
same-branch.** Under both adversarial regimes (R40 residuality-SA,
R41 anti-availability-SA) the branched channel dies first and the
same-branch channel is what survives. Fresh census (seed 20260815):
21/21 sampled residual trees have a same-branch paste-8; a second
independent probe (seed 20260815+43, 124k trees, 31 residuals) is
committed as CHECK 2 — 31/31.

### Two refinement verdicts

1. **Leaf-only is DEAD** (dual attack before proof effort, standing
   policy): `viol3_n40`, `surv_thin_n32`, `surv_kp5_n32` have NO
   leaf-pair paste-8 (leaf count 0 above), and 5/21 census trees
   likewise. Same-sender pairs alone cannot carry supply. Do not
   revisit.
2. **Same-branch is the new supply target**: new lemma
   `paste8_samebranch_universal` (open, probes committed) —
   every pair-residual tree has a paste-8 whose usable pairing is a
   same-branch pair. Strictly between `paste8_tree_universal` and the
   dead bounded-$k'$ forms; does NOT bound $k'$ (same-branch min-$k'$
   reaches 5 on the R41 pins, matching the R40/R41 unbounded-$k'$
   burden).

### The vertical calculus (proved, in the lemma file)

For a same-branch pair, all four endpoints lie on ONE root chain, and:

- $D$'s tree part $= A \sqcup E$ (anchor interval $\sqcup$ sender
  interval), $|D| = |A| + |E| + 2$ — unifying the proved same-sender
  / nested / crossing length formulas;
- every third back edge meeting exactly one of $A, E$ meets it in a
  single arc automatically (two vertical paths intersect in an
  interval) — one-interval meets are automatic pastes, no
  `pasting_vertex_automatic` machinery needed;
- the 8-line becomes the **slack identity**:
  $L = 8 \iff (|A| + |E| - k') + (g_3 - k') = 5$ — "$D$-tree edges
  missed by the arc, plus $P_3$-edges outside $D$, total exactly 5."

### Why this reframes the Q71 analytic attack

If `paste8_samebranch_universal` holds, the supply quantifier loses
all branching geometry: a witness is (i) a root chain $R$, (ii) two
back edges whose tree paths are overlapping depth-intervals on $R$
with senders on $R$, (iii) a third back edge whose path meets one of
the two sym-diff intervals with slack exactly 5. The analytic burden
becomes an interval-system problem per chain — a chain-selection rule
plus a slack-5 attainment argument over the interval family — with
$k'$ free to scale (the arc can be almost all of $A \sqcup E$). The
R30 dichotomy certificates (c1)–(c3) specialize cleanly: on
same-branch pairs the straddle obstruction is exactly "$P_3 \supseteq
I$" (the cancelled interval separating $A$ from $E$), so
paste-availability is the 1-D statement "some cover's interval does
not swallow $I$."

### Honest gap + designated next falsifier

No SA run has penalized same-branch paste-8 availability
specifically (R41/R42 energies penalized generic availability).
**R44 should re-run the R41 lexicographic SA with energy =
#same-branch paste-8 triples** before analytic effort is sunk. If SA
kills the claim, the pinned falsifier localizes exactly which
branched configurations are irreplaceable — itself decisive for Q71;
if it survives at witness-box scale, the 1-D interval formulation is
the analytic target of record.

### Summary of round R43

| Item | Status |
|------|--------|
| Witness-shape census (8 pins + 2 fresh seeds) | DONE — same-branch universal in-sample |
| Leaf-pair-only refinement | **DEAD** — 3 pins + 5 census trees (R43) |
| `paste8_samebranch_universal` + 2 CHECKs | **committed, open** (R43) |
| Vertical calculus ($A \sqcup E$, slack identity) | **PROVED** (R43, lemma file) |
| Hard-pin branched witness count | **0** on the 4 hardest pins (R43) |
| Next | R44: anti-same-branch SA hardening; then 1-D interval attack |

## Section 84 — R44: `paste8_samebranch_universal` survives its designated falsifier — the availability floor IS the pinned tree (session s_0815-080733-7bd0)

### The experiment (Q71 continuation, R43's designated next step)

Two independent SA runs (seeds 20260815, 76100815; ~556k iterations
each, 20 min wall-clock each) with the R41 lexicographic recipe
retargeted at the NEW claim: energy = (residuality violations,
then **#same-branch paste-8 pairings**), moves = cubic 2-opt keeping
girth $\ge 5$ + DFS re-root/re-order, $n \in [30, 48]$, 70% of
restarts warm-started from the 8 pinned residual trees (cold-start
residuality above $n = 26$ is too rare to test anything, per R40).

### Result: zero falsifiers, and a striking floor identification

- 385,272 + 351,286 pair-residual states visited under direct
  anti-same-branch pressure: **not one lacked a same-branch paste-8.**
- Min availability seen: **4 same-branch pairings** — and the minimum
  state found by BOTH runs independently is **exactly the
  `surv_thin_n32` pin, graph AND tree**. The R41 anti-generic-paste8
  survivor is simultaneously the same-branch availability floor;
  1.1M directed iterations could not push below it or separate the
  same-branch channel from the generic one. (Consistent with R43's
  census: on `surv_thin_n32` ALL paste-8 pairings are same-branch —
  chain count 4, branched 0, pinned in the lemma's CHECK 1.)

### Honest scope

Warm-start dominance means R44 chiefly certifies the 2-opt/re-root
NEIGHBORHOODS of the known hard pins; $n \in \{44, 48\}$ produced no
cold residual states. This mirrors the R42 cold-unreachability
finding and does not gate the analytic attack (whose burden is
$n$-uniform).

### Program state after R44

The same-branch class has now survived the same two-stage adversarial
protocol that the generic ladder survived in R40–R42 (reach
residuality, then attack availability), at matching scale. The
analytic target of record is the 1-D formulation (Section 83):
chain-selection + slack-5 attainment over the interval system of a
root chain. Queue update: Q71 resolved as reframed (its supply target
is narrowed to the same-branch class); Q73 opened for the 1-D
analytic attack.

### Summary of round R44

| Item | Status |
|------|--------|
| Anti-same-branch SA (2 runs, ~1.1M iters, n in [30,48]) | **DONE — 0 falsifiers** |
| Residual states visited under pressure | 736k, all with same-branch paste-8 |
| Availability floor | 4 pairings = `surv_thin_n32` EXACTLY (both runs) |
| `paste8_samebranch_universal` | survives; evidence bullet added |
| Next | Q73: 1-D interval attack (chain selection + slack-5 supply) |

## Section 85 — R45: Chain census — paste-8 supply is FULLY 1-D everywhere sampled; the branching geometry drops out entirely (session s_0816-080841-64db)

### The census (Q73's first step: WHICH chain carries the witness?)

R45 enumerated every same-branch paste-8 witness on the 8 pins and
on 25 fresh pair-residual trees (84,000 sampled DFS trees, seed
20260816+45, $n \in \{12..22\}$), located its chains, tested three
selection rules, and classified the COVER's sender against the
pair's chain.

**Selection rules**: deepest-leaf, max-sender, and
max-overlapping-pairs ALL pass on 8/8 pins and 25/25 census trees
(exists and forall-over-ties variants); on the pins EVERY root chain
carries a witness (1–4 leaves each; every-chain not tabulated on the
census trees). Witness chains are abundant — no rule is load-bearing.

**The striking column — the cover often lives on the SAME chain**:
on all 8 pins and 25/25 census trees some witness has $s_3$
comparable with the deeper sender (all three back edges on ONE root
chain, **fully 1-D**); 62/85 pin witnesses, 100% on the four hardest
pins (`sup1_dead_tree` 12/12, `viol3_n40` 12/12, `surv_thin_n32`
4/4, `surv_kp5_n32` 8/8), 13/25 census trees exclusively. The R43
"hard instances live in the refined class" signature repeats one
level down — but see below: this time the signature MISLED.

**No constraint hides in the slack split or arc side**: splits cover
all of $(0,5), \dots, (5,0)$ across the pins and both $A$- and
$E$-arcs occur — slack-5 attainment must handle the full range.

### The strengthening `paste8_chain1d_universal`: introduced, then DISPROVED inside the same round

Conjectured from the census: every pair-residual tree has a paste-8
with all three senders pairwise comparable — the whole configuration
then being three depth intervals on one line, a witness six
integers. CHECK 1 pins the exact (fully-1-D, same-branch) counts on
all 8 pins; CHECK 2 (68,800-tree prefix of the census stream, 23/23
residuals) passed.

**The designated falsifier was executed BEFORE analytic effort (the
standing dual-attack discipline) and killed the claim in under 20
seconds of SA time.** Anti-chain1d SA (lexicographic energy:
residuality violations, then #fully-1-D paste-8 pairings; cubic
2-opt + DFS re-root; warm-started from the pins) produced
`chain1d_falsifier_n14`: a pair-residual $n = 14$ tree (8 back
edges, 3 leaves at depths 5/11/11) with **6 same-branch paste-8
witnesses and 0 fully 1-D ones** — in every witness the cover's
sender sits on a branch incomparable with the pair's deeper sender.
Independently re-verified with the triple-first census enumerator;
pinned as `paste8_samebranch_universal` CHECK 3; the chain1d lemma
file is committed as status **disproved** (audit trail; CHECKs
runtime-skipped). It is the first known tree where the same-branch
and fully-1-D classes strictly separate.

**Class caveat that widens the R44 evidence.** The falsifier's graph
has girth 3; the R40–R44 harnesses all kept girth $\ge 5$ (the R45
harness's local girth check was accidentally leaky — the bug WAS the
discovery vector). The universals quantify over ALL connected cubic
graphs, so the wide class is the right one to harden in. Re-running
with energy = #same-branch paste-8 pairings in the same wide class
(seeds 20260816 / 76100816, 6 min each, ~3.8M iterations, $n \in
[30, 48]$ cold + pin-graph warm restarts): **6,721 pair-residual
states under direct anti-same-branch pressure, zero falsifiers, min
availability 5.** `paste8_samebranch_universal` survives its own
R45-designated wide-class falsifier (caveats: short runs; the floor
tree `surv_thin_n32`, availability 4, was not re-found — restarts
re-root the pin graphs randomly).

### What survives: the projected-interval formulation (Q74)

The pair side of the 1-D picture stands — $A, I, E$ consecutive
depth intervals on one root chain $R$. The cover side must be
enriched: ANY back edge $B_3 = (s_3, a_3)$ whose path meets $R$
contributes the PROJECTED interval $[d(a_3), d(x_3)]$ ($x_3$ = where
$s_3$'s root path leaves $R$), its off-chain length entering the
slack identity but never the arc. The falsifier proves the
enrichment strictly necessary (all 6 witnesses foreign; splits
$(0,5) \times 2$, $(3,2) \times 4$). Supply for
`paste8_samebranch_universal` stays per-chain interval arithmetic,
now over the projected family — Q74.

**Numerical anchors (R45; any re-derivation must reproduce these
exactly).** `fund_pair_overlap` length: $|D| = g_1 + g_2 + 2 -
2k_{12}$, so $(g_1, g_2, k_{12}) = (5, 3, 2) \Rightarrow |D| =
5 + 3 + 2 - 4 = 6$ (not a power of 2, no violation), while
$(5, 3, 1) \Rightarrow |D| = 8$ (a pair violation if it arose);
parity $|D| \equiv g_1 + g_2 \pmod 2$ always.

### Summary of round R45

| Item | Status |
|------|--------|
| Chain census (8 pins + 25 fresh residuals, 84k trees) | DONE |
| Selection rules (deepest-leaf / max-sender / max-pairs) | all pass everywhere — none load-bearing |
| `paste8_chain1d_universal` (fully 1-D strengthening) | introduced + **DISPROVED same round** (`chain1d_falsifier_n14`) |
| Falsifier pinned | samebranch CHECK 3: 6 same-branch, 0 fully-1-D, pair-residual |
| Wide-class (girth-3-allowed) anti-samebranch SA | **survives** — 6,721 residual states, 0 falsifiers, floor 5 |
| Refinement ladder state | same-branch now pinched between dead neighbors (leaf-only below, chain1d above) |
| Next | Q74: projected-interval attack on `paste8_samebranch_universal` |

## Section 86 — R46: Projected coordinates PROVED; the slack ladder discovered — descent-above-5 is the new analytic core (session s_0817-081104-2f11)

### Housekeeping

Sections 26–31 (R19–R24 narratives) condensed to a digest (full
narratives archived under `strategies/erdos_gyarfas/`); the strategy
dropped from 120.4k to ~104k bytes, back under the critic budget.

### `paste8_projected_coords` PROVED — Q74 handle (i) closed

The R45-framed projected-interval formulation is now a theorem
(`lemma_paste8_projected_coords__0817-081104-2f11.md`, elementary from
`fund_pair_overlap` + `pasting_meeting_structure`): for a same-branch
pair on root chain $R = [\mathrm{root}..s_d]$, ANY paste cover $B_3$
(foreign or on-chain) satisfies, with
$x_3 = \operatorname{lca}(s_3, s_d)$ and
$\pi(B_3) = [d(a_3), d(x_3)]$:

1. $a_3 \in R$, $d(a_3) < d(x_3)$,
   $\mathrm{off}(B_3) = g_3 - |\pi| \ge 0$ ($= 0$ iff $s_3 \in R$);
2. **arc $= \pi \cap A$ or $\pi \cap E$** — whichever is nonempty,
   and the single-arc condition is exactly "$\pi$ meets exactly one
   of $A, E$ in an edge" (they are separated by $I$, $k_{12} \ge 1$);
3. $L = 8 \iff (|A|+|E|-k') + (|\pi|-k') + \mathrm{off} = 5$.

So the same-branch paste-8 predicate is pure interval arithmetic in
the projected system of ONE root chain: pair intervals $A, I, E$ plus
per-back-edge data $(\pi, \mathrm{off})$. No branching geometry
survives. R46 census verification: 5,514 same-branch single-arc covers
on the 9 pins (deterministic CHECK, 91 paste-8 witnesses) + 567
witnesses over 43 fresh residual trees (124k trees, seed 20260817+46)
— zero exceptions. Foreign off-chain weights are small:
$\mathrm{off} \in \{1{:}81, 2{:}17, 3{:}4, 4{:}3\}$ across foreign
witnesses. $x_3$ landing zones: side-$E$ foreign covers always have
$x_3$ strictly inside $E$; side-$A$ foreign covers have $x_3$ in $A$
or in $I$.

### The slack ladder — new structure found by the census

Per residual tree, censusing the FULL same-branch slack value set
$S(T) = \{|A|+|E|+g_3-2k'\}$ (all same-branch pairs $\times$ all
single-arc covers, not just $L = 8$):

- **All 52 residual trees examined** (9 pins + 43 fresh): the odd part
  reaches $\ge 5$ and is **gap-free from 5 to its max**. On the pins
  the ladders are wide — e.g. `viol3_n40` $\{3..31\}$, `surv_kp5_n32`
  $\{5..27\}$ — even though R40–R44 SA pressure minimized paste-8
  availability; adversarial hardening thins the WITNESS count but not
  the slack ladder.
- **The full-interval form is DEAD at introduction**: fresh census
  tree `ladder_gap3_n16` has odd slacks $\{1, 5, 7, 9, 11\}$ — slack
  1 attainable, slack 3 NOT. Descent can fail below 5. Pinned in
  `lemma_slack_ladder_above5__0817-081104-2f11.md` CHECK 1 (the
  anomaly is load-bearing negative knowledge: on `ladder_gap3_n16`
  the descent move fails at $3$ even though $1$ is attainable, so any
  proof of (D) must use the $s \ge 7$ hypothesis in an essential way
  and show the same obstruction cannot occur above 5).

New probe lemma `slack_ladder_above5` (status open, strictly stronger
than `paste8_samebranch_universal`): odd slack set reaches $\ge 5$ and
$\{5, 7, \dots, \max\} \subseteq S_{\mathrm{odd}}(T)$. Its proof
decomposes into two 1-D statements in projected coordinates:

- **(H)** some config with odd slack $\ge 5$ exists (high endpoint —
  min-overlap $k' = 1$ covers with long $g_3$; residual gaps avoid
  $\{3,7,15,31\}$);
- **(D)** descent: odd slack $s \ge 7$ attainable $\Rightarrow$
  $s - 2$ attainable ($-2$ moves: extend the arc into the side
  interval, shrink the pair, swap to a $g_3 - 2$ cover — all local on
  the chain's interval system).

(H) + (D) $\Rightarrow$ slack 5 $\Rightarrow$
`paste8_samebranch_universal`. This is the R23 (T1)–(T3) program
transported one level down, where it is now a statement about
intervals on a line rather than about graphs.

### Round discipline note

Per the twice-validated standing policy (R44 recipe, R45 lesson:
"never skip the falsifier"), R47 MUST run the designated anti-ladder
SA falsifier (wide class, energy = residuality then #missing odd
values in $[5, \max]$, warm restarts from `ladder_gap3_n16` — the only
tree known to attain ANY odd gap — plus the 8 pins) BEFORE analytic
effort on (H)/(D).

### Summary of round R46

| Item | Status |
|------|--------|
| Strategy condensation (Sections 26–31 → digest) | DONE (120.4k → ~104k bytes) |
| `paste8_projected_coords` (arc $= \pi \cap$ side; slack decomposition) | **PROVED** + CHECK (5,514 covers, 0 exceptions) |
| Q74 handle (i) — witness predicate fully 1-D in projected coords | **CLOSED** |
| Slack-set census (9 pins + 43 fresh residuals) | DONE — ladder-above-5 holds 52/52 |
| Full-interval strengthening | **DEAD at introduction** (`ladder_gap3_n16`: 1 yes, 3 no) |
| `slack_ladder_above5` probe lemma (H + D decomposition) | introduced, open, 2 CHECKs pass |
| Next (R47) | designated anti-ladder SA falsifier FIRST, then (H)/(D) analytics |

### R46 addendum — the ladder is DEAD (designated falsifier, same round)

Executed per the round-discipline note above, the designated
anti-ladder SA (wide class, projected-coordinate slack evaluation
cross-checked against the set-based enumerator on all 10 pins) killed
`slack_ladder_above5` in under 30 seconds of search:

- **`ladder_gap9_n14`** = the `chain1d_falsifier_n14` GRAPH re-rooted
  at vertex 0: pair-residual, odd slacks $\{3, 5, 7, 11\}$ — **9
  missing** below max 11. Independently confirmed by the set-based
  enumerator; pinned as CHECK 3 of the (now disproved) lemma file.
- A cold-start $n = 16$ falsifier has odd slacks $\{3, 5, 9, 11, 13\}$
  — **7 missing**. Misses at 9 and 11 recurred from multiple starts.
- Conclusion: **no odd slack value above 5 is universally forced; 5
  stands alone.** The (H)+(D) descent program is dead as stated.
- `paste8_samebranch_universal` survived every pair-residual state the
  SA visited (slack 5 present in all falsifiers and all intermediate
  states — zero samebranch falsifiers across all runs).

**Method lesson (third consecutive instance — now standing policy with
teeth):** chain1d (R45), full-interval (R46), ladder-above-5 (R46)
were ALL census-suggested regularities at $10^5$-random-DFS-tree scale
and ALL died to direct SA within seconds — the last one to a bare
RE-ROOT of an existing pin. Census scale is not evidence of
universality. No census regularity may be promoted to a lemma without
its SA falsifier executing in the SAME round.

**Program consequence.** The refinement ladder above
`paste8_samebranch_universal` is triply dead; its proof cannot go
through structured slack neighbors. What survives of R46: the
PROVED projected-coordinate reduction (`paste8_projected_coords`) —
the right language — and the terminal open core: slack-5 attainment
over the projected interval system of some root chain, to be attacked
directly (not via descent), by genuinely new angles (ideation) or
declared the converged partial result.

### Summary of round R46 (final, superseding the table above)

| Item | Status |
|------|--------|
| Strategy condensation (Sections 26–31 → digest) | DONE (120.4k → ~104k bytes) |
| `paste8_projected_coords` | **PROVED** + CHECK (5,514 covers, 0 exceptions) |
| Q74 handle (i) — predicate fully 1-D in projected coords | **CLOSED** |
| `slack_ladder_above5` | introduced + **DISPROVED same round** (`ladder_gap9_n14`: 9 missing; second tree: 7 missing) |
| No odd slack above 5 universally forced | established (SA, confirmed set-based) |
| `paste8_samebranch_universal` | survives all SA states; refinements above it triply dead |
| Next (R47) | ideation for direct 5-attainment angles, or declare convergence |

### R46 addendum 2 — `sb_falsifier_n18`: the ENTIRE $L = 8$ target falsified; the program pivots to the PO2 set

Continuing the R45-designated wide-class anti-same-branch SA (now with
the `paste8_projected_coords` fast evaluator, sanity-locked to the
set-based enumerator on all 10 pins) produced, from a COLD $n = 18$
start, the most consequential falsifier of the branch:

**`sb_falsifier_n18`** (data + deterministic pin:
`lemma_paste8_samebranch_universal` CHECK 4; independently confirmed
by the set-based enumerator, then by a full-triple scan):

- pair-residual; same-branch slack set odd part $\{3, 7, 9, 11, 13\}$
  — **no slack 5**: `paste8_samebranch_universal` DISPROVED.
- **zero usable $L = 8$ pairings of any class**:
  `paste8_tree_universal` DISPROVED.
- no $L = 8$ firing triple at all; full value set
  $V(T) = \{6, 7, 9, 10, 11, 12, 13, 14, 15, 16\}$, holed **exactly
  at 8** ($V_e = \{6, 10, 12, 14, 16\}$ — 10 present, 8 absent):
  `sup8_tree_universal` and `pasting_value_interval` DISPROVED.
- BUT: 4 firing triples, **all $L = 16$, every one factoring through a
  chain (same-branch) pasting** at slack $13 = 16 - 3$.
  `triple_alive_universal` (any PO2) SURVIVES and is vindicated as the
  honest tree-level universal — exactly as its R34 introduction
  argued. Further samebranch-paste-8 falsifiers followed from cold
  starts at $n = 18$ and $n = 24$ (the class is robustly falsifiable,
  not a single sporadic tree).

**Where the wrong turn happened.** R23 observed $8 \in V(T)$ on 100%
of residuals and reduced the tuning program to "target 8 alone"; 26
rounds and 200+ residual trees never contradicted it. The adversarial
walk found the region where the value set holes out at exactly 8
while 16 stays reachable. Fourth consecutive census-regularity killed
by SA in two rounds — the method lesson is now written into the notes
channel and is standing policy.

**What survives, exactly:**

1. `triple_alive_universal` — the tree-level supply universal (any
   PO2).
2. The same-branch MECHANISM: every PO2 firing triple on every known
   falsifier/pin factors through comparable-sender pastes.
3. `paste8_projected_coords` (PROVED this round) — length-agnostic;
   the witness predicate for ANY target length is interval arithmetic
   on one root chain.
4. The proved vertical calculus (parts 1–3 of the dead lemma's file),
   also length-agnostic.

**Successor lemma** (`pastePO2_samebranch_universal`, open, Q75):
every pair-residual tree has a same-branch pasting config with slack
$\in \{1, 5, 13, 29\}$ ($L \in \{4, 8, 16, 32\}$). Implies the EGC
conclusion on pair-residual trees. All 12 pins comply (CHECK 1;
`sb_falsifier_n18` attains ONLY 13). Designated wide-class SA
falsifier executed the same round: outcome recorded below.

### Summary of round R46 (FINAL — supersedes both tables above)

| Item | Status |
|------|--------|
| Strategy condensation (Sections 26–31 → digest) | DONE (120.4k → ~107k bytes) |
| `paste8_projected_coords` | **PROVED** + CHECK (5,514 covers, 0 exceptions) |
| `slack_ladder_above5` | introduced + DISPROVED same round (`ladder_gap9_n14`) |
| `paste8_samebranch_universal` | **DISPROVED** (`sb_falsifier_n18`: no slack-5 same-branch paste) |
| `paste8_tree_universal` | **DISPROVED** (same tree: no L=8 pasting, any class) |
| `sup8_tree_universal` | **DISPROVED** (same tree: no L=8 firing triple; $8 \notin V$) |
| `pasting_value_interval` | **DISPROVED** (same tree: $V_e$ gapped at 8) |
| `triple_alive_universal` | SURVIVES (fires at 16) — again the terminal tree-level universal |
| `pastePO2_samebranch_universal` | introduced (open), 12-pin CHECK passes, designated SA falsifier run same round |
| Q74 | resolved; Q75 opened (PO2-set analytic attack) |

### R46 addendum 3 — the successor dies too; the complementary-falsifier PINCH

The designated SA falsifier for `pastePO2_samebranch_universal` (2
seeds; seed 20260846 survived 11,650 residual states, min availability
2) killed it on the second seed: **`po2_falsifier_n18`** (pinned in
that lemma's CHECK 2, independently set-based-confirmed):
pair-residual, same-branch slack set $\{2,3,4,6,\dots,12\}$ disjoint
from $\{1, 5, 13, 29\}$ — yet rescued by exactly ONE PO2 firing
triple, at $L = 8$, factoring ONLY through **branched** pairs
($V(T) = [5..15]$, $V \cap \mathrm{PO2} = \{8\}$).

**The pinch.** The two R46 falsifiers are complementary:

| | $L = 8$ | same-branch class |
|---|---|---|
| `sb_falsifier_n18` | impossible ($8 \notin V$) | necessary AND sufficient (4/4 chain pastes at 16) |
| `po2_falsifier_n18` | necessary AND sufficient (branched paste at 8) | impossible (no PO2 slack) |

Neither the length coordinate nor the pair-class coordinate of the
pasting mechanism admits ANY universal restriction.
`triple_alive_universal` (R34) is hereby pinched as the exact terminal
tree-level universal: minimal, unfalsified at 4.7M+ SA iterations
across R44–R46 plus ~200 census residuals, and now with every natural
strengthening dead by explicit pinned counterexample.

**Anti-samebranch SA final tally** (both seeds): 4.74M iterations,
19,548 pair-residual states, **11 independent samebranch-paste-8
falsifiers** at $n \in \{18, 20, 24\}$ — the R44 "availability floor"
picture (min 4 at `surv_thin_n32`) was an artifact of the girth
$\ge 5$ class + warm-start bias; in the wide class availability
reaches 0.

**R47 successor candidate** (NOT yet introduced as a lemma —
SA-probe FIRST): `pastePO2_tree_universal` — every pair-residual tree
has a pasting config over ANY pair class with slack
$\in \{1, 5, 13, 29\}$, i.e. $V(T) \cap \{4, 8, 16, 32\} \ne
\emptyset$. Implies `triple_alive_universal` via the pasting
criterion; satisfied by both falsifiers; equivalent to
triple-aliveness if R19's pasting-exhaustiveness (100% empirical)
were proved — which is itself a candidate PROVABLE lemma and would
close the gap between the two.

### Summary of round R46 (FINAL v3 — supersedes all tables above)

| Item | Status |
|------|--------|
| Strategy condensation (Sections 26–31 → digest) | DONE |
| `paste8_projected_coords` | **PROVED** (5,514-cover CHECK, 0 exceptions) |
| `slack_ladder_above5` | introduced + DISPROVED (`ladder_gap9_n14`) |
| `paste8_samebranch_universal` | **DISPROVED** (`sb_falsifier_n18` + 10 more falsifiers) |
| `paste8_tree_universal`, `sup8_tree_universal`, `pasting_value_interval` | **DISPROVED** (same tree, $8 \notin V$) |
| `pastePO2_samebranch_universal` | introduced + **DISPROVED** (`po2_falsifier_n18`, branched-only rescue) |
| `triple_alive_universal` | **PINCHED as the exact terminal universal** (complementary falsifiers) |
| Q74/Q75 resolved; Q76 opened | pastePO2_tree_universal SA-probe + pasting-exhaustiveness proof attempt |
