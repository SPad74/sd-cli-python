import requests
from domain.entities.user import User
from application.services.json_serializer_service import to_json
from application.services.json_deserializer_service import from_json


def create_user(user: User, url_base: str) -> User:
    """
    Envía una solicitud al backend tradicional para crear un nuevo usuario.

    :param user: Objeto User a crear
    :param url_base: URL base del backend tradicional (ej. http://localhost:8080)
    :return: Usuario creado con posibles datos actualizados (como ID)
    """
    json_data = to_json(user)
    response = requests.post(f"{url_base}/users/create", data=json_data)
    response.raise_for_status()  # Lanza excepción si hay error

    created_user = from_json(response.text, User)
    return created_user
