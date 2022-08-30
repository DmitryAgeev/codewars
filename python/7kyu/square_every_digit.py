"""
Welcome. In this kata, you are asked to square every digit of a number and concatenate them.

For example, if we run 9119 through the function, 811181 will come out, because 92 is 81 and 12 is 1.

Note: The function accepts an integer and returns an integer
"""


def square_digits(num):
    concat = ''
    for digit in str(num):
        concat += str(int(digit) ** 2)
    return int(concat)


some_number = input('Enter some number: ')
print(square_digits(some_number))
