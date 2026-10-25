# Workshop troubleshooting

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

In Jupyter, select `Kernel -> Change Kernel` and choose the workshop kernel. If it is absent, register it again using the command in the root README.

## Port 5001 is already in use

Try the workshop stop command:

```bash
./workshop stop
./workshop start
```

## The model endpoint is unavailable

The workshop host service must be running at `http://127.0.0.1:8317/v1`. This service is separate from Jupyter and MLflow. Once it is running, repeat `./workshop doctor`.

## `workshop-gemini` is not found

MLflow is running but its Gateway endpoint has not been created. Follow section 3 in the root README and use the endpoint name exactly as written.

## A structured model response fails validation

Rerun the cell once. If it repeats, inspect the MLflow trace to see the raw model response. Confirm that the prompt asks for the same fields as the Pydantic schema.

## A notebook cannot import `graph_image`

Start Jupyter from the day folder shown in that day's README. Restart the kernel after changing folders or installing packages.

## Local Judge0 is unavailable

Start Docker, then run:

```bash
./workshop judge0-start
./workshop judge0-test
```

If startup fails, inspect `./workshop judge0-logs`. Judge0 CE `v1.13.1` is officially tested on Linux; use the workshop Linux or WSL 2 fallback if Docker Desktop cannot run its privileged worker correctly.

## A Judge0 language smoke test fails

The smoke test must execute Python 3.8.1, C++14 with GCC 9.2, and Java 11. The Judge0 image uses its Java 13 compiler with `--release 11`, then runs the program with its OpenJDK 11 runtime. Inspect the first compiler or runtime error printed by `./workshop judge0-test`.

## Judge0 containers do not become healthy

Confirm Docker is running, then inspect the local Judge0 logs:

```bash
./workshop judge0-logs
```
