def todo():
    # повідомлення про початок роботи
    print('To-Do List')

    tasks = []

    # Основний цикл
    while True:
        #  вибирання дії:
        action = input('Choose: "add", "done", "view", "exit": ')


        if action == 'exit':       # Якщо  вибрав "exit", програма завершується
            break

        elif action == 'add':        # Якщо вибрана дія "add", додаємо нову задачу в список
            task = input('Enter task: ')
            tasks.append((task, False))     # Додаємо задачу, позначаючи її як незавершену (False)

        elif action == 'done':     # Якщо вибрана дія "done", помічає задачу як виконану
            try:
                num = int(input('Task number to mark done: '))
                if 0 <= num < len(tasks):

                    tasks[num] = (tasks[num][0], True)      # Якщо номер задачі правильний, позначаємо її як виконану
                    print(f'Task "{tasks[num][0]}" marked as done.')

                else:
                    print('Invalid task number!')

            except (ValueError, IndexError):
                print('Invalid input! Please enter a valid task number.')    # в випадку якщо не зроблено вибір або неправильно введений

        elif action == 'view':     # Якщо вибрана дія "view", вивести список усіх задач
            print('Your tasks:')

            if not tasks:
                print('No tasks added yet!')  # Якщо задач немає

            else:
                # Виведення кожної задачі
                for i, t in enumerate(tasks):
                    print(f'{i}: {t[0]} - {"Done" if t[1] else "Not Done"}')

        else:
            # якщо неправильно вивести повідомлення про помилку
            print('Invalid action! Please choose "add", "done", "view", or "exit".')


# Виклик функції
todo()