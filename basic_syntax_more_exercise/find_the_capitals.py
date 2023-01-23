input_line = input()
result = []
counter = 0
for index in input_line:

    if 65 <= ord(index) <= 90:
        result.append(input_line.index(index))
        input_line = input_line.replace(f"{index}", "a", 1)
    counter += 1
print(result)