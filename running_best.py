"""
running_best.py — read-only state probe for the agent.

Mirrors the parent quant repo's CLI shape:

    uv run running_best.py              # the bar a keep must clear (global ratchet)
    uv run running_best.py --baseline   # the problem's literature baseline
    uv run running_best.py --trials     # rows logged on this branch (cap awareness)
    uv run running_best.py --headroom   # baseline / current best / upper bound / status

The default probe matches the grader's keep bar: max of the literature
baseline, this branch's kept scores, and the cross-branch global best from
the public hypothesis log (same rule log_result.py applies).
"""
from __future__ import annotations

import argparse
import math
import sys

import pandas as pd

from prepare import load_spec
from log_result import (
    RESULTS_TSV,
    TRIAL_CAP,
    _global_best_valid,
    _read_results_tsv,
    _running_best,
    _short_commit,
)


def main() -> int:
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group()
    g.add_argument("--baseline", action="store_true", help="print the problem's literature baseline")
    g.add_argument("--trials", action="store_true", help="print rows-on-branch / trial-cap")
    g.add_argument("--headroom", action="store_true",
                   help="print baseline, current best, upper bound, status — where the real gap is")
    args = parser.parse_args()

    spec = load_spec()
    baseline = float(spec.get("baseline", 0))

    if args.baseline:
        print(f"{baseline:.6f}")
        return 0

    results = _read_results_tsv()
    if args.trials:
        n = len(results)
        print(f"{n}/{TRIAL_CAP}")
        return 0

    try:
        commit = _short_commit()
    except Exception:  # noqa: BLE001 — detached/absent git must not break a read probe
        commit = "unknown"
    rb = _global_best_valid(commit, _running_best(results, baseline))

    if args.headroom:
        ub = spec.get("upper_bound")
        status = str(spec.get("status", "open"))
        print(f"problem:      {spec.get('name', '?')}")
        print(f"status:       {status}")
        print(f"baseline_lb:  {baseline:.0f}")
        print(f"current_best: {rb:.0f}" if math.isfinite(rb) else "current_best: nan")
        if ub is not None:
            gap = float(ub) - rb if math.isfinite(rb) else float("nan")
            print(f"upper_bound:  {float(ub):.0f}")
            print(f"headroom:     {gap:.0f}" if math.isfinite(gap) else "headroom:     nan")
        else:
            print("upper_bound:  unknown")
            print("headroom:     unknown")
        return 0

    if not math.isfinite(rb):
        print("nan")
    else:
        print(f"{rb:.6f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
