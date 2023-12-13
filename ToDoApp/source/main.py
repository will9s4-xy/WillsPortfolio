import sqlite3
import os
def create_tasks_table():
    # Connect to the database
    conn = sqlite3.connect('todo.db')
    
    # Create a cursor
    db_cursor = conn.cursor()
    
    # SQL statement to create the tasks table
    create_table_sql = '''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task TEXT NOT NULL,
            done BOOLEAN NOT NULL DEFAULT FALSE
        )
    '''
    
    # Execute the SQL statement
    db_cursor.execute(create_table_sql)
    
    # Commit the changes
    conn.commit()
    
    # Close the connection
    conn.close()

# Call the method to create the tasks table
if not os.path.exists('todo.db'):
    create_tasks_table()


