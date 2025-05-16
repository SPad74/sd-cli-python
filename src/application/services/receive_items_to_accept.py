from application.services.json_deserializer_service import from_json
from ports.event_subscriber import EventSubscriber


def receive_items_to_accept(event_subscriber: EventSubscriber):
    """
    Escucha mensajes Kafka con solicitudes de aceptación de objetos.

    :param event_subscriber: Suscriptor Kafka que escucha el tópico 'request_acceptance'
    :return: Diccionario con:
             - sender_username: Usuario que envía la solicitud
             - item_type: Tipo del objeto
             - item: Objeto deserializado
    """
    json_data = event_subscriber.receive("request_acceptance")

    payload = from_json(json_data, dict)

    item_type = payload["item_type"]
    sender_username = payload["sender_username"]
    item_data = payload["item"]

    return {
        "sender_username": sender_username,
        "item_type": item_type,
        "item": item_data  # se puede deserializar después según el tipo
    }
