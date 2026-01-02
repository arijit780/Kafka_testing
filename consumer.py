"""Simple Kafka consumer using kafka-python
"""
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
    enable_auto_commit=True,
    consumer_timeout_ms=10000
)

if __name__ == '__main__':
    print("Listening for messages on 'test-topic' (will timeout after a short period)...")
    for msg in consumer:
        print("Received:", msg.value)
