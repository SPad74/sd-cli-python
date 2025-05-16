from domain.entities.debt import Debt
from application.services.json_serializer_service import to_json
from ports.event_publisher import EventPublisher


def register_debt(debt: Debt, event_publisher: EventPublisher) -> None:
    """
    Envía la deuda al backend para iniciar proceso de aceptación por parte del prestamista.
    No espera respuesta directa, backend notificará luego.

    :param debt: Deuda sin confirmar (sin ID)
    :param event_publisher: Publicador Kafka
    """
    payload = {"debt": debt.to_dict()}
    json_payload = to_json(payload)
    event_publisher.publish("register_debt", json_payload)
