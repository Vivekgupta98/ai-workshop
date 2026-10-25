# Day 1 tutorial

Start from the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-1/tutorial
jupyter lab
```

Open `day-1.ipynb` and run it from top to bottom.

Part 1 builds a triage node, three specialist branches, and a deterministic router. Part 2 builds a bounded retry loop that reads its earlier attempts. Both parts use the [knapsack bug](../../RUNNING_EXAMPLE.md).

The intentional failures show what happens when a route falls outside its `Literal` contract or a loop loses its stopping rule.
