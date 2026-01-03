#!/usr/bin/env bash
set -euo pipefail
if [ -z "${1:-}" ]; then
  echo "Usage: $0 <topic-name> [partitions] [replication]"
  exit 1
fi
TOPIC=$1
PARTS=${2:-3}
REPL=${3:-3}

echo "Creating topic '$TOPIC' (partitions=$PARTS, replication=$REPL)"

docker-compose exec -T kafka1 kafka-topics.sh \
  --create --topic "$TOPIC" --partitions "$PARTS" --replication-factor "$REPL" \
  --bootstrap-server kafka1:9092

 echo "Done."