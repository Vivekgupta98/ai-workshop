# Day 2: parallel nodes, streaming, and human review

Time: about 2 hours.

Day 2 changes how graph work is scheduled and observed. It covers fan-out, reducers, streamed updates, and a graph that pauses for a human decision.

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-2/tutorial
jupyter lab
```

Open `day-2.ipynb` and choose the workshop kernel.

## Follow this order

1. Run three specialist nodes in parallel.
2. Merge their writes with a reducer.
3. Stream updates from a bounded loop.
4. Add `interrupt()` and resume with `Command`.
5. Confirm that the iteration limit still stops repeated retries.

## What success looks like

The parallel graph merges all three diagnoses, streaming shows each completed step, and human review pauses and resumes without bypassing the loop limit.

## If you get stuck

Print streamed chunks before adding the interrupt. If parallel writes fail, inspect the reducer on the shared state key.

**Exit question:** Does streaming change the graph result, or only when the caller sees it?
