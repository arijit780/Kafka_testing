#!/usr/bin/env bash
set -euo pipefail

docker-compose exec -T kafka1 kafka-topics.sh --list --bootstrap-server kafka1:9092
