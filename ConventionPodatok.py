def sal():
    # початок роботи калькулятора
    print('Salary Tax Calculator')

    try:
        # вказуємо свою зарплату
        salary = float(input('Enter gross salary: '))

        # Перевірка на негативне значення зарплати
        if salary < 0:
            print('Salary cannot be negative. Please try again.')
            return

        # Визначення ставки податку залежно від величини зарплати
        tax = 0.18 if salary < 20000 else 0.22

        # Обчислення зарплати після вирахування податку
        net_salary = salary - (salary * tax)

        # Виведення результату з двома десятковими знаками
        print(f'Net salary: {net_salary:.2f}')

    # обробка виключень
    except ValueError:
        print('Invalid input! Please enter a numeric value for the salary.')


# Виклик функції для запуску калькулятора
sal()