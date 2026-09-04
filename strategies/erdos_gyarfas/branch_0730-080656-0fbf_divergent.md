# Branch archive: erdos-proof/0730-080656-0fbf — divergent narrative (R57–R66 of that branch's numbering, sessions s_0823 through s_0829)

Preserved at merge time (2026-09-04): this branch diverged from the
s_0822 close and ran the fractional-certificate / girth-9 / stratum-
exhaustion line in parallel with the criticality/supply line that
became master. Its sessions after s_0825 never ran session_end, so
these sections exist only here. proof_strategy.md conflict resolved
per the documented rule (newest session_close wins = s_0904).

## Section 97 — R57: ideation restart — the fractional-certificate program (Q80) opens; carrier-A's 8-cycle sub-tally corrected (session s_0823-080606-3598)

### Ideation (5 lens-locked proposers + judge, per the R56 closure directive)

Five parallel proposers (sieve/density, weight-redistribution, entropy,
extremal/stability, counterexample-first) ran against the closure
record; a judge ranked them. Outcome (full digest in the notes channel):

- **Q80 opened (rank 1, 35/40 + rank 2, 33/40 merged): the fractional
  starvation program** — this section and the two new lemma files.
- **Q81 opened (rank 3, 32/40): the girth-9 stratum witness hunt** at
  $n = 58$–$64$, the first regime where $c_4 = c_8 = 0$ is provably
  achievable (the (3,9)-cages at $n = 58$ sit INSIDE the witness box)
  and was never searched. First lemma `L-g9c16`: every cubic
  $\{C_4, C_8\}$-free graph on $58 \le n \le 64$ vertices contains a
  $C_{16}$ — falsification IS a candidate witness one $C_{32}$-check
  away.
- **Benched, not queued (31/40): triangle-pocket integral discharging**
  (P2) for the $c_8 \le 1$ integral core; its probes PROVED the qa24 L2
  block is a pure integrality gap (fractional cotree 5-covers feasible
  by Frank-Wolfe; integral UNSAT by R55 CEGAR) and that uniform charge
  counting has 28–40% slack on every carrier. Lemma candidate
  `tri7_blocks_qa24` needs an out-of-block exact SAT before opening.
- **Rejected (23/40): entropy/load-distribution** — its top-$m$-mass
  quantity IS the uniform counting dual $y \equiv 1$, already
  strengthened past by dual ascent; recorded to prevent re-proposal.

### The two new lemmas (Q80's opening move, both CHECK-validated)

**`lp_dual_8cycle`** (L1 layer): an integer weighting $y \ge 0$ on the
8-cycles with $\mathrm{top}_m(w_y) < 5\sum y_c$ is a 3-line proof that
no $m$-subset 5-covers the 8-cycle system — the fractional refinement of
the DEAD integer packing bound (dead-end #8, $\nu \le 2$, never fired).
Live evidence: fires on 4/4 pinned $n \ge 20$ carriers (three uniform,
`qa_grow_n22` via ascent $y = (1,2,1,1,1)$) and 36/36 random
exactly-infeasible instances at $n = 18$; zero integrality gaps
observed. Open content: the no-gap CONVERSE at $n \le 22$. Theorem
shape: max edge-load $d$ and $c_8 > d\,m/5$ $\Rightarrow$ uniform dual
fires $\Rightarrow$ no quad-dead state — "L1 needs $c_8$ collapse" with
explicit constants.

**`frac_starvation_l1pass`** (L2 layer, $c_8 \ge 2$ stratum): with
$\Lambda(G)$ the value of the mixed packing LP (weight 5 per PO2 cycle,
weight 1 per cycle $\le 7$, per-edge load $\le 1$), weak duality gives:
$\Lambda(G) > m$ $\Rightarrow$ no 5-cover is a cotree $\Rightarrow$ no
quad-dead state. Claim: every C4-free 5-coverable cubic $G$ with
$c_8 \ge 2$ has $\Lambda(G) > m$. Pinned rational certificates: QA22
carrier $5\nu^* = 25/2 > 12$; the R56 $n=26$ L1-pass $57/4 > 14$ with
triangle weights $1/4$–$5/8$ on 7 of 8 triangles (R56's "triangle
starvation" now explicit dual data); three fresh subdivision-children
L1-passes at $\Lambda \ge 103/7, 59/4, 103/7 > 14$. Boundary fact
making the hypothesis sharp: $\Lambda(\text{QA24}, c_8{=}1) = 167/14 <
13$ — the $c_8 \le 1$ block is genuinely integral, no LP certificate
exists there (consistent with, and jointly discovered by, the benched
P2 probes).

### Correction to an R55 sub-tally (re-audited independently this session)

Section 95 states "the 8-cycle subsystem is already un-5-coverable for
14 of the 15 carriers" with the lone exception the $(c_8, N) = (7,139)$
carrier at $n = 20$. This is WRONG about carrier A
(`ta_falsifier_warm_n18`, $n = 18$, $c_8 = 3$, $N = 67$): its 8-cycle
subsystem IS 5-coverable within $m = 10$ — the 10-edge cover pinned in
`lemma_lp_dual_8cycle`'s CHECK hits all three 8-cycles exactly 5 times
(re-verified from scratch this session). There are therefore at least
TWO carriers whose L1 obstruction is NOT in the 8-cycle layer alone.
The R55 THEOREM is unaffected: full-system (8+16) un-5-coverability of
all 15 carriers was proved by SAT + the stdlib DP (CHECKs 7–8 of
`lemma_quad_alive_universal`, still passing), and adding 16-cycle
constraints only strengthens infeasibility. What the correction changes
is the MECHANISM story at carrier A: its obstruction needs 16-cycle
weights (the mixed LP of `frac_starvation_l1pass`), not 8-cycle
counting alone.

### The program map after R57

- L1, 8-cycle-rich stratum: `lp_dual_8cycle` counting duals (validated,
  no-gap conjectured at $n \le 22$).
- L2, $c_8 \ge 2$ stratum: `frac_starvation_l1pass` mixed LP
  certificates (validated on every instance tried; next: exact LP over
  all 61 R56 L1-passes to map the survivor family — any $\Lambda \le m$
  instance falsifies).
- $c_8 \le 1$ integral core: benched P2 (integral slot discharging) —
  the sharply-defined residual where EGC-relevant hardness sits.
- Disproof flank: Q81 girth-9 stratum (independent of all the above).

## Section 98 — R58: `frac_starvation_l1pass` DISPROVED by its designated falsifier sweep — the integral obstruction dominates the organic family (session s_0823-080606-3598)

### The sweep (Q80's first falsifier, run same-day as the lemma opened)

All 630 double-subdivision children of QA24 were regenerated and
adjudicated exactly (the census matches R56's growth-children row
exactly: 550 C4-excluded, 30 L1-infeasible, 50 L1-passes — 46 with
$c_8 \ge 2$, 4 exempt). Every L1-pass with $c_8 \ge 2$ got an exact
$\Lambda$ verdict: float LP first, then EXACT rational simplex
(Bland's rule, Fraction arithmetic, 39-row tableau) on every child the
float dual could not push above budget.

**Result: 27 of 46 are certified $\Lambda > 14$; 19 of 46 have exact
optimum $\Lambda < 14$.** The lemma's conclusion fails on 19 members of
its own hypothesis class. Two falsifiers are pinned in the lemma file
with complete self-contained certificates — an explicit 14-edge 5-cover
(the hypothesis) plus an explicit rational dual edge-cover with sum
$27/2$ resp. $736/53 < 14$ (the refutation, via weak duality — no
simplex trusted). Falsifier $c_8$ values: $\{2{\times}9, 3{\times}8,
4{\times}2\}$; certified: $\{3{\times}2, 4{\times}11, 5{\times}7,
6{\times}5, 8{\times}2\}$. The overlap at $c_8 \in \{3, 4\}$ means NO
$c_8$ threshold rescues the claim.

### What the falsification teaches (the corrected L2 landscape)

1. **The integral obstruction is dominant, not marginal.** R57's
   boundary picture ($\Lambda(\mathrm{QA24}) = 167/14 < 13$ making
   $c_8 \le 1$ the "integral core") was wrong in scope: 19/46 (41%) of
   the organic $c_8 \ge 2$ L1-pass family ALSO has $\Lambda \le m$ —
   the L2 block there is a pure integrality gap, invisible to every LP
   certificate. All 19 are quad-death-free regardless (they are among
   R56's 61 CEGAR-certified L1-passes), so no quad-dead candidate
   emerges; what died is the LP EXPLANATION, not the block.
2. **The LP mechanism is real but partial**: 27/46 organic children +
   QA22 (L1 layer, $5\nu^* = 25/2 > 12$) + the pinned R56 $n=26$
   L1-pass carry exact transferable certificates. $\Lambda$ clusters
   ($442/33$, $27/2$, $68/5$, $125/9$, $139/10$, $95/7$, $736/53$ on
   the falsified side; $29/2$–$31/2$ on the certified side) suggest a
   small set of binding dual shapes — the refined question is what
   invariant separates the two subfamilies. That takes a NEW lemma id
   (ledger rule) once a candidate invariant exists.
3. **Ideation P2 (triangle-pocket integral discharging) is PROMOTED**:
   the integral mechanism it targets is now the main phenomenon on the
   organic family. Its bench condition (an out-of-block exact SAT for
   `tri7_blocks_qa24`) is the natural next Q80 deliverable.

### Q81 progress (parallel, computational)

The girth-9-stratum SA hunt confirmed the stratum is trivially
reachable ($c_4 = c_8 = 0$ within seconds at $n \in \{58, 62\}$, single
restart) and that C16 elimination is the real fight: 40-minute anneals
plateau at $c_{16} = 95$ ($n = 58$) and $102$ ($n = 62$) — supporting
`L-g9c16` (no witness; the lemma file with its falsification CHECK is
the next Q81 deliverable). $n = 64$ run pending.

## Section 99 — R59: Q81's first lemma opens — `g9c16_stratum`, with the stratum-reachability discovery pinned (session s_0823-080606-3598)

`lemma_g9c16_stratum` (NEW, open): every connected cubic graph on
$58 \le n \le 64$ vertices with no $C_4$ and no $C_8$ contains a
$C_{16}$. Falsification = a candidate EGC witness one $C_{32}$-check
away; proof = any cubic counterexample is pushed above the 64-vertex
witness box. The session's discovery that motivates it: the
$\{C_4, C_8\}$-free cubic stratum — never reached by any prior hunt
($c_8 > 0$ everywhere at $n \le 28$; algebraic families all screened
out) — is TRIVIALLY reachable at $n \ge 58$ (SA hits $c_4 = c_8 = 0$
in seconds; $O(1)$ expected short-cycle counts make the constraint
load scale-free), and inside it $c_{16}$ anneals to a plateau of
95–102 at $n \in \{58, 62\}$ without approaching 0. C16 is the
binding layer of the witness question; the stratum anchor (a pinned
$n = 58$ member with $c_{16} = 1250$) is CHECK-verified in the lemma
file. Campaign infrastructure notes (argbest storage, cage seeding)
recorded there too.

## Section 100 — R60: the R59 plateau falls — argbest-stored SA reaches $c_{16} = 37$ at $n = 58$; the floor is a robust 2-opt local minimum with diffuse 16-cycle load (session s_0825-081126-3d4c)

R60 re-ran the Q81 stratum campaign with the two fixes R59 itself
prescribed: **store the argbest** (R59 only tracked its value) and
**restart-rich schedules**. Four primary 35-minute anneals (exact
incremental $c_{16}$ delta-counting with distance-pruned per-edge path
enumeration, audited against a full recount at every argbest save and
every 1500 accepted moves — zero drift across the campaign, $\approx
4.8$M proposals / 46k accepts) plus three 20-minute basin-hop reheats:

- $n = 58$, fresh restart: $c_{16} = \mathbf{37}$ — the R59 "plateau"
  of 95 was a schedule artifact. The full descent $1250 \to 37$
  happened inside the first 93 seconds (hot phase); the run then froze.
- $n = 58$, second fresh restart: 112 (restart variance is large);
  seeded from the R59 anchor: 80 (anchor seeding does not beat a good
  fresh restart).
- $n = 62$, fresh restart: 88 — sub-plateau descent confirmed at a
  second scale.
- Three reheats ($T_0 = 4$) from the 37-graph: all returned 37. The
  value is a genuine local minimum of the 2-opt move class, not a
  cooling artifact.

Structure of the 37-graph (pinned with an explicit 16-cycle in
`lemma_g9c16_stratum` CHECK 2; verified from scratch: cubic, connected,
$c_4 = c_8 = 0$): **girth 3** — every low-$c_{16}$ argbest is
triangle-rich, since odd and 6-cycles are free in this problem; the
descent moves AWAY from the girth-9/cage corner, demoting the
cage-seeding prong. The surviving 37 16-cycles are **diffuse**: 85 of
87 edges carry at least one, max per-edge load 13. There is no small
edge core whose surgery kills the residue — consistent with the
R55–R58 finding that the binding obstruction is global-integral, not
local. The live witness verifier rejects the 37-graph in $\sim 1$ ms
citing its 16-cycle; a $c_{16} = 0$ stratum graph would proceed
directly to the $C_{32}$ check.

**Where this leaves Q81.** The gap between the 2-opt floor (37) and a
witness (0) is now the quantitative core of the lemma. Either
$\min c_{16} = 0$ somewhere in the box — richer move classes (triangle
rotations / 3-opt), $n \in \{60, 64\}$, or C16-edge-targeted proposals
could find it — or the floor is real and the right attack is an exact
lower bound: LP over the cycle space of the stratum, or SAT-UNSAT for
"$c_{16} < k$" at small $k$, which at $k = 1$ IS the lemma. Cage
repositories (houseofgraphs.org, aeb.win.tue.nl, users.cecs.anu.edu.au)
are egress-blocked from this container; prong (i) remains unfetched —
and the girth-3 finding suggests it matters less than R59 assumed.

## Section 101 — R61: the 37 floor is move-class-robust — 3-opt + load-targeted proposals do not move it; the floor RISES with $n$ (58: 37, 60: 65, 62: 88), so $n = 58$ is the binding scale (session s_0825-081126-3d4c)

R61 asked the sharp follow-up to R60: is $c_{16} = 37$ a 2-opt
artifact? The harness was extended with (a) **3-opt moves** (remove
three pairwise vertex-disjoint edges, rewire a random alternative
perfect matching on the six endpoints; 40% of proposals) and (b)
**load-targeted proposals** (half the moves pick the first removed edge
as the max-$N_{16}$ of four random candidates), with exact incremental
counting generalized to "16-cycles through $\ge 1$ edge of a set" by
telescoped banned-edge path counts (validated: summing over all 87
edges reproduces $c_{16} = 37$ exactly).

- Three 25-minute runs from the 37-graph ($T_0 = 3$, seeds
  201/202/203): **all returned 37** — $\approx 1.92$M proposals,
  15.7k accepts, zero improvements. Combined with R60's three reheats,
  the floor now survives $\{$2-opt, 3-opt, load-targeted$\}$ local
  search from six independent schedules.
- A fresh full-pipeline run at $n = 60$ with the v2 move class:
  $c_{16} = 65$ (girth 3, max edge load 33, verified from scratch;
  record in the R61 JSON). Best-known floors now: $n = 58$: **37**,
  $n = 60$: **65** (single restart), $n = 62$: **88** (single restart).

The floor *rising* with $n$ — despite the stratum getting roomier — is
the second structural surprise (after girth 3). More vertices means
more 16-cycles to kill, and the constraint density does not thin: the
witness box's binding scale is exactly $n = 58$, the (3,9)-cage number.
Local search has saturated; the honest next attacks are exact:
(i) SAT-UNSAT for "a $\{C_4, C_8, C_{16}\}$-free connected cubic graph
on 58 vertices exists" — which at UNSAT *is* `lemma_g9c16_stratum` at
$n = 58$, and at SAT is a candidate witness one $C_{32}$-check away;
(ii) an LP/counting lower bound on $c_{16}$ over the stratum;
(iii) structured constructions (voltage-graph lifts with forbidden
cycle lengths) instead of unstructured annealing.

## Section 102 — R62: the structured-constructions screen — 9,889 algebraic cubic graphs across the box, 4,062 stratum members, and none within 10x of the SA floors; symmetry itself is a $c_{16}$ obstruction (session s_0826-080904-9561)

R62 executed prong (iii) of the R61 exact-attack menu: an exhaustive
screen of the classical algebraic cubic families over the whole witness
box $n \in \{58, 60, 62, 64\}$ — generalized Petersen $GP(m,k)$,
I-graphs $I(m,j,k)$, Haar graphs (cyclic theta-lifts,
$u_i \sim w_{i+t}$, $t \in \{0,a,b\}$), circulant Cayley graphs of
$\mathbb{Z}_{2m}$ ($S = \{a, -a, m\}$), dihedral Cayley graphs of
$D_m$ ($S = \{r^a, r^{-a}, r^b s\}$; the three-reflection sets coincide
with Haar), and cyclic voltage lifts of $K_4$ over $\mathbb{Z}_{15}$
and $\mathbb{Z}_{16}$ ($n = 60, 64$). 9,889 valid (simple cubic
connected) graphs; every stratum member got an exact $c_{16}$ count.

Findings:

1. **$GP$, I-graphs, circulants, and dihedral mixed Cayley graphs
   contribute ZERO stratum members** anywhere in the box — every single
   one carries a 4- or 8-cycle. The classical "nice" families are
   structurally locked out of the stratum.
2. **Haar graphs flood the stratum but at high $c_{16}$**: 654 members
   across the four scales, girth locked at 6, and $c_{16}$ *quantized
   into just a few orbit-multiples per scale* (at $n = 58$: exactly two
   values, 2552 and 2697, an 84/84 split over 168 members). Range over
   all scales: $[2232, 2970]$ — two orders of magnitude above the SA
   floors (37/65/88).
3. **$K_4$-lifts are the best structured family and still 6x off**:
   3,408 stratum members at $n \in \{60, 64\}$, girths 3–9, minimum
   $c_{16} = 405$ at $K_4$-lift$(\mathbb{Z}_{15}; 0,1,3)$ and 416 at
   $\mathbb{Z}_{16}$ — versus the SA floor 65 at $n = 60$. Notably the
   lowest-$c_{16}$ lifts have girth 3, replicating R60's girth-3
   discovery inside an algebraic family.
4. **$n = 58$ is structurally thin**: $58 = 2 \cdot 29$ with 29 prime
   admits only 2-vertex-base cyclic lifts (= bicirculants; Haar +
   I-graphs exhaust the cubic ones), so the best structured $c_{16}$ at
   the binding scale is Haar's 2552 — 69x the SA floor.

The mechanism reading: cyclic symmetry quantizes $c_{16}$ into
orbit-size multiples, so any vertex-transitive-ish member sits on a
coarse lattice far from 0 — symmetry is not a route to a witness but an
obstruction. This kills prong (iii) as a witness hunt (though not as a
lower-bound tool) and sharpens the SAT prong: the witness, if it
exists, is asymmetric, girth-3-rich, and diffuse — exactly the object
local search already reaches better than algebra does. Screen harness:
scratchpad `q81_structured.py` (reconstructable: families as above,
root-min DFS cycle counts); results JSON `q81_structured_results.json`;
the two family-minimal graphs are pinned by construction in
`lemma_g9c16_stratum` CHECK 3.

## Section 103 — R63: the frontier moves toward $n = 32$ (conditional on F7a) — 2026 literature extends F3, the stratum is reachable at the frontier scales, and the floor profile is U-shaped over the box (session s_0826-080904-9561)

Three developments, one reframe.

**1. Literature (WebSearch this session; full citations in the notes
channel).** (a) arXiv:2608.02675 (Tranquilli, Aug 2026): a certified
exhaustive computation shows every simple cubic **bipartite** graph on
$\le 58$ vertices contains a $C_4$, $C_8$, or $C_{16}$; cubic bipartite
EGC counterexamples need $\ge 60$ vertices. The BIPARTITE half of
`lemma_g9c16_stratum` at $n = 58$ is therefore literature, and the open
content of the lemma at $n = 58$ is exactly the non-bipartite stratum.
Our R62 Haar data (every bipartite stratum member found had girth 6,
$c_{16} \ge 2232$) sits consistently inside their theorem. (b) Reported
in 2608.02675's citation context: a 2026 SAT-modulo-symmetries
computation excluding ALL minimum-degree-3 graphs through order 31. We
could not fetch the primary source (egress proxy), so this is
CONDITIONAL (F7a): the unconditional witness box stays F3's
$n \in [30, 64]$, conditionally sharpened to $[32, 64]$; either way the
frontier scales are $n \in \{30, 32\}$, and at both, $C_{32}$-freeness
is free ($n < 32$) or means non-Hamiltonicity ($n = 32$). (c)
arXiv:2605.22844 (the F3 preprint): $\ge 4/7$ of a minimal
counterexample's vertices have degree exactly 3, every vertex is
adjacent to a degree-3 vertex, and every regular minimal counterexample
is cubic.

**2. SA at the frontier scales — the stratum is reachable at $n = 30$
and $n = 32$.** The reconstructable 2-opt harness (scratchpad
`q81_sa30.py`: double-edge-swap Metropolis, lexicographic
$100c_4 + c_8$ phase 1, exact telescoped through-edge deltas audited
every 5000 proposals, stratum-preserving pre-filter before any $L = 16$
work in phase 2) reached $c_4 = c_8 = 0$ from fresh random starts at
BOTH frontier scales — $n = 30$ at $\sim$1.5M proposals and $n = 32$
twice (seeds 1 and 7, $\sim$1.2M proposals each). Prior cross-branch
data had the stratum unreached anywhere below 58 (R56: $c_8 > 0$
everywhere at $n \le 28$); reachability at 30/32 was open. Phase-2
$c_{16}$ descent floors this session: $n = 30$: **210**; $n = 32$:
**317** (entry 539, one continuous schedule; a second seed entered at
456 and froze — argbest-seeded reheats at $T_0 \in \{0.8, 3\}$ did not
move either floor, matching R60's observation that fresh continuous
descents beat seeded restarts).

**3. The floor profile over the full box is U-shaped, not
monotone.** Best-known SA floors now: $n = 30$: 210, $n = 32$: 317,
$n = 58$: 37, $n = 60$: 65, $n = 62$: 88. R61's "floors rise with $n$"
was the right half of a U: at the small end the stratum is cramped and
$c_{16}$ is forced high; the dip is at $n = 58$. Two readings: the
witness-hunt's best scale remains $n = 58$ (with the lemma's open part
now non-bipartite only), while the *proof* target at the frontier
($n \in \{30, 32\}$, floors 210/317, with SMS-grade exhaustion reported
one scale below — F7a, conditional) looks closest to closable. IF F7a
holds, the $n = 30$ floor 210 is a calibration point: $\min c_{16} > 0$
is then PROVEN there, so a robust SA floor of ~200 over a true positive
minimum is the expected signature of a scale where the lemma-analogue
holds, and observing the same signature at 32 (317) weakly suggests
$n = 32$ is not the witness scale either. Unconditionally, both floors
are just SA local minima over nonempty strata.

**4. SAT CEGAR at three scales — labeled-cycle bans do not converge at
box scales.** Harness `q81_sat.py` (exact-3 seqcounter degrees, ALL
labeled $C_4$s banned statically — 3$\binom{n}{4}$ clauses, $N(0) =
\{1,2,3\}$ symmetry, CEGAR bans for 8/16/(32)-cycles + connectivity
cuts, clause checkpoints for cross-session resume): $n = 30$
($\{4,8,16\}$): $\sim$3,000 rounds / 2.0M ban clauses, models persist at
$c_8 \approx 10\!-\!20$, $c_{16} \approx 500\!-\!800$; $n = 58$ lemma
config: 1,350+ rounds / 1.7M bans, same plateau; $n = 32$ frontier
config ($\{4,8,16,32\}$): 2,175+ rounds / 1.8M bans, model $c_{16}$
dipped to $\approx 400$ mid-run without approaching 0. Conclusion:
labeled-cycle CEGAR without isomorph-aware pruning is not the exact
technology for any scale in the box — the SMS framework (symmetry
breaking inside the solver) that closed order $\le 31$ is the tool to
port; our checkpointed ban sets can seed it.

**Queue.** Q81 is released: its SA prong was saturated in R60–R61, its
structured prong killed in R62, its CEGAR prong measured non-convergent
here; the LP/counting lower-bound prong remains open inside Q81's
released summary. NEW Q82: decide the frontier scales
$n \in \{30, 32\}$ — port SMS-style
isomorph-free exhaustion for $\{C_4, C_8, C_{16}\}$-free cubic (then
min-deg-3) at orders 30 and 32, or find a witness there; exhaustion
at 30 also settles F7a's content for our box unconditionally. CHECK 4
pins both frontier stratum graphs.

## Literature annotations F4–F7 — NOT ledger facts, NOT premises (sessions s_0826-080904-9561; R62 + R63; reframed R66)

The problem ledger `proofs/erdos_gyarfas.json` is frozen for the branch
and consists of F1–F3 ONLY. The items below are literature
ANNOTATIONS recorded for attribution and future-session context. They
are NOT given_facts, and — as of the R66 audit — **no lemma status, no
CHECK block, and no statement this document claims as proved uses F4,
F5, F6, or F7 as a premise.** Specifically: stratum nonemptiness at
$n = 58$ (F4's one former use, Section 99) is established in-house by
the explicit $c_4 = c_8 = 0$ graph pinned in `lemma_g9c16_stratum`
CHECK 2; F5 is a motivating heuristic with every reachability claim
established constructively by pinned runs; F6 and F7 are recorded
expectations whose only role is framing (the frontier scales are
$\{30, 32\}$ with or without them — and R67's in-house exhaustion at
$n = 30$ is replacing even that framing use). Deriving any conclusion
from F4–F7 would be a scope error; the annotations stay in the
document solely so future sessions know these results exist and where
they came from.

- **id: F4_cage_order_58**
  - statement: The smallest cubic graphs of girth 9 have exactly 58
    vertices, and there are exactly 18 of them ((3,9)-cages).
  - sign_disambiguation: Existence statement about girth-9 cubic graphs;
    implies the {C4, C8}-free cubic stratum is NONEMPTY at n = 58. Says
    nothing about C16.
  - citation: G. Brinkmann, B. D. McKay, C. Saager, "The smallest cubic
    graphs of girth nine", Combin. Probab. Comput. 4 (1995) 317-330.
  - warns: Used only for stratum nonemptiness at n = 58 and the phrase
    "the (3,9)-cage number"; no other cage property is used (R60 showed
    the low-c16 region is girth 3, away from the cage corner).
- **id: F5_poisson_short_cycles**
  - statement: In a uniform random cubic graph the numbers of k-cycles
    (k fixed) converge to independent Poisson variables with means
    2^k/(2k); expected c4 = 2 and c8 = 16 are O(1) constants.
  - sign_disambiguation: Heuristic-only asymptotic; NOT a bound for any
    fixed n and NOT conditioned on the stratum.
  - citation: B. Bollobas, European J. Combin. 1 (1980) 311-316;
    N. C. Wormald, J. Combin. Theory Ser. B 31 (1981) 168-182.
  - warns: Motivates stratum reachability by annealing only; the
    reachability claims are established constructively by the runs
    (CHECK 1, CHECK 2, CHECK 4 pin witnesses). No proof step depends on
    this fact.
- **id: F6_tranquilli_bipartite_58**
  - statement: Every simple cubic BIPARTITE graph on at most 58 vertices
    contains a cycle of length 4, 8, or 16; hence any cubic bipartite
    EGC counterexample has at least 60 vertices.
  - sign_disambiguation: POSITIVE partial result for a restricted class
    (cubic AND bipartite AND n <= 58). Using it for non-bipartite
    graphs, non-cubic graphs, or n >= 60 is a scope error.
  - citation: J. Tranquilli, "A 60-Vertex Lower Bound for Cubic
    Bipartite Counterexamples to the Erdos-Gyarfas Conjecture",
    arXiv:2608.02675 (August 2026). Certified exhaustive computation;
    two independently implemented C16 oracles.
  - warns: Proves exactly the bipartite case of lemma_g9c16_stratum at
    n = 58; the lemma's remaining open content at n = 58 is the
    non-bipartite stratum. Provenance is the arXiv listing via search
    (PDF not fetchable through the egress proxy).
- **id: F7_sms_order31_and_predominant_cubicity**
  - statement: (a) CONDITIONAL (primary source unfetched; see
    citation): a 2026 SAT-modulo-symmetries computation reportedly
    excludes all minimum-degree-3 graphs through order 31 (no
    power-of-2-cycle-free such graph on <= 31 vertices), which would
    raise F3's floor from 30 to 32. The unconditional baseline used by
    every proof step in this document remains F3's n >= 30. (b) arXiv:2605.22844 additionally shows: at least 4/7 of the
    vertices of any minimal counterexample have degree exactly 3, every
    vertex is adjacent to a degree-3 vertex, and every regular minimal
    counterexample is cubic.
  - sign_disambiguation: (a) is a POSITIVE exhaustion result; (b) are
    constraints on a HYPOTHETICAL counterexample — neither asserts a
    counterexample exists.
  - citation: (a) cited within arXiv:2608.02675 (primary PDF not
    fetchable through the egress proxy — provenance is the search-index
    summary; conservative fallback is F3's n >= 30, which changes no
    round conclusion in this session beyond the framing of Q82).
    (b) "Every Minimal Counterexample to the Erdos-Gyarfas Conjecture is
    Predominantly Cubic", arXiv:2605.22844 (May 2026) — quantitative
    extension of the F3 summary.
  - warns: (a) is load-bearing NOWHERE unconditionally — it only
    sharpens the framing of Q82 (the frontier scales are {30, 32}
    either way) and, IF it holds, certifies the n = 30 SA floor 210
    sits above a proven-positive minimum. Treat every '[32, 64]' in
    Section 103 as conditional shorthand.

**Internal-consistency note (R63, addressing the internal critic).**
Triple-deadness (Section 95: every cotree cycle carries >= 4 cotree
edges) never implied c8 = 0 anywhere in this document: carrier A
(Sections 87, 91) is triple-dead WITH c8 = 3 — its three 8-cycles each
sit at cotree depth >= 4, which is exactly what triple-deadness asserts.
No section uses "triple-dead implies c8 = 0"; Section 95's covering
reframing depends only on the depth reading.

## Section 104 — R64: the NB-moment probe kills the spectral-LP prong at the frontier scales — banned-length walk mass is theta/dumbbell, not cycle (session s_0828-080832-67a3)

Q82's released predecessor (Q81) left an "LP/counting lower bound on
$c_{16}$" prong open, and Q82 inherits the same idea at the frontier
scales $n \in \{30, 32\}$. Standing dual-attack policy: probe the prong
for falsification BEFORE spending proof rounds on it. This round is
that probe, and it is negative in a precise, pinned way.

**Setup.** For a graph $G$ let $B$ be the non-backtracking edge
operator on the $2m$ darts. By Ihara–Bass, for a cubic graph the
spectrum of $B$ is $\{(\lambda \pm \sqrt{\lambda^2 - 8})/2 :
\lambda \in \mathrm{spec}(A)\} \cup \{\pm 1\}^{m-n}$ — every
$\mathrm{tr}(B^k)$ is an EXACT function of the adjacency spectrum.
$\mathrm{tr}(B^k)$ counts tailless closed NB walks of length $k$, and
$N_k = \sum_{d \mid k} d\,P_d$ with $P_d$ the primitive classes of
length $d$. A $k$-cycle contributes $2k$ walks ($2k$ starting darts
$\times$ … counted once per dart, both directions: $2k$ per cycle in
$N_k$'s $d{=}k$ term, i.e. $P_k \supseteq$ 2 classes per $k$-cycle);
crucially $P_k$ ALSO contains non-cycle primitives — figure-eights
(two short cycles joined by a path, traversed as one NB circuit) and
theta-walks — built entirely from cycles of ALLOWED lengths.

**Data (exact integer computations on the CHECK-4 frontier argbests;
Ihara–Bass cross-check agrees to the integer).**

| graph | $c_3,c_5,c_6,c_7$ | $c_8$ | $\mathrm{tr}(B^8)$ | $c_{16}$ | $32c_{16}$ | $\mathrm{tr}(B^{16})$ | cycle share |
|---|---|---|---|---|---|---|---|
| G30 | 9, 1, 2, 1 | 0 | **320** | 210 | 6,720 | 65,312 | 10.3% |
| G32 | 8, 3, 6, 3 | 0 | **240** | 317 | 10,144 | 66,000 | 15.4% |

Low-order sanity closures: $\mathrm{tr}(B^3) = 6c_3$ and
$\mathrm{tr}(B^5) = 10c_5$ hold exactly on both graphs;
$\mathrm{tr}(B^4) = 0$ (no $C_4$, no length-4 primitives in a simple
graph); on G30, $\mathrm{tr}(B^6) = 78 = 6c_3 + 12c_6$ exactly, so
length-6 non-cycle mass is zero there — the shape mass turns on at
length 8.

**Why this kills the prong as posed.** A moment-LP certificate for
$c_{16} > 0$ must show $\mathrm{tr}(B^{16})$ (spectrally forced)
exceeds the largest possible non-cycle mass. But the length-8 row is a
built-in counterexample to any spectra-only bound on non-cycle mass:
there the cycle mass is exactly zero — $c_8 = 0$ is a stratum
constraint — yet the trace is 320 and 240. The entire banned-length
trace is theta/dumbbell mass supplied by the allowed short cycles
(girth-3 structure: 9 resp. 8 triangles), and its size is set by WHERE
those short cycles sit (pair distances), which the spectrum does not
determine. At length 16 the same shape mass is 89.7% resp. 84.6% of
the trace. So no LP over $\{\mathrm{tr}(A^k)\}_{k \le 16}$ /
$\{\mathrm{tr}(B^k)\}_{k \le 16}$ can separate $c_{16} = 0$ from
$c_{16} = 210$: the separating information is subgraph-positional, not
spectral. A revival would need shape-aware counting (explicit
upper bounds on figure-eight/theta primitives of length 16 in terms of
$c_3, \dots, c_7, c_9, \dots, c_{15}$ and their pairwise distances) —
a genuinely combinatorial, not spectral, argument. Parked, not queued.

**Consequence for Q82.** The prong ordering inside Q82 collapses to
the one the R63 data already favored: isomorph-free exhaustion
(SMS-style lex-minimality) is the only live exact technology for the
frontier scales. R65 begins that port, scoped to reach: an orderly
(lex-minimal adjacency-matrix) generator with in-search $C_4/C_8$
pruning, validated against the known connected-cubic counts at small
$n$, then run upward on the $\{C_4, C_8\}$-free stratum with
per-order exhaustive counts as the deliverable. CHECK 5 of
`lemma_g9c16_stratum` pins this round's computation.
## Section 105 — R65: exhaustive rule-tree enumeration decides the small end — the {C4, C8}-free cubic stratum is EMPTY through n = 22 and turns on at n = 24 with exactly four graphs, all C16-carrying (session s_0828-080832-67a3)

R63 closed with "the SMS isomorph-aware framework is the tool to port".
This round ports the half of it our stack can carry exactly — complete,
isomorph-controlled exhaustion — and it settles more than expected: the
frontier's small end is now DECIDED for the cubic case, by in-house
computation, unconditionally.

**The enumerator.** A rule-tree over labeled adjacency structures:
vertices are completed in index order (vertex $u$ acquires its remaining
neighbors only after $0..u-1$ are full, so those neighbors are all
$> u$); each vertex's neighbors are added in increasing order; a fresh
vertex always takes the smallest unused label (discovery order); and
$N(0) = \{1, 2, 3\}$. Every connected cubic graph admits at least one
labeling satisfying these rules (replay a greedy discovery of the graph
from any root), so the rule tree visits every isomorphism class at
least once — zero completions is an exhaustion proof. Cycle bans are
edge-monotone: a banned cycle can only be created by the addition of
its own last edge, so rejecting exactly those additions that close a
banned cycle (simple $u$–$v$ path of length $L-1$ present before the
add, $L \in \{4, 8\}$) is exhaustion-safe. Completions are labeled
graphs with (heavy) discovery-order multiplicity; classes are counted
downstream by canonical dedup.

**Validation (all in-session, all exact).** (i) Bans off, the
enumerator reproduces A002851's connected-cubic class counts
1/2/5/19/85/509 at $n = 4, \dots, 14$. (ii) In-search banning equals
post-filtering on labeled counts: $C_4$-free at $n = 10/12/14/16$ gives
58/528/12032/275273 both ways; $\{C_4, C_8\}$ at $n = 12..16$ agrees
(both empty). (iii) Three independently written code paths — the
single-process reference, the multiprocessing port (frontier-split
subtrees), and a bitmask/meet-in-the-middle reimplementation of the ban
tests — agree on the full fingerprint (node counts AND completions) at
every order checked, including $n = 24$: 12,297,554 nodes both ways,
9,512 labeled completions each. ($n = 26$ ran on the fastest path
only; its class dedup uses an individualization-refinement canonical
certificate validated against A002851 at $n = 10/12/14$ — 19/85/509 —
and against the VF2 dedup at $n = 24$.) CHECK 1 of
`lemma_stratum_onset_24__0828-080832-67a3.md` re-derives the
fingerprint from scratch in ~3s.

**Results (exhaustive, per order $n$, ban set $\{C_4, C_8\}$, connected
cubic).**

| $n$ | tree nodes | labeled completions | classes | verdict |
|---|---|---|---|---|
| 12 | 490 | 0 | 0 | empty |
| 14 | 2,205 | 0 | 0 | empty |
| 16 | 10,088 | 0 | 0 | empty |
| 18 | 52,293 | 0 | 0 | empty |
| 20 | 307,686 | 0 | 0 | empty |
| 22 | 1,891,538 | 0 | 0 | empty |
| 24 | 12,297,554 | 9,512 | **4** | **NONEMPTY — onset** |
| 26 | 138,937,178 | 200,888 | **23** | **NONEMPTY** |

*[R66 correction: the node counts in the 24 and 26 rows are wrong —
the verbatim CHECK-1 reference gives 12,302,758 and 138,948,598
(Section 106). Completions, classes, and every mathematical conclusion
are unchanged.]*

**The onset at $n = 24$, and $n = 26$.** At 24: exactly four classes,
pinned in CHECK 2 with full edge lists — all girth 3, all
non-bipartite, $c_{16} = 207, 228, 315, 330$. At 26: exactly 23
classes, ALL girth 3 again, $c_{16} \in [161, 454]$ (extremal member
pinned in CHECK 3). No class at either order is $C_{16}$-free, so
(since $C_{32}$ does not fit below $n = 32$) **there is no cubic
Erdős–Gyárfás counterexample on $\le 26$ vertices** — an in-house
re-derivation, by complete enumeration, of the corresponding range of
F3's Markström computation (cubic counterexamples need $\ge 30$
vertices, i.e. exhaustion through 28). One more scale ($n = 28$, R66,
already running) re-derives Markström's cubic bound entirely in-house;
the scales after that ($n = 30, 32$) are NEW unconditional cubic
territory — Markström stopped at 28 and the order-31 SMS exclusion
(F7a) is conditional, primary source unfetched. The floor profile now has EXACT left-wall points: 24: **207
(exact)**, 26: **161 (exact)**, then 30: 210 (SA), 32: 317 (SA), 58:
37 (SA), 60: 65 (SA), 62: 88 (SA). The exact floor DECREASES from the
onset toward the 58-dip — which makes the SA values at 30/32 (210,
317, both ABOVE the exact 26 floor) look like unconverged upper
bounds rather than the true minima: the first concrete evidence that
the SA floors at the frontier scales overestimate.

**Corrections to the working picture.** (a) R56's sampling-based
"$c_8 > 0$ everywhere at $n \le 28$" is FALSE as a structural
statement: the stratum exists from 24 up (4 classes at 24, 23 at
26). SA with the lexicographic
$100 c_4 + c_8$ objective missed a four-class needle in a $\sim 10^8$-class haystack (A002851 growth) —
reachability failure, not emptiness. (b) R63's "prior cross-branch data
had the stratum unreached anywhere below 58" now reads: *unreached by
search*; the true onset is 24. (c) The girth-3 signature of every SA
argbest (R60, R63) is now explained at the small end: ALL 27 stratum
classes at 24 and 26 have girth 3 — below 28 there are no girth-5
stratum graphs at all.

**Why this matters for Q82.** The frontier question at $n \in \{30, 32\}$
is exactly this computation two scales up — and unlike $n \le 28$ it is
not a re-derivation: completing it decides the cubic frontier
unconditionally, independent of F7a. Measured rule-tree growth per order
step: $22 \to 24$: $\times 6.5$; $24 \to 26$: $\times 11.3$ —
putting $n = 28$ near $1.5 \times 10^9$ nodes ($\sim$2 h on this
container's 4 cores with the bitmask/MITM ban tests; running as R66)
and $n = 30$ near $1.5 \times 10^{10}$ (a dedicated long run or one
more pruning idea away). The
witness box's small end is closable by iterating the same validated
tool; R66 continues upward.

**Ledger containment note (R65 fix; wording superseded by the R66
reframing).** `proofs/erdos_gyarfas.json` is frozen for the branch
(read-only environment file), so external facts learned after its audit
CANNOT be added to it. The block following Section 103 — retitled
"Literature annotations F4–F7" in R66 — records them for attribution
and context ONLY: they are not ledger facts and not premises of
anything proved here; each entry carries its citation,
sign-disambiguation, and scope warnings. Independently of that: NO conclusion of R64 or R65
depends on F6 or F7a. R64 (NB-moment probe) uses only in-house exact
computation on CHECK-pinned graphs. R65 (exhaustion through $n = 26$)
uses only in-house enumeration, the arithmetic-checkable A002851
reference counts, and the in-ledger F3 (Markström: cubic
counterexamples need $\ge 30$ vertices) — and F3 is used only as a
CONSISTENCY check (our all-classes-carry-$C_{16}$ result agrees with
it), never as a premise. And with the R65 status
correction in `lemma_g9c16_stratum` (its bipartite-half-at-58 closure
downgraded to CONDITIONAL on F6, the lemma's open content formally
unchanged), F6 and F7a are now load-bearing NOWHERE in this document:
both are recorded expectations with attributed, conditional status,
and every proved statement rests on in-house computation, the frozen
ledger (F1–F3), or arithmetic-checkable references (A002851).


## Section 106 — R66: the exhaustion reaches $n = 28$ — the full Markström range is now re-derived in-house, the exact floor falls to 153, girth 5 enters the stratum at the top of the $c_{16}$ range, and R65's node-count fingerprints at 24/26 are corrected (session s_0829-080615-66f6)

R65 closed with "$n = 28$ near $1.5 \times 10^9$ nodes, running as R66" —
and then session s_0828 ended abnormally, losing the container-local
harness before the run finished. This round rebuilds the tool better and
completes the program's small end.

**The rebuilt harness (C port, validated against every pinned
fingerprint).** The R65 rule-tree enumerator (CHECK 1 of
`lemma_stratum_onset_24`) was ported to C (~40x per-node speedup;
`enum.c`, container-local scratchpad, reconstructable from the CHECK-1
reference + Section 105's rule description; the port preserves the exact
recursion structure: one node count per `rec()` entry, candidates
`(last+1 .. next\_fresh-1)` plus one fresh vertex, edge-monotone in-search
bans via endpoint masks of simple paths of length 3/7 from the current
vertex). Validation, all re-run this session: (i) bans off, labeled
completions 50/639/9609 at $n = 8/10/12$ and A002851 class counts
19/85/509 at $n = 10/12/14$; (ii) $C_4$-only in-search ban $\equiv$
post-filter labeled counts 58/528/12032/275273 at $n = 10..16$; (iii)
$\{C_4, C_8\}$ node counts 2205/10088/52293/307686/1891538 at
$n = 14..22$ — every one equal to the pinned value; (iv) at $n = 24$,
per-subtree comparison against the VERBATIM CHECK-1 Python reference
(19 subtrees at a 10-edge frontier cut + prefix): bit-exact agreement on
every subtree's (nodes, completions).

**Fingerprint correction to Section 105 (content unaffected).** The
verbatim CHECK-1 reference gives $12{,}302{,}758$ tree nodes at
$n = 24$ — NOT the $12{,}297{,}554$ recorded in Section 105's table
(and echoed in CHECK 1's prose) — while completions agree exactly
(9,512). Same at $n = 26$: the C port (whose counting semantics are
proven bit-exact against the reference at 24) gives $138{,}948{,}598$
nodes vs the recorded $138{,}937{,}178$, with completions again agreeing
exactly (200,888) and the class census again coming out 23 classes,
$c_{16} \in [161, 454]$, all girth 3. Diagnosis: the R65 parallel path
under-counted one node per emitted frontier state (the deltas, 5,204 and
11,420, are exactly plausible state counts at the cuts used); its
"single-process reference agreed" claim at those two orders cannot have
been true of the node counts. EVERY mathematical conclusion of R65 —
emptiness through 22, the four onset classes at 24, the 23 classes at
26, all $c_{16}$ values, the girth-3 signature — is re-confirmed
unchanged by two independent implementations this session. Only the two
recorded node counts were wrong; the corrected fingerprints are the ones
above.

**Class dedup, replaced and strengthened.** Classes are now counted by
an EXACT canonical certificate native to the rule tree: the
lexicographically minimal rule-labeling edge sequence (min over root,
root-neighbor order, and fresh-assignment order, computed by constrained
replay with prefix pruning). Validated: A002851 19/85/509 at
$n = 10/12/14$ (bans off); the pinned 4-class onset at 24 with
$c_{16} = 207/228/315/330$; the 23 classes at 26 with floor 161 and
ceiling 454. The certificate is itself an edge list, so the census file
IS the class list.

**R66 result — exhaustive, $n = 28$, ban set $\{C_4, C_8\}$, connected
cubic.** Tree nodes $2{,}969{,}746{,}296$ (growth $26 \to 28$:
$\times 21.4$ — the R65 extrapolation of $1.5 \times 10^9$ was 2x low);
labeled completions $6{,}201{,}596$; EXACTLY **251 classes**; $c_{16}$
range $[153, 731]$ with **no zero**. Since $C_{32}$ does not fit on
$\le 28$ vertices, there is no cubic Erdős–Gyárfás counterexample on
$\le 28$ vertices — with $n = 24, 26$ (R65) this completes the in-house
re-derivation, by complete isomorph-controlled enumeration, of the full
range of F3's Markström computation (cubic counterexamples need
$\ge 30$ vertices). F3 is again used only as a consistency check, never
as a premise; the agreement is now over the entire range it covers.

**Structure at 28.** (a) The exact stratum floor falls again:
$24{:}\,207 \to 26{:}\,161 \to 28{:}\,153$, extending the monotone
descent toward the $n = 58$ SA dip (37) — and the exact 28 floor
already undercuts the SA floor at $n = 30$ (210), hardening R65's
inference that the SA values at the frontier scales are unconverged
upper bounds. (b) Girth 5 enters the stratum for the first time:
girth histogram $\{3{:}\,247,\ 5{:}\,4\}$ — and the four girth-5
classes carry the four HIGHEST $c_{16}$ values (614, 616, 621, 731).
At every scale where we can see it, moving toward the cage corner
(higher girth) is $c_{16}$-adversarial, exactly matching the R60/R63
observation that SA argbests flee to girth 3. CHECK 4 of
`lemma_stratum_onset_24` pins the $c_{16} = 153$ extremal member and
the minimal girth-5 member with from-scratch verification.

**Where this leaves Q82.** The frontier scales are $n \in \{30, 32\}$.
$n = 30$ is NEW territory (Markström stopped at 28): the same validated
tool is running it now (measured growth predicts
$\sim 6 \times 10^{10}$ nodes); at $n = 30$, $C_{32}$ does not fit, so
ANY $C_{16}$-free completion there would be a full witness candidate —
and zero completions... would move the cubic frontier for the first
time since 2004. $n = 32$ at the measured $\times 21$/order growth is
$\sim 1.3 \times 10^{12}$ nodes — out of reach for this container with
the current tool; deciding it needs isomorph-aware in-search pruning
(the SMS port proper), a stronger prune, or more hardware. R67 logs the
$n = 30$ outcome.
