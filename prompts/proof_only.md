<!--
prompts/proof_only.md — frozen template for write_paper.py --mode proof.

Lean alternative to paper_writeup.md: same problem context and verified
construction, same rigor requirements, but no amsart preamble, no title,
no abstract, no section ceremony. The output is plain markdown with
embedded LaTeX math, suitable for a code review or appendix rather than
a journal submission.

This file is READ-ONLY at runtime. The prompt's sha256 lands in every
papers/*.proof.meta.json sidecar; edits silently break reproducibility
across runs unless the change is committed.

Required keys (write_paper.py guarantees them):
  problem_tag, problem_family, problem_param, baseline, score,
  improvement, problem_statement, candidate_block, verifier_summary,
  branch, commit
-->

no internet: Please write a rigorous, self-contained proof that the construction below is valid and has the claimed size. No title, no abstract, no section ceremony — just the proof. Use plain markdown with embedded LaTeX math (inline `$...$` and display `$$...$$` are both fine). State and prove any structural lemma you need. Address subtle points (parity, overlap, modular reduction, etc.) explicitly rather than waving them away. Give the proof directly — do not wrap it in a code block.

# Problem ({problem_family} family, tag `{problem_tag}`)

{problem_statement}

The current literature lower bound for this instance is **{baseline}**.

# Verified construction

A deterministic verifier (auto-erdos repo, branch `{branch}`, commit `{commit}`) confirmed that the following set is **valid** and has size **{score}**, which is **{improvement}** above the literature lower bound.

Verifier summary: {verifier_summary}

The construction:

{candidate_block}

# What to prove

1. **Validity**: the set satisfies the family's defining constraint (no three-term zero-sum AP for capset; all pairwise sums distinct for sidon).
2. **Size**: the set has exactly {score} elements (no hidden duplicates, no off-by-one).
3. **Bound**: the maximum size of a valid set in this instance is at least {score}, strictly improving on the literature lower bound of {baseline}.

The candidate set is fixed — do not silently substitute a different construction. If your proof needs a re-encoding (e.g. lifting capset coordinates to integers, or grouping sidon elements by residue), state the bijection clearly and prove the equivalent claim about the re-encoded set.
