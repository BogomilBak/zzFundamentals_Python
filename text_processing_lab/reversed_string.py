input_line = input()

while not input_line == "end":
    result = input_line[::-1]
    print(f"{input_line} = {result}")
    input_line = input()