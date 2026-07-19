"""formalize_lemma.py — Lean 4 formalization scaffold for a proved lemma.

Rung 4 of the Track 2 formalization ladder (see proof_program.md):

    1. exploration      — markdown + LaTeX in proof_lemmas/
    2. critic screen    — 7-critic pass clean at a logical milestone
    3. numeric screen   — <!-- CHECK --> probes pass deterministically
    4. Lean skeleton    — THIS SCRIPT: render prompts/lean_formalize.md
                          against one lemma file, shell out to `claude -p`
                          (same backend pattern as write_paper.py), write
                          lean/<tag>__<lemma_id>.lean + .meta.json sidecar
    5. human compile    — a human (or CI with a Lean toolchain) runs
                          `lake build` against mathlib4 and audits the
                          FIDELITY NOTES / remaining `sorry`s

The script does NOT run Lean — the toolchain isn't assumed on this
machine. Its value is (a) a faithful formal statement is the strongest
screen for quantifier/sign errors that LLM critics miss, and (b) the
prompt instructs the model to report `-- DEFECT FOUND:` when the informal
statement doesn't survive formalization, which is a first-class result
for the loop (set the lemma's status accordingly).

Usage:

    uv run formalize_lemma.py proof_lemmas/lemma_stratum_sub_bound.md
    uv run formalize_lemma.py proof_lemmas/lemma_x.md --opus-model claude-opus-4-7 --force

Outputs:

    lean/<PROOF_TAG>__<lemma_id>.lean
    lean/<PROOF_TAG>__<lemma_id>.meta.json   (prompt/template/response hashes,
                                              CLI invocation, timestamps —
                                              same provenance chain as papers/)

Pure stdlib. Reuses write_paper's CLI-shelling helpers.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from proof_prepare import PROOF_TAG, load_proof_spec, _lemma_status
from write_paper import call_opus, DEFAULT_OPUS_MODEL

REPO_ROOT = Path(__file__).resolve().parent
PROMPTS_DIR = REPO_ROOT / "prompts"
LEAN_DIR = REPO_ROOT / "lean"
TEMPLATE_PATH = PROMPTS_DIR / "lean_formalize.md"

_ID_RE = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
_LEAN_FENCE_RE = re.compile(r"```lean\s*\n(.*?)\n```", re.DOTALL)


def _lemma_id(text: str, fallback: str) -> str:
    m = _ID_RE.search(text)
    return m.group(1) if m else fallback


def _extract_lean(response: str) -> tuple[str, str]:
    """Return (body, extraction_mode). Prefer a ```lean fence; fall back to
    the raw response (flagged in meta so a human notices)."""
    m = _LEAN_FENCE_RE.search(response)
    if m:
        return m.group(1).strip() + "\n", "fenced-lean"
    return response.strip() + "\n", "raw"


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("lemma_file", help="path to proof_lemmas/lemma_*.md")
    p.add_argument("--opus-model", default=DEFAULT_OPUS_MODEL,
                   help=f"Anthropic model id (default {DEFAULT_OPUS_MODEL})")
    p.add_argument("--force", action="store_true", help="overwrite existing output")
    args = p.parse_args()

    lemma_path = Path(args.lemma_file)
    if not lemma_path.is_absolute():
        lemma_path = REPO_ROOT / lemma_path
    if not lemma_path.exists():
        print(f"ERROR: lemma file not found: {lemma_path}", file=sys.stderr)
        return 2

    lemma_text = lemma_path.read_text(encoding="utf-8")
    status = _lemma_status(lemma_text)
    if status in ("disproved", "abandoned"):
        print(
            f"ERROR: lemma has status '{status}' — formalizing a dead lemma is wasted "
            f"wall-clock. (Override by editing the frontmatter if you really mean it.)",
            file=sys.stderr,
        )
        return 2
    if status != "proved":
        print(
            f"NOTE: lemma status is '{status}' (not 'proved'). Proceeding — a faithful "
            f"formal STATEMENT of an open lemma is still useful — but the ladder's "
            f"intent is to formalize proved lemmas.",
            file=sys.stderr,
        )

    lid = _lemma_id(lemma_text, lemma_path.stem.removeprefix("lemma_"))
    spec = load_proof_spec()

    template_text = TEMPLATE_PATH.read_text(encoding="utf-8")
    template_sha = hashlib.sha256(template_text.encode("utf-8")).hexdigest()
    rendered = template_text.format(
        problem_tag=spec.get("name", PROOF_TAG),
        claim_latex=spec.get("claim_latex", ""),
        lemma_id=lid,
        lemma_status=status,
        lemma_body=lemma_text,
    )
    prompt_sha = hashlib.sha256(rendered.encode("utf-8")).hexdigest()

    lean_path = LEAN_DIR / f"{spec.get('name', PROOF_TAG)}__{lid}.lean"
    meta_path = lean_path.with_suffix(".meta.json")
    if lean_path.exists() and not args.force:
        print(f"skip: {lean_path.name} exists (use --force to overwrite)", file=sys.stderr)
        return 0

    LEAN_DIR.mkdir(parents=True, exist_ok=True)
    print(
        f"formalize_lemma: {lemma_path.name} → {lean_path.name} "
        f"(model={args.opus_model}, prompt={len(rendered)}c)",
        file=sys.stderr,
    )

    try:
        stdout, cmd, rc, dur = call_opus(rendered, args.opus_model)
    except RuntimeError as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1
    response_sha = hashlib.sha256(stdout.encode("utf-8")).hexdigest()
    if rc != 0:
        print(f"ERROR: claude CLI exited {rc} after {dur:.1f}s — no file written", file=sys.stderr)
        return 1

    body, extraction_mode = _extract_lean(stdout)
    lean_path.write_text(body, encoding="utf-8")

    defect_found = "DEFECT FOUND" in body
    meta = {
        "lemma_file": lemma_path.name,
        "lemma_id": lid,
        "lemma_status_at_formalization": status,
        "lemma_sha256": hashlib.sha256(lemma_text.encode("utf-8")).hexdigest(),
        "problem": spec.get("name", PROOF_TAG),
        "model_id_requested": args.opus_model,
        "cli_invocation": cmd,
        "prompt_template_path": TEMPLATE_PATH.relative_to(REPO_ROOT).as_posix(),
        "prompt_template_sha256": template_sha,
        "rendered_prompt_sha256": prompt_sha,
        "response_sha256": response_sha,
        "extraction_mode": extraction_mode,
        "sorry_count": body.count("sorry"),
        "defect_found": defect_found,
        "duration_seconds": round(dur, 2),
        "written_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": "NOT compiled — run `lake build` with mathlib4 and audit FIDELITY NOTES before trusting.",
    }
    meta_path.write_text(json.dumps(meta, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    print(
        f"wrote {lean_path.name} ({len(body)}c, sorries={meta['sorry_count']}, "
        f"extraction={extraction_mode}, {dur:.1f}s)"
    )
    if defect_found:
        print(
            "DEFECT FOUND: the formalizer reports the informal statement does not "
            "survive formalization — read the file's header comment and update the "
            "lemma's status/body accordingly. This is a result, not an error.",
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
