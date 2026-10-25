"""Small HTTP client for the workshop's local Judge0 container."""

from __future__ import annotations

import json
from functools import lru_cache
from urllib.request import Request, urlopen


JUDGE0_URL = "http://127.0.0.1:2358"
LANGUAGE_NAMES = {
    "python": "Python (3.8.1)",
    "cpp14": "C++ (GCC 9.2.0)",
    "java11": "Java (OpenJDK 11)",
}


def _request(path: str, payload: dict | None = None):
    body = None if payload is None else json.dumps(payload).encode()
    request = Request(
        f"{JUDGE0_URL}{path}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="GET" if payload is None else "POST",
    )
    with urlopen(request, timeout=15) as response:
        return json.load(response)


@lru_cache
def _language_ids() -> dict[str, int]:
    available = {language["name"]: language["id"] for language in _request("/languages")}
    missing = [name for name in LANGUAGE_NAMES.values() if name not in available]
    if missing:
        raise RuntimeError(f"Local Judge0 is missing: {', '.join(missing)}")
    return {alias: available[name] for alias, name in LANGUAGE_NAMES.items()}


def execute_code(
    language: str,
    code: str,
    stdin: str,
    expected_output: str | None = None,
) -> dict:
    """Execute one bounded testcase through local Judge0."""
    if language not in LANGUAGE_NAMES:
        raise ValueError("language must be python, cpp14, or java11")
    if len(code) > 12_000 or len(stdin) > 2_000:
        raise ValueError("Code or input is too large")

    payload = {
        "language_id": _language_ids()[language],
        "source_code": code,
        "stdin": stdin,
        "cpu_time_limit": 2,
        "wall_time_limit": 5,
        "memory_limit": 512_000,
        "max_processes_and_or_threads": 60,
        "max_file_size": 1_024,
    }
    if expected_output is not None:
        payload["expected_output"] = expected_output
    if language == "cpp14":
        payload["compiler_options"] = "-std=c++14"

    result = _request("/submissions?wait=true", payload)
    status = result.get("status", {}).get("description", "Unknown")
    return {
        "mode": "local-judge0",
        "status": status,
        "passed": status == "Accepted",
        "stdout": (result.get("stdout") or "").strip()[:2_000],
        "stderr": (result.get("stderr") or "").strip()[:2_000],
        "compile_output": (result.get("compile_output") or "").strip()[:2_000],
        "time": result.get("time"),
        "memory": result.get("memory"),
    }


def execute_python(code: str, stdin: str) -> dict:
    """Backward-compatible helper used by later workshop material."""
    return execute_code("python", code, stdin)
