"""
Greed is a dice game played with five six-sided dice.
Your mission, should you choose to accept it, is to score a throw according to these rules.
You will always be given an array with five six-sided dice values.

 Three 1's => 1000 points
 Three 6's =>  600 points
 Three 5's =>  500 points
 Three 4's =>  400 points
 Three 3's =>  300 points
 Three 2's =>  200 points
 One   1   =>  100 points
 One   5   =>   50 point
A single die can only be counted once in each roll.
For example, a given "5" can only count as part of a triplet (contributing to the 500 points)
or as a single 50 points, but not both in the same roll.

Example scoring

 Throw       Score
 ---------   ------------------
 5 1 3 4 1   250:  50 (for the 5) + 2 * 100 (for the 1s)
 1 1 1 3 1   1100: 1000 (for three 1s) + 100 (for the other 1)
 2 4 4 5 4   450:  400 (for three 4s) + 50 (for the 5)
"""
from collections import Counter
from timeit import timeit


def score(dice: list) -> int:
    points = {1: 1000, 6: 600, 5: 500, 4: 400, 3: 300, 2: 200}
    dices = Counter(dice)
    res = 0
    for k, v in dices.items():
        if v >= 3:
            res += points[k] * (v // 3)
        if k == 1:
            res += 100 * (v % 3)
        elif k == 5:
            res += 50 * (v % 3)
    return res


def score_1(dice: list) -> int:
    # clear but slow solution
    d, dice = {1: 1000, 2: 200, 3: 300, 4: 400, 5: 500, 6: 600}, Counter(dice)
    return sum(d[i] * (dice[i] >= 3) for i in range(1, 7)) + 100 * (dice[1] % 3) + 50 * (dice[5] % 3)


print(score([5, 1, 3, 4, 1]))  # 250
print(score([1, 1, 1, 3, 1]))  # 1100
print(score([2, 4, 4, 5, 4]))  # 450

print(timeit("score([2, 4, 4, 5, 4])", globals=globals(), number=1000000))  # 1.5858612
print(timeit("score_1([2, 4, 4, 5, 4])", globals=globals(), number=1000000))  # 2.806869
