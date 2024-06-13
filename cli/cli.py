import click
from Models.expense import Expense
from Models.category import Category
from orm.orm import ORM

ORM('expenses.db') 