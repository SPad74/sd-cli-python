from kafka import KafkaConsumer
from ports.event_subscriber import EventSubscriber
import os
from dotenv import load_dotenv

class KafkaConsumerAdapter(EventSubscriber):
    def __init__(self, bootstrap_servers=os.getenv("KAFKA_BROKER"), group_id='default-group'):
        self.consumer = KafkaConsumer(
            bootstrap_servers=bootstrap_servers,
            group_id=group_id,
            auto_offset_reset='earliest',
            enable_auto_commit=True,
            value_deserializer=lambda m: m.decode('utf-8')
        )
    
    def receive(self, topic: str) -> str:
        self.consumer.subscribe([topic])
        # Bloqueo esperando el primer mensaje del tópico
        for msg in self.consumer:
            # Retornamos el primer mensaje recibido
            return msg.value
