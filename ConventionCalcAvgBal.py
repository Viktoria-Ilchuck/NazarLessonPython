def avg():
    # початок роботи калькулятора для середнього балу
    print('Average Grade Calculator')

    # Ініціалізація порожнього списку для зберігання оцінок
    grades = []

    # Основний цикл для вводу оцінок
    while True:
        # введеня оцінки або stop
        g = input('Enter grade (or "stop" to finish): ')

        # Якщо "stop", цикл завершиться
        if g.lower() == 'stop':
            break

        try:
            # Перетворення введеного значення на число (float)
            grade = float(g)

            # Перевірка, чи знаходиться оцінка в межах від 0 до 100
            if grade < 0 or grade > 100:
                print('Grade must be between 0 and 100. Please try again.')
            else:
                # Додавання оцінки в список
                grades.append(grade)
        except ValueError:
            # Обробка випадку, коли введено неправилне число (некоректне)
            print('Invalid input! Please enter a numeric value.')

    # Якщо в списку є оцінки, обчислюємо середній бал
    if grades:
        average = sum(grades) / len(grades)

        # Виведення середнього балу
        print(f'Average grade: {average:.2f}')

        # Оцінка результату
        if average >= 90:
            print('Excellent')
        elif average >= 75:
            print('Good')
        else:
            print('Needs Improvement')
    else:
        # Якщо оцінок не було введено
        print('No grades entered.')


# Виклик функції для запуску калькулятора
avg()
