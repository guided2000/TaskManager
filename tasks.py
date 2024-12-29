from datetime import date, datetime, timedelta
from database import *
class Task:
    def __init__(self, title, description=None, due_date=None, priority=None, status='Pending', project_id=None, undertaking=None, progress=0):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.status = status
        self.project_id = project_id
        self.undertaking = undertaking
        self.progress = progress
        self.start_date = date.today().strftime("%Y-%m-%d")

    def deadline(self):
        """
        Calculate the time remaining until the due date.

        Returns:
            str: The time remaining in months, weeks, and days, or an error message if the due date is invalid.
        """
        try:
            start_date_obj = datetime.strptime(self.start_date, "%Y-%m-%d")
            due_date_obj = datetime.strptime(self.due_date, "%Y-%m-%d")

            if due_date_obj < start_date_obj:
                return "تاریخ پایان نمی‌تواند قبل از تاریخ شروع باشد."

            delta = due_date_obj - start_date_obj
            total_days = delta.days

            months = total_days // 30
            remaining_days = total_days % 30

            weeks = remaining_days // 7
            days = remaining_days % 7

            return f"{months} ماه، {weeks} هفته و {days} روز"
        except Exception as e:
            return f"خطا در محاسبه مهلت: {e}"

    def save(self):
        """
        Save the task to the database.

        Returns:
            str: A success or error message.
        """
        try:
            add_task("database.db", self.title, self.description, self.due_date, self.priority, self.status, self.project_id, self.undertaking, self.progress)
            return "وظیفه با موفقیت ذخیره شد."
        except Exception as e:
            return f"خطا در ذخیره وظیفه: {e}"

    def delete(self, task_id):
        """
        Delete a task by its ID.

        Args:
            task_id (int): The ID of the task to delete.

        Returns:
            str: A success or error message.
        """
        try:
            delete_task("database.db", task_id)
            return "وظیفه با موفقیت حذف شد."
        except Exception as e:
            return f"خطا در حذف وظیفه: {e}"

    def update(self, task_id, new_data):
        """
        Update a task's details.

        Args:
            task_id (int): The ID of the task to update.
            new_data (dict): A dictionary containing the updated task details.

        Returns:
            str: A success or error message.
        """
        try:
            update_task("database.db", task_id, new_data)
            return "وظیفه با موفقیت به‌روزرسانی شد."
        except Exception as e:
            return f"خطا در به‌روزرسانی وظیفه: {e}"

    def get_task_by_id(self, task_id):
        """
        Retrieve a task by its ID.

        Args:
            task_id (int): The ID of the task to retrieve.

        Returns:
            dict: The task details or an error message.
        """
        try:
            task = get_task("database.db", task_id)
            if task:
                return task
            return "وظیفه‌ای با این شناسه یافت نشد."
        except Exception as e:
            return f"خطا در دریافت وظیفه: {e}"
