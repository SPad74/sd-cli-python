from kafka import KafkaConsumer
import json
from domain.entities.expense import Expense
from datetime import datetime


class ExpenseNotificatorService:
    def __init__(self, kafka_bootstrap_servers):
        self.kafka_bootstrap_servers = kafka_bootstrap_servers
        self.consumer = None

    def _init_consumer(self, planId: int):
        topic = f"expense_notifications_{planId}"
        if self.consumer:
            try:
                self.consumer.unsubscribe()
            except Exception:
                pass
            self.consumer.close()
            self.consumer = None
        self.consumer = KafkaConsumer(
            topic,
            bootstrap_servers=self.kafka_bootstrap_servers,
            auto_offset_reset="earliest",
            enable_auto_commit=True,
            group_id=f"python-expense-client-{planId}",
            value_deserializer=self.json_deserializer,
            consumer_timeout_ms=1000,
        )

    @staticmethod
    def json_deserializer(data):
        if data is None:
            return None
        try:
            return json.loads(data.decode("utf-8"))
        except Exception as e:
            print(f"Error deserializing message: {e}")
            print(f"Raw data: {data}")
            return {}

    def listen_for_expense(self, planId: int) -> Expense | None:
        """
        Escucha el tópico expense_notifications_{planId} con timeout.
        Retorna una instancia de Expense si llega un mensaje, o None si no.
        """
        if self.consumer is None:
            self._init_consumer(planId)

        try:
            for message in self.consumer:
                data = message.value
                # Aquí construimos Expense desde dict según domain.entities.expense. 
                # Se asume que Expense tiene un constructor compatible o un método from_dict
                # Si no, debes adaptar esta línea a tu constructor real.
                expense = Expense(
                    id=data.get("expenseId", 0),
                    name=data.get("expenseName", ""),
                    amount=data.get("amount", 0.0),
                    date=data.get("date", datetime.now().strftime("%Y-%m-%dT%H:%M:%S")),
                    plan_id=data.get("planId", None)
                )
                return expense
        except Exception as e:
            print(f"Error al escuchar mensajes Kafka: {e}")

        return None
