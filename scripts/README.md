# Workshop Scripts

These files maintain the workshop; they are not part of the daily agent lessons.

Learners should use the simpler root command:

```bash
./workshop start
./workshop doctor
./workshop stop
```

Instructor utilities:

- `check_course.py` validates the course structure, notebooks, documentation, dependencies, and links.
- `make-student-release.sh` creates a learner copy without QA answers, secrets, environments, or generated state.
- `start-mlflow.sh` and `stop-mlflow.sh` are called internally by the root `workshop` command.

Generated MLflow state is stored in the hidden root `.workshop/` folder.
