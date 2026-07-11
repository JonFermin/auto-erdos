"""
problem_brief.py — session-start "state of the problem" digest.

Turns the scattered cross-branch memory (problem spec, best_so_far, elite
archive, hypothesis log, notes channel, committed summaries) into one
compact brief so a fresh session behaves like a CONTINUATION of a research
program instead of an independent restart. Run it BEFORE forming your
first hypothesis:

    PROBLEM_TAG=capset_n8 uv run problem_brief.py

Free to run: read-only, no trial cost, no cache writes.

Sections:
  headroom    — baseline LB, current global best, upper bound, status
  axes        — per-axis trial counts (keep/discard/crash) + best score,
                so exhausted families are visible at a glance (the grader
                hard-rejects an axis after AUTOERDOS_FAMILY_CAP failures
                with zero keeps — exit 6)
  keeps       — every kept thesis so far (what actually worked)
  recent      — the last few trials (what the previous session was doing)
  notes       — the agent-written knowledge channel (literature findings,
                structural analyses left by prior sessions)
"""
from __future__ import annotations

import math
import re
import sys
from collections import defaultdict

from prepare import (
    PROBLEM_TAG,
    REPO_ROOT,
    load_best_so_far,
    load_hypothesis_log,
    load_problem_notes,
    load_spec,
)

_AXIS_RE = re.compile(r"^thesis:\s*\[([A-Za-z0-9_\-]+)\]", re.IGNORECASE)


def _axis(thesis: str) -> str:
    m = _AXIS_RE.match(thesis.strip())
    return m.group(1).lower() if m else "(untagged)"


def main() -> int:
    spec = load_spec()
    rows = load_hypothesis_log()
    best = load_best_so_far()

    print(f"=== problem brief: {spec['name']} ===")
    print()

    # --- headroom ---
    baseline = float(spec.get("baseline", 0))
    ub = spec.get("upper_bound")
    status = str(spec.get("status", "open"))
    best_score = float(best["score"]) if best else float("nan")
    global_best = max(baseline, best_score) if math.isfinite(best_score) else baseline
    print("[headroom]")
    print(f"  status:        {status}")
    print(f"  baseline LB:   {baseline:.0f}")
    print(f"  global best:   {global_best:.0f}"
          + (f"  (branch {best.get('branch_tag', '?')}, commit {best.get('commit', '?')})" if best else "  (no valid candidate yet)"))
    if ub is not None:
        print(f"  upper bound:   {float(ub):.0f}   -> headroom {float(ub) - global_best:.0f}")
    else:
        print("  upper bound:   unknown")
    if status == "closed":
        print("  !! CLOSED — the optimum is known and reached; log_result will refuse runs (exit 7).")
    print()

    # --- axes ---
    per_axis: dict[str, dict] = defaultdict(lambda: {"keep": 0, "discard": 0, "crash": 0, "best": float("nan")})
    for r in rows:
        a = _axis(str(r.get("thesis", "")))
        st = str(r.get("status", "")).strip().lower()
        if st in ("keep", "discard", "crash"):
            per_axis[a][st] += 1
        try:
            sc = float(r.get("score", "nan"))
            iv = float(r.get("is_valid", "nan"))
        except (TypeError, ValueError):
            continue
        if iv == 1 and math.isfinite(sc):
            cur = per_axis[a]["best"]
            per_axis[a]["best"] = sc if not math.isfinite(cur) else max(cur, sc)

    print(f"[axes] {len(rows)} prior trial(s) across all branches")
    if per_axis:
        for a, st in sorted(per_axis.items(), key=lambda kv: -(kv[1]["keep"] * 1000 + kv[1]["discard"])):
            bs = st["best"]
            bs_str = f"{bs:.0f}" if math.isfinite(bs) else "-"
            exhausted = " <- exhausted (gated)" if st["keep"] == 0 and st["discard"] + st["crash"] >= 5 else ""
            print(f"  [{a}]: keep={st['keep']} discard={st['discard']} crash={st['crash']} best={bs_str}{exhausted}")
    else:
        print("  (none — fresh problem)")
    print()

    # --- keeps ---
    keeps = [r for r in rows if str(r.get("status", "")).strip().lower() == "keep"]
    print(f"[keeps] {len(keeps)} kept trial(s)")
    for r in keeps:
        print(f"  score {r.get('score', '?')}  {r.get('thesis', '')[:140]}")
    print()

    # --- recent ---
    print("[recent] last 5 trials")
    for r in rows[-5:]:
        print(f"  {r.get('written_at', '?')}  {r.get('status', '?'):<8} score {r.get('score', '?'):<12} {r.get('thesis', '')[:110]}")
    if not rows:
        print("  (none)")
    print()

    # --- notes ---
    notes = load_problem_notes()
    print("[notes] agent knowledge channel (~/.cache/auto-erdos/notes_<TAG>.md)")
    if notes.strip():
        print(notes.rstrip())
    else:
        print("  (empty — after your literature pass, write findings via prepare.append_problem_notes)")
    print()

    # --- committed summaries mentioning this problem ---
    summaries_dir = REPO_ROOT / "summaries"
    hits = []
    if summaries_dir.is_dir():
        for p in sorted(summaries_dir.glob("*.md")):
            try:
                text = p.read_text(encoding="utf-8")
            except OSError:
                continue
            if PROBLEM_TAG in text:
                stop = ""
                for line in text.splitlines():
                    if "Stop reason" in line:
                        stop = line.split(":", 1)[-1].strip(" *")
                        break
                hits.append((p.name, stop))
    print(f"[summaries] {len(hits)} committed run summary(ies) for this problem")
    for name, stop in hits[-8:]:
        print(f"  summaries/{name}  stop: {stop or '?'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
