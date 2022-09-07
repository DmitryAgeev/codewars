"""
An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram. Ignore letter case.

Example: (Input --> Output)

"Dermatoglyphics" --> true
"aba" --> false
"moOse" --> false (ignore letter case)
"""


def is_isogram(string: str):
    """Regular solution"""
    string = string.lower()
    for char in string:
        if string.count(char) > 1:
            return False
    return True
    # Cool solution
    # return len(string) == len(set(string.lower()))


print(is_isogram("Dermatoglyphics"))
print(is_isogram("aba"))
print(is_isogram("moOse"))
