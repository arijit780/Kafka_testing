Kafka_testing
# Simple Kafka Playground ⚡

This repo sets up a simple Kafka + Zookeeper using Docker Compose and includes tiny Python example producer/consumer scripts.

## Prerequisites
- Docker & Docker Compose
- Python 3.8+

## Quick start

1. Start Kafka and Zookeeper:

```bash
docker-compose up -d
```

2. Create & activate a virtualenv and install dependencies:

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

3. In one terminal, start the consumer:

```bash
python consumer.py
```

4. In another terminal, run the producer:

```bash
python producer.py
```

You should see the consumer print messages sent by the producer.

## Useful Make targets
- `make up` — start Docker
- `make down` — stop Docker
- `make install` — create venv and install requirements
- `make run-producer` / `make run-consumer`

## Notes
- The Compose file uses Bitnami images and advertises Kafka on `localhost:9092` (works for local dev)
- If you want this repo pushed to a remote, add a remote and run:

```bash
git remote add origin <your-repo-url>
git push -u origin main
```
