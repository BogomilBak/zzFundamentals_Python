import math


def merge(list_1, index, end):
    temp_list = []
    temp_el = ""
    if index > len(list_1) or end < index:
        return list_1

    elif index <= len(list_1) < end:
        for x in range(index):
            temp_list.append(list_1[x])
        for i in range(index, len(list_1)):
            temp_el += list_1[i]
        temp_list.append(temp_el)
        return temp_list

    elif index <= len(list_1) >= end and index == 0:
        for i in range(index, end + 1):
            temp_el += list_1[i]
        temp_list.append(temp_el)
        for z in range(end + 1, len(list_1)):
            temp_list.append(list_1[z])
        return temp_list

    elif index <= len(list_1) >= end and not index == 0:
        for y in range(index):
            temp_list.append(list_1[y])
        for i in range(index, end + 1):
            temp_el += list_1[i]
        temp_list.append(temp_el)
        for z in range(end + 1, len(list_1)):
            temp_list.append(list_1[z])
        return temp_list

    elif end == len(list_1) and index < len(list_1):
        for x in range(index):
            temp_list.append(list_1[x])
        for i in range(index, len(list_1)):
            temp_el += list_1[i]
        temp_list.append(temp_el)
        return temp_list


def divide(list_1, index, partitions):
    temp_list = []
    temp_element = ""
    parts = len(list_1[index]) / partitions
    if parts % 2 == 0:
        for element in list_1[index]:
            temp_element += element
            if len(temp_element) == parts:
                temp_list.append(temp_element)
                temp_element = ""
        value = list_1[index]
        list_1.remove(value)

        for i in range(len(temp_list)):
            value = temp_list[0]
            list_1.insert(index + i, value)
            temp_list.remove(value)
        return list_1

    else:
        parts = math.floor(len(list_1[index]) / partitions)
        remaining = parts
        for element in list_1[index]:
            temp_element += element
            if len(temp_element) >= parts and remaining > 1:
                temp_list.append(temp_element)
                temp_element = ""
                remaining -= 1
        temp_list.append(temp_element)
        value = list_1[index]
        list_1.remove(value)

        for i in range(len(temp_list)):
            value = temp_list[0]
            list_1.insert(index + i, value)
            temp_list.remove(value)

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