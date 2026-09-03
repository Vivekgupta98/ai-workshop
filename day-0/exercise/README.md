# Day 0 Homework — Build Your First Graph

## Goal

Build a one-state LangGraph application without copying the completed tutorial graph. Your graph must receive a problem statement and Python code, ask the model to explain what the code does, and return the explanation.

Start with `homework.ipynb` in this folder.

## Start

From the workshop root:

```bash
source .venv/bin/activate
./workshop start
cd day-0/exercise
jupyter lab
```

Open `homework.ipynb`, select **Python 3.12 — Agentic AI Workshop**, and complete one checkpoint at a time. The unfinished `TODO` cells are intentional, so do not use **Run All** until you have completed them.

## Requirements

1. Connect to the shared MLflow Gateway.
2. Define a `TypedDict` state containing `problem`, `code`, and `explanation`.
3. Create one node named `explain_code`.
4. Add `START → explain_code → END`.
5. Compile and display the graph with `show_graph`.
6. Invoke it with the supplied example and one example of your own.
7. Print only the final explanation for each run.

## Acceptance checks

- The notebook runs from top to bottom in a fresh kernel.
- Both the problem statement and code reach the model.
- The result is read from graph state rather than calling the model directly in the test cell.
- The graph image contains exactly one application node.
- No API key is written into the notebook.

When these checks pass, your graph image should show one application node and the final cell should print an explanation produced through the graph.

## Submit

- Your completed `homework.ipynb`.
- The graph image or a screenshot of the rendered graph.
- A two-sentence answer: what does the state hold, and what does the node do?

## Hint

The node should return a dictionary containing only the state field it updates.

## Common mistakes

- Calling the model directly from the final test cell instead of invoking the graph.
- Returning the full input state from the node instead of only `explanation`.
- Putting a provider key in the notebook.

## Optional challenge

Add a second output field named `possible_bug` without adding another graph node.
