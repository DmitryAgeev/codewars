"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!

find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
It’s guaranteed that array contains at least 3 numbers.

The tests contain some very huge arrays, so think about performance.
"""


def find_uniq(arr: list) -> float:
    # arr.sort()
    # if arr[0] < arr[1] and arr[0] < arr[2]:
    #     res = arr[0]
    # else:
    #     res = arr[-1]
    # return res

    # clever solution
    a, b = set(arr)
    return a if arr.count(a) == 1 else b


print(find_uniq([1, 1, 1, 2, 1, 1]))  # 2
print(find_uniq([0, 0, 0.55, 0, 0]))  # 0.55
print(find_uniq([3, 10, 3, 3, 3]))  # 2
