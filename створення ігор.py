import tkinter as tk
from tkinter import messagebox
import re


def validate_input(value):
    pattern = r"^\d+(\.\d{1,2})?$"
    return bool(re.match(pattern, value))


wallet = float(input("Скільки грошей у вас зараз в гаманці? "))
lunch = float(input("Скільки ви витратили на обід? "))
transport_cost = float(input("Скільки плануєте витратити на транспорт? "))

balance = wallet - (lunch + transport_cost)
print(f"Після витрат у вас залишиться {balance:.2f} грн.")

if balance < 100:
    print("Грошей мало, час економити!")
else:
    print("Все добре, можна трохи витратити на себе.")


days = int(input("Скільки днів хочете вести облік витрат? "))


expenses_dict = {}


for day in range(1, days + 1):
    food = float(input(f"День {day}. Витрати на їжу: "))
    transport = float(input(f"День {day}. Витрати на транспорт: "))
    other = float(input(f"День {day}. Інші витрати: "))
    expenses_dict[f"День {day}"] = food + transport + other


print("Витрати по днях:")
for day, amount in expenses_dict.items():
    print(f"{day}: {amount:.2f} грн")


def calculate_total_expenses(exp_dict):
    return sum(exp_dict.values())

def average_daily_expense(exp_dict):
    return sum(exp_dict.values()) / len(exp_dict) if exp_dict else 0


total = calculate_total_expenses(expenses_dict)
average = average_daily_expense(expenses_dict)

print(f"Загальні витрати: {total:.2f} грн")
print(f"Середні витрати на день: {average:.2f} грн")


root = tk.Tk()
root.title("Фінансовий облік")


tk.Label(root, text="Витрати на їжу").pack()
food_entry = tk.Entry(root)
food_entry.pack()

tk.Label(root, text="Витрати на транспорт").pack()
transport_entry = tk.Entry(root)
transport_entry.pack()

tk.Label(root, text="Інші витрати").pack()
other_entry = tk.Entry(root)
other_entry.pack()


def add_day():
    try:
        food = float(food_entry.get())
        transport = float(transport_entry.get())
        other = float(other_entry.get())

        day_num = len(expenses_dict) + 1
        expenses_dict[f"День {day_num}"] = food + transport + other

        food_entry.delete(0, tk.END)
        transport_entry.delete(0, tk.END)
        other_entry.delete(0, tk.END)
    except ValueError:
        messagebox.showerror("Помилка", "Введіть коректні числа!")


def show_results():
    total = calculate_total_expenses(expenses_dict)
    avg = average_daily_expense(expenses_dict)
    messagebox.showinfo("Результати", f"Загальні витрати: {total:.2f} грн\nСередні витрати: {avg:.2f} грн")

# Кнопки
tk.Button(root, text="Додати день", command=add_day).pack()
tk.Button(root, text="Результати", command=show_results).pack()

root.mainloop()