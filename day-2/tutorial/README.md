# Day 2 tutorial

Start from the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-2/tutorial
jupyter lab
```

Open `day-2.ipynb` and run one section at a time.

The notebook has three parts:

1. Three specialists fan out from `START` and merge their diagnoses through a reducer.
2. A bounded loop returns progress through `stream(stream_mode="updates")`.
3. A `human_review` node pauses with `interrupt()` and resumes from `Command(resume=...)`.

The same [knapsack bug](../../RUNNING_EXAMPLE.md) is used throughout the lesson.
