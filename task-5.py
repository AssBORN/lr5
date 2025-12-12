import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Программа со вкладками")
root.geometry("600x400")

notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill='both', padx=10, pady=10)

tab1 = ttk.Frame(notebook)
notebook.add(tab1, text="Главная")

label1 = tk.Label(tab1, text="Добро пожаловать на первую вкладку!", font=("Arial", 14))
label1.pack(pady=20)

tab2 = ttk.Frame(notebook)
notebook.add(tab2, text="Настройки")

label2 = tk.Label(tab2, text="Здесь могут быть настройки.", font=("Arial", 12))
label2.pack(pady=20)

btn = tk.Button(tab2, text="Нажми меня", command=lambda: print("Кнопка нажата!"))
btn.pack()

tab3 = ttk.Frame(notebook)
notebook.add(tab3, text="Справка")

text = tk.Text(tab3, height=8, width=50)
text.insert(tk.END, "Это пример многостраничного интерфейса.\n")
text.config(state=tk.DISABLED)  
text.pack(pady=20, padx=10)

root.mainloop()