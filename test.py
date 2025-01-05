import tkinter as tk

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("منوی راست کلیک در Tkinter")
root.geometry("300x200")

# تابع برای هر گزینه در منو
def say_hello():
    print("سلام!")
    label.config(text="سلام!")

def say_goodbye():
    print("خداحافظ!")
    label.config(text="خداحافظ!")

# ایجاد منوی راست کلیک
right_click_menu = tk.Menu(root, tearoff=0)
right_click_menu.add_command(label="سلام", command=say_hello)
right_click_menu.add_command(label="خداحافظ", command=say_goodbye)
right_click_menu.add_separator()
right_click_menu.add_command(label="خروج", command=root.quit)

# تابع برای نمایش منوی راست کلیک
def show_right_click_menu(event):
    right_click_menu.tk_popup(event.x_root, event.y_root)

# اتصال رویداد راست کلیک به منو
root.bind("<Button-3>", show_right_click_menu)

# برچسب برای نمایش متن انتخاب شده
label = tk.Label(root, text="روی صفحه راست کلیک کنید", font=("Arial", 12))
label.pack(pady=50)

# اجرای حلقه اصلی برنامه
root.mainloop()
