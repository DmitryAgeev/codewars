"""
Write a function that takes an array of numbers and returns the sum of the numbers.
The numbers can be negative or non-integer.
If the array does not contain any numbers then you should return 0.
"""


def sum_array(some_list: list):
    if len(some_list) == 0:
        return 0
    else:
        return sum(some_list)


some_array = list(map(float, input('Enter numbers separated by space: ').split()))
print(sum_array(some_array))
