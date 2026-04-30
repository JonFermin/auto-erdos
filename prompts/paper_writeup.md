<!--
prompts/paper_writeup.md — frozen template for write_paper.py.

This file is READ-ONLY at runtime (treated like library/ and prepare.py).
Edit it deliberately and check in the change — the prompt's sha256 is
recorded in every papers/*.meta.json so we can correlate writeups to the
exact prompt version that produced them. Do not edit casually.

Substitution is plain str.format with the named keys below; literal
braces in the body must be doubled ({{ and }}).

Required keys (write_paper.py guarantees them):
  problem_tag       e.g. "capset_n8"
  problem_family    "capset" or "sidon"
  problem_param     "n=8" or "N=100"
  baseline          literature lower bound, integer
  score             verified score, integer
  improvement       score - baseline, integer (>= 1 by keep rule)
  candidate_block   the verified construction, formatted for the family
  verifier_summary  one-line natural-language statement of what was verified
  branch            git branch the keep was made on
  commit            short commit sha
-->

no internet: Please write a full correct resolution to the problem formatted as a publishable maths research paper using amsart using a4paper, margin=1in. Keep the title brief and to the point. The abstract should only be at most 6 sentences. Use section headings sparingly. Do not add an author entry. Be rigorous and self-contained. Ensure to address any issues you raised. Give the LaTeX in a code markdown block.

# Problem ({problem_family} family, tag `{problem_tag}`)

{problem_statement}

The current literature lower bound for this instance is **{baseline}**.

# Verified construction

A deterministic verifier (auto-erdos repo, branch `{branch}`, commit `{commit}`) confirmed that the following set is **valid** and has size **{score}**, which is **{improvement}** above the literature lower bound.

Verifier summary: {verifier_summary}

The construction:

{candidate_block}

# Required content of the paper

1. State the problem precisely.
2. Present the construction above (you may re-encode it for readability, but the underlying set must be the one given — do not silently substitute a different construction).
3. **Prove validity**: show the set satisfies the family's defining constraint (no three-term zero-sum AP for capset; pairwise-distinct sums for sidon).
4. **Prove the size**: show the set has exactly {score} elements.
5. State the resulting bound clearly: the maximum size of a valid set in this instance is at least {score}, improving on the {baseline} lower bound recorded in the literature.
6. If the proof requires a structural lemma (subspace decomposition, modular arithmetic, etc.), state and prove it.
7. Cite no external sources unless you can quote the result from memory and clearly attribute it; otherwise prove it inline.

Be rigorous and self-contained. Address any subtle issues (parity, overlap, modular reduction, etc.) explicitly rather than waving them away. The candidate is given in full above; the proof must establish that *this specific set* satisfies the constraints.
