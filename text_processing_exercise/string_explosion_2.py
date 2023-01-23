input_line = input()

result = ""
strength = 0

while input_line:
    if input_line[0].isnumeric():
        strength = int(input_line[0])
        while strength > 0:
            if input_line[0] == ">":
                result += input_line[0]
                strength += int(input_line[1]) + 1
            input_line = input_line.replace(input_line[0], "", 1)
            strength -= 1

    else:
        result += input_line[0]
        input_line = input_line.replace(input_line[0], "", 1)

print(result)