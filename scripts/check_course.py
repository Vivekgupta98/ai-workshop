from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TUTORIALS = [
    ROOT / f"day-{day}" / "tutorial" / f"day-{day}.ipynb"
    for day in range(7)
]
EXERCISES = [
    ROOT / "day-0/exercise/homework.ipynb",
    ROOT / "day-1/exercise/homework.ipynb",
    ROOT / "day-2/exercise/homework.ipynb",
    ROOT / "day-3/exercise/evaluation-lab.ipynb",
    ROOT / "day-4/exercise/homework.ipynb",
    ROOT / "day-5/exercise/homework.ipynb",
    ROOT / "day-6/exercise/judge-calibration.ipynb",
]
SKIP = {".git", ".venv", ".workshop", ".next", "QA", "mlruns", "node_modules"}


def cell_source(cell: dict) -> str:
    source = cell.get("source", "")
    return "".join(source) if isinstance(source, list) else source


def main() -> None:
    errors: list[str] = []

    root_readme = (ROOT / "README.md").read_text()
    for required in (
        "python3 --version",
        "./workshop doctor",
        "## Course map",
        "TROUBLESHOOTING.md",
        "is separate from this repository",
    ):
        if required not in root_readme:
            errors.append(f"root README is missing beginner setup guidance: {required}")

    for day in range(8):
        for part in ("tutorial", "exercise"):
            if not (ROOT / f"day-{day}" / part).is_dir():
                errors.append(f"missing day-{day}/{part}")

        day_readme = ROOT / f"day-{day}" / "README.md"
        if not day_readme.exists():
            errors.append(f"missing day-{day}/README.md")
        else:
            text = day_readme.read_text()
            for heading in (
                "## Start",
                "## Follow this order",
                "## What success looks like",
                "## If you get stuck",
            ):
                if heading not in text:
                    errors.append(f"{day_readme.relative_to(ROOT)} is missing {heading}")

        tutorial_readme = ROOT / f"day-{day}" / "tutorial" / "README.md"
        exercise_readme = ROOT / f"day-{day}" / "exercise" / "README.md"
        if not tutorial_readme.exists():
            errors.append(f"missing day-{day}/tutorial/README.md")
        else:
            expected_command = "jupyter lab" if day < 7 else "docker compose"
            if expected_command not in tutorial_readme.read_text():
                errors.append(
                    f"{tutorial_readme.relative_to(ROOT)} is missing {expected_command} startup guidance"
                )
        if not exercise_readme.exists():
            errors.append(f"missing day-{day}/exercise/README.md")
        else:
            exercise_text = exercise_readme.read_text()
            if "## Start" not in exercise_text:
                errors.append(f"{exercise_readme.relative_to(ROOT)} is missing ## Start")
            if "When these checks pass" not in exercise_text:
                errors.append(
                    f"{exercise_readme.relative_to(ROOT)} is missing a visible success description"
                )

    for path in TUTORIALS:
        if not path.exists():
            errors.append(f"missing tutorial notebook: {path.relative_to(ROOT)}")
            continue
        notebook = json.loads(path.read_text())
        code_cells = [cell for cell in notebook["cells"] if cell["cell_type"] == "code"]
        if any(cell.get("execution_count") is None for cell in code_cells):
            errors.append(f"unexecuted tutorial cell: {path.relative_to(ROOT)}")
        if any(
            output.get("output_type") == "error"
            for cell in code_cells
            for output in cell.get("outputs", [])
        ):
            errors.append(f"saved tutorial error: {path.relative_to(ROOT)}")
        if "capacity" not in "\n".join(cell_source(cell) for cell in notebook["cells"]):
            errors.append(f"running example missing: {path.relative_to(ROOT)}")

    for path in EXERCISES:
        if not path.exists():
            errors.append(f"missing exercise notebook: {path.relative_to(ROOT)}")
            continue
        notebook = json.loads(path.read_text())
        text = "\n".join(cell_source(cell) for cell in notebook["cells"])
        if text.lower().count("checkpoint") < 3:
            errors.append(f"exercise needs progressive checkpoints: {path.relative_to(ROOT)}")

    for line in (ROOT / "requirements.txt").read_text().splitlines():
        if line.strip() and not line.startswith("#") and "==" not in line:
            errors.append(f"unpinned dependency: {line}")

    link_pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
    for markdown in ROOT.rglob("*.md"):
        if any(part in SKIP for part in markdown.parts):
            continue
        for target in link_pattern.findall(markdown.read_text()):
            target = target.strip().split("#", 1)[0]
            if not target or "://" in target or target.startswith("mailto:"):
                continue
            if not (markdown.parent / target).resolve().exists():
                errors.append(f"broken link in {markdown.relative_to(ROOT)}: {target}")

    if errors:
        print("Course checks failed:")
        for error in errors:
            print(f"- {error}")
        raise SystemExit(1)

    print(
        "Course checks passed: beginner READMEs, layout, tutorials, checkpoints, "
        "running example, pins, and links"
    )


if __name__ == "__main__":
    main()
