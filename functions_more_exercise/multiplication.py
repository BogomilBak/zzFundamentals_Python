def multiply(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "zero"
    if a < 0:
        if b < 0 and c < 0:
            return "negative"
        elif b < 0 and c > 0:
            return "positive"
        elif b > 0 and c < 0:
            return "positive"
        elif b > 0 and c < 0:
            return "positive"