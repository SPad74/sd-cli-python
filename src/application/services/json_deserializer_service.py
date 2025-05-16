import json
from domain.entities.user import User
from domain.entities.expense import Expense
from domain.entities.debt import Debt
from domain.entities.plan import Plan

def from_json(json_str: str, cls):
    print(f"Deserializando JSON: {json_str}")
    data = json.loads(json_str)
    return from_dict(data, cls)

def from_dict(data: dict, cls):
    if cls == User:
        return User(
            username=data["username"],
            password=data["password"],
            expenses=[from_dict(exp, Expense) for exp in data.get("expenses", [])],
            debts=[from_dict(debt, Debt) for debt in data.get("debts", [])],
            loans=[from_dict(loan, Debt) for loan in data.get("loans", [])]
        )

    elif cls == Expense:
        return Expense(
            id=data["expenseId"],
            name=data["name"],
            amount=data["amount"],
            date=data["date"],
            type=data["type"],
            plan_id=data["plan"],
        )

    elif cls == Debt:
        return Debt(
            id=data["id"],
            amount=data["amount"],
            expense=from_dict(data["expense"], Expense),
            user_nickname=data["user_nickname"]
        )

    elif cls == Plan:
        return Plan(
            id=data["planId"],
            name=data["name"],
            participants=[from_dict(user, User) for user in data.get("users", [])],
            expenses=[from_dict(exp, Expense) for exp in data.get("expenses", [])],
            date=data["date"]
        )
    
    elif cls == dict:
        return data

    else:
        raise ValueError(f"No deserialization logic for class: {cls}")
