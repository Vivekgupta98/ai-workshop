# Workshop scripts

Learners normally use the root command:

```bash
./workshop start
./workshop doctor
./workshop judge0-start
./workshop judge0-test
./workshop stop
```

The scripts in this folder support those commands:

- `start-mlflow.sh` and `stop-mlflow.sh` manage the shared MLflow server.
- `start-judge0.sh` prepares and starts the local Judge0 stack.
- `check-judge0.py` runs Python, C++14, and Java 11 smoke tests.
- `check_course.py` validates the current Days 0 to 5 structure, notebooks, links, and pinned dependencies.
- `make-student-release.sh` creates a learner copy without local environments or generated state.

MLflow state and SQLite checkpoints are stored under the hidden `.workshop/` folder.
