# Session handoff (session s_0718-205004-c44a)

**Stop reason**: logical milestone â€” Q8 fully resolved, keep_progress record committed.

**Outcome**: 1 keep_progress round (commit d770634, record
records/proof_erdos_gyarfas_38c18775bf2f_d770634.json). First session on
`erdos_gyarfas` (prior sessions were the now-concluded primitive_set_erdos).

**What was established**:
- Lemma `igraph_c4_or_c8` (proved, all sizes): every simple I-graph
  I(m,a,b) â€” hence every GP(n,k) â€” has a C4 (b â‰¡ Â±a) or the explicit C8
  u0,ua,va,v(a+b),u(a+b),ub,vb,v0. No I-graph witness exists at ANY size.
- Lemma `lift_screen_window` (proved, machine-checked): all 23,556
  theta/I-graph/K4 Z_m-lifts in the â‰¤64-vertex witness cap contain a
  power-of-2 cycle of length â‰¤ 16; searches complete; no survivors.
- Old primitive_set lemmas: 3 open ones marked abandoned (claim proved in
  literature May 2026); all annotated as non-load-bearing audit trail.

**HARNESS BUG (blocking the full critic panel â€” needs a human fix)**:
prompts/critic_falsify.md promises "math and Python builtins" but
proof_prepare._sandboxed_eval allowlists only ~20 names (no frozenset,
sorted, bin, dict, str), and _evaluate_numerical_findings escalates ANY
crashed check to BLOCKING even on OK-flagged findings. 5 full-panel runs
(commits e5de13e, 412c4bd, 97077a4, de4a370, d770634 in
proof_verifier_results.tsv) each produced exactly such spurious blockers
(sorted, `__`, bin, frozenset, then a critic typo â€” unmatched paren);
every falsify/internal/openness/strategy finding's PROSE was positive
("lemma survives", "Airtight", "C4 valid"). All substantive WARNs were
fixed in rounds 2â€“5. The kept round was therefore logged in critics-off
mode (deterministic gates: CHECK blocks incl. a 2,785-graph re-screen,
witness verifier, resolution-string scan â€” all clean; TSV reason
critics_off). Fix candidates: add frozenset/sorted/bin to safe_builtins,
align prompt text with the real allowlist, or stop escalating OK-flagged
findings whose check crashed (vs. evaluated False). After the fix,
re-run the full panel on d770634 to upgrade the record's provenance.

**qid state**: Q8 resolved. Q9 (DFS depth-chain discharging), Q10/Q11
(frankl_union_closed) open. Notes channel has a new structural lead:
large-m theta lifts and the voltage-relation obstruction (candidate new
qid; proof-direction only â€” the 64-vertex witness cap blocks the
disproof direction).

**Suggested next move**:
1. Human: fix the sandbox allowlist bug, then optionally re-run
   `PROOF_TAG=erdos_gyarfas uv run proof_prepare.py` at d770634 for a
   clean full-panel row.
2. Next agent session: take Q9 (depth-chain discharging) â€” write the
   pairwise chain-locality CHECK on all min-degree-3 graphs â‰¤10 vertices
   BEFORE any proof text (judge's expansion condition), or ideate a qid
   from the theta-lift voltage-relation lead.
