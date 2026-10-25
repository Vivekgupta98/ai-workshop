#!/usr/bin/env bash
set -euo pipefail

WORKSHOP_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
JUDGE0_DIR="$WORKSHOP_ROOT/judge0"
CONFIG="$JUDGE0_DIR/judge0.conf"
COMPOSE="$JUDGE0_DIR/docker-compose.yml"

if ! command -v docker >/dev/null 2>&1; then
  echo "Docker is not installed. Install Docker, then try again."
  exit 1
fi

if ! docker info >/dev/null 2>&1; then
  echo "Docker is installed but not running. Start Docker, then try again."
  exit 1
fi

if [[ ! -f "$CONFIG" ]]; then
  REDIS_SECRET="$(openssl rand -hex 24)"
  POSTGRES_SECRET="$(openssl rand -hex 24)"
  awk \
    -v redis="$REDIS_SECRET" \
    -v postgres="$POSTGRES_SECRET" \
    '{gsub(/__REDIS_PASSWORD__/, redis); gsub(/__POSTGRES_PASSWORD__/, postgres); print}' \
    "$JUDGE0_DIR/judge0.conf.example" > "$CONFIG"
  chmod 600 "$CONFIG"
  echo "Created judge0/judge0.conf with local random passwords."
fi

docker compose -f "$COMPOSE" up -d db redis
docker compose -f "$COMPOSE" up -d

echo "Waiting for Judge0 at http://127.0.0.1:2358 ..."
for _ in {1..90}; do
  if curl -fsS http://127.0.0.1:2358/about >/dev/null 2>&1; then
    echo "Judge0 API is ready."
    break
  fi
  sleep 1
done

if ! curl -fsS http://127.0.0.1:2358/about >/dev/null 2>&1; then
  echo "Judge0 did not become ready. Run: ./workshop judge0-logs"
  exit 1
fi

# Judge0 1.13.1 has a Java 11 runtime but no Java 11 compiler. Its Java 13
# compiler can target the Java 11 language and API with --release 11. Language
# 27 is unused by the workshop, so we turn it into the local Java 11 entry.
if ! docker compose -f "$COMPOSE" exec -T workers sh -lc \
  'test -x /usr/local/openjdk13/bin/javac && test -x /usr/lib/jvm/java-11-openjdk-amd64/bin/java'; then
  echo "The Judge0 worker does not contain the required Java compiler and Java 11 runtime."
  exit 1
fi

docker compose -f "$COMPOSE" exec -T db bash -lc \
  'PGPASSWORD="$POSTGRES_PASSWORD" psql -v ON_ERROR_STOP=1 -U "$POSTGRES_USER" -d "$POSTGRES_DB" -c "UPDATE languages SET name = '\''Java (OpenJDK 11)'\'', compile_cmd = '\''/usr/local/openjdk13/bin/javac --release 11 %s Main.java'\'', run_cmd = '\''/usr/lib/jvm/java-11-openjdk-amd64/bin/java Main'\'', is_archived = FALSE WHERE id = 27;"' \
  >/dev/null

if ! curl -fsS http://127.0.0.1:2358/languages | grep -q 'Java (OpenJDK 11)'; then
  echo "Java 11 could not be configured in the local Judge0 database."
  exit 1
fi

echo "Judge0 is ready with Python, C++14, and Java 11."
