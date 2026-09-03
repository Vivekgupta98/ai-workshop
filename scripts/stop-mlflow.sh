#!/usr/bin/env bash
set -euo pipefail

WORKSHOP_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
MLFLOW_PID_FILE="$WORKSHOP_ROOT/.workshop/mlflow.pid"

if [[ ! -f "$MLFLOW_PID_FILE" ]]; then
  echo "No workshop MLflow process was found."
  exit 0
fi

MLFLOW_PID="$(<"$MLFLOW_PID_FILE")"
MLFLOW_COMMAND="$(ps -p "$MLFLOW_PID" -o command= 2>/dev/null || true)"

if [[ "$MLFLOW_COMMAND" == *mlflow*server* ]]; then
  kill "$MLFLOW_PID"
  echo "MLflow stopped."
else
  echo "MLflow is not running."
fi

rm -f "$MLFLOW_PID_FILE"
