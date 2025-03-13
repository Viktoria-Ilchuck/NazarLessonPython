def is_palindrome(number):

    num_str = str(number)
    return num_str == num_str[::-1]

print(is_palindrome(123321))
print(is_palindrome(546645))
print(is_palindrome(421987))

