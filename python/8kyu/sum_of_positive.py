"""
You get an array of numbers, return the sum of all of the positives ones.

Example [1,-4,7,12] => 1 + 7 + 12 = 20

Note: if there is nothing to sum, the sum is default to 0.
"""


def positive_sum(arr: list):
    return sum(x for x in arr if x > 0)


some_array = list(map(float, (input('Enter mathematical operator, and two numbers separated by space: ').split())))
print(positive_sum(some_array))
