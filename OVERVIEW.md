# Agentic AI Workshop — Programme Overview

## Format

The programme consists of asynchronous **Day 0 pre-work** and seven instructional days. Learners progress from one model call to a durable, observable, tool-using agent application.

## Audience

The workshop is for Python developers who are new to agent building. No LangGraph, MLflow, evaluation, multi-agent, or Temporal experience is expected.

## Running case

Every recorded tutorial uses the same 0/1-knapsack debugging problem. The specification is short, but the buggy program violates a subtle dynamic-programming invariant by iterating capacity upward and therefore reusing an item. See [RUNNING_EXAMPLE.md](RUNNING_EXAMPLE.md).

Homework deliberately uses different problems so students must transfer the ideas rather than copy the demonstration.

## Programme map

| Session | New mental model | Learner outcome |
| --- | --- | --- |
| Day 0 pre-work | A model call is input → probabilistic output; a graph makes state explicit | Call the model, build a one-node graph, and inspect its state |
| Day 1 | An agent is a bounded loop, not unlimited reasoning | Build retry and ReAct loops with deterministic stopping rules |
| Day 2 | Nodes specialize; routers make explicit decisions from state | Build a multi-state debugger with conditional routing |
| Day 3 | Traces are evidence; examples plus expectations form an evaluation dataset | Inspect spans and compare three architectures fairly |
| Day 4 | Tools act on the world and need contracts, limits, and verified outcomes | Verify a proposed fix through a guarded execution tool |
| Day 5 | Multiple agents help only when roles and handoffs are narrow | Coordinate test design and stress testing through typed state |
| Day 6 | Benchmarks require frozen variables; an LLM judge is a fallible evaluator | Calibrate a judge and make an evidence-backed release decision |
| Day 7 | Durable workflow state differs from browser, API, trace, and tool state | Operate a production-shaped application and explain its boundaries |

## Daily rhythm

Every day follows the same learning loop:

1. **Orient:** what we are building, why it matters, and what is not required yet.
2. **Predict:** identify state, next node, stopping condition, and maximum calls.
3. **Build:** implement one small checkpoint at a time.
4. **Observe:** inspect graph state and the MLflow trace.
5. **Break:** trigger one intentional failure and recover from it.
6. **Verify:** run deterministic acceptance checks.
7. **Reflect:** answer one concept question and preview the next day.

## Learning outcomes

By the end, learners can:

- Distinguish a one-shot model call, workflow, and agent.
- Design typed graph state and deterministic routing.
- Bound agent loops and tool usage.
- Read MLflow traces and construct evaluation datasets.
- Design safe execution-tool contracts.
- Explain when multi-agent decomposition helps or adds unnecessary complexity.
- Combine deterministic checks with a calibrated LLM judge.
- Explain durable execution, streaming, observability, and production gaps.

## Assessment strategy

- Notebook assertions check structure, state, bounds, and routing—not exact model prose.
- Each homework produces one graph image and one observable artifact such as a trace, evaluation table, or run ID.
- Optional challenges extend the same graph without blocking the core outcome.
- The instructor QA replica executes completed reference assignments, while student releases exclude it.
