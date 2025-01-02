

def add_task(self):
    self.clear_main_frame()
    
        # عنوان صفحه
    tk.Label(self.main_frame, text="Add Project", font=("Arial", 16)).pack(pady=10)
    
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
    tk.Entry(self.main_frame, textvariable=priority_var, width=30).pack(padx=20)

    tk.Label(self.main_frame, text="Status:").pack(anchor="w", padx=20, pady=5)
    tk.Entry(self.main_frame, textvariable=status_var, width=30).pack(padx=20)

    tk.Label(self.main_frame, text="Project ID:").pack(anchor="w", padx=20, pady=5)
    tk.Entry(self.main_frame, textvariable=project_id_var, width=30).pack(padx=20)

    tk.Label(self.main_frame, text="Undertaking:").pack(anchor="w", padx=20, pady=5)
    tk.Entry(self.main_frame, textvariable=undertaking_var, width=30).pack(padx=20)

    tk.Label(self.main_frame, text="Progress:").pack(anchor="w", padx=20, pady=5)
    tk.Entry(self.main_frame, textvariable=progress_var, width=30).pack(padx=20)

    # تابع ذخیره‌سازی اطلاعات وظیفه
    def save_task():
        title = title_var.get()
        description = description_var.get()
        due_date = due_date_var.get()
        priority = priority_var.get()
        status = status_var.get()
        project_id = project_id_var.get()
        undertaking = undertaking_var.get()
        progress = progress_var.get()

        # بررسی خالی نبودن فیلدها
        if not title or not description or not due_date or not priority or not status or not project_id or not undertaking or not progress:
            messagebox.showerror("Error", "Please fill in all fields!")
            return

        # نمایش پیام موفقیت (می‌توانید ذخیره در دیتابیس را اینجا اضافه کنید)
        messagebox.showinfo("Success", f"Task '{title}' added successfully!")

        # بستن پنجره وظیفه
        self.main_frame.destroy()

    # دکمه اضافه کردن
    tk.Button(
        self.main_frame,
        text="Add Task",
        command=save_task,
        bg="green",
        fg="white",
        font=("Arial", 12),
    ).pack(pady=20)

