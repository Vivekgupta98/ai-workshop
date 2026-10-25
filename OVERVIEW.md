# Agentic AI Workshop: programme overview

## Format

The programme has Day 0 pre-work and five workshop days. Learners move from a direct model call to a tool-using coding agent, then compare several agent designs with deterministic evaluation.

## Audience

The workshop is for Python developers who are new to LangGraph, MLflow tracing, tool calling, and agent evaluation.

## Running examples

Days 0 to 4 use one 0/1-knapsack program with an upward-loop bug. The code is valid and often produces believable answers, but it reuses an item. See [RUNNING_EXAMPLE.md](RUNNING_EXAMPLE.md).

Day 5 uses workshop-authored wrong programs for three Codeforces problems. This gives the benchmark a 1000, 1600, and 2200 rating ladder.

## Programme map

| Session | Main idea | Notebook outcome |
| --- | --- | --- |
| Day 0 | A graph makes model state explicit | Compare a direct call with a one-node graph |
| Day 1 | Deterministic code can route and stop model work | Build a specialist router and a bounded retry loop |
| Day 2 | Graph execution can fan out, stream updates, and pause | Run parallel reviewers, stream a loop, and resume human review |
| Day 3 | Checkpoints are saved after graph steps | Resume a failed Judge0 verifier from SQLite and inspect its traces |
| Day 4 | ReAct alternates model decisions and tool results | Build a two-node coding agent that tests its repairs locally |
| Day 5 | Agent designs need a shared benchmark | Compare five repair agents with Judge0, MLflow, and an LLM judge |

## Teaching pattern

Each notebook asks learners to predict the next state, build or inspect a small graph, run it, and then break one assumption. Days 3 to 5 also use local Judge0 so code claims can be checked by execution.

## Learning outcomes

By the end of Day 5, learners can:

- distinguish a direct model call, fixed workflow, and agent loop;
- define typed state, nodes, reducers, and conditional edges;
- use deterministic limits around retries and tool calls;
- pause and resume a graph with checkpoints;
- expose local Judge0 through a narrow tool contract;
- read MLflow traces and evaluation tables;
- compare agent quality with compile rate, solve rate, false success, and cost;
- compare an LLM judge with deterministic execution results.

## Validation

`python scripts/check_course.py` checks the Days 0 to 5 layout, README structure, notebook source, dependency pins, and local links. Live model, MLflow, and Judge0 checks remain in `./workshop doctor`.
