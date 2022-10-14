"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""
from codecs import encode
from timeit import timeit


def rot11(message):
    return encode(message, 'rot_13')


def rot12(message):
    return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
                                               'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))


def rot13(message: str) -> str:
    alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabet_13 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    return ''.join(alfabet_13[alfabet.index(char)] if char.isalpha() else char for char in message)


print(rot13('test'))
print(rot13('Test'))
print(rot13('aA bB zZ 1234 *!?%'))

print('\n')

print(timeit("rot11('test')", globals=globals(), number=1000000))  # 0.4849136999999999
print(timeit("rot12('test')", globals=globals(), number=1000000))  # 1.8275175
print(timeit("rot13('test')", globals=globals(), number=1000000))  # 1.0866005999999997

"""
ANALYSIS
.encode solution is fastest, but not legal for that challenge.
.translate solution is slowest
index solution in the middle
"""
