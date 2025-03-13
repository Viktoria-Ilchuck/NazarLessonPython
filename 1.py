# 1
def display():
    print('"Don\'t compare yourself with anyone in this world…\nif you do so, you are insulting yourself."\nBill Gates')

display()

# 2
def sub(num1, num2):
    print("In function sub")
    return num1 - num2

def display_odd_numbers(start, end):
    for num in range(start, end + 1):
        if num % 2 != 0:
            print(num)

display_odd_numbers(6, 45)
# 3
def draw_square(size, symbol, filled):
    if filled:
        for i in range(size):
            print(symbol * size)
    else:
        for i in range(size):
            if i == 0 or i == size - 1:
                print(symbol * size)
            else:
                print(symbol + ' ' * (size - 2) + symbol)

draw_square(4, '*', True)

draw_square(4, '#', False)

# 4
def min_num(num1, num2 , num3 , num4,num5):
    print("\nFunction add with return")
    return min(num1, num2, num3, num4,num5)
print(min_num(13,23,34,45,67))


# 5
def product(start, end):
    if start > end:
        start, end = end, start
    return start, end

print(product(2, 5))
print(product(50, 2))
print(product(23, 30))

#6
def count(number):
    return len(str(abs(number)))  #


print(count(3456))
print(count(37456))  
print(count(345698))
# 7
def is_palindrome(number):
    num_str = str(number)
    if num_str == num_str[::-1]:
        return True
    else:
        return False

print(is_palindrome(123321))
print(is_palindrome(421987))
print(is_palindrome(546645))




