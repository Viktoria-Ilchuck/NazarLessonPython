
#1
name = input("Введіть ім'я співробітника: ")
hourly_rate = float(input("Введіть ставку за годину (грн): "))
hours_worked = int(input("Введіть кількість відпрацьованих годин: "))

gross_salary = hourly_rate * hours_worked
tax = 0.20 * gross_salary
net_salary = gross_salary - tax


print(f"{name} отримає {net_salary:.2f} грн після сплати податку.")

#2.1

tasks_input = input("Введіть список справ через кому: ")
tasks = [task.strip() for task in tasks_input.split(",") if task.strip()]

while True:
    if not tasks:
        print("Список справ порожній.")
        break

    print("\nВаш список справ:")
    for i, task in enumerate(tasks, 1):
        print(f"{i}. {task}")

    delete = input("Введіть номер справи, яку хочете видалити (або 'exit' для виходу): ")
    if delete.lower() == 'exit':
        break

    if delete.isdigit():
        index = int(delete) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            print(f"Справу '{removed}' видалено.")
        else:
            print("Невірний номер справи.")
    else:
        print("Введіть коректний номер або 'exit'.")

#2.2

numbers = []

for _ in range(5):
    num = float(input("Введіть число: "))
    numbers.append(num)

print(f"Найбільше число: {max(numbers)}")
print(f"Найменше число: {min(numbers)}")

#2.3

import random

number = random.randint(1, 100)
attempts = 7

print("Вгадайте число від 1 до 100. У вас є 7 спроб.")

while attempts > 0:
    guess = input(f"Спроба {8 - attempts}. Ваше число: ")
    if not guess.isdigit():
        print("Введіть коректне число.")
        continue

    guess = int(guess)
    if guess == number:
        print("Вітаю! Ви вгадали число!")
        break
    elif guess < number:
        print("Більше")
    else:
        print("Менше")

    attempts -= 1

if attempts == 0:
    print(f"Ви програли. Загадане число було {number}.")

#3.1
phonebook = {}

while True:
    print("\nТелефонна книга:")
    print("1. Додати контакт")
    print("2. Шукати контакт")
    print("3. Видалити контакт")
    print("4. Вийти")

    choice = input("Виберіть дію (1-4): ")

    if choice == '1':
        name = input("Введіть ім'я: ")
        number = input("Введіть номер телефону: ")
        phonebook[name] = number
        print(f"Контакт '{name}' додано.")

    elif choice == '2':
        name = input("Введіть ім'я для пошуку: ")
        if name in phonebook:
            print(f"Номер {name}: {phonebook[name]}")
        else:
            print("Контакт не знайдено.")

    elif choice == '3':
        name = input("Введіть ім'я для видалення: ")
        if name in phonebook:
            del phonebook[name]
            print(f"Контакт '{name}' видалено.")
        else:
            print("Контакт не знайдено.")

    elif choice == '4':
        print("Вихід з програми.")
        break

    else:
        print("Невірний вибір. Спробуйте ще раз.")

#3.2

eng_ukr_dict = {
    "hello": "привіт",
    "cat": "кіт",
    "dog": "собака",
    "car": "автомобіль",
    "book": "книга"
}

word = input("Введіть англійське слово: ").lower()
translation = eng_ukr_dict.get(word)

if translation:
    print(f"Переклад: {translation}")
else:
    print("Слово не знайдено у словнику.")

#4.1

import re

email = input("Введіть електронну пошту: ")

pattern = r'^[\w\.]+@[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$'

if re.match(pattern, email):
    print("Електронна пошта валідна")
else:
    print("Невалідна електронна пошта")

#4.2

import re

phone = input("Введіть номер телефону : ")

pattern = r'^\+380\d{9}$'

if re.match(pattern, phone):
    print("Валідний номер")
else:
    print("Помилка")

#5.1

def convert_currency(amount_uah, currency):
    rates = {
        "USD": 36.9,
        "EUR": 39.5,
        "PLN": 8.5
    }
    rate = rates.get(currency.upper())
    if rate:
        return amount_uah / rate
    else:
        return None

amount = float(input("Введіть суму в грн: "))
currency = input("Оберіть валюту (USD, EUR, PLN): ")

result = convert_currency(amount, currency)
if result is not None:
    print(f"{amount} грн = {result:.2f} {currency.upper()}")
else:
    print("Невідома валюта.")

#5.2

def square_area(side):
    return side * side

length = float(input("Введіть довжину сторони квадрата: "))
area = square_area(length)
print(f"Площа квадрата зі стороною {length} = {area}")

#6.1

from datetime import datetime

today = datetime.today()
current_year = today.year
new_year = datetime(current_year + 1, 1, 1)

days_left = (new_year - today).days

print(f"До Нового року залишилося {days_left} днів!")

#6.2

from datetime import datetime

birth_date_str = input("Введіть дату народження: ")
birth_date = datetime.strptime(birth_date_str, "%d.%m.%Y")
today = datetime.today()

age = today.year - birth_date.year


if (today.month, today.day) < (birth_date.month, birth_date.day):
    age -= 1

print(f"Вам {age} років.")

#7

import tkinter as tk

def calculate(op):
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        if op == '+':
            result = num1 + num2
        elif op == '-':
            result = num1 - num2
        elif op == '*':
            result = num1 * num2
        elif op == '/':
            result = num1 / num2 if num2 != 0 else "На нуль ділити не можна!"
        label_result.config(text=f"Результат: {result}")
    except ValueError:
        label_result.config(text="Введіть коректні числа")

root = tk.Tk()
root.title("Калькулятор")

entry1 = tk.Entry(root)
entry1.grid(row=0, column=0, columnspan=2)

entry2 = tk.Entry(root)
entry2.grid(row=1, column=0, columnspan=2)

buttons = [
    ('+', 0, 2),
    ('-', 1, 2),
    ('*', 2, 2),
    ('/', 3, 2)
]

for (text, row, col) in buttons:
    btn = tk.Button(root, text=text, width=5, command=lambda op=text: calculate(op))
    btn.grid(row=row, column=col)

label_result = tk.Label(root, text="Результат:")
label_result.grid(row=4, column=0, columnspan=3)

root.mainloop()

#9.1

class Car:
    def __init__(self, brand, model, year, mileage):
        self.brand = brand
        self.model = model
        self.year = year
        self.mileage = mileage

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year}), Пробіг: {self.mileage} км"

class Owner:
    def __init__(self, name):
        self.name = name
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)
        print(f"Додано авто: {car}")

    def show_cars(self):
        if not self.cars:
            print(f"{self.name} не має автомобілів.")
        else:
            print(f"Автомобілі власника {self.name}:")
            for car in self.cars:
                print(f"- {car}")

# Тестування
if __name__ == "__main__":
    owner = Owner("Іван")
    car1 = Car("Toyota", "Camry", 2015, 50000)
    car2 = Car("BMW", "X5", 2018, 30000)

    owner.add_car(car1)
    owner.add_car(car2)
    owner.show_cars()

#9.2

class Teacher:
    def __init__(self, name, subject, experience):
        self.name = name
        self.subject = subject
        self.experience = experience
        self.students = []

    def add_student(self, student_name):
        if student_name not in self.students:
            self.students.append(student_name)
            print(f"Студент {student_name} доданий.")
        else:
            print(f"Студент {student_name} вже є у списку.")

    def remove_student(self, student_name):
        if student_name in self.students:
            self.students.remove(student_name)
            print(f"Студент {student_name} видалений.")
        else:
            print(f"Студента {student_name} немає у списку.")

    def show_students(self):
        if not self.students:
            print("Список студентів порожній.")
        else:
            print("Студенти:")
            for s in self.students:
                print(f"- {s}")

    def info(self):
        return f"Вчитель: {self.name}, Предмет: {self.subject}, Стаж: {self.experience} років"

# Приклад
teacher = Teacher("Олена", "Математика", 10)
print(teacher.info())
teacher.add_student("Петро")
teacher.add_student("Марія")
teacher.show_students()
teacher.remove_student("Петро")
teacher.show_students()