from application.use_cases.register_expense import register_expense
from application.use_cases.expense_notificator import ExpenseNotificatorService
from domain.entities.plan import Plan
from domain.entities.user import User
from domain.entities.expense import Expense
from cli.dependencies import get_event_publisher, get_event_subscriber

def register_expense_handler(plan: Plan, user: User, expense: Expense):
    publisher = get_event_publisher()
    subscriber = get_event_subscriber()
    register_expense(plan, user, expense, publisher, subscriber)

def handle_expense_notification(expense_notificator: ExpenseNotificatorService) -> Expense | None:
    """
    Llama al notificator para recibir 1 mensaje de gasto.
    Retorna el gasto o None si no hay.
    """
    return expense_notificator.listen_for_expense()