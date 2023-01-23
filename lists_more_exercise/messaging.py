numbers = input().split()
input_line = input()
result = []

for index in numbers:
    current_index = index.split()
    counter = 0
    for num in current_index[0]:
        current_number = int(num)
        counter += current_number

    counter = counter % len(input_line)

    result.append(input_line[counter])
    input_line = input_line.replace(input_line[counter], "", 1)
print("".join(result))
