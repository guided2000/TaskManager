from database import *

class User:
    def __init__(self, first_name, last_name, age, email, password, phone_number, post):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.phone_number = phone_number
        self.post = post
        self.tasks = []  # List to store associated tasks
        self.projects = []  # List to store associated projects

    def add_user(self):
        """
        Add a new user to the database.

        Returns:
            str: A success or error message.
        """
        try:
            add_user_to_db("database.db", self.first_name, self.last_name, self.age, self.email, self.password, self.phone_number, self.post)
            return "کاربر با موفقیت اضافه شد."
        except Exception as e:
            return f"خطا در اضافه کردن کاربر: {e}"

    def change_password(self, new_password):
        """
        Change the user's password.

        Args:
            new_password (str): The new password.

        Returns:
            str: A success or error message.
        """
        try:
            self.password = new_password
            update_user_password("database.db", self.email, new_password)
            return "رمز عبور با موفقیت تغییر کرد."
        except Exception as e:
            return f"خطا در تغییر رمز عبور: {e}"

    def update(self, new_data):
        """
        Update the user's details.

        Args:
            new_data (dict): A dictionary containing the updated user details.

        Returns:
            str: A success or error message.
        """
        try:
            update_user("database.db", self.email, new_data)
            return "اطلاعات کاربر با موفقیت به‌روزرسانی شد."
        except Exception as e:
            return f"خطا در به‌روزرسانی اطلاعات کاربر: {e}"

    def delete_user(self):
        """
        Delete the user from the database.

        Returns:
            str: A success or error message.
        """
        try:
            delete_user("database.db", self.email)
            return "کاربر با موفقیت حذف شد."
        except Exception as e:
            return f"خطا در حذف کاربر: {e}"

    def upgrade_user_post(self, new_post):
        """
        Upgrade the user's post/role.

        Args:
            new_post (str): The new post/role of the user.

        Returns:
            str: A success or error message.
        """
        try:
            self.post = new_post
            update_user_post("database.db", self.email, new_post)
            return "سمت کاربر با موفقیت ارتقا یافت."
        except Exception as e:
            return f"خطا در ارتقای سمت کاربر: {e}"

    def get_projects(self):
        """
        Retrieve all projects associated with the user.

        Returns:
            list: A list of projects or an error message.
        """
        try:
            self.projects = get_user_projects("database.db", self.email)
            return self.projects
        except Exception as e:
            return f"خطا در دریافت پروژه‌ها: {e}"

    def get_tasks(self):
        """
        Retrieve all tasks associated with the user.

        Returns:
            list: A list of tasks or an error message.
        """
        try:
            self.tasks = get_user_tasks("database.db", self.email)
            return self.tasks
        except Exception as e:
            return f"خطا در دریافت وظایف: {e}"
