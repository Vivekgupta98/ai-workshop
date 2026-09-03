#!/usr/bin/env bash
set -euo pipefail

WORKSHOP_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
VENV_DIR="$WORKSHOP_ROOT/.venv"
STATE_DIR="$WORKSHOP_ROOT/.workshop"
MLFLOW_LOG="$STATE_DIR/mlflow.log"
MLFLOW_PID_FILE="$STATE_DIR/mlflow.pid"

mkdir -p "$STATE_DIR"

if [[ ! -f "$VENV_DIR/bin/activate" ]]; then
  echo "Run the setup steps in README.md first."
  exit 1
fi

if curl -fsS http://127.0.0.1:5001/health >/dev/null 2>&1; then
  if [[ -f "$MLFLOW_PID_FILE" ]]; then
    echo "MLflow is already running at http://127.0.0.1:5001"
    exit 0
  fi

  echo "Port 5001 is being used by an older MLflow server."
  echo "Stop that server with Control+C, then run this command again."
  exit 1
fi

source "$VENV_DIR/bin/activate"

MLFLOW_TRACKING_URI="http://127.0.0.1:5001" nohup mlflow server \
  --host 127.0.0.1 \
  --port 5001 \
  --backend-store-uri "sqlite:///$STATE_DIR/mlflow.db" \
  --default-artifact-root "$STATE_DIR/mlruns" \
  > "$MLFLOW_LOG" 2>&1 &

MLFLOW_PID=$!
echo "$MLFLOW_PID" > "$MLFLOW_PID_FILE"
echo "Starting MLflow..."

until curl -fsS http://127.0.0.1:5001/health >/dev/null 2>&1; do
  if ! kill -0 "$MLFLOW_PID" 2>/dev/null; then
    rm -f "$MLFLOW_PID_FILE"
    echo "MLflow could not start. Check $MLFLOW_LOG"
    exit 1
  fi
  sleep 1
done

echo "MLflow: http://127.0.0.1:5001"
