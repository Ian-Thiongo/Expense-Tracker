import click
from Models.expense import Expense
from Models.category import Category
from orm.orm import ORM

ORM('expenses.db') 

@click.group()
def cli():
    """CLI for managing expenses."""
    pass

@cli.command()
@click.argument('description')
@click.argument('amount', type=float)
@click.argument('category_id', type=int)