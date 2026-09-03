# Workshop Troubleshooting

Run this first:

```bash
./workshop doctor
```

Fix the first failed check before investigating later symptoms.

## `pip` and `python` show different versions

Activate the workshop environment and use Python to invoke pip:

```bash
source .venv/bin/activate
python --version
python -m pip --version
python -m pip install -r requirements.txt
```

## Jupyter uses the wrong environment

In Jupyter, select **Kernel → Change Kernel → Python 3.12 — Agentic AI Workshop**. If it is absent, register it again using the command in the root README.

## Port 5001 is already in use

Try the workshop stop command:

```bash
./workshop stop
./workshop start
```

Day 7 has its own MLflow container. Stop the root MLflow server before starting the Day 7 stack.

## The model endpoint is unavailable

The workshop host service must be running at `http://127.0.0.1:8317/v1`. This service is separate from Jupyter and MLflow. Once it is running, repeat `./workshop doctor`.

## `workshop-gemini` is not found

MLflow is running but its Gateway endpoint has not been created. Follow section 3 in the root README and use the endpoint name exactly as written.

## A structured model response fails validation

Rerun the cell once. If it repeats, inspect the MLflow trace to see the raw model response. Confirm that the prompt asks for the same fields as the Pydantic schema.

## A notebook cannot import `graph_image`

Start Jupyter from the day folder shown in that day's README. Restart the kernel after changing folders or installing packages.

## Judge0 credentials or quota are unavailable

Set this in the root `.env` file:

```text
EXECUTION_MODE=mock
```

The mock supports the running tutorial case only. It teaches the tool contract and routing but does not validate arbitrary programs. Switch to `EXECUTION_MODE=judge0` for real execution.

## Judge0 returns timeout or quota errors

Stop repeated runs. Check the provider quota and verify that the notebook's execution limit is bounded. Do not increase CPU, wall-time, output, or process limits merely to hide an unknown failure.

## Docker services do not become healthy

Confirm Docker Desktop is running, then inspect service status and the first failing service's logs:

```bash
docker compose -f day-7/tutorial/compose.yaml ps
docker compose -f day-7/tutorial/compose.yaml logs temporal
```

## The Day 7 stream reconnects

This is expected after a short network interruption. The client uses SSE event IDs to request only unseen durable workflow events. If the workflow itself failed, inspect Temporal first and MLflow second.
