input_line = int(input())

for a in range(97, 97 + input_line):
    for b in range(97, 97 + input_line):
        for c in range(97, 97 + input_line):
            print(f"{chr(a)}{chr(b)}{chr(c)}")
