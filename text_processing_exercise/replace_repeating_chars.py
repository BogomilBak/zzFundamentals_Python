input_line = input()


index = 0
while index < len(input_line) - 1:
    if input_line[index] == input_line[index + 1]:
        letter = f"{input_line[index]}{input_line[index + 1]}"
        input_line = input_line.replace(letter, input_line[index],)
        index = 0
    else:
        index += 1

print(input_line)