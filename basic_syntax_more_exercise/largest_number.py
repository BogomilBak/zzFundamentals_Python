input_line = input()
current_max = 0
result = ""
while len(input_line) > 0:
    current_max = 0
    for index in range(len(input_line)):
        current_number = int(input_line[index])
        if current_number > current_max:
            current_max = current_number
    input_line = input_line.replace(f"{str(current_max)}", "", 1)
    result += str(current_max)
print(result)
