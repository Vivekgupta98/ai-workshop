# Day 0: one model call and one graph node

Time: about 45 to 60 minutes.

Day 0 compares a direct model call with a one-node LangGraph. The lesson introduces explicit state through the workshop knapsack example.

## Start

Complete the [root setup](../README.md), then run:

```bash
source .venv/bin/activate
./workshop start
./workshop doctor
cd day-0/tutorial
jupyter lab
```

Open `day-0.ipynb` and choose the workshop kernel.

## Follow this order

1. Call `workshop-gemini` directly.
2. Read the buggy knapsack program.
3. Predict the state returned by a one-node graph.
4. Run the graph and inspect its state.
5. Remove a required state field, inspect the error, and restore it.

## What success looks like

The model responds, the graph image contains one application node, and the final explanation is stored in graph state.

## If you get stuck

Run `./workshop doctor` from the workshop root. Use [TROUBLESHOOTING.md](../TROUBLESHOOTING.md) for kernel, import, or Gateway problems.

**Exit question:** What did graph state add to the direct model call?
