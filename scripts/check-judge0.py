from __future__ import annotations

import json
import sys
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


BASE_URL = "http://127.0.0.1:2358"


def request_json(path: str, payload: dict | None = None):
    body = None if payload is None else json.dumps(payload).encode()
    request = Request(
        f"{BASE_URL}{path}",
        data=body,
        headers={"Content-Type": "application/json"},
        method="GET" if payload is None else "POST",
    )
    with urlopen(request, timeout=15) as response:
        return json.load(response)


def language_id(languages: list[dict], exact_name: str) -> int:
    for language in languages:
        if language["name"] == exact_name:
            return language["id"]
    raise RuntimeError(f"Required Judge0 language is missing: {exact_name}")


def run_case(label: str, language: int, source: str, compiler_options: str | None = None):
    payload = {
        "language_id": language,
        "source_code": source,
        "expected_output": "42\n",
        "cpu_time_limit": 2,
        "wall_time_limit": 5,
        "memory_limit": 512_000,
        "max_processes_and_or_threads": 60,
        "max_file_size": 1_024,
    }
    if compiler_options:
        payload["compiler_options"] = compiler_options

    result = request_json("/submissions?wait=true", payload)
    status = result.get("status", {}).get("description", "Unknown")
    if status != "Accepted":
        detail = result.get("compile_output") or result.get("stderr") or result.get("message") or ""
        raise RuntimeError(f"{label}: {status}: {detail.strip()}")
    print(f"✓ {label}: {status}")


def main() -> None:
    try:
        about = request_json("/about")
        languages = request_json("/languages")
        print(f"Judge0 {about.get('version', 'unknown')} at {BASE_URL}")

        run_case(
            "Python 3.8.1",
            language_id(languages, "Python (3.8.1)"),
            "print(42)",
        )
        run_case(
            "C++14 (GCC 9.2.0)",
            language_id(languages, "C++ (GCC 9.2.0)"),
            "#include <iostream>\nint main() { std::cout << 42 << '\\n'; }",
            "-std=c++14",
        )
        run_case(
            "Java 11",
            language_id(languages, "Java (OpenJDK 11)"),
            'class Main { public static void main(String[] args) { System.out.println(" 42 ".strip()); } }',
        )
    except (HTTPError, URLError, TimeoutError, RuntimeError, json.JSONDecodeError) as exc:
        print(f"✗ Judge0 smoke test failed: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
