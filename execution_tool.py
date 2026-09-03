import os
import re

import judge0
from dotenv import load_dotenv


load_dotenv()


def _bounded(result) -> dict:
    return {
        "mode": "judge0",
        "status": str(result.status),
        "stdout": (result.stdout or "").strip()[:2_000],
        "error": (
            result.stderr or result.compile_output or result.message or ""
        ).strip()[:2_000],
    }


def _knapsack(stdin: str, reuse_items: bool) -> str:
    lines = [line for line in stdin.strip().splitlines() if line.strip()]
    n, capacity = map(int, lines[0].split())
    items = [tuple(map(int, line.split())) for line in lines[1:]]
    if len(items) != n:
        raise ValueError("Mock input does not contain n items")

    dp = [0] * (capacity + 1)
    for weight, value in items:
        if reuse_items:
            capacities = range(weight, capacity + 1)
        else:
            capacities = range(capacity, weight - 1, -1)
        for current in capacities:
            dp[current] = max(dp[current], dp[current - weight] + value)
    return str(dp[capacity])


def _mock(code: str, stdin: str) -> dict:
    if "seed" in code.lower() and "dp" not in code.lower():
        seed = int(stdin.strip() or "1")
        cases = {
            1: "2 5\n2 4\n3 5",
            2: "1 4\n2 3",
            3: "3 6\n2 4\n3 5\n4 7",
        }
        stdout = cases.get(seed, "1 4\n2 3")
    else:
        upward_loop = bool(
            re.search(r"range\s*\(\s*(weight|w)\s*,\s*(capacity|cap)\s*\+\s*1", code)
        )
        stdout = _knapsack(stdin, reuse_items=upward_loop)

    return {
        "mode": "mock",
        "status": "Accepted",
        "stdout": stdout,
        "error": "",
        "note": "Simulated only for the workshop knapsack example; not proof of arbitrary code execution.",
    }


def execute_python(code: str, stdin: str) -> dict:
    """Execute through Judge0, or simulate only the documented tutorial example."""
    if len(code) > 12_000 or len(stdin) > 2_000:
        raise ValueError("Code or input is too large")

    mode = os.getenv("EXECUTION_MODE", "mock").strip().lower()
    if mode == "mock":
        return _mock(code, stdin)
    if mode != "judge0":
        raise ValueError("EXECUTION_MODE must be mock or judge0")

    result = judge0.run(
        source_code=code,
        stdin=stdin,
        language=judge0.PYTHON,
        cpu_time_limit=2,
        wall_time_limit=4,
        memory_limit=128_000,
        max_processes_and_or_threads=8,
        max_file_size=128,
        enable_network=False,
    )
    return _bounded(result)
