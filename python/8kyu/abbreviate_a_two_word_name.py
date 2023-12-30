"""
Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
"""
from timeit import timeit


def abbrev_name(name: str) -> str:
    first_n, last_n = list(name.upper().split())
    return f'{first_n[0]}.{last_n[0]}.'


def abbrevname(name: str) -> str:
    return '.'.join(w[0] for w in name.split()).upper()


print(abbrev_name('patrick feenan'))
print(abbrevname('patrick feenan'))

print(timeit("abbrev_name('patrick feenan')", globals=globals(), number=10000000))  # 3.8554956000000002
print(timeit("abbrevname('patrick feenan')", globals=globals(), number=10000000))  # 7.040966899999999
