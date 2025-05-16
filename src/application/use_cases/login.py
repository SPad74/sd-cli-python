import requests
from domain.entities.user import User
from application.services.json_deserializer_service import from_json

def login_user(username: str, password: str, api_url_base: str) -> User:
    """
    Intenta iniciar sesión con el backend tradicional.

    :param username: Nombre de usuario
    :param password: Contraseña
    :param api_url_base: URL base del backend, sin barra al final (ejemplo: http://localhost:8080/api)
    :return: Objeto User si es exitoso
    :raises: Exception si la autenticación falla
    """
    full_url = f"{api_url_base}/login"
    payload = {
        "username": username,
        "password": password
    }

    response = requests.post(full_url, json=payload)

    if response.status_code == 200:
        return from_json(response.text, User)
    else:
        raise Exception(f"Login failed: {response.status_code} - {response.text}")
