from Models.expense import Expense
from Models.category import Category
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main_menu():
    clear_screen()
    print("Expense Tracker CLI")
    print("===================")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Add Category")
    print("6. View Categories")
    print("7. Delete Category")
    print("8. Exit")

    choice = input("Enter your choice: ")
    return choice


def add_expense():
    description = input("Enter the expense description: ")
    amount = input("Enter the amount: ")
    category_id = input("Enter the category ID: ")
    try:
        Expense.create(description, float(amount), int(category_id))
        print("Expense added successfully.")
    except Exception as e:
        print(f"Error adding expense: {e}")

def view_expenses():
    try:
        expenses = Expense.get_all()
        if expenses:
            for exp in expenses:
                print(f"ID: {exp[0]}, Description: {exp[1]}, Amount: {exp[2]}, Category ID: {exp[3]}")
        else:
            print("No expenses found.")
    except Exception as e:
        print(f"Error fetching expenses: {e}")

def update_expense():
    expense_id = input("Enter the expense ID to update: ")
    description = input("Enter the new description: ")
    amount = input("Enter the new amount: ")
    category_id = input("Enter the new category ID: ")
    try:
        Expense.update(int(expense_id), description, float(amount), int(category_id))
        print("Expense updated successfully.")
    except Exception as e:
        print(f"Error updating expense: {e}")

def delete_expense():
    expense_id = input("Enter the expense ID to delete: ")
    try:
        Expense.delete(int(expense_id))
        print("Expense deleted successfully.")
    except Exception as e:
        print(f"Error deleting expense: {e}")

def add_category():
    name = input("Enter the category name: ")
    try:
        Category.create(name)
        print("Category added successfully.")
    except Exception as e:
        print(f"Error adding category: {e}")

def view_categories():
    try:
        categories = Category.get_all()
        if categories:
            for cat in categories:
                print(f"ID: {cat[0]}, Name: {cat[1]}")
        else:
            print("No categories found.")
    except Exception as e:
        print(f"Error fetching categories: {e}")

def delete_category():
    category_id = input("Enter the category ID to delete: ")
    try:
        Category.delete(int(category_id))
        print("Category deleted successfully.")
    except Exception as e:
        print(f"Error deleting category: {e}")
