"""
Write a function, which takes a non-negative integer (seconds) as input and returns the time
in a human-readable format (HH:MM:SS)

HH = hours, padded to 2 digits, range: 00 - 99
MM = minutes, padded to 2 digits, range: 00 - 59
SS = seconds, padded to 2 digits, range: 00 - 59
The maximum time never exceeds 359999 (99:59:59)

You can find some examples in the test fixtures.
"""


def make_readable(seconds: int) -> str:
    hours = seconds // 3600
    minutes = seconds % 3600 // 60
    rem_seconds = seconds % 3600 % 60
    return f'{hours:02}:{minutes:02}:{rem_seconds:02}'


print(make_readable(0))
print(make_readable(5))
print(make_readable(60))
print(make_readable(86399))
print(make_readable(359999))
