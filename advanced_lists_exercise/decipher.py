input_line = input().split()
temp_list = []
temp_list_2 = []
for element in input_line:
    if element[2].isdigit():
        digit = (int(element[0]) * 100) + (int(element[1]) * 10) + int(element[2])
        character = chr(digit)
        word = character + element[3:]
        temp_list.append(word)
    elif int(element[1]):
        digit = (int(element[0]) * 10) + int(element[1])
        character = chr(digit)
        word = character + element[2:]
        temp_list.append(word)

for el in temp_list:
    second = el[1]
    last = el[-1]
    if len(el) > 2:
        word = el[0] + last + el[2:-1] + second
        temp_list_2.append(word)
    else:
        word = el[0] + second
        temp_list_2.append(word)
print(' '.join(temp_list_2))
