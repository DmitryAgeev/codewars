"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case).

Examples
"the-stealth-warrior" gets converted to "theStealthWarrior"
"The_Stealth_Warrior" gets converted to "TheStealthWarrior"
"""


def to_camel_case(text: str):
    """
    if not len(text):
        return ''
    if '-' in text:
        text = text.replace('-', '_')
    if '_' in text:
        text = text.split('_')
    new_text = [text[0]]
    new_text += [word.capitalize() for word in text[1:]]
    return ''.join(new_text)
    """
    return text[0] + text.title().translate({'_': None, '-': None})[1:] if text else text


print(to_camel_case(''))
print(to_camel_case('the_stealth_warrior'))
print(to_camel_case('The-Stealth-Warrior'))
print(to_camel_case('A-B-C'))
