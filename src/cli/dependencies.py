# cli/dependencies.py

from infrastructure.kafka_producer import KafkaProducerAdapter
from infrastructure.kafka_consumer import KafkaConsumerAdapter
from infrastructure.http_requests_client import RequestsHttpClient
from cli.config import API_BASE_URL, KAFKA_BROKER
from ports.event_publisher import EventPublisher
from ports.event_subscriber import EventSubscriber
from ports.http_client import HttpClient


def get_event_publisher() -> EventPublisher:
    return KafkaProducerAdapter(bootstrap_servers=KAFKA_BROKER)


def get_event_subscriber() -> EventSubscriber:
    return KafkaConsumerAdapter(bootstrap_servers=KAFKA_BROKER)


def get_http_client() -> HttpClient:
    return RequestsHttpClient()
