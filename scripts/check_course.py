from __future__ import annotations

import ast
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DAYS = range(6)
TUTORIALS = [
    ROOT / f"day-{day}" / "tutorial" / f"day-{day}.ipynb"
    for day in DAYS
]
SKIP = {".git", ".venv", ".workshop", "mlruns", "node_modules", "student-release"}

NOTEBOOK_MARKERS = {
    0: ("StateGraph", "capacity"),
    1: ("route_bug", "attempt"),
    2: ("stream_mode", "interrupt"),
    3: ("SqliteSaver", "run_code"),
    4: ("ToolNode", "run_knapsack_test"),
    5: ("CORE_CASES", "mlflow.genai.evaluate"),
}


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
            errors.append(f"root README is missing setup guidance: {required}")

    for day in DAYS:
        day_dir = ROOT / f"day-{day}"
        tutorial_dir = day_dir / "tutorial"
        if not tutorial_dir.is_dir():
            errors.append(f"missing day-{day}/tutorial")

        day_readme = day_dir / "README.md"
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

        tutorial_readme = tutorial_dir / "README.md"
        if not tutorial_readme.exists():
            errors.append(f"missing day-{day}/tutorial/README.md")
        elif "jupyter lab" not in tutorial_readme.read_text():
            errors.append(
                f"{tutorial_readme.relative_to(ROOT)} is missing jupyter lab startup guidance"
            )

    image_pattern = re.compile(r"!\[[^]]*\]\(([^)]+)\)")
    for day, path in zip(DAYS, TUTORIALS):
        if not path.exists():
            errors.append(f"missing tutorial notebook: {path.relative_to(ROOT)}")
            continue

        try:
            notebook = json.loads(path.read_text())
        except json.JSONDecodeError as exc:
            errors.append(f"invalid notebook JSON: {path.relative_to(ROOT)}: {exc}")
            continue

        text = "\n".join(cell_source(cell) for cell in notebook["cells"])
        for marker in NOTEBOOK_MARKERS[day]:
            if marker not in text:
                errors.append(f"{path.relative_to(ROOT)} is missing lesson marker: {marker}")

        for index, cell in enumerate(notebook["cells"]):
            source = cell_source(cell)
            if cell["cell_type"] == "code":
                try:
                    ast.parse(source)
                except SyntaxError as exc:
                    errors.append(
                        f"invalid Python in {path.relative_to(ROOT)} cell {index}: {exc.msg}"
                    )
            elif cell["cell_type"] == "markdown":
                for target in image_pattern.findall(source):
                    if "://" not in target and not (path.parent / target).exists():
                        errors.append(
                            f"missing notebook image in {path.relative_to(ROOT)}: {target}"
                        )

    for line in (ROOT / "requirements.txt").read_text().splitlines():
        if line.strip() and not line.startswith("#") and "==" not in line:
            errors.append(f"unpinned dependency: {line}")

    link_pattern = re.compile(r"\[[^]]*\]\(([^)]+)\)")
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
        "Course checks passed for Days 0 to 5: READMEs, tutorial notebooks, "
        "lesson markers, images, dependency pins, and links."
    )


if __name__ == "__main__":
    main()
