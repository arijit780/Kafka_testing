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
- The Compose file uses Bitnami images and advertises Kafka on `localhost:9092/9093/9094` (works for local dev)
- Auto-topic creation is disabled so you can explicitly create topics with desired partitions/replication and learn about partitioning and leader election.

---

## Advanced (multi-broker) ⚙️
This repo includes a 3-broker Kafka cluster (kafka1,kafka2,kafka3) + Zookeeper to demonstrate replication, partitioning and leader election.

Ports:
- kafka1 = localhost:9092
- kafka2 = localhost:9093
- kafka3 = localhost:9094

Example workflows:

1) Start the cluster:

```bash
make up
```

2) Create a topic with 3 partitions and replication factor 3:

```bash
./scripts/create-topic.sh test-topic 3 3
# or
make create-topic topic=test-topic parts=3 repl=3
```

3) List topics:

```bash
./scripts/list-topics.sh
# or
make list-topics
```

4) Run a consumer (in one terminal):

```bash
make run-consumer
```

5) Run the producer (in another terminal):

```bash
make run-producer
```

The producer sends messages with keys `key-0/key-1/key-2` which will deterministically be assigned to partitions; the consumer prints partition and offset so you can observe distribution and consumer group behavior.

If you want monitoring or Schema Registry samples, tell me and I can add Prometheus/JMX exporter or Avro examples next. Enjoy learning Kafka! 🎯
