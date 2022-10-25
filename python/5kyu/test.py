"""
Write a program that will calculate the number of trailing zeros in a factorial of a given number.

N! = 1 * 2 * 3 *  ... * N

Be careful 1000! has 2568 digits...

For more info, see: http://mathworld.wolfram.com/Factorial.html

Examples
zeros(6) = 1
# 6! = 1 * 2 * 3 * 4 * 5 * 6 = 720 --> 1 trailing zero

zeros(12) = 2
# 12! = 479001600 --> 2 trailing zeros
Hint: You're not meant to calculate the factorial. Find another way to find the number of zeros.
"""


def zeros(n: int) -> int:
    zero_counter = 0
    while n > 0:
        n //= 5
        zero_counter += n
    return zero_counter


def zeros_1(n: int) -> int:
    # recursion way
    x = n // 5
    return x + zeros(x) if x else 0


print(zeros(0))  # 0
print(zeros(6))  # 1
print(zeros(30))  # 7
