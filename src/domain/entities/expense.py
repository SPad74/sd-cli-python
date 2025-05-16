class Expense:
    def __init__(self, id: int, name: str, amount: float, date: str, plan_id: int, type: str = "shared"):
        self.id = id
        self.name = name
        self.amount = amount
        self.date = date
        self.plan_id = plan_id
        self.type = type

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "amount": self.amount,
            "date": self.date,
            "plan_id": self.plan_id,
            "type": self.type
        }

    def __repr__(self):
        return f"Expense(id={self.id}, name={self.name}, amount={self.amount}, date={self.date}, plan_id={self.plan_id}, type={self.type})"