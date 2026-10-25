# Day 4: an evidence-driven ReAct coding agent

Turn the Day 3 verifier into a bounded agent. The model runs visible testcases one at a time and decides when it has enough evidence. A structured-output node then writes a validated diagnosis, confidence score, and fixed program into explicit graph state. Local Judge0 verifies the full suite outside the agent loop.

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
./workshop judge0-start
./workshop judge0-test
cd day-4/tutorial
jupyter lab
```

Open `day-4.ipynb`. Keep [MLflow](http://127.0.0.1:5001) open in another tab.

## Follow this order

1. Compare a fixed LLM flow with an agent that owns the next-action decision.
2. See why ReAct's reason, act, observe loop became useful.
3. Run one visible testcase and treat its result as evidence.
4. Define `RepairState` and the `RepairProposal` output schema.
5. Build the explicit `agent -> tools -> agent -> proposal` graph.
6. Let the agent request another testcase or leave the loop for structured output.
7. Verify the proposed code against every visible testcase.
8. Inspect the SQLite checkpoint and grouped MLflow traces.

## What success looks like

The agent runs only as many diagnostic testcases as it needs. `final_state` contains typed `diagnosis`, `confidence`, and `fixed_code` fields without regex parsing. The separate verification step reports `verified: True` and `3/3` visible tests passed.

## If you get stuck

The graph uses `recursion_limit=8` as a hard stop on graph steps. It is not a testcase or tool-call limit. If an old message history appears, change `THREAD_ID`.

**Homework:** add a bounded counterexample finder that generates valid inputs, computes expected outputs with a trusted oracle, and returns the smallest mismatch.

**Exit question:** What makes this an agent: access to Judge0, or deciding whether another observation is worth its cost?
