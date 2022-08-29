"""
Complete the solution so that it reverses the string passed into it.
'world'  =>  'dlrow'
'word'   =>  'drow'
"""


def reversed_strings(string: str):
    return string[::-1]


some_string = input('Enter some text to reverse it: ')
print(reversed_strings(some_string))
