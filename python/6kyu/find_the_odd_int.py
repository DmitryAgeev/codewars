"""
Given an array of integers, find the one that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

Examples
[7] should return 7, because it occurs 1 time (which is odd).
[0] should return 0, because it occurs 1 time (which is odd).
[1,1,2] should return 2, because it occurs 1 time (which is odd).
[0,1,0,1,0] should return 0, because it occurs 3 times (which is odd).
[1,2,2,3,3,3,4,3,3,3,2,2,1] should return 4, because it appears 1 time (which is odd).
"""
import operator
from functools import reduce


def find_it(seq: list):
    # reserv = []
    # for el in seq:  # O(n)
    #     if el not in reserv:  # O(n)
    #         if seq.count(el) % 2:
    #             return el

    return reduce(operator.xor, seq)


print(find_it([1, 1, 2]))
print(find_it([0, 1, 0, 1, 0]))
