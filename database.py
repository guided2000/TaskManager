import sqlite3

def initialize_database(db_name="tasks.db"):
    """
    Initializes the database and creates the tasks table if it doesn't exist.

    Args:
        db_name (str): The name of the SQLite database file.

    Returns:
        None
    """
    # Connect to the database
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    # Create the tasks table (if it doesn't exist)
    create_tasks_table_query = """
    CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        due_date TEXT,
        priority TEXT,
        status TEXT DEFAULT 'Pending',  -- Pending, Completed
        category TEXT,
        created_at TEXT DEFAULT CURRENT_TIMESTAMP
    );
    """
    cursor.execute(create_tasks_table_query)

    # Commit changes and close connection
    connection.commit()
    connection.close()
    print(f"Database '{db_name}' initialized successfully with 'tasks' table.")

def add_task(db_name, title, description=None, due_date=None, priority=None, status='Pending', category=None):
    """
    Adds a new task to the tasks table.

    Args:
        db_name (str): The name of the SQLite database file.
        title (str): The title of the task.
        description (str, optional): A detailed description of the task.
        due_date (str, optional): The due date for the task.
        priority (str, optional): The priority of the task (e.g., High, Medium, Low).
        status (str, optional): The status of the task (default is 'Pending').
        category (str, optional): The category of the task.

    Returns:
        None
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    insert_query = """
    INSERT INTO tasks (title, description, due_date, priority, status, category)
    VALUES (?, ?, ?, ?, ?, ?);
    """
    cursor.execute(insert_query, (title, description, due_date, priority, status, category))

    connection.commit()
    connection.close()
    print(f"Task '{title}' added successfully.")

def get_tasks(db_name, status=None):
    """
    Retrieves tasks from the database, optionally filtered by status.

    Args:
        db_name (str): The name of the SQLite database file.
        status (str, optional): The status to filter tasks by (e.g., 'Pending', 'Completed').

    Returns:
        list: A list of tasks.
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    if status:
        select_query = "SELECT * FROM tasks WHERE status = ?;"
        cursor.execute(select_query, (status,))
    else:
        select_query = "SELECT * FROM tasks;"
        cursor.execute(select_query)

    tasks = cursor.fetchall()
    connection.close()
    return tasks

def update_task_status(db_name, task_id, new_status):
    """
    Updates the status of a task.

    Args:
        db_name (str): The name of the SQLite database file.
        task_id (int): The ID of the task to update.
        new_status (str): The new status (e.g., 'Completed').

    Returns:
        None
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    update_query = """
    UPDATE tasks
    SET status = ?
    WHERE id = ?;
    """
    cursor.execute(update_query, (new_status, task_id))

    connection.commit()
    connection.close()
    print(f"Task ID {task_id} updated to status '{new_status}'.")

def delete_task(db_name, task_id):
    """
    Deletes a task from the database.

    Args:
        db_name (str): The name of the SQLite database file.
        task_id (int): The ID of the task to delete.

    Returns:
        None
    """
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()

    delete_query = "DELETE FROM tasks WHERE id = ?;"
    cursor.execute(delete_query, (task_id,))

    connection.commit()
    connection.close()
    print(f"Task ID {task_id} deleted successfully.")

if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Example usage
    add_task("tasks.db", title="Finish project", description="Complete the final project report.", due_date="2024-12-31", priority="High", category="Work")
    tasks = get_tasks("tasks.db")
    print("All Tasks:", tasks)

    update_task_status("tasks.db", task_id=1, new_status="Completed")
    delete_task("tasks.db", task_id=1)