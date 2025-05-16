from application.use_cases.create_user import create_user
from application.use_cases.login import login_user
from domain.entities.user import User

from cli.config import API_BASE_URL


def handle_create_user(username: str, password: str):
    return create_user(username, password, API_BASE_URL)


def handle_login(username: str, password: str):
    return login_user(username, password, API_BASE_URL)
