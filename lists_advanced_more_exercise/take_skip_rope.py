input_line = input()
numbers = []
strings = []
take_list = []
skip_list = []
result = ""
for index in range(len(input_line)):
    if input_line[index].isdigit():
        numbers.append(input_line[index])
    else:
        strings.append(input_line[index])

for index in range(len(numbers)):
    if index % 2 == 0:
        take_list.append(numbers[index])
    else:
        skip_list.append(numbers[index])

rounds = len(take_list)

while rounds > 0:
    current_value = take_list[0]
    for index in range(int(current_value)):
        if strings:
            result += strings.pop(0)

    if strings:
        current_value = skip_list[0]

        for index in range(int(current_value)):
            strings.pop(0)

        take_list.pop(0)
        skip_list.pop(0)

    rounds -= 1

print(result)
