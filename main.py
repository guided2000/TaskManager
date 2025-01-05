import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from database import *  # Your database file
from projects import Project
from tasks import Task
from user import User

class TaskManagerApp:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Task Manager")
        self.window.geometry("800x600")

        # Menu bar
        self.create_menu_bar()

        # Main frame
        self.main_frame = tk.Frame(self.window, padx=10, pady=10)
        self.main_frame.pack(fill="both", expand=True)

        # Show login screen
        self.show_login_screen()

    def create_menu_bar(self):
        menu_bar = tk.Menu(self.window)

        # Profile menu
        profile_menu = tk.Menu(menu_bar, tearoff=0)
        profile_menu.add_command(label="View Profile", command=self.show_profile)
        profile_menu.add_command(label="Logout", command=self.logout)
        menu_bar.add_cascade(label="Profile", menu=profile_menu)

        # Projects menu
        project_menu = tk.Menu(menu_bar, tearoff=0)
        project_menu.add_command(label="View Projects", command=self.show_projects)
        project_menu.add_command(label="Add Project", command=self.add_project)
        menu_bar.add_cascade(label="Projects", menu=project_menu)

        # Tasks menu
        task_menu = tk.Menu(menu_bar, tearoff=0)
        task_menu.add_command(label="View Tasks", command=self.show_tasks)
        task_menu.add_command(label="Add Task", command=self.add_task)
        menu_bar.add_cascade(label="Tasks", menu=task_menu)

        self.window.config(menu=menu_bar)
    def clear_main_frame(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    def show_login_screen(self):
        self.clear_main_frame()

        login_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        login_frame.pack(fill="both", expand=True)

        tk.Label(login_frame, text="Username:").pack(anchor="w")
        username_entry = tk.Entry(login_frame)
        username_entry.pack(fill="x")

        tk.Label(login_frame, text="Password:").pack(anchor="w")
        password_entry = tk.Entry(login_frame, show="*")
        password_entry.pack(fill="x")

        def login():
            username = username_entry.get()
            password = password_entry.get()
            user = User.authenticate(username, password)
            if user:
                self.logged_in_user = username
                messagebox.showinfo("Success", "Login successful!")
                self.show_tasks()
            else:
                messagebox.showerror("Error", "Invalid username or password.")

        tk.Button(login_frame, text="Login", command=login).pack(pady=10)
    def show_projects(self):
        self.clear_main_frame()

        tk.Label(self.main_frame, text="Project List", font=("Arial", 16)).pack(pady=10)

        # Projects table
        project_table = ttk.Treeview(self.main_frame, columns=("Name", "Start date", "End date"), show="headings")
        project_table.heading("Name", text="Project Name")
        project_table.heading("Start date", text="Start date")
        project_table.heading("End date", text="End date")
        project_table.pack(fill="both", expand=True)

        # Retrieve and display projects from the database
        projects = Project.get_all_projects(self.logged_in_user)
        for project in projects:
            project_table.insert("", "end", values=(project["name"], project["start_date"], project["end_date"]))


        # Add project button
        tk.Button(self.main_frame, text="Add Project", command=self.add_project).pack(pady=10)
    def add_project(self):
        self.clear_main_frame()
    
        # عنوان صفحه
        tk.Label(self.main_frame, text="Add Project", font=("Arial", 16)).pack(pady=10)
    
        # متغیرهای ذخیره داده‌های ورودی
        name_var = tk.StringVar()
        description_var = tk.StringVar()
        start_date_var = tk.StringVar()
        end_date_var = tk.StringVar()
        undertaking_var = self.logged_in_user
    
        # ایجاد فرم ورودی‌ها
        tk.Label(self.main_frame, text="Name:").pack(anchor="w", padx=20, pady=5)
        tk.Entry(self.main_frame, textvariable=name_var, width=30).pack(padx=20)
    
        tk.Label(self.main_frame, text="Description:").pack(anchor="w", padx=20, pady=5)
        tk.Entry(self.main_frame, textvariable=description_var, width=30).pack(padx=20)
    
        tk.Label(self.main_frame, text="Start Date:").pack(anchor="w", padx=20, pady=5)
    
        # دکمه انتخاب تاریخ شروع
        def select_start_date():
            calendar_window = tk.Toplevel(self.window)
            calendar_window.title("Select Start Date")
            calendar = Calendar(calendar_window, date_pattern="yyyy-mm-dd")
            calendar.pack(pady=10)
    
            def confirm_date():
                start_date_var.set(calendar.get_date())
                calendar_window.destroy()
    
            tk.Button(calendar_window, text="OK", command=confirm_date).pack()
    
        tk.Entry(self.main_frame, textvariable=start_date_var, width=30).pack(padx=20)
        tk.Button(self.main_frame, text="Select Start Date", command=select_start_date).pack(pady=5)
    
        tk.Label(self.main_frame, text="End Date:").pack(anchor="w", padx=20, pady=5)
    
        # دکمه انتخاب تاریخ پایان
        def select_end_date():
            calendar_window = tk.Toplevel(self.window)
            calendar_window.title("Select End Date")
            calendar = Calendar(calendar_window, date_pattern="yyyy-mm-dd")
            calendar.pack(pady=10)
    
            def confirm_date():
                end_date_var.set(calendar.get_date())
                calendar_window.destroy()
    
            tk.Button(calendar_window, text="OK", command=confirm_date).pack()
    
        tk.Entry(self.main_frame, textvariable=end_date_var, width=30).pack(padx=20)
        tk.Button(self.main_frame, text="Select End Date", command=select_end_date).pack(pady=5)
    
        tk.Label(self.main_frame, text="Undertaking:").pack(anchor="w", padx=20, pady=5)
        tk.Label(self.main_frame, text=self.logged_in_user).pack(padx=20)
    
        # تابع ذخیره‌سازی اطلاعات
        def save_project():
            name = name_var.get()
            description = description_var.get()
            start_date = start_date_var.get()
            end_date = end_date_var.get()
            undertaking = self.logged_in_user
    
            # بررسی خالی نبودن فیلدها
            if not name or not description or not start_date or not end_date or not undertaking:
                tk.messagebox.showerror("Error", "Please fill in all fields!")
                return
    
            # نمایش پیام موفقیت
            project = Project(name, description, start_date, end_date, undertaking)
            project.save()
            tk.messagebox.showinfo("Success", f"Project '{name}' added successfully!")
    
            # پاک کردن ورودی‌ها
            name_var.set("")
            description_var.set("")
            start_date_var.set("")
            end_date_var.set("")
    
        # دکمه اضافه کردن
        tk.Button(
            self.main_frame,
            text="Add",
            command=save_project,
            bg="green",
            fg="white",
            font=("Arial", 12),
        ).pack(pady=20)
    def refresh_task_list(self, query=None):
        """
        Refresh the task list in the table, including the project name for each task.
        """
        try:
            # Clear existing table entries
            for item in self.task_table.get_children():
                self.task_table.delete(item)

            # Connect to the database
            conn = sqlite3.connect("database.db")
            cursor = conn.cursor()

            # Query to retrieve tasks with project names
            sql = """
            SELECT tasks.title, tasks.due_date, tasks.priority, tasks.status, projects.name AS project_name
            FROM tasks
            LEFT JOIN projects ON tasks.project_id = projects.id
            """
            if query:
                sql += f" WHERE tasks.title LIKE '%{query}%' OR projects.name LIKE '%{query}%'"

            cursor.execute(sql)
            tasks = cursor.fetchall()

            # Insert data into the table
            for task in tasks:
                self.task_table.insert("", "end", values=(task[0], task[1], task[2], task[3], task[4]))

            # Close the database connection
            conn.close()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Failed to load tasks: {e}")
    def show_tasks(self):
        """
        Display the task list with an additional column for project names.
        """
        self.clear_main_frame()

        tk.Label(self.main_frame, text="Task List", font=("Arial", 16)).pack(pady=10)

        # Task table
        columns = ["Title", "Due Date", "Priority", "Status", "Project"]
        self.task_table = ttk.Treeview(self.main_frame, columns=columns, show="headings")
        for col in columns:
            self.task_table.heading(col, text=col)
        self.task_table.pack(fill="both", expand=True)

        tasks=Task.get_all_task(self.logged_in_user)
        
            
        self.refresh_task_list()

        # Attach right-click menu
        self.task_table.bind("<Button-3>")
    def add_task(self):
        self.clear_main_frame()

            # عنوان صفحه
        tk.Label(self.main_frame, text="Add Task", font=("Arial", 16)).pack(pady=10)

        # متغیرهای ذخیره داده‌های ورودی
        title_var = tk.StringVar()
        description_var = tk.StringVar()
        due_date_var = tk.StringVar()
        priority_var = tk.StringVar()
        status_var = tk.StringVar()
        project_id_var = tk.StringVar()
        undertaking_var = tk.StringVar()
        progress_var = tk.StringVar()

        # ایجاد فرم ورودی‌ها
        tk.Label(self.main_frame, text="Title:").pack(anchor="w", padx=20, pady=5)
        tk.Entry(self.main_frame, textvariable=title_var, width=30).pack(padx=20)

        tk.Label(self.main_frame, text="Description:").pack(anchor="w", padx=20, pady=5)
        tk.Entry(self.main_frame, textvariable=description_var, width=30).pack(padx=20)

        tk.Label(self.main_frame, text="Due Date:").pack(anchor="w", padx=20, pady=5)
        tk.Entry(self.main_frame, textvariable=due_date_var, width=30).pack(padx=20)

        tk.Label(self.main_frame, text="Priority:").pack(anchor="w", padx=20, pady=5)
        # لیست آیتم‌ها
        items = ["Very high","High","Medium","Low","Very low","No priority"]

        # ایجاد لیست کشویی
        priority_combobox = ttk.Combobox(self.main_frame, values=items,width=28, state="readonly")
        priority_combobox.set("Choose")  # مقدار پیش‌فرض
        priority_combobox.pack(padx=20)

        tk.Label(self.main_frame, text="Status:").pack(anchor="w", padx=20, pady=5)
        # لیست آیتم‌ها
        items = ['Pending','In Progress','Completed']

        # ایجاد لیست کشویی
        status_combobox = ttk.Combobox(self.main_frame, values=items,width=28, state="readonly")
        status_combobox.set("Choose")  # مقدار پیش‌فرض
        status_combobox.pack(padx=20)

        tk.Label(self.main_frame, text="Project:").pack(anchor="w", padx=20, pady=5)
        projects=Project.get_all_projects(self.logged_in_user)
        items = []
        for project in projects:
            item=project["id"]
            item=str(item)+'_'+project["name"]
            items.append(item)

        # ایجاد لیست کشویی
        project_combobox= ttk.Combobox(self.main_frame, values=items,width=28, state="readonly")
        project_combobox.set("Choose")  # مقدار پیش‌فرض
        project_combobox.pack(padx=20)
        tk.Label(self.main_frame, text="Undertaking:").pack(anchor="w", padx=20, pady=5)
        tk.Label(self.main_frame, text=self.logged_in_user).pack(padx=20)

        tk.Label(self.main_frame, text="Progress:").pack(anchor="w", padx=20, pady=5)
        tk.Entry(self.main_frame, textvariable=progress_var, width=30).pack(padx=20)

        # تابع ذخیره‌سازی اطلاعات وظیفه
        def save_task():
            title = title_var.get()
            description = description_var.get()
            due_date = due_date_var.get()
            priority = priority_combobox.get()
            status = status_combobox.get()
            project_id = project_combobox.get()
            undertaking = self.logged_in_user
            progress = progress_var.get()

            # بررسی خالی نبودن فیلدها
            if not title or not description or not due_date or not priority or not status or not project_id or not undertaking or not progress:
                messagebox.showerror("Error", "Please fill in all fields!")
                return
            project_id=int(project_id.split('_')[0])
            # نمایش پیام موفقیت (می‌توانید ذخیره در دیتابیس را اینجا اضافه کنید)
            new_task=Task(title, description, due_date, priority, status, project_id, undertaking, progress)
            new_task.save()
            messagebox.showinfo("Success", f"Task '{title}' added successfully!")
            #پاک کردن مقادیر فرم
            title_var.set("")
            description_var.set("")
            due_date_var.set("")
            priority_combobox.set("Choose")
            status_combobox.set("choose")
            project_combobox.set("choose")
            progress_var.set("")
            

        # دکمه اضافه کردن
        tk.Button(
            self.main_frame,
            text="Add Task",
            command=save_task,
            bg="green",
            fg="white",
            font=("Arial", 12),
        ).pack(pady=20)
    def edit_task(self, task_id):
        messagebox.showinfo("Info", "Edit task functionality not implemented yet.")
    def delete_task(self, task_id):
        confirm = messagebox.askyesno("Delete Task", "Are you sure you want to delete this task?")
        if confirm:
            Task.delete(task_id)
            self.refresh_task_list()
    def show_profile(self):
        self.clear_main_frame()

        profile_frame = tk.Frame(self.main_frame, padx=10, pady=10)
        profile_frame.pack(fill="both", expand=True)

        user = User.get_user_by_username(self.logged_in_user)
        if user:
            profile_info = f"""
            Username:{user['username']}
            Name: {user['first_name']} {user['last_name']}
            Email: {user['email']}
            Phone: {user['phone_number']}
            Age: {user['age']}
            Role: {user['post']}
            """
        else:
            profile_info = "No user found!"

        tk.Label(profile_frame, text=profile_info, justify="left", font=("Arial", 12)).pack(anchor="w")
    def logout(self):
        confirm = messagebox.askyesno("Logout", "Are you sure you want to logout?")
        if confirm:
            self.clear_main_frame()
            self.show_login_screen()

if __name__ == "__main__":
    app = TaskManagerApp()
    app.window.mainloop()
