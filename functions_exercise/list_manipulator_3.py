def exchange_f(x, y):
    y = int(y)
    first_half = x[:y + 1]
    second_half = x[y + 1:]
    result = second_half + first_half
    return result


def max_f(x, y):
    temp_list = []
    if y == "odd":
        for element in x:
            if element % 2 != 0:
                temp_list.append(element)
    elif y == "even":
        for element in x:
            if element % 2 == 0:
                temp_list.append(element)
    if not temp_list:
        return "No matches"
    max_element = max(temp_list)
    index = len(x) - x[::-1].index(max_element) - 1
    return index


def min_f(x, y):
    temp_list = []
    if y == "odd":
        for element in x:
            if element % 2 != 0:
                temp_list.append(element)
    elif y == "even":
        for element in x:
            if element % 2 == 0:
                temp_list.append(element)
    if not temp_list:
        return "No matches"
    min_element = min(temp_list)
    index = len(x) - x[::-1].index(min_element) - 1
    return index


def first_f(x, y, z):
    temp_list = []
    if z == "odd":
        for element in x:
            if element % 2 != 0:
                temp_list.append(element)
    elif z == "even":
        for element in x:
            if element % 2 == 0:
                temp_list.append(element)
    return temp_list[:y]


def last_f(x, y, z):
    temp_list = []
    if z == "odd":
        for element in x:
            if element % 2 != 0:
                temp_list.append(element)
    elif z == "even":
        for element in x:
            if element % 2 == 0:
                temp_list.append(element)
    temp_list = temp_list[::-1]
    return temp_list[:y]


given_list = [int(x) for x in input().split()]
input_line = input()
while not input_line == "end":
    input_line = input_line.split()
    command = input_line[0]
    if command == "exchange":
        if int(input_line[1]) > len(given_list) or int(input_line[1]) < 0:
            print(f"Invalid index")
        else:
            given_list = exchange_f(given_list, input_line[1])
    elif command == "max":
        print(max_f(given_list, input_line[1]))
    elif command == "min":
        print(min_f(given_list, input_line[1]))
    elif command == "first":
        if int(input_line[1]) > len(given_list):
            print(f"Invalid count")
        else:
            print(first_f(given_list, int(input_line[1]), input_line[2]))
    elif command == "last":
        if int(input_line[1]) > len(given_list):
            print(f"Invalid count")
        else:
            print(last_f(given_list, int(input_line[1]), input_line[2]))

    input_line = input()

print(given_list)
print(given_list[::-1])
