from orm.orm import ORM

class Category:
    orm = ORM('expenses.db')

    def __init__(self, name):
        self.name = name