"""Kafka producer demo: keys, partitions, and metadata

Sends messages with keys so partitioning occurs deterministically.
"""
import time
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
    key_serializer=lambda k: k.encode('utf-8') if isinstance(k, str) else k,
)

topic = 'test-topic'

if __name__ == '__main__':
    for i in range(20):
        key = f"key-{i % 3}"
        msg = {'count': i}
        future = producer.send(topic, key=key, value=msg)
        try:
            meta = future.get(timeout=10)
            print(f"Sent: {msg} (key={key}) -> partition={meta.partition} offset={meta.offset}")
        except Exception as exc:
            print("Send failed:", exc)
        time.sleep(0.5)
    producer.flush()
