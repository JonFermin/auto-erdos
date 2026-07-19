"""proof_notes.py — CLI for the Track 2 cumulative notes channel.

The notes file (``~/.cache/auto-erdos/proof_notes_<PROOF_TAG>.md``) is the
ONE cross-branch, cross-session knowledge channel for proof attempts.
Session handoffs are per-branch and capped at one page; this file is where
insight compounds. Append to it whenever you:

  - kill an approach (record WHY it failed and what would revive it),
  - restate the current minimal open lemma,
  - learn something from the literature,
  - pin down a numerical constant future sessions will need.

Usage:

    uv run proof_notes.py                       # print accumulated notes
    uv run proof_notes.py "approach X failed because ..."   # append a note
    PROOF_TAG=erdos_gyarfas uv run proof_notes.py "..."     # other problem

Notes are append-only by convention — do not rewrite history; supersede a
stale note with a newer dated section.
"""
from __future__ import annotations

import sys

from proof_prepare import PROOF_TAG, append_proof_notes, load_proof_notes


def main() -> int:
    # Windows consoles default to cp1252, which chokes on 'Erdős'.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    args = sys.argv[1:]
    if not args:
        notes = load_proof_notes()
        if not notes:
            print(f"(no proof notes yet for {PROOF_TAG})")
        else:
            print(notes)
        return 0
    text = " ".join(args).strip()
    if not text:
        print("ERROR: empty note", file=sys.stderr)
        return 2
    append_proof_notes(text)
    print(f"appended to proof_notes_{PROOF_TAG}.md ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
