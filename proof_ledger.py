"""proof_ledger.py — machine-readable lemma status ledger (Track 2).

The ledger is the cross-branch source of truth for lemma statuses:
an append-only JSONL file at ``proof_lemmas/ledger.jsonl``, union-merged
by git (see ``.gitattributes``), so parallel session branches can all
append without conflicts. The most recent entry per ``lemma_id`` wins.

Why it exists: lemma statuses used to live only in per-branch markdown
frontmatter and in prose notes — which is how one session spent five
rounds re-verifying a statement (pairwise chain-locality) that two prior
sessions had already disproved with machine-verified counterexamples.
The ledger closes that hole with an enforced check in
``proof_log_result.py``: a round whose lemma files re-open a lemma id the
ledger marks ``disproved`` is rejected (exit 8) unless the file itself
carries ``status: disproved``.

Contract:
- Lemma ids are a GLOBAL namespace across problems (``proof_lemmas/`` is
  one shared directory); the ``problem`` field is metadata, not a scope.
- A REVISED claim takes a NEW id (e.g. ``chain_locality`` →
  ``chain_locality_r3``). Never resurrect a disproved id.
- Escape hatch: ``AUTOERDOS_LEDGER_ENFORCE=0`` disables the reject
  (debug only — document why in the journal if you use it).

CLI:

    uv run proof_ledger.py            # latest status per lemma id
    uv run proof_ledger.py --check    # exit 8 if a file re-opens a disproved id
    uv run proof_ledger.py --sync     # append entries for changed frontmatter
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
LEMMAS_DIR = REPO_ROOT / "proof_lemmas"
LEDGER = LEMMAS_DIR / "ledger.jsonl"

# Statuses that block re-opening. `abandoned` is advisory only (a track
# concluded for external reasons, not a refutation).
BLOCKING_STATUSES = {"disproved"}

_FRONTMATTER_RE = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
_ID_RE = re.compile(r"^id:\s*(\S+)\s*$", re.MULTILINE)
_STATUS_RE = re.compile(r"^status:\s*(\S+)\s*$", re.MULTILINE)


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def _content_sha(text: str) -> str:
    norm = re.sub(r"\s+", " ", text).strip().lower()
    return hashlib.sha256(norm.encode("utf-8")).hexdigest()[:16]


def parse_lemma_file(path: Path) -> dict | None:
    """Extract ``{lemma_id, status, file, content_sha}`` from a lemma file's
    YAML-ish frontmatter. Returns None when there is no parseable id."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    m = _FRONTMATTER_RE.match(text)
    if not m:
        return None
    fm = m.group(1)
    id_m = _ID_RE.search(fm)
    status_m = _STATUS_RE.search(fm)
    if not id_m:
        return None
    return {
        "lemma_id": id_m.group(1).strip(),
        "status": (status_m.group(1).strip().lower() if status_m else "unknown"),
        "file": path.relative_to(REPO_ROOT).as_posix(),
        "content_sha": _content_sha(text),
    }


def scan_lemma_files() -> list[dict]:
    if not LEMMAS_DIR.is_dir():
        return []
    out = []
    for p in sorted(LEMMAS_DIR.glob("lemma_*.md")):
        info = parse_lemma_file(p)
        if info:
            out.append(info)
    return out


def read_ledger() -> list[dict]:
    if not LEDGER.exists() or LEDGER.stat().st_size == 0:
        return []
    rows = []
    with open(LEDGER, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                rows.append(json.loads(line))
            except json.JSONDecodeError:
                # Append-only file: a torn tail line is the only realistic
                # corruption; skip it.
                continue
    return rows


def latest_by_id(rows: list[dict] | None = None) -> dict[str, dict]:
    """Most recent ledger row per lemma_id (file order == append order;
    after a union merge, ts decides)."""
    if rows is None:
        rows = read_ledger()
    latest: dict[str, dict] = {}
    for r in rows:
        lid = r.get("lemma_id")
        if not lid:
            continue
        prev = latest.get(lid)
        if prev is None or str(r.get("ts", "")) >= str(prev.get("ts", "")):
            latest[lid] = r
    return latest


def append_entries(entries: list[dict]) -> None:
    if not entries:
        return
    LEMMAS_DIR.mkdir(parents=True, exist_ok=True)
    with open(LEDGER, "a", encoding="utf-8") as f:
        for e in entries:
            f.write(json.dumps(e, separators=(",", ":"), sort_keys=True) + "\n")


def find_reopened_disproved() -> list[dict]:
    """Lemma files whose frontmatter re-opens an id the ledger has in a
    blocking status. Returns one dict per violation."""
    ledger = latest_by_id()
    violations = []
    for info in scan_lemma_files():
        led = ledger.get(info["lemma_id"])
        if not led:
            continue
        if led.get("status") in BLOCKING_STATUSES and info["status"] not in BLOCKING_STATUSES:
            violations.append({
                **info,
                "file_status": info["status"],
                "ledger_status": led.get("status"),
                "ledger_ts": led.get("ts"),
                "ledger_session": led.get("session_id"),
                "ledger_evidence": led.get("evidence", ""),
            })
    return violations


def sync_ledger(*, session_id: str = "", problem: str = "", evidence: str = "") -> list[dict]:
    """Append a ledger entry for every lemma file whose (id, status) is new
    or changed vs the ledger. Never rewrites history. Returns what was
    appended."""
    ledger = latest_by_id()
    now = _now_iso()
    new_entries = []
    for info in scan_lemma_files():
        led = ledger.get(info["lemma_id"])
        if led and led.get("status") == info["status"]:
            continue
        new_entries.append({
            "lemma_id": info["lemma_id"],
            "status": info["status"],
            "file": info["file"],
            "content_sha": info["content_sha"],
            "problem": problem or os.environ.get("PROOF_TAG", ""),
            "session_id": session_id,
            "evidence": evidence,
            "ts": now,
        })
    append_entries(new_entries)
    return new_entries


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true",
                        help="exit 8 if any lemma file re-opens a disproved id")
    parser.add_argument("--sync", action="store_true",
                        help="append ledger entries for new/changed lemma frontmatter")
    parser.add_argument("--session-id", default="",
                        help="session id to stamp on --sync entries")
    parser.add_argument("--evidence", default="",
                        help="one-line evidence/context to stamp on --sync entries")
    args = parser.parse_args()

    if args.sync:
        appended = sync_ledger(session_id=args.session_id, evidence=args.evidence)
        for e in appended:
            print(f"ledger: {e['lemma_id']} -> {e['status']} ({e['file']})")
        print(f"ledger: {len(appended)} entr{'y' if len(appended) == 1 else 'ies'} appended")
        return 0

    if args.check:
        violations = find_reopened_disproved()
        for v in violations:
            print(
                f"VIOLATION: {v['file']} declares id '{v['lemma_id']}' with status "
                f"'{v['file_status']}' but the ledger has it {v['ledger_status'].upper()} "
                f"(session {v.get('ledger_session') or '?'}, {v.get('ledger_ts') or '?'}"
                f"{'; ' + v['ledger_evidence'] if v.get('ledger_evidence') else ''}). "
                f"A revised claim must take a NEW lemma id.",
                file=sys.stderr,
            )
        if violations:
            return 8
        print("ledger: no violations")
        return 0

    # Default: print latest status per id.
    latest = latest_by_id()
    if not latest:
        print("(ledger empty — run `uv run proof_ledger.py --sync` to seed from frontmatter)")
        return 0
    width = max(len(lid) for lid in latest)
    for lid in sorted(latest):
        r = latest[lid]
        print(f"{lid.ljust(width)}  {r.get('status', '?').ljust(10)}  {r.get('file', '')}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
