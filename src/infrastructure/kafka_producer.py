from kafka import KafkaProducer
from ports.event_publisher import EventPublisher
import os
from dotenv import load_dotenv

class KafkaProducerAdapter(EventPublisher):
    def __init__(self, bootstrap_servers=os.getenv("KAFKA_BROKER")):
        self.producer = KafkaProducer(
            bootstrap_servers=bootstrap_servers,
            value_serializer=lambda v: v.encode('utf-8')
        )
    
    def publish(self, topic: str, message: str) -> None:
        # Enviar mensaje (async), pero puede hacer flush para asegurar envío inmediato
        self.producer.send(topic, message)
        self.producer.flush()
