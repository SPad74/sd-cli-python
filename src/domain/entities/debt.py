from domain.entities.expense import Expense

class Debt:
    def __init__(self, id: int, expense: Expense, lender: str, borrower: str):
        self.id = id
        self.expense = expense
        self.lender = lender
        self.borrower = borrower

    
    def __repr__(self):
        return f"Debt(id={self.id}, expense={self.expense}, lender={self.lender}, borrower={self.borrower})"