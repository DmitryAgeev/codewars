"""
You are given an array (which will have a length of at least 3,
but could be very large)containing integers.
The array is either entirely comprised of odd integers or entirely comprised of even integers
except for a single integer N.
Write a method that takes the array as an argument and returns this "outlier" N.

Examples
[2, 4, 0, 100, 4, 11, 2602, 36]
Should return: 11 (the only odd number)

[160, 3, 1719, 19, 11, 13, -21]
Should return: 160 (the only even number)
"""


def find_outlier(integers: list):
    # odds = [number for number in integers if number % 2]
    # evens = [number for number in integers if number % 2 == 0]
    # return odds[0] if len(odds) == 1 else evens[0]

    odds = sum([number & 0x1 for number in integers[:3]])
    evens = 3 - odds

    if evens > odds:
        for i in integers:
            if i & 0x1 != 0:
                return i
    else:
        for i in integers:
            if i & 0x1 == 0:
                return i


print(find_outlier([2, 4, 6, 8, 10, 3]))
print(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]))
print(find_outlier([1, 3, 5, 11, 19, 14, 21]))
print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
