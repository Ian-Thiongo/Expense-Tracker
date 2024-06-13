# Project Name Expense Tracker
# Author: Ian Thiong'o

## Expense Tracker
  # Overview
  Expense Tracker is a command-line application designed to help users manage their personal expenses. With features for adding, viewing, updating, and deleting expenses and categories, this tool provides a straightforward way to track spending and manage finances.


# Project Structure
  ```plaintext
  Expense-Tracker/
│
├── expense_tracker/
│   ├── cli/
│   │   └── cli.py            # CLI logic
│   ├── models/
│   │   ├── category.py       # Category model
│   │   └── expense.py        # Expense model
│   └── orm/
│       ├── database.py       # Database initialization
│       └── orm.py            # ORM class for database interaction
│
├── sql.py                    # SQL script for initializing the database
├── main.py                   # Main entry point for the CLI
├── Pipfile                   # Pipenv configuration file
└── README.md                 # Project documentation
```

# Features
- **Add Expense**: Allows users to add new expenses with a description, amount, and category.
- **View Expenses**: Displays a list of all expenses.
- **Update Expense**: Enables users to update existing expenses.
- **Delete Expense**: Allows for the deletion of expenses.
- **Add Category**: Users can add new categories for expenses.
- **View Categories**: Displays all available categories.
- **Delete Category**: Allows users to delete categories.
- **Persistent Data Storage**: Uses SQLite for data storage.

## Installation
Follow these steps to install and run the Expense Tracker application on your local machine.

### Prerequisites
- Python 3.8 installed on your system.
- Pipenv for managing dependencies.

### Steps
1. **Clone the Repository**:
    ```bash
    git clone https://github.com/lilThiosh/Expense-Tracker.git
    cd Expense-Tracker
    ```

2. **Set Up Virtual Environment**:
    Ensure `pipenv` is installed. If not, install it using:
    ```bash
    pip install pipenv
    ```

3. **Install Dependencies**:
    Use Pipenv to install all necessary packages:
    ```bash
    pipenv install
    ```

4. **Activate the Virtual Environment**:
    ```bash
    pipenv shell
    ```

5. **Initialize the Database**:
    Run the SQL script to create the required tables in the database:
    ```bash
    python sql.py
    ```

6. **Run the Application**:
    Launch the CLI application:
    ```bash
    python main.py
    ```

## Usage
After installing the application, you can run the CLI and interact with it as follows:

```plaintext
Expense Tracker CLI
===================
1. Add Expense
2. View Expenses
3. Update Expense
4. Delete Expense
5. Add Category
6. View Categories
7. Delete Category
8. Exit
```

## Contributions
Contributions to the Expense Tracker project are welcome. Please follow these steps:

1. Fork the repository.
2. Create a new feature branch (git checkout -b    feature/YourFeature).
4. Commit your changes with descriptive messages.
5. Push to your branch (git push origin feature/YourFeature).
6. Open a pull request.

## License
- ©2024 Expense Tracker.This project is licensed under the MIT License.
 
 # contact
- For any questions or feedback, please contact me at: Thiongoian6148@gmail.com
