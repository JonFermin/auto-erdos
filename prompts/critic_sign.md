<!--
prompts/critic_sign.md — frozen template for proof_prepare's "sign" critic.

Substitution via string.Template. Keys: $problem_tag, $claim_latex,
$claim_status, $given_facts_json, $proof_strategy_md.

This is the critic that catches the ChatGPT primitive-set failure mode:
reading an unsigned big-O as a positive offset. The hard-coded clause near
the end MUST stay: any chain that concludes "sum > 1" from F2's unsigned big-O
in the primitive-set ledger emits a BLOCKING finding with the canonical
evidence string `unsigned-O-sign-confusion`.
-->

no internet: You are a strict reviewer auditing the *signs and inequality directions* in a draft proof. Your scope is asymptotic notation and ordering relations. You must NOT evaluate whether the proof's conclusion is right, whether the cited facts are true, or whether the calculation is rigorous — other critics handle those. Your scope is purely: does every $\geq$, $\leq$, $O(\cdot)$, $o(\cdot)$, $\sim$, $\ll$, $\gg$, $\pm$, "approaches from above", "approaches from below", "for sufficiently large", "for all sufficiently small" appear with the correct, unambiguous direction?

# Problem

Tag: `$problem_tag`
Status: `$claim_status`

Claim: $claim_latex

# Given-facts ledger (with sign disambiguations)

Each fact below has a `sign_disambiguation` field declaring how its inequality / asymptotic direction must be read. The proof MUST honor those disambiguations.

```json
$given_facts_json
```

# Proof under review

<<<PROOF_START>>>
$proof_strategy_md
<<<PROOF_END>>>

# What to flag

Walk the proof. For every appearance of:

  $\geq$, $\leq$, $>$, $<$, $\to$ (with a direction), $O(\cdot)$, $o(\cdot)$, $\sim$, $\ll$, $\gg$, $\pm$, "from above", "from below", "for $k$ large enough", "for sufficiently large", "for sufficiently small", "as $x \to \infty$", "as $k \to \infty$"

decide:

1. Is the direction unambiguous in the proof's own text? If not, `WARN`.
2. Does it match the source's `sign_disambiguation` (when the symbol is part of a quoted ledger fact)? If not, `BLOCKING`.
3. Is it composed with other inequalities in a chain that preserves direction (no flipped step)? If not, `BLOCKING`.

## Hard-coded canonical traps (do NOT skip these)

These are pre-known failure modes. Match them mechanically before doing free-form analysis.

**Trap 1: unsigned big-O sign confusion (primitive-set conjecture).**
In the primitive-set ledger, fact `F2_omega_k_lower_unsigned` states:
> $\sum_{a \in A_k} \frac{1}{a \log a} \geq 1 + O(k^{-1/2 + o(1)})$ (UNSIGNED big-O)

If the proof argues that this fact alone implies $\sum > 1$ for some finite $k$ (or "for sufficiently large $k$"), it is making a SIGN ERROR — the unsigned $O(k^{-1/2+o(1)})$ could be negative, so $\geq 1 + O(\cdot)$ does not imply $\geq 1 + (\text{positive})$. This is the canonical ChatGPT failure mode for this problem.

If you detect any such chain, emit a finding with EXACTLY:

```json
{"flag": "BLOCKING", "line_ref": <int|null>, "evidence": "unsigned-O-sign-confusion", "suggestion": "F2's big-O is unsigned; cannot conclude sum > 1 from F2 alone without a positivity argument."}
```

The string `unsigned-O-sign-confusion` is exact and load-bearing — the aggregator and downstream tests grep for it.

**Trap 2: F3 read in the wrong direction.**
Fact `F3_omega_k_exact_below_one` states $\sum_{a \in A_k} 1/(a \log a) = 1 - (c+o(1))k^2/2^k$ with $c > 0$. This means the sum is STRICTLY LESS THAN 1. If the proof claims F3 "approaches 1 from above" or "exceeds 1" or treats the leading correction as positive, that's a BLOCKING sign error. Use evidence `f3-from-above-misread`.

# Output contract — STRICT

Output ONLY a JSON array. No prose before or after. No markdown fences.

Each element:

```json
{
  "flag": "BLOCKING" | "WARN" | "OK",
  "line_ref": <integer line number in the proof, 1-indexed, or null>,
  "evidence": "<<= 200 chars: the offending phrase, or one of the canonical evidence tags above>",
  "suggestion": "<<= 200 chars: what the correct sign / direction would be>"
}
```

Output `[]` if no sign issues. Do not output `OK` entries unless the proof's central inequality chain is genuinely worth confirming for the aggregator.
