input_line = input()

result = ""

for element in input_line:
    current_letter = ord(element) + 3
    result += chr(current_letter)

print(result)