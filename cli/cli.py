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
def add_expense(description, amount, category_id):
    """Add a new expense."""
    try:
        Expense.create(description, amount, category_id)
        click.echo(f'Expense "{description}" with amount {amount} added.')
    except Exception as e:
        click.echo(f'Error adding expense: {e}')

@cli.command()
def view_expenses():
    """View all expenses."""
    try:
        expenses = Expense.get_all()
        for expense in expenses:
            click.echo(f'ID: {expense[0]}, Description: {expense[1]}, Amount: {expense[2]}, Category ID: {expense[3]}')
    except Exception as e:
         click.echo(f'Error fetching expenses: {e}')

@cli.command()
@click.argument('expense_id', type=int)
@click.argument('description')
@click.argument('amount', type=float)
@click.argument('category_id', type=int)
def update_expense(expense_id, description, amount, category_id):
    """Update an expense."""
    try:
        Expense.update(expense_id, description, amount, category_id)
        click.echo(f'Expense with ID {expense_id} updated.')
    except Exception as e:
        click.echo(f'Error updating expense: {e}')
