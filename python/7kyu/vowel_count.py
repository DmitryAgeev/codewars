"""
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""


def get_count(sentence: str):
    # counter = 0
    # for letter in ('a', 'e', 'i', 'o', 'u'):
    #     counter += list(sentence).count(letter)
    # return counter
    return sum(1 for letter in sentence if letter in "aeiouAEIOU")


some_sentence = input('Enter sentence to count vowels in it: ')
print(get_count(some_sentence))
