"""
ROT13 is a simple letter substitution cipher that replaces a letter with the letter 13 letters
after it in the alphabet. ROT13 is an example of the Caesar cipher.

Create a function that takes a string and returns the string ciphered with Rot13.
If there are numbers or special characters included in the string, they should be returned as they are.
Only letters from the latin/english alphabet should be shifted, like in the original Rot13 "implementation".

Please note that using encode is considered cheating.
"""


# import codecs
#
#
# def rot13(message):
#     return codecs.encode(message, 'rot_13')


# def rot13(message):
#     return message.translate(message.maketrans('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz',
#                                                'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'))


def rot13(message: str) -> str:
    alfabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    alfabet_13 = 'nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM'
    return ''.join(alfabet_13[alfabet.index(char)] if char.isalpha() else char for char in message)


print(rot13('test'))
print(rot13('Test'))
print(rot13('aA bB zZ 1234 *!?%'))
