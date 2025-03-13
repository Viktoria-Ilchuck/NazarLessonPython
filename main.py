#завдання 1
expression=input("Ведіть число:")
operator = ""
for symbol in "+-*/":
    if symbol in expression:
        operator = symbol
        break
num1, num2 = expression.split(operator)


num1=int(num1)
num2=int(num2)
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
print("Результат:", result)

# завдання 2
import random

list_number = [random.randint(-50, 100) for _ in range(10)]
negative_count = 0
positive_count = 0
zero_count = 0
max_element = max(list_number)
min_element = min(list_number)
for number in list_number:
    if number < 0:

        negative_count += 1
    elif number > 0:
        positive_count += 1
    else:
        zero_count += 1
print("Списак чисел:", list_number)
print("Max-", max_element)
print("Min-", min_element)
print("Кількість від'ємних чисел", negative_count)
print("Кількість додатних чисел", positive_count)
print("Кількість нулів", zero_count)
