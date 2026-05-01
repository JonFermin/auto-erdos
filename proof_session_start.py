"""proof_session_start.py — boot helper for a Track 2 proof-attempt session.

Run at the start of EVERY agent invocation in the proof loop. This is the
load-bearing resumability primitive: a fresh agent (after token cap, crash,
or interrupt) reads only the files this script prints to stdout and the
files it points at, with no memory of prior conversations.

It does the following, in order:

  1. Generate a fresh session_id (e.g. ``s_0430-143055``).
  2. Detect a dirty tree (uncommitted edits left by a crashed prior session).
     If found, ``git stash push`` into a labelled ref ``proof-wip-<sha>``
     (NEVER discard) and report what was stashed.
  3. Detect a stale ``session_open`` event in ``proof_journal.jsonl`` with
     no matching ``session_close`` — i.e. the previous session ended
     abnormally. Append a synthetic ``session_abandoned`` event referencing
     the orphan session_id and auto-release any open_questions still
     ``claimed`` by that session.
  4. Append a ``session_open`` event with the new session_id.
  5. Print to stdout (in this order, with clear separators):
        - the new session_id
        - the contents of ``proof_session_handoff.md`` (or "no handoff yet"
          on a cold first start)
        - the top-N currently-open items in ``proof_open_questions.jsonl``
        - the most recent ``session_close`` reason (if any)

The agent's prompt boilerplate runs this script and treats its stdout as
the entire context for the new session.

Read-only-ish: this script writes only to ``proof_journal.jsonl`` and
``proof_open_questions.jsonl`` (both append-only) and ``proof_session_active``
(one-line marker file, gitignored). It never edits proof_strategy.md or any
lemma file.
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
OPEN_QUESTIONS = REPO_ROOT / "proof_open_questions.jsonl"
HANDOFF = REPO_ROOT / "proof_session_handoff.md"
ACTIVE_MARKER = REPO_ROOT / ".proof_session_active"  # gitignored, one line

PROOF_TAG = os.environ.get("PROOF_TAG", "primitive_set_erdos")


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _new_session_id() -> str:
    # 4-hex random suffix prevents collisions when two starts land in the
    # same second (relevant in tests, but also during a fast restart loop).
    rnd = os.urandom(2).hex()
    return "s_" + datetime.now().strftime("%m%d-%H%M%S") + "-" + rnd


def _append_jsonl(path: Path, obj: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(obj, separators=(",", ":")) + "\n")


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists() or path.stat().st_size == 0:
        return []
    out = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError:
                # Best-effort: skip garbage lines. The journal is append-only
                # so a partial write at the tail is the only realistic cause.
                continue
    return out


_STATE_FILES = {
    "proof_journal.jsonl",
    "proof_open_questions.jsonl",
    "proof_critic_log.jsonl",
    ".proof_session_active",
}


def _git_status_dirty(excluding_state_files: bool = False) -> bool:
    """True iff the worktree has uncommitted edits.

    With ``excluding_state_files=True`` the loop's append-only state files
    (proof_journal.jsonl, proof_open_questions.jsonl, proof_critic_log.jsonl,
    .proof_session_active) are ignored. Those files MUST NOT be stashed;
    they carry forward by design and stashing them would hide orphan-session
    evidence from the cold-start path.
    """
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "status", "--porcelain"],
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return False
    text = out.decode()
    if not text.strip():
        return False
    if not excluding_state_files:
        return True
    for line in text.splitlines():
        # Porcelain format: 'XY <path>' (or 'XY <orig> -> <new>' for renames).
        if len(line) < 4:
            continue
        path = line[3:].strip()
        # Strip rename arrows.
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        # Quoted paths come wrapped in double quotes.
        path = path.strip('"')
        if path in _STATE_FILES:
            continue
        return True
    return False


def _git_short_sha() -> str:
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "rev-parse", "--short=7", "HEAD"],
            stderr=subprocess.DEVNULL,
        )
        return out.decode().strip()
    except subprocess.CalledProcessError:
        return "unknown"


def _stash_dirty(label: str) -> str | None:
    """Stash uncommitted work under a labelled ref. Returns the stash ref
    on success, None if nothing was stashed (clean tree)."""
    try:
        subprocess.check_call(
            ["git", "-C", str(REPO_ROOT), "stash", "push", "--include-untracked",
             "--message", label],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return None
    # Find the stash we just made by listing.
    try:
        out = subprocess.check_output(
            ["git", "-C", str(REPO_ROOT), "stash", "list"],
            stderr=subprocess.DEVNULL,
        )
        for line in out.decode().splitlines():
            if label in line:
                # Format: "stash@{0}: <message>"
                ref = line.split(":", 1)[0].strip()
                return ref
    except subprocess.CalledProcessError:
        pass
    return None


def _detect_orphan_session(journal: list[dict]) -> str | None:
    """Walk the journal back-to-front. Find the most recent session_open
    that has no later session_close (or session_abandoned) for the same
    session_id. Return that orphan session_id, or None if no orphan."""
    last_close: dict[str, str] = {}  # session_id -> latest close-event ts
    last_open: dict[str, str] = {}
    for evt in journal:
        sid = evt.get("session_id")
        ts = evt.get("ts", "")
        if not sid:
            continue
        ev = evt.get("event")
        if ev == "session_open":
            last_open[sid] = ts
        elif ev in ("session_close", "session_abandoned"):
            last_close[sid] = ts
    # An orphan is a session whose open ts is greater than its close ts (or no close).
    orphans = [sid for sid, ts in last_open.items() if last_close.get(sid, "") < ts]
    if not orphans:
        return None
    # Most recent open wins.
    orphans.sort(key=lambda sid: last_open[sid], reverse=True)
    return orphans[0]


def _release_orphan_claims(orphan_sid: str, current_sid: str) -> list[str]:
    """For each qid most-recently 'claimed' by the orphan session, append
    a 'released' row pointing back. Returns the list of released qids."""
    rows = _read_jsonl(OPEN_QUESTIONS)
    latest: dict[str, dict] = {}
    for r in rows:
        qid = r.get("qid")
        if qid:
            latest[qid] = r
    released: list[str] = []
    for qid, last in latest.items():
        if last.get("status") == "claimed" and last.get("session_id") == orphan_sid:
            _append_jsonl(OPEN_QUESTIONS, {
                "qid": qid,
                "status": "released",
                "parent_qid": last.get("parent_qid"),
                "summary": f"auto-released: prior session {orphan_sid} ended without resolving this qid",
                "ts": _now_iso(),
                "session_id": current_sid,
                "note": f"auto-released by proof_session_start during cold-start of {current_sid}",
            })
            released.append(qid)
    return released


def _live_open_qids(rows: list[dict]) -> list[dict]:
    """For each qid, return its most-recent row; filter to status in
    {open, released}. Returns the row dicts in seed order."""
    latest: dict[str, dict] = {}
    seen_first_at: dict[str, int] = {}
    for i, r in enumerate(rows):
        qid = r.get("qid")
        if not qid:
            continue
        if qid not in seen_first_at:
            seen_first_at[qid] = i
        latest[qid] = r
    available = [
        latest[qid] for qid, _ in sorted(seen_first_at.items(), key=lambda kv: kv[1])
        if latest[qid].get("status") in ("open", "released")
    ]
    return available


def _last_session_close_reason(journal: list[dict]) -> str | None:
    for evt in reversed(journal):
        if evt.get("event") == "session_close":
            return str(evt.get("reason", ""))[:500]
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--top-n", type=int, default=5,
                        help="number of open questions to print (default 5)")
    parser.add_argument("--json", action="store_true",
                        help="emit JSON status to stdout instead of human-readable text")
    args = parser.parse_args()

    new_sid = _new_session_id()
    now = _now_iso()
    short_sha = _git_short_sha()

    # 1. Read journal + open_questions BEFORE stashing. The append-only state
    # files might be dirty (a SIGTERM'd prior session left them uncommitted),
    # and stashing them would hide the orphan-evidence we need.
    journal = _read_jsonl(JOURNAL)
    orphan_sid = _detect_orphan_session(journal)

    # 2. Stash any in-progress edit work (proof_strategy.md, proof_lemmas/,
    # proof_session_handoff.md). Excludes the loop's state files — those
    # carry forward by design and must not be rolled back.
    stashed_ref: str | None = None
    if _git_status_dirty(excluding_state_files=True):
        label = f"proof-wip-{short_sha}-{new_sid}"
        stashed_ref = _stash_dirty(label)
    released_qids: list[str] = []
    if orphan_sid is not None:
        # Append the synthetic abandonment event before re-reading the queue.
        _append_jsonl(JOURNAL, {
            "event": "session_abandoned",
            "session_id": orphan_sid,
            "ts": now,
            "detected_by": new_sid,
            "reason": "no session_close found in journal — assumed crashed/interrupted",
        })
        released_qids = _release_orphan_claims(orphan_sid, new_sid)

    # 3. Append session_open for the new session.
    _append_jsonl(JOURNAL, {
        "event": "session_open",
        "session_id": new_sid,
        "ts": now,
        "commit": short_sha,
        "proof_tag": PROOF_TAG,
        "stashed_ref": stashed_ref,
        "detected_orphan": orphan_sid,
        "released_orphan_qids": released_qids,
    })

    # 4. Write the active marker (gitignored).
    try:
        ACTIVE_MARKER.write_text(f"{new_sid}\t{now}\n", encoding="utf-8")
    except OSError:
        pass

    # 5. Build status payload.
    rows = _read_jsonl(OPEN_QUESTIONS)
    open_items = _live_open_qids(rows)
    last_close = _last_session_close_reason(journal)
    handoff_text = (
        HANDOFF.read_text(encoding="utf-8") if HANDOFF.exists()
        else "(no handoff yet — this is a cold first start)\n"
    )

    if args.json:
        payload = {
            "session_id": new_sid,
            "commit": short_sha,
            "proof_tag": PROOF_TAG,
            "ts": now,
            "stashed_ref": stashed_ref,
            "detected_orphan": orphan_sid,
            "released_orphan_qids": released_qids,
            "last_session_close_reason": last_close,
            "handoff": handoff_text,
            "open_questions": open_items[: args.top_n],
            "live_open_count": len(open_items),
        }
        print(json.dumps(payload, indent=2))
        return 0

    # Human-readable output. The agent reads this whole thing.
    print(f"=== proof_session_start: {new_sid} ===")
    print(f"commit:       {short_sha}")
    print(f"proof_tag:    {PROOF_TAG}")
    print(f"ts:           {now}")
    if stashed_ref:
        print(f"WARNING: dirty tree on cold start — stashed under {stashed_ref}")
        print("         (review with `git stash show -p {stashed_ref}` and decide whether to apply)")
    if orphan_sid:
        print(f"WARNING: previous session {orphan_sid} ended without session_close")
        print(f"         auto-released {len(released_qids)} orphan-claimed qids: {released_qids}")
    print()
    print("=== proof_session_handoff.md ===")
    print(handoff_text)
    if last_close:
        print(f"--- last session_close reason: {last_close}")
    print()
    print(f"=== proof_open_questions (top {args.top_n} of {len(open_items)} live open) ===")
    for q in open_items[: args.top_n]:
        print(f"- {q.get('qid')} [{q.get('status')}]: {q.get('summary')}")
    if len(open_items) > args.top_n:
        print(f"... and {len(open_items) - args.top_n} more open. See proof_open_questions.jsonl.")
    print()
    print("=== next steps ===")
    print("1. Pick a qid above (lowest qid first unless the handoff suggests otherwise).")
    print("2. Append a 'claimed' row to proof_open_questions.jsonl for that qid with this session_id.")
    print("3. Edit proof_strategy.md and/or proof_lemmas/lemma_*.md.")
    print("4. git commit per round. Run proof_prepare.py at logical milestones.")
    print("5. When token budget is low or a logical chunk is done:")
    print("   uv run proof_session_end.py 'reason: <one-line summary>'")
    return 0


if __name__ == "__main__":
    sys.exit(main())
