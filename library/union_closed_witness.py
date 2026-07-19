"""union_closed_witness — verifier for Frankl union-closed counterexample witnesses.

Frankl's union-closed sets conjecture (1979): for every finite union-closed
family F of finite sets with F != {∅} (at least one member is nonempty),
some element belongs to at least half of the members of F. A witness here
is a finite union-closed family in which EVERY element of the ground set
appears in strictly fewer than |F|/2 members — a single such family
disproves the conjecture. This module is the only sanctioned path to
``witness_valid = 1`` on the ``frankl_union_closed`` proof spec.

(Not an Erdős problem — Frankl 1979 — but the same witness-decidable shape
as the rest of the Track 2 portfolio: the claim is universal over finite
objects and one verified finite object settles it.)

Witness payload:

    {
      "sets": [[int, ...], ...]     # the family; elements are ints >= 0
    }

Verifier contract — ``verify_witness(payload, spec) -> VerifyResult``:
    - is_valid=True iff
        (a) members are distinct finite sets within size caps;
        (b) at least one member is nonempty;
        (c) the family is union-closed: for every pair S, T in F,
            S ∪ T ∈ F (checked exhaustively, O(|F|^2) bitmask ORs);
        (d) every element x of the ground set satisfies
            2 * |{S in F : x in S}| < |F|  (strict).
    - score = |F| (family size; keep fires on is_valid alone).

Membership convention: |F| counts ALL members including ∅ if present —
the standard formulation. The strictness in (d) matches "at least half"
in the conjecture: a counterexample needs every frequency strictly below
half.

Implementation: sets are packed into Python int bitmasks after remapping
elements to a dense range, so union-closure is |F|^2 bitwise ORs with
O(1) membership via a hash set of masks. Caps keep worst-case runtime in
seconds. Stdlib only. Matches primitive_set_witness.VerifyResult's shape.

Known context (2026): the conjecture is open. Gilmer (2022,
arXiv:2211.09055) proved a 0.01-fraction bound information-theoretically;
Alweiss–Huang–Sellke and others improved it to (3-sqrt(5))/2 ~ 0.381966,
and Chase–Lovett showed 0.382 is optimal for the approximate relaxation —
so any counterexample must have its max frequency in [0.382, 0.5), a
narrow and heavily-constrained window.
"""
from __future__ import annotations

import time
from dataclasses import dataclass

MAX_SETS = 5000
MAX_UNIVERSE = 4096
MAX_TOTAL_ELEMENTS = 500_000


@dataclass
class VerifyResult:
    is_valid: bool
    score: float
    reason: str
    verifier_seconds: float


def verify_witness(payload: dict, spec: dict) -> VerifyResult:
    t0 = time.time()

    if not isinstance(payload, dict):
        return VerifyResult(False, 0.0, f"payload must be dict, got {type(payload).__name__}", time.time() - t0)
    if "sets" not in payload:
        return VerifyResult(False, 0.0, "payload missing 'sets'", time.time() - t0)
    raw = payload["sets"]
    if not isinstance(raw, list):
        return VerifyResult(False, 0.0, f"'sets' must be list, got {type(raw).__name__}", time.time() - t0)
    m = len(raw)
    if m < 1:
        return VerifyResult(False, 0.0, "family is empty", time.time() - t0)
    if m > MAX_SETS:
        return VerifyResult(False, 0.0, f"family size {m} exceeds cap {MAX_SETS}", time.time() - t0)

    # Parse members, remap elements to dense indices for bitmasking.
    elem_index: dict[int, int] = {}
    members: list[frozenset[int]] = []
    total_elements = 0
    for i, s in enumerate(raw):
        if not isinstance(s, list):
            return VerifyResult(False, 0.0, f"member #{i} is not a list", time.time() - t0)
        try:
            fs = frozenset(int(x) for x in s)
        except (TypeError, ValueError):
            return VerifyResult(False, 0.0, f"member #{i} contains a non-integer", time.time() - t0)
        total_elements += len(fs)
        if total_elements > MAX_TOTAL_ELEMENTS:
            return VerifyResult(False, 0.0, f"total element count exceeds cap {MAX_TOTAL_ELEMENTS}", time.time() - t0)
        for x in fs:
            if x not in elem_index:
                if len(elem_index) >= MAX_UNIVERSE:
                    return VerifyResult(False, 0.0, f"ground set exceeds cap {MAX_UNIVERSE}", time.time() - t0)
                elem_index[x] = len(elem_index)
        members.append(fs)

    if all(len(fs) == 0 for fs in members):
        return VerifyResult(False, 0.0, "family has no nonempty member (F = {∅} is excluded by the conjecture)", time.time() - t0)

    # Bitmasks + distinctness.
    masks: list[int] = []
    for i, fs in enumerate(members):
        mask = 0
        for x in fs:
            mask |= 1 << elem_index[x]
        masks.append(mask)
    mask_set = set(masks)
    if len(mask_set) != m:
        return VerifyResult(False, 0.0, "family members are not distinct", time.time() - t0)

    # Union-closure: every pairwise union must be a member.
    for i in range(m):
        mi = masks[i]
        for j in range(i, m):
            u = mi | masks[j]
            if u not in mask_set:
                return VerifyResult(
                    False, 0.0,
                    f"NOT union-closed: union of member #{i} and member #{j} is not in the family",
                    time.time() - t0,
                )

    # Element frequencies — every element strictly below half.
    n_elems = len(elem_index)
    freq = [0] * n_elems
    for mask in masks:
        rest = mask
        while rest:
            low = rest & (-rest)
            freq[low.bit_length() - 1] += 1
            rest ^= low
    rev = {idx: x for x, idx in elem_index.items()}
    worst_idx = max(range(n_elems), key=lambda k: freq[k]) if n_elems else -1
    if n_elems:
        worst_freq = freq[worst_idx]
        if 2 * worst_freq >= m:
            return VerifyResult(
                False, 0.0,
                f"element {rev[worst_idx]} appears in {worst_freq} of {m} members "
                f"(>= half) — conjecture HOLDS on this family, not a counterexample",
                time.time() - t0,
            )
        margin = 0.5 - worst_freq / m
        return VerifyResult(
            True, float(m),
            f"VERIFIED counterexample candidate: union-closed family of {m} distinct sets over "
            f"a {n_elems}-element ground set; max element frequency {worst_freq}/{m} "
            f"(margin below half: {margin:.6f}); this family disproves Frankl's "
            f"union-closed conjecture if independently confirmed",
            time.time() - t0,
        )
    # n_elems == 0 can't happen here (nonempty member exists), but be defensive.
    return VerifyResult(False, 0.0, "empty ground set", time.time() - t0)
