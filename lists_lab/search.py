number_lines = int(input())
special_string = input()
list_1 = []
for i in range(number_lines):
    input_line = input()
    list_1.append(input_line)

print(list_1)
for i in range(len(list_1) - 1, -1 , -1):
    element = list_1[i]
    if special_string not in element:
        list_1.remove(element)

print(list_1)