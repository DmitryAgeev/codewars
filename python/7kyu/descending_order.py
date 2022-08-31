"""
Your task is to make a function that can take any non-negative integer as an argument and return it with its digits in descending order. Essentially, rearrange the digits to create the highest possible number.

Examples:
Input: 42145 Output: 54421

Input: 145263 Output: 654321

Input: 123456789 Output: 987654321
"""


def descending_order(num):
    # don't know about sorted function
    # i = 0
    # new_num = []
    # num = [int(digit) for digit in str(num)]
    #
    # for i in range(len(num)):
    #     new_num.append(max(num))
    #     num.remove(max(num))
    #     i += 1
    # return int(''.join(str(d) for d in new_num))
    return int("".join(sorted(str(num), reverse=True)))


some_number = int(input('Enter some positive integer: '))
print(descending_order(some_number))
