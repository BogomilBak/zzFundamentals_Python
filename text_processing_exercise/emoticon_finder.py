input_line = input()

for index in range(len(input_line)):
    if input_line[index] == ":":
        print(f":{input_line[index + 1]}")