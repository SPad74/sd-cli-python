from domain.entities.plan import Plan
from domain.entities.user import User
from application.services.json_serializer_service import to_json
from application.services.json_deserializer_service import from_json
from ports.http_client import HttpClient
from datetime import date


def create_plan(name: str, creator: User, http_client: HttpClient, api_url_base: str) -> Plan:
    current_date = date.today().isoformat()
    new_plan = Plan(id=0, name=name, users=[creator], expenses=[], date=current_date)
    json_data = to_json(new_plan)

    # Enviar a backend por HTTP
    full_url = f"{api_url_base}/plans"
    response_json = http_client.post(full_url, json_data)

    return from_json(response_json, Plan)
