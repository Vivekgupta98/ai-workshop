# Day 0 Pre-work — Setup and One-State AI

- **Time:** 45–60 minutes
- **You will build:** one direct model call and one one-node graph
- **Know first:** Python functions and dictionaries
- **Not required yet:** agents, loops, tools, or MLflow internals

## Start

Complete the [root setup](../README.md) first. From the workshop root:

```bash
source .venv/bin/activate
./workshop start
./workshop doctor
cd day-0/tutorial
jupyter lab
```

Open `day-0.ipynb` and select **Python 3.12 — Agentic AI Workshop**.

## Follow this order

1. Complete the [tutorial](tutorial/README.md) one cell at a time.
2. Explain the difference between the direct model call and graph invocation.
3. Move to the [homework](exercise/README.md). Complete one checkpoint at a time.

The tutorial introduces the [running knapsack example](../RUNNING_EXAMPLE.md). Homework uses a different list-index bug.

## What success looks like

- The model responds through `workshop-gemini`.
- The graph image has one application node.
- The final explanation is read from graph state.
- No API key appears in the notebook.

## If you get stuck

Return to the workshop root and run `./workshop doctor`. For kernel, import, or Gateway problems, use [the troubleshooting guide](../TROUBLESHOOTING.md).

**Exit check:** What did explicit graph state add to the direct model call?
