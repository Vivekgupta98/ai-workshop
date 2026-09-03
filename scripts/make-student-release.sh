#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
DESTINATION="${1:-$ROOT/student-release}"

mkdir -p "$DESTINATION"
rsync -a --delete \
  --exclude '.env' \
  --exclude '.git/' \
  --exclude '.venv/' \
  --exclude '.workshop/' \
  --exclude 'QA/' \
  --exclude 'student-release/' \
  --exclude '**/__pycache__/' \
  --exclude '**/.ipynb_checkpoints/' \
  --exclude '**/.next/' \
  --exclude '**/node_modules/' \
  --exclude 'day-7/tutorial/mlflow-data/' \
  --exclude 'day-7/tutorial/temporal-data/' \
  "$ROOT/" "$DESTINATION/"

echo "Student release created at $DESTINATION"
