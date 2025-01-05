from database import *
from user import *
class Project:
    def __init__(self, name, description, start_date, end_date, undertaking):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.undertaking = undertaking

    def save(self):
        """
        Save the project to the database.

        Returns:
            str: A success or error message.
        """
        user=User.get_user_by_username(self.undertaking)
        user_id=user['id']
        try:
            add_project("database.db", self.name, self.description, self.start_date, self.end_date,self.undertaking, user_id)
            return "پروژه با موفقیت ذخیره شد."
        except Exception as e:
            return f"خطا در ذخیره پروژه: {e}"

    def get_tasks(self):
        """
        Retrieve all tasks associated with this project.

        Returns:
            list: A list of tasks or an error message.
        """
        try:
            tasks = get_tasks_by_project("database.db", self.tasks_id)
            return tasks if tasks else "هیچ وظیفه‌ای برای این پروژه یافت نشد."
        except Exception as e:
            return f"خطا در دریافت وظایف پروژه: {e}"

    def update(self, new_data):
        """
        Update the project's details.

        Args:
            new_data (dict): A dictionary containing the updated project details.

        Returns:
            str: A success or error message.
        """
        try:
            update_project("database.db", self.name, new_data)
            return "پروژه با موفقیت به‌روزرسانی شد."
        except Exception as e:
            return f"خطا در به‌روزرسانی پروژه: {e}"

    def delete(self):
        """
        Delete the project from the database.

        Returns:
            str: A success or error message.
        """
        try:
            delete_project("database.db", self.name)
            return "پروژه با موفقیت حذف شد."
        except Exception as e:
            return f"خطا در حذف پروژه: {e}"

    @staticmethod
    def get_all_projects(undertaking):
        """
        Retrieve all projects based on the undertaking attribute.

        Args:
            undertaking (str): The undertaking attribute to filter projects.

        Returns:
            list: A list of projects matching the undertaking, or an empty list if no projects are found.
        """
        conn = sqlite3.connect("database.db")
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM projects WHERE undertaking = ?", (undertaking,))
            projects = cursor.fetchall()
            project_list = [
                {
                    "id":project[0],
                    "name": project[1],
                    "description": project[2],
                    "start_date": project[3],
                    "end_date": project[4],
                    "undertaking": project[5],
                }
                for project in projects
            ]
            return project_list
        except Exception as e:
            print(f"Database error: {e}")
            return []
        finally:
            conn.close()