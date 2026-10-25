# Day 4 tutorial: evidence-driven ReAct

The notebook starts by separating fixed LLM flows from agents, then builds an explicit ReAct graph:

```text
START -> agent
          | tool call -> tools -> agent
          | no tool call -> proposal -> END
```

`RepairState` is a `TypedDict` containing messages, problem input, testcases, diagnosis, confidence, and fixed code. `SqliteSaver` stores that state by `thread_id`, and `recursion_limit` stops a loop that runs too long. The Judge0 tool executes one numbered testcase per call. After each observation, the model decides whether to gather more evidence or leave the loop.

The proposal node uses the `RepairProposal` Pydantic schema. The notebook reads its fields directly from state; it does not parse model prose with regular expressions.

The final verifier is deliberately outside the agent loop. It runs every visible testcase in order, so model confidence never substitutes for execution.

Run the setup commands in [the Day 4 guide](../README.md), then run `jupyter lab` in this folder and open `day-4.ipynb` with the **Python 3.12: Agentic AI Workshop** kernel.

References: [LangGraph agents](https://docs.langchain.com/oss/python/langgraph/agentic-concepts), [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [MLflow tracing](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langchain/), and the [local Judge0 guide](../../judge0/README.md).
