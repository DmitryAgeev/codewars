"""
Implement the function unique_in_order which takes as argument a sequence
and returns a list of items without any elements with the same value next to each other
and preserving the original order of elements.

For example:

unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
unique_in_order([1,2,2,3,3])       == [1,2,3]
"""


def unique_in_order(iterable):
    # new_list = []
    # last = None
    # for i in range(len(iterable)):
    #     if iterable[i] != last:
    #         new_list.append(iterable[i])
    #         last = iterable[i]
    # return new_list
    return [char for i, char in enumerate(iterable) if not i or char != iterable[i - 1]]


print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1, 2, 2, 3, 3]))
print(unique_in_order('A'))
print(unique_in_order('AA'))
print(unique_in_order([]))
print(unique_in_order([None, None, None, 1, 1, 1, 2, 2, 2, 3, 3, 3]))

