number_lines = int(input())
list_1 = []
for _ in range(number_lines):
    input_line = int(input())
    list_1.append(input_line)

command = input()

for index in range(len(list_1) - 1, -1 , -1):
    current_number = list_1[index]
    if command == "even":
        if current_number % 2 != 0 and not current_number == 0:
            list_1.remove(current_number)
    elif command == "odd":
        if current_number % 2 == 0:
            list_1.remove(current_number)
    elif command == "negative":
        if current_number >= 0:
            list_1.remove(current_number)
    elif command == "positive" and not current_number == 0:
        if current_number < 0:
            list_1.remove(current_number)

print(list_1)