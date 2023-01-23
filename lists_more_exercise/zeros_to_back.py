input_line = [int(x) for x in input().split(", ")]

for index in range (len(input_line)):
    if input_line[index] == 0:
        input_line.remove(0)
        input_line.append(0)
        index = index - 1

print(input_line)