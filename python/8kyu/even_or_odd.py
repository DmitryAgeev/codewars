"""
Create a function that takes an integer as an argument and returns "Even" for even numbers or "Odd" for odd numbers.
"""


def even_or_odd(number: int):
    return 'Odd' if number % 2 else 'Even'


some_number = int(input('Enter some number: '))
print(even_or_odd(some_number))
