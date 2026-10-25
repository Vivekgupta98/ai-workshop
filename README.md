# Agentic AI Workshop

This repository contains Day 0 pre-work and five workshop days. The course starts with one model call, adds LangGraph state and control flow, introduces local code execution with Judge0, and ends with an MLflow evaluation of five repair agents.

Days 0 to 4 use the same [0/1-knapsack bug](RUNNING_EXAMPLE.md). Day 5 switches to three Codeforces wrong-answer cases rated 1000, 1600, and 2200.

## Setup

Run these commands from the folder containing this README.

### 1. Check Python

```bash
python3 --version
```

Use Python 3.12. Windows learners should use WSL 2 so the workshop commands and local Judge0 setup match the course.

### 2. Create the environment

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Register the Jupyter kernel once:

```bash
python -m ipykernel install --user \
  --name agentic-ai-workshop \
  --display-name "Python 3.12: Agentic AI Workshop"
```

### 3. Check the workshop model

The model service at `http://127.0.0.1:8317/v1` is separate from this repository. The instructor or workshop host starts it. The local workshop credential is `123456`; it is not a personal provider key.

### 4. Start MLflow

```bash
./workshop start
```

Open [http://127.0.0.1:5001](http://127.0.0.1:5001) and keep it running through Day 5.

### 5. Configure the MLflow Gateway

This is a one-time setup:

1. Open `Settings -> LLM Connections` in MLflow.
2. Create `local-gemini-key` with the OpenAI provider, key `123456`, and base URL `http://127.0.0.1:8317/v1`.
3. Open `AI Gateway -> Endpoints`.
4. Create `workshop-gemini` with model `gemini-3-flash` and connection `local-gemini-key`.
5. Enable usage tracking and save.

### 6. Run the checks

```bash
./workshop doctor
```

Fix the first failed check, then run the command again. From Day 3 onward, Docker and local Judge0 are also required:

```bash
./workshop doctor --start-judge0
```

## Course map

| Session | Topic | Start page |
| --- | --- | --- |
| Day 0 pre-work | One model call and one graph node | [Day 0](day-0/README.md) |
| Day 1 | Conditional routing and a bounded retry loop | [Day 1](day-1/README.md) |
| Day 2 | Parallel nodes, streaming, and human review | [Day 2](day-2/README.md) |
| Day 3 | Checkpoints, SQLite persistence, local Judge0, and traces | [Day 3](day-3/README.md) |
| Day 4 | A two-node ReAct coding agent | [Day 4](day-4/README.md) |
| Day 5 | A wrong-answer repair benchmark in MLflow | [Day 5](day-5/README.md) |

Each day has a completed tutorial notebook under `day-N/tutorial/`. Run one cell at a time on the first pass.

## Start Day 0

```bash
cd day-0/tutorial
jupyter lab
```

Open `day-0.ipynb` and choose the workshop kernel.

## Local Judge0 from Day 3

Judge0 runs in Docker on your machine. The workshop does not use RapidAPI or any hosted Judge0 key.

```bash
./workshop judge0-start
./workshop judge0-test
```

The smoke test runs Python 3, C++14, and Java 11. Read the [local Judge0 guide](judge0/README.md) if startup or language checks fail.

## Stop the services

When you finish:

```bash
./workshop judge0-stop
./workshop stop
```

## Other guides

- [Programme overview](OVERVIEW.md)
- [Running example](RUNNING_EXAMPLE.md)
- [Glossary](GLOSSARY.md)
- [Troubleshooting](TROUBLESHOOTING.md)

## For instructors

Check the current Days 0 to 5 structure, notebooks, dependency pins, and links with:

```bash
python scripts/check_course.py
```

Create a clean learner copy with `./scripts/make-student-release.sh`.
