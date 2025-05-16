import threading
import time

from cli.handlers.user_handlers import handle_create_user, handle_login
from cli.handlers.plan_handlers import handle_create_plan, handle_join_plan
from cli.handlers.expense_handlers import register_expense_handler, handle_expense_notification
from application.use_cases.expense_notificator import ExpenseNotificatorService
from infrastructure.kafka_consumer import KafkaConsumerAdapter

from domain.entities.user import User
from domain.entities.plan import Plan
from domain.entities.expense import Expense

# Variables compartidas para guardar expenses recibidos
user_expenses = []
plan_expenses = []

def kafka_listener(expense_notificator: ExpenseNotificatorService, interval=2):
    while True:
        expense = handle_expense_notification(expense_notificator)
        if expense:
            print(f"\nNuevo gasto detectado vía Kafka: {repr(expense)}")
            user_expenses.append(expense)
            plan_expenses.append(expense)
        time.sleep(interval)

def main():
    user = User(username="jochua", password="admin")
    plan = Plan(id=1, name="Plan de prueba", date="2023-10-01T00:00:00")

    print("Bienvenido a la aplicación CLI.")
    print("Comandos disponibles: create_user | login | create_plan | join_plan | register_expense | exit")

    while True:
        command = input("Ingresa comando: ").strip()

        if command == "create_user":
            username = input("Ingresa el nombre de usuario: ").strip()
            password = input("Ingresa la contraseña: ").strip()
            user = handle_create_user(username=username, password=password)
            print(repr(user))
        elif command == "login":
            username = input("Ingresa el nombre de usuario: ").strip()
            password = input("Ingresa la contraseña: ").strip()
            user = handle_login(password=password, username=username)
            print(repr(user))
        elif command == "create_plan":
            if user is None:
                print("Debes iniciar sesión primero.")
                continue
            plan_name = input("Ingresa el nombre del plan: ").strip()
            plan = handle_create_plan(plan_name)
            print(f"Plan creado: {repr(plan)}")
        elif command == "join_plan":
            plan = handle_join_plan(plan.id, user)
            print(f"Te has unido al plan: {repr(plan)}")
        elif command == "register_expense":
            expense_name = input("Ingresa el nombre del gasto: ").strip()
            expense_amount = float(input("Ingresa el monto del gasto: ").strip())
            expense = Expense(id=0, name=expense_name, amount=expense_amount, date="2023-10-01T00:00:00", plan_id=plan.id)
            register_expense_handler(user=user, plan=plan, expense=expense)
        elif command in ("exit", "quit"):
            print("Saliendo de la aplicación...")
            break
        else:
            print(f"Comando desconocido: {command}")

if __name__ == "__main__":
    # Instancia el notificator
    expense_notificator = ExpenseNotificatorService(event_subscriber=KafkaConsumerAdapter())

    # Hilo que corre el main (CLI)
    main_thread = threading.Thread(target=main)

    # Hilo que escucha Kafka para nuevos expenses
    listener_thread = threading.Thread(target=kafka_listener, args=(expense_notificator,), daemon=True)

    listener_thread.start()
    main_thread.start()

    main_thread.join()
    # listener_thread es daemon, termina al acabar main_thread
