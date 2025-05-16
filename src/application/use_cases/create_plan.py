from domain.entities.plan import Plan
from application.services.json_serializer_service import to_json
from application.services.json_deserializer_service import from_json
from ports.http_client import HttpClient
import datetime
import requests


def create_plan(name: str, api_url_base: str) -> Plan:
    # current_date = datetime.now().replace(microsecond=0).isoformat()
    json_data = to_json(dict({
        "name": name,
        "date": "2023-10-01T00:00:00",
    }))

    # Enviar a backend por HTTP
    response = requests.post(
        f"{api_url_base}/plans/create",
        data=json_data,
        headers={"Content-Type": "application/json"}
    )

    response.raise_for_status()  # Lanza excepción si hay error

    return from_json(response.text, Plan)
