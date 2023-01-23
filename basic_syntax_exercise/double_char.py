while True:
    input_line = input()
    if input_line == "End":
        break
    if input_line == "SoftUni":
        continue
    for a in input_line:
        print(a * 2, end="")
    print()