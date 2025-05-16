from cli.handlers.user_handlers import handle_create_user, handle_login
from cli.handlers.plan_handlers import handle_create_plan, handle_join_plan
from cli.handlers.expense_handlers import register_expense_handler

from domain.entities.user import User
from domain.entities.plan import Plan

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
            # if user is None:
            #     print("Debes iniciar sesión primero.")
            #     continue
            plan_name = input("Ingresa el nombre del plan: ").strip()
            plan = handle_create_plan(plan_name)
            print(f"Plan creado: {repr(plan)}")
        elif command == "join_plan":
            plan = handle_join_plan(plan.id, user)
            print(f"Te has unido al plan: {repr(plan)}")
        elif command == "register_expense":
            register_expense_handler()
        elif command in ("exit", "quit"):
            print("Saliendo de la aplicación...")
            break
        else:
            print(f"Comando desconocido: {command}")

if __name__ == "__main__":
    main()
