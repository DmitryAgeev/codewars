"""
Given the triangle of consecutive odd numbers:

             1
          3     5
       7     9    11
   13    15    17    19
21    23    25    27    29
...
Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)

1 -->  1
2 --> 3 + 5 = 8
"""


def row_sum_odd_numbers(n: int) -> int:
    # start = n ** 2 - (n - 1)
    # return sum(range(start, start + n * 2, 2))

    # sum of first n rows is 1^2,3^2,6^2,10^2,...T_n^2 for T_n the nth Triangular number
    # T_n = n(n+1)/2
    # need to return T_n^2 - T_(n-1)^2
    # n^2(n+1)^2/4 - n^2(n-1)^2/4
    # n^2/4 * ((n+1)^2 - (n-1)^2)
    # n^2/4 * (2 * 2n)
    # n^3
    return n ** 3


print(row_sum_odd_numbers(1))  # 1
print(row_sum_odd_numbers(2))  # 8
print(row_sum_odd_numbers(13))  # 2197
print(row_sum_odd_numbers(19))  # 6859
print(row_sum_odd_numbers(41))  # 68921
