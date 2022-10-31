"""
Complete the function scramble(str1, str2)
that returns true if a portion of str1 characters can be rearranged to match str2, otherwise returns false.

Notes:

Only lower case letters will be used (a-z). No punctuation or digits will be included.
Performance needs to be considered.
Examples
scramble('rkqodlw', 'world') ==> True
scramble('cedewaraaossoqqyt', 'codewars') ==> True
scramble('katas', 'steak') ==> False
"""
from collections import Counter


def scramble(s1: str, s2: str) -> bool:
    # too slow solution
    # for c in set(s2):
    #     if s1.count(c) < s2.count(c):
    #         return False
    # return True

    count1, count2 = Counter(s1), Counter(s2)
    return all(count2[char] <= count1[char] for char in count2)


print(scramble('rkqodlw', 'world'))  # True
print(scramble('cedewaraaossoqqyt', 'codewars'))  # True
print(scramble('katas', 'steak'))  # False
