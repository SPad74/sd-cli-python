from domain.entities.expense import Expense
from domain.entities.user import User
from domain.entities.plan import Plan
from application.services.json_serializer_service import to_json
from application.services.json_deserializer_service import from_json
from ports.event_publisher import EventPublisher
from ports.event_subscriber import EventSubscriber


def register_expense(
    plan: Plan,
    user: User,
    expense: Expense,
    event_publisher: EventPublisher,
    event_subscriber: EventSubscriber
) -> Expense:
    """
    Registra un gasto en un plan y lo asigna al usuario que lo realizó.

    :param plan: Plan al que pertenece el gasto
    :param user: Usuario que realiza el gasto
    :param expense: Objeto de tipo Expense (sin ID)
    :param event_publisher: Publicador Kafka
    :param event_subscriber: Suscriptor Kafka
    :return: Gasto con ID asignado
    """

    # Crear payload con IDs y gasto serializado
    payload = {
        "plan_id": plan.id,
        "user_nickname": user.username,
        "expense": expense.to_dict()
    }

    plan.add_expense(expense)

    # Publicar mensaje a Kafka
    json_payload = to_json(payload)
    event_publisher.publish("register_expense", json_payload)

    # Esperar respuesta del backend
    response_json = event_subscriber.receive("expense_registered")

    # Deserializar gasto con ID generado
    registered_expense = from_json(response_json, Expense)

    # Asociar el gasto al usuario y al plan
    user.expenses.append(registered_expense)
    plan.expenses.append(registered_expense)

    return registered_expense
