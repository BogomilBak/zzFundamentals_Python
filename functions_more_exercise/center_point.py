import math


def gps(a, b, c, d):
    if (abs(a) + abs(b)) < (abs(c) + abs(d)):
        return f"({math.floor(a)}, {math.floor(b)})"
    return f"({math.floor(c)}, {math.floor(d)})"


input_line_1 = float(input())
input_line_2 = float(input())
input_line_3 = float(input())
input_line_4 = float(input())
print(gps(input_line_1, input_line_2, input_line_3, input_line_4))
