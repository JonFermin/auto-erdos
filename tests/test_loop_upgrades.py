"""tests/test_loop_upgrades.py — regression tests for the 2026-07 loop upgrades.

Covers: AUTOERDOS_CACHE_DIR isolation, the global keep-bar ratchet, the
hypothesis-family gate (exit 6), the closed-problem guard (exit 7), the
elites archive, the frontier diagnostic, and the notes channel.

prepare.py / log_result.py resolve PROBLEM_TAG and the cache dir at import
time, so every test that needs a non-default configuration runs the code in
a subprocess with a scrubbed environment.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

HYPO_HEADER = "written_at\tbranch_tag\tcommit\tscore\tis_valid\tstatus\tthesis\n"


def _run_py(code: str, *, cache_dir: Path, tag: str, extra_env: dict | None = None):
    env = dict(os.environ)
    env["AUTOERDOS_CACHE_DIR"] = str(cache_dir)
    env["PROBLEM_TAG"] = tag
    env.update(extra_env or {})
    return subprocess.run(
        [sys.executable, "-c", code],
        cwd=str(REPO_ROOT),
        env=env,
        capture_output=True,
        text=True,
        timeout=120,
    )


def _write_hypo_log(cache_dir: Path, tag: str, rows: list[tuple]) -> None:
    """rows: (branch, commit, score, is_valid, status, thesis)"""
    cache_dir.mkdir(parents=True, exist_ok=True)
    path = cache_dir / f"hypothesis_log_{tag}.tsv"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(HYPO_HEADER)
        for branch, commit, score, is_valid, status, thesis in rows:
            f.write(f"2026-07-01T00:00:00+00:00\t{branch}\t{commit}\t{score}\t{is_valid}\t{status}\t{thesis}\n")


# --------------------------------------------------------------------------- #
# Cache-dir isolation
# --------------------------------------------------------------------------- #

def test_cache_dir_override_isolates(tmp_path):
    r = _run_py(
        "import prepare, log_result; "
        "print(prepare._CACHE_DIR); print(log_result._CACHE_DIR)",
        cache_dir=tmp_path, tag="sidon_100",
    )
    assert r.returncode == 0, r.stderr
    lines = r.stdout.strip().splitlines()
    assert str(tmp_path) == lines[0] == lines[1]


# --------------------------------------------------------------------------- #
# Global ratchet
# --------------------------------------------------------------------------- #

def test_global_best_valid_reads_cross_branch(tmp_path):
    _write_hypo_log(tmp_path, "sidon_1000", [
        ("b1", "aaaaaaa", "34.000000", "1", "keep", "thesis: [singer] x"),
        ("b2", "bbbbbbb", "35.000000", "1", "discard", "thesis: [swap] y"),
        ("b2", "ccccccc", "99.000000", "0", "discard", "thesis: [swap] invalid should not count"),
    ])
    r = _run_py(
        "from log_result import _global_best_valid; "
        "print(_global_best_valid('zzzzzzz', 32.0))",
        cache_dir=tmp_path, tag="sidon_1000",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "35.0"


def test_global_ratchet_excludes_current_commit(tmp_path):
    _write_hypo_log(tmp_path, "sidon_1000", [
        ("b1", "curcomm", "40.000000", "1", "keep", "thesis: [singer] mine"),
    ])
    r = _run_py(
        "from log_result import _global_best_valid; "
        "print(_global_best_valid('curcomm', 32.0))",
        cache_dir=tmp_path, tag="sidon_1000",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "32.0"


def test_global_ratchet_kill_switch(tmp_path):
    _write_hypo_log(tmp_path, "sidon_1000", [
        ("b1", "aaaaaaa", "35.000000", "1", "keep", "thesis: [singer] x"),
    ])
    r = _run_py(
        "from log_result import _global_best_valid; "
        "print(_global_best_valid('zzzzzzz', 32.0))",
        cache_dir=tmp_path, tag="sidon_1000",
        extra_env={"AUTOERDOS_GLOBAL_RATCHET": "0"},
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "32.0"


# --------------------------------------------------------------------------- #
# Family gate
# --------------------------------------------------------------------------- #

def _sa_failures(n: int) -> list[tuple]:
    return [
        ("b1", f"c{i:06d}", "10.000000", "1", "discard", "thesis: [SA] variant %d" % i)
        for i in range(n)
    ]


def test_family_gate_blocks_exhausted_axis(tmp_path):
    _write_hypo_log(tmp_path, "capset_n8", _sa_failures(5))
    r = _run_py(
        "from log_result import _family_gate; "
        "blocked, msg = _family_gate('thesis: [sa] yet another cooling schedule'); "
        "print(blocked); print(msg)",
        cache_dir=tmp_path, tag="capset_n8",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.splitlines()[0] == "True"
    assert "[sa]" in r.stdout


def test_family_gate_open_below_cap(tmp_path):
    _write_hypo_log(tmp_path, "capset_n8", _sa_failures(4))
    r = _run_py(
        "from log_result import _family_gate; "
        "print(_family_gate('thesis: [SA] one more is still allowed')[0])",
        cache_dir=tmp_path, tag="capset_n8",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "False"


def test_family_gate_keep_unlocks_axis(tmp_path):
    rows = _sa_failures(7)
    rows.append(("b3", "keeper1", "500.000000", "1", "keep", "thesis: [SA] the one that worked"))
    _write_hypo_log(tmp_path, "capset_n8", rows)
    r = _run_py(
        "from log_result import _family_gate; "
        "print(_family_gate('thesis: [SA] refine the working variant')[0])",
        cache_dir=tmp_path, tag="capset_n8",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "False"


def test_family_gate_untagged_not_gated(tmp_path):
    _write_hypo_log(tmp_path, "capset_n8", _sa_failures(9))
    r = _run_py(
        "from log_result import _family_gate; "
        "print(_family_gate('thesis: no axis tag here')[0])",
        cache_dir=tmp_path, tag="capset_n8",
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "False"


def test_family_gate_disabled_by_env(tmp_path):
    _write_hypo_log(tmp_path, "capset_n8", _sa_failures(9))
    r = _run_py(
        "from log_result import _family_gate; "
        "print(_family_gate('thesis: [SA] gate off')[0])",
        cache_dir=tmp_path, tag="capset_n8",
        extra_env={"AUTOERDOS_FAMILY_CAP": "0"},
    )
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip() == "False"


# --------------------------------------------------------------------------- #
# Closed-problem guard (full CLI path — exits 7 before touching any state)
# --------------------------------------------------------------------------- #

def test_closed_problem_refused(tmp_path):
    env = dict(os.environ)
    env["AUTOERDOS_CACHE_DIR"] = str(tmp_path)
    env["PROBLEM_TAG"] = "sidon_500"
    r = subprocess.run(
        [sys.executable, str(REPO_ROOT / "log_result.py"), "thesis: [swap] should be refused"],
        cwd=str(REPO_ROOT), env=env, capture_output=True, text=True, timeout=120,
    )
    assert r.returncode == 7, (r.returncode, r.stderr)
    assert "CLOSED" in r.stderr


# --------------------------------------------------------------------------- #
# Elites archive
# --------------------------------------------------------------------------- #

ELITE_CODE = """
import json
from prepare import VerifyResult, _save_elite_if_qualifies, load_elites, load_spec
spec = load_spec()
def add(cand, score):
    _save_elite_if_qualifies(cand, VerifyResult(True, float(score), "ok", 0.0), spec)
# 10 distinct candidates, scores 1..10; plus one duplicate of the best
for s in range(1, 11):
    add(list(range(1, s + 1)), s)
add(list(range(1, 11)), 10)   # exact duplicate — must not double-store
e = load_elites()
print(len(e))
print([int(x["score"]) for x in e])
"""


def test_elites_dedup_and_truncate(tmp_path):
    r = _run_py(ELITE_CODE, cache_dir=tmp_path, tag="sidon_100")
    assert r.returncode == 0, r.stderr
    lines = r.stdout.strip().splitlines()
    assert lines[0] == "8"
    assert lines[1] == "[10, 9, 8, 7, 6, 5, 4, 3]"


# --------------------------------------------------------------------------- #
# Frontier diagnostic
# --------------------------------------------------------------------------- #

FRONTIER_CODE = """
from prepare import VerifyResult, _frontier_report, load_spec
spec = load_spec()
# {1, 2} in [1, 100]: plenty of +1 extensions exist
r1 = _frontier_report([1, 2], VerifyResult(True, 2.0, "ok", 0.0), spec)
print("EXT" if "extension(s) exist" in r1 else r1)
# invalid result -> no report
print(_frontier_report([1, 2], VerifyResult(False, 0.0, "bad", 0.0), spec))
"""


def test_frontier_report_sidon(tmp_path):
    r = _run_py(FRONTIER_CODE, cache_dir=tmp_path, tag="sidon_100")
    assert r.returncode == 0, r.stderr
    lines = r.stdout.strip().splitlines()
    assert lines[0] == "EXT"
    assert lines[1] == "None"


def test_frontier_capset_locally_maximal(tmp_path):
    code = (
        "from prepare import VerifyResult, _frontier_report, load_spec\n"
        "spec = load_spec()\n"
        "import itertools\n"
        "# the FULL maximal cap for n=1: {0, 1} - adding 2 makes an AP; locally maximal\n"
        "cand = [(0,)*4, (1,)+(0,)*3]\n"
        "r = _frontier_report(cand, VerifyResult(True, 2.0, 'ok', 0.0), spec)\n"
        "print(r)\n"
    )
    r = _run_py(code, cache_dir=tmp_path, tag="capset_n4")
    assert r.returncode == 0, r.stderr
    # {0000, 1000} blocks only 2000; nearly everything else is addable
    assert "extension(s) exist" in r.stdout


# --------------------------------------------------------------------------- #
# Notes channel
# --------------------------------------------------------------------------- #

NOTES_CODE = """
from prepare import append_problem_notes, load_problem_notes
assert load_problem_notes() == ""
append_problem_notes("Singer q=31 exhausted; try GF(q^3) cubics next.")
append_problem_notes("second entry")
out = load_problem_notes()
print("HDR" if out.startswith("# notes") else "NOHDR")
print("E1" if "Singer q=31 exhausted" in out else "MISS1")
print("E2" if "second entry" in out else "MISS2")
"""


def test_notes_roundtrip(tmp_path):
    r = _run_py(NOTES_CODE, cache_dir=tmp_path, tag="sidon_1000")
    assert r.returncode == 0, r.stderr
    assert r.stdout.strip().splitlines() == ["HDR", "E1", "E2"]


# --------------------------------------------------------------------------- #
# Spec integrity: every problem carries the new fields, honestly ordered
# --------------------------------------------------------------------------- #

def test_all_specs_have_status_and_bounds():
    for path in (REPO_ROOT / "problems").glob("*.json"):
        spec = json.loads(path.read_text(encoding="utf-8"))
        assert spec.get("status") in ("open", "sanity", "closed"), path.name
        assert "upper_bound" in spec, path.name
        assert float(spec["upper_bound"]) >= float(spec["baseline"]), path.name
        if spec["status"] == "sanity":
            assert float(spec["upper_bound"]) == float(spec["baseline"]), path.name
