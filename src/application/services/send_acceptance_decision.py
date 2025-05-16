from application.services.json_serializer_service import to_json
from ports.event_publisher import EventPublisher


def send_acceptance_decision(item_type: str, item_id: int, user_nickname: str, accepted: bool, event_publisher: EventPublisher):
    """
    Enviar al backend la decisión del usuario sobre aceptar o rechazar un ítem.

    :param item_type: Tipo del ítem ('expense', 'debt', etc.)
    :param item_id: ID del ítem
    :param user_nickname: Usuario que responde
    :param accepted: True si acepta, False si rechaza
    :param event_publisher: Publicador Kafka
    """
    payload = {
        "item_type": item_type,
        "item_id": item_id,
        "user_nickname": user_nickname,
        "accepted": accepted
    }

    event_publisher.publish("send_acceptance_decision", to_json(payload))
