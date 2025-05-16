from domain.entities.user import User
from domain.entities.expense import Expense

class Plan:
    def __init__(self, id: int, name: str, participants: list[User], expenses: list[Expense], date: str):
        self.id = id
        self.name = name
        self.date = date
        self.participants = participants if participants is not None else []
        self.expenses = expenses if expenses is not None else []

    def setId(self, id: int):
        self.id = id

    def add_participant(self, user: User):
        if user not in self.participants:
            self.participants.append(user)
        else:
            raise ValueError("User already in participants list")
        
    def remove_participant(self, user: User):
        if user in self.participants:
            self.participants.remove(user)
        else:
            raise ValueError("User not found in participants list")
        
    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def __repr__(self):
        return f"Plan(id={self.id}, name={self.name}, date={self.date}, participants={self.participants}, expenses={self.expenses})"