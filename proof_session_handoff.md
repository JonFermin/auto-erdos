# Session handoff (session s_0729-131551-1d91)

**Stop reason**: logical milestone — Theorem C proved, n=18 census complete

**Rounds this session**: R29–R33 (5 rounds, all keep_progress)

**Current focus**: Depth-4 resolution for Case A cubic graphs.

## What was proved this session

**Theorem A (Section 55)**: sd=1 (C4 at depth-3) is IMPOSSIBLE in Case A.
Proof: matching constraint forces A3=[t1,k2) making e3 share vertex t1 with e1.

**Cycle Bound (Section 55)**: sd=13 (C16) requires n≥16; for n≤15 sd=5 is unique.

**Connectivity Theorem (Section 54)**: XOR of 3 back edges is single cycle iff c≥1
(c = |(A1△A2)∩A3| ≥ 1).

**Theorem C (Section 57)**: The 4 special back edges (r1,r2,l1,l2) form a
single depth-4 cycle iff ov = max(0, min(a2,s2)-max(a1,s1)) ≥ 1.
When ov≥1: L4 = (a2-a1)+(s2-s1)-2·ov+4.
When ov=0: two disjoint cycles of lengths (a2-a1+2) and (s2-s1+2).

## n=18 findings (Section 56)

Census (a1+a2≤24): 4985 sd=5 (C8), 1491 sd=13 (C16), **18 depth-3 failures**.
The 18 failures have NO depth-1/2/3 resolution. Both verified examples resolve
at depth-4:
- ex1 [(2,0),(6,0),(17,5),(17,15),...]: ov=1 → Theorem C gives C16 ✓
- ex2 [(2,0),(6,0),(17,11),(17,15),...]: ov=0 → interior quadruple gives C8 ✓

## Key open questions (what to do next)

**Q71** (PRIORITY): For Case A assignments with ov=0, prove that some depth-4
quadruple involving interior edges always gives a po2 cycle. This is the
remaining gap for the depth-4 universality argument.

Approach: When ov=0, the root gap [a1,a2) and leaf gap [s1,s2) are disjoint.
Consider triples of interior edges {e_i} with one root edge:
  (a1,0)+e_i+e_j+e_k: analyze the XOR interval and find po2 length.

**Q72** (after Q71): Verify depth≤4 universality for n=14,16,18 (all Case A).
Run full enumeration (not just a1+a2≤24) and check:
  failures = [a for a in all_case_A_assignments(n) if not any_depth4_po2(a)]

**Q73**: For larger n (n=20,22), does depth-4 still suffice, or do depth-5+ cases
appear? This will reveal whether the depth bound is truly uniform.

## Files modified this session

- proof_strategy.md: Sections 53–57 added (Lemma G, connectivity, Theorem A,
  Section 55 sd=1 impossible, Section 56 n=18 census, Section 57 Theorem C)
- proof_open_questions.jsonl: Q67 claimed and resolved this session

## Status of lemma files

No new lemma files created; all results in proof_strategy.md.

## Suggested first move for next session

1. Read proof_session_handoff.md (this file).
2. Read Section 57 in proof_strategy.md (last ~150 lines).
3. Work on Q71: prove depth-4 universality for ov=0 Case A.
   Try: pick one interior edge e_i, combine with r1=(a1,0), r2=(a2,0), e_j:
   need (a2-a1)+(g_i)+g_j - 2*intersections ∈ {0,4,12,28}. Show always achievable.
4. Run depth-4 universality check: python code enumerating all n=14 Case A and
   checking if any quadruple gives single-cycle po2.
