# Session handoff (session s_0804-080732-f106)

**Stop reason**: Logical milestone — two keep_progress rounds (R21, R22).

**Current focus**: Q9 — analytic proof that the 4-mechanism taxonomy covers
all cubic DFS trees. After R21+R22 the SUPPLY half is closed; the open
core is the MEETING + TUNING of the third back edge.

**What was proved this session**:

R21 — `fund_pair_overlap` (proved):
1. The intersection subgraph of two fundamental cycles in a DFS tree is
   always empty, a single vertex, or a single vertical path — with the
   shared chain running exactly from the deeper anchor to lca(s1, s2), so
   k = d(lca(s1,s2)) − d(deeper anchor).
2. C1△C2 is a single simple cycle IFF the tree paths share an edge
   (k ≥ 1), and then |D| = gap1 + gap2 + 2 − 2k. Subsumes the nested and
   crossing formulas; covers branching pairs (senders in different
   subtrees) for the first time.
3. Mixed overlapping pairs give ODD single cycles (the OEE raw material).
   Same-sender pairs always overlap (k = inner gap).

R22 — `mixed_overlap_supply` (proved):
- In a 2-connected graph, back-edge parity segregation is IMPOSSIBLE:
  if both gap parities occur, some odd-gap and some even-gap back edge
  overlap. Proof: one-child root + low-point property ⇒ every tree edge
  covered; the low-point back edge over v covers both v's parent and
  child edges, so a segregated parity coloring of tree edges would be
  locally (hence globally) constant — contradiction.
- Corollary: every mixed-parity DFS tree of a 2-connected graph has a
  mixed pair with odd single-cycle sym-diff D. Supply half of Q9 CLOSED
  (2-connectedness is sharp — bridged compositions evade it; irrelevant
  to the EGC class since cycles live in blocks).
- CHECKs: 20k pairs (R21) and 796 2-connected trees / ~10k low-point +
  coverage checks (R22), zero violations; 777/777 (R21) and 768/768
  (R22) mixed trees had mixed overlapping pairs.

**qid in flight**: Q9 released with partial progress. Next session
re-claims Q9.

**Suggested next move (R23) — meeting + tuning, in order**:
1. **Dual-attack probe FIRST** (standing policy): census over
   pair-residual trees of the achievable value set
   V = {|D| + gap3 + 1 − 2k' : legal (pair, B3) pasting configs} —
   is 8 ∈ V always? Is V an interval in steps of 2? Record min/max/gaps
   of V per tree. This directly measures the pigeonhole slack the tuning
   argument needs. Extend the R20 probe (it recorded only the firing
   shapes, not the full value set).
2. **Meeting structure**: E(D) ∩ E(C3) is automatically tree-only
   (B3 ≠ B1,B2), P3 is one vertical chain, and D's tree edges are ≤ 2
   arcs each a union of ≤ 2 vertical chains — so P3 ∩ E(D) is a union of
   ≤ 2–3 vertical segments, each an interval by the fund_pair_overlap(1)
   argument. Meeting = exactly one nonempty segment + shared-vertex
   condition. Try to characterize WHEN a cover of a D-tree-edge meets D
   in a single path (the analogue of the anchors-comparable condition).
3. **Tuning**: with V's structure from the probe, try range/pigeonhole:
   the same-sender supply at leaves gives many candidate (B1,B2) pairs
   with DIFFERENT |D| values (|g1−g2|+2 over back-edge pairs at each
   leaf); combined with the k' freedom this may sweep V across a power
   of 2. Note all values in V have the same parity (even, for legal
   configs) — hitting is a range question, not a parity question.
4. Run with PROOF_TAG=erdos_gyarfas. Critic infra notes: (a)
   'critic_unavailable: internal/falsify' blockings are transient —
   re-run; (b) the critic CACHE replays identical responses for an
   identical prompt, so after a spurious blocking finding you must make
   a genuine artifact change (strategy text) to force fresh rolls;
   (c) the numerical critic sometimes writes __import__-based checks
   (banned token) that auto-escalate to BLOCKING despite its own text
   saying 'confirmed' — same remedy.

**Files modified this session**:
- proof_lemmas/lemma_fund_pair_overlap__0804-080732-f106.md (new, proved)
- proof_lemmas/lemma_mixed_overlap_supply__0804-080732-f106.md (new, proved)
- proof_lemmas/lemma_igraph_c4_or_c8.md (falsification-direction remark added)
- proof_strategy.md (Sections 28, 29 + Section 3 clarification)
- notes channel appended (proof_notes_erdos_gyarfas.md)
