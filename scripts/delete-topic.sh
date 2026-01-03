#!/usr/bin/env bash
set -euo pipefail
if [ -z "${1:-}" ]; then
  echo "Usage: $0 <topic-name>"
  exit 1
fi

echo "Deleting topic '$1'"

docker-compose exec -T kafka1 kafka-topics.sh --delete --topic "$1" --bootstrap-server kafka1:9092

echo "Done."