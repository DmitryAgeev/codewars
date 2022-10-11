"""
["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"].
You can immediately see that going "NORTH" and immediately "SOUTH" is not reasonable,
better stay to the same place! So the task is to give to the man a simplified version of the plan.
A better plan in this case is simply:

["WEST"]
or
{ "WEST" }
or
[West]
Other examples:
In ["NORTH", "SOUTH", "EAST", "WEST"], the direction "NORTH" + "SOUTH" is going north and coming back right away.

The path becomes ["EAST", "WEST"], now "EAST" and "WEST" annihilate each other,
therefore, the final result is [] (nil in Clojure).

In ["NORTH", "EAST", "WEST", "SOUTH", "WEST", "WEST"],
"NORTH" and "SOUTH" are not directly opposite but they become directly opposite
after the reduction of "EAST" and "WEST" so the whole path is reducible to ["WEST", "WEST"].

Task
Write a function dirReduc which will take an array of strings and returns an array of strings
with the needless directions removed (W<->E or S<->N side by side).
"""


def dirReduc(arr: list) -> list:
    dirs = {'NORTH': 'SOUTH', 'SOUTH': 'NORTH', 'EAST': 'WEST', 'WEST': 'EAST'}
    output = []
    for directory in arr:
        output.pop() if output and output[-1] == dirs[directory] else output.append(directory)
    return output


print(dirReduc(["NORTH", "SOUTH", "SOUTH", "EAST", "WEST", "NORTH", "WEST"]))
print(dirReduc(["NORTH", "WEST", "SOUTH", "EAST"]))
