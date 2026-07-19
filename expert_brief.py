"""expert_brief.py — render a one-page, standalone statement of the current
minimal open problem from Track 2 state.

When the round loop has reduced a conjecture to a stable minimal open
lemma, that reduction is a valuable artifact even unproven: it is the
right object to show a human expert, post to a forum, or hand to a fresh
ideation fan-out. This script assembles the brief DETERMINISTICALLY from
state on disk (no LLM call, no wall-clock cost):

  - the claim + status + literature anchors from proofs/<PROOF_TAG>.json,
  - every OPEN lemma in proof_lemmas/ (these ARE the minimal open
    problems — the round loop's discipline is that the hard part is
    always isolated into open lemma files),
  - the ruled-out approaches (disproved/abandoned lemmas, frontmatter +
    first paragraph),
  - the tail of the cumulative notes channel.

Usage:

    uv run expert_brief.py                 # writes briefs/<tag>_<date>.md
    uv run expert_brief.py --stdout        # print instead of writing
    PROOF_TAG=erdos_gyarfas uv run expert_brief.py

proof_session_end.py suggests running this when open lemmas have
persisted across 2+ sessions.

Pure stdlib.
"""
from __future__ import annotations

import argparse
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

from proof_prepare import (
    PROOF_TAG,
    PROOF_LEMMAS_DIR,
    _lemma_status,
    load_proof_notes,
    load_proof_spec,
)

REPO_ROOT = Path(__file__).resolve().parent
BRIEFS_DIR = REPO_ROOT / "briefs"

_FRONTMATTER_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n", re.DOTALL)
_ID_RE = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)


def _body_of(text: str) -> str:
    return _FRONTMATTER_RE.sub("", text).strip()


def _first_paragraph(text: str, max_chars: int = 600) -> str:
    body = _body_of(text)
    para = body.split("\n\n", 1)[0].strip()
    if len(para) > max_chars:
        para = para[:max_chars] + " ..."
    return para


def build_brief() -> str:
    spec = load_proof_spec()
    tag = spec.get("name", PROOF_TAG)
    now = datetime.now(timezone.utc).isoformat(timespec="seconds")

    open_lemmas: list[tuple[str, str]] = []       # (id, full body)
    dead_lemmas: list[tuple[str, str, str]] = []  # (id, status, first para)
    if PROOF_LEMMAS_DIR.is_dir():
        for path in sorted(PROOF_LEMMAS_DIR.glob("lemma_*.md")):
            try:
                text = path.read_text(encoding="utf-8")
            except OSError:
                continue
            status = _lemma_status(text)
            m = _ID_RE.search(text)
            lid = m.group(1) if m else path.stem.removeprefix("lemma_")
            if status == "open":
                open_lemmas.append((lid, _body_of(text)))
            elif status in ("disproved", "abandoned"):
                dead_lemmas.append((lid, status, _first_paragraph(text)))

    lines: list[str] = []
    lines.append(f"# Expert brief — {tag}")
    lines.append("")
    lines.append(f"_Generated {now} from auto-erdos Track 2 state. Self-contained; no repo context needed._")
    lines.append("")
    lines.append("## The target claim")
    lines.append("")
    lines.append(f"**Status**: {spec.get('claim_status', 'unknown')}")
    res = spec.get("literature_resolution")
    if res:
        lines.append(f"**Literature resolution**: {res.get('citation', '')}")
    lines.append("")
    lines.append(f"$$ {spec.get('claim_latex', '(no claim_latex in spec)')} $$")
    lines.append("")
    lines.append("## Known facts (with sign discipline)")
    lines.append("")
    for fact in spec.get("given_facts", []):
        lines.append(f"- **{fact.get('id')}** ({fact.get('citation', 'no citation')}): {fact.get('statement', '')}")
    lines.append("")

    lines.append("## The minimal open problem(s)")
    lines.append("")
    if open_lemmas:
        lines.append(
            "The round loop has reduced the difficulty to the following open "
            "lemma(s). Proving any of them (or exhibiting a counterexample to "
            "one) is the current bottleneck:"
        )
        lines.append("")
        for lid, body in open_lemmas:
            lines.append(f"### Open lemma `{lid}`")
            lines.append("")
            lines.append(body)
            lines.append("")
    else:
        lines.append(
            "_No open lemma files on disk — either the attempt is at the "
            "whole-claim stage (no reduction achieved yet) or all lemmas are "
            "discharged. See the notes below for the live state._"
        )
        lines.append("")

    if dead_lemmas:
        lines.append("## Ruled out (do not re-derive)")
        lines.append("")
        for lid, status, para in dead_lemmas:
            lines.append(f"- **`{lid}`** ({status}): {para}")
        lines.append("")

    notes = load_proof_notes()
    if notes:
        tail = notes[-3000:]
        lines.append("## Cross-session notes (tail)")
        lines.append("")
        lines.append("```")
        lines.append(tail.strip())
        lines.append("```")
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    # Windows consoles default to cp1252, which chokes on 'Erdős'.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--stdout", action="store_true", help="print to stdout instead of writing briefs/")
    args = p.parse_args()

    brief = build_brief()
    if args.stdout:
        print(brief)
        return 0

    BRIEFS_DIR.mkdir(parents=True, exist_ok=True)
    date = datetime.now(timezone.utc).strftime("%Y%m%d")
    out = BRIEFS_DIR / f"{PROOF_TAG}_{date}.md"
    out.write_text(brief, encoding="utf-8")
    print(f"wrote {out.relative_to(REPO_ROOT).as_posix()} ({len(brief)} chars)")
    print("Next: hand it to a human expert, post it, or feed it to /erdos-proof-ideation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
