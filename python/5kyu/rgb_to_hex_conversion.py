"""
The rgb function is incomplete.
Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned.
Valid decimal values for RGB are 0 - 255.
Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
"""


def rgb(r: int, g: int, b: int) -> str:
    color = []
    for number in (r, g, b):
        number = min(255, max(number, 0))
        color.append(hex(number).upper()[2:].zfill(2))
    return ''.join(color)
    # return ''.join(hex(min(255, max(number, 0)))[2:].zfill(2) for number in (r, g, b)).upper()


print(rgb(0, 0, 0))
print(rgb(1, 2, 3))
print(rgb(255, 255, 255))
print(rgb(254, 253, 252))
print(rgb(-20, 275, 125))
print(rgb(255, 255, 300))
