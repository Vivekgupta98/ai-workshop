# Day 1: routing and a bounded retry loop

Time: about 2 hours.

Day 1 builds two graph shapes around the same knapsack bug. The first routes to one specialist. The second retries its own diagnosis with a fixed iteration limit.

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-1/tutorial
jupyter lab
```

Open `day-1.ipynb` and choose the workshop kernel.

## Follow this order

1. Define structured bug categories.
2. Route state to one specialist without another model call.
3. Run the router on the knapsack bug.
4. Build a one-node retry loop that keeps attempt history.
5. Verify that deterministic code stops the loop.

## What success looks like

The routing graph visits triage, one specialist, and finalize. The retry graph appends its attempts and never exceeds its iteration limit.

## If you get stuck

Test the router and stopping rule with a small dictionary before calling the model. Debug graph wiring and model output separately.

**Exit question:** Which decisions belong to the model, and which belong to deterministic code?
