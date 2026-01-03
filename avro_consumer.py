"""Simple Avro consumer using AvroConsumer (confluent-kafka[avro])"""
from confluent_kafka.avro import AvroConsumer

SCHEMA_REGISTRY_URL = 'http://localhost:8081'
BROKER = 'localhost:9092'
TOPIC = 'users'

if __name__ == '__main__':
    c = AvroConsumer({'bootstrap.servers': BROKER, 'group.id': 'avro-consumer-group', 'schema.registry.url': SCHEMA_REGISTRY_URL, 'auto.offset.reset': 'earliest'})
    c.subscribe([TOPIC])

    print('Listening for Avro messages on topic', TOPIC)
    try:
        while True:
            msg = c.poll(1.0)
            if msg is None:
                continue
            if msg.error():
                print('Error:', msg.error())
                continue
            print('Received:', msg.value())
    except KeyboardInterrupt:
        pass
    finally:
        c.close()
