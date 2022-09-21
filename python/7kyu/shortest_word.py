"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s: str):
    return min(len(word) for word in s.split())


print(find_short('bitcoin take over the world maybe who knows perhaps'))
print(find_short('turns out random test cases are easier than writing out basic ones'))
