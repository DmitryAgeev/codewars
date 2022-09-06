"""
This time no story, no theory. The examples below show you how to write function accum:

Examples:
accum("abcd") -> "A-Bb-Ccc-Dddd"
accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
accum("cwAt") -> "C-Ww-Aaa-Tttt"
The parameter of accum is a string which includes only letters from a..z and A..Z.
"""


def accum(s: str):
    # new_s = []
    # for i, letter in enumerate(s, 1):
    #     new_s.append((letter * i).title())
    # return '-'.join(new_s)

    return '-'.join(((letter * i).title()) for i, letter in enumerate(s, 1))


print(accum('abcd'))
