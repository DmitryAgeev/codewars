"""
Simple, remove the spaces from the string, then return the resultant string.
"""


def no_space(x: str):
    # return ''.join(x.split())
    return x.replace(' ', '')


print(no_space('8 j 8   mBliB8g  imjB8B8  jl  B'))
print(no_space('8aaaaa dddd r     '))
print(no_space('jfBm  gk lf8hg  88lbe8 '))
