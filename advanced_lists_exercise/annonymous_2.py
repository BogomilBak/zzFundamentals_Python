def merge(list_1, index, end):

    if index < 0:
        index = 0
    if end > len(list_1) - 1:
        end = len(list_1) - 1

    for index_1, string in enumerate(list_1):
        if index_1 in range(index + 1, end + 1):
            list_1[index] += list_1[index_1]
    for index_1 in range(end, index, -1):
        list_1.pop(index_1)

    return list_1


def divide(list_1, index, partitions):
    if partitions > len(list_1[index]):
        step = 1
    else:
        step = len(list_1[index]) // partitions
    start = 0

    for parts in range(partitions):
        if parts == partitions - 1:
            list_1.insert(index, parts[start::])
            break
        else:
            list_1.insert(index, parts[start: start + step:])
        start += step
        index += 1

    return list_1


input_line = input().split()
result = []
command = input()
while not command == "3:1":
    command = command.split()
    if command[0] == "merge":
        input_line = merge(input_line, int(command[1]), int(command[2]))
    elif command[0] == "divide":
        input_line = divide(input_line, int(command[1]), int(command[2]))
    command = input()

print(' '.join(input_line))