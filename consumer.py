"""Kafka consumer demo: consumer groups and partition info
"""
import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    'test-topic',
    bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'],
    auto_offset_reset='earliest',
    group_id='demo-group',
    value_deserializer=lambda m: json.loads(m.decode('utf-8')),
)

if __name__ == '__main__':
    print("Consumer group: demo-group — listening for messages on 'test-topic'...\n")
    for msg in consumer:
        key = msg.key.decode('utf-8') if msg.key else None
        print(f"Received: partition={msg.partition} offset={msg.offset} key={key} value={msg.value}")
