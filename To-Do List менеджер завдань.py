from datetime import datetime

class Task:
    def __init__(self, title, description, deadline):
        self.title = title
        self.description = description
        self.deadline = deadline
        self.done = False

    def mark_done(self):
        """Позначити завдання як виконане."""
        self.done = True

    def __str__(self):
        status = "Виконано" if self.done else "Не виконано"
        return f"{self.title} - {self.description} (Термін: {self.deadline}) - {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description, deadline):
        """Додає завдання, якщо таке з тією ж назвою ще не існує."""
        if any(task.title.strip().lower() == title.strip().lower() for task in self.tasks):
            raise ValueError("Завдання з такою назвою вже існує.")

        try:
            deadline_date = datetime.strptime(deadline, "%Y-%m-%d")
            task = Task(title, description, deadline_date)
            self.tasks.append(task)
            print(f"Завдання '{title}' додано.")
        except ValueError:
            print("Невірний формат дати! Використовуйте формат: Рік-місяць-день (наприклад, 2025-03-04).")

    def mark_done(self, title):
        """Позначити завдання як виконане."""
        for task in self.tasks:
            print(f"Перевірка: '{task.title.strip().lower()}' == '{title.strip().lower()}'")  # Для налагодження
            if task.title.strip().lower() == title.strip().lower():
                task.mark_done()
                print(f"Завдання '{title}' позначене як виконане.")
                return
        print(f"Завдання з назвою '{title}' не знайдено.")

    def remove_task(self, title):
        """Видалити завдання за назвою."""
        task_to_remove = None
        for task in self.tasks:
            print(f"Перевірка: '{task.title.strip().lower()}' == '{title.strip().lower()}'")  # Для налагодження
            if task.title.strip().lower() == title.strip().lower():
                task_to_remove = task
                break

        if task_to_remove:
            self.tasks.remove(task_to_remove)
            print(f"Завдання '{title}' видалено.")
        else:
            print(f"Завдання з назвою '{title}' не знайдено.")

    def show_active_tasks(self):
        """Показати всі активні (не виконані) завдання."""
        print("\nАктивні завдання:")
        active_tasks = [task for task in self.tasks if not task.done]
        if not active_tasks:
            print("Немає активних завдань.")
        else:
            for task in active_tasks:
                print(task)

    def show_done_tasks(self):
        """Показати всі виконані завдання."""
        print("\nВиконані завдання:")
        done_tasks = [task for task in self.tasks if task.done]
        if not done_tasks:
            print("Немає виконаних завдань.")
        else:
            for task in done_tasks:
                print(task)


def main():
    manager = TaskManager()

    while True:
        print("\n1. Додати завдання")
        print("2. Позначити завдання як виконане")
        print("3. Видалити завдання")
        print("4. Показати активні завдання")
        print("5. Показати виконані завдання")
        print("6. Вийти")

        try:
            choice = int(input("Оберіть дію: "))

            if choice == 1:
                title = input("Введіть назву завдання: ").strip()
                description = input("Введіть опис завдання: ").strip()
                deadline = input("Введіть термін виконання (Рік-місяць-день): ").strip()
                try:
                    manager.add_task(title, description, deadline)
                except ValueError as e:
                    print(e)

            elif choice == 2:
                title = input("Введіть назву завдання, яке хочете позначити як виконане: ").strip()
                manager.mark_done(title)

            elif choice == 3:
                title = input("Введіть назву завдання для видалення: ").strip()
                manager.remove_task(title)

            elif choice == 4:
                manager.show_active_tasks()

            elif choice == 5:
                manager.show_done_tasks()

            elif choice == 6:
                print("До побачення!")
                break

            else:
                print("Невірний вибір. Спробуйте ще раз.")

        except ValueError:
            print("Будь ласка, введіть правильне число.")

if __name__ == "__main__":
    main()