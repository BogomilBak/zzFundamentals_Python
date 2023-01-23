input_line = int(input())

for number in range(1, input_line + 1):
    number_as_string = str(number)
    result = 0
    for string in number_as_string:
        result += int(string)
    if result == 5 or result == 7 or result == 11:
        print(f"{number} -> True")
    else:
        print(f"{number} -> False")