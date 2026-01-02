"""Simple Kafka producer using kafka-python
"""
import time
import json
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

topic = 'test-topic'

if __name__ == '__main__':
    for i in range(10):
        msg = {'count': i}
        producer.send(topic, msg)
        print(f"Sent: {msg}")
        time.sleep(1)
    producer.flush()
