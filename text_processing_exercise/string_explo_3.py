input_line = input()

result = ""
strength = 0

for index in range(len(input_line)):
    if input_line[index] == ">":
        strength += int(input_line[index + 1])
        result += input_line[index]
    elif strength > 0:
        strength -= 1
    else:
        result += input_line[index]

print(result)