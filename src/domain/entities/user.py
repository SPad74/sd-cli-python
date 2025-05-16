from domain.entities.expense import Expense
from domain.entities.debt import Debt

class User:
    def __init__(self, username: str, password: str, expenses: list[Expense] = None, debts: list[Debt] = None, loans: list[Debt] = None):
        self.username = username
        self.password = password
        self.expenses = expenses if expenses is not None else []
        self.debts = debts if debts is not None else []
        self.loans = loans if loans is not None else []

    def add_expense(self, expense: Expense):
        self.expenses.append(expense)

    def add_debt(self, debt: Debt):
        self.debts.append(debt)
    
    def add_loan(self, loan: Debt):
        self.loans.append(loan)
    
    def remove_debt(self, debt: Debt):
        if debt in self.debts:
            self.debts.remove(debt)
        else:
            raise ValueError("Debt not found in user's debts")
    
    def remove_loan(self, loan: Debt):
        if loan in self.loans:
            self.loans.remove(loan)
        else:
            raise ValueError("Loan not found in user's loans")
    
    def __repr__(self):
       return f"User(username={self.username}, password={self.password}, expenses={self.expenses}, debts={self.debts}, loans={self.loans})"