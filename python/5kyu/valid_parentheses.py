"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.

Examples
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
Constraints
0 <= input.length <= 100

Along with opening (() and closing ()) parenthesis, input may contain any valid ASCII characters.
Furthermore, the input string may be empty and/or not contain any parentheses at all.
Do not treat other forms of brackets as parentheses (e.g. [], {}, <>).
"""


def valid_parentheses(string: str) -> bool:
    # string = list(string)
    # open_br = string.count('(')
    # close_br = string.count(')')
    # if open_br == 0 and close_br == 0:
    #     return True
    # elif open_br != close_br:
    #     return False
    # while open_br > 0:
    #     if string.index('(') < string.index(')'):
    #         string.pop(string.index('('))
    #         string.pop(string.index(')'))
    #         open_br -= 1
    #     else:
    #         return False
    # return True
    counter = 0
    for char in string:
        if char == '(':
            counter += 1
        if char == ')':
            counter -= 1
        if counter < 0:
            return False
    return counter == 0


print(valid_parentheses('  ('))
print(valid_parentheses(')test'))
print(valid_parentheses(''))
print(valid_parentheses(')hi('))
print(valid_parentheses('hi())('))
print(valid_parentheses('hi(hi)()'))
