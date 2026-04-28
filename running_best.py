"""
running_best.py — read-only state probe for the agent.

Mirrors the parent quant repo's CLI shape:

    uv run running_best.py              # current best kept score
    uv run running_best.py --baseline   # the problem's literature baseline
    uv run running_best.py --trials     # rows logged on this branch (cap awareness)

All numbers come from results.tsv on the current branch and the active
problem's JSON. The shared per-problem trial cache is harness-side and is
NOT read by this tool — agents must not see other branches' scores.
"""
from __future__ import annotations

import argparse
import math
import sys

import pandas as pd

from prepare import load_spec
from log_result import RESULTS_TSV, TRIAL_CAP, _read_results_tsv, _running_best


def main() -> int:
    parser = argparse.ArgumentParser()
    g = parser.add_mutually_exclusive_group()
    g.add_argument("--baseline", action="store_true", help="print the problem's literature baseline")
    g.add_argument("--trials", action="store_true", help="print rows-on-branch / trial-cap")
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

    rb = _running_best(results, baseline)
    if not math.isfinite(rb):
        print("nan")
    else:
        print(f"{rb:.6f}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
