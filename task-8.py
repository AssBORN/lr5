import tkinter as tk
from tkinter import ttk, messagebox

class MultiWindowApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Главная программа")
        self.root.geometry("400x200")

        self.win_hello = None
        self.win_settings = None

        tk.Label(root, text=" Программа с несколькими окнами", font=("Arial", 14, "bold")).pack(pady=15)

        tk.Button(root, text="Открыть окно «Привет»", font=("Arial", 11),
                  command=self.open_hello_window, width=25).pack(pady=5)

        tk.Button(root, text="Открыть окно «Настройки»", font=("Arial", 11),
                  command=self.open_settings_window, width=25).pack(pady=5)

        tk.Button(root, text="Выход", font=("Arial", 11), bg="#f44336", fg="white",
                  command=root.quit, width=25).pack(pady=15)

    def open_hello_window(self):
        # Если окно уже открыто — фокус на него
        if self.win_hello and self.win_hello.winfo_exists():
            self.win_hello.focus_set()
            return

        self.win_hello = tk.Toplevel(self.root)
        self.win_hello.title("Окно «Привет»")
        self.win_hello.geometry("300x150")
        self.win_hello.resizable(False, False)

        self.win_hello.protocol("WM_DELETE_WINDOW", self.on_hello_close)

        tk.Label(self.win_hello, text="Привет из дочернего окна!", font=("Arial", 12)).pack(pady=20)
        tk.Button(self.win_hello, text="Закрыть", command=self.win_hello.destroy).pack()

    def on_hello_close(self):
        self.win_hello.destroy()
        self.win_hello = None

    def open_settings_window(self):
        if self.win_settings and self.win_settings.winfo_exists():
            self.win_settings.focus_set()
            return

        self.win_settings = tk.Toplevel(self.root)
        self.win_settings.title("Окно «Настройки»")
        self.win_settings.geometry("350x200")
        self.win_settings.resizable(False, False)

        self.win_settings.protocol("WM_DELETE_WINDOW", self.on_settings_close)

        tk.Label(self.win_settings, text="⚙ Настройки", font=("Arial", 12, "bold")).pack(pady=10)

        self.dark_mode = tk.BooleanVar(value=True)
        chk = tk.Checkbutton(self.win_settings, text="Тёмная тема", variable=self.dark_mode)
        chk.pack(anchor="w", padx=30, pady=5)

        tk.Label(self.win_settings, text="Имя пользователя:").pack(anchor="w", padx=30, pady=(10, 0))
        self.username_entry = tk.Entry(self.win_settings, width=30)
        self.username_entry.insert(0, "user")
        self.username_entry.pack(padx=30, pady=5)

        tk.Button(self.win_settings, text="Сохранить", command=self.save_settings, width=15).pack(pady=15)

    def on_settings_close(self):
        self.win_settings.destroy()
        self.win_settings = None

    def save_settings(self):
        name = self.username_entry.get().strip()
        theme = "включена" if self.dark_mode.get() else "отключена"
        messagebox.showinfo("Сохранено", f"Настройки сохранены:\nИмя: {name}\nТёмная тема: {theme}")


root = tk.Tk()
app = MultiWindowApp(root)
root.mainloop()