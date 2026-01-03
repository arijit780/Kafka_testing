#!/usr/bin/env bash
set -euo pipefail

# Bring up core cluster + advanced services
echo "Starting containers..."
docker-compose up -d

# Wait for Kafka broker (kafka1) to respond to topic list
echo "Waiting for kafka1 to be ready..."
for i in {1..40}; do
  if docker-compose exec -T kafka1 kafka-topics.sh --bootstrap-server kafka1:9092 --list >/dev/null 2>&1; then
    echo "kafka1 ready"
    break
  fi
  sleep 3
done

# Wait for Schema Registry
echo "Waiting for Schema Registry at http://localhost:8081..."
for i in {1..40}; do
  if curl -sS -f http://localhost:8081/subjects >/dev/null 2>&1; then
    echo "Schema Registry ready"
    break
  fi
  sleep 3
done

# Wait for Connect
echo "Waiting for Connect REST at http://localhost:8083..."
for i in {1..40}; do
  if curl -sS -f http://localhost:8083/ >/dev/null 2>&1; then
    echo "Connect ready"
    break
  fi
  sleep 3
done

# Register schemas and start connectors
echo "Registering schemas..."
./scripts/register_schemas.py || true

echo "Starting connectors..."
curl -X POST -H "Content-Type: application/json" --data @connectors/file-sink.json http://localhost:8083/connectors || true

cat <<EOF

All services started. Next steps:
 - Create a topic (e.g. ./scripts/create-topic.sh users 3 3)
 - Run Avro producer: make run-avro-producer
 - Run Avro consumer: make run-avro-consumer
 - Check connector output: /tmp/kafka-connect-sink-output.txt

EOF
