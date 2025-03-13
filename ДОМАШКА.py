#1

while True:
    try:
        name = input("Введіть ваше ім'я : ")
        if name.lower() == "stop":
            print("Програма завершена.")
            break

        age_input = input("Введіть ваш вік : ")
        if age_input.lower() == "stop":
            print("Програма завершена.")
            break

        age = int(age_input)
        if age < 0 or age > 130:
            raise ValueError("Некоректний вік!")

        print(f"Привіт, {name}! Твій вік — {age}.")
    except ValueError as e:
        print(f"Помилка: {e}")
#2

def greeting(name, age):
    if age < 0 or age > 130:
        raise ValueError("Некоректний вік!")
    return f"Привіт, {name}! Твій вік — {age}."

try:
    name = input("Введіть ваше ім'я: ")
    age = int(input("Введіть ваш вік: "))
    message = greeting(name, age)
    print(message)
except ValueError as e:
    print(f"Помилка: {e}")

#2

def greeting(name, age):
    try:
        if age < 0 or age > 130:
            raise ValueError("Некоректний вік!")
        return f"Привіт, {name}! Твій вік — {age}."
    except ValueError as e:
        return f"Помилка: {e}"

name = input("Введіть ваше ім'я: ")
age = int(input("Введіть ваш вік: "))
print(greeting(name, age))

#3

try:
    numbers = []
    print("Введіть додатні числа :")
    while True:
        user_input = input()
        if user_input.lower() == "stop":
            break
        number = float(user_input)
        if number <= 0:
            raise ValueError("Значення має бути додатним!")
        numbers.append(number)

    print(f"Сума чисел: {sum(numbers)}")
except ValueError as e:
    print(f"Помилка: {e}")

#4

def positive_numbers(numbers):
    for number in numbers:
        if number <= 0:
            raise ValueError("У списку є від'ємне або нульове значення!")
    return sum(numbers)

try:
    numbers = list(map(float, input("Введіть числа через пробіл: ").split()))
    result = positive_numbers(numbers)
    print(f"Сума чисел: {result}")
except ValueError as e:
    print(f"Помилка: {e}")

#4

def positive_numbers(numbers):
    try:
        for number in numbers:
            if number <= 0:
                raise ValueError("У списку є від'ємне або нульове значення!")
        return sum(numbers)
    except ValueError as e:
        return f"Помилка: {e}"

numbers = list(map(float, input("Введіть числа через пробіл: ").split()))
print(positive_numbers(numbers))