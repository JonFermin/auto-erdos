"""Literature-record caps in AG(n,3), loaded from committed data files.

Public:
  record_cap(n)      — the largest shipped literature-record cap in F_3^n
                       (None if no record file exists for that n).
  record_sizes()     — {n: size} of every shipped record.

These are the constructions that make capset problems *winnable*: the keep
rule is `score > baseline`, so a seed that starts below the literature LB
spends its whole trial budget re-deriving known results. With these files
the seed starts AT the LB and every +1 idea is an attempt at a new record.

Shipped records (see library/data/records/SOURCES.md for full provenance,
verification protocol, and the conversion applied to each source):

  n=7:  236   affine part of Edel's (248,7,3) projective cap
  n=8:  512   FunSearch explicit construction (Romera-Paredes et al.,
              Nature 625, 2024) — supersedes the older 496 doubling,
              which also ships as cap_ag8_3_496.txt
  n=9:  1082  doubling of Edel's (541,8,3) projective cap
  n=10: 2432  doubling of Edel's (1216,9,3) projective cap. NOTE: this cap
              is COMPLETE (no single-point extension exists) — beating it
              requires a genuinely different construction, not +1 greed.

File format: one point per line, n digits from {0,1,2}.

Loading does structural validation only (digit alphabet, dimension,
distinctness, expected count) — full O(k²) cap-freeness was verified when
the files were committed (and is re-checked by tests/test_capset_records.py
and by the real verifier on any candidate built from these). Skipping the
pairwise check keeps load ~instant even at n=10.
"""
from __future__ import annotations

import re
from functools import lru_cache
from pathlib import Path

_DATA_DIR = Path(__file__).resolve().parent / "data" / "records"

_FILE_RE = re.compile(r"^cap_ag(\d+)_3_(\d+)(?:_[a-z0-9]+)?\.txt$")


@lru_cache(maxsize=1)
def _record_files() -> dict[int, tuple[int, Path]]:
    """{n: (size, path)} of the largest record file per dimension."""
    out: dict[int, tuple[int, Path]] = {}
    if not _DATA_DIR.is_dir():
        return out
    for p in _DATA_DIR.glob("cap_ag*.txt"):
        m = _FILE_RE.match(p.name)
        if not m:
            continue
        n, size = int(m.group(1)), int(m.group(2))
        if n not in out or size > out[n][0]:
            out[n] = (size, p)
    return out


def record_sizes() -> dict[int, int]:
    """{n: size} of every shipped literature-record cap."""
    return {n: size for n, (size, _) in _record_files().items()}


@lru_cache(maxsize=8)
def record_cap(n: int) -> list[tuple[int, ...]] | None:
    """Load the largest shipped record cap in F_3^n, or None.

    Returns a list of length-n tuples with coords in {0,1,2}. Structural
    validation only (see module docstring); a malformed file returns None
    rather than raising, so callers can fall through to product-lifts.
    """
    entry = _record_files().get(n)
    if entry is None:
        return None
    size, path = entry
    try:
        lines = [ln.strip() for ln in path.read_text(encoding="utf-8").splitlines()]
    except OSError:
        return None
    cap: list[tuple[int, ...]] = []
    for ln in lines:
        if not ln:
            continue
        if len(ln) != n or any(ch not in "012" for ch in ln):
            return None
        cap.append(tuple(int(ch) for ch in ln))
    if len(cap) != size or len(set(cap)) != size:
        return None
    return cap
