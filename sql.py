import sqlite3

def create_database():
    
    conn = sqlite3.connect('expenses.db')
    cursor = conn.cursor()

    
    create_expenses_table = """
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        amount REAL NOT NULL,
        category_id INTEGER NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """

    create_categories_table = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL UNIQUE
    )
    """

    
    cursor.execute(create_expenses_table)
    cursor.execute(create_categories_table)

    
    conn.commit()

    
    conn.close()

if __name__ == '__main__':
    create_database()
    print("Database 'expenses.db' created successfully.")
