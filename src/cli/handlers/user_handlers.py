from application.use_cases.create_user import create_user
from application.use_cases.login import login_user
from domain.entities.user import User

from cli.dependencies import get_http_client
from config import API_BASE_URL


def handle_create_user(user: User):
    return create_user(user, API_BASE_URL)


def handle_login(username: str, password: str):
    return login_user(username, password, API_BASE_URL)
