"""
Complete the solution so that it returns true if the first argument(string)
passed in ends with the 2nd argument (also a string).

Examples:

solution('abc', 'bc') # returns true
solution('abc', 'd') # returns false
"""


def solution(string: str, ending: str) -> bool:
    return string.endswith(ending)


print(solution('abc', 'bc'))  # returns True
print(solution('abc', 'd'))  # returns False
