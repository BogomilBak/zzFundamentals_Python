input_line = [x for x in input().split(", ")]
positive = [x for x in input_line if int(x) >= 0]
negative = [x for x in input_line if int(x) < 0]
even = [x for x in input_line if int(x) % 2 == 0]
odd = [x for x in input_line if not int(x) % 2 == 0]

print(f"Positive: {', '.join(positive)}")
print(f"Negative: {', '.join(negative)}")
print(f"Even: {', '.join(even)}")
print(f"Odd: {', '.join(odd)}")
