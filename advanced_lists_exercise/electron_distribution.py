input_line = int(input())
result = []
counter = 1
while input_line > 0:
    maximum = int(2 * counter ** 2)
    if input_line >= maximum:
        result.append(maximum)
        input_line -= maximum
    else:
        result.append(int(input_line))
        input_line = 0
    counter += 1
print(result)
