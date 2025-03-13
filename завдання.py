# books завдання 1
books = ["гаррі поттер", "володар перснів", "маленький принц", "Аліса в країні див"]

book = input(" назва книги: ")

if book in books:
    print(f"Книга {book} є у бібліотеці.")
else:
    print(f"Книга {book} відсутня у бібліотеці.")

# pasword завдання 2
passwords = ["12345", "qwerty", "sekret123", "kate12354%m", "pwd", "vika","nazar"]

for password in passwords:
    if len(password) < 6:
        print(f" password {password} короткий.")
    else:
        print(f"password {password} надійний.")

# завдання 3
operations = [100, -50, -50, 200]

balance = 0

for operation in operations:
    if operation > 0:
        print("Поповнення")
    elif operation < 0:
        print("Витрати")
    print (operation)
    balance += operation
print(f"баланс: {balance}")

#завдання
list_number = [ 65675, 0, 788678,0, 547]


total_expenses = sum(list_number)

zero_expenses_days = list_number.count(0)

days_above_1000 = 0
for i in range(len(list_number)):
    print(f"{i+1} день {list_number[i]} грн")
    if list_number[i] > 1000 :
        days_above_1000 += 1


print(f"\nсума витрат: {total_expenses} грн")
print(f"з 0 витратами: {zero_expenses_days}")
print(f"Кількість днів з витратами більше 1000: {days_above_1000}")