import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.simpledialog import askstring
from database import get_user_tasks, delete_task, update_task  # Importing your database functions

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")
        self.db_name = "database.db"  # Database name

        # Menu Bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Adding Profile menu
        profile_menu = tk.Menu(self.menu_bar, tearoff=0)
        profile_menu.add_command(label="View Profile", command=self.view_profile)
        profile_menu.add_command(label="Logout", command=self.logout)
        self.menu_bar.add_cascade(label="Profile", menu=profile_menu)

        # Adding Projects menu
        projects_menu = tk.Menu(self.menu_bar, tearoff=0)
        projects_menu.add_command(label="View Projects", command=self.view_projects)
        projects_menu.add_command(label="Add Project", command=self.add_project)
        self.menu_bar.add_cascade(label="Projects", menu=projects_menu)

        # Adding Tasks menu
        tasks_menu = tk.Menu(self.menu_bar, tearoff=0)
        tasks_menu.add_command(label="View Tasks", command=self.view_tasks)
        tasks_menu.add_command(label="Add Task", command=self.add_task)
        self.menu_bar.add_cascade(label="Tasks", menu=tasks_menu)

        # Search Bar
        self.search_frame = tk.Frame(self.root)
        self.search_frame.pack(fill=tk.X, padx=10, pady=5)

        self.search_label = tk.Label(self.search_frame, text="Search Tasks:")
        self.search_label.pack(side=tk.LEFT, padx=(0, 5))

        self.search_entry = tk.Entry(self.search_frame)
        self.search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 5))

        self.search_button = tk.Button(self.search_frame, text="Search", command=self.search_tasks)
        self.search_button.pack(side=tk.RIGHT)

        # Task List
        self.tree = ttk.Treeview(self.root, columns=("ID", "Title", "Description", "Due Date", "Priority", "Status", "Progress"), show="headings")
        self.tree.heading("ID", text="ID")
        self.tree.heading("Title", text="Title")
        self.tree.heading("Description", text="Description")
        self.tree.heading("Due Date", text="Due Date")
        self.tree.heading("Priority", text="Priority")
        self.tree.heading("Status", text="Status")
        self.tree.heading("Progress", text="Progress")
        self.tree.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Adding Right-Click Menu
        self.context_menu = tk.Menu(self.root, tearoff=0)
        self.context_menu.add_command(label="Edit Task", command=self.edit_task)
        self.context_menu.add_command(label="Delete Task", command=self.delete_task)

        self.tree.bind("<Button-3>", self.show_context_menu)

        # Load Tasks
        self.load_tasks()

    def load_tasks(self):
        for row in self.tree.get_children():
            self.tree.delete(row)

        tasks = get_user_tasks(self.db_name, user_id=1)  # Assuming user_id is 1 for demonstration
        for task in tasks:
            self.tree.insert("", "end", values=task)

    def search_tasks(self):
        query = self.search_entry.get()
        for row in self.tree.get_children():
            self.tree.delete(row)

        tasks = get_user_tasks(self.db_name, user_id=1)  # Assuming user_id is 1
        filtered_tasks = [task for task in tasks if query.lower() in task[1].lower()]

        for task in filtered_tasks:
            self.tree.insert("", "end", values=task)

    def show_context_menu(self, event):
        selected_item = self.tree.identify_row(event.y)
        if selected_item:
            self.tree.selection_set(selected_item)
            self.context_menu.post(event.x_root, event.y_root)

    def edit_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a task to edit.")
            return

        task_id = self.tree.item(selected_item[0])['values'][0]
        new_title = askstring("Edit Task", "Enter new title:")
        if new_title:
            update_task(self.db_name, task_id, {"title": new_title})
            self.load_tasks()

    def delete_task(self):
        selected_item = self.tree.selection()
        if not selected_item:
            messagebox.showwarning("No Selection", "Please select a task to delete.")
            return

        task_id = self.tree.item(selected_item[0])['values'][0]
        if messagebox.askyesno("Confirm Delete", "Are you sure you want to delete this task?"):
            delete_task(self.db_name, task_id)
            self.load_tasks()

    def view_profile(self):
        messagebox.showinfo("Profile", "Profile view is not yet implemented.")

    def logout(self):
        messagebox.showinfo("Logout", "Logout functionality is not yet implemented.")

    def view_projects(self):
        messagebox.showinfo("Projects", "View Projects functionality is not yet implemented.")

    def add_project(self):
        messagebox.showinfo("Add Project", "Add Project functionality is not yet implemented.")

    def view_tasks(self):
        messagebox.showinfo("Tasks", "View Tasks functionality is not yet implemented.")

    def add_task(self):
        messagebox.showinfo("Add Task", "Add Task functionality is not yet implemented.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
