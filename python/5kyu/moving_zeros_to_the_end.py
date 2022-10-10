"""
Write an algorithm that takes an array and moves all of the zeros to the end,
preserving the order of the other elements.

move_zeros([1, 0, 1, 2, 0, 1, 3]) # returns [1, 1, 2, 1, 3, 0, 0]
"""


def move_zeros(lst: list) -> list:
    # new_list = []
    # i = 0
    # for el in lst:
    #     if el:
    #         new_list.append(el)
    #     else:
    #         i += 1
    # while i != 0:
    #     new_list.append(0)
    #     i -= 1
    # return new_list
    b = [el for el in lst if el != 0 or el is False]
    return b + [0] * (len(lst) - len(b))


print(move_zeros([1, 0, 1, 2, 0, 1, 3]))
print(move_zeros([1, 2, 1, 1, 3, 1, 0, 0, 0, 0]))
print(move_zeros([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
print(move_zeros([1, 0, 1, False, 2, 0, 1, 3]))
