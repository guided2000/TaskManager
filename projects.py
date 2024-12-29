from database import *

class Project:
    def __init__(self, name, description, start_date, end_date, tasks_id, undertaking):
        self.name = name
        self.description = description
        self.start_date = start_date
        self.end_date = end_date
        self.tasks_id = tasks_id
        self.undertaking = undertaking

    def save(self):
        """
        Save the project to the database.

        Returns:
            str: A success or error message.
        """
        try:
            add_project("database.db", self.name, self.description, self.start_date, self.end_date, self.tasks_id, self.undertaking)
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
