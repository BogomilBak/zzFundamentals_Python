import math


def gps(a, b, c, d, aa, bb, cc, dd):
    if abs(a) + abs(b) + abs(c) + abs(d) > abs(aa) + abs(bb) + abs(cc) + abs(dd):
        if abs(a) + abs(b) <= abs(c) + abs(d):
            return f"({math.floor(a)}, {math.floor(b)})({math.floor(c)}, {math.floor(d)})"
        return f"({math.floor(c)}, {math.floor(d)})({math.floor(a)}, {math.floor(b)})"
    elif abs(a) + abs(b) + abs(c) + abs(d) == abs(aa) + abs(bb) + abs(cc) + abs(dd):
        if abs(a) + abs(b) <= abs(c) + abs(d):
            return f"({math.floor(a)}, {math.floor(b)})({math.floor(c)}, {math.floor(d)})"
        return f"({math.floor(c)}, {math.floor(d)})({math.floor(a)}, {math.floor(b)})"
    elif abs(a) + abs(b) + abs(c) + abs(d) < abs(aa) + abs(bb) + abs(cc) + abs(dd):
        if abs(aa) + abs(bb) <= abs(cc) + abs(dd):
            return f"({math.floor(aa)}, {math.floor(bb)})({math.floor(cc)}, {math.floor(dd)})"
    return f"({math.floor(cc)}, {math.floor(dd)})({math.floor(aa)}, {math.floor(bb)})"


input_line_1 = float(input())
input_line_2 = float(input())
input_line_3 = float(input())
input_line_4 = float(input())
input_line_5 = float(input())
input_line_6 = float(input())
input_line_7 = float(input())
input_line_8 = float(input())
print(gps(input_line_1, input_line_2, input_line_3, input_line_4, input_line_5, input_line_6, input_line_7, input_line_8))

