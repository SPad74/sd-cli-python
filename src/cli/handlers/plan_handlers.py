from application.use_cases.create_plan import create_plan
from application.use_cases.join_plan import join_plan
from domain.entities.user import User
from domain.entities.plan import Plan
from cli.config import API_BASE_URL
from cli.dependencies import get_event_publisher, get_event_subscriber
from cli.config import API_BASE_URL


def handle_create_plan(name: str):
    return create_plan(name, API_BASE_URL)

def handle_join_plan(plan_id: int, user: User):
    # join_plan hace llamada al back tradicional para obtener el plan actualizado
    return join_plan(plan_id, user, get_event_publisher(), API_BASE_URL)
