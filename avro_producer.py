"""Simple Avro producer that uses Schema Registry to register schema and send Avro-encoded messages.
Requires: confluent-kafka[avro], fastavro
"""
from confluent_kafka import avro
from confluent_kafka.avro import AvroProducer

SCHEMA_REGISTRY_URL = 'http://localhost:8081'
BROKER = 'localhost:9092'
TOPIC = 'users'

value_schema = avro.load('schemas/user_v1.avsc')

def delivery_report(err, msg):
    if err:
        print('Delivery failed:', err)
    else:
        print('Delivered message to {} [{}]'.format(msg.topic(), msg.partition()))

if __name__ == '__main__':
    producer = AvroProducer({'bootstrap.servers': BROKER, 'schema.registry.url': SCHEMA_REGISTRY_URL}, default_value_schema=value_schema)

    for i in range(5):
        user = {"name": f"user_{i}", "age": 20 + i}
        producer.produce(topic=TOPIC, value=user, callback=delivery_report)
    producer.flush()
