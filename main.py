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
