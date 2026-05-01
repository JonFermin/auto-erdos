"""proof_prepare.py — READ-ONLY proof-attempt verifier (Track 2).

Parallel to ``prepare.py``. Reads ``proof_strategy.md`` and the problem ledger
at ``proofs/<PROOF_TAG>.json``, runs five critic LLMs in parallel against the
proof draft, optionally runs the deterministic witness verifier (when the
proof commits a ``<!-- WITNESS -->`` block), aggregates findings, and emits a
fixed ``print_summary`` block that ``proof_log_result.py`` parses.

Track 1 (``prepare.py``) is untouched. This module duplicates the small bits
it needs (``load_spec``, ``_short_commit``, repo-root resolution) so the
search-loop invariants are preserved exactly.

Public API:
    verify_proof(proof_md, spec, *, witness_payload=None) -> ProofVerifyResult
    print_summary(proof_md, result) -> None

CLI:
    PROOF_TAG=primitive_set_erdos uv run proof_prepare.py > run.log 2>&1

The module reads ``proof_strategy.md`` as the proof under review and writes
the metric block to stdout, plus a row to ``proof_verifier_results.tsv``.
"""
from __future__ import annotations

import json
import math
import os
import platform
import re
import subprocess
import sys
import threading
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from string import Template
from typing import Any

REPO_ROOT = Path(__file__).resolve().parent
PROOF_TAG = os.environ.get("PROOF_TAG", "primitive_set_erdos")
PROOFS_DIR = REPO_ROOT / "proofs"
PROMPTS_DIR = REPO_ROOT / "prompts"
PROOF_VERIFIER_RESULTS_TSV = REPO_ROOT / "proof_verifier_results.tsv"
PROOF_STRATEGY_MD = REPO_ROOT / "proof_strategy.md"

DEFAULT_TIME_BUDGET_S = 1800  # 30 min default for proof verification

CRITIC_NAMES = ("ledger", "sign", "openness", "numerical", "internal")
CRITIC_TIMEOUT_S = 240  # per critic; 4 minutes is generous for opus

# Witness block markers in proof_strategy.md.
_WITNESS_RE = re.compile(
    r"<!--\s*WITNESS\s*\n(.*?)\nWITNESS\s*-->",
    re.DOTALL,
)


# --------------------------------------------------------------------------- #
# Spec loader (deliberately duplicates prepare.load_spec — see module doc)
# --------------------------------------------------------------------------- #

def load_proof_spec(tag: str | None = None) -> dict:
    name = tag or PROOF_TAG
    path = PROOFS_DIR / f"{name}.json"
    if not path.exists():
        raise FileNotFoundError(
            f"Proof spec not found: {path}. Available: "
            f"{[p.stem for p in PROOFS_DIR.glob('*.json')]}"
        )
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _short_commit() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--short=7", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except subprocess.CalledProcessError:
        return "unknown"


# --------------------------------------------------------------------------- #
# Result types
# --------------------------------------------------------------------------- #

@dataclass
class Finding:
    critic: str
    flag: str  # "BLOCKING" | "WARN" | "OK"
    line_ref: int | None
    evidence: str
    suggestion: str
    numerical_check: str | None = None
    numerical_check_result: str | None = None  # "pass" | "fail" | "skipped" | None


@dataclass
class ProofVerifyResult:
    claim_status: str
    witness_valid: int  # 0 or 1
    witness_score: float  # NaN if no witness
    critic_blocking_count: int
    critic_warn_count: int
    verdict_hint: str  # "counterexample_proven" | "partial_result" | "blocked" | "open"
    verifier_seconds: float
    findings: list[Finding] = field(default_factory=list)
    witness_reason: str = ""
    proof_hash: str = ""
    critic_metas: dict[str, dict] = field(default_factory=dict)


# --------------------------------------------------------------------------- #
# Witness extraction + verification
# --------------------------------------------------------------------------- #

def extract_witness_payload(proof_md: str) -> dict | None:
    """Return the parsed JSON payload of the FIRST WITNESS block, or None."""
    m = _WITNESS_RE.search(proof_md)
    if not m:
        return None
    body = m.group(1)
    try:
        return json.loads(body)
    except json.JSONDecodeError:
        return None


def _run_witness_verifier(payload: dict, spec: dict) -> tuple[int, float, str]:
    """Returns (witness_valid:0|1, score:float, reason:str)."""
    module_path = spec.get("witness_verifier_module")
    if not module_path:
        return 0, float("nan"), "spec has no witness_verifier_module"
    try:
        import importlib
        mod = importlib.import_module(module_path)
    except ImportError as e:
        return 0, float("nan"), f"failed to import {module_path}: {e}"
    if not hasattr(mod, "verify_witness"):
        return 0, float("nan"), f"{module_path}.verify_witness missing"
    try:
        result = mod.verify_witness(payload, spec)
    except Exception as e:  # noqa: BLE001 — surface as invalid
        return 0, float("nan"), f"witness verifier raised {type(e).__name__}: {e}"
    return (
        1 if getattr(result, "is_valid", False) else 0,
        float(getattr(result, "score", float("nan"))),
        str(getattr(result, "reason", ""))[:500],
    )


# --------------------------------------------------------------------------- #
# Critic execution
# --------------------------------------------------------------------------- #

def _render_critic_prompt(critic_name: str, spec: dict, proof_md: str, *, witness_valid: int) -> str:
    template_path = PROMPTS_DIR / f"critic_{critic_name}.md"
    if not template_path.exists():
        raise FileNotFoundError(f"critic prompt template missing: {template_path}")
    template_text = template_path.read_text(encoding="utf-8")
    given_facts_json = json.dumps(spec.get("given_facts", []), indent=2)
    fields = {
        "problem_tag": spec.get("name", PROOF_TAG),
        "claim_latex": spec.get("claim_latex", ""),
        "claim_status": spec.get("claim_status", "unknown"),
        "given_facts_json": given_facts_json,
        "proof_strategy_md": proof_md,
        "witness_valid": str(witness_valid),
    }
    return Template(template_text).safe_substitute(**fields)


def _parse_critic_response(response: str) -> tuple[list[dict] | None, str]:
    """Tolerant JSON-array extractor.

    Returns (parsed_list, status_message). On success, parsed_list is a list
    of dicts; on failure, parsed_list is None and status_message describes
    what went wrong.
    """
    if not response or not response.strip():
        return None, "empty response"
    stripped = response.strip()

    # 1. Whole-response JSON parse.
    try:
        parsed = json.loads(stripped)
        if isinstance(parsed, list):
            return parsed, "ok"
        return None, f"top-level JSON is {type(parsed).__name__}, expected list"
    except json.JSONDecodeError:
        pass

    # 2. Strip a leading/trailing markdown fence and retry.
    fence_re = re.compile(r"^```(?:json)?\s*\n(.*)\n```\s*$", re.DOTALL)
    m = fence_re.match(stripped)
    if m:
        try:
            parsed = json.loads(m.group(1))
            if isinstance(parsed, list):
                return parsed, "ok-after-fence-strip"
        except json.JSONDecodeError:
            pass

    # 3. Find the first [ and last ] and try to parse between them.
    first_bracket = stripped.find("[")
    last_bracket = stripped.rfind("]")
    if first_bracket != -1 and last_bracket > first_bracket:
        candidate = stripped[first_bracket : last_bracket + 1]
        try:
            parsed = json.loads(candidate)
            if isinstance(parsed, list):
                return parsed, "ok-after-bracket-extract"
        except json.JSONDecodeError:
            pass

    return None, "no parseable JSON array found in response"


def _findings_from_parsed(critic_name: str, items: list[dict]) -> list[Finding]:
    findings: list[Finding] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        flag = str(item.get("flag", "WARN")).upper()
        if flag not in ("BLOCKING", "WARN", "OK"):
            flag = "WARN"
        line_ref = item.get("line_ref")
        if not isinstance(line_ref, int):
            line_ref = None
        evidence = str(item.get("evidence", ""))[:300]
        suggestion = str(item.get("suggestion", ""))[:300]
        numerical_check = item.get("numerical_check")
        if numerical_check is not None:
            numerical_check = str(numerical_check)[:500]
        findings.append(
            Finding(
                critic=critic_name,
                flag=flag,
                line_ref=line_ref,
                evidence=evidence,
                suggestion=suggestion,
                numerical_check=numerical_check,
            )
        )
    return findings


# --------------------------------------------------------------------------- #
# Sandboxed numerical-check evaluator
# --------------------------------------------------------------------------- #

_NUMERICAL_BANNED = ("__", "import ", "exec(", "open(", "eval(", "compile(", "globals(", "locals(", "getattr", "setattr", "delattr")


def _sandboxed_eval(expr: str, timeout_s: int = 5) -> tuple[bool, str]:
    """Evaluate expr in a math-only sandbox. Returns (truthy, message).

    The sandbox uses a restricted builtins dict and ``math`` only. Banned
    tokens are stripped via simple substring search before eval — not a
    formal sandbox, but adequate for the no-internet-no-fs critic context
    where the model has no incentive to break out and the worst case is
    we mark a finding as failed.
    """
    if len(expr) > 500:
        return False, f"expression too long ({len(expr)} chars > 500)"
    for ban in _NUMERICAL_BANNED:
        if ban in expr:
            return False, f"banned token in expression: {ban!r}"

    safe_builtins = {
        "abs": abs, "min": min, "max": max, "sum": sum, "range": range,
        "len": len, "int": int, "float": float, "round": round, "pow": pow,
        "True": True, "False": False, "None": None,
        "all": all, "any": any, "list": list, "tuple": tuple, "set": set,
        "enumerate": enumerate, "zip": zip, "map": map, "filter": filter,
    }
    safe_globals: dict[str, Any] = {"__builtins__": safe_builtins, "math": math}

    holder: dict[str, Any] = {"result": None, "error": None}

    def run() -> None:
        try:
            holder["result"] = eval(expr, safe_globals, {})  # noqa: S307 — restricted globals
        except Exception as e:  # noqa: BLE001
            holder["error"] = f"{type(e).__name__}: {e}"

    t = threading.Thread(target=run, daemon=True)
    t.start()
    t.join(timeout_s)
    if t.is_alive():
        return False, f"timeout > {timeout_s}s (thread abandoned)"
    if holder["error"] is not None:
        return False, str(holder["error"])
    return bool(holder["result"]), repr(holder["result"])


def _evaluate_numerical_findings(findings: list[Finding]) -> None:
    """Mutate findings: for each Finding from the numerical critic with a
    numerical_check, run it sandboxed; record pass/fail; escalate WARN→BLOCKING
    on FAIL. Findings with numerical_check==None get result=skipped."""
    for f in findings:
        if f.critic != "numerical":
            continue
        if f.numerical_check is None:
            f.numerical_check_result = "skipped"
            continue
        ok, msg = _sandboxed_eval(f.numerical_check)
        if ok:
            f.numerical_check_result = f"pass: {msg}"
        else:
            f.numerical_check_result = f"fail: {msg}"
            # If the critic itself flagged BLOCKING, leave it. If WARN/OK,
            # escalate to BLOCKING — a numerical claim that doesn't pass
            # re-derivation is a hard fail.
            if f.flag != "BLOCKING":
                f.flag = "BLOCKING"


# --------------------------------------------------------------------------- #
# Main verifier
# --------------------------------------------------------------------------- #

def _proof_hash(proof_md: str) -> str:
    """Content hash for dedup. Strips HTML comments EXCEPT the WITNESS block,
    collapses whitespace, lowercases, then sha256."""
    import hashlib
    # Stash the WITNESS block, strip other comments, restore.
    witness_match = _WITNESS_RE.search(proof_md)
    witness_block = witness_match.group(0) if witness_match else ""
    body = _WITNESS_RE.sub("__WITNESS_BLOCK__", proof_md)
    body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)
    body = body.replace("__WITNESS_BLOCK__", witness_block)
    body = re.sub(r"\s+", " ", body).strip().lower()
    return hashlib.sha256(body.encode("utf-8")).hexdigest()


def verify_proof(
    proof_md: str,
    spec: dict,
    *,
    use_critic_cache: bool = True,
) -> ProofVerifyResult:
    """Run the full Track 2 verifier on a proof draft. Idempotent given
    the critic cache."""
    t0 = time.time()
    findings: list[Finding] = []
    critic_metas: dict[str, dict] = {}

    # 1. Witness extraction + verification (deterministic).
    payload = extract_witness_payload(proof_md)
    if payload is None:
        witness_valid, witness_score, witness_reason = 0, float("nan"), "no WITNESS block found"
    else:
        witness_valid, witness_score, witness_reason = _run_witness_verifier(payload, spec)

    # 2. Run all five critics in parallel via the cache helper.
    try:
        from library._critic_subprocess import call_critics_parallel, CriticUnavailable  # noqa: F401
    except ImportError as e:
        # If the helper is missing we synthesize BLOCKING findings for every
        # critic so the loop fails loudly rather than silently passing.
        for name in CRITIC_NAMES:
            findings.append(Finding(
                critic=name, flag="BLOCKING", line_ref=None,
                evidence=f"critic_unavailable: {name}",
                suggestion=f"library._critic_subprocess import failed: {e}",
            ))
        result = ProofVerifyResult(
            claim_status=spec.get("claim_status", "unknown"),
            witness_valid=witness_valid,
            witness_score=witness_score,
            critic_blocking_count=sum(1 for f in findings if f.flag == "BLOCKING"),
            critic_warn_count=sum(1 for f in findings if f.flag == "WARN"),
            verdict_hint=_compute_verdict_hint(
                spec, witness_valid, sum(1 for f in findings if f.flag == "BLOCKING"), proof_md,
            ),
            verifier_seconds=time.time() - t0,
            findings=findings,
            witness_reason=witness_reason,
            proof_hash=_proof_hash(proof_md),
            critic_metas=critic_metas,
        )
        return result

    items = [
        (name, _render_critic_prompt(name, spec, proof_md, witness_valid=witness_valid))
        for name in CRITIC_NAMES
    ]

    critic_results = call_critics_parallel(
        items,
        timeout_s=CRITIC_TIMEOUT_S,
        use_cache=use_critic_cache,
    )

    for name in CRITIC_NAMES:
        response, meta = critic_results.get(name, (None, {"error": "no result returned"}))
        critic_metas[name] = meta
        if response is None:
            err = meta.get("error", "unknown error")
            findings.append(Finding(
                critic=name, flag="BLOCKING", line_ref=None,
                evidence=f"critic_unavailable: {name}",
                suggestion=str(err)[:300],
            ))
            continue
        parsed, parse_status = _parse_critic_response(response)
        if parsed is None:
            findings.append(Finding(
                critic=name, flag="BLOCKING", line_ref=None,
                evidence=f"critic_unparseable: {name}",
                suggestion=parse_status[:300],
            ))
            continue
        findings.extend(_findings_from_parsed(name, parsed))

    # 3. Numerical check post-processing.
    _evaluate_numerical_findings(findings)

    # 4. Aggregate.
    blocking = sum(1 for f in findings if f.flag == "BLOCKING")
    warn = sum(1 for f in findings if f.flag == "WARN")
    verdict = _compute_verdict_hint(spec, witness_valid, blocking, proof_md)

    return ProofVerifyResult(
        claim_status=spec.get("claim_status", "unknown"),
        witness_valid=witness_valid,
        witness_score=witness_score,
        critic_blocking_count=blocking,
        critic_warn_count=warn,
        verdict_hint=verdict,
        verifier_seconds=time.time() - t0,
        findings=findings,
        witness_reason=witness_reason,
        proof_hash=_proof_hash(proof_md),
        critic_metas=critic_metas,
    )


# Phrases that a proof claiming a partial / conditional result might use. If
# a proof makes none of these hedges and also doesn't trip openness, we treat
# it as "open" (the loop is still running).
_PARTIAL_REGEX = re.compile(
    r"\b(partial result|under the assumption|conditional on|"
    r"this remains open|we have ruled out|we cannot rule out|"
    r"subject to|assuming the truth of)\b",
    re.IGNORECASE,
)


def _compute_verdict_hint(spec: dict, witness_valid: int, blocking: int, proof_md: str) -> str:
    if witness_valid == 1:
        return "counterexample_proven"
    if blocking > 0:
        return "blocked"
    # Defense-in-depth: if proof asserts resolution but no witness, treat as
    # blocked even if the openness critic missed.
    if spec.get("claim_status") == "open":
        resolution_strings = (
            "the assertion is false", "the conjecture is false",
            "we disprove", "this disproves", "we have proven",
            "qed", "resolves the conjecture",
        )
        low = proof_md.lower()
        if any(s in low for s in resolution_strings):
            return "blocked"
    if _PARTIAL_REGEX.search(proof_md):
        return "partial_result"
    return "open"


# --------------------------------------------------------------------------- #
# Output + audit trail
# --------------------------------------------------------------------------- #

def print_summary(proof_md: str, result: ProofVerifyResult) -> None:
    spec = load_proof_spec()
    first_blocking = next(
        (f for f in result.findings if f.flag == "BLOCKING"),
        None,
    )
    reason = result.witness_reason
    if first_blocking is not None:
        reason = f"BLOCKING({first_blocking.critic}): {first_blocking.evidence}"
    elif result.witness_valid == 1:
        reason = f"witness verified: {result.witness_reason}"
    if len(reason) > 200:
        reason = reason[:197] + "..."
    reason = reason.replace("\t", " ").replace("\n", " ")

    score_str = "nan" if math.isnan(result.witness_score) else f"{result.witness_score:.6f}"

    print("---")
    print(f"problem:           {spec.get('name', PROOF_TAG)}")
    print(f"family:            {spec.get('family', 'unknown')}")
    print(f"claim_status:      {result.claim_status}")
    print(f"witness_valid:     {result.witness_valid}")
    print(f"witness_score:     {score_str}")
    print(f"critic_blocking_count: {result.critic_blocking_count}")
    print(f"critic_warn_count: {result.critic_warn_count}")
    print(f"verdict_hint:      {result.verdict_hint}")
    print(f"verifier_seconds:  {result.verifier_seconds:.4f}")
    print(f"reason:            {reason}")

    _append_audit_row(spec, result, reason)


def _append_audit_row(spec: dict, result: ProofVerifyResult, reason: str) -> None:
    commit = _short_commit()
    needs_header = (
        not PROOF_VERIFIER_RESULTS_TSV.exists()
        or PROOF_VERIFIER_RESULTS_TSV.stat().st_size == 0
    )
    score_str = "nan" if math.isnan(result.witness_score) else f"{result.witness_score:.6f}"
    row = [
        commit,
        spec.get("name", PROOF_TAG),
        result.claim_status,
        str(result.witness_valid),
        score_str,
        str(result.critic_blocking_count),
        str(result.critic_warn_count),
        result.verdict_hint,
        f"{result.verifier_seconds:.4f}",
        result.proof_hash,
        reason,
    ]
    header = [
        "commit", "problem", "claim_status", "witness_valid", "witness_score",
        "critic_blocking", "critic_warn", "verdict_hint", "verifier_seconds",
        "proof_hash", "reason",
    ]
    try:
        with open(PROOF_VERIFIER_RESULTS_TSV, "a", encoding="utf-8", newline="") as f:
            if needs_header:
                f.write("\t".join(header) + "\n")
            f.write("\t".join(row) + "\n")
    except OSError as e:
        print(f"WARNING: failed to append audit row: {e}", file=sys.stderr)


# --------------------------------------------------------------------------- #
# CLI entry
# --------------------------------------------------------------------------- #

def main() -> int:
    spec = load_proof_spec()
    if not PROOF_STRATEGY_MD.exists():
        print(f"ERROR: {PROOF_STRATEGY_MD} not found — nothing to verify.", file=sys.stderr)
        return 5
    proof_md = PROOF_STRATEGY_MD.read_text(encoding="utf-8")
    result = verify_proof(proof_md, spec)
    print_summary(proof_md, result)
    return 0


if __name__ == "__main__":
    sys.exit(main())
