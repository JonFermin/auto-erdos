"""proof_session_end.py — checkpoint helper for a Track 2 session.

Run at the END of every agent invocation in the proof loop. The agent
calls this when:
  (a) a logical chunk of work is done, OR
  (b) the token-budget warning fires.

Usage:

    uv run proof_session_end.py "reason: stopping for token budget; next: prove sub-bound (b) of Lemma 2"

The script:
  1. Reads the active session_id (and proof_tag) from ``.proof_session_active``.
  2. Reads handoff text from stdin (multi-line markdown). If stdin is
     empty/closed (interactive terminal), writes a default handoff template.
  3. Overwrites ``proof_session_handoff.md`` with the new handoff.
  4. Archives ``proof_strategy.md`` to ``strategies/<problem>/<session>.md``
     and regenerates that folder's ``INDEX.md`` (parallel-merge insurance —
     see ``_archive_strategy``).
  5. Appends a ``session_close`` event to ``proof_journal.jsonl``.
  6. ``git add -A && git commit`` of all dirty journal/handoff/lemma files.
  7. Removes ``.proof_session_active``.
  8. Pushes the session branch to origin and opens a draft PR if none
     exists (best-effort; ``--no-push`` / ``AUTOERDOS_NO_PUSH=1`` skips).
     Unpublished branches are how results go invisible — a verified
     disproof once sat unpushed in a local worktree for days.

The handoff is the FIRST thing the next session reads; keep it terse and
action-oriented. ≤ 1 page.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
JOURNAL = REPO_ROOT / "proof_journal.jsonl"
HANDOFF = REPO_ROOT / "proof_session_handoff.md"
ACTIVE_MARKER = REPO_ROOT / ".proof_session_active"
STRATEGY = REPO_ROOT / "proof_strategy.md"
STRATEGIES_DIR = REPO_ROOT / "strategies"


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


def _read_marker_proof_tag() -> str | None:
    """Third whitespace-separated field of the active marker (written by
    proof_session_start); None on old two-field markers or no marker."""
    if not ACTIVE_MARKER.exists():
        return None
    try:
        parts = ACTIVE_MARKER.read_text(encoding="utf-8").splitlines()[0].split()
        return parts[2] if len(parts) >= 3 else None
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


def _git_current_branch() -> str | None:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--abbrev-ref", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip() or None
    except (subprocess.CalledProcessError, OSError):
        return None


def _git_dirty() -> bool:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "status", "--porcelain"],
            stderr=subprocess.DEVNULL,
        )
        return bool(out.strip())
    except subprocess.CalledProcessError:
        return False


def _archive_strategy(sid: str, proof_tag: str) -> str | None:
    """Snapshot proof_strategy.md to strategies/<problem>/<session>.md and
    regenerate that folder's INDEX.md.

    This is what makes parallel-branch merges mechanical: proof_strategy.md
    is one mutable document that every session rewrites, so concurrent
    branches always conflict on it. With every session's full narrative
    archived here (append-only, distinct filenames), the documented merge
    policy for proof_strategy.md conflicts is simply "keep the version
    whose session_close is newest" — nothing is lost.
    """
    if not STRATEGY.exists():
        return None
    safe_sid = re.sub(r"[^A-Za-z0-9_-]", "-", sid or "unknown")
    dest_dir = STRATEGIES_DIR / (proof_tag or "unknown")
    try:
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = dest_dir / (safe_sid + ".md")
        stamp = (
            f"<!-- archived by proof_session_end: session {sid} "
            f"at {_now_iso()} -->\n"
        )
        dest.write_text(stamp + STRATEGY.read_text(encoding="utf-8"),
                        encoding="utf-8")
        names = sorted(q.name for q in dest_dir.glob("*.md") if q.name != "INDEX.md")
        index_lines = [
            f"# Strategy archive — {proof_tag or 'unknown'}",
            "",
            "One snapshot of `proof_strategy.md` per closed session, written by",
            "`proof_session_end.py`. The newest session is the current narrative.",
            "Merge policy for `proof_strategy.md` conflicts: keep the newer",
            "session_close's version — every session's narrative survives here.",
            "",
        ] + [f"- {n}" for n in names]
        (dest_dir / "INDEX.md").write_text("\n".join(index_lines) + "\n",
                                           encoding="utf-8")
        return dest.relative_to(REPO_ROOT).as_posix()
    except OSError as e:
        print(f"WARNING: strategy archive failed: {e}", file=sys.stderr)
        return None


def _push_and_open_pr(reason: str, sid: str) -> None:
    """Publish the session branch and make sure a PR exists for it.

    Best-effort by design — a session close must never fail on a missing
    network or gh CLI. But silent non-publication is how results go
    invisible, so every skip prints its reason.
    """
    if os.environ.get("AUTOERDOS_NO_PUSH", "").lower() in ("1", "on", "true"):
        print("push: skipped (AUTOERDOS_NO_PUSH is set)")
        return
    branch = _git_current_branch()
    if branch in (None, "HEAD", "master", "main"):
        print(f"push: skipped (on {branch!r} — session work belongs on a session branch)")
        return
    try:
        subprocess.check_call(
            ["git", "-C", str(REPO_ROOT), "remote", "get-url", "origin"],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
        )
    except (subprocess.CalledProcessError, OSError):
        print("push: skipped (no origin remote)")
        return
    try:
        subprocess.check_call(
            ["git", "-C", str(REPO_ROOT), "push", "--quiet", "-u", "origin", branch],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120,
        )
        print(f"push: {branch} -> origin")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as e:
        print(
            f"WARNING: push failed ({e}) — publish manually: git push -u origin {branch}",
            file=sys.stderr,
        )
        return
    gh = shutil.which("gh")
    if gh is None:
        print("pr: skipped (gh not on PATH) — open one manually", file=sys.stderr)
        return
    try:
        subprocess.check_call(
            [gh, "pr", "view", branch],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=60,
        )
        print(f"pr: {branch} already has a PR")
        return
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError):
        pass
    title = f"auto-erdos PROOF: {branch} — {reason[:80]}"
    body = (
        f"Automated session-close PR for session {sid}.\n\n"
        f"Stop reason: {reason}\n\n"
        "Opened by proof_session_end.py so parallel-session results are always "
        "visible on GitHub. The archived strategy narrative for this session is "
        "under strategies/<problem>/."
    )
    try:
        subprocess.check_call(
            [gh, "pr", "create", "--draft", "--head", branch, "--base", "master",
             "--title", title, "--body", body],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=120,
        )
        print(f"pr: draft PR opened for {branch}")
    except (subprocess.CalledProcessError, subprocess.TimeoutExpired, OSError) as e:
        print(f"WARNING: gh pr create failed ({e}) — open one manually.", file=sys.stderr)


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
    # Windows consoles default to cp1252, which chokes on math glyphs.
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
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
    parser.add_argument(
        "--no-push",
        action="store_true",
        help="skip the branch push + draft PR (also: AUTOERDOS_NO_PUSH=1)",
    )
    args = parser.parse_args()
    reason = args.reason.strip().replace("\t", " ").replace("\n", " ")
    if not reason:
        print("ERROR: empty reason", file=sys.stderr)
        return 2

    sid = _read_active_session_id()
    proof_tag = _read_marker_proof_tag() or os.environ.get("PROOF_TAG", "primitive_set_erdos")
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

    # Archive this session's strategy narrative (parallel-merge insurance;
    # survives any later semantic merge of the shared proof_strategy.md).
    archived = _archive_strategy(sid, proof_tag)
    if archived:
        print(f"strategy archived: {archived}")

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

    # Publish the branch (after the commit so the push carries it).
    if not args.no_push:
        _push_and_open_pr(reason, sid)

    print(f"session_close: {sid} ({reason})")
    _maybe_suggest_expert_brief()
    return 0


def _maybe_suggest_expert_brief() -> None:
    """If open lemmas exist and this problem has already burned 2+ sessions,
    the reduction is stable enough to be worth showing a human — say so.
    Best-effort: never let this break session close."""
    try:
        lemmas_dir = REPO_ROOT / "proof_lemmas"
        open_lemmas = []
        if lemmas_dir.is_dir():
            status_re = re.compile(r"^status:\s*(\w+)\s*$", re.MULTILINE)
            for p in lemmas_dir.glob("lemma_*.md"):
                m = status_re.search(p.read_text(encoding="utf-8"))
                if m and m.group(1).lower() == "open":
                    open_lemmas.append(p.name)
        if not open_lemmas:
            return
        closes = 0
        if JOURNAL.exists():
            with open(JOURNAL, encoding="utf-8") as f:
                for line in f:
                    if '"session_close"' in line:
                        closes += 1
        if closes >= 2:
            print(
                f"HINT: {len(open_lemmas)} open lemma(s) have now survived {closes} sessions "
                f"({', '.join(sorted(open_lemmas)[:3])}{'...' if len(open_lemmas) > 3 else ''}). "
                f"A stable reduction is an artifact worth escalating: run "
                f"`uv run expert_brief.py` to render a standalone one-page statement "
                f"for a human expert or a fresh /erdos-proof-ideation pass."
            )
    except Exception:  # noqa: BLE001 — advisory only
        return


if __name__ == "__main__":
    sys.exit(main())
