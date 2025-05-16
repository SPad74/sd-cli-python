import requests
from domain.entities.user import User
from domain.entities.plan import Plan
from application.services.json_serializer_service import to_json
from application.services.json_deserializer_service import from_json
from ports.event_publisher import EventPublisher


def join_plan(plan_id: int, user: User, event_publisher: EventPublisher, url_base: str) -> Plan:
    """
    Publica un evento para unir al usuario a un plan y recupera el plan actualizado desde el backend tradicional.

    :param plan_id: ID del plan al que se unirá el usuario
    :param user: Usuario a unirse
    :param event_publisher: Publicador Kafka
    :param url_base: URL base del backend tradicional (por ejemplo, http://localhost:8080)
    :return: Plan actualizado
    """
    # Publicar evento al backend Kafka
    print(f"Publicando evento para unirse al plan {plan_id} para el usuario {user}")
    payload = {
        "planId": plan_id,
        "username": user.username
    }
    json_data = to_json(payload)
    event_publisher.publish("join_plan", json_data)

    # Obtener plan actualizado desde el backend tradicional (REST)
    response = requests.get(f"{url_base}/plans/{plan_id}")
    response.raise_for_status()  # Lanza excepción si el status no es 2xx
    try:
        updated_plan = from_json(response.text, Plan)
    except Exception as e:
        print(f"Error al deserializar el plan: {e}")
        return Plan(
            id=plan_id,
            name="error",
            participants=[user],
            expenses=[],
            date=""
        )
    return updated_plan
