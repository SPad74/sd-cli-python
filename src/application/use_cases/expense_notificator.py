from application.services.json_deserializer_service import from_json
from domain.entities.expense import Expense

class ExpenseNotificatorService:
    def __init__(self, event_subscriber):
        self.event_subscriber = event_subscriber
        self.event_subscriber.consumer.subscribe(["expense_notification"])

    def listen_for_expense(self, timeout_ms=1000) -> Expense | None:
        """
        Escucha el tópico expense_notification con timeout.
        Retorna Expense si llega un mensaje, o None si no.
        """
        records = self.event_subscriber.consumer.poll(timeout_ms=timeout_ms)
        for tp, messages in records.items():
            for msg in messages:
                expense = from_json(msg.value, Expense)
                return expense
        return None
