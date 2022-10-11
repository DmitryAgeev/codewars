"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.

Examples
pig_it('Pig latin is cool') # igPay atinlay siay oolcay
pig_it('Hello world !')     # elloHay orldway !
"""


def pig_it(text: str) -> str:
    # new_text = []
    # for word in text.split():
    #     print(f"{word[1:]}{word[0]}ay")
    return ' '.join(f"{word[1:]}{word[0]}ay" if word.isalpha() else word for word in text.split())


print(pig_it('Pig latin is cool'))
print(pig_it('Hello world !'))
print(pig_it('This is my string'))
