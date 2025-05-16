from application.services.json_serializer_service import to_json
from ports.event_publisher import EventPublisher


def send_request_for_acceptance(
    item_type: str,
    item_id: int,
    item: object,
    sender_nickname: str,
    receivers_nicknames: list[str],
    event_publisher: EventPublisher
):
    """
    Envía una única solicitud de aceptación a varios usuarios.

    :param item_type: Tipo del ítem ('debt', 'expense', etc.)
    :param item_id: ID del ítem
    :param sender_nickname: Nickname del usuario que solicita la aceptación
    :param receivers_nicknames: Lista de nicknames de usuarios que deben aceptar
    :param event_publisher: Publicador Kafka
    """
    payload = {
        "item_type": item_type,
        "item": item,
        "sender_nickname": sender_nickname,
        "receiver_nicknames": receivers_nicknames
    }

    json_data = to_json(payload)
    event_publisher.publish("send_request_for_acceptance", json_data)
