import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Окно с меню")
root.geometry("400x300")

def exit_app():
    if messagebox.askyesno("Выход", "Вы действительно хотите выйти?"):
        root.destroy() 

menubar = tk.Menu(root)

file_menu = tk.Menu(menubar, tearoff=0)
file_menu.add_command(label="Exit", command=exit_app, accelerator="Ctrl+Q")
menubar.add_cascade(label="File", menu=file_menu)

root.config(menu=menubar)

root.bind('<Control-q>', lambda e: exit_app())

label = tk.Label(root, text="Меню: File → Exit", font=("Arial", 14))
label.pack(expand=True)

root.mainloop()