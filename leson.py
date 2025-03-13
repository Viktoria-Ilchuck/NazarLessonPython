#ex1
def first_function():
    print("\nDon't let the noise of others' \nopinions drown out your own inner voice.\nSteve Jobs")
first_function()
#ex2
def sub(num1, num2):
    print("In function sub")
    return num1 - num2

def display_odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

display_odd_numbers(6, 45)

#ex3

def line(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        print(f"{symbol}\n" * length)

line(50, "horizontal", "*")
line(50, "vertical", "*")


# ex4
def max_num(num1, num2 , num3 , num4):
    print("\nFunction add with return")
    return max(num1, num2, num3, num4)
print(max_num(13,23,34,45))

#ex5
def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32
print(f"\n перевід у фарангейти - {celsius_to_fahrenheit(25)}")

#ex6
def is_working_hours(hour):
    if 0 <= hour <= 24:
        print("Робоча година")
        return 9 <= hour < 18

    else:
        print("Неробоча")
        return


print(is_working_hours(9))

#ex6
def convert_minutes(minutes):
    if minutes < 0:
        return "Кількість хвилин не може бути від'ємною!"
    hours = minutes // 60
    remaining_minutes = minutes % 60
    return f"{hours} годин {remaining_minutes} хвилин"
print(f"\n перетворює кількість хвилин у години - {convert_minutes(150)}")

#7

def is_lucky_number(number):
    num_str = str(number)

    if len(num_str) == 6:

        sum_first_three = int(num_str[0]) + int(num_str[1]) + int(num_str[2])
        sum_last_three = int(num_str[3]) + int(num_str[4]) + int(num_str[5])

        if sum_first_three == sum_last_three:
            return True
        else:
            return False
    else:
        return False

print(is_lucky_number(123420))
print(is_lucky_number(723422))
print(is_lucky_number(12345))

#ex8

def sum_list(list):
    return sum(list)

print(f"\n сума елементів списку цілих - {sum_list([1, 2, 3, 4, 5])}")


#ex9
def max_list(list):
    if list:
        return max(list)
    else:
        return None

print(f"\n знаходження максимуму - {max_list([-1, -2, -3])}")

