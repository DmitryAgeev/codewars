"""
You are going to be given a word. Your job is to return the middle character of the word. If the word's length is odd,
return the middle character. If the word's length is even, return the middle 2 characters.

#Examples:

Kata.getMiddle("test") should return "es"

Kata.getMiddle("testing") should return "t"

Kata.getMiddle("middle") should return "dd"

Kata.getMiddle("A") should return "A"
#Input

A word (string) of length 0 < str < 1000
You do not need to test for this.
This is only here to tell you that you do not need to worry about your solution timing out.

#Output

The middle character(s) of the word represented as a string.
"""


def get_middle(s):
    # return s[len(s) // 2] if len(s) % 2 else s[int(len(s) / 2 - 1)] + s[int(len(s) / 2)]
    index, odd = divmod(len(s), 2)
    return s[index] if odd else s[index - 1:index + 1]


print(get_middle('test'))
print(get_middle('testing'))
