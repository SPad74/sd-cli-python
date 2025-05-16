from application.services.json_serializer_service import to_json
from ports.event_publisher import EventPublisher


def record_loan(loan_id: int, accepted: bool, event_publisher: EventPublisher) -> None:
    """
    Prestamista responde si acepta o rechaza el préstamo.

    :param loan_id: ID del préstamo o deuda a responder
    :param accepted: True si acepta, False si rechaza
    :param event_publisher: Publicador Kafka
    """
    payload = {
        "loan_id": loan_id,
        "accepted": accepted
    }
    json_payload = to_json(payload)
    event_publisher.publish("loan_decision", json_payload)
