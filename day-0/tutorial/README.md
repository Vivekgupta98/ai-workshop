# Day 0 — One-State LangGraph with MLflow Gateway

This is the completed notebook used in the recorded tutorial. The video follows a direct model call, introduces the running knapsack example, predicts graph state, builds one node, renders the graph, and checks the returned state.

Complete the environment and shared MLflow setup in the repository's main `README.md` first.

Then enter Day 0 and start JupyterLab:

```bash
cd day-0/tutorial
jupyter lab
```

Select **Python 3.12 — Agentic AI Workshop** if Jupyter asks for a kernel, then run `day-0.ipynb` from top to bottom.

Before running each section, read its short prediction question and guess what will happen. Run one cell at a time rather than using **Run All** on your first pass. A successful run ends with a graph image, a model reply, and passing structural checks.

The notebook:

1. Produces a first model response before introducing graph abstractions.
2. Compares a direct call with explicit graph state.
3. Builds and renders a one-state LangGraph.
4. Runs deterministic structural checks around the model output.
5. Demonstrates what happens when required state is missing.

The notebook uses `workshop-gemini` as its model name. MLflow forwards requests to `gemini-3-flash`, while keeping the real provider key outside the notebook.

After watching the video, continue to the [homework](../exercise/README.md).
