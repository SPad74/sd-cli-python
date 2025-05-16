import threading
import time

from cli.handlers.user_handlers import handle_create_user, handle_login
from cli.handlers.plan_handlers import handle_create_plan, handle_join_plan
from cli.handlers.expense_handlers import register_expense_handler, handle_expense_notification
from application.use_cases.expense_notificator import ExpenseNotificatorService

from domain.entities.user import User
from domain.entities.plan import Plan
from domain.entities.expense import Expense

# Variables compartidas para guardar expenses recibidos
user = User(username="jochua", password="admin")
plan = Plan(id=1, name="Plan de prueba", date="2023-10-01T00:00:00")
idPlan = 1

def kafka_listener(expense_notificator: ExpenseNotificatorService, planId: int, user: User, plan: Plan, interval=0.01):
    """
    Loop que escucha mensajes Kafka y maneja gastos nuevos.
    user y plan son objetos a actualizar con los nuevos gastos recibidos.
    """
    while True:
        try:
            expense = handle_expense_notification(expense_notificator, planId)
            if expense:
                print(f"\nNuevo gasto detectado: {repr(expense)}")
                user.expenses.append(expense)
                plan.expenses.append(expense)
                print(f"Lista de gastos del usuario: {user.expenses}")
            time.sleep(interval)
        except Exception as e:
            print(f"Error en kafka_listener: {e}")
            time.sleep(interval)

def main():
    global idPlan
    global user
    global plan

    print("Bienvenido a la aplicación CLI.")

    while True:
        print("Comandos disponibles: create_user | login | create_plan | join_plan | register_expense | exit")
        command = input("Ingresa comando: ").strip()

        if command == "create_user":
            username = input("Ingresa el nombre de usuario: ").strip()
            password = input("Ingresa la contraseña: ").strip()
            user = handle_create_user(username=username, password=password)
            print(repr(user))
        # elif command == "login":
        #     username = input("Ingresa el nombre de usuario: ").strip()
        #     password = input("Ingresa la contraseña: ").strip()
        #     user = handle_login(password=password, username=username)
        #     print(repr(user))
        elif command == "create_plan":
            if user is None:
                print("Debes iniciar sesión primero.")
                continue
            plan_name = input("Ingresa el nombre del plan: ").strip()
            plan = handle_create_plan(plan_name)
            idPlan = plan.id
            print(f"Plan creado: {repr(plan)}")
        elif command == "join_plan":
            plan_id = int(input("Ingresa el ID del plan al que deseas unirte: ").strip())
            plan = handle_join_plan(plan_id, user)
            idPlan = plan.id
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
    # Configura tus brokers Kafka aquí
    bootstrap_servers = ["10.24.160.135:9092"]

    # Instancia el notificator con la lista de brokers
    expense_notificator = ExpenseNotificatorService(kafka_bootstrap_servers=bootstrap_servers)

    # Hilos para CLI y escucha de Kafka
    main_thread = threading.Thread(target=main)
    listener_thread = threading.Thread(target=kafka_listener, args=(expense_notificator, idPlan, user, plan), daemon=True)

    listener_thread.start()
    main_thread.start()

    main_thread.join()
    # listener_thread es daemon, termina al acabar main_thread
