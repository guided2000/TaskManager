import sqlite3

def create_database(db_name="database.db"):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()

        # Create users table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age INTEGER,
                email TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                phone_number TEXT,
                post TEXT
            )
        ''')
        cursor.execute('''
            INSERT OR IGNORE INTO users (first_name, last_name, age, email, password, phone_number, post)
            VALUES ('Admin', 'User', 30, 'admin', 'admin', '0000000000', 'admin')
        ''')

        # Create projects table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS projects (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                description TEXT,
                start_date TEXT NOT NULL,
                end_date TEXT NOT NULL,
                undertaking TEXT,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(id)
            )
        ''')

        # Create tasks table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                due_date TEXT,
                priority TEXT,
                status TEXT DEFAULT 'Pending',
                progress INTEGER DEFAULT 0,
                project_id INTEGER,
                undertaking TEXT,
                FOREIGN KEY(project_id) REFERENCES projects(id)
            )
        ''')

def add_user_to_db(db_name, first_name, last_name, age, email, password, phone_number, post):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (first_name, last_name, age, email, password, phone_number, post)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (first_name, last_name, age, email, password, phone_number, post))
        conn.commit()

def update_user_password(db_name, user_id, new_password):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users SET password = ? WHERE id = ?
        ''', (new_password, user_id))
        conn.commit()

def update_user_post(db_name, user_id, new_post):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            UPDATE users SET post = ? WHERE id = ?
        ''', (new_post, user_id))
        conn.commit()

def update_user(db_name, user_id, new_data):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        columns = ', '.join([f"{key} = ?" for key in new_data.keys()])
        values = list(new_data.values()) + [user_id]
        cursor.execute(f'''
            UPDATE users SET {columns} WHERE id = ?
        ''', values)
        conn.commit()

def delete_user(db_name, user_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM users WHERE id = ?
        ''', (user_id,))
        conn.commit()

def get_user_projects(db_name, user_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM projects WHERE user_id = ?
        ''', (user_id,))
        return cursor.fetchall()

def get_user_tasks(db_name, user_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT tasks.* FROM tasks
            INNER JOIN projects ON tasks.project_id = projects.id
            WHERE projects.user_id = ?
        ''', (user_id,))
        return cursor.fetchall()

def add_task(db_name, title, description, due_date, priority, status, progress, project_id, undertaking):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (title, description, due_date, priority, status, progress, project_id, undertaking)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (title, description, due_date, priority, status, progress, project_id, undertaking))
        conn.commit()

def delete_task(db_name, task_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM tasks WHERE id = ?
        ''', (task_id,))
        conn.commit()

def update_task(db_name, task_id, new_data):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        columns = ', '.join([f"{key} = ?" for key in new_data.keys()])
        values = list(new_data.values()) + [task_id]
        cursor.execute(f'''
            UPDATE tasks SET {columns} WHERE id = ?
        ''', values)
        conn.commit()

def get_task(db_name, task_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM tasks WHERE id = ?
        ''', (task_id,))
        return cursor.fetchone()

def get_tasks_by_project(db_name, project_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM tasks WHERE project_id = ?
        ''', (project_id,))
        return cursor.fetchall()

def add_project(db_name, name, description, start_date, end_date, undertaking, user_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO projects (name, description, start_date, end_date, undertaking, user_id)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (name, description, start_date, end_date, undertaking, user_id))
        conn.commit()

def delete_project(db_name, project_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            DELETE FROM projects WHERE id = ?
        ''', (project_id,))
        conn.commit()

def update_project(db_name, project_id, new_data):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        columns = ', '.join([f"{key} = ?" for key in new_data.keys()])
        values = list(new_data.values()) + [project_id]
        cursor.execute(f'''
            UPDATE projects SET {columns} WHERE id = ?
        ''', values)
        conn.commit()

def get_project(db_name, project_id):
    with sqlite3.connect(db_name) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT * FROM projects WHERE id = ?
        ''', (project_id,))
        return cursor.fetchone()

# Initialize the database
create_database()
