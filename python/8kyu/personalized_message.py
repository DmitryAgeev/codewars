"""
Create a function that gives a personalized greeting.
This function takes two parameters: name and owner.
Use conditionals to return the proper message:

case	            return
name equals owner	'Hello boss'
otherwise	        'Hello guest'
"""


def greet(name, owner):
    if name == owner:
        return 'Hello boss'
    else:
        return 'Hello guest'


user_name, owner_name = input('Enter your name and owner name separated by space: ').split()
print(greet(user_name, owner_name))
