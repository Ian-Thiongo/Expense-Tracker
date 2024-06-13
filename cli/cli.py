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

@cli.command()
@click.argument('expense_id', type=int)
def delete_expense(expense_id):
    """Delete an expense."""
    try:
        Expense.delete(expense_id)
        click.echo(f'Expense with ID {expense_id} deleted.')
    except Exception as e:
        click.echo(f'Error deleting expense: {e}')

@cli.command()
def clear_expenses():
    """Clear all expenses."""
    try:
        Expense.clear()
        click.echo('All expenses cleared.')
    except Exception as e:
          click.echo(f'Error clearing expenses: {e}')


@cli.command()
@click.argument('name')
def add_category(name):
    """Add a new category."""
    try:
        Category.create(name)
        click.echo(f'Category "{name}" added.')
    except Exception as e:
        click.echo(f'Error adding category: {e}')

@cli.command()
def view_categories():
    """View all categories."""
    try:
        categories = Category.get_all()
        for category in categories:
            click.echo(f'ID: {category[0]}, Name: {category[1]}')
    except Exception as e:
        click.echo(f'Error fetching categories: {e}')

@cli.command()
@click.argument('category_id', type=int)
def delete_category(category_id):
    """Delete a category."""
    try:
        Category.delete(category_id)
        click.echo(f'Category with ID {category_id} deleted.')
    except Exception as e:
        click.echo(f'Error deleting category: {e}')
