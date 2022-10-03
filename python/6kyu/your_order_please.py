"""
Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

Note: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

Examples
"is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
"4of Fo1r pe6ople g3ood th5e the2"  -->  "Fo1r the2 g3ood 4of th5e pe6ople"
""  -->  ""
"""


def order(sentence: str):
    # words = [(int(digit), word) for word in sentence.split() for digit in word if digit.isdigit()]
    # words.sort(key=lambda p: p[0])
    # return ' '.join(p[1] for p in words)

    sentence = sentence.split()
    result = []
    for i in range(len(sentence)):
        for word in sentence:
            if str(i + 1) in word:
                result.append(word)
    return " ".join(result)


print(order('is2 Thi1s T4est 3a'))
print(order('4of Fo1r pe6ople g3ood th5e the2'))
print(order(''))
