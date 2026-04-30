"""
write_paper.py — generate an amsart LaTeX writeup of a kept record.

Given a `records/<tag>_<score>_<commit>.json` produced by `log_result.py`,
this script renders the frozen prompt at `prompts/paper_writeup.md` with
problem-specific values, shells out to one or more model CLIs (Claude
`claude -p`, OpenAI Codex `codex exec`), and writes the resulting paper
plus a sidecar reproducibility manifest.

The artifacts:

    papers/<tag>_<score>_<commit>__<model>.tex
    papers/<tag>_<score>_<commit>__<model>.meta.json

The .meta.json captures: rendered-prompt sha256, frozen-template sha256,
model id requested, full CLI invocation, response sha256, run timestamp,
duration, exit code. Together with the `records/*.json` (verified
candidate) and the prompt template (committed), this is the whole
provenance chain — anyone with this repo can rerun and audit.

Reproducibility caveat: language models are non-deterministic. "Same
inputs → similar paper" is the goal, not bit-identical output. The chain
of hashes lets a future reader verify *which* prompt and record produced
*which* response.

Usage:

    uv run write_paper.py records/capset_n8_137_a1b2c3d.json
        --models opus,codex

    uv run write_paper.py records/sidon_500_26_a1c1c6b.json
        --models opus
        --opus-model claude-opus-4-7
        --force                      # overwrite existing paper

    uv run write_paper.py --all      # process every record without a paper

Pure stdlib (subprocess, hashlib, json) — no new dependencies.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
PROMPTS_DIR = REPO_ROOT / "prompts"
RECORDS_DIR = REPO_ROOT / "records"
PAPERS_DIR = REPO_ROOT / "papers"
PROBLEMS_DIR = REPO_ROOT / "problems"

PROMPT_TEMPLATE_PATH = PROMPTS_DIR / "paper_writeup.md"

# Model preset registry. Each preset maps a short alias the user types
# (`opus`, `codex`) to: the CLI invocation builder, the default model id,
# and the filename suffix. Keep this small and stable — adding a new
# backend is a deliberate code change, not config.
DEFAULT_OPUS_MODEL = "claude-opus-4-7"
DEFAULT_CODEX_MODEL: str | None = None  # use codex's configured default

# Hard cap on candidate-block size in the rendered prompt. Bigger than
# this and we abbreviate (still include sha256 of the full set so the
# model can be told the exact construction is on disk). Picked to keep
# typical capset_n10 writeups under ~64KB of prompt.
CANDIDATE_BLOCK_MAX_CHARS = 64_000


# --------------------------------------------------------------------------- #
# Rendering the prompt
# --------------------------------------------------------------------------- #

def _format_capset_candidate(candidate: list, n: int) -> str:
    """Format a capset candidate as a base-3 dump.

    Each point in F_3^n becomes a length-n string of digits {0,1,2}.
    Example for n=4: ["0000", "0011", ...]. Compact and readable; the
    LaTeX writer can re-encode as it likes.
    """
    if not candidate:
        return "_(empty set)_"
    encoded = []
    for pt in candidate:
        if not isinstance(pt, (list, tuple)) or len(pt) != n:
            raise ValueError(f"capset point has wrong shape: {pt!r} (expected length {n})")
        encoded.append("".join(str(int(c)) for c in pt))
    body = " ".join(encoded)
    return (
        f"The set consists of {len(encoded)} points in F_3^{n}, each written "
        f"as a length-{n} base-3 string (digit i is the i-th coordinate, 0-indexed):\n\n"
        f"```\n{body}\n```"
    )


def _format_sidon_candidate(candidate: list, N: int) -> str:
    if not candidate:
        return "_(empty set)_"
    ints = [int(x) for x in candidate]
    body = ", ".join(str(x) for x in ints)
    return (
        f"The set consists of {len(ints)} integers in the interval [1, {N}]:\n\n"
        f"```\n{{{body}}}\n```"
    )


def _abbreviate_if_huge(block: str, candidate_sha: str) -> str:
    if len(block) <= CANDIDATE_BLOCK_MAX_CHARS:
        return block
    head = block[: CANDIDATE_BLOCK_MAX_CHARS // 2]
    tail = block[-CANDIDATE_BLOCK_MAX_CHARS // 4 :]
    return (
        head
        + "\n\n"
        + f"... [{len(block) - CANDIDATE_BLOCK_MAX_CHARS} characters elided to fit prompt budget; "
        f"the SHA-256 of the full candidate JSON is `{candidate_sha}`] ...\n\n"
        + tail
    )


def _problem_statement(spec: dict) -> str:
    family = spec.get("family")
    if family == "capset":
        n = int(spec["n"])
        return (
            f"A *cap set* in the vector space F_3^{n} is a subset S such that no "
            f"three distinct points a, b, c in S satisfy a + b + c = 0 elementwise "
            f"in F_3 (equivalently, S contains no three-term arithmetic progression). "
            f"The problem is to determine, or to lower-bound, the maximum size of "
            f"such a set."
        )
    if family == "sidon":
        N = int(spec["N"])
        return (
            f"A *Sidon set* (or B_2 set) in the interval [1, {N}] is a set S of "
            f"distinct positive integers such that all pairwise sums a + b with "
            f"a, b in S, a < b, are distinct. The problem is to determine, or to "
            f"lower-bound, the maximum size of such a set."
        )
    raise ValueError(f"unknown family: {family!r}")


def render_prompt(record: dict, spec: dict, template: str) -> tuple[str, dict]:
    """Render the frozen template with values from a record + spec.

    Returns (rendered_prompt, debug_meta). The meta dict is plumbed
    into the .meta.json sidecar so we know exactly what was substituted.
    """
    family = spec.get("family")
    candidate = record.get("candidate")
    if not record.get("candidate_available") or candidate is None:
        raise ValueError(
            "record has no candidate available — prepare.py's per-run cache "
            "was missing or stale at log_result time. Cannot write a paper."
        )

    if family == "capset":
        n = int(spec["n"])
        candidate_block = _format_capset_candidate(candidate, n)
        problem_param = f"n={n}"
    elif family == "sidon":
        N = int(spec["N"])
        candidate_block = _format_sidon_candidate(candidate, N)
        problem_param = f"N={N}"
    else:
        raise ValueError(f"unknown family: {family!r}")

    candidate_sha = hashlib.sha256(
        json.dumps(candidate, sort_keys=True).encode("utf-8")
    ).hexdigest()
    candidate_block = _abbreviate_if_huge(candidate_block, candidate_sha)

    score = int(record["score"])
    baseline = int(record["baseline"])
    improvement = score - baseline

    fields = {
        "problem_tag": record["problem"],
        "problem_family": family,
        "problem_param": problem_param,
        "baseline": str(baseline),
        "score": str(score),
        "improvement": str(improvement),
        "problem_statement": _problem_statement(spec),
        "candidate_block": candidate_block,
        "verifier_summary": (
            f"valid {family} set of size {score} "
            f"({'in F_3^' + str(spec.get('n')) if family == 'capset' else 'in [1,' + str(spec.get('N')) + ']'})"
        ),
        "branch": record.get("branch", "unknown"),
        "commit": record.get("commit", "unknown"),
    }

    rendered = template.format(**fields)
    meta = {
        "candidate_sha256": candidate_sha,
        "score": score,
        "baseline": baseline,
        "improvement": improvement,
        "n_or_N": int(spec.get("n", spec.get("N", 0))),
        "rendered_prompt_chars": len(rendered),
    }
    return rendered, meta


# --------------------------------------------------------------------------- #
# Model invocation
# --------------------------------------------------------------------------- #

def _check_cli(name: str) -> str:
    """Return the resolved CLI path or raise with a useful error."""
    path = shutil.which(name)
    if not path:
        raise RuntimeError(
            f"`{name}` is not on PATH. Install it (or skip this model with "
            f"--models flag). Common locations: claude → @anthropic-ai/claude-code "
            f"npm package; codex → @openai/codex npm package."
        )
    return path


def call_opus(prompt: str, model: str) -> tuple[str, list[str], int, float]:
    """Invoke `claude -p` with web/file tools disabled, return its stdout.

    --output-format text → no JSON wrapping, just the model's prose.
    --disallowedTools → strips tools that would let the model read the
    filesystem or browse; the prompt requests "no internet" so this
    enforces it from outside.
    """
    _check_cli("claude")
    disallowed = (
        "Bash Edit Write Glob Grep Read WebFetch WebSearch Skill Agent "
        "NotebookEdit TaskCreate"
    )
    cmd = [
        "claude", "-p",
        "--model", model,
        "--output-format", "text",
        "--disallowedTools", disallowed,
    ]
    return _run_with_stdin(cmd, prompt)


def call_codex(prompt: str, model: str | None) -> tuple[str, list[str], int, float]:
    """Invoke `codex exec` with read-only sandbox, return its stdout.

    --sandbox read-only → model can't write the filesystem.
    --skip-git-repo-check → robust whether or not run inside a repo.
    Model defaults to whatever codex config has if `model` is None.
    """
    _check_cli("codex")
    cmd = [
        "codex", "exec",
        "--sandbox", "read-only",
        "--skip-git-repo-check",
    ]
    if model:
        cmd += ["-m", model]
    cmd.append("-")
    return _run_with_stdin(cmd, prompt)


def _run_with_stdin(cmd: list[str], stdin_text: str) -> tuple[str, list[str], int, float]:
    """Run a CLI with stdin_text on stdin, return (stdout, cmd, returncode, duration_s)."""
    started = time.time()
    proc = subprocess.run(
        cmd,
        input=stdin_text,
        text=True,
        capture_output=True,
        encoding="utf-8",
        errors="replace",
    )
    duration = time.time() - started
    return proc.stdout, cmd, proc.returncode, duration


# --------------------------------------------------------------------------- #
# LaTeX extraction
# --------------------------------------------------------------------------- #

def extract_latex(response: str) -> tuple[str, str]:
    """Extract a LaTeX block from a model response.

    Strategy: look for a fenced code block whose tag is `latex` or `tex`.
    If none, look for a fenced block whose contents start with
    `\\documentclass`. If none, return the raw response and a `mode`
    string telling the caller what happened.
    """
    lines = response.splitlines(keepends=True)
    in_block = False
    fence_tag = None
    block_start = -1
    blocks: list[tuple[str, str]] = []  # (tag, body)
    body: list[str] = []

    for i, line in enumerate(lines):
        stripped = line.lstrip()
        if stripped.startswith("```"):
            if not in_block:
                in_block = True
                fence_tag = stripped[3:].strip().lower()
                block_start = i
                body = []
            else:
                blocks.append((fence_tag or "", "".join(body)))
                in_block = False
                fence_tag = None
                body = []
        elif in_block:
            body.append(line)

    # Prefer explicit latex/tex tag.
    for tag, b in blocks:
        if tag in ("latex", "tex"):
            return b.strip() + "\n", "fenced-tagged"

    # Fall back to any block whose body looks like LaTeX.
    for tag, b in blocks:
        if "\\documentclass" in b:
            return b.strip() + "\n", "fenced-untagged"

    # Last resort: return the whole response and let the caller flag it.
    return response.strip() + "\n", "raw"


# --------------------------------------------------------------------------- #
# Orchestration
# --------------------------------------------------------------------------- #

def _load_record(path: Path) -> dict:
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def _load_spec(tag: str) -> dict:
    spec_path = PROBLEMS_DIR / f"{tag}.json"
    if not spec_path.exists():
        raise FileNotFoundError(f"problem spec not found: {spec_path}")
    with open(spec_path, encoding="utf-8") as f:
        return json.load(f)


def _paper_paths(record: dict, model_id: str) -> tuple[Path, Path]:
    tag = record["problem"]
    score = int(record["score"])
    commit = str(record["commit"])
    safe_model = model_id.replace("/", "-").replace(" ", "-")
    base = f"{tag}_{score}_{commit}__{safe_model}"
    return PAPERS_DIR / f"{base}.tex", PAPERS_DIR / f"{base}.meta.json"


def write_paper(
    record_path: Path,
    *,
    model_alias: str,
    opus_model: str,
    codex_model: str | None,
    force: bool,
) -> tuple[bool, str]:
    """Generate one paper for one model. Returns (ok, message).

    Failures (CLI missing, non-zero exit, etc.) return ok=False with a
    message; the caller decides whether to abort or skip to the next
    model.
    """
    record = _load_record(record_path)
    spec = _load_spec(record["problem"])

    template_text = PROMPT_TEMPLATE_PATH.read_text(encoding="utf-8")
    template_sha = hashlib.sha256(template_text.encode("utf-8")).hexdigest()
    rendered, render_meta = render_prompt(record, spec, template_text)
    prompt_sha = hashlib.sha256(rendered.encode("utf-8")).hexdigest()

    if model_alias == "opus":
        model_id = opus_model
    elif model_alias == "codex":
        model_id = codex_model or "codex-default"
    else:
        return False, f"unknown model alias: {model_alias!r}"

    tex_path, meta_path = _paper_paths(record, model_id)
    if tex_path.exists() and not force:
        return False, f"skip: {tex_path.name} exists (use --force to overwrite)"

    PAPERS_DIR.mkdir(parents=True, exist_ok=True)

    print(
        f"write_paper: {record_path.name} → {tex_path.name} "
        f"(model={model_id}, prompt={len(rendered)}c)",
        file=sys.stderr,
    )

    try:
        if model_alias == "opus":
            stdout, cmd, rc, dur = call_opus(rendered, opus_model)
        else:
            stdout, cmd, rc, dur = call_codex(rendered, codex_model)
    except RuntimeError as e:
        return False, str(e)

    response_sha = hashlib.sha256(stdout.encode("utf-8")).hexdigest()
    if rc != 0:
        return False, (
            f"{model_alias} CLI exited {rc} after {dur:.1f}s "
            f"(stdout sha256 {response_sha[:12]}, no paper written)"
        )

    latex, mode = extract_latex(stdout)
    tex_path.write_text(latex, encoding="utf-8")

    meta = {
        "record": record_path.name,
        "record_problem": record["problem"],
        "record_score": int(record["score"]),
        "record_commit": record["commit"],
        "record_branch": record.get("branch"),
        "model_alias": model_alias,
        "model_id_requested": model_id,
        "cli_invocation": cmd,
        "prompt_template_path": PROMPT_TEMPLATE_PATH.relative_to(REPO_ROOT).as_posix(),
        "prompt_template_sha256": template_sha,
        "rendered_prompt_sha256": prompt_sha,
        "response_sha256": response_sha,
        "extraction_mode": mode,
        "duration_seconds": round(dur, 2),
        "exit_code": rc,
        "written_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "render_meta": render_meta,
    }
    meta_path.write_text(
        json.dumps(meta, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    return True, (
        f"wrote {tex_path.name} ({len(latex)}c, extraction={mode}, "
        f"{dur:.1f}s, exit={rc})"
    )


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #

def _parse_models(s: str) -> list[str]:
    raw = [x.strip().lower() for x in s.split(",") if x.strip()]
    valid = {"opus", "codex"}
    bad = [x for x in raw if x not in valid]
    if bad:
        raise argparse.ArgumentTypeError(
            f"unknown model(s): {bad}. Valid: {sorted(valid)}"
        )
    if not raw:
        raise argparse.ArgumentTypeError("--models cannot be empty")
    return raw


def _records_without_papers() -> list[Path]:
    out: list[Path] = []
    for p in sorted(RECORDS_DIR.glob("*.json")):
        record = _load_record(p)
        score = int(record.get("score", 0))
        commit = str(record.get("commit", ""))
        tag = record.get("problem", "")
        if not (tag and commit):
            continue
        # If at least one paper exists for this record, consider it covered.
        if any(PAPERS_DIR.glob(f"{tag}_{score}_{commit}__*.tex")):
            continue
        out.append(p)
    return out


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("record", nargs="?", help="path to records/*.json")
    p.add_argument("--all", action="store_true",
                   help="process every record without an existing paper")
    p.add_argument("--models", type=_parse_models, default=["opus", "codex"],
                   help="comma-separated model aliases (opus, codex). default: opus,codex")
    p.add_argument("--opus-model", default=DEFAULT_OPUS_MODEL,
                   help=f"Anthropic model id (default {DEFAULT_OPUS_MODEL})")
    p.add_argument("--codex-model", default=DEFAULT_CODEX_MODEL,
                   help="OpenAI Codex model id (default: codex's configured default)")
    p.add_argument("--force", action="store_true",
                   help="overwrite existing papers")
    args = p.parse_args()

    if args.all and args.record:
        print("ERROR: pass either a record path or --all, not both", file=sys.stderr)
        return 2
    if not args.all and not args.record:
        print("ERROR: pass a record path or --all", file=sys.stderr)
        return 2

    if args.all:
        targets = _records_without_papers()
        if not targets:
            print("write_paper: no records without papers found.")
            return 0
        print(f"write_paper: {len(targets)} record(s) to process.", file=sys.stderr)
    else:
        path = Path(args.record)
        if not path.is_absolute():
            path = REPO_ROOT / path
        if not path.exists():
            print(f"ERROR: record not found: {path}", file=sys.stderr)
            return 2
        targets = [path]

    fails = 0
    for record_path in targets:
        for model_alias in args.models:
            ok, msg = write_paper(
                record_path,
                model_alias=model_alias,
                opus_model=args.opus_model,
                codex_model=args.codex_model,
                force=args.force,
            )
            print(f"  [{model_alias}] {msg}", file=sys.stderr)
            if not ok and "skip:" not in msg:
                fails += 1
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
