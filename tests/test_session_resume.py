"""tests/test_session_resume.py — resumability acceptance test.

Simulates the failure mode that motivated Track 2's session-lifecycle
design: an agent thinks for ~80 minutes, hits the token cap mid-round,
gets killed (SIGTERM), and a fresh agent must pick up where it left off
from disk state alone.

Each test runs in an isolated temp git repo (fixture ``proof_repo``) so
the live working tree is never touched.
"""
from __future__ import annotations

import json
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(cwd: Path, *cmd: str, env: dict | None = None, check: bool = True, input_text: str | None = None) -> subprocess.CompletedProcess:
    full_env = os.environ.copy()
    if env:
        full_env.update(env)
    return subprocess.run(
        cmd,
        cwd=str(cwd),
        env=full_env,
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        check=check,
        input=input_text,
    )


@pytest.fixture
def proof_repo(tmp_path: Path) -> Path:
    """Build a minimal isolated copy of the repo (just the bits the session
    helpers need) inside an initialized git repo."""
    sandbox = tmp_path / "auto-erdos"
    sandbox.mkdir()

    # Copy the load-bearing files.
    for rel in (
        "proof_session_start.py",
        "proof_session_end.py",
    ):
        shutil.copy2(REPO_ROOT / rel, sandbox / rel)

    # Init git so the helpers' git-status / git-stash calls work.
    _run(sandbox, "git", "init", "-q")
    _run(sandbox, "git", "config", "user.email", "test@example.com")
    _run(sandbox, "git", "config", "user.name", "Test User")

    # Seed the queue and journal as empty / minimal.
    (sandbox / "proof_journal.jsonl").write_text("", encoding="utf-8")
    (sandbox / "proof_open_questions.jsonl").write_text(
        '{"qid":"Q1","status":"open","summary":"first task","ts":"2026-04-30T00:00:00+00:00","session_id":"seed"}\n'
        '{"qid":"Q2","status":"open","summary":"second task","ts":"2026-04-30T00:00:00+00:00","session_id":"seed"}\n',
        encoding="utf-8",
    )

    # Initial commit.
    _run(sandbox, "git", "add", "-A")
    _run(sandbox, "git", "commit", "-q", "-m", "seed")

    return sandbox


def _read_journal(repo: Path) -> list[dict]:
    p = repo / "proof_journal.jsonl"
    if not p.exists() or p.stat().st_size == 0:
        return []
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def _read_questions(repo: Path) -> list[dict]:
    p = repo / "proof_open_questions.jsonl"
    if not p.exists() or p.stat().st_size == 0:
        return []
    return [json.loads(line) for line in p.read_text(encoding="utf-8").splitlines() if line.strip()]


def _start_session(repo: Path) -> tuple[str, subprocess.CompletedProcess]:
    """Run proof_session_start.py --json and parse the session_id."""
    res = _run(repo, sys.executable, "proof_session_start.py", "--json")
    payload = json.loads(res.stdout)
    return payload["session_id"], res


def _end_session(repo: Path, reason: str) -> subprocess.CompletedProcess:
    return _run(
        repo,
        sys.executable, "proof_session_end.py",
        reason,
        input_text="",  # use default handoff template
    )


# --------------------------------------------------------------------------- #
# Happy path: session_start → work → session_end → session_start again
# --------------------------------------------------------------------------- #

def test_clean_session_lifecycle(proof_repo: Path):
    sid1, res1 = _start_session(proof_repo)
    assert sid1.startswith("s_"), f"session_id format unexpected: {sid1!r}"
    payload = json.loads(res1.stdout)
    assert payload["detected_orphan"] is None
    assert payload["live_open_count"] == 2

    # Active marker exists.
    assert (proof_repo / ".proof_session_active").exists()

    # Session_open written to journal.
    journal = _read_journal(proof_repo)
    assert len(journal) == 1
    assert journal[0]["event"] == "session_open"
    assert journal[0]["session_id"] == sid1

    # End the session cleanly.
    _end_session(proof_repo, "reason: clean test exit")

    # Active marker removed.
    assert not (proof_repo / ".proof_session_active").exists()

    # Journal has session_open + session_close.
    journal = _read_journal(proof_repo)
    events = [(e["event"], e["session_id"]) for e in journal]
    assert ("session_open", sid1) in events
    assert ("session_close", sid1) in events

    # Handoff was written.
    assert (proof_repo / "proof_session_handoff.md").exists()

    # Second cold start does NOT detect orphan.
    sid2, res2 = _start_session(proof_repo)
    payload2 = json.loads(res2.stdout)
    assert sid2 != sid1
    assert payload2["detected_orphan"] is None


# --------------------------------------------------------------------------- #
# Resumability: session_open without session_close (simulated SIGTERM)
# --------------------------------------------------------------------------- #

def test_orphan_session_detected_and_handled(proof_repo: Path):
    sid1, _ = _start_session(proof_repo)

    # Simulate: agent claims Q1 but never resolves and never calls session_end.
    # We append a 'claimed' row directly, mimicking what the agent's prompt
    # boilerplate would do.
    with open(proof_repo / "proof_open_questions.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "qid": "Q1",
            "status": "claimed",
            "summary": "starting Q1",
            "ts": "2026-04-30T01:00:00+00:00",
            "session_id": sid1,
        }) + "\n")

    # Simulate SIGTERM: just remove the active marker without calling session_end.
    # (Real SIGTERM would leave the marker too; we test BOTH cases — see next test.)
    (proof_repo / ".proof_session_active").unlink()

    # Cold-start session 2.
    sid2, res2 = _start_session(proof_repo)
    payload2 = json.loads(res2.stdout)
    assert sid2 != sid1
    assert payload2["detected_orphan"] == sid1, (
        f"expected session 2 to detect orphan {sid1}; got payload={payload2}"
    )
    assert "Q1" in payload2["released_orphan_qids"]

    # Q1 is back in the live-open list (released → available).
    journal = _read_journal(proof_repo)
    abandon_evts = [e for e in journal if e["event"] == "session_abandoned"]
    assert len(abandon_evts) == 1
    assert abandon_evts[0]["session_id"] == sid1

    questions = _read_questions(proof_repo)
    # Find the most-recent row for Q1.
    q1_rows = [q for q in questions if q.get("qid") == "Q1"]
    assert q1_rows[-1]["status"] == "released"
    assert q1_rows[-1]["session_id"] == sid2  # released by sid2


def test_orphan_with_marker_left_behind(proof_repo: Path):
    """Real SIGTERM may leave .proof_session_active behind. The next
    session_start must still detect the abandoned session via the journal,
    and overwrite the active marker for itself."""
    sid1, _ = _start_session(proof_repo)
    # Don't end. Don't remove the marker. Just start a new session.
    # (proof_session_start.py overwrites the marker.)
    sid2, res2 = _start_session(proof_repo)
    assert sid2 != sid1
    payload2 = json.loads(res2.stdout)
    assert payload2["detected_orphan"] == sid1


def test_dirty_tree_is_stashed_not_discarded(proof_repo: Path):
    """A SIGTERM mid-edit leaves uncommitted changes. session_start MUST
    stash, not discard."""
    sid1, _ = _start_session(proof_repo)
    # Simulate an in-flight edit.
    (proof_repo / "proof_strategy.md").write_text(
        "# Half-written proof\n\nLemma 1: ...\n",
        encoding="utf-8",
    )
    # Don't commit, don't end the session.
    (proof_repo / ".proof_session_active").unlink()

    # Cold-start session 2.
    sid2, res2 = _start_session(proof_repo)
    payload2 = json.loads(res2.stdout)
    stashed_ref = payload2.get("stashed_ref")
    assert stashed_ref is not None, "dirty tree must be stashed, not discarded"
    assert stashed_ref.startswith("stash@"), f"unexpected stash ref: {stashed_ref!r}"

    # The stash list contains a labelled entry for this session.
    stash_list = _run(proof_repo, "git", "stash", "list").stdout
    assert sid2 in stash_list, "stash should be labelled with current session_id"


# --------------------------------------------------------------------------- #
# Cross-session progress invariant
# --------------------------------------------------------------------------- #

def test_progress_strictly_advances_across_sessions(proof_repo: Path):
    """Run session 1 → resolve Q1 → end. Then session 2 → see Q2 only.
    Then session 3 → resolve Q2 → end. Confirm questions log shows the
    expected lifecycle."""
    sid1, _ = _start_session(proof_repo)
    with open(proof_repo / "proof_open_questions.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps({
            "qid": "Q1", "status": "claimed", "session_id": sid1,
            "summary": "starting Q1", "ts": "2026-04-30T01:00:00+00:00",
        }) + "\n")
        f.write(json.dumps({
            "qid": "Q1", "status": "resolved", "session_id": sid1,
            "summary": "Q1 done: bound established", "ts": "2026-04-30T01:30:00+00:00",
        }) + "\n")
    _end_session(proof_repo, "reason: Q1 done")

    sid2, res2 = _start_session(proof_repo)
    payload2 = json.loads(res2.stdout)
    open_qids = [q["qid"] for q in payload2["open_questions"]]
    assert open_qids == ["Q2"], (
        f"after Q1 resolved, only Q2 should be open; got {open_qids}"
    )

    # End session 2 without doing work — that's a valid case (interrupted).
    _end_session(proof_repo, "reason: interrupted")

    sid3, res3 = _start_session(proof_repo)
    payload3 = json.loads(res3.stdout)
    open_qids = [q["qid"] for q in payload3["open_questions"]]
    assert open_qids == ["Q2"]


def test_handoff_propagates_across_sessions(proof_repo: Path):
    """The handoff written by session 1's session_end is the FIRST thing
    session 2 sees on cold-start."""
    sid1, _ = _start_session(proof_repo)
    custom_handoff = (
        "# Custom handoff\n\nWorking on Lemma 2; need Mertens' formula in the bound.\n"
    )
    _run(
        proof_repo,
        sys.executable, "proof_session_end.py",
        "reason: stopping for token budget",
        input_text=custom_handoff,
    )

    sid2, res2 = _start_session(proof_repo)
    # Custom handoff text appears in stdout.
    assert "Working on Lemma 2; need Mertens' formula" in res2.stdout
    # And in the parsed payload (if --json mode).
    payload = json.loads(res2.stdout)
    assert "Working on Lemma 2; need Mertens' formula" in payload["handoff"]


def test_journal_is_append_only(proof_repo: Path):
    """Multiple sessions accumulate journal rows; nothing is rewritten."""
    sid1, _ = _start_session(proof_repo)
    _end_session(proof_repo, "reason: 1")
    sid2, _ = _start_session(proof_repo)
    _end_session(proof_repo, "reason: 2")
    sid3, _ = _start_session(proof_repo)
    _end_session(proof_repo, "reason: 3")

    journal = _read_journal(proof_repo)
    open_evts = [e for e in journal if e["event"] == "session_open"]
    close_evts = [e for e in journal if e["event"] == "session_close"]
    assert len(open_evts) == 3
    assert len(close_evts) == 3
    sids = [e["session_id"] for e in open_evts]
    assert sorted(sids) == sorted([sid1, sid2, sid3])
