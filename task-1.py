import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Окно с кнопкой «Привет»")
root.geometry("300x150")

def say_hello():
    messagebox.showinfo("Приветствие", "Привет! Рады вас видеть!")

btn_hello = tk.Button(
    root,
    text="Привет",
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
    command=say_hello
)
btn_hello.pack(expand=True)

root.mainloop()