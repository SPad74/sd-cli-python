from domain.entities.expense import Expense
from domain.entities.user import User
from application.services.json_serializer_service import to_json
from ports.event_publisher import EventPublisher

def cover_full_expense(expense: Expense, user: User, event_publisher: EventPublisher):
    """
    Permite que un usuario cubra completamente un gasto compartido.

    :param expense: Gasto a cubrir
    :param user: Usuario que asume el gasto completo
    :param event_publisher: Publicador Kafka
    """
    payload = {
        "expense_id": expense.id,
        "user_nickname": user.username
    }

    # Publicar evento indicando que este usuario cubrirá todo el gasto
    json_payload = to_json(payload)
    event_publisher.publish("cover_full_expense", json_payload)

    # (Opcional) Actualizar localmente la lista del usuario, si aplica
    if expense not in user.expenses:
        user.expenses.append(expense)
