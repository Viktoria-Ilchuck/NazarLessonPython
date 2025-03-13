try:
    age = int(input("Введіть ваш вік: "))
    if 0 <= age <= 100:
        print("Вік коректний.")
    else:
        print("Вік некоректний.")
except ValueError:
    print("Помилка: ")

try:
    amount = float(input(" суму у гривнях: "))
    exchange = float(input("Введіть курс обміну : "))

    if amount < 0 or exchange <= 0:
        print("Сума та курс повинні бути додатніми числами.")
    else:
        amount = amount / exchange
        print(f"{amount} грн за курсом {exchange} дорівнює {amount:.2f} USD")
except ValueError:
    print("Помилка: Введіть числові значення для суми та курсу.")
