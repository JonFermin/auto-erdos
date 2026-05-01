"""proof_session_end.py — checkpoint helper for a Track 2 session.

Run at the END of every agent invocation in the proof loop. The agent
calls this when:
  (a) a logical chunk of work is done, OR
  (b) the token-budget warning fires.

Usage:

    uv run proof_session_end.py "reason: stopping for token budget; next: prove sub-bound (b) of Lemma 2"

The script:
  1. Reads the active session_id from ``.proof_session_active``.
  2. Reads handoff text from stdin (multi-line markdown). If stdin is
     empty/closed (interactive terminal), writes a default handoff template.
  3. Overwrites ``proof_session_handoff.md`` with the new handoff.
  4. Appends a ``session_close`` event to ``proof_journal.jsonl``.
  5. ``git add -A && git commit`` of all dirty journal/handoff/lemma files.
  6. Removes ``.proof_session_active``.

The handoff is the FIRST thing the next session reads; keep it terse and
action-oriented. ≤ 1 page.
"""
from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
JOURNAL = REPO_ROOT / "proof_journal.jsonl"
HANDOFF = REPO_ROOT / "proof_session_handoff.md"
ACTIVE_MARKER = REPO_ROOT / ".proof_session_active"


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _read_active_session_id() -> str | None:
    if not ACTIVE_MARKER.exists():
        return None
    try:
        first_line = ACTIVE_MARKER.read_text(encoding="utf-8").splitlines()[0]
        return first_line.split("\t")[0].strip()
    except (OSError, IndexError):
        return None


def _git_short_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--short=7", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except subprocess.CalledProcessError:
        return "unknown"


def _git_dirty() -> bool:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "status", "--porcelain"],
            stderr=subprocess.DEVNULL,
        )
        return bool(out.strip())
    except subprocess.CalledProcessError:
        return False


def _read_handoff_from_stdin_or_default(reason: str, sid: str) -> str:
    """If stdin is non-tty and has data, read it as the handoff. Otherwise
    write a default template the agent can iterate on next session."""
    handoff_text: str | None = None
    if not sys.stdin.isatty():
        try:
            handoff_text = sys.stdin.read()
        except OSError:
            handoff_text = None
    if handoff_text is None or not handoff_text.strip():
        handoff_text = (
            f"# Session handoff (session {sid})\n\n"
            f"**Stop reason**: {reason}\n\n"
            "**Current focus**: (fill me in next session — what was being worked on)\n\n"
            "**qid in flight**: (fill me in — which qid was claimed but not yet resolved, if any)\n\n"
            "**Obstacle**: (one paragraph describing what blocked progress, if anything)\n\n"
            "**Files modified this session**:\n\n"
            "(see `git log --since='1 hour ago' --name-only` from this commit)\n\n"
            "**Suggested next move**:\n\n"
            "1. Read proof_strategy.md from start to finish.\n"
            "2. Read the most recent open lemma file in proof_lemmas/.\n"
            "3. Run `uv run proof_prepare.py` to see current critic verdict.\n"
            "4. Pick the next open qid and continue.\n"
        )
    return handoff_text


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "reason",
        help='one-line stop reason; should start "reason:" by convention',
    )
    parser.add_argument(
        "--no-commit",
        action="store_true",
        help="skip the auto git-commit (for tests)",
    )
    args = parser.parse_args()
    reason = args.reason.strip().replace("\t", " ").replace("\n", " ")
    if not reason:
        print("ERROR: empty reason", file=sys.stderr)
        return 2

    sid = _read_active_session_id()
    now = _now_iso()
    if sid is None:
        # No active session marker — likely the agent forgot to call
        # proof_session_start.py, or the marker got removed. We can still
        # close the most recent session_open in the journal as a defensive
        # fallback.
        print(
            f"WARNING: no active session marker at {ACTIVE_MARKER}; "
            f"closing most recent session_open in journal anyway.",
            file=sys.stderr,
        )
        sid = "<unknown>"
        if JOURNAL.exists():
            with open(JOURNAL, encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        evt = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if evt.get("event") == "session_open":
                        sid = str(evt.get("session_id", sid))

    handoff_text = _read_handoff_from_stdin_or_default(reason, sid)
    HANDOFF.write_text(handoff_text, encoding="utf-8")

    # Append session_close.
    JOURNAL.parent.mkdir(parents=True, exist_ok=True)
    with open(JOURNAL, "a", encoding="utf-8") as f:
        f.write(
            json.dumps({
                "event": "session_close",
                "session_id": sid,
                "ts": now,
                "commit": _git_short_sha(),
                "reason": reason,
            }, separators=(",", ":")) + "\n"
        )

    # Auto-commit unless suppressed.
    if not args.no_commit and _git_dirty():
        try:
            subprocess.check_call(
                ["git", "-C", str(REPO_ROOT), "add", "-A"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
            subprocess.check_call(
                ["git", "-C", str(REPO_ROOT), "commit", "-m",
                 f"session_close: {sid} — {reason[:120]}"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
            )
        except subprocess.CalledProcessError as e:
            print(
                f"WARNING: auto-commit failed ({e}). "
                f"State is on disk but not yet committed; commit manually before next session.",
                file=sys.stderr,
            )

    # Remove active marker.
    try:
        if ACTIVE_MARKER.exists():
            ACTIVE_MARKER.unlink()
    except OSError:
        pass

    print(f"session_close: {sid} ({reason})")
    return 0


if __name__ == "__main__":
    sys.exit(main())
