"""
Complete the function that accepts a string parameter, and reverses each word in the string. All spaces in the string should be retained.

Examples
"This is an example!" ==> "sihT si na !elpmaxe"
"double  spaces"      ==> "elbuod  secaps"
"""


def reverse_words(text):
    return ' '.join(text.split(' ')[::-1])[::-1]


some_text = input('Enter some text: ')
print(reverse_words(some_text))
