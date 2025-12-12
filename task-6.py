import tkinter as tk
from tkinter import ttk, messagebox


RATES = {
    'USD': 1.0,
    'EUR': 0.8525,
    'RUB': 77.8998,
}

CURRENCIES = list(RATES.keys())

def convert():
    amount = float(entry_amount.get())
    from_curr = combo_from.get()
    to_curr = combo_to.get()

    amount_in_usd = amount / RATES[from_curr]
    result = amount_in_usd * RATES[to_curr]

    label_result.config(text=f"{amount} {from_curr} = {result:.2f} {to_curr}")

root = tk.Tk()
root.title("Конвертер валют")
root.geometry("400x260")
root.resizable(False, False)

tk.Label(root, text="💱 Конвертер валют", font=("Arial", 16, "bold")).pack(pady=10)

frame_amount = tk.Frame(root)
frame_amount.pack(pady=5)
tk.Label(frame_amount, text="Сумма:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
entry_amount = tk.Entry(frame_amount, font=("Arial", 12), width=12)
entry_amount.pack(side=tk.LEFT, padx=5)
entry_amount.insert(0, "100")

frame_from = tk.Frame(root)
frame_from.pack(pady=5)
tk.Label(frame_from, text="Из:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
combo_from = ttk.Combobox(frame_from, values=CURRENCIES, state="readonly", width=10, font=("Arial", 12))
combo_from.set("RUB")
combo_from.pack(side=tk.LEFT, padx=5)

frame_to = tk.Frame(root)
frame_to.pack(pady=5)
tk.Label(frame_to, text="В:", font=("Arial", 12)).pack(side=tk.LEFT, padx=5)
combo_to = ttk.Combobox(frame_to, values=CURRENCIES, state="readonly", width=10, font=("Arial", 12))
combo_to.set("USD")
combo_to.pack(side=tk.LEFT, padx=5)

btn_convert = tk.Button(root, text="Конвертировать", font=("Arial", 12, "bold"),
                        bg="#2196F3", fg="white", command=convert)
btn_convert.pack(pady=15)

label_result = tk.Label(root, text="", font=("Arial", 14, "bold"), fg="#333")
label_result.pack()

root.mainloop()