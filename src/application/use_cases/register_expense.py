from domain.entities.expense import Expense
from domain.entities.user import User
from domain.entities.plan import Plan
from application.services.json_serializer_service import to_json
from application.services.json_deserializer_service import from_json
from ports.event_publisher import EventPublisher


def register_expense(
    plan: Plan,
    user: User,
    expense: Expense,
    event_publisher: EventPublisher,
) -> None:
    """
    Registra un gasto en un plan enviando la solicitud al backend, sin esperar respuesta.

    :param plan: Plan al que pertenece el gasto
    :param user: Usuario que realiza el gasto
    :param expense: Objeto Expense (sin ID)
    :param event_publisher: Publicador Kafka
    """

    payload = {
        "planId": plan.id,
        "username": user.username,
        "expense": expense.to_dict(),
    }

    json_payload = to_json(payload)
    event_publisher.publish("register_expense", json_payload)
