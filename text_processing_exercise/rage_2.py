input_line = input()

index = 0
current_letters = ""
result = ""
while index < len(input_line):
    if not input_line[index].isdigit():
        current_letters += input_line[index]
        index += 1
    else:
        current_number = ""
        while index < len(input_line) and input_line[index].isdigit():
            current_number += input_line[index]
            index += 1

        current_number = int(current_number)

        result += current_letters.upper() * current_number
        current_letters = ""

print(f"Unique symbols used: {len(set(result))}")
print(result)

