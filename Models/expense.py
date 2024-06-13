from orm.orm import ORM

class Expense:
    orm = ORM('expenses.db')

    def __init__(self, description, amount, category_id):
        self.description = description
        self.amount = amount
        self.category_id = category_id
