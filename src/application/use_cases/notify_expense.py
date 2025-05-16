from domain.entities.expense import Expense
from application.services.json_deserializer_service import from_json
from ports.event_subscriber import EventSubscriber

def notify_expense(event_subscriber: EventSubscriber) -> Expense:
    """
    Recibe la notificación de gasto registrado desde Kafka (u otro broker)
    y devuelve el objeto Expense correspondiente.

    :param event_subscriber: Implementación del subscriber de eventos
    :return: Objeto Expense deserializado
    """
    # Esperar a recibir el evento de gasto registrado
    json_data = event_subscriber.receive("expense_registered")
    
    # Deserializar el JSON recibido a Expense
    expense = from_json(json_data, Expense)
    return expense
