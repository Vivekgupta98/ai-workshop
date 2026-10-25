# Day 3 tutorial

The notebook builds a resumable testcase verifier with local Judge0, LangGraph checkpoints, SQLite, and MLflow.

Run the setup commands in [the Day 3 guide](../README.md), then run `jupyter lab` in this folder and open `day-3.ipynb` with the **Python 3.12: Agentic AI Workshop** kernel.

The important distinction is:

- a checkpoint stores state after a graph step;
- SQLite keeps that state after the Python process stops;
- an MLflow trace shows what ran and where it failed.

Judge0 runs locally and supports Python 3.8.1, C++14, and Java 11. See [the local Judge0 guide](../../judge0/README.md) for Docker setup.

References: [LangGraph persistence](https://docs.langchain.com/oss/python/langgraph/persistence), [MLflow LangGraph tracing](https://mlflow.org/docs/latest/genai/tracing/integrations/listing/langgraph/), and [Judge0 submissions](https://github.com/judge0/judge0/blob/master/docs/api/submissions/submissions.md).
