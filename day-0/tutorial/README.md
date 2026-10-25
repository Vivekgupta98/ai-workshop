# Day 0 tutorial

Start from the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-0/tutorial
jupyter lab
```

Open `day-0.ipynb` and run one cell at a time.

The notebook makes a direct model call, introduces the [knapsack bug](../../RUNNING_EXAMPLE.md), builds a one-node graph, and inspects the returned state. The final section removes required input so learners can see the state contract fail.

A successful run produces a model response, one graph image, and passing structural checks.
