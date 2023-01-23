def increasing(list_1, value_1):
    list_1 = [(x + value_1) if x <= value_1 else (x - value_1) for x in list_1]
    return list_1


input_line = list(map(int, input().split()))
result = 0

while input_line:
    command = int(input())
    if command > len(input_line) - 1:
        command = len(input_line) - 1
        value = input_line[-1]
        result += value
        input_line[-1] = input_line[0]
        input_line = increasing(input_line, value)

    elif command < 0:
        command = 0
        value = input_line[0]
        result += value
        input_line[0] = input_line[-1]
        input_line = increasing(input_line, value)
    else:
        value = input_line[command]
        input_line.pop(command)
        result += value
        input_line = increasing(input_line, value)

print(result)

