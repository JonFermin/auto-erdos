"""tests/test_chatgpt_failure_caught.py — acceptance test for the proof loop.

This test exists to guarantee the loop catches the canonical failure mode
that motivated Track 2: a ChatGPT-style proof that "disproves" an open
conjecture by misreading an unsigned big-O bound. The fixture
``tests/fixtures/chatgpt_primitive_set_round0.md`` is the literal output of
that ChatGPT chat.

We monkey-patch ``library._critic_subprocess.call_critics_parallel`` to
return canned responses (committed under
``tests/fixtures/critic_responses/critic_*.json``). This isolates the test
from the live LLM. The canned responses are produced once-by-hand by
running the real critics against the fixture and checked in. A separate
manual test (``pytest -m live_llm``, not run in CI) re-runs the live
critics to confirm the canned stubs still match.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO_ROOT))

import pytest

import proof_prepare
from proof_prepare import (
    CRITIC_NAMES,
    extract_witness_payload,
    verify_proof,
)

FIXTURE_DIR = Path(__file__).parent / "fixtures"
CHATGPT_FIXTURE = FIXTURE_DIR / "chatgpt_primitive_set_round0.md"
CANNED_DIR = FIXTURE_DIR / "critic_responses"


def _load_canned_response(critic_name: str) -> str:
    """Return the canned critic response as a JSON-array string ready to be
    parsed. The fixtures are stored as JSON files for human readability;
    we re-serialize compactly so the parser sees what the real CLI emits."""
    path = CANNED_DIR / f"critic_{critic_name}.json"
    with open(path, encoding="utf-8") as f:
        items = json.load(f)
    return json.dumps(items)


def _stub_call_critics_parallel(items, **_kwargs):
    """Stub that replaces library._critic_subprocess.call_critics_parallel.

    Accepts the same shape (iterable of (name, prompt) pairs) and returns
    a dict ``{name: (canned_response, meta)}`` exactly like the real one
    on cache hit.
    """
    out: dict[str, tuple[str, dict]] = {}
    for name, _prompt in items:
        response = _load_canned_response(name)
        out[name] = (response, {"from_cache": True, "stub": True})
    return out


@pytest.fixture
def proof_md() -> str:
    return CHATGPT_FIXTURE.read_text(encoding="utf-8")


@pytest.fixture
def spec() -> dict:
    spec_path = REPO_ROOT / "proofs" / "primitive_set_erdos.json"
    with open(spec_path, encoding="utf-8") as f:
        return json.load(f)


@pytest.fixture
def patched(monkeypatch):
    """Monkey-patch the critic-subprocess helper to return canned responses."""
    import library._critic_subprocess as critic_mod
    monkeypatch.setattr(critic_mod, "call_critics_parallel", _stub_call_critics_parallel)
    # proof_prepare imports the function inside verify_proof; since import is
    # local-scoped there, we also patch the namespace to be safe.
    yield


# --------------------------------------------------------------------------- #
# Unit-ish tests on proof_prepare's individual pieces
# --------------------------------------------------------------------------- #

def test_chatgpt_writeup_has_no_witness_block(proof_md):
    """The ChatGPT output never produced a finite primitive set — its 'disproof'
    is asymptotic hand-waving. extract_witness_payload must return None."""
    assert extract_witness_payload(proof_md) is None


def test_proof_hash_is_stable(proof_md):
    a = proof_prepare._proof_hash(proof_md)
    b = proof_prepare._proof_hash(proof_md)
    assert a == b
    # And whitespace-only mutation shouldn't change it.
    perturbed = proof_md.replace("\n", "\n   ")
    assert proof_prepare._proof_hash(perturbed) == a


def test_canned_responses_load(spec):
    """Every critic_<name>.json must be a JSON array of dicts with the
    required keys. This pins the fixture format; if a maintainer renames
    a key, this test fails before the runtime parser does."""
    for name in CRITIC_NAMES:
        path = CANNED_DIR / f"critic_{name}.json"
        assert path.exists(), f"missing canned fixture for critic_{name}"
        with open(path, encoding="utf-8") as f:
            items = json.load(f)
        assert isinstance(items, list), f"critic_{name}.json top-level must be array"
        for item in items:
            assert isinstance(item, dict)
            assert "flag" in item
            assert item["flag"] in ("BLOCKING", "WARN", "OK")
            assert "evidence" in item
            assert "suggestion" in item


# --------------------------------------------------------------------------- #
# End-to-end with stubbed critics
# --------------------------------------------------------------------------- #

def test_openness_critic_blocks_unwitnessed_disproof(patched, proof_md, spec):
    result = verify_proof(proof_md, spec)
    blockings = [f for f in result.findings if f.flag == "BLOCKING"]
    openness_blocks = [f for f in blockings if f.critic == "openness"]
    assert openness_blocks, "openness critic must emit at least one BLOCKING finding"
    canonical = [f for f in openness_blocks if f.evidence == "open-claim-asserted-resolved-without-witness"]
    assert canonical, (
        f"expected canonical 'open-claim-asserted-resolved-without-witness' "
        f"BLOCKING; got: {[(f.evidence, f.suggestion) for f in openness_blocks]}"
    )


def test_sign_critic_blocks_unsigned_O_misread(patched, proof_md, spec):
    result = verify_proof(proof_md, spec)
    sign_blocks = [
        f for f in result.findings
        if f.critic == "sign" and f.flag == "BLOCKING"
    ]
    assert sign_blocks, "sign critic must emit at least one BLOCKING finding"
    canonical = [f for f in sign_blocks if f.evidence == "unsigned-O-sign-confusion"]
    assert canonical, (
        f"expected canonical 'unsigned-O-sign-confusion' BLOCKING; got: "
        f"{[(f.evidence, f.suggestion) for f in sign_blocks]}"
    )


def test_numerical_critic_warns_on_sufficiently_large_k(patched, proof_md, spec):
    result = verify_proof(proof_md, spec)
    num_warns = [
        f for f in result.findings
        if f.critic == "numerical" and "sufficiently large" in f.evidence.lower()
    ]
    assert num_warns, "numerical critic must flag 'for sufficiently large k' phrasing"


def test_internal_critic_flags_contradiction(patched, proof_md, spec):
    result = verify_proof(proof_md, spec)
    internal_blocks = [
        f for f in result.findings
        if f.critic == "internal" and f.flag == "BLOCKING"
    ]
    assert internal_blocks, "internal critic must flag the F3 contradiction"


def test_aggregate_verdict_is_blocked(patched, proof_md, spec):
    result = verify_proof(proof_md, spec)
    assert result.verdict_hint == "blocked", (
        f"verdict must be 'blocked' for the ChatGPT writeup; got {result.verdict_hint!r}. "
        f"blocking={result.critic_blocking_count} warn={result.critic_warn_count}"
    )
    assert result.witness_valid == 0
    assert result.critic_blocking_count > 0


def test_no_resolution_phrasing_passes_silently(patched, proof_md, spec):
    """Even if every critic returned [], the defense-in-depth check in
    _compute_verdict_hint MUST flag 'the assertion is false' phrasing as
    blocked. This guards against canned-fixture rot."""
    # Patch the stub to return empty arrays for all critics.
    import library._critic_subprocess as critic_mod
    critic_mod.call_critics_parallel = lambda items, **_: {
        name: ("[]", {"from_cache": True, "stub": True})
        for name, _ in items
    }
    result = verify_proof(proof_md, spec)
    # All critic-side findings are empty; verdict must STILL be blocked
    # because the proof_md contains "the assertion is false" without a witness.
    assert result.verdict_hint == "blocked", (
        f"defense-in-depth must catch resolution phrasing without witness; got {result.verdict_hint!r}"
    )


# --------------------------------------------------------------------------- #
# Numerical check sandbox
# --------------------------------------------------------------------------- #

def test_sandboxed_eval_blocks_dangerous():
    ok, msg = proof_prepare._sandboxed_eval("__import__('os').system('echo pwn')")
    assert ok is False
    assert "banned" in msg.lower() or "error" in msg.lower()


def test_sandboxed_eval_blocks_long_expr():
    ok, msg = proof_prepare._sandboxed_eval("1 + " + "1 + " * 200 + "1")
    assert ok is False
    assert "too long" in msg.lower()


def test_sandboxed_eval_runs_math():
    ok, msg = proof_prepare._sandboxed_eval("math.log(2) > 0.69")
    assert ok is True


def test_sandboxed_eval_handles_runtime_error():
    ok, msg = proof_prepare._sandboxed_eval("1/0")
    assert ok is False
    assert "ZeroDivisionError" in msg
