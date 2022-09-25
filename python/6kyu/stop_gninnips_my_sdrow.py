"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and spaces. Spaces will be included only when more than one word is present.

Examples:

spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


def spin_words(sentence: str):
    # new_sentence = []
    # for word in sentence.split():
    #     if len(word) >= 5:
    #         word = word[::-1]
    #     new_sentence.append(word)
    # return ' '.join(new_sentence)

    return ' '.join(word[::-1] if len(word) >= 5 else word for word in sentence.split())


print(spin_words('Hey fellow warriors'))
print(spin_words('This is a test'))
