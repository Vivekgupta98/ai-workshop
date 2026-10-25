# Day 3: checkpoints and local Judge0

Build a three-test verifier. The run fails before test 3, restores its state from SQLite, and continues without repeating tests 1 and 2.

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
./workshop judge0-start
./workshop judge0-test
cd day-3/tutorial
jupyter lab
```

Open `day-3.ipynb`. Keep [MLflow](http://127.0.0.1:5001) open in another tab.

## Follow this order

1. Call local Judge0 through a small tool.
2. Run one test per graph step.
3. Fail before the third test and inspect the checkpoint.
4. Reopen SQLite, resume the thread, and inspect both MLflow traces.

## What success looks like

The resumed run executes only test 3, and MLflow shows separate failed and resumed traces.

## If you get stuck

If a previous run already finished, change `THREAD_ID`. For setup problems, run `./workshop doctor --start-judge0` from the workshop root.

**Exit question:** Why does the graph run one test per step instead of the whole suite in one node?
