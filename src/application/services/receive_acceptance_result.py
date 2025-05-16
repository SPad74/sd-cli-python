from application.services.json_deserializer_service import from_json
from ports.event_subscriber import EventSubscriber


def receive_acceptance_result(event_subscriber: EventSubscriber):
    """
    Escucha mensajes Kafka con el resultado de aceptación de un objeto previamente enviado.

    :param event_subscriber: Suscriptor Kafka que escucha el tópico 'acceptance_result'
    :return: Diccionario con:
             - item_type: Tipo del objeto evaluado
             - accepted: True si se aceptó, False si se rechazó
             - item: Objeto en formato dict (deserializable posteriormente)
    """
    json_data = event_subscriber.receive("acceptance_result")

    payload = from_json(json_data, dict)

    return {
        "item_type": payload["item_type"],
        "accepted": payload["accepted"],
        "item": payload["item"]
    }
