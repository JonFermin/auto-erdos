"""library/_critic_subprocess — shell out to `claude -p` with response caching.

Used by ``proof_prepare.py`` to run the five Track 2 critics. Each critic is
a fresh Claude invocation with the rendered prompt on stdin; the response is
parsed by the caller as a JSON array.

Determinism strategy: every (prompt sha256) → (response sha256, response)
pair is appended to ``~/.cache/auto-erdos/critic_cache.tsv``. On a re-run
with an identical prompt (i.e. the proof under review is unchanged), the
cached response is replayed without firing the LLM. This is the main lever
for cross-session resumability — a fresh agent that re-runs proof_prepare
on an unchanged proof gets the prior critic outputs in milliseconds.

Track 1 (``write_paper.py``) is intentionally NOT migrated to use this
helper. Track 1 has been working for months; the user told us not to touch
it. This module is additive.
"""
from __future__ import annotations

import hashlib
import os
import platform
import shutil
import subprocess
import sys
import time
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

if platform.system() == "Windows":
    import msvcrt
else:
    import fcntl  # type: ignore[unused-ignore]

# Default backend
DEFAULT_OPUS_MODEL = "claude-opus-4-7"
DEFAULT_TIMEOUT_S = 180

# Tools we prevent the model from invoking. Mirrors write_paper.call_opus —
# the prompt is supposed to be self-contained text-in-text-out, no fs/web.
DISALLOWED_TOOLS = (
    "Bash Edit Write Glob Grep Read WebFetch WebSearch Skill Agent "
    "NotebookEdit TaskCreate"
)

CACHE_DIR = Path.home() / ".cache" / "auto-erdos"
CACHE_TSV = CACHE_DIR / "critic_cache.tsv"
CACHE_HEADER = ["prompt_sha256", "critic_name", "response_sha256", "response_b64", "written_at"]


# --------------------------------------------------------------------------- #
# Cache — newline-safe TSV via base64 of the response.
# --------------------------------------------------------------------------- #

def _b64_encode(s: str) -> str:
    """Base64-encode s for TSV-safe single-line storage. The cache is
    line-oriented, so any newline / tab inside a critic response would
    corrupt the file format."""
    import base64
    return base64.b64encode(s.encode("utf-8")).decode("ascii")


def _b64_decode(b: str) -> str:
    import base64
    return base64.b64decode(b.encode("ascii")).decode("utf-8")


@contextmanager
def _cache_lock(path: Path, *, exclusive: bool):
    """Cross-process lock on a sidecar .lock file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    lock_path = path.with_suffix(".tsv.lock")
    f = open(lock_path, "a+", encoding="utf-8")
    try:
        if platform.system() == "Windows":
            f.seek(0)
            msvcrt.locking(f.fileno(), msvcrt.LK_LOCK, 1)
        else:
            fcntl.flock(f.fileno(), fcntl.LOCK_EX if exclusive else fcntl.LOCK_SH)
        yield
    finally:
        try:
            if platform.system() == "Windows":
                try:
                    f.seek(0)
                    msvcrt.locking(f.fileno(), msvcrt.LK_UNLCK, 1)
                except OSError:
                    pass
            else:
                fcntl.flock(f.fileno(), fcntl.LOCK_UN)
        finally:
            f.close()


def _cache_lookup(prompt_sha: str, critic_name: str) -> str | None:
    if not CACHE_TSV.exists() or CACHE_TSV.stat().st_size == 0:
        return None
    try:
        with _cache_lock(CACHE_TSV, exclusive=False):
            with open(CACHE_TSV, encoding="utf-8") as f:
                lines = f.readlines()
    except OSError:
        return None
    if not lines:
        return None
    header = lines[0].rstrip("\n").split("\t")
    try:
        i_prompt = header.index("prompt_sha256")
        i_critic = header.index("critic_name")
        i_resp = header.index("response_b64")
    except ValueError:
        return None
    # Iterate newest-first so a later entry shadows an earlier one for the
    # same key (defensive — the writer is append-only and shouldn't dup,
    # but if it ever does the most recent wins).
    for line in reversed(lines[1:]):
        parts = line.rstrip("\n").split("\t")
        if len(parts) != len(header):
            continue
        if parts[i_prompt] == prompt_sha and parts[i_critic] == critic_name:
            try:
                return _b64_decode(parts[i_resp])
            except (ValueError, UnicodeDecodeError):
                return None
    return None


def _cache_store(prompt_sha: str, critic_name: str, response: str) -> None:
    response_sha = hashlib.sha256(response.encode("utf-8")).hexdigest()
    written_at = datetime.now(timezone.utc).isoformat(timespec="seconds")
    encoded = _b64_encode(response)
    row = [prompt_sha, critic_name, response_sha, encoded, written_at]
    try:
        with _cache_lock(CACHE_TSV, exclusive=True):
            needs_header = (not CACHE_TSV.exists()) or CACHE_TSV.stat().st_size == 0
            with open(CACHE_TSV, "a", encoding="utf-8", newline="") as f:
                if needs_header:
                    f.write("\t".join(CACHE_HEADER) + "\n")
                f.write("\t".join(row) + "\n")
                f.flush()
                try:
                    os.fsync(f.fileno())
                except OSError:
                    pass
    except OSError as e:
        print(
            f"WARNING: critic cache write failed at {CACHE_TSV}: {e}",
            file=sys.stderr,
        )


# --------------------------------------------------------------------------- #
# Subprocess invocation
# --------------------------------------------------------------------------- #

class CriticUnavailable(RuntimeError):
    """Raised when the critic CLI cannot be invoked. The caller should
    treat this as a synthetic BLOCKING finding — silent timeouts must
    NEVER let an open-claim disproof slip through."""


def _check_cli(name: str) -> str:
    path = shutil.which(name)
    if not path:
        raise CriticUnavailable(
            f"`{name}` is not on PATH. Install via "
            f"`@anthropic-ai/claude-code` (npm) and ensure it's runnable."
        )
    return path


def call_critic(
    prompt: str,
    *,
    critic_name: str,
    model: str = DEFAULT_OPUS_MODEL,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    use_cache: bool = True,
) -> tuple[str, dict]:
    """Run a critic prompt through `claude -p` and return (response, meta).

    On cache hit: returns the cached response with meta.from_cache=True.
    On cache miss: shells out, stores the response, returns it.

    Raises ``CriticUnavailable`` on CLI-missing, timeout, or non-zero exit.
    The caller is responsible for converting that into a synthetic BLOCKING
    finding.
    """
    prompt_sha = hashlib.sha256(prompt.encode("utf-8")).hexdigest()

    if use_cache:
        cached = _cache_lookup(prompt_sha, critic_name)
        if cached is not None:
            return cached, {
                "from_cache": True,
                "prompt_sha256": prompt_sha,
                "response_sha256": hashlib.sha256(cached.encode("utf-8")).hexdigest(),
                "duration_s": 0.0,
                "model": model,
            }

    _check_cli("claude")
    cmd = [
        "claude", "-p",
        "--model", model,
        "--output-format", "text",
        "--disallowedTools", DISALLOWED_TOOLS,
    ]

    started = time.time()
    try:
        proc = subprocess.run(
            cmd,
            input=prompt,
            text=True,
            capture_output=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout_s,
        )
    except subprocess.TimeoutExpired:
        raise CriticUnavailable(
            f"`{critic_name}` exceeded {timeout_s}s timeout (model={model})"
        )
    except OSError as e:
        raise CriticUnavailable(f"`{critic_name}` could not launch claude CLI: {e}")
    duration = time.time() - started

    if proc.returncode != 0:
        # Surface the stderr tail so the caller can pin the failure mode in
        # the synthetic BLOCKING finding's evidence string.
        stderr_tail = (proc.stderr or "")[-300:].replace("\n", " ").replace("\t", " ")
        raise CriticUnavailable(
            f"`{critic_name}` claude -p exited {proc.returncode} after {duration:.1f}s: "
            f"{stderr_tail}"
        )

    response = proc.stdout
    if use_cache:
        _cache_store(prompt_sha, critic_name, response)

    return response, {
        "from_cache": False,
        "prompt_sha256": prompt_sha,
        "response_sha256": hashlib.sha256(response.encode("utf-8")).hexdigest(),
        "duration_s": round(duration, 3),
        "model": model,
    }


def call_critics_parallel(
    items: Iterable[tuple[str, str]],
    *,
    model: str = DEFAULT_OPUS_MODEL,
    timeout_s: int = DEFAULT_TIMEOUT_S,
    use_cache: bool = True,
    max_workers: int = 5,
) -> dict[str, tuple[str | None, dict]]:
    """Run multiple critics concurrently. ``items`` is an iterable of
    ``(critic_name, rendered_prompt)`` pairs. Returns a dict
    ``{critic_name: (response_or_None, meta_or_error)}``.

    On any individual critic failure the entry has ``response=None`` and
    ``meta`` includes ``error: "...the CriticUnavailable message..."``. The
    caller MUST convert that into a synthetic BLOCKING finding so the
    aggregator's verdict reflects a critic miss.
    """
    from concurrent.futures import ThreadPoolExecutor, as_completed

    items_list = list(items)
    out: dict[str, tuple[str | None, dict]] = {}
    if not items_list:
        return out

    # Cache hits resolve synchronously — short-circuit them so we don't pay
    # thread overhead. Misses fan out via threads (claude CLI is I/O-bound).
    misses: list[tuple[str, str]] = []
    for name, prompt in items_list:
        if use_cache:
            prompt_sha = hashlib.sha256(prompt.encode("utf-8")).hexdigest()
            cached = _cache_lookup(prompt_sha, name)
            if cached is not None:
                out[name] = (cached, {
                    "from_cache": True,
                    "prompt_sha256": prompt_sha,
                    "response_sha256": hashlib.sha256(cached.encode("utf-8")).hexdigest(),
                    "duration_s": 0.0,
                    "model": model,
                })
                continue
        misses.append((name, prompt))

    if not misses:
        return out

    with ThreadPoolExecutor(max_workers=min(max_workers, len(misses))) as ex:
        futures = {
            ex.submit(
                call_critic,
                prompt,
                critic_name=name,
                model=model,
                timeout_s=timeout_s,
                use_cache=use_cache,
            ): name
            for name, prompt in misses
        }
        for fut in as_completed(futures):
            name = futures[fut]
            try:
                response, meta = fut.result()
                out[name] = (response, meta)
            except CriticUnavailable as e:
                out[name] = (None, {
                    "from_cache": False,
                    "error": str(e),
                    "duration_s": None,
                    "model": model,
                })
            except Exception as e:  # noqa: BLE001 — defensive; never let a critic crash crash the loop
                out[name] = (None, {
                    "from_cache": False,
                    "error": f"unexpected {type(e).__name__}: {e}",
                    "duration_s": None,
                    "model": model,
                })

    return out
